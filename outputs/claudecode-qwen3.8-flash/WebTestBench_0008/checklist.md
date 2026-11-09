# Test Checklist

## Functionality
- [ ] FT-01: User can register an account with valid credentials
  - Action: Open the registration page, enter a unique username, valid email, and password (meeting any stated rules), and click the register/submit button.
  - Expected: Account is created and the user is logged in or redirected to login/dashboard with a confirmation that registration succeeded.

- [ ] FT-02: Registered user can log in and access the challenge catalog
  - Action: Log out (if auto-logged-in), then log in with the newly registered email/username and password.
  - Expected: Login succeeds and the browsable catalog of programming challenges is reachable.

- [ ] FT-03: Catalog displays challenges labeled by difficulty and topic
  - Action: From the catalog/browse page, view the list of default challenges.
  - Expected: Each challenge entry shows its title, a difficulty label (e.g., Easy/Medium/Hard), and a topic label (e.g., Arrays, Strings).

- [ ] FT-04: User can open a challenge and type code in an embedded editor
  - Action: Click a default challenge from the catalog and type several lines of code into the on-page editor.
  - Expected: The challenge detail view opens with an embedded code editor in which the typed code is visible and editable (no external tool required).

- [ ] FT-05: Submitting code automatically runs it against test cases and shows a pass/fail verdict
  - Action: With a code solution entered in the editor, click the Submit/Run button.
  - Expected: The system automatically executes the solution against predefined test cases and displays a clear PASSED or FAILED result.

- [ ] FT-06: Passing all test cases marks the challenge as solved and awards points
  - Action: Submit a correct solution for a default challenge not yet solved by this user.
  - Expected: The challenge is marked completed/solved and points are awarded for its difficulty.

- [ ] FT-07: Dashboard shows progress statistics, including challenges completed by difficulty
  - Action: Open the personal dashboard as the logged-in user.
  - Expected: The dashboard displays progress data including a count of challenges completed broken down by difficulty (e.g., Easy/Medium/Hard).

- [ ] FT-08: Past submissions can be reviewed
  - Action: Open the submissions history section (on the dashboard or a dedicated page) after making at least one submission.
  - Expected: The list shows previous submissions with challenge name and result (passed/failed), and at least one entry can be opened to view its details.

- [ ] FT-09: Leaderboard displays users ranked by points
  - Action: Navigate to the leaderboard page.
  - Expected: A ranking list is shown with user names ordered by points earned, and the test user's points appear consistent with solved challenges.

## Constraint
- [ ] CS-01: Registration is blocked for a duplicate account
  - Action: Attempt to register again using the exact same username/email as the existing account.
  - Expected: Registration is rejected with a visible error (e.g., "already taken/exists") and no second account is created.

- [ ] CS-02: Registration requires all mandatory fields
  - Action: Submit the registration form with required fields left empty or with an invalid email format.
  - Expected: Submission is blocked and an inline error identifies the missing/invalid field.

- [ ] CS-03: Unauthenticated users cannot submit solutions
  - Action: While logged out, try to open a challenge's code editor/submit page directly.
  - Expected: The app prevents solving — it redirects to login/registration or disables submission — and does not run tests for anonymous users.

- [ ] CS-04: Empty code submission is rejected without running tests
  - Action: Open the editor for a challenge and click Submit with the code area empty (or unchanged starter stub).
  - Expected: A validation message appears (e.g., "code is required") and no test-run result is produced.

- [ ] CS-05: Failed submissions do not complete the challenge or award points
  - Action: Submit an intentionally incorrect solution to an unsolved default challenge, then check the dashboard/leaderboard.
  - Expected: The challenge remains marked unsolved and the user's points/completion counts do not increase.

## Interaction
- [ ] IX-01: Interface gives feedback while the submission is being executed
  - Action: Click Submit and observe the UI during execution.
  - Expected: The app shows an in-progress state (e.g., "Running tests…" indicator or disabled submit button) and then reveals the final result.

- [ ] IX-02: Failed submissions show basic per-test feedback
  - Action: Submit a solution that passes some but not all test cases.
  - Expected: The result panel indicates which test case(s) failed (e.g., "Test case 2/4 failed") plus basic feedback text explaining the failure, not just a generic "FAILED".

- [ ] IX-03: Solving a challenge produces a success response and refreshes state
  - Action: Submit a fully passing solution while monitoring the UI.
  - Expected: A success indication appears (e.g., toast, badge, or "Challenge solved" message with points earned) and the dashboard/leaderboard reflects the new solved status and points.

## Content
- [ ] CT-01: Default catalog content is relevant and complete
  - Action: Inspect several default challenges across the catalog and open their detail pages.
  - Expected: Challenges cover multiple difficulties and topics; each detail page contains a real problem statement (no placeholder/lorem text) and at least one example input/output tied to the test cases.

- [ ] CT-02: Reported statistics are consistent with actual activity
  - Action: Compare the dashboard's completed-by-difficulty counts, total points, and the submission history against the user's actual test runs from FT-05/FT-06/CS-05.
  - Expected: Every displayed number matches reality (passed submissions counted, failed submissions excluded, points match difficulty values shown on the leaderboard).