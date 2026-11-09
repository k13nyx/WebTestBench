# Test Result

## Functionality
- [X] FT-01: User can register an account with valid credentials
  - Action: Open the registration page, enter a unique username, valid email, and password (meeting any stated rules), and click the register/submit button.
  - Expected: Account is created and the user is logged in or redirected to login/dashboard with a confirmation that registration succeeded.
  - Result: Registered `qa_alice_742` / `qa_alice_742@example.com`; redirected to `/dashboard`, auto-logged in, toast "Welcome to CodeForge, qa_alice_742!" shown.

- [X] FT-02: Registered user can log in and access the challenge catalog
  - Action: Log out (if auto-logged-in), then log in with the newly registered email/username and password.
  - Expected: Login succeeds and the browsable catalog of programming challenges is reachable.
  - Result: Logged out via user menu → `/login`; signed in with the new credentials ("Welcome back" toast); "Challenges" nav opened the catalog (10 challenges) with search and difficulty/topic filters.

- [X] FT-03: Catalog displays challenges labeled by difficulty and topic
  - Action: From the catalog/browse page, view the list of default challenges.
  - Expected: Each challenge entry shows its title, a difficulty label (e.g., Easy/Medium/Hard), and a topic label (e.g., Arrays, Strings).
  - Result: All 10 entries show title + difficulty (easy/medium/hard) + topic (arrays, strings, algorithms, data structures, dynamic programming, recursion), plus test-case count and points.

- [X] FT-04: User can open a challenge and type code in an embedded editor
  - Action: Click a default challenge from the catalog and type several lines of code into the on-page editor.
  - Expected: The challenge detail view opens with an embedded code editor in which the typed code is visible and editable (no external tool required).
  - Result: `/challenge/1` opened with an embedded Monaco editor (starter stub visible); multi-line code typed and edited (selection/delete/replace all worked). Note: Monaco auto-bracketing inserts extra braces while typing, but the editor remains fully functional.

- [X] FT-05: Submitting code automatically runs it against test cases and shows a pass/fail verdict
  - Action: With a code solution entered in the editor, click the Submit/Run button.
  - Expected: The system automatically executes the solution against predefined test cases and displays a clear PASSED or FAILED result.
  - Result: Clicking "Run Tests" auto-executed against the 3 predefined cases and displayed "Test Results: 3/3 passed" with per-case Input/Expected/Got.

- [X] FT-06: Passing all test cases marks the challenge as solved and awards points
  - Action: Submit a correct solution for a default challenge not yet solved by this user.
  - Expected: The challenge is marked completed/solved and points are awarded for its difficulty.
  - Result: After Two Sum passed 3/3, its title showed a solved check icon, dashboard went to Total Points 10 / Challenges Solved 1/10 / Easy 1/5. Second solve (Maximum Subarray, medium) awarded +20 (points 30, Medium 1/4).

- [X] FT-07: Dashboard shows progress statistics, including challenges completed by difficulty
  - Action: Open the personal dashboard as the logged-in user.
  - Expected: The dashboard displays progress data including a count of challenges completed broken down by difficulty (e.g., Easy/Medium/Hard).
  - Result: Dashboard shows Total Points, Challenges Solved (x/10), Submissions, Success Rate, and "Progress by Difficulty": Easy 1/5, Medium 1/4, Hard 0/1, Overall 20%, plus Recent Submissions.

- [ ] FT-08: Past submissions can be reviewed
  - Action: Open the submissions history section (on the dashboard or a dedicated page) after making at least one submission.
  - Expected: The list shows previous submissions with challenge name and result (passed/failed), and at least one entry can be opened to view its details.
  - Bug Report:
    - Issue: Unopenable submission history entries — no detail view exists
    - Actual: The challenge "History" tab lists entries as plain non-interactive divs (only "3/3 passed" / "1/3 passed" + date; clicking does nothing — verified `link: false, btn: false, cursor: auto` and DOM unchanged after click). Dashboard "Recent Submissions" links open the challenge page (its Description/History), not the submission itself: submitted code and per-test results of past runs cannot be viewed. The dashboard list also shows results only via icons/points ("✕" / "+10 pts"), not explicit passed/failed text.

- [X] FT-09: Leaderboard displays users ranked by points
  - Action: Navigate to the leaderboard page.
  - Expected: A ranking list is shown with user names ordered by points earned, and the test user's points appear consistent with solved challenges.
  - Result: Leaderboard shows "Top coders ranked by total points earned": charlie_algo 110, alice_codes 80, bob_dev 50, then rank 4 qa_alice_742 — "2 challenges solved, 30 points", exactly matching the two solves (Easy 10 + Medium 20) in descending points order.

## Constraint
- [X] CS-01: Registration is blocked for a duplicate account
  - Action: Attempt to register again using the exact same username/email as the existing account.
  - Expected: Registration is rejected with a visible error (e.g., "already taken/exists") and no second account is created.
  - Result: Duplicate submission stayed on `/register` and displayed the visible error "Email already registered"; no account created, no auto-login.

- [X] CS-02: Registration requires all mandatory fields
  - Action: Submit the registration form with required fields left empty or with an invalid email format.
  - Expected: Submission is blocked and an inline error identifies the missing/invalid field.
  - Result: All three inputs have `required=true` and email uses `type=email`; submitting empty blocked submission and focused the username field; with `not-an-email` submission blocked and focus moved to the email field (`validity.valid: false`). Errors surface via browser-native validation bubbles anchored to the offending field (no separate app-rendered inline error text, but submission is correctly blocked and the invalid field is identified).

