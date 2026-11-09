# Test Result

## Functionality

- [X] FT-01: View multiple projects
  - Action: Open the project management page.
  - Expected: Multiple projects are listed (e.g., project cards/links with names), and at least two distinct projects are visible.
  - Actual: Sidebar lists "Website Redesign" and "Mobile App Launch" (later also "QA Testing Project"). PASS.

- [X] FT-02: Create a new project
  - Action: Click the "New Project" (or similarly named) button, enter a project name, and submit.
  - Expected: The new project appears in the project list and can be opened.
  - Actual: "Create New Project" dialog opened; after entering name "QA Testing Project" and clicking Create Project, it appeared in the sidebar and opened with an empty board. PASS.

- [X] FT-03: Open a project's kanban board
  - Action: Click on an existing project.
  - Expected: A kanban board with multiple columns (e.g., "To Do", "In Progress", "Done") is displayed with tasks in them.
  - Actual: Clicking "Mobile App Launch" showed 4 columns — To Do (2), In Progress (1), Review (0), Done (2) — with task cards. PASS.

- [X] FT-04: Create a task with all attributes
  - Action: Click "Add Task", enter a title, set a due date, a priority (e.g., High), and an assignee, then save.
  - Expected: The task appears in a column showing its title, due date, priority, and assignee.
  - Actual: "QA smoke test task" created in To Do showing title, High badge, Nov 20 date, and Sarah Miller avatar. PASS.

- [X] FT-05: Drag task between columns
  - Action: Drag a task from the "To Do" column to the "In Progress" column.
  - Expected: The task is now in "In Progress" and no longer in "To Do"; the change persists after navigating away and back.
  - Actual: Note — Playwright's built-in `dragTo` did NOT move the card ("moved from position 3 to position 3"); a manual stepped mouse-drag (pointer events) worked. Task moved To Do → In Progress and persisted after navigating to Website Redesign and back. PASS.

- [X] FT-06: Search tasks by keyword
  - Action: Type a word from an existing task's title into the search box.
  - Expected: Only matching tasks are shown; tasks not containing the keyword are hidden.
  - Actual: Searching "authentication" left only "Implement authentication flow" visible; all other cards hidden. PASS.

- [X] FT-07: Filter tasks by status
  - Action: Apply a status filter (e.g., select "Done").
  - Expected: Only tasks whose column/status is "Done" are shown.
  - Actual: Status filter "Done" showed only "Setup React Native project" and "Design app icon and splash" in the Done column. PASS.

- [X] FT-08: Filter tasks by assignee
  - Action: Select an assignee from the assignee filter dropdown.
  - Expected: Only tasks assigned to that person are shown.
  - Actual: Member filter "Sarah Miller" showed exactly her 3 tasks (Implement authentication flow, QA smoke test task, Setup React Native project); James Wilson's and unassigned tasks hidden. PASS.

- [X] FT-09: Mark task progress
  - Action: Open a task and update its progress (e.g., set progress percentage, mark as complete, or move to "Done").
  - Expected: The task reflects the new progress state (e.g., progress bar/percent or Done status) on the board.
  - Actual: Edit Task dialog: progress slider set to 100% persisted (reopened dialog confirms 100%), then changing Status to Done + Save moved the card to the Done column and summary updated to 50%. PASS.
  - Observation (not a listed criterion): a card at 100% progress still sitting in "In Progress" displays no progress bar/percent on the card; the progress value is only visible in the edit dialog.

- [X] FT-10: View project status summary
  - Action: Open a project's summary/overview section.
  - Expected: A concise summary is shown (e.g., total tasks, tasks done/in progress counts or percentage complete) consistent with the board's tasks.
  - Actual: Header shows per-column counts (2 To Do / 1 In Progress / 0 Review / 3 Done) and "50% Complete" with progress bar, consistent with 3/6 done tasks. PASS.

- [X] FT-11: Send chat message in project chat panel
  - Action: In a project's chat panel, type a message and press Enter or click Send.
  - Expected: The message appears in the chat history with sender name and time.
  - Actual: "QA automated test message" appended to chat history attributed to "You" at "08:36". PASS.
  - Note: The chat panel renders at x=1280–1600, i.e., off-viewport on a 1280px window; it only becomes reachable after clicking the floating toggle button.

## Constraint

