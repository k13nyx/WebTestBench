# Test Checklist

## Functionality
- [ ] FT-01: Create a new task with an assignee and due date
  - Action: Click the "Add Task" button, enter a task title, select a teammate from the assignee dropdown, pick a date from the due date picker, and click "Save".
  - Expected: A new task card appears in the initial column displaying the title, assigned teammate, and due date.
- [ ] FT-02: Move a task between columns to update status
  - Action: Drag a default task card from the "To Do" column and drop it into the "In Progress" column.
  - Expected: The task card moves to the "In Progress" column and its status updates accordingly.
- [ ] FT-03: Edit task information
  - Action: Open a default task, change its title and due date in the edit form, and click "Save Changes".
  - Expected: The updated title and due date are saved and reflected on the task card on the board.
- [ ] FT-04: Add a status update or short note to a task
  - Action: Open a default task's detail view, type "Completed initial draft" into the note input field, and click "Add Note".
  - Expected: The note is added and displayed in the task's notes list with the entered text.
- [ ] FT-05: Filter tasks by assignee
  - Action: Select a specific teammate from the assignee filter dropdown.
  - Expected: Only task cards assigned to the selected teammate are displayed on the board; all other cards are hidden.
- [ ] FT-06: Filter tasks by status
  - Action: Select a status (e.g., "In Progress") from the status filter control.
  - Expected: Only tasks matching the selected status remain visible on the board.

## Constraint
- [ ] CS-01: Prevent task creation with an empty title
  - Action: Click "Add Task", leave the title field empty while selecting an assignee and due date, and click "Save".
  - Expected: Task creation is blocked, and an inline error message indicates the title is required.
- [ ] CS-02: Prevent adding an empty note
  - Action: Open a task's details view, leave the note input field empty, and click the "Add Note" button.
  - Expected: No note is added to the notes list, and the input shows a validation warning or the button remains disabled.
- [ ] CS-03: Reset filters restores all tasks
  - Action: Apply an assignee or status filter, then click the "Reset Filters" or "All" option.
  - Expected: All tasks across all assignees and statuses reappear on the board.

## Interaction
- [ ] IX-01: Open task details modal on card click
  - Action: Click on any default task card on the Kanban board.
  - Expected: A task detail modal or slide-over panel opens showing the task's full information and notes section.
- [ ] IX-02: Close task details view
  - Action: Click the "Close" (X) button on an open task detail modal.
  - Expected: The detail modal closes, returning focus to the Kanban board.
- [ ] IX-03: Drag feedback during card movement
  - Action: Click and drag a task card over an adjacent column.
  - Expected: The dragged card shows an elevated or semi-transparent dragging state, and the target column highlights as a drop zone.
- [ ] IX-04: Active visual state for applied filter
  - Action: Click on an assignee or status filter option.
  - Expected: The selected filter item visibly indicates its active state through distinct highlighting, a badge, or a checkmark.

## Content
- [ ] CT-01: Kanban board columns display distinct status headers
  - Action: View the main Kanban board layout.
  - Expected: Columns display clear, sequential workflow headers (e.g., "To Do", "In Progress", "Done").
- [ ] CT-02: Task card displays essential metadata
  - Action: Inspect any default task card on the board.
  - Expected: The card clearly displays the task title, assigned teammate's name or avatar, and the due date.
- [ ] CT-03: Task detail view displays comprehensive task data
  - Action: Open the detail view of a default task.
  - Expected: The view displays the task's title, full description, current status, assigned teammate, due date, and note history.