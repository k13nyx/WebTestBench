# Test Checklist

## Functionality

- [ ] FT-01: Board displays default tasks organized across status columns
  - Action: Open the Kanban board page.
  - Expected: Pre-existing tasks are visible, each placed in exactly one status column (e.g., To Do / In Progress / Done), with column headers shown.

- [ ] FT-02: User can create a new task with title, assignee, and due date
  - Action: Click the "Add Task" / "New Task" button, fill in a title, select a teammate as assignee, pick a due date, and save.
  - Expected: The new task is created and appears on the board in the initial column, showing its title, assignee, and due date on the card.

- [ ] FT-03: User can open a task to view its details
  - Action: Click a default task card on the board.
  - Expected: A detail view opens showing the task's full information: title, description, assignee, due date, current status, and any existing notes/status updates.

- [ ] FT-04: User can edit a task's information
  - Action: Open a default task, change its title and due date via the edit controls, and save.
  - Expected: The changes are saved; the detail view and the board card reflect the updated title and due date.

- [ ] FT-05: User can update a task's status by moving it between columns
  - Action: Drag (or use the move control on) a default task card from its current column to another column (e.g., To Do → In Progress).
  - Expected: The task appears in the destination column and its status is updated accordingly in the task detail view.

- [ ] FT-06: User can add a status update / short note to a task
  - Action: Open a default task, type a short note (e.g., "Started working on this") into the notes/status update field, and submit it.
  - Expected: The note is added and displayed in the task's detail view with its content (and timestamp/author if provided).

- [ ] FT-07: User can filter the board by assignee
  - Action: Select a specific teammate from the assignee filter control.
  - Expected: Only tasks assigned to that teammate are shown (or clearly highlighted) on the board; other tasks are hidden or de-emphasized.

- [ ] FT-08: User can filter or highlight tasks by status
  - Action: Apply a status filter/highlight for one specific column/status (e.g., "In Progress").
  - Expected: Only tasks in that status are shown (or clearly highlighted), while tasks in other statuses are hidden or de-emphasized.

- [ ] FT-09: Clearing filters restores the full board view
  - Action: With an assignee or status filter active, clear/reset the filter control.
  - Expected: All default tasks are visible again in their correct columns, matching the unfiltered board.

## Constraint

- [ ] CS-01: Cannot create a task without a title
  - Action: Open the task creation form, leave the title empty (assignee and due date optional or filled), and attempt to save.
  - Expected: The task is not created; a validation message indicating the title is required is shown, and no empty card appears on the board.

- [ ] CS-02: Cannot save task edits that empty a required field
  - Action: Open a default task in edit mode, clear its title, and attempt to save.
  - Expected: The edit is rejected with a required-field validation message; the task retains its previous title.

- [ ] CS-03: Task must be assigned to a teammate from the available team list
  - Action: Open the assignee selector in the create or edit form and inspect the options; attempt to enter a name not on the team.
  - Expected: Only predefined teammates are selectable/valid; a free-text or unknown assignee cannot be saved.

- [ ] CS-04: Due date must be a valid date
  - Action: Interact with the due date field in the task form and attempt to enter an invalid or empty date format where a date is required.
  - Expected: An invalid date cannot be saved; a validation message or the date picker's restrictions prevent it.

- [ ] CS-05: A task exists in only one column at a time
  - Action: Move a default task from one column to another, then inspect both the source and destination columns.
  - Expected: The task appears only in the destination column and is removed from the source column; it is not duplicated across columns.

## Interaction

- [ ] IX-01: New task appears on the board immediately after creation
  - Action: Create a task with valid details and save it.
  - Expected: The task card appears on the board without requiring a manual page reload, and the creation form closes (or resets).

- [ ] IX-02: Visual feedback is shown while moving a task between columns
  - Action: Begin dragging a task card (or hover/activate its move control) toward another column.
  - Expected: The card follows the pointer or the target column is visually indicated (e.g., highlighted drop zone), confirming the move is registering.

- [ ] IX-03: Newly added note appears immediately in the task detail view
  - Action: Submit a note/status update on an open task.
  - Expected: The note is appended to the task's update/note list right away, with the input field cleared, and no page reload needed.

- [ ] IX-04: Highlighted tasks are visually distinguished when using highlight mode
  - Action: Apply an assignee or status highlight (if highlight is offered instead of/in addition to filtering).
  - Expected: Matching tasks are visually emphasized (e.g., colored border, glow, or dimmed non-matching tasks) so the user can instantly spot them.

- [ ] IX-05: Closing the task detail view returns to the board
  - Action: Open a task's detail view, then click the close/"X"/back control.
  - Expected: The detail view closes and the board is displayed with its current state (including any filters still applied).

## Content

- [ ] CT-01: Task cards display relevant key information
  - Action: Inspect the default task cards on the board.
  - Expected: Each card clearly shows its title, assignee (name/avatar), and due date; no card shows placeholder text, broken images, or unrelated data.

- [ ] CT-02: Column headers reflect task statuses and tasks are correctly categorized
  - Action: Compare each default task's status in its detail view with the column it sits in.
  - Expected: Column headers are meaningful status names (e.g., To Do, In Progress, Done) and every task's column matches its status; no task is in an unlabeled or mismatched column.

- [ ] CT-03: Assignee options consist of actual team members
  - Action: Open the assignee filter and the assignee selector in the task form.
  - Expected: Both lists contain the same set of teammate names matching those used on existing task cards; no duplicate, empty, or non-teammate entries appear.