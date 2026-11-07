# Test Checklist

## Functionality
- [ ] FT-01: Registered user can create a poll with question, description, and multiple choices
  - Action: As a registered user, open poll creation, enter a question, description, and add 2+ choices, then submit.
  - Expected: Poll is created and appears in the dashboard.

- [ ] FT-02: Creator can set an optional voting deadline when creating a poll
  - Action: During poll creation, set an optional voting deadline date/time and submit.
  - Expected: Poll is created with the specified deadline applied.

- [ ] FT-03: Creator can choose voting mode (anonymous or sign-in required)
  - Action: During poll creation, select the voting mode (anonymous OR require sign-in) and submit.
  - Expected: Poll is created with the chosen voting mode.

- [ ] FT-04: Creator can obtain a shareable poll link
  - Action: Open a created poll and use the share/link control.
  - Expected: A shareable poll URL is generated/provided.

- [ ] FT-05: Voter can cast a vote via the shared link
  - Action: As a voter, open the shared poll link, select a choice, and submit the vote.
  - Expected: The vote is recorded for the poll.

- [ ] FT-06: Voter can see live results after voting
  - Action: After voting, view the poll's results view.
  - Expected: Live results are visible to the voter.

- [ ] FT-07: Creator can close a poll early
  - Action: As creator, open poll management and choose the close option.
  - Expected: Poll is closed and no longer accepts votes.

- [ ] FT-08: Creator can reopen a closed poll
  - Action: As creator, reopen a closed poll from management controls.
  - Expected: Poll reopens and accepts votes again.

- [ ] FT-09: Creator can switch a poll to read-only results mode
  - Action: As creator, switch a poll to "read-only results" mode.
  - Expected: Poll shows results but disables new voting.

- [ ] FT-10: Dashboard lists the user's own polls
  - Action: Open the dashboard as the registered user.
  - Expected: The user's own polls are listed.

- [ ] FT-11: Dashboard search filters polls by keyword
  - Action: In the dashboard search box, enter a keyword from a poll title.
  - Expected: Only polls matching the keyword are shown.

- [ ] FT-12: Dashboard sorts polls by title
  - Action: In the dashboard, sort by title.
  - Expected: Polls are ordered alphabetically by title.

- [ ] FT-13: Dashboard sorts polls by creation date
  - Action: In the dashboard, sort by creation date.
  - Expected: Polls are ordered by creation date.

- [ ] FT-14: Dashboard sorts polls by status
  - Action: In the dashboard, sort by status.
  - Expected: Polls are ordered/grouped by status (e.g., open/closed).

## Constraint
- [ ] CS-01: Poll creation blocked without required question or with fewer than 2 choices
  - Action: Attempt to submit a poll with no question or with only 1 choice.
  - Expected: Submission is blocked with a validation error; no poll is created.

- [ ] CS-02: Voting blocked on closed or read-only polls
  - Action: Attempt to vote on a poll that is closed or in read-only mode.
  - Expected: Voting is prevented; no vote is recorded.

- [ ] CS-03: Sign-in-required mode blocks unsigned voters
  - Action: As an unsigned user, attempt to vote on a sign-in-required poll.
  - Expected: Voting is blocked; user is required to sign in.

- [ ] CS-04: Voting blocked after the deadline passes
  - Action: Attempt to vote after the poll's voting deadline has passed.
  - Expected: Voting is blocked; a deadline-expired message is shown.

- [ ] CS-05: Vote submission requires a selected choice
  - Action: Open a poll and submit a vote without selecting any choice.
  - Expected: Submission is blocked with a prompt to select a choice.

## Interaction
- [ ] IX-01: Results render as live-updating bar-style breakdown
  - Action: Cast a vote on a poll and observe the results view.
  - Expected: Results show a bar-style breakdown per choice that updates live as new votes are cast.

## Content
- [ ] CT-01: Poll results display the correct question and choices
  - Action: Open a poll's results view and inspect the displayed text.
  - Expected: The poll's question and choice labels are shown accurately and match the poll's definition.