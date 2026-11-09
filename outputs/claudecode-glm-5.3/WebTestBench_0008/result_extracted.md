# Test Result

## Functionality
- [X] FT-01: User can register a new account
  - Action: Navigate to the registration page, fill in username, email, and password with valid values, and click the "Register" (or "Sign Up") button.
  - Expected: Account is created, the user is logged in (or redirected to login), and subsequent login with the same credentials succeeds.
  - Verified: Registered `qa_tester_01` / `qa_tester_01@test.com`; auto-logged-in and redirected to `/dashboard` with toast "Welcome to CodeForge, qa_tester_01!". After logout, logging in with the same credentials succeeded ("Welcome back, qa_tester_01!" on /dashboard).

- [X] FT-02: Challenge catalog displays predefined challenges
  - Action: Open the challenge catalog page.
  - Expected: A list of pre-existing programming challenges is displayed, each showing at least a title, difficulty level, and topic.
  - Verified: `/challenges` shows 10 pre-existing challenges ("10 challenges" counter); every card shows title (e.g., Two Sum, Binary Search), difficulty chip (easy/medium/hard), topic chip (arrays, strings, algorithms, data structures, dynamic programming, recursion), plus test-case count and points.

- [X] FT-03: Catalog can be filtered by difficulty
  - Action: On the catalog page, apply a difficulty filter (e.g., "Easy").
  - Expected: Only challenges with the selected difficulty are shown; all displayed challenges are labeled with that difficulty.
  - Verified: Clicking the "easy" filter shows "5 challenges"; all 5 displayed (Two Sum, Reverse String, Valid Palindrome, Climbing Stairs, Fibonacci Number) are labeled "easy".

- [X] FT-04: Catalog can be filtered by topic
  - Action: On the catalog page, apply a topic filter (e.g., "Arrays").
  - Expected: Only challenges belonging to the selected topic are shown.
  - Verified: Clicking the "arrays" topic filter shows "2 challenges" — Two Sum and Merge Sorted Array — both labeled "arrays"; no other topics appear.

- [X] FT-05: Challenge detail page shows description and embedded code editor
  - Action: Click any challenge title in the catalog.
  - Expected: A detail page opens showing the challenge description, the predefined test cases (or their count), and an embedded code editor ready for input.
  - Verified: `/challenge/1` (Two Sum) shows full description, "Examples" with predefined test cases as Input → Output pairs (e.g., `[2,7,11,15], 9` → `[0,1]`), points (10 pts), and a Monaco JS editor pre-loaded with a `function twoSum(nums, target)` template, ready for input. Full predefined test list (3 cases) renders in the Test Results panel when run.

- [X] FT-06: User can submit a correct solution that passes all test cases
  - Action: Open a default challenge, type a known-correct solution into the embedded editor, and click "Submit".
  - Expected: The system runs the solution against the predefined test cases and displays a "Passed" (accepted) result.
  - Verified: Typed a correct hash-map Two Sum solution and clicked "Run Tests" → "Test Results: 3/3 passed" with all 3 predefined cases green (Got: [0,1], [1,2], [0,1]) and toast "Congratulations! You earned 10 points!".

- [X] FT-07: User can submit an incorrect solution that fails test cases
  - Action: Open a default challenge, type a known-wrong solution (e.g., returns a wrong value), and click "Submit".
  - Expected: The system displays a "Failed" result indicating the solution did not pass the test cases, with basic feedback (e.g., which test case failed or expected vs. actual output).
  - Verified: Typed `return [99, 99]` solution → "Test Results: 0/3 passed" with per-test feedback: Input `[2,7,11,15], 9` / Expected `[0,1]` / Got `[99,99]` (same pattern for all 3 cases).

- [X] FT-08: Dashboard tracks progress after solving a challenge
  - Action: Solve one default challenge successfully, then open the personal dashboard.
  - Expected: The dashboard reflects the newly solved challenge in progress stats (e.g., solved count or completion percentage increases).
  - Verified: Baseline before solving: Points 0, Solved 0/10, Submissions 0, 0%. After solving Two Sum: Total Points **10**, Challenges Solved **1/10**, Submissions **3**, Success Rate **33%**, Overall Progress 10%.

- [X] FT-09: Dashboard shows statistics of challenges completed by difficulty
  - Action: Open the personal dashboard.
  - Expected: A breakdown of solved challenges per difficulty level (e.g., Easy / Medium / Hard counts) is displayed and matches the user's actual solved challenges.
  - Verified: "Progress by Difficulty" section shows Easy **1/5**, Medium **0/4**, Hard **0/1** — exactly matches my actual solves (one easy challenge, Two Sum).

- [X] FT-10: User can review past submissions
  - Action: Open the submissions (submission history) page after having made at least one submission.
  - Expected: A list of past submissions is shown, each including at least the challenge name, submission time, and pass/fail result.
  - Verified: Dashboard "Recent Submissions" lists all 3 of my submissions, each with challenge name ("Two Sum"), time (11/8/2026), and result (✕ fail ×2, ✓ +10 pts pass). The per-challenge "History (3)" tab on `/challenge/1` also lists each run's result ("0/3 passed", "3/3 passed", "0/3 passed") with dates.

