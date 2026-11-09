# Test Checklist

## Functionality
- [ ] FT-01: Create a new task with a title
  - Action: Click the "New Task" (or "Add Task") button, enter title "Design landing page", and submit the form.
  - Expected: A task card titled "Design landing page" appears on the Kanban board in the first/default column.
- [ ] FT-02: Assign a task to a teammate
  - Action: Create a task (or edit an existing one) and select a teammate, e.g. "Alice", from the assignee field.
  - Expected: The task card displays the assigned teammate's name or avatar after saving.
- [ ] FT-03: Set a due date on a task
  - Action: Create a task (or edit an existing one) and set a due date, e.g. "2026-11-15", then save.
  - Expected: The task card displays the due date "2026-11-15" (or a human-readable equivalent, e.g. "Nov 15").
- [ ] FT-04: Move a task between columns to update status
  - Action: Drag (or use the move control on) a task card from the "To Do" column into the "In Progress" column.
  - Expected: The card is now located in the "In Progress" column and no longer appears in "To Do".
- [ ] FT-05: Open a task to view its details
  - Action: Click on any task card on the board.
  - Expected: A detail view (panel or modal) opens showing the task's title, assignee, due date, status, and a section for notes/updates.
- [ ] FT-06: Edit a task's information
  - Action: Open a task, change its title to "Design landing page v2", change assignee and due date, then save.
  - Expected: After saving, the task card on the board reflects the new title, assignee, and due date.
- [ ] FT-07: Add a status update / note to a task
  - Action: Open a task, type "Blocked until Friday" into the note/update field, and submit.
  - Expected: The note "Blocked until Friday" appears on the task's detail view and is still visible after closing and reopening the task.
- [ ] FT-08: Filter tasks by assignee
  - Action: Select "Alice" in the assignee filter control on the board.
  - Expected: Only tasks assigned to Alice remain visible (or are highlighted); tasks assigned to others are hidden or dimmed.
- [ ] FT-09: Filter tasks by status
  - Action: Select "In Progress" in the status filter control on the board.
  - Expected: Only tasks in the "In Progress" status remain visible (or are highlighted); other tasks are hidden or dimmed.
- [ ] FT-10: Clear filters to show all tasks
  - Action: After applying an assignee or status filter, click "Clear"/"All" (or reset the filter control).
  - Expected: All tasks across all columns are visible on the board again.

## Constraint
- [ ] CS-01: Cannot create a task with an empty title
  - Action: Open the "New Task" form, leave the title field empty, and click submit/save.
  - Expected: The task is not created; a validation message is shown or the submit is blocked.
- [ ] CS-02: Assignee is limited to existing teammates
  - Action: Open the assignee dropdown on a task (new or existing).
  - Expected: The dropdown lists only predefined teammates (e.g. Alice, Bob); no arbitrary/unknown person can be assigned.
- [ ] CS-03: Task status stays consistent with its column
  - Action: Move a task into the "Done" column, then open its detail view.
  - Expected: The status shown in the detail view is "Done", matching the column the card is in.
- [ ] CS-04: Cannot add an empty note/status update
  - Action: Open a task, leave the note/update field empty, and click submit/add.
  - Expected: The empty note is not added; the button is disabled or a validation message appears.

## Interaction
- [ ] IX-01: Dragging a card gives visual feedback
  - Action: Press and drag a task card over another column.
  - Expected: The dragged card appears visually lifted/following the cursor, and the hovered column shows a drop indicator or highlight.
- [ ] IX-02: Active filter is visibly indicated
  - Action: Apply an assignee or status filter on the board.
  - Expected: The selected filter control (chip/dropdown/option) shows a highlighted or selected state so the user can see a filter is active.
- [ ] IX-03: Board updates immediately after task actions
  - Action: Create, move, or edit a task and observe the board.
  - Expected: The board reflects the change immediately without a full page reload (optionally with a success toast).

## Content
- [ ] CT-01: Default teammates are available for assignment
  - Action: Open the assignee dropdown on any task creation/edit form.
  - Expected: At least 2 predefined teammates with names (e.g. Alice, Bob) are listed and selectable.
- [ ] CT-02: Board displays labeled status columns
  - Action: View the Kanban board on page load.
  - Expected: At least 3 columns with clear status headers (e.g. "To Do", "In Progress", "Done") are displayed.
- [ ] CT-03: Default task data is meaningful and relevant
  - Action: View the pre-existing task cards on the board.
  - Expected: Cards show real, team-work-relevant titles with assignee/due-date info; no placeholder text like "Lorem ipsum" or "Task 1" only.