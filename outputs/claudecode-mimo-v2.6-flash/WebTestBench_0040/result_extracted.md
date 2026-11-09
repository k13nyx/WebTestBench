# Test Result

## Functionality
- [X] FT-01: Create a new task on the Kanban board
  - Action: Click the add/create task control, enter a title (e.g., "Prepare sprint report"), and submit.
  - Expected: The new task card appears in the board's default/start column with its title visible.

- [X] FT-02: Assign a task to a specific teammate
  - Action: Create a task selecting a teammate (e.g., "Alice") in the assignee field, or edit an existing task to assign "Alice".
  - Expected: The task card and its detail view both display "Alice" as the assignee.
  - Note: This app's roster has no "Alice" (roster: Alex Chen, Sarah Kim, Marcus Johnson, Emma Wilson); assigned **Alex Chen** as the specific teammate. Card avatar shows "Alex Chen" and detail view shows "Alex Chen".

- [X] FT-03: Set a due date on a task
  - Action: Create or edit a task and set a due date (e.g., 2026-11-20), then save.
  - Expected: The due date is displayed on the task card and/or in its detail view as selected.
  - Note: Card showed "Nov 20", detail view input showed exact value "2026-11-20". Re-verified after edit: card "Dec 25", detail "2026-12-25".

- [X] FT-04: Update task status by moving it between columns
  - Action: Drag (or move via control) a task from its current column to another status column (e.g., "To Do" → "In Progress").
  - Expected: The task card now appears only in the target column, and the column's task count updates accordingly.
  - Note: Moved via detail-view Status control: card appeared only in "In Progress"; counts updated To Do 4→3, In Progress 2→3.

- [X] FT-05: Open a task to view its details
  - Action: Click on an existing task card.
  - Expected: A detail view opens showing the task's title, assignee, due date, status/column, and any notes.

- [ ] FT-06: Edit a task's information
  - Action: Open a task, change its title and due date, and save.
  - Expected: The updated title and due date are reflected both in the detail view and on the board card.
  - Bug Report:
    - Issue: Stale detail view after saving edits (UI does not refresh open dialog)
    - Actual: Immediately after clicking "Save", the board card updated to "Prepare sprint report v2" / "Dec 25", but the still-open detail view continued showing the old title "Prepare sprint report" and old due date "2026-11-20" (and old Status "To Do" after the status change). Updated values only appeared in the detail view after closing and reopening the dialog.

- [ ] FT-07: Add a status update/note to a task
  - Action: Open a task, type a short note (e.g., "Waiting on design review") in the notes/update field, and submit.
  - Expected: The note is saved and appears in the task's detail view notes/updates list.
  - Bug Report:
    - Issue: Notes list does not update after submitting a note (stale detail view)
    - Actual: After submitting "Waiting on design review" (and a second note), the note field cleared and the card's comment badge incremented (1→2), but the open detail view kept showing "Notes & Updates (0)" and "No notes yet. Add the first one above." The notes only became visible in the detail view after closing and reopening the dialog.

- [X] FT-08: Filter tasks by assignee
  - Action: Select a teammate (e.g., "Alice") in the assignee filter.
  - Expected: Only tasks assigned to "Alice" remain visible (or are clearly highlighted) while other tasks are hidden/de-emphasized.
  - Note: Selected Alex Chen (no "Alice" in roster). Only his 2 tasks remained in DOM; other columns showed counts 0 and "No tasks yet".

- [X] FT-09: Filter tasks by status
  - Action: Select a status (e.g., "In Progress") in the status filter.
  - Expected: Only tasks in the "In Progress" status are shown (or clearly highlighted) across the board.
  - Note: Only the 3 In Progress tasks remained; To Do/Review/Done columns showed count 0 and "No tasks yet".

