# Test Checklist

## Functionality
- [ ] FT-01: Display multiple projects on the management page
  - Action: Open the project management page.
  - Expected: A list of at least two distinct existing projects is visible.

- [ ] FT-02: Open a project to view its dedicated kanban board
  - Action: Click on an existing project from the list.
  - Expected: The project's own kanban board with task columns is displayed.

- [ ] FT-03: Create a task with due date, priority, and assignee
  - Action: Use the "Create Task" control and fill in title, due date, priority, and assignee from default data, then save.
  - Expected: A new task card appears on the board with the specified due date, priority, and assignee.

- [ ] FT-04: Filter or search tasks by status, assignee, or keyword
  - Action: Apply the filter/search controls using an existing status, an existing assignee, or a known keyword.
  - Expected: Only tasks matching the selected status, assignee, or keyword remain visible.

- [ ] FT-05: Mark progress on a task
  - Action: Change an existing task's status/progress (e.g., move it to "In Progress" or "Done" via its controls).
  - Expected: The task's progress/status is updated and reflected on the board.

- [ ] FT-06: View a concise summary of the project's overall status
  - Action: Locate the project status summary area.
  - Expected: A summary (e.g., counts per status or completion percentage) is displayed and reflects current tasks.

- [ ] FT-07: Send and view messages in the project's chat panel
  - Action: Open the chat panel on the project and send a message.
  - Expected: The sent message is displayed in the chat panel thread.

## Constraint
- [ ] CS-01: Cannot create a task with empty required fields
  - Action: Attempt to save a task leaving title, due date, priority, or assignee empty.
  - Expected: The task is not created; a validation error identifies the missing required field(s).

- [ ] CS-02: Cannot assign a task to a non-team member
  - Action: Attempt to assign a task to a user not in the project's team list.
  - Expected: The assignment is rejected; only valid team members can be selected/assigned.

- [ ] CS-03: Cannot move a task into an invalid column state
  - Action: Attempt to drop a task into a column that conflicts with a rule (e.g., "Done" without completion).
  - Expected: The drag is rejected or reverted; the task remains in a valid column.

## Interaction
- [ ] IX-01: Dragging a task between columns updates its status
  - Action: Drag an existing task card from one column to another.
  - Expected: The card moves to the new column and its status updates without page reload.

- [ ] IX-02: Show success confirmation after task creation
  - Action: Create a valid task and save.
  - Expected: A success toast/confirmation appears indicating the task was created.

- [ ] IX-03: Chat message appears instantly without page refresh
  - Action: Send a chat message in the project panel.
  - Expected: The message renders immediately in the thread without manually refreshing.

## Content
- [ ] CT-01: Kanban columns are clearly labeled by status
  - Action: Inspect the board column headers.
  - Expected: Columns are labeled with distinct statuses (e.g., To Do, In Progress, Done) relevant to task workflow.

- [ ] CT-02: Task cards show due date, priority, and assignee
  - Action: Inspect an existing task card.
  - Expected: The card displays its due date, priority level, and assignee name.

- [ ] CT-03: Chat panel content is relevant to the project
  - Action: Review the chat panel and its messages.
  - Expected: The panel is attached to the current project and its messages relate to that project's discussion.