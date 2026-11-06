import os
import copy
import json
import platform
import re
import sys
import time
import subprocess
import shutil
import urllib.error
import urllib.request
from urllib.parse import urlparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Literal

from utils import *


@dataclass
class APIConfig:
    base_url: str
    api_key: str
    model: str


StageStatus = Literal["running", "complete", "skip", "error"]


class DependencyInstallFailed(RuntimeError):
    """`npm install` failed; not worth retrying within the same deploy stage."""


def _env_number(name: str, default: Any, cast: type = float) -> Any:
    """Read a numeric env override; a typo must not break importing this module."""
    raw = os.environ.get(name)
    if raw is None or not str(raw).strip():
        return default

    try:
        return cast(raw)
    except (TypeError, ValueError):
        print_red(f"Ignoring non-numeric {name}={raw!r}; using {default}")
        return default


# Hosts that count as "this machine". `0.0.0.0` and `::` are listen wildcards, but
# a caller may still put them in a URL, and they never mean a page on the internet.
LOCAL_HOSTS = frozenset({
    "localhost", "127.0.0.1", "::1", "0.0.0.0", "::", "host.docker.internal",
})


def is_local_url(url: str) -> bool:
    """True when `url` addresses this machine, i.e. a dev server has to be running for it."""
    host = (urlparse(url).hostname or "").lower()
    return host in LOCAL_HOSTS or host.startswith("127.")


