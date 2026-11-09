# Test Result

## Functionality

- [X] FT-01: Registered users can create a poll with a question, description, and at least two answer choices.
  - Action: Sign in as a registered user, open the poll creation form, enter a question, description, multiple choices, and submit.
  - Expected: The poll is created and its question, description, and choices are displayed.

- [X] FT-02: Poll creators can set an optional voting deadline and select a voting mode.
  - Action: Create or edit a poll, set a future deadline, choose Anonymous voting or Sign-in required, and save.
  - Expected: The selected deadline and voting mode are saved and displayed on the poll.

- [ ] FT-03: Poll creators can share a usable voting link.
  - Action: Open an existing poll owned by the registered user and activate its Share or Copy link control.
  - Expected: A poll URL is provided, and opening it displays the corresponding poll voting page.
  - Bug Report:
    - Issue: Shared poll link opens an unavailable poll page
    - Actual: The Share control copied `http://localhost:6015/poll/poll-1794205300154`, but opening that URL in another browser tab displayed “Poll Not Found” and “This poll may have been deleted or the link is incorrect.”

- [ ] FT-04: Voters can submit a vote through a shared poll link.
  - Action: Open a shared poll link, select one available choice, and submit the vote.
  - Expected: The vote is accepted and the selected choice is recorded.
  - Bug Report:
    - Issue: Voting page is unavailable through the shared link
    - Actual: The newly created poll’s shared URL displayed “Poll Not Found,” so no choice or vote submission control was available.

- [ ] FT-05: Voters can view poll results after voting.
  - Action: Submit a valid vote and inspect the results section.
  - Expected: Results are displayed immediately after the vote is submitted.
  - Bug Report:
    - Issue: Vote cannot be submitted
    - Actual: The shared poll URL returned “Poll Not Found,” preventing a vote from being submitted and preventing immediate post-vote results from being verified.

- [X] FT-06: Poll creators can close a poll early.
  - Action: Open an active poll owned by the user and select the control to close it.
  - Expected: The poll changes to a closed state and no longer accepts votes.

- [X] FT-07: Poll creators can reopen a closed poll.
  - Action: Open a closed poll owned by the user and select the Reopen control.
  - Expected: The poll returns to an active voting state and accepts a valid vote.

- [X] FT-08: Poll creators can switch a poll to read-only results mode.
  - Action: Change an active poll to read-only results mode.
  - Expected: Existing results remain visible while voting controls are unavailable.

- [X] FT-09: Users can browse their polls from the dashboard.
  - Action: Sign in and open the polls dashboard.
  - Expected: The dashboard lists the user’s available polls with enough information to open each poll.

- [X] FT-10: Users can search dashboard polls by title.
  - Action: Enter an exact or partial existing poll title in the dashboard search field.
  - Expected: Only polls whose titles match the search query are listed.

- [ ] FT-11: Users can sort dashboard polls by title, creation date, and status.
  - Action: Apply each available sort option and toggle its ascending or descending order when available.
  - Expected: The poll list is reordered according to the selected field and direction.
  - Bug Report:
    - Issue: Status is not available as a dashboard sort field
    - Actual: The dashboard provided “Newest first,” “Oldest first,” “Title A-Z,” and “Most votes,” but no status sort option or ascending/descending status control.

## Constraint

- [ ] CS-01: Poll creation cannot be submitted without a question, description, and multiple choices.
  - Action: Leave each required field empty in separate submission attempts, or provide fewer than two choices, and submit.
  - Expected: Submission is blocked and the missing or invalid field is identified.
  - Bug Report:
    - Issue: Description is not enforced as a required field
    - Actual: The creation form labels the field “Description” without a required marker and uses the placeholder “Add more context about your poll (optional).” The UI therefore does not identify description as a required field. A fewer-than-two-options submission did correctly show “Please add at least 2 options.”

