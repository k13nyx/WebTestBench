# Test Checklist

## Functionality
- [ ] FT-01: Project page lists all available projects
  - Action: Load the project management page.
  - Expected: A list of multiple projects is displayed; each project is selectable.

- [ ] FT-02: Selecting a project opens its own kanban board
  - Action: Click a project from the project list.
  - Expected: A kanban board with task columns for that specific project is displayed.

- [ ] FT-03: User can create a task with due date, priority, and assignee
  - Action: In a project board, click "Add Task"/"New Task", enter a title, set a due date, choose a priority, select an assignee, and save.
  - Expected: The new task appears on the board showing its title, due date, priority, and assignee.

- [ ] FT-04: User can drag a task between columns
  - Action: Drag a task card from one column and drop it into a different column.
  - Expected: The task is removed from the source column and appears in the destination column.

- [ ] FT-05: User can filter tasks by status
  - Action: Apply a status filter (e.g., "In Progress").
  - Expected: Only tasks with the selected status are shown; other tasks are hidden.

- [ ] FT-06: User can filter tasks by assignee
  - Action: Apply an assignee filter for a specific team member.
  - Expected: Only tasks assigned to that member are shown.

- [ ] FT-07: User can search tasks by keyword
  - Action: Type a keyword matching a task's title into the search field.
  - Expected: Only tasks containing the keyword are shown.

- [ ] FT-08: User can send a message in the project chat panel
  - Action: Open the project's chat panel, type a message, and send it.
  - Expected: The message is posted and visible in that project's chat panel.

## Constraint
- [ ] CS-01: Task cannot be created with empty required fields
  - Action: Attempt to save a new task with the title (or other required field) left empty.
  - Expected: Save is blocked and a validation message indicates the missing required field.

- [ ] CS-02: Empty chat message cannot be sent
  - Action: Attempt to send a blank or whitespace-only chat message.
  - Expected: The message is not posted; a send is prevented.

- [ ] CS-03: Non-matching filter/search shows a clear empty state
  - Action: Apply a filter or keyword that matches no tasks.
  - Expected: No tasks are shown and an explicit "no results" / empty message is displayed.

- [ ] CS-04: Task cannot be dropped outside a valid column
  - Action: Drag a task and drop it outside any kanban column.
  - Expected: The task returns to its original column; no invalid state is created.

## Interaction
- [ ] IX-01: Drag operation shows visual feedback and snaps to target
  - Action: Begin dragging a task card and hover over a drop column.
  - Expected: The card visually follows the cursor and the target column highlights; on drop the card snaps into place.

- [ ] IX-02: Confirmation appears after task creation
  - Action: Successfully create a new task.
  - Expected: A success notification/toast is displayed confirming the task was created.

- [ ] IX-03: Marking progress updates the task immediately
  - Action: Mark a task's progress (e.g., change its status to "Done"/"In Progress").
  - Expected: The task's progress indicator/state updates on screen without a manual page refresh.

- [ ] IX-04: Chat messages arrive in real time
  - Action: Have another team member (or another session) send a message to the project chat.
  - Expected: The new message appears in the chat panel automatically without reloading the page.

- [ ] IX-05: Project status summary updates after task changes
  - Action: Move or complete a task on the board.
  - Expected: The project's overall status summary reflects the change without manual refresh.

## Content
- [ ] CT-01: Project status summary reflects actual board data
  - Action: Compare the summary (e.g., counts/percentages by status) with the tasks currently on the board.
  - Expected: Summary values match the real task data; no stale or fabricated numbers.

- [ ] CT-02: Chat messages are scoped to the correct project
  - Action: Open two different projects' chat panels and inspect their messages.
  - Expected: Each panel shows only that project's conversation; no messages leak across projects.

- [ ] CT-03: Assignees correspond to valid team members
  - Action: Inspect task assignee names/avatars on the board and in the assignee filter.
  - Expected: All assignees are real team members; no blank, placeholder, or invalid names.