# Test Checklist

## Functionality
- [ ] FT-01: Register a new user account
  - Action: Navigate to registration, enter a unique username, valid email, and password, then submit.
  - Expected: Account is created and the user is signed in (navigation shows the new username or a logged-in state).

- [ ] FT-02: Log in with registered credentials
  - Action: Log out, then log in using the registered username and password.
  - Expected: Login succeeds and the user is taken to the authenticated view.

- [ ] FT-03: Browse the challenge catalog
  - Action: Open the catalog page using default data.
  - Expected: A list of challenges is displayed, each showing its title, difficulty, and topic.

- [ ] FT-04: Filter catalog by difficulty
  - Action: Select a difficulty filter (e.g., "Easy") in the catalog.
  - Expected: Only challenges of that difficulty are listed.

- [ ] FT-05: Filter catalog by topic
  - Action: Select a topic filter (e.g., "Arrays") in the catalog.
  - Expected: Only challenges belonging to that topic are listed.

- [ ] FT-06: Open a challenge and view its details
  - Action: Click a challenge title in the catalog.
  - Expected: The challenge page shows the problem description, difficulty, topic, and an embedded code editor.

- [ ] FT-07: Submit a correct solution and receive a pass result
  - Action: Enter a correct solution in the editor for a challenge and click the submit button.
  - Expected: Test cases run and the result indicates the solution passed, with basic feedback shown.

- [ ] FT-08: Submit an incorrect solution and receive a fail result
  - Action: Enter a deliberately wrong solution for a challenge and submit it.
  - Expected: Test cases run and the result indicates the solution failed, with basic feedback shown.

- [ ] FT-09: View personal dashboard with progress
  - Action: Open the dashboard page after registering/solving.
  - Expected: The dashboard shows the user's progress, including challenges completed broken down by difficulty.

- [ ] FT-10: Review past submissions
  - Action: Open the submissions/history section of the dashboard.
  - Expected: A list of the user's previous submissions appears with challenge name, result (passed/failed), and submission time.

- [ ] FT-11: View the leaderboard
  - Action: Open the leaderboard page.
  - Expected: Users are listed with their points, ordered so higher-scoring users rank higher.

## Constraint
- [ ] CS-01: Registration rejects duplicate username
  - Action: Attempt to register with an existing username from default/created accounts.
  - Expected: Registration is blocked and an error message about the username being taken is shown.

- [ ] CS-02: Registration rejects empty required fields
  - Action: Submit the registration form with one or more required fields empty.
  - Expected: The form is not submitted and an error is shown for the empty field(s).

- [ ] CS-03: Login rejects invalid credentials
  - Action: Attempt to log in with a wrong password for an existing username.
  - Expected: Login fails and an error message is displayed; the user remains logged out.

- [ ] CS-04: Protected pages are inaccessible when logged out
  - Action: While logged out, attempt to open the dashboard or submissions page.
  - Expected: Access is denied (redirect to login or explicit message); private data is not shown.

- [ ] CS-05: Points are awarded only once per solved challenge
  - Action: Submit a correct solution for a challenge already solved by the same user, then check the leaderboard score.
  - Expected: The user's total points do not increase for re-solving the same challenge.

## Interaction
- [ ] IX-01: Submission provides immediate processing feedback
  - Action: Click the submit button with code in the editor.
  - Expected: The UI indicates the solution is being judged (e.g., loading/running state) and then transitions to displaying the pass/fail result without a page reload.

- [ ] IX-02: Result view distinguishes pass from fail visually
  - Action: Submit a correct solution, then an incorrect solution.
  - Expected: Each result is clearly shown as passed or failed with distinct visual indication (e.g., color/label) and the associated test-case feedback.

## Content
- [ ] CT-01: Challenge catalog content is complete and relevant
  - Action: Browse the full catalog using default data.
  - Expected: Every listed challenge displays a meaningful title, a programming-challenge description, and exactly one difficulty and one topic label; no placeholder or unrelated entries are present.

- [ ] CT-02: Leaderboard and dashboard statistics are accurate
  - Action: Compare the leaderboard points for a user and the dashboard's completed-by-difficulty counts against the user's actual solved challenges.
  - Expected: Displayed points and difficulty counts match the actual solved challenges exactly.