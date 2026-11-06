@echo off
rem ====================================================================
rem WebTestBench eval launcher for Windows cmd.exe.
rem Same knobs as evaluate.sh; extra arguments are passed through, e.g.
rem   evaluate.bat --limit 2 --models claude-haiku-5.5
rem   evaluate.bat --prewarm
rem ====================================================================
setlocal
cd /d "%~dp0"

where python >nul 2>nul || (echo python not found on PATH & exit /b 1)

set "MODELS=all"
set "JOBS=10"

rem The dev server listens on 0.0.0.0 (all network interfaces).
rem The agent's browser opens localhost.
set "WEBTESTBENCH_BIND_HOST=0.0.0.0"
set "WEBTESTBENCH_CONNECT_HOST=localhost"
rem set "WEBTESTBENCH_CONNECT_HOST=host.docker.internal"

python evaluate.py --run --models "%MODELS%" --jobs "%JOBS%" %*
set "RC=%ERRORLEVEL%"

endlocal & exit /b %RC%