- [X] FT-11: Leaderboard ranks users by earned points
  - Action: Open the leaderboard page after solving at least one challenge.
  - Expected: Users are listed with their earned points and ranked in descending order of points; the current user appears with points consistent with their solved challenges.
  - Verified: Leaderboard shows #1 charlie_algo (110 pts, 7 solved), #2 alice_codes (80 pts, 5 solved), #3 bob_dev (50 pts, 3 solved), #4 qa_tester_01 (**10 pts, 1 solved**) — descending order, and my 10 points exactly match my single 10-pt easy solve.

## Constraint
- [X] CS-01: Registration cannot submit with empty required fields
  - Action: On the registration page, leave one or more required fields (username/email/password) empty and click "Register".
  - Expected: The account is not created and a validation message identifies the missing required fields.
  - Verified: Clicking "Create Account" with all fields empty blocked submission — all three inputs carry `required` constraint, browser validation moved focus to the first missing field (Username) identifying it, no account was created, and the page stayed on `/register` with the form unchanged.

- [X] CS-02: Registration rejects duplicate credentials
  - Action: Attempt to register a new account using the username or email of an existing default user.
  - Expected: Registration is rejected with an error message indicating the username or email is already taken.
  - Verified: Attempted registration with email `alice@demo.com` (a listed demo account) → rejected with error notification "Email already registered"; stayed on `/register`, no account created.

- [ ] CS-03: Code submission cannot be empty
  - Action: Open a challenge, leave the embedded editor empty, and click "Submit".
  - Expected: The submission is not executed and a message prompts the user to enter code before submitting.
  - Bug Report:
    - Issue: Missing empty-code validation on submission
    - Actual: With the editor fully cleared (empty model), clicking "Run Tests" executed the submission anyway: a "0/3 tests passed" toast appeared, the run was evaluated against all 3 predefined test cases with "Got: Error: solution is not defined", and the submission was recorded in history (History count incremented 0 → 1). No message prompted the user to enter code before submitting.

- [X] CS-04: Unauthenticated user cannot access personal pages
  - Action: While logged out, attempt to access the personal dashboard or submission history (e.g., by URL or navigation link).
  - Expected: Access is denied and the user is redirected to the login/registration page.
  - Verified: While logged out, navigating directly to `http://localhost:6008/dashboard` redirected to `/login` — the login form ("Welcome Back") was displayed instead of any personal data.

## Interaction
- [X] IX-01: Submission result feedback appears after automatic test run
  - Action: Submit any solution from the challenge editor.
  - Expected: The page shows a running/evaluating state and then updates in place with the pass/fail outcome and basic feedback, without requiring a manual page reload.
  - Verified: On clicking Run Tests the button label changed from "Run Tests" to **"Running..."** (evaluating state, sampled immediately after click), then the "Test Results" panel rendered in place below the editor on the same URL (`/challenge/1`, no reload) with the outcome ("Test Results: 3/3 passed" / "Test Results: 0/3 passed") and per-test Input/Expected/Got feedback, plus a toast notification.

- [X] IX-02: Leaderboard updates after a challenge is solved
  - Action: Solve a default challenge successfully, then navigate to the leaderboard.
  - Expected: The current user's points and rank on the leaderboard increase to reflect the newly solved challenge.
  - Verified: Baseline before solving showed qa_tester_01 at 0 points / 0 challenges solved. After solving Two Sum (+10 pts), the leaderboard entry updated to **10 points / 1 challenges solved**. Rank remained #4, which is correct since all other listed users (110/80/50 pts) still out-score a single 10-pt solve; points updated to reflect the newly solved challenge.

## Content
- [X] CT-01: Challenge content is relevant to programming topics
  - Action: Browse the catalog and open at least two different challenges.
  - Expected: Each challenge's title, description, and test cases are clearly a programming task consistent with its labeled topic and difficulty (no off-theme or placeholder content).
  - Verified: Opened multiple challenges — Two Sum (arrays/easy: return index pair summing to target, tests `[2,7,11,15], 9 → [0,1]`), Climbing Stairs (dynamic programming/easy: count distinct ways climbing 1-or-2 steps, tests `n=2 → 2`, `n=3 → 3`), Longest Common Subsequence (dynamic programming/hard: LCS length of two strings, tests `"abcde","ace" → 3`). All titles, descriptions, and test cases are genuine, coherent programming tasks matching their labeled topic/difficulty; no placeholder content found.

- [X] CT-02: Difficulty labels on challenges are valid values
  - Action: Inspect all challenges in the catalog and on their detail pages.
  - Expected: Every challenge displays exactly one difficulty from the expected set (e.g., Easy, Medium, Hard) — no missing, misspelled, or contradictory labels.
  - Verified: Catalog: all 10 challenges show exactly one valid difficulty — easy (Two Sum, Reverse String, Valid Palindrome, Climbing Stairs, Fibonacci Number), medium (Maximum Subarray, Binary Search, Valid Parentheses, Merge Sorted Array), hard (Longest Common Subsequence); counter "10 challenges" matches. Detail pages: programmatically inspected all 10 (`/challenge/1`–`/challenge/10`) — each shows exactly one difficulty chip matching the catalog value (5 easy, 4 medium, 1 hard), no missing/misspelled/contradictory labels.