- [ ] CS-03: Unauthenticated users cannot submit solutions
  - Action: While logged out, try to open a challenge's code editor/submit page directly.
  - Expected: The app prevents solving — it redirects to login/registration or disables submission — and does not run tests for anonymous users.
  - Bug Report:
    - Issue: Missing auth guard on challenge solve/submit flow
    - Actual: While logged out, `/challenge/4` loaded fully (navbar showed Login/Get Started), the Monaco editor rendered with the starter stub, and the "Run Tests" button was enabled (`disabled: false`). Clicking it executed the tests for the anonymous user and displayed "Test Results: 0/3 passed" with per-case Expected/Got — no redirect, no login prompt, submission not disabled.

- [ ] CS-04: Empty code submission is rejected without running tests
  - Action: Open the editor for a challenge and click Submit with the code area empty (or unchanged starter stub).
  - Expected: A validation message appears (e.g., "code is required") and no test-run result is produced.
  - Bug Report:
    - Issue: No empty-code validation; tests executed on blank input
    - Actual: With the editor fully empty (verified `.view-lines` innerText `""`), clicking Run Tests produced a fresh test run: heading "Test Results: 0/3 passed" and per-case results "Got: Error: solution is not defined" for all 3 test cases. No validation message (no "required/empty" text anywhere, empty toasts). The unchanged starter stub likewise ran tests (0/3 passed) without warning.

- [X] CS-05: Failed submissions do not complete the challenge or award points
  - Action: Submit an intentionally incorrect solution to an unsolved default challenge, then check the dashboard/leaderboard.
  - Expected: The challenge remains marked unsolved and the user's points/completion counts do not increase.
  - Result: Incorrect Maximum Subarray solution (1/3 passed) and `return n` for Fibonacci (1/4 passed) both awarded no points and triggered no "solved" state/toast (verified `solvedBadge: null`, toasts empty at fail time). Final dashboard: 30 pts, 2/10 solved, Easy 1/5 (Fibonacci still unsolved) — only the two fully-passing submissions counted. (Submissions count and success rate did update to 4 / 50%, which is correct accounting, not points.)

## Interaction
- [X] IX-01: Interface gives feedback while the submission is being executed
  - Action: Click Submit and observe the UI during execution.
  - Expected: The app shows an in-progress state (e.g., "Running tests…" indicator or disabled submit button) and then reveals the final result.
  - Result: UI sampling during the run captured a "Running..." state (button replaced, indicator visible across ~5 samples over ~600 ms), after which the final "Test Results: 3/3 passed" panel appeared.

- [X] IX-02: Failed submissions show basic per-test feedback
  - Action: Submit a solution that passes some but not all test cases.
  - Expected: The result panel indicates which test case(s) failed (e.g., "Test case 2/4 failed") plus basic feedback text explaining the failure, not just a generic "FAILED".
  - Result: A 1/3-failing and a 1/4-failing run showed heading "Test Results: 1/3 passed" / "1/4 passed" plus each case's Input with "Expected: X" vs "Got: Y" (e.g., Input [-2,1,-3,4,-1,2,1,-5,4]: Expected 6, Got 4), clearly identifying which tests failed and why, not a generic FAILED.

- [X] IX-03: Solving a challenge produces a success response and refreshes state
  - Action: Submit a fully passing solution while monitoring the UI.
  - Expected: A success indication appears (e.g., toast, badge, or "Challenge solved" message with points earned) and the dashboard/leaderboard reflects the new solved status and points.
  - Result: On the passing submission the toast "Congratulations! You earned 20 points!" appeared immediately, the title gained a solved check icon, History count incremented (0→2), and dashboard/leaderboard updated (30 total pts, 2/10 solved, Medium 1/4; leaderboard row "qa_alice_742 — 2 challenges solved, 30 points").

## Content
- [X] CT-01: Default catalog content is relevant and complete
  - Action: Inspect several default challenges across the catalog and open their detail pages.
  - Expected: Challenges cover multiple difficulties and topics; each detail page contains a real problem statement (no placeholder/lorem text) and at least one example input/output tied to the test cases.
  - Result: 10 challenges spanning Easy/Medium/Hard and 6 topics. Opened Two Sum, Maximum Subarray, and Fibonacci Number: all show genuine, coherent problem statements and Example Input/Output blocks that match the executed test cases (e.g., Two Sum examples [2,7,11,15],9→[0,1] and [3,2,4],6→[1,2] appear verbatim as tests 1–2; Maximum Subarray [-2,1,-3,4,-1,2,1,-5,4]→6 matches test 1). No lorem/placeholder text found.

- [X] CT-02: Reported statistics are consistent with actual activity
  - Action: Compare the dashboard's completed-by-difficulty counts, total points, and the submission history against the user's actual test runs from FT-05/FT-06/CS-05.
  - Expected: Every displayed number matches reality (passed submissions counted, failed submissions excluded, points match difficulty values shown on the leaderboard).
  - Result: Actual activity = 4 runs: Two Sum passed (+10), Max Subarray failed, Max Subarray passed (+20), Fibonacci failed. Dashboard: Total Points 30 ✓ (10+20 only), Challenges Solved 2/10 ✓ (passed-only), Easy 1/5 / Medium 1/4 / Hard 0/1 / Overall 20% ✓, Submissions 4 ✓ (all runs), Success Rate 50% ✓ (2 passed / 4). Recent Submissions lists exactly the 4 runs (failures marked ✕, no points). Leaderboard shows the same 30 points and 2 solves, consistent with catalog difficulty values (easy +10, medium +20, hard +30).
