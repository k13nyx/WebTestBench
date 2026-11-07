# Test Result

## Functionality

- [X] FT-01: User can register a new account
  - Action: Click "Register"/"Sign Up", enter a new email, a password (and any other required fields), submit the form.
  - Expected: Account is created, the user is signed in or redirected to login, and a confirmation is shown.

- [X] FT-02: Registered user can log in and log out
  - Action: Log out via the header/account menu, then log back in with the registered email and password.
  - Expected: Logout returns to an unauthenticated state (dashboard/submit inaccessible); login restores the same account's session and data.

- [X] FT-03: Catalog page lists the default programming challenges
  - Action: Open the catalog/challenges page without creating any new data.
  - Expected: A list of pre-existing challenges is displayed, each with a title, difficulty, and topic.

- [X] FT-04: Catalog can be filtered by difficulty
  - Action: On the catalog page, select a difficulty filter (e.g. Easy, Medium, Hard) from the difficulty control.
  - Expected: The visible list contains only challenges of that difficulty and at least one entry remains.

- [X] FT-05: Catalog can be filtered by topic
  - Action: On the catalog page, select a topic filter (e.g. Arrays, Strings, Algorithms).
  - Expected: The visible list contains only challenges of that topic and at least one entry remains.

- [X] FT-06: A challenge detail page opens from the catalog
  - Action: Click any challenge title in the filtered catalog list.
  - Expected: The challenge's detail page shows its problem statement, difficulty, topic, and the code editor area.

- [X] FT-07: User can solve a challenge and the site auto-runs it against the test cases
  - Action: Open a challenge, type a correct solution into the embedded code editor, click "Submit"/"Run".
  - Expected: The solution is executed against the predefined test cases automatically and the result shows "Passed" with a green/success indication.

- [ ] FT-08: An incorrect solution is reported as failed
  - Action: Open a challenge, type an incorrect or empty-behavior solution into the editor, click "Submit"/"Run".
  - Expected: The result shows "Failed"/"Wrong Answer" instead of "Passed", and no false success is reported.
  - Bug Report:
    - Issue: Missing failure verdict wording (no explicit failure label in the result UI)
    - Actual: The failing run renders a red `lucide-circle-x` icon and `border-destructive/50` styling, but the only verdict text produced is the heading `"Test Results: 2/3 passed"` and the toast `"2/3 tests passed"` — i.e. the word "passed" still appears in the failure verdict, and the strings "Failed"/"Wrong Answer" appear nowhere in the result markup. A user cannot read an explicit "Failed"/"Wrong Answer" verdict (source check of the compiled `ChallengeDetail.tsx` shows no "Failed"/"Wrong Answer" string in the component).

- [ ] FT-09: Personal dashboard shows the user's progress
  - Action: Log in and open the dashboard from the navigation.
  - Expected: The dashboard shows the user's challenge list, solved/unsolved state per challenge, and completion progress.
  - Bug Report:
    - Issue: Missing feature — no per-challenge list on the dashboard
    - Actual: The dashboard only renders aggregate widgets: "Total Points" (30), "Challenges Solved 3 / 10", "Submissions" (8), "Success Rate" (63%), "Progress by Difficulty" (Easy 3/5, Medium 0/4, Hard 0/1, Overall Progress 30%) and a "Recent Submissions" list limited to the 5 most recent entries. There is no list of the user's challenges with a solved/unsolved state per challenge (the per-challenge solved check-mark only appears on the /challenges catalog cards). Compiled `Dashboard.tsx` contains no iteration over the challenge catalog.

- [ ] FT-10: User can review past submissions
  - Action: Open the "Submissions"/"History" area of the dashboard and click one of the recorded submissions.
  - Expected: The submission's challenge, submitted code, timestamp, and its pass/fail verdict are displayed.
  - Bug Report:
    - Issue: Missing feature — submitted code is never displayed
    - Actual: The dashboard's "Recent Submissions" entries are links to `/challenge/:id` (not to a specific submission), and the challenge "History (n)" tab lists only a verdict string ("2/3 passed" / "3/3 passed") plus a date ("11/7/2026"); the history rows are not clickable and expand nothing. The submitted source code is stored in `localStorage.codeforge_submissions[].code` but is never rendered anywhere (the compiled `ChallengeDetail.tsx`/`Dashboard.tsx` contain no reference to a submission's `code` field).