- [X] FT-10: Clear active filters
  - Action: With a filter applied, clear/reset the assignee or status filter.
  - Expected: All tasks on the board become visible again with no filtering applied.
  - Note: "Clear" button removed both the assignee filter and status filter; full board restored (4/3/1/2 = 10 tasks) after each.

## Constraint
- [ ] CS-01: Cannot create a task with an empty title
  - Action: Open the create-task form, leave the title field empty, and submit.
  - Expected: An error/validation message appears, no task is created, and the form remains open.
  - Bug Report:
    - Issue: Missing validation message (silent prevention only)
    - Actual: With an empty title, the "Create Task" button is disabled and clicking it does nothing; typing then clearing the title and blurring also produces no message. No task is created and the form stays open, but no error/validation message ever appears anywhere in the dialog.

- [X] CS-02: Cannot add an empty note to a task
  - Action: Open a task detail, leave the note field empty, and click the add/submit note button.
  - Expected: The empty note is rejected (button disabled or validation message shown) and no blank note is added to the list.

## Interaction
- [ ] IX-01: Success feedback after creating a task
  - Action: Create a valid new task and submit.
  - Expected: A visible confirmation (e.g., toast/message) appears indicating the task was created, alongside the new card on the board.
  - Bug Report:
    - Issue: No success feedback/toast on task creation
    - Actual: The new card appeared on the board, but the Notifications region (`<ol>` in "Notifications (F8)") remained empty at 0 ms, 300 ms, and 1000 ms after clicking "Create Task"; zero toast DOM elements (`[data-sonner-toast]`) were ever rendered. No confirmation message appeared anywhere on screen.

- [ ] IX-02: Success feedback after adding a note
  - Action: Add a valid note to a task.
  - Expected: A visible confirmation appears and the note field clears after submission.
  - Bug Report:
    - Issue: No success feedback/toast on note submission
    - Actual: The note field cleared correctly after submission, but no visible confirmation appeared — the Notifications region stayed empty immediately and 1.5 s after submitting, and the notes list itself still showed "No notes yet" (see FT-07).

- [X] IX-03: Task detail view opens and closes correctly
  - Action: Click a task card to open details, then click the close (×) button.
  - Expected: The detail view opens over the board; closing it returns to the full board with no lingering overlay.

- [X] IX-04: Filtered/highlighted tasks are visually distinguished
  - Action: Apply an assignee or status filter.
  - Expected: Matching tasks are visually highlighted (or non-matching tasks visibly dimmed/hidden) so the focused set is immediately apparent.

## Content
- [X] CT-01: Assignee names shown on tasks match the teammate roster
  - Action: Inspect several task cards and their detail views.
  - Expected: Every displayed assignee name corresponds exactly to a teammate available in the assignee selection list—no blank, unknown, or mismatched names.
  - Note: Roster = Alex Chen, Sarah Kim, Marcus Johnson, Emma Wilson (+ Unassigned). All card avatars and detail views showed only these names; zero unknown names found. (One task was left unassigned by design and displays no name.)

- [X] CT-02: Due dates are displayed accurately and readably
  - Action: Compare the due dates shown on task cards/detail views with the dates entered during creation/editing.
  - Expected: Displayed dates match the entered dates exactly and are shown in a consistent, readable format.
  - Note: Entered 2026-11-20 → card "Nov 20", detail "2026-11-20"; entered 2026-12-25 → card "Dec 25", detail "2026-12-25". All cards use one consistent "Mon D" format (Dec 8, Dec 10, Dec 14, Dec 15, Dec 16, Dec 18, Dec 20, Dec 25).

- [X] CT-03: Notes/status updates display their full content
  - Action: Add two distinct notes to a task and review the detail view.
  - Expected: Both notes appear with their full original text intact, in a logical (e.g., newest-last or newest-first) order.
  - Note: Detail view showed "Notes & Updates (2)": "Waiting on design review" (Nov 9, 2:17 AM) then "Design tokens finalized" (Nov 9, 2:18 AM) — full text intact, chronological newest-last order.
