# Test Result

## Functionality

- [X] FT-01: Registered user can create a poll with a question, description, and multiple choices
  - Action: Sign in, open the "Create Poll" form, enter question `Favorite season?`, description `Pick your favorite`, add choices `Spring`, `Summer`, `Autumn`, and submit.
  - Expected: Poll is created and its page shows the question, the description, and all three choices.

- [X] FT-02: Creator can set an optional voting deadline and choose the voting mode
  - Action: Create one poll with a future deadline and mode `Require sign-in`; create a second poll with no deadline and mode `Anonymous`. Open both afterwards.
  - Expected: Each poll displays the deadline it was given (or no deadline label when left blank) and displays the selected voting mode.
  - Note: "Deadline poll?" showed `Sign-in required` + `Ends Dec 31, 11:59 PM`; "Anon no-deadline poll?" showed `Anonymous` with no deadline label.

- [X] FT-03: Creator can copy a shareable poll link that others can open
  - Action: Open one of your polls, click the share/copy-link button, then paste the copied URL into a new browser tab.
  - Expected: A copy confirmation is shown, and the pasted link loads that same poll's voting page with its question and choices.
  - Note: Clipboard verified via `navigator.clipboard.readText()` → `http://localhost:6015/poll/poll-1`; the new tab rendered the question, description and all 4 choices.

- [X] FT-04: A voter can cast a vote through the shared link
  - Action: Open the shared link of an `Anonymous` poll in a separate browser window that is not signed in, select one choice, click `Vote`.
  - Expected: The vote is accepted, a confirmation appears, and the poll's total vote count increases by 1.
  - Note: Executed from a signed-out session; toast `Your vote has been recorded!` shown and `Total votes: 0 → 1`.

- [X] FT-05: Results are shown as bar-style breakdowns that update as votes are cast
  - Action: View results for a poll, note the bars, then cast another vote for a different choice from a second browser window and return to the results view.
  - Expected: Each choice is rendered as a bar with its vote count/percentage, and the bars/percentages change to include the new vote without a manual page reload.
  - Note: Bars carry inline widths and updated from `Yes 1 vote 100% / No 0 votes 0%` to `Yes 1 vote 50% / No 1 vote 50%` (widths `50%`,`50%`) with no browser reload. Caveat: the app stores all poll data only in memory (localStorage is empty), so a genuinely separate browser window loads the seeded polls only — the second vote had to be cast within the same SPA session.

- [X] FT-06: Creator can close a poll early and reopen it
  - Action: On your poll, click `Close poll`; confirm the state; then click `Reopen poll`.
  - Expected: Status changes to Closed and voting is rejected; after reopening, status returns to Open and a vote can be cast again.
  - Note: `Close` set the badge to `closed` and the voting page to "This poll is closed and no longer accepting votes." with 0 vote controls. Reopening works through the segmented control labelled `Open` (toast `Poll is now active and accepting votes`), after which `Submit Vote` returned. There is no control literally named "Reopen poll".

- [X] FT-07: Creator can switch a poll to read-only results
  - Action: On your poll, click the read-only results action (e.g. `Switch to read-only` / `Results only`).
  - Expected: Poll status shows Read-only, results remain visible, and no voting control is offered.
  - Note: `Read-only` → toast `Poll is now in read-only mode`, status text "Results are visible but voting is disabled", badge `readonly`, results bars intact, 0 vote buttons on the voting page.

- [X] FT-08: Dashboard lists all of my polls
  - Action: Sign in and open the dashboard / `My Polls`.
  - Expected: Every poll belonging to the signed-in user is listed, each showing title, creation date, and status.
  - Note: All 6 owned polls listed (3 seeded + 3 created), each with title, date (e.g. `Nov 8, 2026`) and status badge (`active`/`readonly`); filter counts confirmed `All (6) / Active (4) / Closed (0) / Readonly (2)`.

