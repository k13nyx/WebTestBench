# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Click "Register"/"Sign Up", enter a new email, a password (and any other required fields), submit the form.
  - Expected: Account is created, the user is signed in or redirected to login, and a confirmation is shown.

- [ ] FT-02: Registered user can log in and log out
  - Action: Log out via the header/account menu, then log back in with the registered email and password.
  - Expected: Logout returns to an unauthenticated state (dashboard/submit inaccessible); login restores the same account's session and data.

- [ ] FT-03: Catalog page lists the default programming challenges
  - Action: Open the catalog/challenges page without creating any new data.
  - Expected: A list of pre-existing challenges is displayed, each with a title, difficulty, and topic.

- [ ] FT-04: Catalog can be filtered by difficulty
  - Action: On the catalog page, select a difficulty filter (e.g. Easy, Medium, Hard) from the difficulty control.
  - Expected: The visible list contains only challenges of that difficulty and at least one entry remains.

- [ ] FT-05: Catalog can be filtered by topic
  - Action: On the catalog page, select a topic filter (e.g. Arrays, Strings, Algorithms).
  - Expected: The visible list contains only challenges of that topic and at least one entry remains.

- [ ] FT-06: A challenge detail page opens from the catalog
  - Action: Click any challenge title in the filtered catalog list.
  - Expected: The challenge's detail page shows its problem statement, difficulty, topic, and the code editor area.

- [ ] FT-07: User can solve a challenge and the site auto-runs it against the test cases
  - Action: Open a challenge, type a correct solution into the embedded code editor, click "Submit"/"Run".
  - Expected: The solution is executed against the predefined test cases automatically and the result shows "Passed" with a green/success indication.

- [ ] FT-08: An incorrect solution is reported as failed
  - Action: Open a challenge, type an incorrect or empty-behavior solution into the editor, click "Submit"/"Run".
  - Expected: The result shows "Failed"/"Wrong Answer" instead of "Passed", and no false success is reported.

- [ ] FT-09: Personal dashboard shows the user's progress
  - Action: Log in and open the dashboard from the navigation.
  - Expected: The dashboard shows the user's challenge list, solved/unsolved state per challenge, and completion progress.

- [ ] FT-10: User can review past submissions
  - Action: Open the "Submissions"/"History" area of the dashboard and click one of the recorded submissions.
  - Expected: The submission's challenge, submitted code, timestamp, and its pass/fail verdict are displayed.

- [ ] FT-11: Dashboard shows challenges completed by difficulty
  - Action: Open the dashboard and locate the statistics section.
  - Expected: Statistics break down the number of challenges the user completed for each difficulty (e.g. Easy/Medium/Hard counts).

- [ ] FT-12: Leaderboard ranks users by points from solved challenges
  - Action: Open the leaderboard page.
  - Expected: Users are listed in descending order of points earned from solved challenges, with each user's points value shown.

## Constraint
- [ ] CS-01: Duplicate account registration is rejected
  - Action: Attempt to register using an email that already has an account.
  - Expected: Registration is refused with a clear "already registered"/duplicate error and no second account is created.

- [ ] CS-02: Required registration fields are validated before account creation
  - Action: Submit the registration form with an empty email and/or empty password, and with an invalid email format.
  - Expected: The form is rejected with a field-level validation message and no account is created.

- [ ] CS-03: Dashboard, submissions, and submitting code require an authenticated session
  - Action: Log out, then attempt to open the dashboard, the submissions page, and a challenge's submit action directly.
  - Expected: Access is blocked or redirected to the login/registration page; no private data is shown.

- [ ] CS-04: Points are awarded only for solved challenges and only once per challenge
  - Action: Submit a failing solution to a challenge, then submit a correct solution to the same challenge, then re-submit the correct solution.
  - Expected: The failing attempt awards no points, the first correct solution awards that challenge's points exactly once, and repeated correct submissions do not increase the points total.

## Interaction
- [ ] IX-01: Verdict is shown automatically after the run completes without a manual page reload
  - Action: Submit a solution and watch the submit control and result area during execution.
  - Expected: The submit button shows a running/pending state while tests execute, and the Passed/Failed verdict replaces it automatically with no manual refresh.

- [ ] IX-02: Dashboard and leaderboard reflect a newly solved challenge without manual refresh
  - Action: Solve a new challenge successfully, then navigate to the dashboard and the leaderboard.
  - Expected: The dashboard counts/statistics and the leaderboard points for the current user already include the newly solved challenge.

## Content
- [ ] CT-01: Challenge detail page shows complete and relevant programming content
  - Action: Open any challenge detail page and read its description, difficulty label, topic label, and any example/test cases shown.
  - Expected: All fields are present, non-empty, and describe an actual programming problem of the stated topic/difficulty (no placeholder or lorem text).

- [ ] CT-02: Failure feedback identifies the failing case and the expected output
  - Action: Submit an incorrect solution to a challenge and read the feedback shown next to the failed result.
  - Expected: The feedback states that the submission failed, identifies which test case failed, and shows the expected versus actual output for that case.