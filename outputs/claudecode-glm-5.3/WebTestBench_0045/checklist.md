# Test Checklist

## Functionality

- [ ] FT-01: Add a new task with title, optional description, deadline, and priority
  - Action: Click "Add Task", enter title "Prepare slides", leave description blank, set a deadline date and priority "High", then save.
  - Expected: Task "Prepare slides" appears in the list showing its deadline and "High" priority; no error is raised for the empty description.

- [ ] FT-02: Edit an existing task's details
  - Action: On a default task, click "Edit", change its title, description, and deadline, then save.
  - Expected: The list shows the task with the updated title, description, and deadline.

- [ ] FT-03: Mark a task as completed without losing it
  - Action: Click the "Complete" button (or checkbox) on an active default task.
  - Expected: The task displays a completed state (e.g., checkmark/strikethrough) and remains visible in the list.

- [ ] FT-04: Delete a task
  - Action: Click the "Delete" button on a default task and confirm the deletion.
  - Expected: The task is removed from the list and no longer appears anywhere on the page.

- [ ] FT-05: Assign a priority to a task
  - Action: While adding or editing a task, select a priority level (e.g., "Medium") and save.
  - Expected: The chosen priority is stored and displayed on the task card.

- [ ] FT-06: Sort the task list by priority
  - Action: Select the "Sort by Priority" option.
  - Expected: Tasks are re-ordered by priority level (e.g., High before Medium, Medium before Low).

- [ ] FT-07: Sort the task list by deadline
  - Action: Select the "Sort by Deadline" option.
  - Expected: Tasks are re-ordered chronologically by deadline date (earliest first).

- [ ] FT-08: View active tasks before completed tasks
  - Action: With default active and completed tasks in the list, open the main list view (use the active-first view/filter if provided).
  - Expected: All active tasks appear above the completed tasks.

- [ ] FT-09: Bind one or more prerequisite tasks to a task
  - Action: On Task A, use the "Add Prerequisite" (dependency) option and bind two incomplete tasks, B and C, as prerequisites; save.
  - Expected: Task A is linked to both B and C; the dependency is persisted and reflected on Task A (e.g., prerequisite list/connections shown).

- [ ] FT-10: Completing a prerequisite unlocks the dependent task
  - Action: With Task A dependent on incomplete Task B, mark Task B as completed.
  - Expected: Task A's "Edit" and "Complete" buttons become enabled (no longer grayed out) and Task A can be completed.

## Constraint

- [ ] CS-01: Cannot save a task with an empty title
  - Action: Open the add-task form, leave the title empty, fill in other fields, and attempt to save.
  - Expected: The task is not created; a validation message indicates the title is required.

- [ ] CS-02: Edit and Complete buttons grayed out while a prerequisite is incomplete
  - Action: View Task A that is bound to incomplete prerequisite Task B (from FT-09).
  - Expected: Task A's "Edit" and "Complete" buttons render grayed out/disabled, and clicking them does not open the normal edit dialog or mark the task complete.

- [ ] CS-03: Only description and priority are modifiable on a locked dependent task
  - Action: While Task A is locked by incomplete Task B, attempt to change Task A's description and priority, then attempt to change its title and deadline.
  - Expected: Description and priority changes can be made and saved; title and deadline fields are disabled and cannot be modified or saved.

## Interaction

- [ ] IX-01: Prominent "Prerequisite … Incomplete" label next to the dependent task
  - Action: View Task A that depends on incomplete Task B.
  - Expected: A prominent label (badge/highlighted text) reading "Prerequisite Task B Incomplete" is displayed next to Task A.

- [ ] IX-02: Dashed lines visually connect dependent tasks
  - Action: Observe the task display area where a dependency pair (Task A → Task B) exists.
  - Expected: A dashed line visually connects prerequisite Task B to its dependent Task A (line style is dashed, not solid).

- [ ] IX-03: Hovering over the connection opens a dependency-chain pop-up
  - Action: Hover the mouse pointer over the dashed line between Task A and Task B.
  - Expected: A pop-up window appears showing the details of the dependency chain (relationship and task info); it dismisses when the pointer moves away.

## Content

- [ ] CT-01: Prerequisite label names the correct bound task
  - Action: Compare the label next to dependent Task A with the actual title of its bound prerequisite(s), Task B (and C).
  - Expected: The label text exactly reflects the bound prerequisite task's title (e.g., "Prerequisite <Task B title> Incomplete") and covers all prerequisites when several are bound.

- [ ] CT-02: Hover pop-up shows accurate dependency chain details
  - Action: Hover over the dashed connection in a multi-level chain (e.g., Task C depends on B, B depends on A).
  - Expected: The pop-up lists each link of the chain with correct task titles and completion statuses matching the current task list data.