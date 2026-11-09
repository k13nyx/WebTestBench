# Test Result

## Functionality
- [X] FT-01: Registered user can create a poll with all details
  - Action: Sign in, click "Create Poll", fill in a question, a description, at least 2 answer choices, leave deadline empty, select "Anonymous voting" mode, and submit.
  - Expected: Poll is created and appears in the dashboard list with the entered question, description, and choices, and with no voting deadline.

- [X] FT-02: Registered user can create a poll that requires voters to sign in
  - Action: In the "Create Poll" form, select the "Require sign-in to vote" mode, fill all required fields, and submit.
  - Expected: Poll is created successfully and its settings/details page shows voting mode as sign-in required.

- [X] FT-03: Poll can be created with an optional voting deadline
  - Action: In the "Create Poll" form, set a future voting deadline (e.g., a date/time tomorrow), fill required fields, and submit.
  - Expected: Poll is created and its page displays the chosen deadline.

- [X] FT-04: Poll creator can obtain a shareable link to the poll
  - Action: From the dashboard, open a pre-existing poll created by the signed-in user and click the "Share"/"Copy link" control.
  - Expected: A link to that specific poll is provided (e.g., copied to clipboard or displayed) and, when opened, loads that poll's page.

- [X] FT-05: A visitor can vote on a shared anonymous poll without signing in
  - Action: Open the shared link of a pre-existing anonymous poll in a session where the visitor is not signed in, select a choice, and submit the vote.
  - Expected: The vote is accepted and recorded (vote count for the chosen choice increases).

- [X] FT-06: A signed-in user can vote on a poll requiring sign-in
  - Action: Open a pre-existing sign-in-required poll while signed in as a registered user, select a choice, and submit.
  - Expected: The vote is accepted and recorded.

- [X] FT-07: Poll creator can close a poll early
  - Action: As the creator, open one of your open polls and click "Close Poll".
  - Expected: Poll status changes to Closed, and this is reflected on the poll page and dashboard.

- [X] FT-08: Poll creator can reopen a closed poll
  - Action: On a poll you created that is currently Closed, click "Reopen".
  - Expected: Poll status changes back to Open and voting is possible again.

- [X] FT-09: Poll creator can switch a poll to read-only results
  - Action: As the creator, open one of your open polls and choose the "Read-only results" option.
  - Expected: Poll changes so only results are viewable — no voting is possible, and results remain visible to visitors.

- [X] FT-10: Dashboard shows the creator's polls
  - Action: Sign in as a registered user who owns pre-existing polls and open the dashboard.
  - Expected: Dashboard lists the user's polls, each showing at least title, status, and creation date.

- [X] FT-11: Dashboard search filters polls by title
  - Action: Type the full title (or a word from the title) of a pre-existing poll into the dashboard search box.
  - Expected: The list shows only the poll(s) whose titles match the search text.

- [X] FT-12: Dashboard can sort polls by creation date
  - Action: On the dashboard, apply the "Creation date" sort (toggling ascending/descending if available).
  - Expected: Polls are listed in order of creation date that matches the applied direction (newest-first or oldest-first), verifiable against the displayed dates.

- [X] FT-13: Dashboard can sort polls by status
  - Action: On the dashboard, apply the "Status" sort.
  - Expected: Polls are grouped/ordered by status (e.g., Open polls together, Closed polls together).

## Constraint
- [X] CS-01: Poll cannot be created without required fields
  - Action: Open "Create Poll", leave the question empty or provide fewer than 2 choices, and submit.
  - Expected: Poll is not created; a validation error indicates the missing required field(s).

- [X] CS-02: Votes are rejected after the deadline passes
  - Action: Create a poll with a deadline a couple of minutes in the future, wait (or use a pre-existing poll already past its deadline), then attempt to vote.
  - Expected: Vote is not accepted and the poll shows as Closed/expired with voting disabled.

- [X] CS-03: Unauthenticated users cannot vote on a sign-in-required poll
  - Action: Open the shared link of a pre-existing sign-in-required poll while not signed in, and attempt to vote.
  - Expected: Vote is not accepted; the page prompts the user to sign in before voting.

- [X] CS-04: A voter cannot vote twice on the same poll
  - Action: Submit a vote on a poll (e.g., the shared anonymous poll from FT-05), then attempt to vote again on the same choice or another choice.
  - Expected: The second vote is rejected or the voting form is disabled, and the vote counts do not change from a second submission.

- [X] CS-05: A non-creator cannot manage a poll
  - Action: Sign in as a different registered user, open the shared link of another user's poll, and look for Close/Reopen/Read-only controls.
  - Expected: Poll management controls are not shown/enabled for users who did not create the poll.

## Interaction
- [ ] IX-01: Results update live as votes are cast
  - Action: With the poll's results view open, cast a new vote from another session/window; observe the results bar chart.
  - Expected: The bar for the voted choice increases (counts/percentages) without a manual page reload.
  - Bug Report:
    - Issue: No cross-window/session data synchronization — results cannot update live from another window
    - Actual: All poll state is held in per-window, in-memory React context (localStorage/sessionStorage are empty and there are no backend API, WebSocket, or BroadcastChannel calls). A poll created in one window returns "Poll Not Found — This poll may have been deleted or the link is incorrect." when its share link is opened in another window (verified in two separate fresh windows for two different created polls). The only polls shared across windows are the seeded demo polls, and all of them are past deadline ("Expired") or read-only, so they cannot accept votes in any window. Consequently, no vote cast from another session/window can ever increase a bar in an open results view — the chart only updates within the single window where the vote is cast.

- [X] IX-02: Voter sees live results immediately after voting
  - Action: Submit a vote on any open poll.
  - Expected: The page transitions to a results view showing the bar-style breakdown including the just-cast vote.

- [X] IX-03: Voting action gives immediate feedback
  - Action: Select a choice and submit a vote on an open poll.
  - Expected: A visible confirmation (e.g., "Your vote has been recorded" message or highlighted selected choice) appears before/at the transition to results.

## Content
- [X] CT-01: Results view shows complete and correct poll information
  - Action: Open the results of a pre-existing poll with votes.
  - Expected: The poll's question and description are shown, every configured choice is listed with its vote count and/or percentage, and bar lengths match the displayed numbers.

- [X] CT-02: Dashboard poll entries show accurate data
  - Action: Open the dashboard and inspect several pre-existing polls.
  - Expected: Each entry's title, creation date, and status accurately match that poll's actual details on its own page, and no unrelated data (e.g., other users' polls) is listed.
