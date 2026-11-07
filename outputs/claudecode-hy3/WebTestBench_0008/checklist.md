# Test Checklist

## Functionality
- [ ] FT-01: Register a new user account
  - Action: Navigate to the registration page, fill required fields (username, email, password), click "Sign Up"
  - Expected: Account is created and the user is logged in / redirected into the app

- [ ] FT-02: Browse the challenge catalog
  - Action: Open the "Challenges" / catalog page
  - Expected: A list or grid of programming challenges is displayed

- [ ] FT-03: Filter challenges by difficulty and topic
  - Action: Select a difficulty filter and a topic filter from the catalog controls
  - Expected: Catalog shows only challenges matching the selected difficulty and topic

- [ ] FT-04: Open a challenge and access the embedded code editor
  - Action: Click a challenge from the catalog
  - Expected: Challenge detail page opens containing an embedded code editor

- [ ] FT-05: Submit a code solution
  - Action: Enter/modify code in the embedded editor and click "Submit"
  - Expected: The solution is sent to the system for evaluation

- [ ] FT-06: System automatically runs the solution against predefined test cases
  - Action: Submit a valid solution
  - Expected: The system executes the solution against predefined test cases without any manual "run" trigger

- [ ] FT-07: View pass/fail result of a submission
  - Action: Submit a solution
  - Expected: The result clearly states whether the solution passed or failed the test cases

- [ ] FT-08: View basic feedback for failed test cases
  - Action: Submit a solution that fails some test cases
  - Expected: Basic feedback is shown (e.g., which tests failed or an error message)

- [ ] FT-09: View personal dashboard with progress
  - Action: Navigate to the personal dashboard
  - Expected: Dashboard displays the user's progress (e.g., challenges solved / completion status)

- [ ] FT-10: Review past submissions
  - Action: Open the submissions history section
  - Expected: A list of past submissions appears with challenge name, result, and timestamp

- [ ] FT-11: View statistics of challenges completed by difficulty
  - Action: Open the statistics area on the dashboard
  - Expected: Statistics show the count of completed challenges grouped by difficulty

- [ ] FT-12: View leaderboard ranked by points
  - Action: Open the leaderboard page
  - Expected: Leaderboard displays users ordered by points earned from solved challenges

## Constraint
- [ ] CS-01: Block submission of empty code
  - Action: Open a challenge, clear the editor, click "Submit"
  - Expected: Submission is rejected with a validation message and no test run is triggered

- [ ] CS-02: Require login to submit solutions
  - Action: Log out, open a challenge, attempt to click "Submit"
  - Expected: Submission is blocked and the user is prompted to log in

## Interaction
- [ ] IX-01: Catalog updates dynamically when filters change
  - Action: Change the difficulty or topic filter
  - Expected: The catalog list refreshes to reflect the new filter without a full page reload

- [ ] IX-02: Show a visual submission status indicator
  - Action: Submit a solution
  - Expected: A visual indicator (e.g., toast or banner) shows the submission was received and its result (pass/fail)

## Content
- [ ] CT-01: Challenge cards show relevant metadata
  - Action: Browse the catalog
  - Expected: Each challenge displays a title, difficulty, and topic relevant to programming challenges

- [ ] CT-02: Leaderboard shows usernames and points
  - Action: Open the leaderboard
  - Expected: Each entry shows a username and the earned points used for comparison

- [ ] CT-03: Dashboard statistics are labeled by difficulty
  - Action: Open the dashboard statistics
  - Expected: Statistics are clearly labeled by difficulty category (e.g., Easy, Medium, Hard)