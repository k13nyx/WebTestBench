# Test Result

## Functionality
- [ ] FT-01: Create a new project and open its kanban board
  - Action: Click "New Project", enter name "Website Redesign", confirm, then open the project.
  - Expected: The project appears in the project list and its board opens showing the default columns ("To Do", "In Progress", "Done").
  - Bug Report:
    - Issue: Incorrect default board columns (extra column)
    - Actual: The project was created and appeared in the project list, and its empty board opened automatically — but with 4 columns "To Do, In Progress, Review, Done" instead of the expected default columns "To Do, In Progress, Done" ("Review" is an unexpected extra default column).

- [X] FT-02: Switch between multiple projects
  - Action: Select a different project from the project list/switcher.
  - Expected: The board, chat panel, and summary update to show the selected project's data.

- [ ] FT-03: Create a task with due date, priority, and assignee
  - Action: Click "New Task", enter title "Design homepage", set due date, set priority "High", set assignee from the member list, save.
  - Expected: A task card with that title appears in the "To Do" column and persists after reload.
  - Bug Report:
    - Issue: Data not persisted across page reload (task lost)
    - Actual: The task card "Design homepage … High Dec 15" appeared in the "To Do" column after saving, but after page reload the card was gone and the board reverted to the original seed tasks. localStorage/sessionStorage are empty — all created/edited data resets on every page load.

- [X] FT-04: Edit an existing task's details
  - Action: Open an existing task, change its title/due date/priority/assignee, save.
  - Expected: The task card reflects all updated values on the board.

- [ ] FT-05: Drag a task between columns
  - Action: Drag a task card from "To Do" to "In Progress".
  - Expected: The task moves to "In Progress" and stays there after reload.
  - Bug Report:
    - Issue: Data not persisted across page reload (column change reverts)
    - Actual: The drag works — "Optimize images for web" moved to "In Progress" immediately (summary updated to "1 To Do 3 In Progress") — but after page reload the task was back in "To Do".

- [X] FT-06: Filter tasks by status
  - Action: Set the status filter to "Done".
  - Expected: Only tasks in the "Done" column (or with status Done) are listed; other tasks are hidden.

- [X] FT-07: Filter tasks by assignee
  - Action: Set the assignee filter to a specific team member.
  - Expected: Only tasks assigned to that member are shown; tasks of other assignees are hidden.

- [X] FT-08: Search tasks by keyword
  - Action: Type "homepage" in the search box.
  - Expected: Only tasks whose title or description contains "homepage" are shown.

- [X] FT-09: Combine keyword search with filters
  - Action: Enter a keyword and simultaneously set the assignee filter.
  - Expected: Results match both the keyword and the assignee; clearing filters restores the full task list.

- [ ] FT-10: Mark progress on a task
  - Action: Open a task and set its progress (e.g., progress value 50% or "In Progress" status), save.
  - Expected: The task card shows the new progress value, and the change persists after reload.
  - Bug Report:
    - Issue: Data not persisted across page reload (progress change lost)
    - Actual: Progress was set to 50% via the editor slider and the card showed "Progress 50%" after saving, but after page reload the card showed "Progress 40%" again (reverted to stored seed value).

- [ ] FT-11: View the project's overall status summary
  - Action: Open the project summary panel/section.
  - Expected: The summary shows counts of total tasks, tasks per status column, and completion (e.g., % or "n of m done") for the current project.
  - Bug Report:
    - Issue: Missing total task count in project summary
    - Actual: The summary section shows only per-status counts and completion ("2 To Do 2 In Progress 1 Review 1 Done 17% Complete"); there is no total task count (e.g., "6 tasks") displayed anywhere in the summary.

- [ ] FT-12: Send a chat message in the project chat panel
  - Action: Type "When is the kickoff?" in the chat input and send.
  - Expected: The message appears in the chat panel with sender name and timestamp, and persists after reload.
  - Bug Report:
    - Issue: Data not persisted across page reload (chat message lost)
    - Actual: The message "You 15:15 When is the kickoff?" appeared immediately with sender and timestamp, but after page reload it was gone (only the 3 seeded messages remained).

