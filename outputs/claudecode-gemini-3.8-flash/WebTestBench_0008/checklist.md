# Test Checklist

## Functionality
- [ ] FT-01: User registration with valid credentials
  - Action: Fill in username, email, and password in the registration form and click "Register".
  - Expected: Account is created successfully and the user is logged into the application.
- [ ] FT-02: Filter challenge catalog by difficulty and topic
  - Action: Navigate to the catalog, select difficulty "Easy" from the difficulty filter, and select "Arrays" from the topic filter.
  - Expected: Catalog displays only challenges tagged with "Easy" difficulty and "Arrays" topic.
- [ ] FT-03: Open programming challenge in embedded editor
  - Action: Click on any challenge from the catalog list.
  - Expected: Challenge details page loads with the problem description, test cases, and an interactive embedded code editor.
- [ ] FT-04: Submit passing code solution
  - Action: Enter correct solution code into the embedded editor and click "Submit".
  - Expected: Solution runs against predefined test cases and displays a "Passed" status with test case success feedback.
- [ ] FT-05: View past submissions on dashboard
  - Action: Navigate to the personal dashboard and click the "Submissions" tab.
  - Expected: Displays a chronological history of past submissions showing challenge title, submission date/time, and pass/fail status.
- [ ] FT-06: View solved challenges statistics by difficulty
  - Action: Open the personal dashboard and view the statistics section.
  - Expected: Displays the total number of solved challenges categorized by difficulty level (Easy, Medium, Hard).
- [ ] FT-07: View leaderboard rankings by points
  - Action: Click on the "Leaderboard" navigation link.
  - Expected: Displays a ranked list of users ordered descending by total points earned from solved challenges.

## Constraint
- [ ] CS-01: Prevent registration with empty required fields
  - Action: Leave the registration form fields blank and click "Register".
  - Expected: Form submission is blocked and field-level validation messages appear on required inputs.
- [ ] CS-02: Prevent registration with an existing email
  - Action: Enter an email address belonging to an existing default user and click "Register".
  - Expected: Registration fails and an error message displays stating the email is already in use.
- [ ] CS-03: Prevent submission of empty code
  - Action: Clear all code from the embedded editor and click "Submit".
  - Expected: Submission is prevented and an alert or validation message prompts the user to enter code before submitting.
- [ ] CS-04: Display failure feedback for incorrect solution
  - Action: Enter code that produces incorrect output or a syntax error in the embedded editor and click "Submit".
  - Expected: Test execution marks the submission as "Failed" and displays error feedback specifying the failed test case.
- [ ] CS-05: Restrict dashboard access to unauthenticated users
  - Action: Log out and attempt to navigate directly to the dashboard URL.
  - Expected: User is redirected to the login or registration page and dashboard content is not shown.

## Interaction
- [ ] IX-01: Code submission loading state
  - Action: Click the "Submit" button while code is in the editor.
  - Expected: The "Submit" button displays a loading spinner or "Running..." text and remains disabled until execution finishes.
- [ ] IX-02: Switch between test case result tabs
  - Action: After submitting code, click between different test case tabs (e.g., "Test Case 1", "Test Case 2") in the results panel.
  - Expected: Active tab highlights and the panel immediately updates to show corresponding input, expected output, and actual output without refreshing the page.
- [ ] IX-03: Reset catalog filters
  - Action: Apply difficulty and topic filters in the catalog, then click the "Reset Filters" button.
  - Expected: Filter dropdowns reset to their default unselected state and the catalog immediately restores the full challenge list.

## Content
- [ ] CT-01: Challenge problem description details
  - Action: Inspect the problem panel of an active challenge.
  - Expected: Displays problem title, difficulty badge, topic tag, detailed description, input/output specifications, and at least one example case.
- [ ] CT-02: Catalog challenge item metadata
  - Action: View any challenge item card in the catalog list.
  - Expected: Shows challenge title, difficulty badge, topic tag, and points awarded upon completion.
- [ ] CT-03: Leaderboard table columns and user data
  - Action: Inspect the leaderboard table layout and default data.
  - Expected: Table displays columns for Rank, Username, Challenges Solved, and Total Points with non-empty values for each listed user.