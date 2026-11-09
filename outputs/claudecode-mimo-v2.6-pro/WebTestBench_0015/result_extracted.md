# Test Result

## Functionality
- [X] FT-01: Create a poll with question, description, and multiple choices.
  - Action: Fill the poll form with a Question, a Description, and 3 choices; click "Create Poll".
  - Expected: Poll is created and appears in the dashboard with the entered question.
- [X] FT-02: Voting deadline is optional and can be set or omitted.
  - Action: Create one poll with a future "Voting deadline" set, and one with the deadline left empty.
  - Expected: Both polls are created; the deadline is shown on the first poll and absent on the second.
- [X] FT-03: Poll creator can choose anonymous voting or sign-in-required voting.
  - Action: Create one poll selecting the "Anonymous" mode and another selecting "Require sign-in".
  - Expected: Both polls are created and display their selected voting mode.
- [ ] FT-04: Poll creator can share a link that lets others vote.
  - Action: Open a poll from the dashboard, use the "Share"/"Copy link" control, open the copied link.
  - Expected: The link opens the poll's voting page showing the question and choices.
  - Bug Report:
    - Issue: Broken Share Link / Poll Data Not Persisted
    - Actual: The "Copy" control works ("Link copied to clipboard!", link = http://localhost:6015/poll/poll-1794123842710), but opening the copied link in any other session (new tab, signed-out or signed-in) renders "Poll Not Found — This poll may have been deleted or the link is incorrect." instead of the voting page with question and choices. Created polls exist only in the creating tab's in-memory state (localStorage, sessionStorage, cookies and IndexedDB are all empty), so no one else — not even a new tab of the creator's own browser — can open the poll.
- [ ] FT-05: A voter can submit a vote on an open poll.
  - Action: Open a shared poll link, select one choice, click "Vote".
  - Expected: The vote is accepted and recorded for that choice.
  - Bug Report:
    - Issue: Broken Share Link — Voting Unreachable for Voters
    - Actual: The first step of the action fails: opening the shared poll link (e.g. http://localhost:6015/poll/poll-1794123842710) in a voter's session shows "Poll Not Found" with no choices and no Vote button, so no choice can be selected and no vote can be submitted via the shared link. (Voting only works inside the very tab that created the poll, reached via the home-page listing: selecting "Spring Breeze" + "Submit Vote" then shows "Your vote has been recorded!" — but that path is not available to any voter.)
- [X] FT-06: Voter sees results after voting.
  - Action: Submit a vote on an open poll, then view the page.
  - Expected: A results view (bar-style breakdown) is displayed after voting.
- [X] FT-07: Poll creator can close a poll early.
  - Action: On the creator's poll, click "Close poll".
  - Expected: The poll status changes to closed and is shown as closed.
- [X] FT-08: Poll creator can reopen a closed poll.
  - Action: On a closed poll, click "Reopen".
  - Expected: The poll becomes open again and accepts votes.
- [X] FT-09: Poll creator can switch a poll to read-only results.
  - Action: On the creator's poll, select "Read-only results".
  - Expected: The poll shows results only; the voting form is no longer offered.
- [X] FT-10: Dashboard lists the user's polls.
  - Action: Open the dashboard page.
  - Expected: A list of the user's polls is displayed with title and status per poll.
- [X] FT-11: Dashboard search filters the poll list.
  - Action: Enter a keyword from an existing poll's title in the dashboard search box.
  - Expected: The list shows only matching polls; clearing the search restores the full list.
- [ ] FT-12: Dashboard can sort polls by title, creation date, and status.
  - Action: Use the "Sort by" control and select Title, then Creation date, then Status.
  - Expected: The list reorders accordingly each time (ascending/descending as labeled).
  - Bug Report:
    - Issue: Missing Sort Option (Status)
    - Actual: The sort dropdown offers only "Newest first", "Oldest first", "Title A-Z", "Most votes" — there is no "Status" option, so sorting by status cannot be performed. Title A-Z correctly reorders ascending (Best Programming Language… → Office Pet Policy → QA Favorite Season? → QA Lunch Venue? → Team Lunch Preference) and Newest/Oldest first correctly reorder by creation date in both directions, but the Status sort required by the expected behavior does not exist.

## Constraint
- [ ] CS-01: Poll cannot be created with a missing question or invalid choices.
  - Action: Attempt to create a poll with an empty Question; then attempt with fewer than two choices or a blank choice text.
  - Expected: Creation is blocked both times; the missing field (question / choices) is identified.
  - Bug Report:
    - Issue: Missing Validation Feedback for Empty Question
    - Actual: With an empty Question (options filled), creation is blocked only by a disabled "Create Poll" button — no error message or field indicator identifies the Question as the missing field (only the always-visible "Question *" label). The blank-choice case behaves correctly ("Please add at least 2 options" is shown and creation is blocked), so the question case deviates from "the missing field is identified".
- [ ] CS-02: Sign-in-required poll blocks signed-out voters.
  - Action: Open the share link of a "Require sign-in" poll in a signed-out state and try to vote.
  - Expected: Voting is blocked with a prompt to sign in; no vote is recorded.
  - Bug Report:
    - Issue: No Sign-in Prompt — Share Link Renders "Poll Not Found"
    - Actual: Opening the "Require sign-in" poll's share link (http://localhost:6015/poll/poll-1794123876344) in a signed-out session renders "Poll Not Found — This poll may have been deleted or the link is incorrect." No poll content and no sign-in prompt are shown (only nav "Log in"/"Sign up"). No vote is recorded, but the expected prompt to sign in never appears. The demo sign-in poll (/poll/poll-2) signed-out likewise shows only "This poll has expired and is no longer accepting votes." with no sign-in prompt.
- [X] CS-03: Closed or read-only polls cannot be voted on.
  - Action: Open the share link of a closed poll and of a read-only poll; attempt to vote.
  - Expected: Voting is blocked on both; only results are viewable.
- [X] CS-04: Poll cannot be voted on after the voting deadline passes.
  - Action: Open a poll whose voting deadline has passed; attempt to vote.
  - Expected: Voting is blocked; the poll is treated as ended.
- [X] CS-05: A signed-in user cannot vote twice on the same poll.
  - Action: Vote once on a sign-in-required poll as the same user, then attempt to vote again.
  - Expected: The second vote is rejected; the user's single vote remains counted once.

## Interaction
- [ ] IX-01: Bar breakdown updates as votes are cast.
  - Action: View a poll's results, then cast a vote on it (from this or another session) without reloading the page.
  - Expected: The bar lengths/figures update to reflect the new totals.
  - Bug Report:
    - Issue: No Live Update of Results Breakdown (Realtime/Cross-Session Update Non-Functional)
    - Actual: The breakdown can never be observed updating in place. (1) Another session cannot open the poll at all ("Poll Not Found" via the share link), so no vote can be cast from elsewhere while a results view is open. (2) Within a session, the results breakdown is only rendered after voting — an open poll's voting page shows just the choice buttons ("Spring Breeze | Summer Sun | Autumn Leaves | Submit Vote") before voting — so no results view is on screen at vote time to update. Bar widths are applied once per render (`--target-width: 100% / 0% / 0%`) and the "Live breakdown of all votes" panel only reflects state changes after navigation, never live vote arrivals.

## Content
- [X] CT-01: Poll content is displayed exactly as created.
  - Action: Create a poll with a known question, description, and choice texts; view its voting page and dashboard entry.
  - Expected: Question, description, and all choice texts match the entered values in both places.
- [X] CT-02: Results data is accurate and proportional to votes.
  - Action: After voting, compare the results view against the known votes per choice.
  - Expected: Each choice shows the correct vote count and percentage, and bar lengths are proportional to those counts.
