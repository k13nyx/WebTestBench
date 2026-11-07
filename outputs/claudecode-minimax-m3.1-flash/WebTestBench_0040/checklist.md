# Test Checklist

## Functionality
- [ ] FT-01: User can create a new task on the Kanban board
  - Action: Click the "New Task" / "+ Add Task" button, enter a task title (e.g., "Ship release notes"), and submit.
  - Expected: A task card with the entered title appears in the board's default/first column (To Do), and the card count for that column increases by 1.

- [ ] FT-02: User can assign a task to a specific teammate
  - Action: Open the task creation form (or a newly created task), open the assignee selector, pick one of the listed teammates, and save.
  - Expected: The task card shows the selected teammate's name (or avatar/name) on the card, and the detail view for that task lists the same assignee.

- [ ] FT-03: User can set a due date on a task
  - Action: Open the task form, set the due date field to a valid future date (e.g., 2026-12-01), and save.
  - Expected: The task card displays the due date, and the task detail view shows the same due date.

- [ ] FT-04: User can move a task between columns to update its status
  - Action: Drag the card "Ship release notes" from the To Do column into the In Progress column.
  - Expected: The card is no longer in To Do, appears in In Progress, and the card's status/labels now reflect "In Progress".

- [ ] FT-05: User can open a task to see its full details
  - Action: Click a task card's title or a "Details"/"Open" affordance on the card.
  - Expected: A task detail view/modal opens showing the task title, assignee, due date, status, and existing notes/status updates.

- [ ] FT-06: User can edit a task's information
  - Action: In the open task detail view, change the title, description, assignee, and due date, then save.
  - Expected: The edited values are displayed in the detail view and on the task card after closing it (e.g., changed title appears on the board).

- [ ] FT-07: User can add a short note to a task
  - Action: In the open task detail view, type text into the note/comment field (e.g., "Waiting on API schema") and submit.
  - Expected: The note is appended to the task's notes/status-update list with the entered text.

- [ ] FT-08: User can add a status update to a task
  - Action: In the open task detail view, use the status update control to post a short progress message (e.g., "50% done") and submit.
  - Expected: The status update appears in the task's activity/status-update list in chronological order with the posted text.

- [ ] FT-09: User can filter the board by assignee
  - Action: Select a teammate (e.g., "Alice") in the board's filter control by assignee.
  - Expected: Only tasks assigned to that teammate remain visible on the board; tasks assigned to other people are hidden.

- [ ] FT-10: User can filter the board by status
  - Action: Select a status (e.g., "In Progress") in the board's filter control by status.
  - Expected: Only tasks in that status are displayed, and all of them are shown in the corresponding column.

- [ ] FT-11: User can clear an active filter to restore the full board
  - Action: With a filter applied, click "Clear filter" / "All" / the filter's reset control.
  - Expected: All default tasks reappear across all columns.

## Constraint
- [ ] CS-01: Task title is required when creating a task
  - Action: Open the new task form, leave the title field empty, and submit.
  - Expected: Submission is blocked, an inline validation message appears on/next to the title field (e.g., "Title is required"), and no task card is created.

- [ ] CS-02: Due date must be a valid date within an acceptable range
  - Action: In the task form, attempt to enter an invalid date value (e.g., "abc" / "13/45/2026") in the due date field and save.
  - Expected: The invalid date is rejected (validation message or field refuses the value) and the task's due date is not saved as an invalid value.

- [ ] CS-03: A task cannot be moved into a column that does not exist
  - Action: Attempt to drag a card to a target area that is not a valid board column (e.g., empty space outside all columns).
  - Expected: The card snaps back to its original column and its status is unchanged.

- [ ] CS-04: Notes cannot be submitted empty
  - Action: In the task detail view, click the note/post submit button with the note field empty.
  - Expected: No empty note or blank entry is added to the notes list, and an indication that text is required appears.

- [ ] CS-05: Assignee selection is restricted to existing teammates
  - Action: Open the assignee selector in the task form and inspect the available options.
  - Expected: The list contains only the pre-existing team members from the application's default data, with no arbitrary free-text entry.

- [ ] CS-06: Filters combine correctly (assignee + status)
  - Action: Apply an assignee filter (Alice) and then a status filter (In Progress), and observe the board.
  - Expected: Only tasks that match both conditions are shown; tasks that match only one are hidden.

## Interaction
- [ ] IX-01: Creating a task gives immediate visual feedback
  - Action: Submit the new task form for a task titled "Ship release notes".
  - Expected: A success confirmation (e.g., toast/inline message) appears and the new card is immediately visible on the board.

- [ ] IX-02: Card is highlighted/visually emphasized when filtered
  - Action: Apply an assignee filter and compare the appearance of matching vs. non-matching cards.
  - Expected: Matching cards remain fully visible/normal while non-matching cards are visibly dimmed, faded, or otherwise distinguished (not merely hidden), consistent with the app's highlight behavior.

- [ ] IX-03: Task detail view can be opened and closed
  - Action: Open a task card, then close the detail view via the close button, the X, or by pressing Escape.
  - Expected: The detail view dismisses and the board is fully visible again with the card still in place.

- [ ] IX-04: Task detail view updates live after an edit
  - Action: With the task detail view open, change the assignee or status and save.
  - Expected: The change is reflected immediately in the detail view and on the card behind it without requiring a page reload.

- [ ] IX-05: Moving a card gives feedback that the move was registered
  - Action: Drag a card from one column to another and observe both columns.
  - Expected: The target column's card count increments and the source column's count decrements as a result of the drop.

- [ ] IX-06: Filter controls show the currently active filter
  - Action: Apply the "Alice" assignee filter and look at the filter control.
  - Expected: The control indicates that "Alice" is the active filter (e.g., selected chip/dropdown value or highlighted state).

## Content
- [ ] CT-01: Kanban board displays the expected status columns
  - Action: Inspect the board's column headers on load.
  - Expected: Columns representing the task workflow (e.g., To Do, In Progress, Done) are present and clearly labeled.

- [ ] CT-02: Task card displays title, assignee, and due date
  - Action: Inspect any default task card on the board.
  - Expected: The card shows the task title, the assignee's name/avatar, and the due date, all with readable labels and no placeholder text such as "Lorem ipsum" or "TBD" unless that is the actual default data value.

- [ ] CT-03: Task detail view lists all task fields and updates without placeholders
  - Action: Open a default task and review each field.
  - Expected: Title, description/details, assignee, due date, and status all contain the task's actual default data, with no empty or dummy values.

- [ ] CT-04: Notes and status updates display authored content and timestamps
  - Action: Open a task that has at least one existing note/status update (from default data) and review the list.
  - Expected: Each entry shows the entered text, the author, and an indication of when it was posted.

- [ ] CT-05: All visible content is relevant to task management
  - Action: Review all headings, labels, buttons, and empty-state text on the page.
  - Expected: Text refers to tasks, teammates, statuses, due dates, and notes — no unrelated marketing copy, placeholder lorem text, or broken/empty labels.