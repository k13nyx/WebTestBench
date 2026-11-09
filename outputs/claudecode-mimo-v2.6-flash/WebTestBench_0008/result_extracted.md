# Test Result

## Functionality
- [X] FT-01: Register a new user account
  - Action: Navigate to registration, enter a unique username, valid email, and password, then submit.
  - Expected: Account is created and the user is signed in (navigation shows the new username or a logged-in state).
  - Actual: Submitted username `qa_tester_1`, `qa_tester_1@example.com`, password; redirected to `/dashboard`, toast "Welcome to CodeForge, qa_tester_1!", nav shows button "qa_tester_1".

- [X] FT-02: Log in with registered credentials
  - Action: Log out, then log in using the registered username and password.
  - Expected: Login succeeds and the user is taken to the authenticated view.
  - Actual: Logged out via user menu → `/login`; signed in with registered email + password (`qa_tester_1` is blocked by native email validation since the field is typed as email); landed on `/dashboard` with "Welcome back, qa_tester_1!" and username in nav.

- [X] FT-03: Browse the challenge catalog
  - Action: Open the catalog page using default data.
  - Expected: A list of challenges is displayed, each showing its title, difficulty, and topic.
  - Actual: `/challenges` shows "10 challenges"; each card has title (e.g., "Two Sum"), difficulty label (e.g., "easy") and topic label (e.g., "arrays").

- [X] FT-04: Filter catalog by difficulty
  - Action: Select a difficulty filter (e.g., "Easy") in the catalog.
  - Expected: Only challenges of that difficulty are listed.
  - Actual: Clicked "easy" → count changed to "5 challenges"; remaining cards: Two Sum, Reverse String, Valid Palindrome, Climbing Stairs, Fibonacci Number (all easy). Toggling off restored 10.

- [X] FT-05: Filter catalog by topic
  - Action: Select a topic filter (e.g., "Arrays") in the catalog.
  - Expected: Only challenges belonging to that topic are listed.
  - Actual: With easy filter cleared, clicked "arrays" → "2 challenges": Two Sum (arrays) and Merge Sorted Array (arrays).

- [X] FT-06: Open a challenge and view its details
  - Action: Click a challenge title in the catalog.
  - Expected: The challenge page shows the problem description, difficulty, topic, and an embedded code editor.
  - Actual: `/challenge/1` shows heading "Two Sum", labels "easy"/"arrays"/"10 pts", Description tab with full problem statement + Examples, and a Monaco editor with starter code `function twoSum(nums, target) {...}`.

- [X] FT-07: Submit a correct solution and receive a pass result
  - Action: Enter a correct solution in the editor for a challenge and click the submit button.
  - Expected: Test cases run and the result indicates the solution passed, with basic feedback shown.
  - Actual: Entered hash-map solution, clicked "Run Tests" → "Test Results: 3/3 passed" with per-case feedback (Input / Expected: [0,1] / Got: [0,1], etc.).

- [X] FT-08: Submit an incorrect solution and receive a fail result
  - Action: Enter a deliberately wrong solution for a challenge and submit it.
  - Expected: Test cases run and the result indicates the solution failed, with basic feedback shown.
  - Actual: Entered `return [0,0];` → "Test Results: 0/3 passed" with feedback "Expected: [0,1] / Got: [0,0]" for each case.

- [X] FT-09: View personal dashboard with progress
  - Action: Open the dashboard page after registering/solving.
  - Expected: The dashboard shows the user's progress, including challenges completed broken down by difficulty.
  - Actual: `/dashboard` shows "Welcome back, qa_tester_1!", Total Points 10, Challenges Solved 1/10, Submissions 4, Success Rate 50%, "Progress by Difficulty": Easy 1/5, Medium 0/4, Hard 0/1, Overall 10%.

- [X] FT-10: Review past submissions
  - Action: Open the submissions/history section of the dashboard.
  - Expected: A list of the user's previous submissions appears with challenge name, result (passed/failed), and submission time.
  - Actual: "Recent Submissions" lists all 4 entries: "Two Sum" with green check icon (`lucide-circle-check-big text-success`) for passes, red "✕" in `bg-destructive/20` circle for failures, each with timestamp "11/9/2026" (and "+10 pts" on the scoring pass). Result is conveyed by distinct pass/fail iconography rather than explicit "Passed/Failed" text.

- [X] FT-11: View the leaderboard
  - Action: Open the leaderboard page.
  - Expected: Users are listed with their points, ordered so higher-scoring users rank higher.
  - Actual: `/leaderboard` "Rankings": 1. charlie_algo 110 pts (7 solved), 2. alice_codes 80 (5), 3. bob_dev 50 (3), 4. qa_tester_1 10 (1), 5–6. qa_tester_1 0 (0) — strictly descending points.

