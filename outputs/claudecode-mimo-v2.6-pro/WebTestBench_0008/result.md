✅ **CS-01 PASS** — Registration rejected with error "Email already registered", stayed on /register, no duplicate account created.

All checklist items executed. Final results:

# Test Result

## Functionality

- [X] FT-01: User can create a new account through the registration form.
  - Action: Open the registration page, fill in the username, email, and password fields with valid values, and click "Register".
  - Expected: The account is created and the user is authenticated and taken to the logged-in area (Dashboard).

- [X] FT-02: User can log in with a registered account.
  - Action: Open the login page, enter the credentials created in FT-01, and click "Log In".
  - Expected: The user is logged in and the Dashboard / user menu is displayed.

- [X] FT-03: User can browse the catalog of programming challenges.
  - Action: Navigate to the Challenges / Catalog page.
  - Expected: The list of default programming challenges is displayed.

- [X] FT-04: User can filter the catalog by difficulty.
  - Action: Select a difficulty (e.g., "Easy") in the difficulty filter control on the Catalog page.
  - Expected: Only challenges with the selected difficulty are listed; challenges of other difficulties are hidden.

- [X] FT-05: User can filter the catalog by topic.
  - Action: Select a topic (e.g., "Arrays") in the topic filter control on the Catalog page.
  - Expected: Only challenges with the selected topic are listed; other topics are hidden.

- [X] FT-06: User can open a challenge and view its problem statement.
  - Action: Click on a challenge in the catalog list.
  - Expected: The challenge page opens showing the challenge title, its problem description, and a code editor.

- [X] FT-07: User can enter code in the embedded editor and submit it.
  - Action: On a challenge page, type a code solution into the embedded editor and click "Submit".
  - Expected: The submission is accepted and the evaluation process starts.

- [X] FT-08: Submitted code is automatically run against predefined test cases and a pass/fail result is shown.
  - Action: Submit a correct solution for a challenge, then submit an incorrect solution for another challenge.
  - Expected: The correct solution is reported as "Passed" and the incorrect solution is reported as "Failed", based on the predefined test cases.

- [X] FT-09: User receives basic feedback after a submission.
  - Action: Submit a solution that fails one or more test cases.
  - Expected: Basic feedback is displayed (e.g., which test cases failed or the error/exception message), not just the verdict alone.

- [X] FT-10: Personal dashboard shows the user's progress and statistics by difficulty.
  - Action: Navigate to the Dashboard page as a logged-in user.
  - Expected: A progress summary and counts of completed challenges per difficulty (e.g., Easy/Medium/Hard) are shown, matching the user's actual solved challenges.

- [X] FT-11: User can review past submissions.
  - Action: Open the Submissions / History page from the Dashboard.
  - Expected: The user's past submissions are listed with their status (passed or failed).

- [X] FT-12: User can view the leaderboard.
  - Action: Open the Leaderboard page.
  - Expected: Users are listed with their earned points and ranked by points.

## Constraint

- [X] CS-01: Registration with an already-used username or email is rejected.
  - Action: Attempt to register using the username or email of an existing default account.
  - Expected: Registration is rejected with an error message and no duplicate account is created.

- [ ] CS-02: Code cannot be submitted when the editor is empty.
  - Action: On a challenge page, leave the code editor empty and click "Submit".
  - Expected: The submission is blocked with a validation message and no evaluation is run.
  - Bug Report:
    - Issue: Missing Empty-Editor Validation / Unvalidated Submission
    - Actual: With the editor completely empty, clicking "Run Tests" was not blocked — the evaluation ran anyway showing "Test Results: 0/3 passed" with "Got: Error: solution is not defined" for every test case, and a submission was recorded (challenge History counter incremented from 0 to 1). No validation message was displayed.

- [X] CS-03: Points are awarded only when all test cases pass.
  - Action: Submit a failing solution, then check the user's points on the Dashboard or Leaderboard.
  - Expected: The points total does not increase after the failing submission.

- [X] CS-04: Points are not awarded twice for the same challenge.
  - Action: Submit a passing solution for an already-solved challenge, then check the user's points.
  - Expected: The points total does not increase beyond the points for the first successful solve.

## Interaction

- [X] IX-01: A loading/processing state is shown while the submitted code is being evaluated.
  - Action: Click "Submit" with a valid solution and observe the page during evaluation.
  - Expected: A loading or "Running..." indicator appears while evaluation is in progress and disappears once the result is displayed.

- [X] IX-02: Filter selection is visually reflected in the UI and updates the list immediately.
  - Action: Select a difficulty filter, then a topic filter on the Catalog page.
  - Expected: The challenge list refreshes immediately after each selection and the active filter is visually indicated (e.g., highlighted/selected state).

## Content

- [X] CT-01: The catalog displays accurate title, difficulty, and topic for each challenge.
  - Action: View the Catalog page listing the default challenges.
  - Expected: Each challenge entry shows its title, difficulty, and topic, matching that challenge's actual data.

- [X] CT-02: The leaderboard shows accurate usernames and points, ordered by points.
  - Action: View the Leaderboard page with the default users.
  - Expected: Each row shows a username and a points value, and rows are sorted by points from highest to lowest.

---

**Summary: 20 PASS / 1 FAIL** — The only defect is **CS-02**: the empty-editor submission guard is missing; an empty editor is evaluated (producing "solution is not defined" errors and a recorded failed submission) instead of being blocked with a validation message.