# Test Checklist

## Functionality
- [ ] FT-01: Registered users can create a poll with a question, description, and at least two answer choices.
  - Action: Sign in as a registered user, open the poll creation form, enter a question, description, multiple choices, and submit.
  - Expected: The poll is created and its question, description, and choices are displayed.

- [ ] FT-02: Poll creators can set an optional voting deadline and select a voting mode.
  - Action: Create or edit a poll, set a future deadline, choose Anonymous voting or Sign-in required, and save.
  - Expected: The selected deadline and voting mode are saved and displayed on the poll.

- [ ] FT-03: Poll creators can share a usable voting link.
  - Action: Open an existing poll owned by the registered user and activate its Share or Copy link control.
  - Expected: A poll URL is provided, and opening it displays the corresponding poll voting page.

- [ ] FT-04: Voters can submit a vote through a shared poll link.
  - Action: Open a shared poll link, select one available choice, and submit the vote.
  - Expected: The vote is accepted and the selected choice is recorded.

- [ ] FT-05: Voters can view poll results after voting.
  - Action: Submit a valid vote and inspect the results section.
  - Expected: Results are displayed immediately after the vote is submitted.

- [ ] FT-06: Poll creators can close a poll early.
  - Action: Open an active poll owned by the user and select the control to close it.
  - Expected: The poll changes to a closed state and no longer accepts votes.

- [ ] FT-07: Poll creators can reopen a closed poll.
  - Action: Open a closed poll owned by the user and select the Reopen control.
  - Expected: The poll returns to an active voting state and accepts a valid vote.

- [ ] FT-08: Poll creators can switch a poll to read-only results mode.
  - Action: Change an active poll to read-only results mode.
  - Expected: Existing results remain visible while voting controls are unavailable.

- [ ] FT-09: Users can browse their polls from the dashboard.
  - Action: Sign in and open the polls dashboard.
  - Expected: The dashboard lists the user’s available polls with enough information to open each poll.

- [ ] FT-10: Users can search dashboard polls by title.
  - Action: Enter an exact or partial existing poll title in the dashboard search field.
  - Expected: Only polls whose titles match the search query are listed.

- [ ] FT-11: Users can sort dashboard polls by title, creation date, and status.
  - Action: Apply each available sort option and toggle its ascending or descending order when available.
  - Expected: The poll list is reordered according to the selected field and direction.

## Constraint
- [ ] CS-01: Poll creation cannot be submitted without a question, description, and multiple choices.
  - Action: Leave each required field empty in separate submission attempts, or provide fewer than two choices, and submit.
  - Expected: Submission is blocked and the missing or invalid field is identified.

- [ ] CS-02: An optional voting deadline must be valid.
  - Action: Submit a poll with no deadline, then attempt submission with an invalid or past deadline.
  - Expected: A poll without a deadline can be saved; an invalid or past deadline is rejected with a clear validation message.

- [ ] CS-03: Sign-in-required polls cannot be voted on by signed-out users.
  - Action: Open a sign-in-required poll while signed out and attempt to vote.
  - Expected: Voting is blocked and the user is prompted to sign in.

- [ ] CS-04: Anonymous polls allow voting without requiring sign-in.
  - Action: Open an anonymous poll while signed out, select a choice, and submit the vote.
  - Expected: The vote can be submitted without a sign-in prompt.

- [ ] CS-05: Closed, expired, and read-only polls do not accept votes.
  - Action: Open a poll in each of these states and attempt to select and submit a choice.
  - Expected: Voting is unavailable or submission is blocked, while any permitted results remain viewable.

- [ ] CS-06: Poll management controls are restricted to the poll creator.
  - Action: Open another user’s poll while signed in as a different registered user.
  - Expected: Close, reopen, and read-only management controls are unavailable.

## Interaction
- [ ] IX-01: Poll results update live when a new vote is cast.
  - Action: Open the same active poll in two browser sessions, cast a vote in one session, and observe the results in the other session without manually refreshing.
  - Expected: The second session updates its result bars and vote totals to include the new vote.

- [ ] IX-02: Results display a visual bar breakdown for every answer choice.
  - Action: Open results for a poll containing multiple choices and inspect the results visualization.
  - Expected: Each choice has a visible bar and an associated count or percentage that corresponds to its votes.

- [ ] IX-03: Poll state changes are reflected immediately in the creator interface.
  - Action: Close, reopen, and switch a poll to read-only mode in succession.
  - Expected: The displayed status, available management action, and voting controls change to match the current state after each action.

- [ ] IX-04: The dashboard responds to search and sort actions without showing stale poll entries.
  - Action: Search for a title, clear the search, and apply different sort options.
  - Expected: The list refreshes after each action and contains only the records matching the current filter and sort settings.

## Content
- [ ] CT-01: Poll details accurately display the configured question, description, choices, deadline, and voting mode.
  - Action: Open a configured poll and compare its displayed content with the values saved during creation.
  - Expected: Every displayed value matches the saved poll configuration.

- [ ] CT-02: Poll results show accurate labels, totals, and percentages.
  - Action: Compare each result bar’s choice label, vote count, and percentage with the votes submitted for that poll.
  - Expected: All labels and figures are present, readable, and mathematically consistent.

- [ ] CT-03: Dashboard poll metadata accurately identifies title, creation date, and status.
  - Action: Compare dashboard entries with the corresponding poll pages and inspect entries in each available status.
  - Expected: Each dashboard title, creation date, and status matches the associated poll.