class BaseAgent:
    # A cold Vite start pre-bundles its dependencies before it binds its port, which
    # is slow. The budget is generous and overridable instead of a hardcoded 80s.
    SERVER_TIMEOUT: float = _env_number("WEBTESTBENCH_SERVER_TIMEOUT", 300.0)
    SERVER_POLL: float = 0.5
    SERVER_PROGRESS_INTERVAL: float = 15.0
    SERVER_DEPLOY_ATTEMPTS: int = _env_number("WEBTESTBENCH_SERVER_ATTEMPTS", 3, int)
    SERVER_RETRY_DELAY_S: float = _env_number("WEBTESTBENCH_SERVER_RETRY_DELAY", 30.0)
    # Wall-clock cap for the whole deploy stage, so a hopeless app cannot cost
    # attempts x budget.
    SERVER_TOTAL_BUDGET_S: float = _env_number("WEBTESTBENCH_DEPLOY_BUDGET", 900.0)

    BIND_HOST: str = os.environ.get("WEBTESTBENCH_BIND_HOST", "0.0.0.0").strip() or "0.0.0.0"
    CONNECT_HOST: str = os.environ.get("WEBTESTBENCH_CONNECT_HOST", "localhost").strip() or "localhost"

    def __init__(
        self,
        instruction: str,
        api_config: APIConfig,
        output_dir: str | Path,
        server_url: str,
        # None is legitimate: server_deploy treats it as "no local app" (online URL).
        local_project_dir: Optional[str | Path],
        event_log_stream: Optional[Any] = None,
    ) -> None:
        self.instruction = instruction
        self.api_config = api_config
        self.server_url = server_url
        self.local_project_dir = local_project_dir

        self.event_log_stream = event_log_stream

        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.current_stage: Optional[str] = None

        self.checklist_path = self.output_dir / "checklist.md"
        self.result_path = self.output_dir / "result.md"
        self.result_extracted_path = self.output_dir / "result_extracted.md"
        self.session_meta_path = self.output_dir / "session_meta.json"

        self.dev_server_process: Optional[subprocess.Popen] = None
        self._dev_server_log_handle: Optional[Any] = None
    
    async def extract_result_file(self) -> bool:
        stage = "result_extract"
        self.current_stage = stage

        if self._should_skip_stage(self.result_extracted_path, stage):
            return True

        self._write_stage_success(stage, True)
        try:
            content = self._load_file_content(self.result_path)
        except Exception as exc:
            self._mark_stage(stage=stage, status="error", message=f"Failed to read result.md: {exc}")
            return False

        extracted = self._extract_test_result_section(content)
        if extracted is None or extracted.strip() == "":
            if self.result_path.exists():
                timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
                # result 
                error_path = self.result_path.with_name(f"result-error_{timestamp}.md")
                self.result_path.rename(error_path)
                # session
                session_error_path = self.session_meta_path.with_name(f"session_meta-error_{timestamp}.json")
                shutil.copy2(self.session_meta_path, session_error_path)
            self._mark_stage(stage=stage, status="error", message="Missing '# Test Result' section.")
            return False

        self.result_extracted_path.write_text(extracted, encoding="utf-8")
        if self._verify_output_file(self.result_extracted_path):
            self._emit_file_event(stage, self.result_extracted_path)
            return True
        else:
            self._mark_stage(stage=stage, status="error", message=f"Stage {stage} did not produce {self.result_extracted_path}.")
            return False

    def _extract_test_result_section(self, content: str) -> str:
        lines = content.splitlines()
        start_idx = None
        for i, line in enumerate(lines):
            if line.strip().startswith("# Test Result"):
                start_idx = i
                break
        if start_idx is None:
            return ""

        extracted_lines = lines[start_idx:]
        last_item_idx = None
        for i, line in enumerate(extracted_lines):
            if line.lstrip().startswith("- [") and "]" in line:
                last_item_idx = i

        if last_item_idx is None:
            trimmed = "\n".join(extracted_lines).strip()
            return f"{trimmed}\n" if trimmed else ""

        end_idx = last_item_idx + 1
        while end_idx < len(extracted_lines):
            line = extracted_lines[end_idx]
            if line.strip() == "" or line[0].isspace():
                end_idx += 1
                continue
            break

        trimmed = "\n".join(extracted_lines[:end_idx]).strip()
        return f"{trimmed}\n" if trimmed else ""

    # ------------------------------------------------------------------ #
    # Server Deployment
    # ------------------------------------------------------------------ #

    async def server_deploy(self):
        """
        Ensure project dev server is up.

        Rules:
        - Kill previous dev server on port 5173.
        - If `dev_server.log` already exists and curl succeeds, we skip.
        - Otherwise install deps and run dev server in background.
        """
        stage = "server_deploy"
        if not is_local_url(self.server_url):
            self._mark_stage(stage=stage, status="skip", message=f"⏭️ Skipping {stage}: server_url is an online webpage, skipping server deployment: {self.server_url}")
            return True

        if not self.local_project_dir:
            self._mark_stage(stage=stage, status="error", message=f"{stage}: local_project_dir is not set.")
            return False
        
        self._mark_stage(stage=stage, status="running", message="🚀 Starting Server Deployment ...")
        
        # Extract port from server_url
        parsed_url = urlparse(self.server_url)
        port = parsed_url.port

        if port is None or not (1024 <= port <= 65535):
            self._mark_stage(
                stage=stage, status="error",
                message=f"{stage}: {self.server_url} has no usable port ({port}); cannot start a dev server",
            )
            return False

        self._kill_exist_port(port)
        self._deploy_with_retry(port, stage=stage)

        return True

    def _deploy_with_retry(self, port: int, stage: str = "server_deploy") -> None:
        """
        Deploy the dev server, with retry on failure.
        Waiting for the burst to pass and retrying is cheaper than losing the record.
        """
        attempts = max(1, self.SERVER_DEPLOY_ATTEMPTS)
        started = time.time()

        for attempt in range(1, attempts + 1):
            final_attempt = attempt >= attempts
            try:
                self._deploy_local_server(port, stage=stage, final_attempt=final_attempt)
                # Intermediate attempts report status "running", but be explicit: a
                # retried deploy that did start must not stay recorded as failed.
                self._write_stage_success(stage, True, force=True)
                return

            except (DependencyInstallFailed, FileNotFoundError):
                raise  # deterministic: another attempt cannot change the outcome

            except Exception as exc:
                if final_attempt:
                    raise

                elapsed = time.time() - started
                if elapsed + self.SERVER_RETRY_DELAY_S > self.SERVER_TOTAL_BUDGET_S:
                    raise RuntimeError(
                        f"{exc} (deploy budget {self.SERVER_TOTAL_BUDGET_S:.0f}s exhausted after {elapsed:.0f}s)"
                    ) from exc

                delay = self.SERVER_RETRY_DELAY_S
                self._emit_event(
                    type_name="server_retry", stage=stage, status="running",
                    message=f"dev server attempt {attempt}/{attempts} failed ({type(exc).__name__}); retrying in {delay:.0f}s",
                    payload=dict(
                        attempt=attempt, attempts=attempts, delay_s=delay, error=str(exc),
                    ),
                )
                self._stop_dev_server_process()
                self._kill_exist_port(port, stage=stage)
                time.sleep(delay)

        raise RuntimeError(f"dev server for port {port} could not be deployed")  # unreachable

    def _kill_exist_port(self, port: int, stage: str = "server_deploy") -> None:
        """Kill old dev server process on the given port if it exist."""
        self._mark_stage(stage=stage, message=f"🧹 Checking old dev server on port {port} ...")
        try:
            # Kill the process running on the extracted port
            result = subprocess.run(
                f"lsof -ti:{port} | xargs kill -9",
                shell=True, capture_output=True, text=True,
            )
            if result.returncode == 0:
                self._mark_stage(stage=stage, message=f"🧹 Killed process on port {port}.")
            else:
                self._mark_stage(stage=stage, message=f"✅ No process found on port {port}.")
                pass  # It's okay if nothing was running on the port
        except Exception as e:
            # Best effort: cleanup must never fail a stage that then succeeds.
            self._mark_stage(stage=stage, message=f"⚠️ Could not inspect port {port}: {e}")

        # A Vite server only binds its port after pre-bundling its deps, so it is
        # invisible to the lookup above while it keeps a core (and later the port)
        # busy. Sweep by command line as well; `[ ]` keeps the pattern from matching
        # its own command line and the port makes it specific to this record.
        try:
            sweep = subprocess.run(
                ["pkill", "-9", "-f", f"vite[ ]--port[ ]{port}"],
                capture_output=True, text=True,
            )
        except FileNotFoundError:
            return  # pkill not installed: the port lookup above is all we can do
        except Exception as e:
            self._mark_stage(stage=stage, message=f"⚠️ Command-line sweep skipped: {e}")
            return

        if sweep.returncode == 0:
            self._mark_stage(stage=stage, message=f"🧹 Killed stale dev server still starting up for port {port}.")
    
    def _deploy_local_server(self, port: int, stage: str = "server_deploy", final_attempt: bool = True):
        """Start dev server in background on the given port and wait until it responds."""
        if not self.local_project_dir:
            raise FileNotFoundError("local_project_dir is not set; cannot deploy a dev server")

        project_dir = Path(self.local_project_dir)
        if not project_dir.exists():
            raise FileNotFoundError(f"local_project_dir not found: {project_dir}")
        
        self._check_disk_space(project_dir, stage=stage)
        self._install_dependencies(project_dir, stage=stage)

        # session_meta.json only ever ANDs stage_success, so an intermediate attempt
        # reports "running": the retry that succeeds must leave the stage successful.
        failure_status: StageStatus = "error" if final_attempt else "running"

        log_path = self.output_dir / "dev_server.log"
        cmd = self._dev_server_command(project_dir, port)
        self._mark_stage(stage=stage, message=f"🚀 Starting dev server on port {port} (log: {log_path}) ...")

        self._dev_server_log_handle = open(log_path, "w", encoding="utf-8")
        self.dev_server_process = subprocess.Popen(
            cmd, cwd=str(project_dir),
            stdout=self._dev_server_log_handle, stderr=subprocess.STDOUT, preexec_fn=os.setsid,
        )

        # step 3: wait for server to respond
        wait_s = self.SERVER_TIMEOUT
        probe_urls = [self.server_url]
        for extra in (f"http://127.0.0.1:{port}/", f"http://[::1]:{port}/"):
            if extra not in probe_urls:
                probe_urls.append(extra)

        print("⏳ Waiting for server to start...")
        self._emit_event(
            type_name="server_wait", stage=stage, status="running",
            message=f"waiting up to {wait_s:.0f}s for {self.server_url}",
            payload=dict(
                url=self.server_url, log=str(log_path), timeout_s=wait_s,
                command=" ".join(cmd), probe_urls=list(probe_urls),
            ),
        )
        started = time.time()
        next_progress = started + self.SERVER_PROGRESS_INTERVAL

        while True:
            # Fail fast when the dev server already died (bad config, port taken with
            # --strictPort, missing script); waiting the full budget hides that.
            exit_code = self.dev_server_process.poll()
            if exit_code is not None:
                tail = self._tail_file(log_path)
                self._stop_dev_server_process()
                self._emit_event(
                    type_name="server_exit", stage=stage, status=failure_status,
                    message=f"dev server exited before listening (exit {exit_code})",
                    payload=dict(
                        url=self.server_url, exit_code=exit_code, command=" ".join(cmd),
                        dev_server_log_tail=tail,
                    ),
                )
                raise RuntimeError(
                    f"Dev server exited (exit {exit_code}) before answering on {self.server_url}. "
                    f"See log: {log_path}"
                )

            for probe_url in probe_urls:
                if self._probe_url(probe_url):
                    elapsed = round(time.time() - started, 1)
                    self._mark_stage(stage=stage, status="complete", message=f"✅ Server is ready at {self.server_url} ({elapsed}s)")
                    self._mark_stage(stage=stage, message=f"✅ Dev server started (PID: {self.dev_server_process.pid})")
                    return True

            elapsed = time.time() - started
            if elapsed >= wait_s:
                break
            if time.time() >= next_progress:
                next_progress = time.time() + self.SERVER_PROGRESS_INTERVAL
                last_line = (self._tail_file(log_path, limit=1) or "<no output>").strip()
                self._mark_stage(
                    stage=stage,
                    message=f"⏳ still waiting for {self.server_url} ({elapsed:.0f}s/{wait_s:.0f}s, last log line: {last_line})",
                )
            time.sleep(self.SERVER_POLL)

        tail = self._tail_file(log_path)
        elapsed = round(time.time() - started, 1)
        self._stop_dev_server_process()

        self._emit_event(
            type_name="server_timeout", stage=stage, status=failure_status,
            message=f"dev server did not answer within {wait_s:.0f}s",
            payload=dict(
                url=self.server_url, seconds=elapsed, command=" ".join(cmd),
                expected_port=port, log_reported_port=self._log_reported_port(log_path),
                hint=self._deploy_timeout_hint(log_path, port),
                dev_server_log_tail=tail
            ),
        )
        raise RuntimeError(
            f"Dev server failed to start within {wait_s:.0f}s ({elapsed}s). "
            f"{self._deploy_timeout_hint(log_path, port)} See log: {log_path}"
        )

    def _dev_server_command(self, project_dir: Path, port: int) -> list:
        """`npm run dev` plus the port flag, with Vite-only extras when applicable.

        `--strictPort` makes Vite fail instead of silently shifting to another port,
        which would leave the pipeline polling a URL nothing listens on. `--host`
        only widens the bind address; clients still connect through CONNECT_HOST.
        """
        cmd = ["npm", "run", "dev", "--", "--port", str(port)]
        if "vite" in self._dev_script(project_dir).lower():
            cmd.extend(["--strictPort", "--host", self.BIND_HOST])

        return cmd

    @staticmethod
    def _dev_script(project_dir: Path) -> str:
        """`scripts.dev` from package.json, or '' when it cannot be read."""
        try:
            package = json.loads((project_dir / "package.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return ""

        return str((package.get("scripts") or {}).get("dev", "") or "")

    @staticmethod
    def _probe_url(url: str, timeout: float = 1.5) -> bool:
        """True when something answers HTTP on `url`; any status code counts.

        Proxies are bypassed so an http_proxy env var cannot turn a local readiness
        probe into a misleading failure.
        """
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        try:
            with opener.open(url, timeout=timeout):
                return True
        except urllib.error.HTTPError:
            return True
        except Exception:
            return False

    @staticmethod
    def _log_reported_port(path: Path) -> Optional[int]:
        """Last `localhost:<port>` port printed by the dev server, if any."""
        try:
            text = Path(path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            return None

        ports = re.findall(r"localhost:(\d{2,5})", text)
        return int(ports[-1]) if ports else None

    def _deploy_timeout_hint(self, log_path: Path, port: int) -> str:
        """Actionable one-liner explaining the most likely cause of a timeout."""
        reported = self._log_reported_port(log_path)
        if reported is not None and reported != port:
            return f"Dev server is listening on port {reported}, not {port}; align server_url with the chosen port."

        if "Re-optimizing dependencies" in self._tail_file(log_path, limit=200):
            return (
                "Vite was still pre-bundling dependencies (slow on /mnt/c under WSL2); "
                "raise WEBTESTBENCH_SERVER_TIMEOUT or delete node_modules/.vite to re-warm it."
            )

        return "Check dev_server.log for build errors or a port conflict."

    def _stop_dev_server_process(self) -> None:
        """Kill the spawned dev server process group and close its log handle.

        A port-only kill misses a server that is still pre-bundling deps and not
        listening yet, which leaves an orphan competing with the next run.
        """
        self._kill_process_group(self.dev_server_process)
        self.dev_server_process = None

        handle = self._dev_server_log_handle
        if handle is not None:
            try:
                handle.close()
            except Exception:
                pass
        self._dev_server_log_handle = None

    @staticmethod
    def _kill_process_group(proc: Optional[subprocess.Popen]) -> None:
        """Best-effort kill of a Popen started with `preexec_fn=os.setsid`.

        The process group id equals the pid, so a negative target also takes down
        the npm/vite/esbuild children instead of only the shell we spawned.
        """
        if proc is None or proc.poll() is not None:
            return

        try:
            subprocess.run(f"kill -9 -{proc.pid}", shell=True, capture_output=True)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass

        try:
            proc.wait(timeout=10)
        except Exception:
            pass

    # ------------------------------------------------------------------ #
    # Deployment diagnostics
    # ------------------------------------------------------------------ #

    @staticmethod
    def _tail_file(path: Path, limit: int = 25) -> str:
        """Last `limit` lines of a log file, or '' when unreadable."""
        try:
            text = Path(path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            return ""
        return "\n".join(text.splitlines()[-limit:])

    def _check_disk_space(self, path: Path, stage: str, need_gb: float = 3.0) -> None:
        """Report free space before npm writes ~500 MB; loud when it is about to fail."""
        try:
            usage = shutil.disk_usage(str(path))
        except OSError as exc:
            self._emit_event(
                type_name="disk_space", stage=stage, status="error",
                message=f"unable to read disk usage for {path}: {exc}"
            )
            return

        free_gb = round(usage.free / 1e9, 2)
        payload = dict(path=str(path), free_gb=free_gb, total_gb=round(usage.total / 1e9, 2))
        if free_gb < need_gb:
            # status stays "running": _emit_event(status="error") latches the stage
            # as failed in session_meta.json, and npm may still succeed.
            payload["warning"] = True
            self._emit_event(
                type_name="disk_space", stage=stage, status="running",
                message=f"⚠️ only {free_gb} GB free on {path} - npm install needs ~{need_gb:.0f} GB and may hang",
                payload=payload,
            )
        else:
            self._emit_event(
                type_name="disk_space", stage=stage, status="running",
                message=f"{free_gb} GB free on {path}", payload=payload
            )

    def _install_dependencies(self, project_dir: Path, stage: str) -> None:
        """Run `npm install` and record its output, so ENOSPC/network errors are in the log."""
        self._mark_stage(stage=stage, message=f"📦 Installing dependencies (npm install) in {project_dir} ...")
        started = time.time()
        result = subprocess.run(
            ["npm", "install"], cwd=str(project_dir),
            capture_output=True, text=True, errors="replace",
        )

        seconds = round(time.time() - started, 1)
        combined = (result.stdout or "") + (result.stderr or "")
        tail = "\n".join(combined.strip().splitlines()[-25:])
        payload = dict(
            cmd="npm install", cwd=str(project_dir),
            seconds=seconds, exit_code=result.returncode,
            output_tail=tail
        )

        if result.returncode != 0:
            self._emit_event(
                type_name="dependency_install", stage=stage, status="error",
                message=f"npm install failed (exit {result.returncode}) after {seconds}s",
                payload=payload,
            )
            raise DependencyInstallFailed(
                f"npm install failed in {project_dir} (exit {result.returncode}): {tail[-400:]}"
            )

        self._emit_event(
            type_name="dependency_install", stage=stage, status="complete",
            message=f"npm install finished in {seconds}s", payload=payload,
        )

    def kill_local_server(self) -> None:
        """Cleanup for local dev server."""
        self._stop_dev_server_process()
        if not is_local_url(self.server_url):
            return

        port = urlparse(self.server_url).port
        if port is None:
            return

        self._kill_exist_port(port, stage="server_cleanup")

    # ------------------------------------------------------------------ #
    # Helpers
    # ------------------------------------------------------------------ #

    _ENVIRONMENT: Optional[dict] = None

    @classmethod
    def _environment_info(cls) -> dict:
        """Tool versions, probed once per process (`--version` is not free)."""
        if cls._ENVIRONMENT is None:
            info: Dict[str, Any] = {
                "python": platform.python_version(),
                "platform": platform.platform(),
            }
            for tool in ("node", "npm", "claude"):
                try:
                    proc = subprocess.run([tool, "--version"], capture_output=True, text=True, timeout=10)
                    text = (proc.stdout or proc.stderr or "").strip()
                    info[tool] = text.splitlines()[0] if text else "unknown"
                except Exception:
                    info[tool] = "missing"
            cls._ENVIRONMENT = info
        return dict(cls._ENVIRONMENT)

    def _log_instruction(self) -> None:
        """Persist and display the input instruction for traceability."""
        print("=" * 20, "Instruction", "=" * 20)
        print(self.instruction)
        print("=" * 50)
    
    def _should_skip_stage(self, file_path: Path, stage: str) -> bool:
        """Skip a stage if its output file already exists."""
        if file_path.exists():
            self._mark_stage(stage=stage, status="skip", message=f"⏭️ Skipping {stage}: output already exists at {file_path}.")
            self._emit_file_event(stage, file_path)
            return True
        return False

    def _mark_stage(self, stage: str, status: Optional[StageStatus] = None, message: Optional[str] = None) -> None:
        """Emit structured stage updates."""
        self.current_stage = stage
        if status is None:
            status = "running"

        if message:
            print_red(message) if status == "error" else print(message)

        self._emit_event(type_name="stage_status", stage=stage, status=status, message=message)
    
    def _emit_event(self, type_name: str, stage: str, status: Optional[StageStatus] = None,
                    message: Optional[str] = None, payload: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Emit a single structured event.
        {
            "type": <type name>,
            "stage": <stage name>,
            "status": <optional status string>,
            "message": <optional human readable string>,
            "payload": <optional structured data dict>
        }
        - Console: truncated content for readability (written directly to the real stdout).
        - Log file: full content (appended to `event_log_path`).
        """
        event_stage = stage or self.current_stage
        base_event: Dict[str, Any] = {
            "type": type_name, "stage": event_stage, "status": status, "message": message, "payload": payload
        }

        if status == "error":
            self._write_stage_success(stage, False)
        else:
            self._write_stage_success(stage, True)

        display_event = self._to_display_event(base_event)

        # Console-friendly event (bypass Tee to avoid duplicating truncated content in logs)
        try:
            sys.__stdout__.write(f"__EVENT__ {json.dumps(display_event, ensure_ascii=False)}\n")
            sys.__stdout__.flush()
        except Exception as exc:
            print_red(f"Failed to encode event {display_event}: {exc}")

        # Full event log for later debugging
        try:
            self.event_log_stream.write("__EVENT__ " + json.dumps(base_event, ensure_ascii=False, indent=2) + "\n")
            self.event_log_stream.flush()
        except Exception as exc:
            print_red(f"Failed to write full event: {exc}")
    
    def _to_display_event(self, event: Dict[str, Any], limit: int = 200) -> Dict[str, Any]:
        """Return a console-friendly copy of the event with long strings truncated."""

        def truncate(value: Any) -> Any:
            if isinstance(value, str) and len(value) > limit:
                truncated = value[:limit]
                truncated = truncated.rsplit(" ", 1)[0] or truncated
                return f"{truncated} ... (truncated)"
            if isinstance(value, list):
                return [truncate(item) for item in value]
            if isinstance(value, dict):
                return {k: truncate(v) for k, v in value.items()}
            return value

        return truncate(copy.deepcopy(event))

    def _emit_file_event(self, stage: str, path: Path) -> None:
        """Emit a file event with a predictable payload."""
        try:
            content = path.read_text(encoding="utf-8")
        except Exception as exc:
            self._emit_event(
                type_name="file_generate", stage=stage, status="error",
                message=f"Unable to read generated file {path}: {exc}",
            )
            return

        self._emit_event(
            type_name="file_generate", stage=stage, status="complete",
            payload={"file": {"name": path.name, "path": str(path), "content": content}},
        )

    def _write_stage_success(self, stage: str, success: bool, force: bool = False) -> None:
        session_meta: Dict[str, Any] = {}
        if self.session_meta_path.exists():
            try:
                session_meta = json.loads(self.session_meta_path.read_text(encoding="utf-8"))
            except Exception as exc:
                print_red(f"Failed to read session meta from {self.session_meta_path}: {exc}")
        if not isinstance(session_meta, dict):
            session_meta = {}

        stage_success = session_meta.get("stage_success")
        if not isinstance(stage_success, dict):
            stage_success = {}
        current_value = stage_success.get(stage)
        if force:
            # Only for a stage that is re-run and ends successfully (deploy retry).
            stage_success[stage] = bool(success)
        elif isinstance(current_value, bool):
            stage_success[stage] = current_value and bool(success)
        else:
            stage_success[stage] = bool(success)
        session_meta["stage_success"] = stage_success
        try:
            self.session_meta_path.write_text(
                json.dumps(session_meta, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        except Exception as exc:
            print_red(f"Failed to write session meta to {self.session_meta_path}: {exc}")

    def _verify_output_file(self, file_path: Path) -> bool:
        """Verify that an output file exists and is non-empty."""
        if not file_path.exists():
            return False
        
        try:
            size = file_path.stat().st_size
            return size > 0
        except Exception as e:
            print_red(f"Error verifying file {file_path}: {e}")
            return False
    
    def _load_file_content(self, file_path: Path) -> str:
        """Load the complete content of a file."""
        return file_path.read_text(encoding="utf-8")
        
    def _load_file_until_marker(self, filepath: Path, marker: str) -> str:
        """Load file content up to a marker line (exclusive). Returns full file if the marker is missing."""
        if not filepath.exists():
            print_red(f"⚠️  File not found: {filepath}")
            return ""
        
        content_lines = []
        with filepath.open('r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith(marker):
                    break
                content_lines.append(line)
        
        return ''.join(content_lines)
    
    def write_markdown(self, path: Path, text: str) -> None:
        """Persist markdown content, unwrapping ```markdown fences when present."""
        m = re.search(r"```(?:markdown|md)\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)
        content = m.group(1).strip() if m else text.strip()
        path.write_text(content, encoding="utf-8")

    def _has_required_checklist(self, content: str | None) -> bool:
        if content:
            for line in content.splitlines():
                if line.strip().startswith("# Test Checklist"):
                    return True
        return False
    
    def _has_required_result(self, content: str | None) -> bool:
        if content:
        #     for line in content.splitlines():
        #         if line.strip().startswith("# Test Result"):
        #             return True
        # return False
            for line in content.splitlines():
                s = line.strip()
                if s.startswith("#") and s.lstrip("#").strip().startswith("Test Result"):
                    return True
        return False
    
    
