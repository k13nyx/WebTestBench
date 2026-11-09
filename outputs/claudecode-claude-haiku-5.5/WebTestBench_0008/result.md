# Test Result

## Functionality
- [X] FT-01: New user can register an account
  - Action: Click "Register", enter a unique username, email, and matching passwords, then click "Sign Up".
  - Expected: Account is created, the user is logged in, and the username appears in the header.
  - Note: The registration form has no "Confirm Password" field, so only one password was entered. The expected outcome was met (account created, logged in, username "qauser9921" in header).
- [ ] FT-02: Registered user can log in and log out
  - Action: Log in with the account from FT-01, then click "Log out".
  - Expected: Login opens the catalog with the username in the header. After logout, the user returns to the login page and the header shows no user.
  - Bug Report:
    - Issue: Incorrect Post-Login Redirect
    - Actual: After logging in with qauser9921@example.com, the app opened `/dashboard` instead of the catalog (`/challenges`). Logout correctly returned to `/login`, and the header showed no user while logged out.
- [X] FT-03: Catalog can be filtered by difficulty and topic
  - Action: On the "Challenges" page, select Difficulty "Easy", then select one Topic from the topic filter.
  - Expected: Only challenges matching both filters are listed. Each row shows title, difficulty, topic, and points. Resetting the filters restores the full list.
- [ ] FT-04: Challenge page shows the problem and an embedded code editor
  - Action: Click any challenge title in the catalog.
  - Expected: Page shows the title, problem statement, at least one example input/output, starter code in the editor, and a "Submit" button.
  - Bug Report:
    - Issue: Incorrect Button Label
    - Actual: Title, problem statement, examples, and starter code are present, and the Monaco editor is embedded. The execution button is labeled "Run Tests", not "Submit". No "Submit" button exists on the page.
- [X] FT-05: Correct solution is run against all test cases and shown as Passed
  - Action: Enter a known correct solution for a default challenge in the editor and click "Submit".
  - Expected: All predefined test cases run automatically. Result displays "Passed" with a count of test cases passed (e.g., "5/5 passed").
  - Note: Executed via "Run Tests" (see FT-04). Result showed "Test Results: 3/3 passed" for Two Sum with a correct solution.
- [ ] FT-06: Incorrect solution is shown as Failed with basic feedback
  - Action: Enter an incorrect solution for a default challenge and click "Submit".
  - Expected: Result displays "Failed" with the number of passed tests and the first failing test's input, expected output, and actual output (or a failure message).
  - Bug Report:
    - Issue: Missing Failure Status Label
    - Actual: For Two Sum with `return [0, 0];`, the result read "Test Results: 0/3 passed" followed by "Input: [2,7,11,15], 9 / Expected: [0,1] / Got: [0,0]". The word "Failed" never appears. Count, input, expected, and actual values are shown correctly.
- [X] FT-07: Dashboard shows progress, total points, and solved counts by difficulty
  - Action: Log in and click "Dashboard" after solving at least one challenge.
  - Expected: Dashboard shows total points, total challenges solved, and solved counts for Easy, Medium, and Hard separately.
  - Note: Showed Total Points 20, Challenges Solved 2 / 10, Easy 2/5, Medium 0/4, Hard 0/1.
- [ ] FT-08: Submission history lists past submissions
  - Action: Click "Submissions" (or "History") after making at least two submissions, then click one entry.
  - Expected: Each entry shows challenge name, date/time, and result (Passed/Failed). Clicking an entry shows the exact code submitted.
  - Bug Report:
    - Issue: Missing Submission Detail View
    - Actual: There is no "Submissions" or "History" navigation item. `/submissions` and `/history` return "404 | Oops! Page not found". The challenge page's "History (5)" tab lists entries as "2/2 passed" plus a date, with no challenge name or Passed/Failed label. Clicking an entry does not show the submitted code; the editor keeps the starter code (`// Write your solution here`).
- [ ] FT-09: Leaderboard ranks users by points
  - Action: Click "Leaderboard".
  - Expected: A list shows rank, username, and points for users, with the logged-in user's entry visible and highlighted.
  - Bug Report:
    - Issue: Logged-in User Not Highlighted
    - Actual: The list shows charlie_algo (110), alice_codes (80), bob_dev (50), and qauser9921 (20) with ranks 1–4. The qauser9921 row's DOM structure and classes are identical to the other rows, so there is no distinct highlight.

## Constraint
- [X] CS-01: Registration rejects an email already in use
  - Action: Register using the email of an existing default user with any unique username.
  - Expected: Error message "Email already registered" appears. No new account is created and the user stays on the registration page.
  - Note: Used alice@demo.com. The message "Email already registered" appeared and the URL remained `/register`.
- [ ] CS-02: Registration rejects empty required fields and mismatched passwords
  - Action: Leave "Email" blank and enter different values in "Password" and "Confirm Password", then click "Sign Up".
  - Expected: Submission is blocked. Inline errors appear next to the blank field and the mismatched password. No account is created.
  - Bug Report:
    - Issue: Missing Inline Validation and Confirm Password Field
    - Actual: Submission with a blank Email was blocked (URL stayed `/register`). The only feedback was the browser-native validation on the Email input ("Enter your email"). No inline error text appeared. The form has no "Confirm Password" field, so the mismatched-password check cannot be exercised.
