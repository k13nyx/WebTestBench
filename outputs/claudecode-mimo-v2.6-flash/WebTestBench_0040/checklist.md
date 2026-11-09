# Test Checklist

## Functionality
- [ ] FT-01: Create a new task on the Kanban board
  - Action: Click the add/create task control, enter a title (e.g., "Prepare sprint report"), and submit.
  - Expected: The new task card appears in the board's default/start column with its title visible.

- [ ] FT-02: Assign a task to a specific teammate
  - Action: Create a task selecting a teammate (e.g., "Alice") in the assignee field, or edit an existing task to assign "Alice".
  - Expected: The task card and its detail view both display "Alice" as the assignee.

- [ ] FT-03: Set a due date on a task
  - Action: Create or edit a task and set a due date (e.g., 2026-11-20), then save.
  - Expected: The due date is displayed on the task card and/or in its detail view as selected.

- [ ] FT-04: Update task status by moving it between columns
  - Action: Drag (or move via control) a task from its current column to another status column (e.g., "To Do" → "In Progress").
  - Expected: The task card now appears only in the target column, and the column's task count updates accordingly.

- [ ] FT-05: Open a task to view its details
  - Action: Click on an existing task card.
  - Expected: A detail view opens showing the task's title, assignee, due date, status/column, and any notes.

- [ ] FT-06: Edit a task's information
  - Action: Open a task, change its title and due date, and save.
  - Expected: The updated title and due date are reflected both in the detail view and on the board card.

- [ ] FT-07: Add a status update/note to a task
  - Action: Open a task, type a short note (e.g., "Waiting on design review") in the notes/update field, and submit.
  - Expected: The note is saved and appears in the task's detail view notes/updates list.

- [ ] FT-08: Filter tasks by assignee
  - Action: Select a teammate (e.g., "Alice") in the assignee filter.
  - Expected: Only tasks assigned to "Alice" remain visible (or are clearly highlighted) while other tasks are hidden/de-emphasized.

- [ ] FT-09: Filter tasks by status
  - Action: Select a status (e.g., "In Progress") in the status filter.
  - Expected: Only tasks in the "In Progress" status are shown (or clearly highlighted) across the board.

- [ ] FT-10: Clear active filters
  - Action: With a filter applied, clear/reset the assignee or status filter.
  - Expected: All tasks on the board become visible again with no filtering applied.

## Constraint
- [ ] CS-01: Cannot create a task with an empty title
  - Action: Open the create-task form, leave the title field empty, and submit.
  - Expected: An error/validation message appears, no task is created, and the form remains open.

- [ ] CS-02: Cannot add an empty note to a task
  - Action: Open a task detail, leave the note field empty, and click the add/submit note button.
  - Expected: The empty note is rejected (button disabled or validation message shown) and no blank note is added to the list.

## Interaction
- [ ] IX-01: Success feedback after creating a task
  - Action: Create a valid new task and submit.
  - Expected: A visible confirmation (e.g., toast/message) appears indicating the task was created, alongside the new card on the board.

- [ ] IX-02: Success feedback after adding a note
  - Action: Add a valid note to a task.
  - Expected: A visible confirmation appears and the note field clears after submission.

- [ ] IX-03: Task detail view opens and closes correctly
  - Action: Click a task card to open details, then click the close (×) button.
  - Expected: The detail view opens over the board; closing it returns to the full board with no lingering overlay.

- [ ] IX-04: Filtered/highlighted tasks are visually distinguished
  - Action: Apply an assignee or status filter.
  - Expected: Matching tasks are visually highlighted (or non-matching tasks visibly dimmed/hidden) so the focused set is immediately apparent.

## Content
- [ ] CT-01: Assignee names shown on tasks match the teammate roster
  - Action: Inspect several task cards and their detail views.
  - Expected: Every displayed assignee name corresponds exactly to a teammate available in the assignee selection list—no blank, unknown, or mismatched names.

- [ ] CT-02: Due dates are displayed accurately and readably
  - Action: Compare the due dates shown on task cards/detail views with the dates entered during creation/editing.
  - Expected: Displayed dates match the entered dates exactly and are shown in a consistent, readable format.

- [ ] CT-03: Notes/status updates display their full content
  - Action: Add two distinct notes to a task and review the detail view.
  - Expected: Both notes appear with their full original text intact, in a logical (e.g., newest-last or newest-first) order.