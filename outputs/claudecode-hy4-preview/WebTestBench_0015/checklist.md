# Test Checklist

## Functionality
- [ ] FT-01: Registered user can create a poll with a question, description, and multiple choices
  - Action: Sign in, open the "Create Poll" form, enter question `Favorite season?`, description `Pick your favorite`, add choices `Spring`, `Summer`, `Autumn`, and submit.
  - Expected: Poll is created and its page shows the question, the description, and all three choices.

- [ ] FT-02: Creator can set an optional voting deadline and choose the voting mode
  - Action: Create one poll with a future deadline and mode `Require sign-in`; create a second poll with no deadline and mode `Anonymous`. Open both afterwards.
  - Expected: Each poll displays the deadline it was given (or no deadline label when left blank) and displays the selected voting mode.

- [ ] FT-03: Creator can copy a shareable poll link that others can open
  - Action: Open one of your polls, click the share/copy-link button, then paste the copied URL into a new browser tab.
  - Expected: A copy confirmation is shown, and the pasted link loads that same poll's voting page with its question and choices.

- [ ] FT-04: A voter can cast a vote through the shared link
  - Action: Open the shared link of an `Anonymous` poll in a separate browser window that is not signed in, select one choice, click `Vote`.
  - Expected: The vote is accepted, a confirmation appears, and the poll's total vote count increases by 1.

- [ ] FT-05: Results are shown as bar-style breakdowns that update as votes are cast
  - Action: View results for a poll, note the bars, then cast another vote for a different choice from a second browser window and return to the results view.
  - Expected: Each choice is rendered as a bar with its vote count/percentage, and the bars/percentages change to include the new vote without a manual page reload.

- [ ] FT-06: Creator can close a poll early and reopen it
  - Action: On your poll, click `Close poll`; confirm the state; then click `Reopen poll`.
  - Expected: Status changes to Closed and voting is rejected; after reopening, status returns to Open and a vote can be cast again.

- [ ] FT-07: Creator can switch a poll to read-only results
  - Action: On your poll, click the read-only results action (e.g. `Switch to read-only` / `Results only`).
  - Expected: Poll status shows Read-only, results remain visible, and no voting control is offered.

- [ ] FT-08: Dashboard lists all of my polls
  - Action: Sign in and open the dashboard / `My Polls`.
  - Expected: Every poll belonging to the signed-in user is listed, each showing title, creation date, and status.

- [ ] FT-09: Dashboard search filters polls by title
  - Action: Type a partial title of a known poll (e.g. `season`) into the dashboard search box, then clear it.
  - Expected: Only polls whose title contains the text remain listed; unrelated polls are hidden; clearing the box restores the full list.

- [ ] FT-10: Dashboard sort works by title, creation date, and status
  - Action: Use the sort control to sort the poll list by `Title`, then by `Creation date`, then by `Status`.
  - Expected: The list re-orders accordingly — titles in A→Z order, creation dates in chronological order, and entries grouped by status in each case.

## Constraint
- [ ] CS-01: Poll cannot be created with an empty question
  - Action: Open the create form, leave the Question field blank, fill in at least two choices, and submit.
  - Expected: Submission is blocked, an error message appears on/near the Question field, and no new poll is added to the dashboard.

- [ ] CS-02: Poll cannot be created with fewer than two choices
  - Action: On the create form, enter a valid question and leave only one choice (remove the others), then submit.
  - Expected: Submission is blocked and an error states that at least two choices are required; no poll is created.

- [ ] CS-03: A poll set to require sign-in blocks unauthenticated voting
  - Action: Open the shared link of a `Require sign-in` poll in a browser window that is not signed in and attempt to vote.
  - Expected: The vote is not recorded; the voter is prompted to sign in; after signing in, voting succeeds.

- [ ] CS-04: A poll past its voting deadline no longer accepts votes
  - Action: Create a poll with a deadline in the past, open its voting page, and attempt to vote.
  - Expected: Voting is not possible, the poll shows a closed/expired state, and results remain viewable.

- [ ] CS-05: A signed-in voter cannot vote twice on the same poll
  - Action: On a `Require sign-in` poll, sign in as a voter, cast a vote, then return to the same poll and try to vote again.
  - Expected: The second attempt is rejected with an "already voted" indication, the earlier choice is shown as selected, and the total count is unchanged.

## Interaction
- [ ] IX-01: Choice fields can be added and removed while creating a poll
  - Action: On the create form, click `Add choice`, then click the remove control on the added field.
  - Expected: A new empty choice input appears immediately when added and disappears when removed, leaving the remaining fields intact.

- [ ] IX-02: Success feedback is shown after a poll is created
  - Action: Submit a valid poll creation form.
  - Expected: A success message/notification appears and the view moves to the new poll or to the dashboard listing it.

- [ ] IX-03: Selecting a choice gives immediate visual feedback before submitting
  - Action: On the voting page, click one choice option.
  - Expected: The clicked choice is visually marked as selected and the `Vote` control becomes active; the selection is visible before submission.

## Content
- [ ] CT-01: Voting page shows all poll information supplied by the creator
  - Action: Open the voting page of a default poll that has a description, a deadline, and a voting mode set.
  - Expected: The question, description, every choice, the deadline (or an explicit "no deadline" state), and the voting mode are all displayed; no placeholder/lorem text and no unrelated content.

- [ ] CT-02: Results content matches the poll's choices and vote data
  - Action: Open the results view of a poll that already has default votes and compare labels, bars, counts, and percentages against the choices.
  - Expected: Every choice appears exactly once with its correct label, a bar, a vote count, and a percentage; percentages total ~100%; no duplicate, missing, `N/A`, or `undefined` entries.