- [ ] CS-02: An optional voting deadline must be valid.
  - Action: Submit a poll with no deadline, then attempt submission with an invalid or past deadline.
  - Expected: A poll without a deadline can be saved; an invalid or past deadline is rejected with a clear validation message.
  - Bug Report:
    - Issue: Past deadline is not rejected with a validation message
    - Actual: A poll with no deadline was saved successfully, but submitting a poll with deadline `2020-01-01T12:00` left the user on the creation form without displaying a clear validation message.

- [ ] CS-03: Sign-in-required polls cannot be voted on by signed-out users.
  - Action: Open a sign-in-required poll while signed out and attempt to vote.
  - Expected: Voting is blocked and the user is prompted to sign in.
  - Bug Report:
    - Issue: Signed-out user is not prompted to sign in
    - Actual: The signed-out sign-in-required poll page displayed “This poll has expired and is no longer accepting votes” and only showed results; no sign-in prompt was displayed.

- [ ] CS-04: Anonymous polls allow voting without requiring sign-in.
  - Action: Open an anonymous poll while signed out, select a choice, and submit the vote.
  - Expected: The vote can be submitted without a sign-in prompt.
  - Bug Report:
    - Issue: Anonymous poll voting page is unavailable
    - Actual: Opening the shared URL for the newly created anonymous poll displayed “Poll Not Found,” so no anonymous voting control was available.

- [ ] CS-05: Closed, expired, and read-only polls do not accept votes.
  - Action: Open a poll in each of these states and attempt to select and submit a choice.
  - Expected: Voting is unavailable or submission is blocked, while any permitted results remain viewable.
  - Bug Report:
    - Issue: Closed-state public voting behavior could not be verified because shared poll URLs were unavailable
    - Actual: Expired and read-only poll pages showed results without voting controls, but the created poll’s public/shared URL returned “Poll Not Found,” preventing verification of the closed-state voting page.

- [ ] CS-06: Poll management controls are restricted to the poll creator.
  - Action: Open another user’s poll while signed in as a different registered user.
  - Expected: Close, reopen, and read-only management controls are unavailable.
  - Bug Report:
    - Issue: Cross-user management restriction could not be verified
    - Actual: The test environment did not provide a second usable registered account and public poll links for newly created polls returned “Poll Not Found,” so management-control visibility for another user’s poll could not be confirmed.

## Interaction

- [ ] IX-01: Poll results update live when a new vote is cast.
  - Action: Open the same active poll in two browser sessions, cast a vote in one session, and observe the results in the other session without manually refreshing.
  - Expected: The second session updates its result bars and vote totals to include the new vote.
  - Bug Report:
    - Issue: Shared poll cannot be opened in a second browser session
    - Actual: The newly created poll returned “Poll Not Found” in the second tab, so a cross-session vote and live result update could not occur.

- [X] IX-02: Results display a visual bar breakdown for every answer choice.
  - Action: Open results for a poll containing multiple choices and inspect the results visualization.
  - Expected: Each choice has a visible bar and an associated count or percentage that corresponds to its votes.

- [X] IX-03: Poll state changes are reflected immediately in the creator interface.
  - Action: Close, reopen, and switch a poll to read-only mode in succession.
  - Expected: The displayed status, available management action, and voting controls change to match the current state after each action.

- [X] IX-04: The dashboard responds to search and sort actions without showing stale poll entries.
  - Action: Search for a title, clear the search, and apply different sort options.
  - Expected: The list refreshes after each action and contains only the records matching the current filter and sort settings.

## Content

- [X] CT-01: Poll details accurately display the configured question, description, choices, deadline, and voting mode.
  - Action: Open a configured poll and compare its displayed content with the values saved during creation.
  - Expected: Every displayed value matches the saved poll configuration.

- [X] CT-02: Poll results show accurate labels, totals, and percentages.
  - Action: Compare each result bar’s choice label, vote count, and percentage with the votes submitted for that poll.
  - Expected: All labels and figures are present, readable, and mathematically consistent.

- [X] CT-03: Dashboard poll metadata accurately identifies title, creation date, and status.
  - Action: Compare dashboard entries with the corresponding poll pages and inspect entries in each available status.
  - Expected: Each dashboard title, creation date, and status matches the associated poll.