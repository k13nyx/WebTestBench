# Test Checklist

## Functionality
- [ ] FT-01: Registered user can create a poll with a question, description, and multiple choices.
  - Action: Sign in, create a new poll filling question, description, and at least 3 choices, then save.
  - Expected: The poll is created successfully and appears as an available poll.
- [ ] FT-02: Poll creator can set a voting deadline when creating a poll.
  - Action: Create a poll and set a future voting deadline before saving.
  - Expected: The poll is saved with the specified deadline visible on the poll.
- [ ] FT-03: Poll creator can choose anonymous voting or sign-in-required voting modes.
  - Action: Create one poll with anonymous mode and another requiring voters to sign in.
  - Expected: Both polls are saved with their respective voting modes as selected.
- [ ] FT-04: Creator can obtain a shareable link for a poll.
  - Action: Open a created poll and use the share option.
  - Expected: A shareable poll link is provided and can be opened in a new browser session to reach the voting page.
- [ ] FT-05: Voter can cast a vote by selecting a choice and submitting.
  - Action: Open a poll via its link, select one choice, and submit the vote.
  - Expected: The vote is recorded and the vote count for that poll increases by 1.
- [ ] FT-06: Voter sees live results after voting.
  - Action: After submitting a vote, view the poll.
  - Expected: Results are displayed showing the voter's choice and updated tallies.
- [ ] FT-07: Results display bar-style visual breakdowns.
  - Action: Open a poll's results view.
  - Expected: Each choice is represented by a bar whose length corresponds proportionally to its vote share.
- [ ] FT-08: Bar results update as votes are cast.
  - Action: Note the bars, then cast an additional vote from another session, and re-check results.
  - Expected: The bars and counts reflect the newly cast vote.
- [ ] FT-09: Creator can close a poll early.
  - Action: Open a poll's management options and close it before its deadline.
  - Expected: Poll status changes to closed and voting is no longer accepted.
- [ ] FT-10: Creator can reopen a closed poll.
  - Action: Open a closed poll's management options and reopen it.
  - Expected: Poll status returns to open and voting is accepted again.
- [ ] FT-11: Creator can switch a poll to read-only results mode.
  - Action: Set a poll to read-only results.
  - Expected: The poll shows results only and no voting option is available.
- [ ] FT-12: Dashboard lists the user's polls.
  - Action: Open the dashboard.
  - Expected: All polls created by the signed-in user are listed.
- [ ] FT-13: Dashboard search filters polls by title.
  - Action: Enter a title keyword in the dashboard search field.
  - Expected: Only polls whose titles match the keyword are shown.
- [ ] FT-14: Dashboard sorts polls by title, creation date, and status.
  - Action: Apply each sort option (title, creation date, status) in both orders.
  - Expected: The poll list reorders correctly for each sort criterion and direction.

## Constraint
- [ ] CS-01: Poll cannot be created without a question and at least two choices.
  - Action: Attempt to save a new poll with an empty question, or with fewer than two choices.
  - Expected: Saving is blocked and an error indicates the missing required fields.
- [ ] CS-02: Sign-in-required polls cannot be voted on by an unauthenticated visitor.
  - Action: Open a sign-in-required poll in a signed-out session and attempt to vote.
  - Expected: Voting is blocked and the user is prompted to sign in.
- [ ] CS-03: No voting on closed or read-only polls.
  - Action: Attempt to vote on a poll that is closed or set to read-only results.
  - Expected: No voting controls are available and submission is rejected.
- [ ] CS-04: Voting is blocked after the deadline passes.
  - Action: Attempt to vote on a poll whose deadline has passed.
  - Expected: Voting is prevented and the poll is shown as ended.
- [ ] CS-05: A voter cannot vote more than once on the same poll.
  - Action: Submit a vote, then attempt to vote again on the same poll from the same voter session.
  - Expected: The second vote is rejected; the poll's total count does not increase twice.

## Interaction
- [ ] IX-01: Poll management controls reflect and apply state changes immediately.
  - Action: Use the close, reopen, and read-only controls on a poll.
  - Expected: The displayed status label updates instantly to Closed, Open, or Read-only accordingly.

## Content
- [ ] CT-01: Poll view displays all creator-entered content accurately.
  - Action: Open a poll created with a specific question, description, and choice texts.
  - Expected: The question, description, and every choice text appear exactly as entered, with correct vote counts and percentages next to each bar.