## Constraint
- [ ] CS-01: Registration rejects duplicate username
  - Action: Attempt to register with an existing username from default/created accounts.
  - Expected: Registration is blocked and an error message about the username being taken is shown.
  - Bug Report:
    - Issue: Duplicate Username Accepted (no validation error)
    - Actual: Registering with the existing username `qa_tester_1` (tried both while logged in and while logged out, with fresh emails `dup_check@example.com` / `dup_check2@example.com`) was not blocked — the form submitted and redirected to `/dashboard` with the toast "Welcome to CodeForge, qa_tester_1!". No error message appeared; the leaderboard now contains three separate `qa_tester_1` accounts, confirming duplicates were created.

- [X] CS-02: Registration rejects empty required fields
  - Action: Submit the registration form with one or more required fields empty.
  - Expected: The form is not submitted and an error is shown for the empty field(s).
  - Actual: Clicking "Create Account" with all fields empty stayed on `/register`; all three inputs are `required` with validity error "Please fill out this field." and the first invalid field was focused. With username+email filled and password empty, submission was again blocked and the Password field focused with its own validation error.

- [ ] CS-03: Login rejects invalid credentials
  - Action: Attempt to log in with a wrong password for an existing username.
  - Expected: Login fails and an error message is displayed; the user remains logged out.
  - Bug Report:
    - Issue: Authentication Bypass / Invalid Credentials Accepted
    - Actual: Entered existing email `qa_tester_1@example.com` with wrong password `WrongPass999` (registered password was `TestPass123!`) and clicked Sign In — login succeeded and navigated to `/dashboard` with "Welcome back, qa_tester_1!". No error was displayed and the user was NOT kept logged out.

- [X] CS-04: Protected pages are inaccessible when logged out
  - Action: While logged out, attempt to open the dashboard or submissions page.
  - Expected: Access is denied (redirect to login or explicit message); private data is not shown.
  - Actual: While logged out, navigating directly to `http://localhost:6008/dashboard` redirected to `/login` ("Welcome Back / Sign in to continue your coding journey"); no private data rendered.

- [X] CS-05: Points are awarded only once per solved challenge
  - Action: Submit a correct solution for a challenge already solved by the same user, then check the leaderboard score.
  - Expected: The user's total points do not increase for re-solving the same challenge.
  - Actual: Two Sum (easy, +10 pts) was solved correctly twice (two "3/3 passed" submissions); dashboard shows Total Points **10** and leaderboard row shows **10 points / 1 challenges solved** — no double award.

## Interaction
- [X] IX-01: Submission provides immediate processing feedback
  - Action: Click the submit button with code in the editor.
  - Expected: The UI indicates the solution is being judged (e.g., loading/running state) and then transitions to displaying the pass/fail result without a page reload.
  - Actual: On clicking "Run Tests", the button immediately changed to "Running..." and became `disabled` for ~400–500ms, then reverted to "Run Tests" as the result panel rendered — all within the SPA at the unchanged URL `/challenge/1` (no reload/navigation).

- [X] IX-02: Result view distinguishes pass from fail visually
  - Action: Submit a correct solution, then an incorrect solution.
  - Expected: Each result is clearly shown as passed or failed with distinct visual indication (e.g., color/label) and the associated test-case feedback.
  - Actual: Pass state: heading "Test Results: 3/3 passed", card class `border-success/50` (green, `rgba(26,188,85,0.5)`). Fail state: heading "Test Results: 0/3 passed", card class `border-destructive/50` (red, `rgba(223,58,58,0.5)`). Both show per-case Input/Expected/Got feedback.

## Content
- [X] CT-01: Challenge catalog content is complete and relevant
  - Action: Browse the full catalog using default data.
  - Expected: Every listed challenge displays a meaningful title, a programming-challenge description, and exactly one difficulty and one topic label; no placeholder or unrelated entries are present.
  - Actual: All 10 cards verified programmatically: meaningful titles (Two Sum, Reverse String, Valid Palindrome, Maximum Subarray, Binary Search, Valid Parentheses, Climbing Stairs, Fibonacci Number, Merge Sorted Array, Longest Common Subsequence), each with a real 103-char problem description, exactly one difficulty label (5 easy / 4 medium / 1 hard) and exactly one topic label (arrays, strings, algorithms, data structures, dynamic programming, recursion); no placeholder text (lorem/todo/placeholder/n-a) found.

- [X] CT-02: Leaderboard and dashboard statistics are accurate
  - Action: Compare the leaderboard points for a user and the dashboard's completed-by-difficulty counts against the user's actual solved challenges.
  - Expected: Displayed points and difficulty counts match the actual solved challenges exactly.
  - Actual: Actual solved = Two Sum (easy) only. Dashboard: 10 points, Challenges Solved 1/10, Easy 1/5, Medium 0/4, Hard 0/1, Overall 10%. Leaderboard: 10 points, "1 challenges solved". Both match exactly (Submissions 4 and Success Rate 50% also match the 2 passed / 2 failed submission history).
