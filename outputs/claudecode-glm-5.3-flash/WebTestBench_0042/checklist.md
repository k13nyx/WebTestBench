# Test Checklist

## Functionality
- [ ] FT-01: View multiple projects
  - Action: Open the project management page.
  - Expected: Multiple projects are listed (e.g., project cards/links with names), and at least two distinct projects are visible.
- [ ] FT-02: Create a new project
  - Action: Click the "New Project" (or similarly named) button, enter a project name, and submit.
  - Expected: The new project appears in the project list and can be opened.
- [ ] FT-03: Open a project's kanban board
  - Action: Click on an existing project.
  - Expected: A kanban board with multiple columns (e.g., "To Do", "In Progress", "Done") is displayed with tasks in them.
- [ ] FT-04: Create a task with all attributes
  - Action: Click "Add Task", enter a title, set a due date, a priority (e.g., High), and an assignee, then save.
  - Expected: The task appears in a column showing its title, due date, priority, and assignee.
- [ ] FT-05: Drag task between columns
  - Action: Drag a task from the "To Do" column to the "In Progress" column.
  - Expected: The task is now in "In Progress" and no longer in "To Do"; the change persists after navigating away and back.
- [ ] FT-06: Search tasks by keyword
  - Action: Type a word from an existing task's title into the search box.
  - Expected: Only matching tasks are shown; tasks not containing the keyword are hidden.
- [ ] FT-07: Filter tasks by status
  - Action: Apply a status filter (e.g., select "Done").
  - Expected: Only tasks whose column/status is "Done" are shown.
- [ ] FT-08: Filter tasks by assignee
  - Action: Select an assignee from the assignee filter dropdown.
  - Expected: Only tasks assigned to that person are shown.
- [ ] FT-09: Mark task progress
  - Action: Open a task and update its progress (e.g., set progress percentage, mark as complete, or move to "Done").
  - Expected: The task reflects the new progress state (e.g., progress bar/percent or Done status) on the board.
- [ ] FT-10: View project status summary
  - Action: Open a project's summary/overview section.
  - Expected: A concise summary is shown (e.g., total tasks, tasks done/in progress counts or percentage complete) consistent with the board's tasks.
- [ ] FT-11: Send chat message in project chat panel
  - Action: In a project's chat panel, type a message and press Enter or click Send.
  - Expected: The message appears in the chat history with sender name and time.

## Constraint
- [ ] CS-01: Cannot save task with empty title
  - Action: Open "Add Task", leave the title empty, and submit.
  - Expected: The task is not created; a validation error is shown (e.g., "Title is required").
- [ ] CS-02: Task requires a valid due date
  - Action: Create a task with an invalid or missing due date (if required), or a date field that rejects invalid input.
  - Expected: Invalid date input is rejected with a visible error, or a valid date format is enforced.
- [ ] CS-03: Search/filter results show empty state correctly
  - Action: Search for a keyword that matches no tasks (e.g., "zzzznotexist").
  - Expected: No tasks are shown and an empty-state message (e.g., "No tasks found") appears; the board does not error or show unrelated tasks.
- [ ] CS-04: Cannot send empty chat message
  - Action: Click Send in the chat panel with an empty input.
  - Expected: No message is sent/appended to the chat history.

## Interaction
- [ ] IX-01: Drag-and-drop visual feedback
  - Action: Start dragging a task card over another column.
  - Expected: A visual drop indicator/highlight (e.g., target column highlights or a placeholder appears) is shown while dragging.
- [ ] IX-02: Task creation form opens on demand
  - Action: Click "Add Task" (or "+") button on a column.
  - Expected: A task creation form/modal opens immediately without page reload, and can be closed via Cancel/X.
- [ ] IX-03: Chat panel visible with project context
  - Action: Open a project and locate the chat panel.
  - Expected: The chat panel is displayed alongside the project board, showing existing messages for that project; switching projects shows that project's own chat.

## Content
- [ ] CT-01: Task cards display complete information
  - Action: Inspect several task cards on a board.
  - Expected: Each card shows title, due date, priority indicator, and assignee name/avatar; no blank or placeholder values on existing default tasks.
- [ ] CT-02: Priority indicators are visually distinct
  - Action: Compare tasks with different priorities on the board.
  - Expected: High/Medium/Low priorities are distinguishable (e.g., different color badges or labels), and the values match each task's actual priority.