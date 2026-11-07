# Test Checklist

## Functionality
- [ ] FT-01: Kanban board loads with default tasks distributed across status columns
  - Action: Open the board page and observe the columns and cards.
  - Expected: At least 3 status columns (e.g., To Do / In Progress / Done) are visible, each containing at least one pre-existing task card. No column is empty due to missing default data.

- [ ] FT-02: User can create a new task with a title
  - Action: Click the "Add Task" / "New Task" button, enter title "QA Test Task 1", and submit the form.
  - Expected: A new card titled "QA Test Task 1" appears on the board (in the first/backlog column) and the form closes.

- [ ] FT-03: User can assign a task to a teammate
  - Action: Open the task created in FT-02 (or any default task), select an existing teammate name from the "Assignee" dropdown, and save.
  - Expected: The chosen teammate's name is shown on the task card and in the task detail view.

- [ ] FT-04: User can set a due date on a task
  - Action: In the same task's edit/detail form, set a due date (e.g., tomorrow's date) and save.
  - Expected: The due date is displayed on the task card and in the detail view in a readable date format.

- [ ] FT-05: User can change a task's status by moving it between columns
  - Action: Drag the card from the "To Do" column and drop it into the "In Progress" column.
  - Expected: The card is removed from "To Do", appears in "In Progress", and moving it again to "Done" also succeeds.

- [ ] FT-06: User can open a task to view its details
  - Action: Click once on any default task card.
  - Expected: A detail panel/modal opens showing that task's title, description, assignee, due date, and current status.

- [ ] FT-07: User can edit a task's information
  - Action: In the detail view, click "Edit", change the title to "QA Test Task 1 - Edited", and save.
  - Expected: The updated title appears immediately on the card and persists after closing and reopening the detail view.

- [ ] FT-08: User can add a short note / status update to a task
  - Action: In a task's detail view, type "Blocked on design review" into the note/comment field and submit.
  - Expected: The note appears in the task's activity/notes list with its text visible, and remains after reopening the detail view.

- [ ] FT-09: User can filter the board by assignee
  - Action: Select a teammate from the "Filter by assignee" control.
  - Expected: Only tasks assigned to that teammate are displayed; all other tasks are hidden or clearly de-emphasized across all columns.

- [ ] FT-10: User can filter / highlight the board by status
  - Action: Select a single status option from the "Filter by status" control (e.g., "In Progress").
  - Expected: Only "In Progress" tasks remain visible/highlighted; tasks in other statuses are filtered out or visually dimmed.

## Constraint
- [ ] CS-01: Task cannot be created with an empty title
  - Action: Open the "New Task" form, leave the title field blank, and click submit.
  - Expected: Submission is blocked; a validation message such as "Title is required" appears and no empty/unnamed card is added to the board.

- [ ] CS-02: Assignee selection is limited to existing teammates
  - Action: Open the assignee control for any task and inspect the available options.
  - Expected: Only real teammate names appear as selectable options; there is no way to save a free-text/blank assignee value.

- [ ] CS-03: Empty note cannot be submitted
  - Action: In a task detail view, leave the note field blank and click the add/submit note button.
  - Expected: The button is disabled or a validation prevents submission; no blank entry is added to the notes list.

- [ ] CS-04: Task data is preserved when its status changes
  - Action: Note the assignee and due date of a card, drag it to a different column, then open the card.
  - Expected: The assignee, due date, title, and notes are all unchanged; only the status/column has changed.

- [ ] CS-05: A filter with no matching tasks shows an empty state
  - Action: Choose an assignee filter for a teammate who has no tasks assigned.
  - Expected: No task cards are shown and an empty message (e.g., "No tasks found") is displayed rather than a broken/blank board.

## Interaction
- [ ] IX-01: Task card shows a draggable/pointer state on hover
  - Action: Hover the mouse over any task card.
  - Expected: The card visibly responds (cursor changes to pointer/grab, and/or border/background highlight appears).

- [ ] IX-02: A confirmation/success feedback appears after a task is created
  - Action: Complete a valid new-task creation (from FT-02).
  - Expected: A brief success toast or inline confirmation message (e.g., "Task created") appears and then disappears without manual dismissal.

- [ ] IX-03: Clearing a filter restores the full board
  - Action: Apply an assignee filter, then select the "All"/"Clear" option to remove it.
  - Expected: All previously hidden task cards become visible again in their original columns, with their original order preserved.

- [ ] IX-04: Task detail view can be closed without changing the task
  - Action: Open a task detail view, make no changes, and close it via the "X"/"Close" button or the Esc key.
  - Expected: The detail view closes and the task card on the board is unchanged.

## Content
- [ ] CT-01: Task cards display the required task information
  - Action: Inspect 3 default task cards on the board.
  - Expected: Each card shows its title, assignee name (or avatar), due date, and a visual status indicator — none of these fields are blank on cards that have data.

- [ ] CT-02: Column headers are labeled with their status and show a task count
  - Action: Read the header of each board column.
  - Expected: Each header clearly names a status (e.g., "To Do", "In Progress", "Done") and displays a number matching the actual count of cards in that column.