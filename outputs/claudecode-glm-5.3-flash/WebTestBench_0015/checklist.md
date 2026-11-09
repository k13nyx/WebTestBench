# Test Checklist

## Functionality
- [ ] FT-01: Registered user can create a poll with a question, description, and multiple answer choices
  - Action: Sign in, open the create-poll form, fill in a question (e.g., "Favorite color?"), a description, and at least 2–3 choices (e.g., "Red", "Blue", "Green"), then submit.
  - Expected: The poll is created successfully and appears (in the dashboard or confirmation view) with the entered question, description, and choices.
- [ ] FT-02: Poll creator can set an optional voting deadline
  - Action: Create a poll with a future date/time entered in the deadline field and submit.
  - Expected: The poll is saved with the deadline visible on its detail/share page.
- [ ] FT-03: Poll creator can omit the voting deadline
  - Action: Create a poll leaving the deadline field empty and submit.
  - Expected: The poll is created successfully with no deadline shown.
- [ ] FT-04: Poll creator can choose the voting mode (anonymous vs. sign-in required)
  - Action: Create one poll with mode "anonymous" and another with mode "sign-in required"; open each poll's voting page.
  - Expected: Each poll reflects the selected mode (anonymous poll allows voting without sign-in; the other poll indicates sign-in is required).
- [ ] FT-05: Poll creator can copy/obtain a shareable link that others can open to vote
  - Action: Open a created poll and copy its share link; open the link in a logged-out or different browser session.
  - Expected: The link opens the poll's voting page showing the question and choices.
- [ ] FT-06: A voter can cast a vote on an open poll
  - Action: On the poll's voting page, select one choice (e.g., "Blue") and submit the vote.
  - Expected: The vote is accepted and recorded.
- [ ] FT-07: Results are shown as a bar-style visual breakdown per choice
  - Action: Open a poll that has votes and view its results section.
  - Expected: Each choice displays a bar visual whose length/size reflects its share of votes, with vote counts or percentages shown.
- [ ] FT-08: Poll creator can close a poll early
  - Action: Open an open poll in the management/dashboard view and use the close action (e.g., "Close poll" button).
  - Expected: The poll's status changes to closed/closed-early.
- [ ] FT-09: Poll creator can reopen a closed poll
  - Action: Use the reopen action on a poll that was closed.
  - Expected: The poll's status returns to open and voting is available again.
- [ ] FT-10: Poll creator can switch a poll to read-only results
  - Action: Use the "read-only results" action on an open or closed poll.
  - Expected: The poll's status changes to read-only and its voting page shows results without voting options.
- [ ] FT-11: Dashboard allows browsing all of the user's polls
  - Action: Sign in and open the dashboard.
  - Expected: All polls created by the user are listed.
- [ ] FT-12: Dashboard supports searching polls by title
  - Action: Enter a keyword from an existing poll's title (e.g., "Favorite") into the dashboard search box.
  - Expected: Only matching polls are shown; non-matching polls are filtered out.
- [ ] FT-13: Dashboard supports sorting polls by title, creation date, and status
  - Action: Apply each sort option (title, creation date, status) in the dashboard.
  - Expected: The list reorders correctly for each sort (e.g., alphabetical by title, newest/oldest first by date, grouped by status).
- [ ] FT-14: Voter sees live results after voting
  - Action: Submit a vote on a poll and remain on the page.
  - Expected: The results view with the bar-style breakdown is shown to the voter immediately after voting.

## Constraint
- [ ] CS-01: Poll creation cannot be submitted with empty required fields
  - Action: Submit the create-poll form with an empty question or fewer than 2 choices.
  - Expected: Submission is blocked with a validation message; the poll is not created.
- [ ] CS-02: Voting on a "sign-in required" poll is blocked for unauthenticated visitors
  - Action: Open a sign-in-required poll's share link while logged out and attempt to vote.
  - Expected: Voting is prevented and the user is prompted to sign in first.
- [ ] CS-03: Voting is blocked after the deadline has passed
  - Action: Open a poll whose deadline has expired and attempt to vote.
  - Expected: The vote is rejected or voting controls are disabled, with the poll shown as closed/expired.
- [ ] CS-04: Voting is blocked on a poll closed early by its creator
  - Action: Open the share link of a poll that was closed early and attempt to vote.
  - Expected: Voting is prevented; results or a "closed" message is shown instead.
- [ ] CS-05: A read-only results poll cannot be voted on
  - Action: Open a poll switched to read-only and attempt to vote.
  - Expected: No voting controls are available; only the results are displayed.

## Interaction
- [ ] IX-01: Results update live as votes are cast
  - Action: Have a poll's results page open in one session, then cast a vote from another session for the same poll.
  - Expected: The bar breakdown/counts on the first session update without a manual page reload.
- [ ] IX-02: A success confirmation appears after a poll is created
  - Action: Submit a valid create-poll form.
  - Expected: A success toast/message (e.g., "Poll created") is displayed.
- [ ] IX-03: A confirmation/feedback appears after casting a vote
  - Action: Submit a vote on a poll.
  - Expected: Feedback such as "Vote recorded" is shown and the results view is revealed.

## Content
- [ ] CT-01: Poll detail page displays all entered content accurately
  - Action: Open a poll and compare with what was entered at creation.
  - Expected: The question, description, and all choices are shown correctly and completely.
- [ ] CT-02: Dashboard list shows each poll's title, creation date, and status
  - Action: View the dashboard list rows.
  - Expected: Each row displays the poll's title, its creation date, and a status label (e.g., Open / Closed / Read-only) matching the poll's actual state.
- [ ] CT-03: Results breakdown shows accurate per-choice vote data
  - Action: Cast a known set of votes (e.g., 2 votes for "Red", 1 for "Blue") and view results.
  - Expected: Counts/percentages shown per choice match the actual votes cast (e.g., Red 66%, Blue 33%).