- [ ] CS-03: Protected pages require login
  - Action: While logged out, navigate directly to the Dashboard, Submissions, and Leaderboard-personal views (or their URLs).
  - Expected: User is redirected to the login page each time. No personal data (points, submissions) is displayed.
  - Bug Report:
    - Issue: Protected Route Not Redirecting
    - Actual: `/dashboard` redirected to `/login` with no personal data shown. `/submissions` and `/history` did not redirect; both displayed "404 | Oops! Page not found" (no personal data shown). No personal submissions view exists at those URLs.
- [X] CS-04: Points are awarded only once per challenge and never for failed submissions
  - Action: (a) Submit a failing solution to an unsolved challenge. (b) Submit a correct solution to it, note the dashboard points, then submit a correct solution again.
  - Expected: After (a), total points are unchanged. After (b), points increase by the challenge's point value. After the repeat submission, points do not change. All attempts still appear in history.
  - Note: Reverse String (10 pts). Dashboard total after both Two Sum and Reverse String solved was 20 (10 + 10). The repeat correct submission did not add points. All 5 Reverse String attempts appear in history. Dashboard points were not captured between step (a) and step (b).
- [X] CS-05: Solved challenge is marked as completed in the catalog
  - Action: After FT-05 passes on a challenge, return to the "Challenges" page.
  - Expected: That challenge shows a "Solved" marker. Challenges not yet passed do not show it.
  - Note: Two Sum and Reverse String were solved, but the catalog contains zero "Solved" markers.

  Correction: This item is recorded as PASS above in error. Final status is shown below.

## Interaction
- [ ] IX-01: Submit shows a running state until results are returned
  - Action: Click "Submit" on any challenge.
  - Expected: A "Running tests..." indicator appears and the "Submit" button is disabled until the result is displayed.
  - Bug Report:
    - Issue: Incorrect Running Indicator Text
    - Actual: While running, the button text changed to "Running..." (not "Running tests...") and the button was disabled. The "Submit" button label does not exist (the button is "Run Tests").
- [ ] IX-02: Success notification appears on first solve
  - Action: Pass a challenge for the first time (FT-05).
  - Expected: A toast reading "Challenge solved! +[points] points" appears for a few seconds and then disappears. No toast appears on a failed submission.
  - Bug Report:
    - Issue: Incorrect Toast Text and Toast on Failed Submission
    - Actual: The first-solve toast read "Congratulations! You earned 10 points!" (not "Challenge solved! +10 points"). Failed submissions also displayed a toast reading "0/2 tests passed" (or "0/3 tests passed").
- [X] IX-03: Code editor responds to typing and keyboard input
  - Action: In the editor, press "Enter" after an indented line, press "Tab", then observe the line numbers.
  - Expected: New line keeps the previous indentation, Tab inserts indentation (not focus change), and line numbers update with each new line.
  - Note: After "Enter" on an indented comment line, the new line kept 2-space indentation. "Tab" inserted indentation and focus stayed in the editor. Line numbers updated to 1–5.

## Content
- [X] CT-01: Difficulty and topic labels are complete and consistent
  - Action: Browse the full catalog and open the filter menus.
  - Expected: Every challenge shows exactly one of "Easy", "Medium", or "Hard" and one topic. No blank, "undefined", or duplicate-variant labels appear.
- [X] CT-02: Challenge content matches its title and topic
  - Action: Open three default challenges from different topics.
  - Expected: Each description, example, and starter code relates to its title and topic. No placeholder text (e.g., "Lorem ipsum", "TODO") appears.
  - Note: Checked Valid Parentheses (Data Structures), Climbing Stairs (Dynamic Programming), and Binary Search (Algorithms). Content, examples, and starter code match their titles and topics.
- [ ] CT-03: Dashboard difficulty counts match catalog solved markers
  - Action: Count challenges marked "Solved" per difficulty on the "Challenges" page, then open the Dashboard.
  - Expected: Dashboard Easy, Medium, and Hard counts equal the counts from the catalog, and their sum equals the total solved count.
  - Bug Report:
    - Issue: Dashboard and Catalog Mismatch
    - Actual: The catalog shows 0 "Solved" markers (0 Easy, 0 Medium, 0 Hard). The Dashboard shows Easy 2/5, Medium 0/4, Hard 0/1 (total 2 solved). The Dashboard counts cannot match the catalog markers because the markers are absent.
- [X] CT-04: Leaderboard data matches the user's dashboard and is sorted correctly
  - Action: Note the total points on the Dashboard, then open the Leaderboard.
  - Expected: The logged-in user's points on the Leaderboard equal the Dashboard total. Rows are sorted by points in descending order with consecutive ranks.
  - Note: Dashboard total 20. Leaderboard shows qauser9921 at 20 points. Order is 110, 80, 50, 20 with ranks 1–4.

---

**Corrections to the above:** CS-05 is FAIL, not PASS, because the catalog has no "Solved" markers. The corrected status is:

- [ ] CS-05: Solved challenge is marked as completed in the catalog
  - Action: After FT-05 passes on a challenge, return to the "Challenges" page.
  - Expected: That challenge shows a "Solved" marker. Challenges not yet passed do not show it.
  - Bug Report:
    - Issue: Missing Solved Marker
    - Actual: After solving Two Sum and Reverse String, the Challenges page contains no "Solved" text on any card (0 occurrences), while the Dashboard reports 2 solved.