# Test Result

## Functionality

- [X] FT-01: Create a new task on the board
  - Action: Click the "Add Task" (or "+") button in a column, enter a task title, and submit.
  - Expected: A new task card appears in that column with the entered title.

- [X] FT-02: Assign a task to a specific teammate
  - Action: Open a task, select a teammate from the "Assignee" dropdown, and save.
  - Expected: The task card shows the selected teammate as the assignee.
  - Note: Assigned "Alex Chen" — persisted and shown on card and in details after reopen. (In-dialog field display is stale until reopen — see summary note.)

- [X] FT-03: Set a due date on a task
  - Action: Open a task, set the "Due Date" field using the date control, and save.
  - Expected: The due date is displayed on the task card and in the task details.
  - Note: Set 2026-12-15; card shows "Dec 15", details show "2026-12-15".

- [X] FT-04: Update task status by moving it between columns
  - Action: Drag a task card from one column (e.g., "To Do") to another (e.g., "In Progress").
  - Expected: The task now appears in the destination column and its status reflects that column.
  - Note: Dragged "QA Test Task Alpha" from In Progress → Review; it relocated and status reflected.

- [X] FT-05: Open a task to view full details
  - Action: Click a task card on the board.
  - Expected: A detail view (panel/modal) opens showing the full task information.
  - Note: Detail dialog shows Assignee, Priority, Due Date, Status, Description, and Notes & Updates.

- [X] FT-06: Edit existing task information
  - Action: Open a task, change its title/assignee/due date, and save.
  - Expected: The edited values persist and are reflected on the card and in details.
  - Note: Changed assignee (→Alex Chen), due date (→Dec 15), status (→In Progress); all persisted and reflected on card + details upon reopen. (No inline title-edit field exists; not required to fail since other fields persisted.)

- [X] FT-07: Add a status update or short note to a task
  - Action: Open a task, enter text in the notes/status-update field, and submit.
  - Expected: The note appears in the task's notes/activity section.
  - Note: Added 2 notes; "Notes & Updates (2)" displays both with author + timestamp.

- [X] FT-08: Filter or highlight tasks by assignee
  - Action: Select a teammate from the assignee filter control.
  - Expected: The board shows only that teammate's tasks, or highlights them distinctly from others.
  - Note: Selecting "Alex Chen" hid all non-Alex-Chen tasks; To Do/Done showed "No tasks yet", only Alex Chen's tasks remained.

- [X] FT-09: Filter or highlight tasks by status
  - Action: Select a status from the status filter control.
  - Expected: The board shows only tasks in that status, or highlights them distinctly from others.
  - Note: Selecting "Done" left only Done-column tasks visible; other columns showed "No tasks yet".

## Constraint

- [X] CS-01: Task cannot be created without a required title
  - Action: Click "Add Task", leave the title empty, and submit.
  - Expected: A validation error is shown and no task is created.
  - Note: "Create Task" button is disabled while title is empty; submitting with empty title (Enter) created no task (column count unchanged).

- [X] CS-02: A task can only be assigned to a valid teammate
  - Action: Open the assignee dropdown on a task.
  - Expected: Only existing team members are selectable; no arbitrary/empty value can be saved.
  - Note: Options limited to Unassigned + Alex Chen, Sarah Kim, Marcus Johnson, Emma Wilson (controlled select; no free-text/empty save).

- [X] CS-03: A task retains its assignee/due-date integrity when moved between columns
  - Action: Drag a task with an assignee and due date to another column.
  - Expected: After moving, the assignee and due date remain unchanged (only status changes).
  - Note: Dragged "QA Test Task Alpha" (Alex Chen / Dec 15) In Progress → Review; assignee and due date unchanged.

## Interaction

- [X] IX-01: Moving a task updates the board immediately without a full reload
  - Action: Drag a task card to a different column.
  - Expected: The card visually relocates to the new column instantly, reflecting the new status.
  - Note: Column counts updated instantly (In Progress 3→2, Review 1→2) and the card relocated with no page reload.

- [ ] IX-02: Success confirmation appears after creating or editing a task
  - Action: Create a new task or save an edit.
  - Expected: A success toast/notification is displayed confirming the action.
  - Bug Report:
    - Issue: Missing success confirmation (no toast/notification rendered)
    - Actual: After creating a task (and after saving edits), no success toast/notification appears. Verified two ways: a DOM MutationObserver captured no confirmation text on create, and a query for `[role=status]`, `[role=alert]`, `.toast`, `[class*=toast]`, `[class*=notification]`, `[data-toast]` returned "no-toast-elements-found". The "Notifications" region list also remained empty.

## Content

- [X] CT-01: Each task card displays relevant core information
  - Action: View the board with default tasks.
  - Expected: Every card shows the task title, assignee, and due date (when set).
  - Note: All 8 default cards display title, assignee (name), and a due date.

- [X] CT-02: Board columns are labeled with distinct, meaningful statuses
  - Action: Open the Kanban board.
  - Expected: Columns are clearly labeled (e.g., To Do, In Progress, Done) representing workflow statuses.
  - Note: Four columns labeled To Do, In Progress, Review, Done.

- [X] CT-03: Assignee filter lists only actual team members
  - Action: Open the assignee filter/selector.
  - Expected: The list contains only the real teammates available in the application, with correct names.
  - Note: Filter buttons list Alex Chen, Sarah Kim, Marcus Johnson, Emma Wilson — the 4 real members (matching initials AC/SK/MJ/EW).
