# Test Result

## Functionality
- [X] FT-01: Create a poll with complete details
  - Action: Fill in Question, Description, at least two Choice fields, select a Voting Deadline, choose "Anonymous" mode, and click the "Create Poll" button.
  - Expected: Poll is successfully created and the creator is redirected to the poll overview page.
- [X] FT-02: Cast a vote on an anonymous poll
  - Action: Open an active anonymous poll link as an unauthenticated user, select an option, and click "Submit Vote".
  - Expected: Vote is accepted and recorded without prompting for login.
- [X] FT-03: Cast a vote on a sign-in required poll
  - Action: Log in to a registered voter account, open a poll configured with "Require Sign-In", select an option, and click "Submit Vote".
  - Expected: Vote is accepted and successfully recorded under the authenticated account.
- [X] FT-04: Display post-vote results to voter
  - Action: Submit a valid vote on an active poll.
  - Expected: The view immediately transitions to display the visual results breakdown.
- [X] FT-05: Share poll link
  - Action: On the poll detail page, click the "Share" button to copy the poll URL.
  - Expected: The direct voting link is copied to the system clipboard.
- [X] FT-06: Close an active poll early
  - Action: As the poll creator, navigate to poll management and click "Close Poll".
  - Expected: Poll status changes to "Closed" and further voting is stopped.
- [X] FT-07: Reopen a closed poll
  - Action: As the poll creator, open a closed poll and click "Reopen Poll".
  - Expected: Poll status reverts to "Active" and voting is re-enabled.
- [X] FT-08: Switch poll to read-only results mode
  - Action: As the poll creator, select the "Set to Read-Only" option in poll management.
  - Expected: Poll status updates to "Read-Only" and voting inputs are removed while results remain visible.
- [X] FT-09: Search polls by title on dashboard
  - Action: Type an existing poll title into the dashboard "Search" bar and press Enter.
  - Expected: Dashboard list filters to display only polls with matching titles.
- [ ] FT-10: Sort polls on dashboard
  - Action: Select "Title", "Creation Date", and "Status" sequentially from the dashboard "Sort By" dropdown.
  - Expected: Dashboard list reorders accurately based on each selected sorting criterion.
  - Bug Report:
    - Issue: Missing Sort Options
    - Actual: The "Sort By" dropdown only provides "Newest first", "Oldest first", "Title A-Z", and "Most votes". It does not provide options named "Creation Date" or "Status", preventing sorting sequentially by those criteria via the dropdown.

## Constraint
- [ ] CS-01: Validate mandatory poll creation fields
  - Action: Leave the Question field empty, provide only one choice, and click "Create Poll".
  - Expected: Form submission is blocked and validation error messages indicate required fields and the two-choice minimum.
  - Bug Report:
    - Issue: Missing Field Validation Error Messages
    - Actual: When the Question field is empty, the "Create Poll" button is disabled (`disabled`), preventing form submission. No inline validation error messages indicating required fields or the two-choice minimum are displayed to the user.
- [X] CS-02: Prevent voting on closed or expired polls
  - Action: Open a poll link where the status is "Closed" or the deadline timestamp is in the past.
  - Expected: Choice selection and "Submit Vote" button are disabled, and a notice indicates voting has ended.
- [X] CS-03: Block unauthenticated voting on sign-in required polls
  - Action: Open a poll configured with "Require Sign-In" mode while logged out.
  - Expected: Voting is blocked and a prompt redirecting to the sign-in page is displayed.
- [X] CS-04: Prevent voting on read-only polls
  - Action: Access the public link of a poll marked as "Read-Only".
  - Expected: Voting controls are absent or disabled, preventing any new vote submission.

## Interaction
- [X] IX-01: Dynamically add and remove poll choices
  - Action: In the poll creator form, click "+ Add Choice", enter text, and then click the "Delete" icon next to an added choice.
  - Expected: A new choice input field is appended dynamically, and clicking "Delete" removes that specific field immediately.
- [X] IX-02: Provide feedback upon copying share link
  - Action: Click the "Share" or "Copy Link" button on a poll page.
  - Expected: A confirmation toast or tooltip with text "Link copied to clipboard" appears temporarily.
- [ ] IX-03: Real-time update of visual results
  - Action: Keep the visual results page open while casting a vote from a separate browser session.
  - Expected: The bar graphs and vote tally figures update in real time without a manual page refresh.
  - Bug Report:
    - Issue: Missing Cross-Session Real-Time Synchronization
    - Actual: Poll state is stored exclusively in client-side React memory (`useState(defaultPolls)` in `PollContext`), without backend or cross-tab synchronization. Votes cast from a separate browser session are neither propagated nor displayed in real time without a manual page reload.

## Content
- [X] CT-01: Display visual bar-style results breakdown
  - Action: View the results section of a poll with cast votes.
  - Expected: Each choice shows a proportional horizontal bar, exact vote count, and percentage share of total votes.
- [X] CT-02: Display complete poll metadata on dashboard
  - Action: View the creator dashboard poll list.
  - Expected: Each entry displays the poll title, creation date, and current status badge ("Active", "Closed", or "Read-Only").
