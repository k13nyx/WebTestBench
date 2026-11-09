# Test Checklist

## Functionality
- [ ] FT-01: Create a new task with title, assignee, and due date.
  - Action: Click "Add Task" (or "+" in a column), enter a title, select a teammate, pick a due date, then click "Save".
  - Expected: New task card appears in the target column showing the title, assignee, and due date.

- [ ] FT-02: Assign a task to a specific teammate.
  - Action: In the task form or detail view, select a teammate from the "Assignee" dropdown.
  - Expected: The selected teammate's name is saved and displayed on the task card.

- [ ] FT-03: Set/change a due date on a task.
  - Action: In the task form or detail view, set the "Due Date" field to a date and save.
  - Expected: The chosen due date is saved and displayed on the task card and detail view.

- [ ] FT-04: Update task status by moving it between columns.
  - Action: Drag a task card from one column to another (e.g., "To Do" → "In Progress").
  - Expected: Task card moves to the new column and its status reflects the new column after reload.

- [ ] FT-05: Open a task to view its details.
  - Action: Click on an existing task card.
  - Expected: A detail view opens showing the task's title, assignee, due date, status, and notes.

- [ ] FT-06: Edit an existing task's information.
  - Action: Open a task, change its title/assignee/due date, then click "Save".
  - Expected: Changes are saved and the task card plus detail view show the updated values.

- [ ] FT-07: Add a short status update or note to a task.
  - Action: Open a task, type text in the "Add note"/"Status update" field, and submit.
  - Expected: The note is appended to the task's notes/activity list with a timestamp.

- [ ] FT-08: Filter tasks by assignee.
  - Action: Use the "Assignee" filter and select a teammate.
  - Expected: Only tasks assigned to that teammate are shown on the board.

- [ ] FT-09: Filter tasks by status.
  - Action: Use the "Status" filter and select a column/status.
  - Expected: Only tasks with that status are shown; other columns are hidden or emptied.

## Constraint
- [ ] CS-01: Prevent creating a task without a title.
  - Action: Click "Save" on the task form with the title field left empty.
  - Expected: Save is blocked and a required-field message appears on the title field.

- [ ] CS-02: Restrict assignee selection to existing teammates.
  - Action: Open the "Assignee" dropdown and inspect available options.
  - Expected: Only pre-existing teammates are listed; no free-text arbitrary names can be saved.

- [ ] CS-03: Prevent saving an empty note/status update.
  - Action: Submit the note field while it is empty or whitespace-only.
  - Expected: Submission is blocked; no blank note entry is added to the task.

- [ ] CS-04: Ensure a task exists in exactly one status column at a time.
  - Action: Move a task between columns, then reload the board.
  - Expected: The task appears only in its new column and has a single current status (no duplicate cards).

## Interaction
- [ ] IX-01: Drag-and-drop provides visual feedback during a move.
  - Action: Begin dragging a task card and hover over another column.
  - Expected: The dragged card shows a drag state and the target column shows a drop/insertion highlight.

- [ ] IX-02: Highlight tasks belonging to the current user or a chosen assignee.
  - Action: Activate the assignee highlight (e.g., hover/select a teammate).
  - Expected: That teammate's task cards are visually emphasized (e.g., border/color) distinct from others.

- [ ] IX-03: Confirm task creation/edits with feedback.
  - Action: Save a newly created or edited task.
  - Expected: A success toast/message appears (e.g., "Task saved") and dismisses automatically.

- [ ] IX-04: Filters update results immediately without reload.
  - Action: Change the assignee or status filter.
  - Expected: The board re-renders instantly to the filtered set with no page reload.

## Content
- [ ] CT-01: Board columns use clear, task-status labels.
  - Action: Inspect the board column headers.
  - Expected: Columns are labeled with task statuses (e.g., "To Do", "In Progress", "Done") consistent with the workflow.

- [ ] CT-02: Task cards display key metadata.
  - Action: Inspect any task card on the board.
  - Expected: Each card shows its title, assignee, and due date.

- [ ] CT-03: All displayed content is relevant to team task management.
  - Action: Review text, labels, and any icons/media across the board.
  - Expected: Every element relates to tasks, teammates, due dates, or status — no unrelated/placeholder content.