# Test Checklist

## Functionality
- [ ] FT-01: New user can register an account
  - Action: Open the registration page, enter a valid username/email and password, submit the form
  - Expected: Registration succeeds, the user is logged in (or redirected to login and can log in), and the app shows the authenticated user's identity (e.g., username in the header)
- [ ] FT-02: Registered user can log in
  - Action: Enter the credentials of the account created in FT-01 on the login form and submit
  - Expected: User is authenticated and taken to the catalog or dashboard
- [ ] FT-03: Catalog displays programming challenges organized by difficulty
  - Action: Open the challenge catalog
  - Expected: Multiple pre-existing challenges are listed and each is labeled with a difficulty level (e.g., Easy/Medium/Hard), with grouping or filter controls by difficulty
- [ ] FT-04: Catalog supports filtering/browsing by topic
  - Action: Select a topic (e.g., "Arrays", "Strings", "Dynamic Programming") from the catalog's topic navigation/filter
  - Expected: Only challenges matching that topic are shown; the list updates accordingly
- [ ] FT-05: User can open a challenge and write code in the embedded editor
  - Action: Click any challenge in the catalog to open its detail page
  - Expected: The challenge description is shown together with an embedded code editor where the user can type/edit code
- [ ] FT-06: User can submit a solution and it is automatically evaluated
  - Action: Type a correct solution for a challenge in the embedded editor and click the Submit button
  - Expected: The submission is accepted without manual intervention, the code is run against the challenge's predefined test cases, and a result appears (e.g., "Passed")
- [ ] FT-07: Incorrect solution shows failed result with basic feedback
  - Action: Submit deliberately wrong code for the same challenge
  - Expected: Result shows a failure state (e.g., "Failed"), and basic feedback is displayed such as which test case failed or expected vs. actual output
- [ ] FT-08: Dashboard tracks solved challenges
  - Action: After solving at least one challenge (FT-06), open the personal dashboard
  - Expected: The dashboard lists the challenge just solved as completed and shows an overall progress indicator (e.g., X challenges completed)
- [ ] FT-09: User can review past submissions
  - Action: Open the submissions history section (dashboard or challenge page)
  - Expected: A chronological list of the user's own submissions is shown with challenge name, timestamp, and pass/fail status
- [ ] FT-10: Dashboard shows statistics of challenges completed by difficulty
  - Action: Open the dashboard statistics section
  - Expected: Statistics are displayed breaking down completed challenges per difficulty level (e.g., Easy: 2, Medium: 1, Hard: 0) matching the user's actual solved challenges
- [ ] FT-11: Leaderboard ranks users by points earned from solved challenges
  - Action: Open the leaderboard page
  - Expected: A ranked list of users is shown sorted by total points (descending), including the current user, with points earned from solved challenges

## Constraint
- [ ] CS-01: Registration cannot proceed with invalid or missing required fields
  - Action: Submit the registration form with an empty username or email, or an invalid email format, or too-short password
  - Expected: Submission is rejected with a validation error message; no account is created and the user remains unauthenticated
- [ ] CS-02: Registration rejects a username/email that is already registered
  - Action: Attempt to register again with the exact credentials of the account created in FT-01
  - Expected: An error message indicates the account/username already exists and registration is not completed
- [ ] CS-03: Challenge catalog and submission features are inaccessible when not logged in
  - Action: Log out (or use a fresh/incognito session) and attempt to open the dashboard, submit code, or view the leaderboard
  - Expected: Access is denied — the user is redirected to login/registration or shown an "access denied" message; no personal data is visible
- [ ] CS-04: Submitting with an empty editor is not allowed
  - Action: Open a challenge, leave the code editor empty (or clear it), and click Submit
  - Expected: Submission is blocked with a validation message (e.g., "Code cannot be empty") and no test run is triggered
- [ ] CS-05: A failed submission does not award points or mark the challenge as solved
  - Action: Submit a wrong solution to a previously unsolved challenge (FT-07), then check the dashboard and leaderboard
  - Expected: The challenge is not counted as completed, no points are added for it, and dashboard statistics are unchanged

## Interaction
- [ ] IX-01: Submission shows an in-progress state while test cases are running
  - Action: Click Submit on a challenge solution
  - Expected: The UI immediately shows a pending/running indicator (e.g., "Running tests…" or a spinner) before the final result appears
- [ ] IX-02: Passing result is highlighted with success feedback
  - Action: Submit a correct solution (FT-06)
  - Expected: A success state is clearly visible (e.g., green "All tests passed" message, badge, or toast) and the tests-passed count (e.g., "5/5") is shown

## Content
- [ ] CT-01: Challenge descriptions are relevant to programming challenges
  - Action: Open at least two different challenges from the catalog
  - Expected: Each shows a problem statement containing task description, examples/input-output, and/or constraints relevant to programming problems — no placeholder or empty text
- [ ] CT-02: Leaderboard entries show meaningful, non-placeholder data
  - Action: Inspect the leaderboard list
  - Expected: Each row shows a username and a numeric point total consistent with the points system; default seeded users appear with plausible values (no "Lorem ipsum", empty cells, or test placeholders)