- [ ] FT-13: Receive a chat message in real time
  - Action: Have another team member send a message in the same project's chat, without reloading the page.
  - Expected: The new message appears in the chat panel automatically within a few seconds.
  - Bug Report:
    - Issue: No real-time chat delivery (messages do not sync between sessions)
    - Actual: A message sent from a second browser session ("Hello from teammate") never appeared in the first session's chat panel even after waiting 6+ seconds without reload. Additionally, no incoming message ever arrives automatically (7s watch after sending) and the app makes zero network calls (no fetch/XHR/WebSocket) — chat state is isolated in-memory per session. (Note: the second session runs as the same user "You"; true multi-member impersonation was not possible in this environment.)

## Constraint
- [ ] CS-01: Task cannot be created without a title
  - Action: Click "New Task", leave the title empty, set other fields, save.
  - Expected: Save is blocked and an inline validation error indicates the title is required; no task is added.
  - Bug Report:
    - Issue: Missing inline validation error on required field
    - Actual: Save is silently blocked (dialog stays open, no task added) but no validation error is displayed at all: no error message text in the dialog, no `aria-invalid`/`aria-describedby` on the title input, no error styling (border unchanged), and no alert/live-region content.

- [ ] CS-02: Task due date cannot be set to an invalid value
  - Action: Enter a malformed or past due date (e.g., "2020-01-01" or "abc") and save.
  - Expected: Save is blocked with a validation message about the due date; no task is created/updated.
  - Bug Report:
    - Issue: Invalid (past) due date accepted without validation
    - Actual: With title "Date test task" and due date "2020-01-01" the save succeeded — the task was created with the past due date and no validation message appeared. (Malformed input "abc" is rejected only by the native `type=date` control itself, with no app-level message.)

- [X] CS-03: Task assignee must be a member of the project
  - Action: Open the assignee dropdown for a task.
  - Expected: Only project team members are selectable; no external/non-member accounts are offered.

- [ ] CS-04: Empty required project name is rejected
  - Action: Click "New Project" and confirm with a blank name.
  - Expected: Creation is blocked with a validation message; no empty project is added to the list.
  - Bug Report:
    - Issue: Missing validation message on required project name
    - Actual: Creation is silently blocked (dialog stays open, project list unchanged at 2 projects) but no validation message is shown: no error text in the dialog, no `aria-invalid` or error styling on the name input, no alert/live-region content.

- [ ] CS-05: Task status stays consistent after drag and progress update
  - Action: Mark a task's progress as complete/100% via the task editor, then inspect the board.
  - Expected: The task appears in (or is labeled with) the "Done" status and is not shown simultaneously in a conflicting column status.
  - Bug Report:
    - Issue: Task status inconsistent with 100% progress
    - Actual: After setting progress to 100% and saving, "User testing sessions" remains in the "In Progress" column with no "Done" label — a conflicting state (100% complete but In Progress). Its progress indicator also disappears entirely at 100% ("Progress X%" text vanishes from the card).

## Interaction
- [X] IX-01: Drag feedback and drop confirmation on the board
  - Action: Drag a task card over each column and drop it.
  - Expected: The target column highlights while the card is dragged over it, and the card settles into the target column immediately after drop.

- [X] IX-02: Filter and search update results without page reload
  - Action: Change the status filter, assignee filter, and search keyword one after another.
  - Expected: The task list/board updates in place for each change with no full page reload.

- [X] IX-03: Progress/status change updates the project summary immediately
  - Action: Move a task to "Done" and open/refresh the summary view without reloading the page.
  - Expected: The summary counts (e.g., done count, completion percentage) reflect the change immediately.

- [X] IX-04: Chat panel is attached to and scoped to the active project
  - Action: Open the chat panel, then switch to a different project.
  - Expected: The chat panel shows the second project's conversation history, not the previous project's messages.

## Content
- [X] CT-01: Task cards display all required task information
  - Action: Inspect any existing task card on the board.
  - Expected: Each card shows the task title, due date, priority label, and assignee name; all values match the task's stored data.

- [X] CT-02: Priority is displayed with distinct, meaningful labels
  - Action: Inspect tasks of different priorities (e.g., Low, Medium, High).
  - Expected: Each priority level is visibly distinguishable (distinct label/text) and matches the set priority value.

- [X] CT-03: Project summary content is relevant to the project
  - Action: Read the project summary panel.
  - Expected: The summary lists only metrics about the current project's tasks (status breakdown, completion) with no data from other projects.

- [X] CT-04: Chat messages show sender and time and match the project discussion
  - Action: Read the chat panel history for a project.
  - Expected: Each message shows sender name, timestamp, and message text; messages are discussion content belonging to that project.
