All checklist items have been executed and verified. Here is the complete report.

# Test Result

## Functionality
- [X] FT-01: New user can register an account
  - Action: Navigate to registration page and submit valid username, email, and password
  - Expected: Account is created and user is redirected to a logged-in state
- [X] FT-02: User can browse the programming challenge catalog
  - Action: Navigate to the challenges catalog page
  - Expected: A list of available programming challenges is displayed
- [X] FT-03: User can filter the challenge list by difficulty
  - Action: Select a difficulty level (e.g., Easy, Medium, Hard) from a filter control
  - Expected: The displayed challenge list updates to show only challenges of the selected difficulty
- [X] FT-04: User can filter the challenge list by topic
  - Action: Select a topic (e.g., Arrays, Strings, Algorithms) from a filter control
  - Expected: The displayed challenge list updates to show only challenges tagged with the selected topic
- [X] FT-05: User can open a challenge and view its description
  - Action: Click on a challenge from the catalog
  - Expected: A challenge detail view is shown with description, requirements, and an embedded code editor
- [X] FT-06: User can write code in the embedded editor
  - Action: Click inside the code editor and type code
  - Expected: The text appears in the editor as typed
- [X] FT-07: User can submit a code solution
  - Action: Write code in the editor and click the Submit button
  - Expected: The system accepts the submission and runs it against the test cases
- [X] FT-08: System shows pass/fail status for each test case
  - Action: Submit a solution and wait for evaluation
  - Expected: A result is displayed showing which test cases passed and which failed
- [X] FT-09: User can review their past submissions
  - Action: Navigate to the submissions history section
  - Expected: A list of previous submissions is shown with challenge name, date, and result
- [X] FT-10: User can view their personal dashboard
  - Action: Navigate to the personal dashboard
  - Expected: Dashboard is shown displaying the user's progress information
- [X] FT-11: Dashboard shows statistics of challenges completed by difficulty
  - Action: View the personal dashboard
  - Expected: A breakdown of completed challenges grouped by difficulty level (Easy, Medium, Hard) is visible
- [X] FT-12: User can view the leaderboard
  - Action: Navigate to the leaderboard page
  - Expected: A ranking of users with their points earned from solved challenges is displayed

## Constraint
- [X] CS-01: Registration is rejected when mandatory fields are missing
  - Action: Submit the registration form with one or more required fields left blank
  - Expected: The form is not submitted and an error message indicates which fields are required
- [ ] CS-02: Empty code cannot be submitted
  - Action: Leave the code editor empty and click the Submit button
  - Expected: Submission is blocked and a message indicates code must be provided
  - Bug Report:
    - Issue: Missing Input Validation (empty submission accepted)
    - Actual: With the editor completely empty, clicking "Run Tests" was **not** blocked. The request was accepted, a submission record was created (the challenge's "History" tab incremented from `History (0)` to `History (1)`), and the evaluation ran, showing the toast "0/3 tests passed" with per-case output `Got: Error: solution is not defined`. No message stating that code must be provided was ever displayed.
- [X] CS-03: Dashboard and submissions are only accessible to logged-in users
  - Action: Log out and try to navigate directly to the dashboard or submissions page
  - Expected: Access is denied and the user is redirected to the login or registration page
- [X] CS-04: Leaderboard only counts fully solved challenges
  - Action: Review the leaderboard ranking after solving only some test cases of a challenge
  - Expected: Partially passed challenges do not contribute points; only fully solved challenges count

## Interaction
- [X] IX-01: Dashboard updates after solving a new challenge
  - Action: Solve a challenge successfully, then revisit the personal dashboard
  - Expected: The progress and difficulty statistics reflect the newly completed challenge
- [X] IX-02: Applying a filter updates the displayed challenge list
  - Action: Change the difficulty or topic filter after a list is shown
  - Expected: The list reloads immediately to show only challenges matching the new filter
- [X] IX-03: Submission result appears after evaluation completes
  - Action: Submit a code solution
  - Expected: A visible status indicator (e.g., loading then pass/fail result) is shown without requiring a page refresh

## Content
- [X] CT-01: Feedback identifies which test case failed when a solution is incorrect
  - Action: Submit an incorrect solution that passes some tests but fails others
  - Expected: The feedback output specifies which test case(s) failed and shows relevant input/expected values
- [X] CT-02: Challenges in the catalog are clearly labeled by difficulty and topic
  - Action: View the challenge catalog
  - Expected: Each challenge entry visibly displays its difficulty level and topic category

---

### Evidence summary

| Item | Key observation |
|---|---|
| FT-01 | Redirected to `/dashboard`, toast "Welcome to CodeForge, testuser!", nav shows logged-in menu |
| FT-02 | `/challenges` → "10 challenges", 10 cards |
| FT-03 | `easy` → "5 challenges" (all easy); `hard` → "1 challenge"; active button gets `bg-primary` |
| FT-04 | `arrays` → "1 challenge"; `strings` → "0 challenges" combined with `hard` |
| FT-05 | Detail view: description, Examples section, difficulty/topic/pts badges, Monaco editor, "Run Tests" |
| FT-06 | `page.keyboard.type` into Monaco produced `function twoSum(nums, target) {...}` in editor DOM |
| FT-07/08 | "Test Results: 3/3 passed" with per-case `Input` / `Expected` / `Got`; toast "Congratulations! You earned 10 points!" |
| FT-09 | Dashboard "Recent Submissions": `✓ Two Sum 11/7/2026 +10 pts`, `✕ Reverse String 11/7/2026`; per-challenge "History (N)" tab shows `3/3 passed` |
| FT-10/11 | Total Points 10, Solved 1/10, Submissions 2, Success Rate 50%; Easy 1/5, Medium 0/4, Hard 0/1 |
| FT-12 | Leaderboard: charlie_algo 110, alice_codes 80, bob_dev 50, testuser 10 pts (rank 4) |
| CS-01 | `input.required === true`; after submit URL stayed `/register`, no account created, focus moved to first invalid field (native browser validation bubble) |
| CS-03 | Logged out → `/dashboard` redirected to `/login` (URL `http://localhost:6008/login`) |
| CS-04 | After 1/2 pass on Reverse String, leaderboard still showed testuser = 10 pts, 1 challenge solved |
| IX-02 | Filter clicks changed counts with `framenavigated` never firing and URL unchanged (no reload) |
| CT-01 | "Test Results: 1/2 passed" — case 2 showed `Expected: ["h","a","n","n","a","H"]` vs `Got: ["H","a","n","n","a","h"]` |
| CT-02 | All 10 cards contain both a difficulty badge and a topic badge |

**Notable findings beyond the checklist:** there is no dedicated submissions route (`/submissions` returns 404); submission history is exposed via the dashboard's "Recent Submissions" panel and the per-challenge "History" tab. The submit control is labelled **"Run Tests"** rather than "Submit". The only genuine defect found is **CS-02** — the editor accepts and evaluates empty code instead of blocking it with a "code required" message.