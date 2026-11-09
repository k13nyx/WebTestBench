All test data is collected. Here is the complete test report:

# Test Result

## Functionality
- [ ] FT-01: Create a new task on the Kanban board.
  - Action: Click "Add Task", fill in Title, select an Assignee from the default teammate list, set a Due Date, click "Save".
  - Expected: A new task card with the entered title appears in the default (first) column and persists after reload.
  - Bug Report:
    - Issue: Missing Data Persistence – Created Task Lost on Reload
    - Actual: The new card "QA Test Task" appears immediately in the first column ("To Do") with the entered data, but after reloading the page the board resets to the original 8 seed tasks and the created task disappears (reproduced on two separate creations).

- [X] FT-02: Assign a task to a specific teammate.
  - Action: Open the Assignee dropdown on the create/edit form and select one teammate from the default teammate list.
  - Expected: The task card displays the selected teammate's name as assignee.

- [X] FT-03: Set a due date on a task.
  - Action: Set a due date (today or later) in the Due Date field and save.
  - Expected: The due date is shown on the task card and in the task detail view, matching the entered date.

- [ ] FT-04: Update task status by moving it between columns.
  - Action: Drag a pre-existing task card from its current column and drop it into a different column (e.g., from "To Do" to "In Progress").
  - Expected: The card appears in the target column, its status field reads the target column's status, and the change persists after reload.
  - Bug Report:
    - Issue: Missing Data Persistence – Column Move Lost on Reload
    - Actual: Dragging "Create component library docs" from "To Do" to "In Progress" works in-session (card appears in "In Progress", its detail Status reads "In Progress"), but after reload the card is back in "To Do" with status "To Do"; the move is not persisted.

- [X] FT-05: Open a task to see more details.
  - Action: Click a pre-existing task card on the board.
  - Expected: A detail view opens showing the task's title, description, assignee, due date, status, and notes/status updates.

- [ ] FT-06: Edit task information.
  - Action: In the detail view, click "Edit", change the title and assignee, click "Save".
  - Expected: The detail view and the task card both show the updated title and assignee; the change persists after reload.
  - Bug Report:
    - Issue: Stale Detail View After Save + Missing Data Persistence
    - Actual: After saving an edited title ("Design new dashboard layout EDITED") and assignee ("Marcus Johnson"), the board card updates correctly, but the open detail view still displays the old title "Design new dashboard layout" and assignee "Sarah Kim" (reproduced twice); after reload both title and assignee revert to the original values.

- [ ] FT-07: Add a status update / short note to a task.
  - Action: Open a task's detail view, type a short note in the note field, click "Add Note".
  - Expected: The note appears in the task's notes list in the detail view, most recent first.
  - Bug Report:
    - Issue: Non-functional "Add Note" Button (Unresponsive Note Submission)
    - Actual: Typing a note (e.g., "QA note one") and clicking the add-note button clears the input, but the note never appears and the "Notes & Updates (N)" count stays unchanged (reproduced on both newly created and pre-existing tasks, via button click and via Enter key).

- [X] FT-08: Filter or highlight tasks by assignee.
  - Action: Select one teammate in the "Assignee" filter on the board toolbar.
  - Expected: Only tasks assigned to that teammate are shown (or highlighted while others are dimmed); each visible card lists that teammate as assignee.

- [X] FT-09: Filter or highlight tasks by status.
  - Action: Select one status (e.g., "In Progress") in the "Status" filter on the board toolbar.
  - Expected: Only tasks with that status are shown (or highlighted while others are dimmed); clearing the filter restores all tasks to full visibility.

## Constraint
- [ ] CS-01: Task cannot be saved without a title.
  - Action: Click "Add Task", leave Title empty, fill assignee and due date, click "Save".
  - Expected: Save is blocked with an error message next to the Title field (e.g., "Title is required"); no task card is created.
  - Bug Report:
    - Issue: Missing Validation Error Message (Disabled Save Button Without Feedback)
    - Actual: With Title empty the "Create Task" button is disabled — "Save" cannot be clicked at all and no error message (e.g., "Title is required") ever appears next to the Title field (only a static "Title *" label marker); save is prevented and no card is created, but the expected validation message is missing.

