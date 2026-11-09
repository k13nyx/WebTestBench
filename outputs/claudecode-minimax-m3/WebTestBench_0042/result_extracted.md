# Test Result

## Functionality

- [X] FT-01: Open a default project's kanban board
  - Action: Click on a pre-existing project from the project list.
  - Expected: The project's kanban board loads with its default task columns (e.g., To Do, In Progress, Done).

- [X] FT-02: View the list of all default projects
  - Action: Navigate to the main project management page.
  - Expected: All pre-existing projects are listed and selectable.

- [X] FT-03: Create a new task with due date, priority, and assignee
  - Action: Click "Add Task", fill in title, description, due date, priority (e.g., High/Medium/Low), and assignee, then save.
  - Expected: A new task card appears in the default column with all entered details visible.

- [X] FT-04: Drag a task from one kanban column to another
  - Action: Click and drag a default task card from "To Do" to "In Progress" (or another existing column).
  - Expected: The task card moves to the target column and persists in that column after release.

- [X] FT-05: Filter tasks by status (column)
  - Action: Apply the status filter to show only tasks in a specific column (e.g., "Done").
  - Expected: Only tasks matching the selected status are displayed.

- [X] FT-06: Filter tasks by assignee
  - Action: Select a team member from the assignee filter dropdown.
  - Expected: Only tasks assigned to that team member are displayed.

- [X] FT-07: Search tasks by keyword
  - Action: Enter a keyword (e.g., part of a default task title or description) into the search field.
  - Expected: Only tasks containing the keyword in title/description are shown.

- [X] FT-08: Mark progress on a task
  - Action: Open a default task and click the progress/complete action (e.g., checkbox or progress bar).
  - Expected: The task's progress state updates and is reflected on the board.

- [X] FT-09: View concise project status summary
  - Action: Open a default project's dashboard or summary view.
  - Expected: A summary is shown with overall metrics (e.g., total tasks, completed tasks, in-progress tasks, overdue tasks).

- [X] FT-10: Send a message in the project's real-time chat panel
  - Action: Open the chat panel for a default project, type a message, and click send.
  - Expected: The message appears in the chat panel with sender identity and timestamp.

- [ ] FT-11: Receive messages in real-time in chat
  - Action: With the chat panel open in one view, send a message from another session/user for the same project.
  - Expected: The new message appears in the chat panel without requiring a page refresh.
  - Bug Report:
    - Issue: Missing Real-Time Transport (No Backend / No WebSocket)
    - Actual: A second browser tab was opened on the same URL for the same project ("Website Redesign") and its chat panel was used to send two messages ("SECOND SESSION MESSAGE - realtime probe" and "REALTIME-PROBE-2 from tab1"). The first tab kept its chat panel open and polled for >15 seconds: neither message ever appeared (tab0 chat showed only "Real-time test message from QA"). The app has no server-side store at all — `performance.getEntriesByType('resource')` showed no API/socket requests, `localStorage` and `sessionStorage` were both empty, and the second tab started from pristine seed data (it never saw the task created in tab 1). Reloading tab 1 discarded all changes, proving chat/tasks live only in per-tab React memory. Messages are therefore never delivered to other sessions without a page refresh.

## Constraint

- [ ] CS-01: Cannot create a task without mandatory fields
  - Action: Click "Add Task" and attempt to save with the title (and/or other required field) empty.
  - Expected: Submission is blocked and a validation error is shown for the missing field(s).
  - Bug Report:
    - Issue: Missing Validation Error Message (Silent Form Rejection)
    - Actual: Clicking "Create" with an empty title correctly blocks submission (dialog stayed open, no task card created, To Do count stayed at 3), but **no validation error is shown anywhere**. Polled the DOM every 100ms for 2.5s: no toast/`role=alert`/`role=status` text, no `border-destructive` on the Title input, no `aria-invalid`, and no text containing "required" or "error". The same was true after typing then clearing the title and blurring, and after pressing Enter. The user gets no indication of *why* the save did nothing.

- [ ] CS-02: Cannot create a project without a name
  - Action: Click "New Project" and attempt to save with the project name field empty.
  - Expected: Submission is blocked and a validation error requires a project name.
  - Bug Report:
    - Issue: Missing Validation Error Message (Silent Form Rejection)
    - Actual: Clicking "Create Project" with an empty Name field correctly blocks submission (the "Create New Project" dialog stayed open and the sidebar project list remained `["Website Redesign", "Mobile App Launch", "New Project"]` — no project added), but **no validation error is displayed**. Polled the DOM every 100ms for 2.5s: no toast/`role=alert`/`role=status` message, the Name input did not get a `border-destructive` class, and the document contained no "required"/"error" text. The form fails silently.

- [X] CS-03: Combining filters (status + assignee + keyword) refines results
  - Action: Apply status filter AND assignee filter AND keyword search simultaneously on default data.
  - Expected: Only tasks matching ALL active filters are shown; results match the logical AND of criteria.

- [X] CS-04: Each project has an isolated chat panel
  - Action: Send a message in Project A's chat, then open Project B's chat.
  - Expected: Project B's chat does not contain Project A's messages; chats are separated by project.

## Interaction

- [X] IX-01: Visual feedback while dragging a task
  - Action: Begin dragging a task card between columns.
  - Expected: The card shows a drag state (e.g., lifted/elevated) and the target column highlights as a drop zone.

- [X] IX-02: Task progress updates reflect in the project summary
  - Action: Mark a default task as complete and revisit the project's summary view.
  - Expected: The summary metrics (e.g., completed task count) update to reflect the new status.

- [ ] IX-03: New chat messages appear without manual refresh
  - Action: Send a chat message from another user; observe the chat panel currently open.
  - Expected: The new message appears automatically in the chat panel within seconds, no refresh required.
  - Bug Report:
    - Issue: Missing Real-Time Message Delivery (No Cross-Session Sync)
    - Actual: With the chat panel open on the "Website Redesign" project in the first tab, a message was sent from a second tab/session for the same project. After waiting 15+ seconds with continuous polling, the open chat panel in the first tab still contained only its own message ("You / 19:12 / Real-time test message from QA"); the incoming message never appeared, and no refresh was performed. The second tab's chat showed the new message locally only. No refresh-independent update occurred.

## Content

- [X] CT-01: Priority labels are correctly displayed on task cards
  - Action: Inspect default task cards with different priority values (High/Medium/Low).
  - Expected: Each card displays a priority label (and/or color/icon) matching its assigned priority.

- [X] CT-02: Due dates are displayed in a readable, correct format on task cards
  - Action: View default tasks with due dates set.
  - Expected: Due dates are shown in a consistent, readable format (e.g., "Nov 15, 2026") matching the underlying date.

- [X] CT-03: Kanban columns use correct, theme-relevant status labels
  - Action: Inspect the kanban board's column headers.
  - Expected: Columns are labeled with clear status names (e.g., "To Do", "In Progress", "Done") appropriate to project task management.