- [X] FT-11: Dashboard shows challenges completed by difficulty
  - Action: Open the dashboard and locate the statistics section.
  - Expected: Statistics break down the number of challenges the user completed for each difficulty (e.g. Easy/Medium/Hard counts).

- [X] FT-12: Leaderboard ranks users by points from solved challenges
  - Action: Open the leaderboard page.
  - Expected: Users are listed in descending order of points earned from solved challenges, with each user's points value shown.

## Constraint

- [X] CS-01: Duplicate account registration is rejected
  - Action: Attempt to register using an email that already has an account.
  - Expected: Registration is refused with a clear "already registered"/duplicate error and no second account is created.

- [X] CS-02: Required registration fields are validated before account creation
  - Action: Submit the registration form with an empty email and/or empty password, and with an invalid email format.
  - Expected: The form is rejected with a field-level validation message and no account is created.

- [ ] CS-03: Dashboard, submissions, and submitting code require an authenticated session
  - Action: Log out, then attempt to open the dashboard, the submissions page, and a challenge's submit action directly.
  - Expected: Access is blocked or redirected to the login/registration page; no private data is shown.
  - Bug Report:
    - Issue: Inconsistent authentication enforcement — the submit action is not gated
    - Actual: The dashboard IS correctly protected (navigating to `/dashboard` while logged out redirects to `/login`, and the challenge History tab shows "History (0)" with no private data; no submission was recorded while logged out). However, the challenge submit action is not blocked or redirected: with no session, opening `/challenge/1`, entering a solution and clicking "Run Tests" executed the code and displayed a full verdict panel ("Test Results: 3/3 passed") to the anonymous visitor instead of redirecting to `/login`. Additionally there is no `/submissions` route at all (`/submissions` returns the 404 page), so the "Submissions" area exists only inside the protected dashboard.

- [X] CS-04: Points are awarded only for solved challenges and only once per challenge
  - Action: Submit a failing solution to a challenge, then submit a correct solution to the same challenge, then re-submit the correct solution.
  - Expected: The failing attempt awards no points, the first correct solution awards that challenge's points exactly once, and repeated correct submissions do not increase the points total.

## Interaction

- [X] IX-01: Verdict is shown automatically after the run completes without a manual page reload
  - Action: Submit a solution and watch the submit control and result area during execution.
  - Expected: The submit button shows a running/pending state while tests execute, and the Passed/Failed verdict replaces it automatically with no manual refresh.

- [X] IX-02: Dashboard and leaderboard reflect a newly solved challenge without manual refresh
  - Action: Solve a new challenge successfully, then navigate to the dashboard and the leaderboard.
  - Expected: The dashboard counts/statistics and the leaderboard points for the current user already include the newly solved challenge.

## Content

- [X] CT-01: Challenge detail page shows complete and relevant programming content
  - Action: Open any challenge detail page and read its description, difficulty label, topic label, and any example/test cases shown.
  - Expected: All fields are present, non-empty, and describe an actual programming problem of the stated topic/difficulty (no placeholder or lorem text).

- [ ] CT-02: Failure feedback identifies the failing case and the expected output
  - Action: Submit an incorrect solution to a challenge and read the feedback shown next to the failed result.
  - Expected: The feedback states that the submission failed, identifies which test case failed, and shows the expected versus actual output for that case.
  - Bug Report:
    - Issue: Failure feedback lacks an explicit failure statement and case identification
    - Actual: For the failing run the result panel shows the heading `"Test Results: 1/3 passed"` with a red `circle-x` icon, and three case blocks each containing `Input: … / Expected: … / Got: …`. The expected-vs-actual values are present, but no case is labelled or numbered as failed (cases are only distinguished by green `bg-success/10` vs red `bg-destructive/10` styling) and nothing in the feedback states in words that the submission failed — the only failure signal is the icon colour and the ratio in a string that still contains the word "passed".
