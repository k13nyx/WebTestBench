# Test Checklist

## Functionality
- [ ] FT-01: User can create a new project and it appears in the project list
  - Action: Click "New Project" (or "Create Project"), enter a name, submit
  - Expected: The new project appears in the sidebar/project list and can be opened

- [ ] FT-02: Each project has its own dedicated kanban board
  - Action: Open two different projects from the project list
  - Expected: Each shows a board with distinct task columns (e.g., "To Do", "In Progress", "Done") holding only that project's tasks

- [ ] FT-03: User can create a task with due date, priority, and assignee
  - Action: On a board, open "Add Task"/"New Task", set title, due date (e.g., 2026-11-15), priority (e.g., High), and assignee, then save
  - Expected: A new task card appears in the first column showing the entered due date, priority, and assignee

- [ ] FT-04: Task can be dragged between columns and the move persists
  - Action: Drag a task card from "To Do" to "In Progress", then switch away and back (or reload)
  - Expected: The card is now under "In Progress" and remains there after navigation/reload

- [ ] FT-05: Keyword search returns matching tasks
  - Action: Type an existing task keyword into the search field and apply
  - Expected: Only task cards containing that keyword remain visible; non-matching cards are hidden

- [ ] FT-06: Tasks can be filtered by assignee and by status
  - Action: Choose a specific assignee from the filter control; then re-filter by a status/column value
  - Expected: Only tasks assigned to that person show; then only tasks of the chosen status show

- [ ] FT-07: User can mark progress on a task
  - Action: Open a task and update its progress (e.g., checkbox or progress %), save
  - Expected: The task card reflects the new progress value (e.g., "60%" or a completion indicator)

- [ ] FT-08: Overall project status summary is visible
  - Action: Open a project's board and read the summary/header area
  - Expected: A concise summary is shown (e.g., total tasks, tasks per status, % complete, overdue count)

- [ ] FT-09: User can send a message in the project's chat panel
  - Action: In the chat panel of the open project, type a message and click "Send"
  - Expected: The message immediately appears in the chat list with sender name and timestamp

- [ ] FT-10: Chat updates in real time across sessions
  - Action: Open the same project in two browser windows; send a message in window A
  - Expected: The message appears in window B's chat panel without reloading the page

## Constraint
- [ ] CS-01: Task creation requires a title
  - Action: Open "Add Task", leave the title empty, and attempt to save
  - Expected: Save is blocked and a validation message appears on the title field; no empty task card is added

- [ ] CS-02: Boards are isolated between projects
  - Action: Note tasks in Project A, then switch to Project B; also add a task in Project B
  - Expected: Project A's tasks never appear in Project B's board, and vice versa

- [ ] CS-03: Empty chat messages cannot be sent
  - Action: Click "Send" with an empty (or whitespace-only) chat input
  - Expected: No message is added to the chat; the input stays focused/empty

- [ ] CS-04: Search/filter with no matches shows an empty state
  - Action: Enter a keyword that no task contains (e.g., "zzzz9999")
  - Expected: All non-matching cards are hidden and a "no results"/empty message is shown; the app does not error or blank the page

## Interaction
- [ ] IX-01: Dragging gives visual feedback
  - Action: Click and hold a task card and drag it over another column without dropping
  - Expected: A drag ghost/placeholder is visible and the target column is visually highlighted as a valid drop zone

- [ ] IX-02: Success feedback on creating a project or task
  - Action: Complete project creation, then task creation
  - Expected: A toast/confirmation (e.g., "Project created", "Task added") is shown for each, and it disappears automatically

- [ ] IX-03: Chat auto-scrolls to new messages
  - Action: Scroll up in the chat history, then trigger an incoming message (second session or own send)
  - Expected: The message list scrolls/jumps to the newest message so it is visible without manual scrolling

## Content
- [ ] CT-01: Default data matches the theme
  - Action: Load the page fresh and inspect the project list, boards, and team members
  - Expected: At least 2 pre-existing projects exist, each with a kanban board containing task cards, and a roster of named team members/assignees

- [ ] CT-02: Task cards display complete metadata
  - Action: Inspect several default task cards on a board
  - Expected: Each card shows its title plus due date, priority label, and assignee with relevant, non-placeholder text (no "lorem ipsum"/broken fields)

- [ ] CT-03: Status summary figures match the board
  - Action: Manually count tasks per column, then compare with the summary values
  - Expected: Summary counts/percentages equal the actual board contents and update after FT-04 (drag) and FT-07 (progress change)