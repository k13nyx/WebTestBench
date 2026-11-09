# Test Checklist

## Functionality
- [ ] FT-01: Registered user can create a poll with a question, description, and multiple choices
  - Action: Sign in, open the poll creation form, enter a question, a description, and at least two choices, then submit
  - Expected: Poll is created and shown with the entered question, description, and all choices

- [ ] FT-02: Creator can set an optional voting deadline
  - Action: On the creation form, set a voting deadline (and separately, leave it empty)
  - Expected: With a deadline set, the poll displays that deadline; with it empty, the poll is created with no deadline and remains open

- [ ] FT-03: Creator can choose the voting mode
  - Action: Select "Anonymous" and create a poll, then select "Require sign-in" and create another poll
  - Expected: The selected mode is saved and displayed for each poll

- [ ] FT-04: Voter can cast a vote using a shared poll link
  - Action: Open a poll's share link, select a choice, and submit the vote
  - Expected: The vote is recorded and the voter is taken to the results view

- [ ] FT-05: Voter can see live results after voting
  - Action: Cast a vote and view the results page
  - Expected: Results are displayed for that poll immediately after voting

- [ ] FT-06: Creator can close a poll early
  - Action: From poll management, click "Close" on an open poll
  - Expected: Poll status changes to closed and no further votes are accepted

- [ ] FT-07: Creator can reopen a closed poll
  - Action: From poll management, reopen a previously closed poll
  - Expected: Poll status returns to open and voting is accepted again

- [ ] FT-08: Creator can switch a poll to read-only results
  - Action: From poll management, switch a poll to "read-only results" mode
  - Expected: Poll shows results only, with voting disabled

- [ ] FT-09: Creator can browse and search their polls in the dashboard
  - Action: Open the dashboard and enter a known poll title in the search field
  - Expected: The list filters to polls whose title matches the search term

- [ ] FT-10: Creator can sort polls by title, creation date, and status
  - Action: Apply each sort option on the dashboard
  - Expected: The list reorders correctly for each selected sort field

## Constraint
- [ ] CS-01: A poll cannot be created without a question
  - Action: Submit the creation form with the question field empty
  - Expected: Submission is blocked with a validation message for the missing question

- [ ] CS-02: A poll cannot be created with fewer than two choices
  - Action: Submit the creation form with one choice or no choices
  - Expected: Submission is blocked with a validation message requiring at least two choices

- [ ] CS-03: Voting is blocked after the voting deadline passes
  - Action: Open a poll whose deadline has passed and attempt to vote
  - Expected: Voting is prevented and the poll indicates it has ended

- [ ] CS-04: A "require sign-in" poll blocks unauthenticated voters
  - Action: Open a "require sign-in" poll while signed out and attempt to vote
  - Expected: Voting is blocked and the voter is prompted to sign in

- [ ] CS-05: A voter cannot vote more than once on the same poll
  - Action: Vote on a poll, then attempt to vote on the same poll again
  - Expected: The second vote is rejected or the voter is prevented from submitting it

- [ ] CS-06: A closed or read-only poll does not accept votes
  - Action: Open a closed poll and a read-only poll and attempt to vote on each
  - Expected: Voting is disabled or rejected for both poll states

## Interaction
- [ ] IX-01: Results bar breakdown updates live as votes are cast
  - Action: With the results view open, cast additional votes on the same poll
  - Expected: The bars and counts update to reflect the new votes without a full page reload

- [ ] IX-02: User receives confirmation feedback after key actions
  - Action: Create a poll and, separately, cast a vote
  - Expected: A success confirmation (e.g., toast/message) appears after each action

## Content
- [ ] CT-01: Poll page displays content exactly as entered
  - Action: Open a created poll and compare it against the creator's input
  - Expected: Question, description, and all choices match the entered text

- [ ] CT-02: Results breakdown displays accurate labels and values
  - Action: Open the results view of a poll with known votes
  - Expected: Each choice label, vote count, and percentage/proportion bar correctly reflects the recorded votes