- [X] FT-09: Dashboard search filters polls by title
  - Action: Type a partial title of a known poll (e.g. `season`) into the dashboard search box, then clear it.
  - Expected: Only polls whose title contains the text remain listed; unrelated polls are hidden; clearing the box restores the full list.
  - Note: `season` → only `Favorite season?` remained (`Team Lunch` absent); clearing restored all 6.

- [ ] FT-10: Dashboard sort works by title, creation date, and status
  - Action: Use the sort control to sort the poll list by `Title`, then by `Creation date`, then by `Status`.
  - Expected: The list re-orders accordingly — titles in A→Z order, creation dates in chronological order, and entries grouped by status in each case.
  - Bug Report:
    - Issue: Missing sort option (Status sorting not implemented)
    - Actual: The sort control offers only four options — `Newest first`, `Oldest first`, `Title A-Z`, `Most votes` — and there is no `Status` option. Verified: `Title A-Z` correctly produced "Anon no-deadline poll?, Best Programming Language for Beginners?, Deadline poll?, Favorite season?, Office Pet Policy, Team Lunch Preference", and `Oldest first` was the exact reverse of `Newest first` (Best Programming Language… → Anon no-deadline poll?), so title and creation-date sorting work. However status can only be *filtered* via the `All / Active / Closed / Readonly` tabs, which hide polls rather than re-ordering/grouping the full list by status as expected.

## Constraint

- [ ] CS-01: Poll cannot be created with an empty question
  - Action: Open the create form, leave the Question field blank, fill in at least two choices, and submit.
  - Expected: Submission is blocked, an error message appears on/near the Question field, and no new poll is added to the dashboard.
  - Bug Report:
    - Issue: No validation error message surfaced (silent disabled control)
    - Actual: With Question cleared and two valid choices filled in, the `Create Poll` submit button is disabled (`isDisabled() === true`) and clicking it produces no navigation (URL stayed `http://localhost:6015/create`) and no new poll was created — so blocking works. However no error message is rendered on or near the Question field: the queried DOM contained no `[role="alert"]`/destructive-styled text, the toast region was empty (`toast = ""`), and the Question input carried no error styling or `aria-invalid` (its HTML is `<input class="... border-input ..." id="title" placeholder="What would you like to ask?" required="" value="">`). The user is given no indication of why submission is unavailable.

- [X] CS-02: Poll cannot be created with fewer than two choices
  - Action: On the create form, enter a valid question and leave only one choice (remove the others), then submit.
  - Expected: Submission is blocked and an error states that at least two choices are required; no poll is created.
  - Note: With a valid question and one choice blanked, submitting stayed on `/create` and raised the toast `Please add at least 2 options`; no poll was created. The remove (x) control is hidden once only two choice rows remain, so the row count cannot be driven below two from the UI.

- [ ] CS-03: A poll set to require sign-in blocks unauthenticated voting
  - Action: Open the shared link of a `Require sign-in` poll in a browser window that is not signed in and attempt to vote.
  - Expected: The vote is not recorded; the voter is prompted to sign in; after signing in, voting succeeds.
  - Bug Report:
    - Issue: Missing sign-in prompt / false confirmation shown to unauthenticated voter
    - Actual: Opening `http://localhost:6015/poll/poll-1794075914598` (mode `Sign-in required`) while signed out, the vote was correctly not recorded (`Total votes: 0`) and no voting control was rendered (only header `Log in` / `Sign up` links). But instead of being prompted to sign in, the page displayed `✓ Thank you for voting!` above the results, i.e. a false confirmation to a visitor who never voted. After signing in through the app, voting did succeed (`Your vote has been recorded!`, `Total votes: 1`), so only the "prompted to sign in" part of the expectation fails.

