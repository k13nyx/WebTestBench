# Test Checklist

## Functionality
- [ ] FT-01: New user can register an account
  - Action: Navigate to registration page and submit valid username, email, and password
  - Expected: Account is created and user is redirected to a logged-in state

- [ ] FT-02: User can browse the programming challenge catalog
  - Action: Navigate to the challenges catalog page
  - Expected: A list of available programming challenges is displayed

- [ ] FT-03: User can filter the challenge list by difficulty
  - Action: Select a difficulty level (e.g., Easy, Medium, Hard) from a filter control
  - Expected: The displayed challenge list updates to show only challenges of the selected difficulty

- [ ] FT-04: User can filter the challenge list by topic
  - Action: Select a topic (e.g., Arrays, Strings, Algorithms) from a filter control
  - Expected: The displayed challenge list updates to show only challenges tagged with the selected topic

- [ ] FT-05: User can open a challenge and view its description
  - Action: Click on a challenge from the catalog
  - Expected: A challenge detail view is shown with description, requirements, and an embedded code editor

- [ ] FT-06: User can write code in the embedded editor
  - Action: Click inside the code editor and type code
  - Expected: The text appears in the editor as typed

- [ ] FT-07: User can submit a code solution
  - Action: Write code in the editor and click the Submit button
  - Expected: The system accepts the submission and runs it against the test cases

- [ ] FT-08: System shows pass/fail status for each test case
  - Action: Submit a solution and wait for evaluation
  - Expected: A result is displayed showing which test cases passed and which failed

- [ ] FT-09: User can review their past submissions
  - Action: Navigate to the submissions history section
  - Expected: A list of previous submissions is shown with challenge name, date, and result

- [ ] FT-10: User can view their personal dashboard
  - Action: Navigate to the personal dashboard
  - Expected: Dashboard is shown displaying the user's progress information

- [ ] FT-11: Dashboard shows statistics of challenges completed by difficulty
  - Action: View the personal dashboard
  - Expected: A breakdown of completed challenges grouped by difficulty level (Easy, Medium, Hard) is visible

- [ ] FT-12: User can view the leaderboard
  - Action: Navigate to the leaderboard page
  - Expected: A ranking of users with their points earned from solved challenges is displayed

## Constraint
- [ ] CS-01: Registration is rejected when mandatory fields are missing
  - Action: Submit the registration form with one or more required fields left blank
  - Expected: The form is not submitted and an error message indicates which fields are required

- [ ] CS-02: Empty code cannot be submitted
  - Action: Leave the code editor empty and click the Submit button
  - Expected: Submission is blocked and a message indicates code must be provided

- [ ] CS-03: Dashboard and submissions are only accessible to logged-in users
  - Action: Log out and try to navigate directly to the dashboard or submissions page
  - Expected: Access is denied and the user is redirected to the login or registration page

- [ ] CS-04: Leaderboard only counts fully solved challenges
  - Action: Review the leaderboard ranking after solving only some test cases of a challenge
  - Expected: Partially passed challenges do not contribute points; only fully solved challenges count

## Interaction
- [ ] IX-01: Dashboard updates after solving a new challenge
  - Action: Solve a challenge successfully, then revisit the personal dashboard
  - Expected: The progress and difficulty statistics reflect the newly completed challenge

- [ ] IX-02: Applying a filter updates the displayed challenge list
  - Action: Change the difficulty or topic filter after a list is shown
  - Expected: The list reloads immediately to show only challenges matching the new filter

- [ ] IX-03: Submission result appears after evaluation completes
  - Action: Submit a code solution
  - Expected: A visible status indicator (e.g., loading then pass/fail result) is shown without requiring a page refresh

## Content
- [ ] CT-01: Feedback identifies which test case failed when a solution is incorrect
  - Action: Submit an incorrect solution that passes some tests but fails others
  - Expected: The feedback output specifies which test case(s) failed and shows relevant input/expected values

- [ ] CT-02: Challenges in the catalog are clearly labeled by difficulty and topic
  - Action: View the challenge catalog
  - Expected: Each challenge entry visibly displays its difficulty level and topic category