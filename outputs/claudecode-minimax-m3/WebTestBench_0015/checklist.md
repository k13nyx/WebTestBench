# Test Checklist

## Functionality
- [ ] FT-01: Registered user can sign in to access the application
  - Action: Click "Sign In" / "Register" and submit valid credentials
  - Expected: User is authenticated and redirected to the dashboard or home page

- [ ] FT-02: User can create a poll with a question, description, and multiple choices
  - Action: Fill in the poll creation form with a question, description, and at least 2 choices, then submit
  - Expected: Poll is created and a confirmation/confirmation page is shown

- [ ] FT-03: User can set an optional voting deadline when creating a poll
  - Action: Fill in the poll creation form including a future date/time as the voting deadline and submit
  - Expected: Poll is created with the deadline saved and visible on the poll page

- [ ] FT-04: User can select either anonymous mode or sign-in required mode when creating a poll
  - Action: Create one poll with anonymous mode and another with sign-in required mode
  - Expected: Both polls are saved with the chosen mode, and voting behaves accordingly

- [ ] FT-05: Poll creator can share a poll via a shareable link
  - Action: Open the creator's poll page and copy/share the provided link
  - Expected: A unique URL is provided that opens the correct poll for any visitor

- [ ] FT-06: User can cast a vote on an open poll
  - Action: Open a poll link, select one choice, and submit the vote
  - Expected: Vote is recorded and the user is shown the results

- [ ] FT-07: Voter can view live results after submitting their vote
  - Action: Submit a vote on a poll
  - Expected: Results (bar chart and counts) are displayed immediately after voting

- [ ] FT-08: Poll creator can close, reopen, and switch a poll to read-only results
  - Action: Use the poll management controls to: (1) close the poll, (2) reopen it, (3) set it to read-only results
  - Expected: Each action succeeds and the poll's status updates accordingly

- [ ] FT-09: Dashboard allows browsing, searching, and sorting the user's polls by title, creation date, and status
  - Action: Use dashboard search to find a poll by title, then sort by title, creation date, and status
  - Expected: The poll list filters correctly and reorders according to each selected sort

## Constraint
- [ ] CS-01: Poll creation cannot be submitted when required fields are empty
  - Action: Attempt to submit the poll creation form with an empty question or no choices
  - Expected: Form submission is blocked and an inline error message identifies the missing field(s)

- [ ] CS-02: Users cannot vote on a poll that is closed or set to read-only results
  - Action: Open a poll that has been closed or set to read-only and look for vote options
  - Expected: Vote choices/buttons are not available and only results are shown

- [ ] CS-03: Users cannot vote on a poll after the voting deadline has passed
  - Action: Open a poll whose deadline is in the past and attempt to vote
  - Expected: Voting is disabled and the page indicates the poll is closed/expired

- [ ] CS-04: Anonymous visitors cannot vote when the poll is set to require sign-in
  - Action: While signed out, open a poll configured to require sign-in and attempt to vote
  - Expected: User is prompted to sign in and cannot submit a vote without authentication

- [ ] CS-05: Only the poll creator can manage (close/reopen/read-only) their poll
  - Action: Sign in as a non-creator user, open another user's poll, and look for management controls
  - Expected: Management controls (close, reopen, read-only) are not visible to non-creators

## Interaction
- [ ] IX-01: Bar-style results update live as new votes are cast
  - Action: Open the poll results page, cast a vote from another browser/session, and observe the results
  - Expected: The bar lengths and vote counts update without requiring a manual page refresh

- [ ] IX-02: A confirmation message is shown after a poll is successfully created
  - Action: Submit a new poll via the creation form
  - Expected: A success message/toast and/or redirect confirms the poll was created

- [ ] IX-03: The poll status indicator on the dashboard updates after the creator changes the poll's status
  - Action: Close/reopen a poll from its management page, then return to the dashboard
  - Expected: The dashboard's status label for that poll reflects the new state (e.g., Open/Closed/Read-only)

- [ ] IX-04: A success feedback is shown after the user submits a vote
  - Action: Cast a vote on any open poll
  - Expected: A confirmation indicator appears and the UI transitions to display the results

## Content
- [ ] CT-01: The poll page correctly displays the question, description, and all choices provided at creation
  - Action: Create a poll with a specific question, description, and list of choices, then open the poll page
  - Expected: All entered text appears verbatim and every choice is listed

- [ ] CT-02: Bar chart proportions accurately reflect the distribution of votes
  - Action: Cast votes across multiple choices in known ratios (e.g., 3 votes on A, 1 vote on B) and inspect the chart
  - Expected: Bar lengths and percentages visually correspond to the actual vote counts