- [ ] CS-01: Cannot save task with empty title
  - Action: Open "Add Task", leave the title empty, and submit.
  - Expected: The task is not created; a validation error is shown (e.g., "Title is required").
  - Bug Report:
    - Issue: Missing validation error feedback (silent rejection)
    - Actual: Submitting with an empty title does NOT create a task and the dialog stays open (correct blocking), but no validation error is shown anywhere — no error text, no `aria-invalid`, no red border/highlight on the title input, no toast (sonner `[data-sonner-toast]` empty), and `validationMessage` is empty. The form fails silently with no user feedback.

- [X] CS-02: Task requires a valid due date
  - Action: Create a task with an invalid or missing due date (if required), or a date field that rejects invalid input.
  - Expected: Invalid date input is rejected with a visible error, or a valid date format is enforced.
  - Actual: Due Date is a native `type="date"` input; typing "not-a-date" is rejected (value stays empty, console warns "does not conform to the required format, yyyy-MM-dd") — a valid date format is enforced. Note: the due date itself is optional — a task was created successfully with no date. PASS.

- [ ] CS-03: Search/filter results show empty state correctly
  - Action: Search for a keyword that matches no tasks (e.g., "zzzznotexist").
  - Expected: No tasks are shown and an empty-state message (e.g., "No tasks found") appears; the board does not error or show unrelated tasks.
  - Bug Report:
    - Issue: Missing empty-state message
    - Actual: Searching "zzzznotexist" correctly hides all tasks (no unrelated tasks, no error), but no empty-state message appears — all four columns simply show their headers with count "0" and nothing else; no "No tasks found"-style message exists anywhere in the DOM.

- [X] CS-04: Cannot send empty chat message
  - Action: Click Send in the chat panel with an empty input.
  - Expected: No message is sent/appended to the chat history.
  - Actual: Send button is disabled while input is empty; pressing Enter with an empty input did not append any message (message count unchanged at 2). PASS.

## Interaction

- [X] IX-01: Drag-and-drop visual feedback
  - Action: Start dragging a task card over another column.
  - Expected: A visual drop indicator/highlight (e.g., target column highlights or a placeholder appears) is shown while dragging.
  - Actual: Mid-drag, the target column's drop zone showed highlight classes `bg-primary/5 ring-2 ring-dashed` (highlighted background + dashed ring). PASS.

- [X] IX-02: Task creation form opens on demand
  - Action: Click "Add Task" (or "+") button on a column.
  - Expected: A task creation form/modal opens immediately without page reload, and can be closed via Cancel/X.
  - Actual: "Create Task" dialog opened immediately on + click (no navigation/reload) and closed cleanly via Cancel. PASS.
  - Observation: After closing/saving *Edit Task* dialogs on some paths, a leftover full-screen backdrop (`div.fixed.inset-0.bg-background/20.backdrop-blur-sm.z-40`) and/or `body { pointer-events: none }` briefly remained, blocking page interaction until the overlay was clicked/removed — a dialog-cleanup glitch.

- [X] IX-03: Chat panel visible with project context
  - Action: Open a project and locate the chat panel.
  - Expected: The chat panel is displayed alongside the project board, showing existing messages for that project; switching projects shows that project's own chat.
  - Actual: Website Redesign chat shows mockups/mobile-nav/analytics messages; Mobile App Launch shows auth-flow/app-icons messages plus the newly sent message; the new "QA Testing Project" shows an empty chat. Each project has its own chat history. PASS.

## Content

- [ ] CT-01: Task cards display complete information
  - Action: Inspect several task cards on a board.
  - Expected: Each card shows title, due date, priority indicator, and assignee name/avatar; no blank or placeholder values on existing default tasks.
  - Bug Report:
    - Issue: Missing assignee on existing default task card
    - Actual: All cards show title, due date and priority badge, but the default task "App store submission prep" (Mobile App Launch, To Do) renders no assignee name or avatar at all (no `img[alt]` in the card). Likewise on Website Redesign, "Write API documentation" shows no assignee. Unassigned tasks display nothing in the assignee slot rather than a placeholder/name.

- [X] CT-02: Priority indicators are visually distinct
  - Action: Compare tasks with different priorities on the board.
  - Expected: High/Medium/Low priorities are distinguishable (e.g., different color badges or labels), and the values match each task's actual priority.
  - Actual: Badge colors differ by priority and match each task's data — High = red `rgb(239,67,67)`, Medium = amber `rgb(245,159,10)`, Low = green `rgb(33,196,93)` (text, background tint, border, and flag icon all color-coded). PASS.
