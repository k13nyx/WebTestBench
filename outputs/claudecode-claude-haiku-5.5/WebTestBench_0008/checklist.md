# Test Checklist

## Functionality
- [ ] FT-01: New user can register an account
  - Action: Click "Register", enter a unique username, email, and matching passwords, then click "Sign Up".
  - Expected: Account is created, the user is logged in, and the username appears in the header.
- [ ] FT-02: Registered user can log in and log out
  - Action: Log in with the account from FT-01, then click "Log out".
  - Expected: Login opens the catalog with the username in the header. After logout, the user returns to the login page and the header shows no user.
- [ ] FT-03: Catalog can be filtered by difficulty and topic
  - Action: On the "Challenges" page, select Difficulty "Easy", then select one Topic from the topic filter.
  - Expected: Only challenges matching both filters are listed. Each row shows title, difficulty, topic, and points. Resetting the filters restores the full list.
- [ ] FT-04: Challenge page shows the problem and an embedded code editor
  - Action: Click any challenge title in the catalog.
  - Expected: Page shows the title, problem statement, at least one example input/output, starter code in the editor, and a "Submit" button.
- [ ] FT-05: Correct solution is run against all test cases and shown as Passed
  - Action: Enter a known correct solution for a default challenge in the editor and click "Submit".
  - Expected: All predefined test cases run automatically. Result displays "Passed" with a count of test cases passed (e.g., "5/5 passed").
- [ ] FT-06: Incorrect solution is shown as Failed with basic feedback
  - Action: Enter an incorrect solution for a default challenge and click "Submit".
  - Expected: Result displays "Failed" with the number of passed tests and the first failing test's input, expected output, and actual output (or a failure message).
- [ ] FT-07: Dashboard shows progress, total points, and solved counts by difficulty
  - Action: Log in and click "Dashboard" after solving at least one challenge.
  - Expected: Dashboard shows total points, total challenges solved, and solved counts for Easy, Medium, and Hard separately.
- [ ] FT-08: Submission history lists past submissions
  - Action: Click "Submissions" (or "History") after making at least two submissions, then click one entry.
  - Expected: Each entry shows challenge name, date/time, and result (Passed/Failed). Clicking an entry shows the exact code submitted.
- [ ] FT-09: Leaderboard ranks users by points
  - Action: Click "Leaderboard".
  - Expected: A list shows rank, username, and points for users, with the logged-in user's entry visible and highlighted.

## Constraint
- [ ] CS-01: Registration rejects an email already in use
  - Action: Register using the email of an existing default user with any unique username.
  - Expected: Error message "Email already registered" appears. No new account is created and the user stays on the registration page.
- [ ] CS-02: Registration rejects empty required fields and mismatched passwords
  - Action: Leave "Email" blank and enter different values in "Password" and "Confirm Password", then click "Sign Up".
  - Expected: Submission is blocked. Inline errors appear next to the blank field and the mismatched password. No account is created.
- [ ] CS-03: Protected pages require login
  - Action: While logged out, navigate directly to the Dashboard, Submissions, and Leaderboard-personal views (or their URLs).
  - Expected: User is redirected to the login page each time. No personal data (points, submissions) is displayed.
- [ ] CS-04: Points are awarded only once per challenge and never for failed submissions
  - Action: (a) Submit a failing solution to an unsolved challenge. (b) Submit a correct solution to it, note the dashboard points, then submit a correct solution again.
  - Expected: After (a), total points are unchanged. After (b), points increase by the challenge's point value. After the repeat submission, points do not change. All attempts still appear in history.
- [ ] CS-05: Solved challenge is marked as completed in the catalog
  - Action: After FT-05 passes on a challenge, return to the "Challenges" page.
  - Expected: That challenge shows a "Solved" marker. Challenges not yet passed do not show it.

## Interaction
- [ ] IX-01: Submit shows a running state until results are returned
  - Action: Click "Submit" on any challenge.
  - Expected: A "Running tests..." indicator appears and the "Submit" button is disabled until the result is displayed.
- [ ] IX-02: Success notification appears on first solve
  - Action: Pass a challenge for the first time (FT-05).
  - Expected: A toast reading "Challenge solved! +[points] points" appears for a few seconds and then disappears. No toast appears on a failed submission.
- [ ] IX-03: Code editor responds to typing and keyboard input
  - Action: In the editor, press "Enter" after an indented line, press "Tab", then observe the line numbers.
  - Expected: New line keeps the previous indentation, Tab inserts indentation (not focus change), and line numbers update with each new line.

## Content
- [ ] CT-01: Difficulty and topic labels are complete and consistent
  - Action: Browse the full catalog and open the filter menus.
  - Expected: Every challenge shows exactly one of "Easy", "Medium", or "Hard" and one topic. No blank, "undefined", or duplicate-variant labels appear.
- [ ] CT-02: Challenge content matches its title and topic
  - Action: Open three default challenges from different topics.
  - Expected: Each description, example, and starter code relates to its title and topic. No placeholder text (e.g., "Lorem ipsum", "TODO") appears.
- [ ] CT-03: Dashboard difficulty counts match catalog solved markers
  - Action: Count challenges marked "Solved" per difficulty on the "Challenges" page, then open the Dashboard.
  - Expected: Dashboard Easy, Medium, and Hard counts equal the counts from the catalog, and their sum equals the total solved count.
- [ ] CT-04: Leaderboard data matches the user's dashboard and is sorted correctly
  - Action: Note the total points on the Dashboard, then open the Leaderboard.
  - Expected: The logged-in user's points on the Leaderboard equal the Dashboard total. Rows are sorted by points in descending order with consecutive ranks.