# Test Checklist

## Functionality
- [ ] FT-01: Multiple projects are listed and each opens its own kanban board
  - Action: On the project management page, note the number of default projects in the project list; click a project name (e.g., the second project in the list).
  - Expected: At least two projects are listed, and clicking one opens a kanban board area displaying that project's kanban board with its columns and task cards.

- [ ] FT-02: User can create a task with due date, priority, and assignee
  - Action: On an open project's board, click "Add Task"/"+", fill in title, due date, priority, and assignee, then submit.
  - Expected: The new task card appears in the board's first/selected column and its saved detail shows the exact title, due date, priority, and assignee entered.

- [ ] FT-03: Task can be dragged between kanban columns
  - Action: Drag an existing task card from its current column and drop it into a different column (e.g., from "To Do" to "In Progress").
  - Expected: The card is displayed in the target column, its status in the task detail equals the target column's status, and it remains there after a page reload.

- [ ] FT-04: Tasks can be filtered by status
  - Action: Set the status filter to one status (e.g., "In Progress") using the board's filter control.
  - Expected: Only cards matching that status are displayed; all cards of other statuses are hidden.

- [ ] FT-05: Tasks can be filtered by assignee
  - Action: Set the assignee filter to one default team member.
  - Expected: Only cards assigned to that member are displayed; cards assigned to others or unassigned are hidden.

- [ ] FT-06: Tasks can be searched by keyword
  - Action: Type a word that exists in a default task's title into the search box.
  - Expected: Only cards whose title contains that keyword are displayed; non-matching cards are hidden.

- [ ] FT-07: Progress can be marked on a task
  - Action: Open an existing task and set its progress (e.g., move the progress control to 50% or toggle a progress/step control), then save/close.
  - Expected: The card displays the updated progress value, and the value persists after reopening the task.

- [ ] FT-08: Concise project status summary is displayed
  - Action: Open a default project and locate the project summary area.
  - Expected: The summary shows the project's overall status concisely — total tasks, count per status, and a completion percentage that matches the board's card data.

- [ ] FT-09: User can post a message in the project chat panel
  - Action: In the chat panel of the open project, type "Status update from QA" and send it.
  - Expected: The message appears in the chat panel's message list with the sender name and is visible immediately after sending.

- [ ] FT-10: Chat panel updates in real time without a manual refresh
  - Action: With the project page open, have a second team member (or a second browser session) post a message in the same project's chat; do not reload the first page.
  - Expected: The new message appears in the first page's chat panel automatically without refreshing or re-navigating.

## Constraint
- [ ] CS-01: Task cannot be created with an empty title
  - Action: Open the task creation form and submit it with the title field left empty.
  - Expected: The task is not created, no empty card is added to the board, and a required-field indication is shown on the title field.

- [ ] CS-02: Filter/search with no matches shows an empty result state
  - Action: Enter a nonsense keyword (e.g., "zzzznotarealtask") in the search box.
  - Expected: No task cards are displayed and an explicit "no tasks"/"no results" empty-state message is shown instead of stale results.

- [ ] CS-03: Empty chat message cannot be sent
  - Action: In the chat input, leave the field empty (or only spaces) and attempt to send.
  - Expected: The send action is disabled or rejected, and no empty message bubble is added to the conversation.

- [ ] CS-04: Multiple filters applied together return only tasks matching all criteria
  - Action: Apply a status filter and an assignee filter together where at least one task matches both.
  - Expected: Only cards satisfying both the status and the assignee criteria are displayed.

- [ ] CS-05: Tasks are scoped to the selected project
  - Action: Note the task titles in Project A's board, then switch to a different default project (Project B).
  - Expected: None of Project A's task titles appear in Project B's board; only Project B's tasks are shown.

## Interaction
- [ ] IX-01: Drag operation shows a drop indicator in the target column
  - Action: Start dragging a task card and hover it over a different column without releasing.
  - Expected: The target column displays a visible drop indicator/placeholder, and the dragged card is visually distinguished from the others.

- [ ] IX-02: Filters and search apply immediately without a page reload
  - Action: Change the status filter and then type in the search box while watching the board.
  - Expected: The visible cards update instantly on each change, with no full page reload or loss of the current project view.

- [ ] IX-03: New chat message is scrolled into view after sending
  - Action: Send a message in a project chat whose history is long enough to scroll.
  - Expected: The chat list auto-scrolls so the newly sent message is visible at the bottom, and the input field is cleared and refocused.

## Content
- [ ] CT-01: Each task card displays title, due date, priority, and assignee
  - Action: Inspect three default task cards on a project board.
  - Expected: Every card displays its title, a due date, a priority indication, and an assignee name/avatar matching the values in its detail view.

- [ ] CT-02: Kanban columns are labeled with statuses and contain the project's default tasks
  - Action: Observe the column headers and the cards within them on an open project board.
  - Expected: Each column has a distinct status label, all default tasks of the project are present in exactly one column, and the labels match the statuses available in the status filter.

- [ ] CT-03: Chat messages show sender and timestamp and belong to the current project
  - Action: Inspect the chat panel messages in Project A, then switch to Project B and inspect its chat.
  - Expected: Every message shows a sender name and a timestamp, and Project B's chat contains no messages that appeared only in Project A's chat.