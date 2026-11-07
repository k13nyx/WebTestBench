# Test Result

## Functionality

- [X] FT-01: New user can register an account
  - Action: Open the registration page, fill in username, email, and password (with matching confirmation), submit the form.
  - Expected: Account is created, user is signed in, and lands on the home/catalog or dashboard page (no error message).

- [X] FT-02: Registered user can log in
  - Action: Log out (if signed in), go to the login page, enter the credentials from FT-01, submit.
  - Expected: User is authenticated and the signed-in state (username/profile link) is visible.

- [X] FT-03: Catalog lists programming challenges
  - Action: Open the Challenges/Catalog page.
  - Expected: Multiple challenges are listed (at least 3 from default data), each reachable by clicking it.

- [X] FT-04: Catalog can be filtered by difficulty and by topic
  - Action: Select one difficulty level (e.g., "Easy"), then clear it and select one topic (e.g., "Arrays").
  - Expected: Only challenges matching the selected difficulty are shown; only challenges matching the selected topic are shown; results change after each selection.

- [X] FT-05: Correct solution passes all predefined test cases
  - Action: Open any challenge, enter a known-correct solution into the embedded editor, click the "Submit"/"Run" button.
  - Expected: All predefined test cases pass; result shows a "Passed"/"Accepted" status (e.g., "All tests passed") with success feedback.

- [X] FT-06: Incorrect solution fails and shows basic feedback
  - Action: Open a challenge, enter a deliberately wrong solution (e.g., returns a constant), click "Submit".
  - Expected: Result shows a "Failed"/"Wrong Answer" status and includes feedback identifying at least one failing test case.

- [X] FT-07: Dashboard shows progress statistics by difficulty
  - Action: Open the personal Dashboard page.
  - Expected: Statistics section displays the number of challenges completed broken down by difficulty (Easy/Medium/Hard), plus total solved and total points.

- [ ] FT-08: Past submissions can be reviewed
  - Action: Open the "My Submissions"/history page.
  - Expected: All previous submissions are listed, each showing challenge name, date/time, and Passed/Failed status; the submissions from FT-05 and FT-06 both appear.
  - Bug Report:
    - Issue: Missing Page / Missing Status Label
    - Actual: No "My Submissions" page exists. Navigating to http://localhost:6008/submissions and http://localhost:6008/my-submissions both return the 404 page ("404 — Oops! Page not found"), and the user dropdown menu contains only "Dashboard" and "Logout" (no submissions link). The only cross-challenge view is the Dashboard's "Recent Submissions" card, which does list all 5 past submissions (including the FT-05 pass and the FT-06 failure) with challenge name and date, but shows status only as an unlabeled ✓/✕ icon — there is no textual "Passed"/"Failed" label. The per-challenge "History" tab (e.g. /challenge/1) does show text status ("3/3 passed", "0/3 passed") but is scoped to a single challenge.

- [X] FT-09: Leaderboard ranks users by points earned
  - Action: Open the Leaderboard page.
  - Expected: Users are listed in descending order of points; the signed-in user appears with the points total matching their dashboard.

## Constraint

- [X] CS-01: Duplicate registration is rejected
  - Action: Register again using the same email/username as an existing account.
  - Expected: Registration fails, an explicit error (e.g., "Email already in use") is shown, and no duplicate account is created.

- [ ] CS-02: Registration validation blocks incomplete/invalid input
  - Action: Submit the registration form with an empty required field and with mismatched password confirmation.
  - Expected: Submission is blocked each time with a validation message; no account is created.
  - Bug Report:
    - Issue: Missing Form Field (test case not executable)
    - Actual: The empty-required-field case works: the Username/Email/Password inputs are all marked `required`, and submitting with Username cleared blocked submission (URL stayed /register, input `checkValidity()` = false with message "Please fill out this field.", no account created). However, the mismatched-password-confirmation case cannot be executed: the registration form has only three fields (Username, Email, Password) and contains no "Confirm Password" field at all, so no mismatch can be entered and no validation for it exists.

- [ ] CS-03: Empty code cannot be submitted
  - Action: Open a challenge, leave the editor empty (or clear it), click "Submit".
  - Expected: No test run occurs; an inline error such as "Code cannot be empty" is displayed (or the Submit control is disabled).
  - Bug Report:
    - Issue: Missing Validation / Unblocked Invalid Submission
    - Actual: With the editor cleared (model value = ""), the "Run Tests" button remained enabled (not disabled, no aria-disabled). Clicking it executed a full test run and recorded a new submission (History tab count went from 2 to 3). No inline error message such as "Code cannot be empty" appeared anywhere on the page. The result panel showed "Test Results: 0/3 passed" with "Got: Error: solution is not defined" for all three test cases.

- [X] CS-04: Solving an already-solved challenge does not double-count points
  - Action: Note the user's points, re-submit a correct solution for a challenge already solved, then check points.
  - Expected: Points total is unchanged (or increased only if the app explicitly awards first-solve only); completed-challenge count does not increase.

- [ ] CS-05: Personal pages require authentication
  - Action: Log out, then navigate directly to the Dashboard and My Submissions pages.
  - Expected: Access is denied and the user is redirected to the login page; no personal data is displayed.
  - Bug Report:
    - Issue: Missing Route (redirect not applied for submissions page)
    - Actual: After logging out, navigating directly to /dashboard correctly redirected to /login (URL became http://localhost:6008/login) with no personal data displayed. However, the second required target cannot be satisfied: navigating to /submissions (and /my-submissions) while signed out renders the 404 "Oops! Page not found" page instead of redirecting to the login page, because no My Submissions route exists in the application.

## Interaction

- [X] IX-01: Clicking a challenge opens its solving view
  - Action: Click any challenge card/title in the catalog.
  - Expected: The challenge detail page opens with the problem statement, difficulty, topic, and an editable embedded code editor.

- [X] IX-02: Submission shows a running state then the result without a page reload
  - Action: Click "Submit" on a challenge and observe the page.
  - Expected: A loading/running indicator appears, then is replaced by the result panel (page does not fully reload or navigate away).

- [X] IX-03: Dashboard updates to reflect a newly solved challenge
  - Action: Note dashboard stats, solve a previously unsolved challenge (correct solution), return to the Dashboard.
  - Expected: The newly solved challenge is marked as completed and the completed count for its difficulty level increases by 1.

## Content

- [X] CT-01: Catalog entries display required attributes
  - Action: Inspect every challenge card in the unfiltered catalog.
  - Expected: Each card shows a title, a difficulty badge (e.g., Easy/Medium/Hard), and a topic label — none blank or missing.

- [X] CT-02: Challenge detail shows full problem content
  - Action: Open any challenge detail page.
  - Expected: It displays the problem description, difficulty level, topic, and the predefined example test case(s) with input and expected output.

- [X] CT-03: Leaderboard entries show required fields
  - Action: Inspect the leaderboard rows.
  - Expected: Each row displays rank, username, and points earned; values are non-empty and consistent (rank 1 has the highest points).
