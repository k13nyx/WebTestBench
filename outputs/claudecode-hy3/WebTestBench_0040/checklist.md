# Test Checklist

## Functionality
- [ ] FT-01: Create a new task on the board
  - Action: Click the "Add Task" (or "+") button in a column, enter a task title, and submit.
  - Expected: A new task card appears in that column with the entered title.

- [ ] FT-02: Assign a task to a specific teammate
  - Action: Open a task, select a teammate from the "Assignee" dropdown, and save.
  - Expected: The task card shows the selected teammate as the assignee.

- [ ] FT-03: Set a due date on a task
  - Action: Open a task, set the "Due Date" field using the date control, and save.
  - Expected: The due date is displayed on the task card and in the task details.

- [ ] FT-04: Update task status by moving it between columns
  - Action: Drag a task card from one column (e.g., "To Do") to another (e.g., "In Progress").
  - Expected: The task now appears in the destination column and its status reflects that column.

- [ ] FT-05: Open a task to view full details
  - Action: Click a task card on the board.
  - Expected: A detail view (panel/modal) opens showing the full task information.

- [ ] FT-06: Edit existing task information
  - Action: Open a task, change its title/assignee/due date, and save.
  - Expected: The edited values persist and are reflected on the card and in details.

- [ ] FT-07: Add a status update or short note to a task
  - Action: Open a task, enter text in the notes/status-update field, and submit.
  - Expected: The note appears in the task's notes/activity section.

- [ ] FT-08: Filter or highlight tasks by assignee
  - Action: Select a teammate from the assignee filter control.
  - Expected: The board shows only that teammate's tasks, or highlights them distinctly from others.

- [ ] FT-09: Filter or highlight tasks by status
  - Action: Select a status from the status filter control.
  - Expected: The board shows only tasks in that status, or highlights them distinctly from others.

## Constraint
- [ ] CS-01: Task cannot be created without a required title
  - Action: Click "Add Task", leave the title empty, and submit.
  - Expected: A validation error is shown and no task is created.

- [ ] CS-02: A task can only be assigned to a valid teammate
  - Action: Open the assignee dropdown on a task.
  - Expected: Only existing team members are selectable; no arbitrary/empty value can be saved.

- [ ] CS-03: A task retains its assignee/due-date integrity when moved between columns
  - Action: Drag a task with an assignee and due date to another column.
  - Expected: After moving, the assignee and due date remain unchanged (only status changes).

## Interaction
- [ ] IX-01: Moving a task updates the board immediately without a full reload
  - Action: Drag a task card to a different column.
  - Expected: The card visually relocates to the new column instantly, reflecting the new status.

- [ ] IX-02: Success confirmation appears after creating or editing a task
  - Action: Create a new task or save an edit.
  - Expected: A success toast/notification is displayed confirming the action.

## Content
- [ ] CT-01: Each task card displays relevant core information
  - Action: View the board with default tasks.
  - Expected: Every card shows the task title, assignee, and due date (when set).

- [ ] CT-02: Board columns are labeled with distinct, meaningful statuses
  - Action: Open the Kanban board.
  - Expected: Columns are clearly labeled (e.g., To Do, In Progress, Done) representing workflow statuses.

- [ ] CT-03: Assignee filter lists only actual team members
  - Action: Open the assignee filter/selector.
  - Expected: The list contains only the real teammates available in the application, with correct names.