- [X] CS-04: A poll past its voting deadline no longer accepts votes
  - Action: Create a poll with a deadline in the past, open its voting page, and attempt to vote.
  - Expected: Voting is not possible, the poll shows a closed/expired state, and results remain viewable.
  - Note: The create form enforces `min="2026-11-07T18:32"` on the datetime-local input, so a past deadline had to be forced by removing the `min` attribute. The resulting poll showed `Expired Jan 1` and "This poll has expired and is no longer accepting votes.", with `0` `Submit Vote` buttons, while results (`X 0 votes 0%`, `Y 0 votes 0%`, `Total votes: 0`) stayed viewable.

- [ ] CS-05: A signed-in voter cannot vote twice on the same poll
  - Action: On a `Require sign-in` poll, sign in as a voter, cast a vote, then return to the same poll and try to vote again.
  - Expected: The second attempt is rejected with an "already voted" indication, the earlier choice is shown as selected, and the total count is unchanged.
  - Bug Report:
    - Issue: No "already voted" indication; earlier choice not marked as selected
    - Actual: After signing in, voting for `Alpha` succeeded (`Total votes: 1`). Returning to `http://localhost:6015/poll/poll-1794075914598` shows only `✓ Thank you for voting!` followed by `Alpha 1 vote 100%` and `Beta 0 votes 0%` — there is no "already voted" text (regex `/already voted|you have already|voted already/i` → false) and no marker distinguishing the voter's earlier choice (`/your choice|your vote|you voted/i` → false); the selected choice is not visually indicated. The total count is unchanged (1) and no second vote can be submitted, so duplicate voting is prevented, but the expected indication/selection state is missing.

## Interaction

- [X] IX-01: Choice fields can be added and removed while creating a poll
  - Action: On the create form, click `Add choice`, then click the remove control on the added field.
  - Expected: A new empty choice input appears immediately when added and disappears when removed, leaving the remaining fields intact.
  - Note: `Add Option` took the row count 2 → 3; removing the added row returned it to 2 with `Option 1 = "Spring"` and `Option 2 = "Summer"` still intact.

- [X] IX-02: Success feedback is shown after a poll is created
  - Action: Submit a valid poll creation form.
  - Expected: A success message/notification appears and the view moves to the new poll or to the dashboard listing it.
  - Note: Toast `Poll created successfully!` and the view moved to `/manage/poll-<new-id>`.

- [X] IX-03: Selecting a choice gives immediate visual feedback before submitting
  - Action: On the voting page, click one choice option.
  - Expected: The clicked choice is visually marked as selected and the `Vote` control becomes active; the selection is visible before submission.
  - Note: `Submit Vote` was disabled before selection and enabled after. The clicked choice changed classes from `border-border bg-card` to `border-primary bg-accent shadow-md` with the label turning `text-primary` and the radio circle filled `border-primary bg-primary`, while the other choice kept its unselected styling.

## Content

- [X] CT-01: Voting page shows all poll information supplied by the creator
  - Action: Open the voting page of a default poll that has a description, a deadline, and a voting mode set.
  - Expected: The question, description, every choice, the deadline (or an explicit "no deadline" state), and the voting mode are all displayed; no placeholder/lorem text and no unrelated content.
  - Note: `http://localhost:6015/poll/poll-1` rendered question `Best Programming Language for Beginners?`, its description, all 4 choices, deadline `Expired Dec 31`, and mode `Anonymous voting`; no placeholder/lorem or unrelated content present.

- [X] CT-02: Results content matches the poll's choices and vote data
  - Action: Open the results view of a poll that already has default votes and compare labels, bars, counts, and percentages against the choices.
  - Expected: Every choice appears exactly once with its correct label, a bar, a vote count, and a percentage; percentages total ~100%; no duplicate, missing, `N/A`, or `undefined` entries.
  - Note: `Python 45 votes 42%`, `JavaScript 32 votes 30%`, `Scratch 18 votes 17%`, `Java 12 votes 11%`, each once with an inline bar width (`42.0561%`, `29.9065%`, `16.8224%`, `11.215%` — summing to 100%); `Total votes: 107` equals 45+32+18+12; displayed percentages sum to 100%; no `undefined`/`NaN`/`N/A`/`null` tokens found.
