# Test Checklist

## Functionality
- [ ] FT-01: Open a default project's kanban board
  - Action: Click on a pre-existing project from the project list.
  - Expected: The project's kanban board loads with its default task columns (e.g., To Do, In Progress, Done).

- [ ] FT-02: View the list of all default projects
  - Action: Navigate to the main project management page.
  - Expected: All pre-existing projects are listed and selectable.

- [ ] FT-03: Create a new task with due date, priority, and assignee
  - Action: Click "Add Task", fill in title, description, due date, priority (e.g., High/Medium/Low), and assignee, then save.
  - Expected: A new task card appears in the default column with all entered details visible.

- [ ] FT-04: Drag a task from one kanban column to another
  - Action: Click and drag a default task card from "To Do" to "In Progress" (or another existing column).
  - Expected: The task card moves to the target column and persists in that column after release.

- [ ] FT-05: Filter tasks by status (column)
  - Action: Apply the status filter to show only tasks in a specific column (e.g., "Done").
  - Expected: Only tasks matching the selected status are displayed.

- [ ] FT-06: Filter tasks by assignee
  - Action: Select a team member from the assignee filter dropdown.
  - Expected: Only tasks assigned to that team member are displayed.

- [ ] FT-07: Search tasks by keyword
  - Action: Enter a keyword (e.g., part of a default task title or description) into the search field.
  - Expected: Only tasks containing the keyword in title/description are shown.

- [ ] FT-08: Mark progress on a task
  - Action: Open a default task and click the progress/complete action (e.g., checkbox or progress bar).
  - Expected: The task's progress state updates and is reflected on the board.

- [ ] FT-09: View concise project status summary
  - Action: Open a default project's dashboard or summary view.
  - Expected: A summary is shown with overall metrics (e.g., total tasks, completed tasks, in-progress tasks, overdue tasks).

- [ ] FT-10: Send a message in the project's real-time chat panel
  - Action: Open the chat panel for a default project, type a message, and click send.
  - Expected: The message appears in the chat panel with sender identity and timestamp.

- [ ] FT-11: Receive messages in real-time in chat
  - Action: With the chat panel open in one view, send a message from another session/user for the same project.
  - Expected: The new message appears in the chat panel without requiring a page refresh.

## Constraint
- [ ] CS-01: Cannot create a task without mandatory fields
  - Action: Click "Add Task" and attempt to save with the title (and/or other required field) empty.
  - Expected: Submission is blocked and a validation error is shown for the missing field(s).

- [ ] CS-02: Cannot create a project without a name
  - Action: Click "New Project" and attempt to save with the project name field empty.
  - Expected: Submission is blocked and a validation error requires a project name.

- [ ] CS-03: Combining filters (status + assignee + keyword) refines results
  - Action: Apply status filter AND assignee filter AND keyword search simultaneously on default data.
  - Expected: Only tasks matching ALL active filters are shown; results match the logical AND of criteria.

- [ ] CS-04: Each project has an isolated chat panel
  - Action: Send a message in Project A's chat, then open Project B's chat.
  - Expected: Project B's chat does not contain Project A's messages; chats are separated by project.

## Interaction
- [ ] IX-01: Visual feedback while dragging a task
  - Action: Begin dragging a task card between columns.
  - Expected: The card shows a drag state (e.g., lifted/elevated) and the target column highlights as a drop zone.

- [ ] IX-02: Task progress updates reflect in the project summary
  - Action: Mark a default task as complete and revisit the project's summary view.
  - Expected: The summary metrics (e.g., completed task count) update to reflect the new status.

- [ ] IX-03: New chat messages appear without manual refresh
  - Action: Send a chat message from another user; observe the chat panel currently open.
  - Expected: The new message appears automatically in the chat panel within seconds, no refresh required.

## Content
- [ ] CT-01: Priority labels are correctly displayed on task cards
  - Action: Inspect default task cards with different priority values (High/Medium/Low).
  - Expected: Each card displays a priority label (and/or color/icon) matching its assigned priority.

- [ ] CT-02: Due dates are displayed in a readable, correct format on task cards
  - Action: View default tasks with due dates set.
  - Expected: Due dates are shown in a consistent, readable format (e.g., "Nov 15, 2026") matching the underlying date.

- [ ] CT-03: Kanban columns use correct, theme-relevant status labels
  - Action: Inspect the kanban board's column headers.
  - Expected: Columns are labeled with clear status names (e.g., "To Do", "In Progress", "Done") appropriate to project task management.