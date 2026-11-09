# Test Result

## Functionality

- [X] FT-01: User can register a new account
  - Action: Enter valid values in the registration form and select “Register” or “Sign Up.”
  - Expected: The account is created successfully and the user is signed in or redirected to the application.

- [X] FT-02: User can browse the programming challenge catalog
  - Action: Open the “Challenges” or catalog page.
  - Expected: Pre-existing programming challenges are displayed and can be browsed.

- [X] FT-03: User can locate challenges by difficulty and topic
  - Action: Select an available difficulty and an available topic from the catalog controls.
  - Expected: The catalog displays only challenges matching the selected difficulty and topic.

- [X] FT-04: User can open a challenge and access its coding workspace
  - Action: Select a challenge from the catalog.
  - Expected: The challenge description, difficulty, topic, predefined test information, embedded code editor, and code submission control are displayed.

- [X] FT-05: User can submit a correct solution
  - Action: Enter a solution that satisfies the challenge requirements and select “Submit”.
  - Expected: The solution is executed against the predefined test cases and is reported as passed when all tests succeed.

- [X] FT-06: User can submit an incorrect solution
  - Action: Enter a solution that does not satisfy the challenge requirements and select “Submit”.
  - Expected: The solution is executed against the predefined test cases and is reported as failed when one or more tests fail.

- [X] FT-07: User can view personal progress on the dashboard
  - Action: Open the “Dashboard” or personal progress page.
  - Expected: The dashboard shows the signed-in user’s challenge progress, including solved or completed challenges.

- [X] FT-08: User can review past submissions
  - Action: Open the dashboard’s “Submissions” or submission-history section.
  - Expected: Previous submissions are listed with enough information to identify the challenge, submission result, and submission date or time.

- [X] FT-09: User can view completion statistics by difficulty
  - Action: Open the statistics section of the personal dashboard.
  - Expected: Statistics show the number of completed challenges for each available difficulty level.

- [X] FT-10: User can view the leaderboard
  - Action: Open the “Leaderboard” page or section.
  - Expected: Users are listed with their earned points and relative ranking or position.

- [X] FT-11: Solving challenges contributes to leaderboard points
  - Action: Record the user’s points before solving an unsolved challenge, submit a correct solution, and revisit the leaderboard.
  - Expected: The user’s points increase according to the challenge’s defined score, and the updated total appears on the leaderboard.

## Constraint

- [X] CS-01: Registration prevents submission with missing required information
  - Action: Leave one or more required registration fields empty and select “Register” or “Sign Up.”
  - Expected: Registration is blocked and a validation message identifies the missing required field or fields.

- [X] CS-02: Catalog filters do not show mismatched challenges
  - Action: Apply a difficulty or topic filter and inspect every displayed challenge.
  - Expected: Every displayed challenge matches all active filter selections; mismatched challenges are excluded.

- [ ] CS-03: Empty code cannot be submitted
  - Action: Leave the embedded code editor empty and select “Submit.”
  - Expected: Submission is blocked and the interface clearly indicates that code must be entered.
  - Bug Report:
    - Issue: Empty submission is accepted
    - Actual: Selecting “Run Tests” with the empty editor created a submission, displayed “0/2 tests passed,” and added an entry to submission history instead of blocking the submission or showing a required-code validation message.

- [X] CS-04: Personal data is scoped to the signed-in user
  - Action: Sign in as a registered user and open the dashboard and submission history.
  - Expected: The dashboard and history contain only that user’s progress, statistics, and submissions.

## Interaction

- [ ] IX-01: Submission displays an execution state
  - Action: Submit code for a challenge.
  - Expected: The interface indicates that the submission is being evaluated and prevents or clearly handles duplicate submissions while evaluation is in progress.
  - Bug Report:
    - Issue: No evaluation state is displayed
    - Actual: After selecting “Run Tests,” the interface immediately displayed the test result notification and results; no “evaluating” or loading state was observable, and duplicate-submission handling during evaluation was not indicated.

- [X] IX-02: Submission result and basic feedback are clearly presented
  - Action: Wait for a submitted solution to finish evaluation.
  - Expected: A clear passed or failed result is shown together with basic feedback identifying the outcome, such as passed tests, failed tests, or an execution error.

- [X] IX-03: Dashboard updates after a successful challenge completion
  - Action: Successfully solve an unsolved challenge, then open or refresh the dashboard.
  - Expected: The completed challenge, completion statistics, and corresponding progress state are updated without requiring unrelated user actions.

## Content

- [X] CT-01: Challenge catalog content is relevant and complete
  - Action: Review the challenges shown in the catalog.
  - Expected: Each challenge is a programming problem with a title, description, difficulty, and topic that accurately represent its content.

- [X] CT-02: Challenge test and feedback content corresponds to the selected challenge
  - Action: Open a challenge, submit code, and inspect the displayed evaluation feedback.
  - Expected: The test-case results and feedback refer to the selected challenge and do not display content from another challenge.

- [X] CT-03: Dashboard statistics and leaderboard values are labeled and understandable
  - Action: Review the dashboard statistics and leaderboard.
  - Expected: Difficulty labels, completion counts, user names, rankings, and point totals are clearly labeled and use consistent values across the application.