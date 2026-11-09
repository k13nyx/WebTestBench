# Test Checklist

## Functionality
- [ ] FT-01: Registered user can create a poll with all fields
  - Action: Log in as a registered user, open the poll creation form, enter a question, a description, at least two choices, set a voting deadline, select a mode (anonymous or sign-in required), and submit.
  - Expected: Poll is created and viewable; question, description, choices, deadline, and mode are all displayed correctly.

- [ ] FT-02: Poll creator can obtain a shareable link
  - Action: Open a poll created by the logged-in user and activate the share function (e.g., "Share" button / copy link).
  - Expected: A unique poll link is displayed/copyable, and opening that link leads directly to the voting page for that poll.

- [ ] FT-03: Voter can cast a vote via the shared link
  - Action: Open the shared poll link and select one of the choices, then submit the vote.
  - Expected: The vote is recorded (vote count increases by one) and the vote page confirms the vote was accepted.

- [ ] FT-04: Live results are visible after voting
  - Action: After casting a vote on a poll, remain on the results view.
  - Expected: Bar-style breakdown is shown immediately after voting, with per-choice counts/percentages.

- [ ] FT-05: Results update as new votes are cast
  - Action: Cast an additional vote on the same poll from another session, then refresh/recheck the results view.
  - Expected: The bar breakdown reflects the new totals (counts/percentages change accordingly).

- [ ] FT-06: Creator can manage poll status (close, reopen, read-only)
  - Action: As the poll creator, close an open poll early; then reopen it; then switch it to read-only results mode.
  - Expected: After closing, voting is disabled; after reopening, voting is enabled again; in read-only mode results are shown but no new votes can be cast.

- [ ] FT-07: Dashboard lists polls and supports search and sort
  - Action: Open the dashboard, type a known poll title keyword in the search box, then sort the list by title, by creation date, and by status.
  - Expected: Search filters to polls whose title matches the keyword; sorting reorders the list correctly by title, creation date, and status respectively.

## Constraint
- [ ] CS-01: Poll requires a question and at least two choices
  - Action: Submit the poll creation form with the question empty, and separately with fewer than two choices filled in.
  - Expected: Creation is blocked and a validation error is shown; the poll is not created.

- [ ] CS-02: Anonymous polls allow voting without sign-in; sign-in-required polls reject anonymous voters
  - Action: Open an anonymous-mode poll link while logged out and vote; then open a sign-in-required poll link while logged out.
  - Expected: The anonymous poll accepts the vote with no login prompt; the sign-in-required poll shows a sign-in prompt and does not allow voting until logged in.

- [ ] CS-03: Expired polls do not accept votes
  - Action: Open a default poll whose voting deadline has passed and attempt to vote.
  - Expected: Voting controls are disabled/hidden, results are still viewable, and no vote can be recorded.

- [ ] CS-04: A voter cannot vote twice on the same poll
  - Action: After successfully voting on a poll (in the same session/account), attempt to vote again.
  - Expected: Second vote is rejected (options disabled or duplicate-vote message shown) and the total vote count does not increase.

## Interaction
- [ ] IX-01: Confirmation feedback on vote submission
  - Action: Submit a vote on a poll and observe the interface response.
  - Expected: A clear confirmation (e.g., "Vote recorded" message/toast or immediate switch to results view) appears after the vote is accepted.

- [ ] IX-02: Status change is reflected in the UI immediately
  - Action: As creator, close a poll early, then reopen it, observing the poll page and dashboard after each action.
  - Expected: Poll status label (Open/Closed/Read-only) updates immediately on the poll page and in the dashboard status column without stale state.

- [ ] IX-03: Search filters the dashboard list in real time
  - Action: On the dashboard, type characters into the search field one by one.
  - Expected: The poll list updates as the query is entered, showing only matching polls; a query matching nothing displays an explicit empty/no-results state.

## Content
- [ ] CT-01: Poll details display completely and consistently everywhere
  - Action: Compare the question, description, choices, deadline, and mode shown on the voting page, the shared link page, and the dashboard entry for the same poll.
  - Expected: All fields display identically and legibly in each view; description and deadline are not truncated or missing.

- [ ] CT-02: Bar breakdown content is accurate and relevant
  - Action: With a default poll that has recorded votes, inspect the results chart.
  - Expected: Each choice has a corresponding bar labeled with its text, count, and percentage; bars are proportional to the actual vote counts and match the displayed total.