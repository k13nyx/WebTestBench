# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Open the registration page, enter a unique username, valid email, and matching password, then click the "Register" / "Sign Up" button.
  - Expected: Account is created and the user is logged in or redirected to the login/catalog page.
- [ ] FT-02: Registered user can log in
  - Action: Enter valid existing credentials on the login page and submit.
  - Expected: User is authenticated and taken to the catalog or dashboard.
- [ ] FT-03: User can browse the challenge catalog
  - Action: Navigate to the catalog/challenges page.
  - Expected: A list of existing challenges is displayed.
- [ ] FT-04: Challenges can be filtered/viewed by difficulty
  - Action: Select a difficulty level (e.g., "Easy", "Medium", "Hard") in the catalog filter.
  - Expected: Only challenges matching the selected difficulty are listed.
- [ ] FT-05: Challenges can be filtered/viewed by topic
  - Action: Select a topic (e.g., "Arrays", "Strings") in the catalog filter.
  - Expected: Only challenges belonging to the selected topic are listed.
- [ ] FT-06: User can open a challenge with its embedded code editor
  - Action: Click a challenge in the catalog.
  - Expected: Challenge details and an embedded code editor with a "Submit" / "Run" button are shown.
- [ ] FT-07: Submitting a correct solution runs tests and reports pass
  - Action: Enter a known-correct solution in the editor and click "Submit".
  - Expected: System runs it against predefined test cases and reports the result as PASSED.
- [ ] FT-08: Submitting an incorrect solution reports failure with feedback
  - Action: Enter an incorrect solution and click "Submit".
  - Expected: Result is reported as FAILED along with basic feedback describing the failure.
- [ ] FT-09: Dashboard shows progress and completed challenges by difficulty
  - Action: Open the personal dashboard as a logged-in user.
  - Expected: Progress overview and statistics of challenges completed broken down by difficulty are displayed.
- [ ] FT-10: User can review past submissions
  - Action: Open the submissions/history section from the dashboard.
  - Expected: A list of the user's previous submissions with their results is displayed.
- [ ] FT-11: Leaderboard ranks users by points earned
  - Action: Open the leaderboard page.
  - Expected: Users are listed in descending order of points earned from solved challenges.

## Constraint
- [ ] CS-01: Registration is rejected for an already-used email
  - Action: Attempt to register using an email that already belongs to an existing account.
  - Expected: Registration is blocked with an error indicating the email is already in use.
- [ ] CS-02: Registration is rejected when required fields are empty
  - Action: Submit the registration form with one or more required fields left blank.
  - Expected: Submission is blocked and validation errors identify the missing required fields.
- [ ] CS-03: Empty code submission is rejected
  - Action: Click "Submit" with an empty editor.
  - Expected: Submission is blocked or immediately reported as invalid; no test run is executed as a valid solution.
- [ ] CS-04: Personal dashboard/submissions require authentication
  - Action: Attempt to open the dashboard or submissions page while logged out.
  - Expected: Access is denied and the user is redirected to login.
- [ ] CS-05: A failed solution awards no points
  - Action: Submit an incorrect solution, then compare the user's points before and after.
  - Expected: Points remain unchanged for the failed submission.

## Interaction
- [ ] IX-01: Confirmation is shown after successful registration
  - Action: Complete registration with valid unique details.
  - Expected: A success message/toast or confirmation is displayed before or alongside redirection.
- [ ] IX-02: Loading indicator appears while tests run
  - Action: Click "Submit" on a solution.
  - Expected: A visible loading/running indicator appears until the result is returned.

## Content
- [ ] CT-01: Challenge listings display title, difficulty, and topic
  - Action: Inspect challenge items in the catalog.
  - Expected: Each entry clearly shows the challenge title, its difficulty, and its topic.
- [ ] CT-02: Leaderboard entries display username and point value
  - Action: Inspect rows on the leaderboard.
  - Expected: Each row shows the user's name/username and their earned points.