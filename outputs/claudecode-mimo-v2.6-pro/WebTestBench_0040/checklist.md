# Test Checklist

## Functionality
- [ ] FT-01: Create a new task on the Kanban board.
  - Action: Click "Add Task", fill in Title, select an Assignee from the default teammate list, set a Due Date, click "Save".
  - Expected: A new task card with the entered title appears in the default (first) column and persists after reload.

- [ ] FT-02: Assign a task to a specific teammate.
  - Action: Open the Assignee dropdown on the create/edit form and select one teammate from the default teammate list.
  - Expected: The task card displays the selected teammate's name as assignee.

- [ ] FT-03: Set a due date on a task.
  - Action: Set a due date (today or later) in the Due Date field and save.
  - Expected: The due date is shown on the task card and in the task detail view, matching the entered date.

- [ ] FT-04: Update task status by moving it between columns.
  - Action: Drag a pre-existing task card from its current column and drop it into a different column (e.g., from "To Do" to "In Progress").
  - Expected: The card appears in the target column, its status field reads the target column's status, and the change persists after reload.

- [ ] FT-05: Open a task to see more details.
  - Action: Click a pre-existing task card on the board.
  - Expected: A detail view opens showing the task's title, description, assignee, due date, status, and notes/status updates.

- [ ] FT-06: Edit task information.
  - Action: In the detail view, click "Edit", change the title and assignee, click "Save".
  - Expected: The detail view and the task card both show the updated title and assignee; the change persists after reload.

- [ ] FT-07: Add a status update / short note to a task.
  - Action: Open a task's detail view, type a short note in the note field, click "Add Note".
  - Expected: The note appears in the task's notes list in the detail view, most recent first.

- [ ] FT-08: Filter or highlight tasks by assignee.
  - Action: Select one teammate in the "Assignee" filter on the board toolbar.
  - Expected: Only tasks assigned to that teammate are shown (or highlighted while others are dimmed); each visible card lists that teammate as assignee.

- [ ] FT-09: Filter or highlight tasks by status.
  - Action: Select one status (e.g., "In Progress") in the "Status" filter on the board toolbar.
  - Expected: Only tasks with that status are shown (or highlighted while others are dimmed); clearing the filter restores all tasks to full visibility.

## Constraint
- [ ] CS-01: Task cannot be saved without a title.
  - Action: Click "Add Task", leave Title empty, fill assignee and due date, click "Save".
  - Expected: Save is blocked with an error message next to the Title field (e.g., "Title is required"); no task card is created.

- [ ] CS-02: Task cannot be saved without a valid teammate as assignee.
  - Action: Click "Add Task", enter a title, leave the Assignee dropdown unselected, click "Save".
  - Expected: Save is blocked with an error message on the Assignee field; the Assignee dropdown only offers teammates from the default teammate list, with no free-text entry.

- [ ] CS-03: Due date cannot be set in the past.
  - Action: In the task form, enter a due date earlier than today and click "Save".
  - Expected: Save is blocked with an error on the Due Date field (e.g., "Due date cannot be in the past"); the task is not created/updated.

- [ ] CS-04: Empty or overlong notes cannot be added.
  - Action: Open a task's detail view, click "Add Note" with an empty note field; then enter a note longer than 200 characters and click "Add Note".
  - Expected: Both attempts are rejected with a validation message; the notes list is unchanged.

## Interaction
- [ ] IX-01: Moving a task card provides drag-and-drop feedback without reloading.
  - Action: Drag a task card toward another column and release it inside that column.
  - Expected: While dragging, the card visibly follows the pointer (lifted/moved); on drop it settles into the target column immediately with no page reload.

- [ ] IX-02: Task cards show a clickable affordance on hover.
  - Action: Hover the mouse over a task card on the board.
  - Expected: The cursor changes to a pointer and the card shows a hover highlight, indicating it can be opened.

- [ ] IX-03: Closing the detail view without saving discards edits.
  - Action: Open a task, click "Edit", change the title, then click "Cancel" (or the close icon).
  - Expected: The detail view closes and the task card still shows the original title; no change is saved.

- [ ] IX-04: The system confirms successful task actions.
  - Action: Create a task, then edit it, then add a note to it.
  - Expected: After each completed action a success message (e.g., toast "Task created / Task updated / Note added") appears briefly and then dismisses.

## Content
- [ ] CT-01: Columns are labeled by status and tasks are grouped accordingly.
  - Action: View the board on load and compare each card's status in its detail view with its column.
  - Expected: Columns show status names (e.g., "To Do", "In Progress", "Done") and every card in a column has exactly that status.

- [ ] CT-02: Task cards show the core task information.
  - Action: Inspect any pre-existing task card on the board.
  - Expected: Each card displays its title, assignee name, and due date (with a date or calendar label) that match the values in its detail view.

- [ ] CT-03: Default data is present on load.
  - Action: Open the board page and the Assignee filter / task form's Assignee dropdown.
  - Expected: The board shows pre-existing tasks across columns, and the assignee selections list the same default teammates that appear on those tasks.