# Test Result

## Functionality

- [X] FT-01: Create a new task with its required information.
  - Action: Select **Create task**, enter a task title, choose an assignee, set a due date, select an initial status, and save.
  - Expected: The new task appears as a card in the selected status column with the entered information.

- [X] FT-02: Assign a task to a specific teammate.
  - Action: Open a task and select a teammate from the **Assignee** control, then save.
  - Expected: The selected teammate is displayed as the task’s assignee on the card and task details.

- [X] FT-03: Set and retain a task due date.
  - Action: Open a task, choose a due date, save, and reopen the task.
  - Expected: The selected due date is displayed both on the task card and in the task details.

- [X] FT-04: Move a task between Kanban status columns.
  - Action: Drag an existing task card from its current column to another status column.
  - Expected: The task appears in the destination column and its displayed status matches that column.

- [X] FT-05: Open a task to view its details.
  - Action: Select an existing task card.
  - Expected: A task detail view opens and displays the task’s title, assignee, due date, status, and available notes or updates.

- [X] FT-06: Edit existing task information.
  - Action: Open a task, change its title, assignee, due date, or status, and save the changes.
  - Expected: The updated values appear in the task detail view and on the corresponding board card.

- [X] FT-07: Add a status update or short note to a task.
  - Action: Open a task, enter text in the available status update or note control, and save it.
  - Expected: The submitted update or note is displayed in the task’s details after saving and reopening it.

- [X] FT-08: Filter or highlight tasks by assignee.
  - Action: Select a specific teammate in the assignee filter or highlight control.
  - Expected: Tasks assigned to that teammate are the only tasks shown or are visibly highlighted.

- [X] FT-09: Filter or highlight tasks by status.
  - Action: Select a status in the status filter or highlight control.
  - Expected: Tasks with the selected status are the only tasks shown or are visibly highlighted.

## Constraint

- [X] CS-01: A task exists in only one status column at a time.
  - Action: Move an existing task from one status column to another and inspect the board.
  - Expected: The task is removed from its previous column and appears only in the destination column.

- [X] CS-02: Filtering does not modify task information.
  - Action: Apply an assignee or status filter, open a visible task, clear the filter, and inspect the task again.
  - Expected: The task’s title, assignee, due date, status, and notes remain unchanged.

- [X] CS-03: Changes to one task do not alter other tasks.
  - Action: Edit the assignee, due date, or status of one existing task, then inspect another task.
  - Expected: The other task retains all of its original information.

## Interaction

- [X] IX-01: The task detail view opens and closes without losing board context.
  - Action: Open an existing task, close the detail view, and inspect the board.
  - Expected: The detail view closes and the board remains visible with the same task cards and columns.

- [ ] IX-02: Dragging a task provides clear placement feedback.
  - Action: Begin dragging an existing task card over another status column.
  - Expected: The valid destination column visibly indicates where the task can be dropped, and dropping completes the move.
  - Bug Report:
    - Issue: Missing drag-and-drop placement feedback
    - Actual: The task moved successfully to the destination column, but no visible indication of the valid drop target was observed while dragging.

- [X] IX-03: Clearing filters restores the complete board.
  - Action: Apply an assignee or status filter, then use the available clear or reset filter control.
  - Expected: All previously visible task cards are restored and no filter remains active.

- [ ] IX-04: Successful task changes produce visible confirmation.
  - Action: Save a task creation, edit, or note update.
  - Expected: The interface visibly confirms that the change was saved, and the updated data is immediately displayed.
  - Bug Report:
    - Issue: Missing save confirmation
    - Actual: Task creation, task edits, and note updates were reflected in the board or task details, but no visible saved confirmation or notification appeared in the notification region.

## Content

- [X] CT-01: Task cards present essential task information accurately.
  - Action: Inspect several existing task cards across the Kanban columns.
  - Expected: Each card displays the correct task title, current status or column, assignee when set, and due date when set.

- [X] CT-02: Task details contain relevant and consistent information.
  - Action: Open several existing tasks and compare their detail views with their board cards.
  - Expected: Each detail view contains information relevant to that task, and its title, assignee, due date, status, and notes match the corresponding card and saved data.