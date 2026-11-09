# Test Checklist

## Functionality
- [ ] FT-01: User can create a new task with title, assignee, and due date
  - Action: Click the "Add Task" / "New Task" button, fill in title, select a teammate, set a due date, and submit.
  - Expected: A new task card with that title, assignee, and due date appears on the board (in the initial/"To Do" column).

- [ ] FT-02: Task can be assigned to a specific teammate
  - Action: Open the task detail view and change the assignee to another teammate, then save.
  - Expected: The task card on the board displays the new teammate's name/avatar; the old assignee is no longer shown.

- [ ] FT-03: Task status changes by moving it between columns
  - Action: Drag a task card from the "To Do" column to the "In Progress" (or "Done") column.
  - Expected: The card is now displayed under the target column, and its status reflects the new column.

- [ ] FT-04: User can open a task to see its details
  - Action: Click on an existing default task card.
  - Expected: A detail view/modal opens showing title, description, assignee, due date, status, and notes for that task.

- [ ] FT-05: User can edit a task's information
  - Action: From the open task detail view, change the title and due date, then save.
  - Expected: Changes persist — the updated title and due date are shown on the task card and reopen correctly in the detail view.

- [ ] FT-06: User can add a status update or short note to a task
  - Action: In the task detail view, type a note (e.g., "Waiting on design review") into the notes field and submit.
  - Expected: The note is appended to the task's notes/activity list and is visible when the task is reopened.

- [ ] FT-07: Board can be filtered by assignee
  - Action: Select a specific teammate from the assignee filter control.
  - Expected: Only tasks assigned to that teammate remain visible on the board; all other task cards are hidden.

- [ ] FT-08: Board can be filtered or highlighted by status
  - Action: Select a status filter (e.g., "In Progress").
  - Expected: Only tasks with that status are shown, or tasks of that status are visually highlighted while others are dimmed.

- [ ] FT-09: Filters can be combined and cleared
  - Action: Apply an assignee filter and a status filter together, then clear/reset the filters.
  - Expected: Both filters apply simultaneously (intersection of results); after clearing, all default tasks are visible again.

## Constraint
- [ ] CS-01: Task creation requires a title
  - Action: Click "Add Task", leave the title field empty, select assignee and due date, and attempt to submit.
  - Expected: Submission is blocked and a validation message indicates the title is required; no new card is created.

- [ ] CS-02: Assignee must be an existing teammate
  - Action: Open the assignee selector on the task creation form or detail view.
  - Expected: Only the names of existing team members are offered as options; no free-text or nonexistent teammate can be assigned.

- [ ] CS-03: Due date must be a valid date
  - Action: Enter an invalid date (e.g., "13/32/2026" or non-date text) in the due date field and attempt to save.
  - Expected: The invalid date is rejected with a validation message, or the date picker prevents entry of impossible dates.

- [ ] CS-04: A moved task exists in exactly one column
  - Action: Drag a task card from "To Do" to "Done", then inspect both columns and refresh/reopen the task.
  - Expected: The card appears only under "Done" — no duplicate remains in "To Do", and the status change persisted.

- [ ] CS-05: Empty notes/status updates are not recorded
  - Action: Open the notes field on a task and submit it with no text (or whitespace only).
  - Expected: No empty note entry is added to the task's notes/activity list.

## Interaction
- [ ] IX-01: Confirmation feedback after task creation
  - Action: Create a new task successfully.
  - Expected: A visible confirmation (toast message or the new card appearing highlighted) indicates the task was created; the creation form/modal closes.

- [ ] IX-02: Drag-and-drop affordances on the board
  - Action: Begin dragging a task card and hover it over a different column.
  - Expected: The card shows a drag preview and the target column is visually highlighted as a valid drop zone; dropping elsewhere returns the card to its original column.

- [ ] IX-03: Task detail view opens and closes without side effects
  - Action: Click a task card to open the detail view, then close it via the "X" button or backdrop, without editing.
  - Expected: The modal closes, the board is still fully visible, and the task's data is unchanged.

- [ ] IX-04: Empty-state feedback when a filter matches no tasks
  - Action: Apply a filter combination (e.g., teammate with no tasks in the selected status).
  - Expected: The board shows a clear "no tasks match" message or empty columns rather than a broken/blank page.

## Content
- [ ] CT-01: Board loads with default team tasks and data
  - Action: Open the page fresh and inspect the board and detail views of seeded tasks.
  - Expected: Multiple status columns (e.g., "To Do", "In Progress", "Done") are present, each seeded with relevant sample tasks having assignees, due dates, and at least one task containing notes.

- [ ] CT-02: Task cards display complete key information
  - Action: Inspect any task card on the board.
  - Expected: Each card shows the task title, assignee identifier (name/avatar), and due date — no missing, placeholder ("Lorem ipsum"), or broken fields.

- [ ] CT-03: Teammate content is consistent across the app
  - Action: Compare the names in the assignee filter and assignee dropdown with the names shown on task cards.
  - Expected: The same set of teammate names appears everywhere; no mismatched or duplicated teammate entries.