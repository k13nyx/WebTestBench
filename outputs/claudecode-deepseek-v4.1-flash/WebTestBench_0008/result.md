CS-01 PASS (blocked with "Email already registered" toast). All checklist items have been executed. Here is the complete result.

# Test Result

## Functionality

- [X] FT-01: User can register a new account
  - Action: Open the registration page, enter a unique username, valid email, and matching password, then click the "Register" / "Sign Up" button.
  - Expected: Account is created and the user is logged in or redirected to the login/catalog page.

- [X] FT-02: Registered user can log in
  - Action: Enter valid existing credentials on the login page and submit.
  - Expected: User is authenticated and taken to the catalog or dashboard.

- [X] FT-03: User can browse the challenge catalog
  - Action: Navigate to the catalog/challenges page.
  - Expected: A list of existing challenges is displayed.

- [X] FT-04: Challenges can be filtered/viewed by difficulty
  - Action: Select a difficulty level (e.g., "Easy", "Medium", "Hard") in the catalog filter.
  - Expected: Only challenges matching the selected difficulty are listed.

- [X] FT-05: Challenges can be filtered/viewed by topic
  - Action: Select a topic (e.g., "Arrays", "Strings") in the catalog filter.
  - Expected: Only challenges belonging to the selected topic are listed.

- [X] FT-06: User can open a challenge with its embedded code editor
  - Action: Click a challenge in the catalog.
  - Expected: Challenge details and an embedded code editor with a "Submit" / "Run" button are shown.

- [X] FT-07: Submitting a correct solution runs tests and reports pass
  - Action: Enter a known-correct solution in the editor and click "Submit".
  - Expected: System runs it against predefined test cases and reports the result as PASSED.

- [X] FT-08: Submitting an incorrect solution reports failure with feedback
  - Action: Enter an incorrect solution and click "Submit".
  - Expected: Result is reported as FAILED along with basic feedback describing the failure.

- [X] FT-09: Dashboard shows progress and completed challenges by difficulty
  - Action: Open the personal dashboard as a logged-in user.
  - Expected: Progress overview and statistics of challenges completed broken down by difficulty are displayed.

- [X] FT-10: User can review past submissions
  - Action: Open the submissions/history section from the dashboard.
  - Expected: A list of the user's previous submissions with their results is displayed.

- [X] FT-11: Leaderboard ranks users by points earned
  - Action: Open the leaderboard page.
  - Expected: Users are listed in descending order of points earned from solved challenges.

## Constraint

- [X] CS-01: Registration is rejected for an already-used email
  - Action: Attempt to register using an email that already belongs to an existing account.
  - Expected: Registration is blocked with an error indicating the email is already in use.

- [X] CS-02: Registration is rejected when required fields are empty
  - Action: Submit the registration form with one or more required fields left blank.
  - Expected: Submission is blocked and validation errors identify the missing required fields.

- [ ] CS-03: Empty code submission is rejected
  - Action: Click "Submit" with an empty editor.
  - Expected: Submission is blocked or immediately reported as invalid; no test run is executed as a valid solution.
  - Bug Report:
    - Issue: Missing empty-input validation — empty submission is accepted and executed as a test run instead of being blocked.
    - Actual: With the editor cleared, clicking "Run Tests" does not block or warn; it runs the test suite and displays `Test Results: 0/2 passed` with `Got: Error: solution is not defined` for each case. The empty attempt is also recorded (History increments, submission count rises). No validation message or blocked submission occurs, and a test run is executed.

- [X] CS-04: Personal dashboard/submissions require authentication
  - Action: Attempt to open the dashboard or submissions page while logged out.
  - Expected: Access is denied and the user is redirected to login.

- [X] CS-05: A failed solution awards no points
  - Action: Submit an incorrect solution, then compare the user's points before and after.
  - Expected: Points remain unchanged for the failed submission.

## Interaction

- [X] IX-01: Confirmation is shown after successful registration
  - Action: Complete registration with valid unique details.
  - Expected: A success message/toast or confirmation is displayed before or alongside redirection.

- [X] IX-02: Loading indicator appears while tests run
  - Action: Click "Submit" on a solution.
  - Expected: A visible loading/running indicator appears until the result is returned.

## Content

- [X] CT-01: Challenge listings display title, difficulty, and topic
  - Action: Inspect challenge items in the catalog.
  - Expected: Each entry clearly shows the challenge title, its difficulty, and its topic.

- [X] CT-02: Leaderboard entries display username and point value
  - Action: Inspect rows on the leaderboard.
  - Expected: Each row shows the user's name/username and their earned points.

---

### Summary

- **Total items:** 20
- **Passed:** 19
- **Failed:** 1 (CS-03)

**Only defect found:** Empty code submissions are not blocked or flagged as invalid — clicking "Run Tests" with an empty editor executes the full test harness (`0/2 passed`, `Error: solution is not defined`) and records the attempt, contrary to the expectation that empty submissions be rejected before any test run. All other functionality (registration, login, catalog browsing/filtering, editor, pass/fail results with per-case feedback, dashboard stats by difficulty, submission history, leaderboard ordering, auth gating, and no-points-on-failure) worked as specified.