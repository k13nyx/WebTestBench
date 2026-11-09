# Test Checklist

## Functionality
- [ ] FT-01: View and open multiple projects from the project management page
  - Action: On the projects page, locate the default projects list and click on a project.
  - Expected: The project opens, showing its own dedicated kanban board (not another project's board).

- [ ] FT-02: Kanban board displays default tasks organized into workflow columns
  - Action: Open a default project and inspect its kanban board.
  - Expected: Tasks from the default data appear in columns (e.g., To Do, In Progress, Done) matching their status.

- [ ] FT-03: Create a new task with title, due date, priority, and assignee
  - Action: Click the "New Task" / "Add Task" button, fill in title, due date, priority, and assignee, then save.
  - Expected: The new task card appears on the board showing all entered values.

- [ ] FT-04: Drag a task card to a different column to change its status
  - Action: Drag a default task card from "To Do" and drop it into "In Progress".
  - Expected: The task is removed from the source column and shown in the destination column; its status now reads "In Progress".

- [ ] FT-05: Filter tasks by status
  - Action: Apply the status filter selecting "Done".
  - Expected: Only tasks with status "Done" are displayed; all other tasks are hidden.

- [ ] FT-06: Filter tasks by assignee
  - Action: Apply the assignee filter and select a default team member.
  - Expected: Only tasks assigned to that team member are displayed.

- [ ] FT-07: Search tasks by keyword
  - Action: Type a keyword from an existing default task title into the search box.
  - Expected: Only tasks whose title (or content) contains the keyword are displayed; the board updates accordingly.

- [ ] FT-08: Mark progress on a task
  - Action: Open a default task in progress and mark it complete (e.g., check "Complete" or move it to "Done").
  - Expected: The task shows a completed state and is reflected in the Done column.

- [ ] FT-09: Send a message in the project's chat panel
  - Action: Open the project's chat panel, type a message, and send it.
  - Expected: The sent message appears in the chat panel, attributed to the sender.

- [ ] FT-10: Chat is real-time across team members
  - Action: With the project open in two sessions (two team members), have one member send a chat message.
  - Expected: The other member sees the new message appear in the chat panel without refreshing the page.

- [ ] FT-11: Concise project status summary is available
  - Action: Open a default project and locate its status summary section.
  - Expected: A concise overview (e.g., counts of tasks per status, completion percentage) of the project's overall status is displayed.

## Constraint
- [ ] CS-01: Cannot create a task with an empty required title
  - Action: Open the task creation form, leave the title empty, fill other fields, and attempt to save.
  - Expected: The task is not created; the form indicates the title is required.

- [ ] CS-02: Task must be assigned only to an existing team member
  - Action: Open the task creation form and inspect the assignee field.
  - Expected: The assignee can only be selected from a list of existing team members (no free-text unknown users).

- [ ] CS-03: Projects are isolated — tasks and chat do not leak between projects
  - Action: Compare the kanban board and chat panel of two different default projects.
  - Expected: Each project shows only its own tasks and its own chat history; no task or message from one project appears in the other.

## Interaction
- [ ] IX-01: Drag-and-drop provides visual feedback
  - Action: Begin dragging a task card over the board and hover over another column.
  - Expected: The task card follows the cursor and the target column visibly highlights (e.g., border/background change) as a valid drop zone.

- [ ] IX-02: Filters and search update the board instantly
  - Action: Type or select filter/search values.
  - Expected: The task list updates immediately as input changes, without a full page reload.

- [ ] IX-03: Incoming chat messages are surfaced without manual refresh
  - Action: While viewing a project's chat panel, have another team member send a message.
  - Expected: A new-message indicator (unread badge, highlight, or appended message) appears without the viewer refreshing.

## Content
- [ ] CT-01: Task cards display due date, priority, and assignee
  - Action: Inspect default task cards on any kanban board.
  - Expected: Each card visibly shows its due date, priority (e.g., High/Medium/Low), and assigned team member.

- [ ] CT-02: Priority levels are distinctly labeled
  - Action: Compare task cards with different priorities on the board.
  - Expected: Priorities use clear, distinct labels or colors (e.g., High in red, Medium in yellow, Low in green) consistent across all cards.

- [ ] CT-03: Status summary matches the actual board state
  - Action: Count tasks in each kanban column and compare with the project's status summary.
  - Expected: Summary counts/percentages exactly match the tasks currently on the board.