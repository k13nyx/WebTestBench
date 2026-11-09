# Test Result

## Functionality
- [X] FT-01: User can create a new task with title, assignee, and due date
  - Action: Click "New Task"/"Add Task" button, fill in title, select a teammate from assignee dropdown, pick a future date, and save.
  - Expected: A new task card appears in the first column (e.g., "To Do") with the entered title, assignee name, and due date visible.

- [X] FT-02: User can move a task between columns to change its status
  - Action: Drag (or use a status control on) an existing task card from one column to another column (e.g., "To Do" → "In Progress").
  - Expected: The task card is removed from the source column and appears in the destination column; its status reflects the new column.

- [X] FT-03: User can open a task to view its full details
  - Action: Click on an existing task card.
  - Expected: A detail view (modal or panel) opens showing the task's title, description, assignee, due date, status, and a list/area for status updates or notes.

- [X] FT-04: User can edit a task's information
  - Action: Open a task, change its title and/or assignee and/or due date, and save the changes.
  - Expected: The task card and its detail view reflect the updated values; closing and reopening shows the edits persisted.

- [X] FT-05: User can add a status update / short note to a task
  - Action: Open an existing task, type a note in the status/comment input, and submit it.
  - Expected: The note is added to the task's update history inside the detail view with the entered text visible.

- [X] FT-06: User can filter the board by assignee
  - Action: Select a teammate from the assignee filter control.
  - Expected: Only tasks assigned to that teammate are visible on the board; other tasks are hidden (or clearly de-emphasized if highlighting is used).

- [X] FT-07: User can filter the board by status
  - Action: Select a status/column from the status filter control.
  - Expected: Only tasks matching that status are visible, OR only the matching column is shown depending on the app's design.

## Constraint
- [ ] CS-01: Task cannot be created without a title
  - Action: Click "New Task", leave the title field empty, fill other fields, and attempt to save.
  - Expected: Save is blocked and a validation message indicates the title is required; no empty task is created.
  - Bug Report:
    - Issue: Missing Inline Validation Message
    - Actual: The "Create Task" button is correctly disabled for an empty (and whitespace-only) title, the click is blocked, and no task is created — but no validation message ever appears. The title field has no `aria-invalid`/`aria-describedby`, and the only indication is the static "Title *" label. The dialog text after the blocked attempt was unchanged: "Create New Task | Title * | Description | Status | To Do | ... | Create Task | Close".

- [ ] CS-02: Due date entered must be a valid future (or current) date format
  - Action: Attempt to enter an invalid value (e.g., past date or malformed text) into the due date field when creating/editing a task.
  - Expected: Input is rejected or corrected; the task does not save with an invalid/inconsistent due date.
  - Bug Report:
    - Issue: Missing Date Validation (Past Date Accepted)
    - Actual: Malformed text is rejected (typing "not-a-date" into `input[type=date]#dueDate` leaves the value empty), but a past date is accepted and saved with no correction: the `#dueDate` input has no `min` attribute and no validation message, so "CS02 Past Due Task" was created with due date 2020-01-15 and persisted on the board, where the card renders it as "Jan 15" (no year), displaying a 2020 date as if it were upcoming.

- [ ] CS-03: Task persistence — created task survives page reload
  - Action: Create a new task, then refresh the page.
  - Expected: The newly created task remains visible in its column with title, assignee, due date, and any notes intact.
  - Bug Report:
    - Issue: State Lost on Reload (No Persistence)
    - Actual: After creating "Persistence Check Task" (To Do, assignee Alex Chen, due Feb 10, note badge showing 1 note) and reloading, the board reverted to the 8 seeded tasks (card count 8, badges "To Do=3, In Progress=2, Review=1, Done=2"). The new task, its note, and the earlier drag/edit changes were all gone; `localStorage` and `sessionStorage` were both empty.

- [X] CS-04: Status update / note cannot be saved empty
  - Action: Open a task, leave the note input blank, and attempt to submit.
  - Expected: Submission is blocked (button disabled or validation message shown); no blank note is appended to the history.

## Interaction
- [X] IX-01: Filter by assignee visually highlights matching tasks
  - Action: Apply an assignee filter for one teammate.
  - Expected: Tasks belonging to that teammate are visually distinguished (highlighted, full opacity, or otherwise emphasized) versus non-matching tasks which are dimmed/hidden.

- [X] IX-02: Moving a task between columns provides immediate visual feedback
  - Action: Drag a task card from one column into another.
  - Expected: The card is visibly repositioned into the destination column without page reload, and the source column count updates immediately.

- [X] IX-03: Opening a task detail closes or stays dismissible
  - Action: Open a task detail view, then click the close (X), outside the panel, or press Escape.
  - Expected: The detail view closes and the board returns to its normal state; no overlay remains blocking interaction.

- [X] IX-04: Newly created task appears without requiring page reload
  - Action: Create a new task via the "New Task" form.
  - Expected: The new task card instantly appears in its starting column on the board.

## Content
- [X] CT-01: Default Kanban board contains multiple status columns on first load
  - Action: Open the application with no prior user actions.
  - Expected: The board displays at least the columns "To Do", "In Progress", and "Done" (or equivalent status stages).

- [X] CT-02: Default tasks populate the board on first load
  - Action: Open the application with no prior user actions.
  - Expected: At least one pre-existing task card is visible in a column, with assignee and due date shown.

- [X] CT-03: Task card content aligns with instruction — shows title, assignee, and due date
  - Action: Inspect any task card on the board.
  - Expected: The card visibly displays the task title, the assignee's name, and the due date — no key field is missing.

- [X] CT-04: Status updates / notes appear in chronological order within the task detail view
  - Action: Open a task that has multiple notes/updates and review the order.
  - Expected: Notes are listed with the newest at the top (or bottom) in a consistent, readable order — not randomly ordered or missing timestamps/text.
