# Test Checklist

## Functionality
- [ ] FT-01: Registered user can create a poll with a question, description, and multiple choices.
  - Action: Sign in, open the create-poll form, enter question "Best lunch spot?", description "Pick one option", choices "Pizza", "Sushi", "Tacos", select Anonymous mode, and submit.
  - Expected: The poll is saved and its page shows the question, description, and all three choices in the entered order.
- [ ] FT-02: Creator can share a poll link that lets others vote.
  - Action: On the poll page, click the share/copy-link control, then open the copied link in a private window without signing in.
  - Expected: The poll loads and the choices are selectable and votable (Anonymous mode).
- [ ] FT-03: Voter's submitted vote is recorded and results appear immediately.
  - Action: Select "Sushi" on an open poll and click the vote button.
  - Expected: The vote is accepted and a bar-style breakdown appears showing vote counts and percentages for every choice.
- [ ] FT-04: Creator can close a poll early and then reopen it.
  - Action: On an open poll you created, click "Close Poll", then click "Reopen Poll".
  - Expected: Status changes to Closed after the first click and back to Open after the second; voting is blocked only while Closed.
- [ ] FT-05: Creator can switch a poll to read-only results.
  - Action: On a poll you created, select the "Read-only results" option.
  - Expected: The voting controls disappear, results remain visible, and the status shows Read-only.
- [ ] FT-06: Dashboard lists the signed-in user's polls with title, creation date, and status.
  - Action: Sign in and open the Dashboard.
  - Expected: Only polls created by this user are listed, each showing its title, creation date, and status.
- [ ] FT-07: Dashboard search filters polls by title.
  - Action: Type a distinctive part of an existing poll's title into the search box.
  - Expected: Only polls whose titles contain the typed text remain listed; clearing the box restores the full list.
- [ ] FT-08: Dashboard sorting orders polls by title, creation date, and status.
  - Action: Choose "Title (A–Z)", then "Created (newest first)", then "Status" from the sort control.
  - Expected: The list reorders correctly for each option (titles alphabetical; dates newest first; grouped by status).

## Constraint
- [ ] CS-01: Poll cannot be created without a question and at least two choices.
  - Action: Open the create-poll form, leave the question empty and enter only one choice, then submit.
  - Expected: Submission is blocked, error messages name the missing question and the minimum of two choices, and no poll is created.
- [ ] CS-02: Voting deadline must be a future date and time.
  - Action: In the create-poll form, set the deadline to yesterday's date and submit.
  - Expected: Submission is rejected with a message that the deadline must be in the future.
- [ ] CS-03: In sign-in-required mode, anonymous visitors cannot vote.
  - Action: Open an existing sign-in-required poll in a private window without signing in and attempt to vote.
  - Expected: The vote is not accepted and the page prompts the visitor to sign in; results are not changed.
- [ ] CS-04: A registered user can vote only once per poll.
  - Action: Sign in, vote on a poll, then attempt to vote again on the same poll.
  - Expected: The second vote is blocked with the message "You have already voted," and the vote count does not increase.
- [ ] CS-05: Closed, read-only, or deadline-expired polls reject new votes.
  - Action: Open one closed poll, one read-only poll, and one poll whose deadline has passed; check the voting controls on each.
  - Expected: No voting controls are active on any of them; the status shows Closed, Read-only, or Expired respectively.

## Interaction
- [ ] IX-01: Bar results update live when other votes are cast, without reloading.
  - Action: Open an open poll in two windows, vote in one window, and watch the other window without refreshing.
  - Expected: The bar lengths, vote counts, and percentages in the second window update to reflect the new vote.
- [ ] IX-02: Closing, reopening, or switching to read-only shows feedback and updates the control label.
  - Action: On a poll you created, click "Close Poll," then "Reopen Poll," then choose read-only.
  - Expected: Each action shows a confirmation message ("Poll closed," "Poll reopened," "Poll set to read-only"), and the action button label changes to match the next available action.
- [ ] IX-03: After voting, choice selection locks and a confirmation appears.
  - Action: Vote on an open poll, then try clicking a different choice.
  - Expected: A "Vote recorded" confirmation appears, and the choices can no longer be changed.

## Content
- [ ] CT-01: Poll page text matches the poll's saved question, description, and choices exactly.
  - Action: Open an existing poll and compare its displayed question, description, and choice labels with the values shown in its edit view or creation record.
  - Expected: All text matches exactly, with no truncation, placeholder text, or missing choices.
- [ ] CT-02: Result percentages match vote counts.
  - Action: Open a poll with at least three votes and note each choice's count and percentage.
  - Expected: Each percentage equals that choice's count divided by the total votes (rounded), and the percentages total 100%.
- [ ] CT-03: Dashboard status labels and creation dates are accurate.
  - Action: Compare the status and creation date shown for three of your polls on the Dashboard with each poll's detail page.
  - Expected: Status and creation date match on both views for every poll checked.