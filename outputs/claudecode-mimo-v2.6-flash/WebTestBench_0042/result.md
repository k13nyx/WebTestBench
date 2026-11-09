All remaining verifications are complete. Send button click succeeded: message **"You | 02:37 | Sent via the send button"** appended immediately, input cleared, button re-disabled, no reload (marker intact), message in viewport.

**Final state of evidence gathered — compiling results:**

# Test Result

## Functionality
- [X] FT-01: Create a new project
  - Action: Click the "New Project" (or "Create Project") button and submit a project name.
  - Expected: The new project appears in the project list and can be opened.
- [X] FT-02: Switch between multiple projects
  - Action: Select a different project from the project list/navigation.
  - Expected: The page displays that project's own kanban board, summary, and chat panel, with no data from the previous project.
- [X] FT-03: Create a task with full details
  - Action: Click "Add Task" (or "New Task") and enter a title, due date, priority, and assignee, then save.
  - Expected: The task card appears in the selected column showing its title, due date, priority, and assignee.
- [ ] FT-04: Drag a task between columns
  - Action: Drag a task card from its current column to another column (e.g., "To Do" → "In Progress").
  - Expected: The task card moves to the target column and remains there after a page refresh.
  - Bug Report:
    - Issue: Data Not Persisted (State Lost on Refresh)
    - Actual: The drag itself succeeded in-session (card moved To Do → In Progress, confirmed in droppable "in-progress"), but after a page refresh the entire application reset to seed data: the moved task no longer existed, the created task "Integrate payment gateway" vanished, and the new project "QA Test Project" disappeared from the sidebar. The card did not remain in the target column after refresh because no changes are persisted.
- [X] FT-05: Filter tasks by status
  - Action: Select a status filter (e.g., "In Progress") from the filter control.
  - Expected: Only tasks in that status are shown; other tasks are hidden.
- [X] FT-06: Filter tasks by assignee
  - Action: Select a specific assignee from the assignee filter.
  - Expected: Only tasks assigned to that person are shown across the board.
- [X] FT-07: Search tasks by keyword
  - Action: Type a keyword matching an existing task title into the search box.
  - Expected: Only tasks whose title/description contains the keyword are displayed.
- [X] FT-08: Mark task progress
  - Action: Change a task's progress/status (e.g., move to "Done" or update its progress indicator).
  - Expected: The task displays the updated status, and the project summary reflects the change.
- [X] FT-09: Send a chat message
  - Action: Type a message in the project chat panel and press send.
  - Expected: The message appears in the chat panel with sender name and timestamp.

## Constraint
- [ ] CS-01: Cannot create a task with empty title
  - Action: Open the task creation form, leave the title field empty, and try to save.
  - Expected: Saving is blocked and a validation message indicates the title is required; no empty task is created.
  - Bug Report:
    - Issue: Missing Validation Message (Silent Failure)
    - Actual: With title empty (due date filled), clicking "Create" kept the dialog open and created no task, but NO validation message was ever displayed — no error text in the dialog, no aria-invalid attribute (title input has required="false"), no toast/notification. The user gets zero feedback about why saving failed.
- [ ] CS-02: Cannot create a task without a due date
  - Action: Open the task creation form, leave the due date empty, and try to save.
  - Expected: Saving is blocked with a validation message; no task is created.
  - Bug Report:
    - Issue: Missing Due-Date Validation (Task Created Without Due Date)
    - Actual: With a title filled and the due date cleared, clicking "Create" succeeded — the dialog closed and a new task "Validation probe task" (no due date, card shows only priority "Medium", no date) was added to the To Do column (task count rose 5 → 6). Saving was not blocked and no validation message appeared; the date input has required="false".
- [X] CS-03: Cannot send an empty chat message
  - Action: Click the chat send button with an empty or whitespace-only message input.
  - Expected: No message is posted to the chat.
- [X] CS-04: Filters combine correctly without conflicting results
  - Action: Apply a status filter and an assignee filter simultaneously where they intersect.
  - Expected: Only tasks matching BOTH criteria are shown; no task violating either filter appears.

## Interaction
- [X] IX-01: Project summary updates after task changes
  - Action: Move a task to "Done" (or change its status) and observe the project summary area.
  - Expected: The summary (task counts/progress) updates immediately to reflect the new state without a manual refresh.
- [ ] IX-02: Filters and search respond immediately
  - Action: Type in the search box or toggle a filter.
  - Expected: The board updates within a moment with no page reload, and a visible "clear/reset filters" control restores the full task list when used.
  - Bug Report:
    - Issue: Missing Clear/Reset Filters Control
    - Actual: Search and filters do update the board instantly with no reload (verified: URL unchanged while typing "authentication" left only "Implement authentication flow"), but the toolbar contains ONLY the search input and the two dropdowns — a DOM scan of the entire page found no clear/reset button of any kind. The full task list can only be restored by manually setting each dropdown back to "All Status"/"All Members" and emptying the search box; the required visible reset control does not exist.
- [X] IX-03: Drag feedback on kanban board
  - Action: Hover and start dragging a task card over a column.
  - Expected: The card visually follows the cursor and the target column indicates it is a valid drop target; on drop, the card settles in the new column.
- [X] IX-04: Chat panel shows new messages in real time
  - Action: Send a message in the chat panel.
  - Expected: The message appends to the conversation immediately, scrolled into view, without reloading the page.

## Content
- [X] CT-01: Task cards display complete, accurate details
  - Action: Inspect an existing task card created with a due date, priority, and assignee.
  - Expected: The card shows the correct due date, the correct priority level label, and the correct assignee name — all matching what was entered.
- [X] CT-02: Chat messages show sender and timestamp
  - Action: Review messages in the project chat panel.
  - Expected: Each message displays the sender's name and a readable timestamp, and messages belong to the current project's discussion.
- [X] CT-03: Project summary content matches board data
  - Action: Compare the summary figures (total tasks, per-status counts, completion percentage) with the visible tasks on the board.
  - Expected: All summary figures exactly match the actual tasks shown on the board.

---

**Summary: 16 PASS / 4 FAIL**

| Failed | Root cause |
|---|---|
| FT-04 | No persistence — refresh resets app to seed data (task move, tasks, and created project all lost) |
| CS-01 | Empty-title save is blocked but silently — no validation message ever shown (`required=false`, no error text/toast) |
| CS-02 | Due-date validation entirely missing — task without due date was created successfully |
| IX-02 | Filters apply live, but no clear/reset filters control exists anywhere in the toolbar |