# Test Checklist

## Functionality
- [ ] FT-01: Create a poll with question, description, and multiple choices.
  - Action: Fill the poll form with a Question, a Description, and 3 choices; click "Create Poll".
  - Expected: Poll is created and appears in the dashboard with the entered question.
- [ ] FT-02: Voting deadline is optional and can be set or omitted.
  - Action: Create one poll with a future "Voting deadline" set, and one with the deadline left empty.
  - Expected: Both polls are created; the deadline is shown on the first poll and absent on the second.
- [ ] FT-03: Poll creator can choose anonymous voting or sign-in-required voting.
  - Action: Create one poll selecting the "Anonymous" mode and another selecting "Require sign-in".
  - Expected: Both polls are created and display their selected voting mode.
- [ ] FT-04: Poll creator can share a link that lets others vote.
  - Action: Open a poll from the dashboard, use the "Share"/"Copy link" control, open the copied link.
  - Expected: The link opens the poll's voting page showing the question and choices.
- [ ] FT-05: A voter can submit a vote on an open poll.
  - Action: Open a shared poll link, select one choice, click "Vote".
  - Expected: The vote is accepted and recorded for that choice.
- [ ] FT-06: Voter sees results after voting.
  - Action: Submit a vote on an open poll, then view the page.
  - Expected: A results view (bar-style breakdown) is displayed after voting.
- [ ] FT-07: Poll creator can close a poll early.
  - Action: On the creator's poll, click "Close poll".
  - Expected: The poll status changes to closed and is shown as closed.
- [ ] FT-08: Poll creator can reopen a closed poll.
  - Action: On a closed poll, click "Reopen".
  - Expected: The poll becomes open again and accepts votes.
- [ ] FT-09: Poll creator can switch a poll to read-only results.
  - Action: On the creator's poll, select "Read-only results".
  - Expected: The poll shows results only; the voting form is no longer offered.
- [ ] FT-10: Dashboard lists the user's polls.
  - Action: Open the dashboard page.
  - Expected: A list of the user's polls is displayed with title and status per poll.
- [ ] FT-11: Dashboard search filters the poll list.
  - Action: Enter a keyword from an existing poll's title in the dashboard search box.
  - Expected: The list shows only matching polls; clearing the search restores the full list.
- [ ] FT-12: Dashboard can sort polls by title, creation date, and status.
  - Action: Use the "Sort by" control and select Title, then Creation date, then Status.
  - Expected: The list reorders accordingly each time (ascending/descending as labeled).

## Constraint
- [ ] CS-01: Poll cannot be created with a missing question or invalid choices.
  - Action: Attempt to create a poll with an empty Question; then attempt with fewer than two choices or a blank choice text.
  - Expected: Creation is blocked both times; the missing field (question / choices) is identified.
- [ ] CS-02: Sign-in-required poll blocks signed-out voters.
  - Action: Open the share link of a "Require sign-in" poll in a signed-out state and try to vote.
  - Expected: Voting is blocked with a prompt to sign in; no vote is recorded.
- [ ] CS-03: Closed or read-only polls cannot be voted on.
  - Action: Open the share link of a closed poll and of a read-only poll; attempt to vote.
  - Expected: Voting is blocked on both; only results are viewable.
- [ ] CS-04: Poll cannot be voted on after the voting deadline passes.
  - Action: Open a poll whose voting deadline has passed; attempt to vote.
  - Expected: Voting is blocked; the poll is treated as ended.
- [ ] CS-05: A signed-in user cannot vote twice on the same poll.
  - Action: Vote once on a sign-in-required poll as the same user, then attempt to vote again.
  - Expected: The second vote is rejected; the user's single vote remains counted once.

## Interaction
- [ ] IX-01: Bar breakdown updates as votes are cast.
  - Action: View a poll's results, then cast a vote on it (from this or another session) without reloading the page.
  - Expected: The bar lengths/figures update to reflect the new totals.

## Content
- [ ] CT-01: Poll content is displayed exactly as created.
  - Action: Create a poll with a known question, description, and choice texts; view its voting page and dashboard entry.
  - Expected: Question, description, and all choice texts match the entered values in both places.
- [ ] CT-02: Results data is accurate and proportional to votes.
  - Action: After voting, compare the results view against the known votes per choice.
  - Expected: Each choice shows the correct vote count and percentage, and bar lengths are proportional to those counts.