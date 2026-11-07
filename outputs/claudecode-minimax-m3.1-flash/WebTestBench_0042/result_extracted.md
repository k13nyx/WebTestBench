# Test Result

## Functionality

- [X] FT-01: Multiple projects are listed and each has its own independent kanban board
  - Action: Open the project management page; note the list of default projects; select a second project from the project list.
  - Expected: At least two default projects are listed; switching selection loads the second project's own columns and task cards, distinct from the first project's board.

- [X] FT-02: A task can be created with title, due date, priority, and assignee
  - Action: On the active project, click the "Add Task"/"New Task" control; enter a title, set a due date, choose a priority, and select an assignee; save.
  - Expected: The new task appears as a card in the board's first/To Do column and displays the entered due date, priority, and assignee.

- [X] FT-03: A task can be dragged from one column to another
  - Action: Drag an existing task card from the "To Do" column and drop it onto the "In Progress" column.
  - Expected: The card relocates into the "In Progress" column, is no longer present in "To Do", and is counted under "In Progress" in the project summary.

- [X] FT-04: Tasks can be filtered by status
  - Action: Use the status filter control to select "Done"; observe the board.
  - Expected: Only tasks whose status is "Done" remain visible; tasks in other columns are hidden and the visible count matches.

- [X] FT-05: Tasks can be filtered by assignee
  - Action: Select a specific team member in the assignee filter; observe the board.
  - Expected: Only tasks assigned to that member are displayed; tasks assigned to other members are hidden.

- [X] FT-06: Tasks can be searched by keyword
  - Action: Type a distinctive word from one default task's title into the search field; observe results.
  - Expected: Only tasks whose title/description contains that keyword are shown; unrelated tasks are hidden.

- [X] FT-07: Progress can be marked on a task
  - Action: Open a task and change its progress value (e.g., set progress to 50%).
  - Expected: The task card reflects the updated progress (progress indicator and/or value) and the saved value persists after the task panel is closed and reopened.

- [X] FT-08: A concise overall project status summary is displayed
  - Action: Open a project and locate the summary/statistics area above or beside the board.
  - Expected: The summary shows per-status task counts and/or a completion metric consistent with the tasks currently on the board.

- [ ] FT-09: Each project has a working real-time chat panel
  - Action: Open the chat panel for the active project and send a message with text "Realtime check 1"; then, in a second browser session on the same project, observe the chat.
  - Expected: The sent message appears in the chat log with its author, and it appears in the second session without a manual page reload.
  - Bug Report:
    - Issue: Missing Real-Time Synchronization / No Server Persistence (chat is local-only client state)
    - Actual: The message was sent successfully and appeared in the sending session's chat with the author label "You" and timestamp "20:43". However, in a second browser session (second tab on the same project, chat panel open *before* the message was sent), the chat log still contained only the 3 default messages ("Just finished the homepage mockups…", "Looking great!…", "Analytics integration is almost done…") after waiting — the new message never arrived without a reload. A fresh load of the app also restored the original default board (no "QA Automation Task", "Optimize images for web" back in To Do, 17% Complete), proving chat messages and task edits are never broadcast or persisted server-side.

## Constraint

- [ ] CS-01: A task cannot be saved without a title
  - Action: Open the new-task form, leave the title blank, fill in the other fields, and attempt to save.
  - Expected: The save is blocked, a validation message appears identifying the missing title, and no task is added to the board.
  - Bug Report:
    - Issue: Missing Validation Feedback (silent save block)
    - Actual: The save was correctly blocked — the "Create Task" dialog stayed open, no card was added (To Do remained at 2 cards), and the task count did not change. However, no validation message was rendered anywhere: the dialog contained no error text, the title input had no `aria-invalid="true"`, no destructive/red styling was applied, and no toast/banner appeared. The user receives no indication of which field is missing.

- [X] CS-02: A task exists in exactly one column after a move
  - Action: Drag a task card from "To Do" to "In Progress", then review all columns.
  - Expected: The card appears in "In Progress" only, with no leftover copy or duplicate in "To Do" or any other column.

- [X] CS-03: Boards, filters, and chat are isolated per project
  - Action: Set a filter/search keyword in project A, switch to project B, then return to project A.
  - Expected: Project B shows its own tasks and its own chat messages (no messages from project A); project A retains its own filter state and tasks.

- [X] CS-04: An empty chat message cannot be sent
  - Action: Open the chat panel, leave the message field empty, and attempt to send.
  - Expected: No message is posted and the chat log remains unchanged.

## Interaction

- [ ] IX-01: The app gives immediate feedback when a task is created
  - Action: Create a task with a title and save.
  - Expected: A confirmation indicator (toast, banner, or inline confirmation) appears within the board area, and the new task is immediately visible.
  - Bug Report:
    - Issue: Missing Confirmation Indicator (no toast/banner/inline feedback)
    - Actual: The new card ("QA Toast Probe") appeared immediately in the To Do column, but no confirmation indicator of any kind was produced. A `MutationObserver` installed on `document.body` before clicking "Create" recorded only the dialog and the new card being added — no toast/banner element was inserted; the Sonner "Notifications" region stayed empty; and the page contained no "created"/"success" text anywhere.

- [X] IX-02: Drag-and-drop gives visible feedback about the drop target
  - Action: Press and hold a task card and drag it over a target column without releasing.
  - Expected: The card shows a dragging state and the column under the cursor is visually highlighted to indicate it will receive the drop.

- [X] IX-03: The summary and progress indicators update live after task changes
  - Action: Note the summary counts, then drag one task to a new column and set another task's progress to 100%.
  - Expected: The summary counts and completion metric update immediately without a page refresh to reflect the moved and completed tasks.

- [X] IX-04: The chat panel can be opened and closed per project without losing messages
  - Action: Open the chat panel, close it, and reopen it for the same project.
  - Expected: The panel opens on demand with the project's existing messages intact, and closing it does not delete or hide messages from other views.

## Content

- [X] CT-01: Task cards display the required task metadata
  - Action: Inspect the task cards currently on the board (including the newly created task).
  - Expected: Each card visibly shows its title, due date, priority, and assignee in a readable form; no required field is blank or shown as raw undefined/placeholder text.

- [X] CT-02: Kanban columns use clear, meaningful status labels
  - Action: Read the column headers on the board.
  - Expected: Headers are recognizable workflow statuses (e.g., To Do, In Progress, Done), are distinct from one another, and contain no placeholder or lorem-ipsum text.

- [X] CT-03: Chat messages are attributed to their sender
  - Action: Read the messages in the project chat panel, including the message sent in FT-09.
  - Expected: Each message shows the author (and a timestamp if displayed), with no unlabeled or empty-sender entries.
