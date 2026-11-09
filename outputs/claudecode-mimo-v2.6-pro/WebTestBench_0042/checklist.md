# Test Checklist

## Functionality
- [ ] FT-01: Create a new project and open its kanban board
  - Action: Click "New Project", enter name "Website Redesign", confirm, then open the project.
  - Expected: The project appears in the project list and its board opens showing the default columns ("To Do", "In Progress", "Done").

- [ ] FT-02: Switch between multiple projects
  - Action: Select a different project from the project list/switcher.
  - Expected: The board, chat panel, and summary update to show the selected project's data.

- [ ] FT-03: Create a task with due date, priority, and assignee
  - Action: Click "New Task", enter title "Design homepage", set due date, set priority "High", set assignee from the member list, save.
  - Expected: A task card with that title appears in the "To Do" column and persists after reload.

- [ ] FT-04: Edit an existing task's details
  - Action: Open an existing task, change its title/due date/priority/assignee, save.
  - Expected: The task card reflects all updated values on the board.

- [ ] FT-05: Drag a task between columns
  - Action: Drag a task card from "To Do" to "In Progress".
  - Expected: The task moves to "In Progress" and stays there after reload.

- [ ] FT-06: Filter tasks by status
  - Action: Set the status filter to "Done".
  - Expected: Only tasks in the "Done" column (or with status Done) are listed; other tasks are hidden.

- [ ] FT-07: Filter tasks by assignee
  - Action: Set the assignee filter to a specific team member.
  - Expected: Only tasks assigned to that member are shown; tasks of other assignees are hidden.

- [ ] FT-08: Search tasks by keyword
  - Action: Type "homepage" in the search box.
  - Expected: Only tasks whose title or description contains "homepage" are shown.

- [ ] FT-09: Combine keyword search with filters
  - Action: Enter a keyword and simultaneously set the assignee filter.
  - Expected: Results match both the keyword and the assignee; clearing filters restores the full task list.

- [ ] FT-10: Mark progress on a task
  - Action: Open a task and set its progress (e.g., progress value 50% or "In Progress" status), save.
  - Expected: The task card shows the new progress value, and the change persists after reload.

- [ ] FT-11: View the project's overall status summary
  - Action: Open the project summary panel/section.
  - Expected: The summary shows counts of total tasks, tasks per status column, and completion (e.g., % or "n of m done") for the current project.

- [ ] FT-12: Send a chat message in the project chat panel
  - Action: Type "When is the kickoff?" in the chat input and send.
  - Expected: The message appears in the chat panel with sender name and timestamp, and persists after reload.

- [ ] FT-13: Receive a chat message in real time
  - Action: Have another team member send a message in the same project's chat, without reloading the page.
  - Expected: The new message appears in the chat panel automatically within a few seconds.

## Constraint
- [ ] CS-01: Task cannot be created without a title
  - Action: Click "New Task", leave the title empty, set other fields, save.
  - Expected: Save is blocked and an inline validation error indicates the title is required; no task is added.

- [ ] CS-02: Task due date cannot be set to an invalid value
  - Action: Enter a malformed or past due date (e.g., "2020-01-01" or "abc") and save.
  - Expected: Save is blocked with a validation message about the due date; no task is created/updated.

- [ ] CS-03: Task assignee must be a member of the project
  - Action: Open the assignee dropdown for a task.
  - Expected: Only project team members are selectable; no external/non-member accounts are offered.

- [ ] CS-04: Empty required project name is rejected
  - Action: Click "New Project" and confirm with a blank name.
  - Expected: Creation is blocked with a validation message; no empty project is added to the list.

- [ ] CS-05: Task status stays consistent after drag and progress update
  - Action: Mark a task's progress as complete/100% via the task editor, then inspect the board.
  - Expected: The task appears in (or is labeled with) the "Done" status and is not shown simultaneously in a conflicting column status.

## Interaction
- [ ] IX-01: Drag feedback and drop confirmation on the board
  - Action: Drag a task card over each column and drop it.
  - Expected: The target column highlights while the card is dragged over it, and the card settles into the target column immediately after drop.

- [ ] IX-02: Filter and search update results without page reload
  - Action: Change the status filter, assignee filter, and search keyword one after another.
  - Expected: The task list/board updates in place for each change with no full page reload.

- [ ] IX-03: Progress/status change updates the project summary immediately
  - Action: Move a task to "Done" and open/refresh the summary view without reloading the page.
  - Expected: The summary counts (e.g., done count, completion percentage) reflect the change immediately.

- [ ] IX-04: Chat panel is attached to and scoped to the active project
  - Action: Open the chat panel, then switch to a different project.
  - Expected: The chat panel shows the second project's conversation history, not the previous project's messages.

## Content
- [ ] CT-01: Task cards display all required task information
  - Action: Inspect any existing task card on the board.
  - Expected: Each card shows the task title, due date, priority label, and assignee name; all values match the task's stored data.

- [ ] CT-02: Priority is displayed with distinct, meaningful labels
  - Action: Inspect tasks of different priorities (e.g., Low, Medium, High).
  - Expected: Each priority level is visibly distinguishable (distinct label/text) and matches the set priority value.

- [ ] CT-03: Project summary content is relevant to the project
  - Action: Read the project summary panel.
  - Expected: The summary lists only metrics about the current project's tasks (status breakdown, completion) with no data from other projects.

- [ ] CT-04: Chat messages show sender and time and match the project discussion
  - Action: Read the chat panel history for a project.
  - Expected: Each message shows sender name, timestamp, and message text; messages are discussion content belonging to that project.