- [ ] CS-02: Task cannot be saved without a valid teammate as assignee.
  - Action: Click "Add Task", enter a title, leave the Assignee dropdown unselected, click "Save".
  - Expected: Save is blocked with an error message on the Assignee field; the Assignee dropdown only offers teammates from the default teammate list, with no free-text entry.
  - Bug Report:
    - Issue: Incorrect Form Submission – Missing Assignee Validation
    - Actual: With Assignee left "Unassigned" and Title filled, the "Create Task" button is enabled and Save succeeds — a task card is created (board count 8→9) with no error message on the Assignee field. (The dropdown is a select with no free-text entry, listing "Unassigned" plus the 4 teammates.)

- [ ] CS-03: Due date cannot be set in the past.
  - Action: In the task form, enter a due date earlier than today and click "Save".
  - Expected: Save is blocked with an error on the Due Date field (e.g., "Due date cannot be in the past"); the task is not created/updated.
  - Bug Report:
    - Issue: Incorrect Form Submission – Past Due Date Accepted
    - Actual: Entering 2026-01-01 (earlier than today, 2026-11-08) and clicking Save creates the task (board count 9→10) with no error on the Due Date field (no min restriction on the date input); the new card even displays "Jan 1" as its due date.

- [ ] CS-04: Empty or overlong notes cannot be added.
  - Action: Open a task's detail view, click "Add Note" with an empty note field; then enter a note longer than 200 characters and click "Add Note".
  - Expected: Both attempts are rejected with a validation message; the notes list is unchanged.
  - Bug Report:
    - Issue: Missing Validation Messages for Notes (Silent Rejection)
    - Actual: With an empty note the add button is simply disabled with no validation message; a 250-character note is accepted into the input (no maxlength is enforced) and silently ignored with no validation message. The notes list stays unchanged in both cases, but no rejection message is ever shown — and note submission is non-functional overall (see FT-07).

## Interaction
- [X] IX-01: Moving a task card provides drag-and-drop feedback without reloading.
  - Action: Drag a task card toward another column and release it inside that column.
  - Expected: While dragging, the card visibly follows the pointer (lifted/moved); on drop it settles into the target column immediately with no page reload.

- [X] IX-02: Task cards show a clickable affordance on hover.
  - Action: Hover the mouse over a task card on the board.
  - Expected: The cursor changes to a pointer and the card shows a hover highlight, indicating it can be opened.

- [X] IX-03: Closing the detail view without saving discards edits.
  - Action: Open a task, click "Edit", change the title, then click "Cancel" (or the close icon).
  - Expected: The detail view closes and the task card still shows the original title; no change is saved.

- [ ] IX-04: The system confirms successful task actions.
  - Action: Create a task, then edit it, then add a note to it.
  - Expected: After each completed action a success message (e.g., toast "Task created / Task updated / Note added") appears briefly and then dismisses.
  - Bug Report:
    - Issue: Missing Success Feedback (No Toast/Confirmation Messages)
    - Actual: No success message appears after any action — after task creation (checked at ~150 ms, 900 ms, 3 s), after saving an edit, and after note attempts, the notifications region and page text contain no toast or confirmation element at all.

## Content
- [X] CT-01: Columns are labeled by status and tasks are grouped accordingly.
  - Action: View the board on load and compare each card's status in its detail view with its column.
  - Expected: Columns show status names (e.g., "To Do", "In Progress", "Done") and every card in a column has exactly that status.

- [X] CT-02: Task cards show the core task information.
  - Action: Inspect any pre-existing task card on the board.
  - Expected: Each card displays its title, assignee name, and due date (with a date or calendar label) that match the values in its detail view.

- [X] CT-03: Default data is present on load.
  - Action: Open the board page and the Assignee filter / task form's Assignee dropdown.
  - Expected: The board shows pre-existing tasks across columns, and the assignee selections list the same default teammates that appear on those tasks.