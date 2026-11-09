# Test Checklist

## Functionality
- [ ] FT-01: Adding a task with title, description, and deadline creates a visible task in the list.
  - Action: In the add-task form, fill the title, description, and deadline fields, then click the "Add" button.
  - Expected: The new task appears in the task list showing its title, description, and deadline.

- [ ] FT-02: An existing task's title, description, and deadline can be edited and saved.
  - Action: Click the "Edit" button on an unblocked task, change its title, description, and deadline, and save.
  - Expected: The task in the list shows the updated title, description, and deadline; the old values are replaced.

- [ ] FT-03: A task can be completed and is retained in the list as completed.
  - Action: Click the "Complete" button on an active task.
  - Expected: The task is marked as completed but remains visible in the task list (e.g., completed state/section) — it is not deleted or lost.

- [ ] FT-04: A task can be deleted.
  - Action: Click the "Delete" button on a task in the list.
  - Expected: The task is removed from the task list and no longer appears in any view.

- [ ] FT-05: A priority can be assigned to a task and is shown on it.
  - Action: Set a priority level (e.g., High/Medium/Low) for a task via the add form or the task's "Edit" form, and save.
  - Expected: The chosen priority value is displayed on that task in the list.

- [ ] FT-06: The task list can be sorted by priority.
  - Action: Select the "sort by priority" option in the sort control.
  - Expected: The list reorders so tasks are arranged by priority level, highest priority first (e.g., High before Medium before Low).

- [ ] FT-07: The task list can be sorted by deadline.
  - Action: Select the "sort by deadline" option in the sort control.
  - Expected: The list reorders so tasks are arranged by deadline date, earliest deadline first.

- [ ] FT-08: Active tasks can be viewed first.
  - Action: Use the page's way to view active tasks first (e.g., an "Active" filter/tab or default list ordering).
  - Expected: Every active (incomplete) task is displayed above every completed task; no completed task precedes an active task.

- [ ] FT-09: One or more prerequisite tasks can be bound to a task.
  - Action: Open a task's prerequisite/dependency selector (in the add or "Edit" form) and select two other existing tasks as its prerequisites, then save.
  - Expected: The task is bound to both selected tasks as prerequisites; both dependency relationships are recorded and visible.

## Constraint
- [ ] CS-01: Title is a required field — a task cannot be added without it.
  - Action: In the add-task form, leave the title empty and click "Add".
  - Expected: The task is not added; submission is blocked with a validation message indicating the title is required.

- [ ] CS-02: Description is optional — a task can be added without one.
  - Action: Add a task with a title (and deadline) but leave the description empty.
  - Expected: The task is added successfully and appears in the list without a description.

- [ ] CS-03: A task with an incomplete prerequisite cannot be completed.
  - Action: With Task A dependent on incomplete Task B, click the "Complete" button on Task A.
  - Expected: Task A is not marked completed; it stays active while Task B is incomplete.

- [ ] CS-04: A blocked task allows only description and priority to be modified.
  - Action: With Task A blocked by incomplete Task B, open Task A's edit interface and attempt to change title, deadline, description, and priority.
  - Expected: Description and priority changes are saved; title and deadline cannot be modified (fields locked/read-only or changes rejected).

- [ ] CS-05: A task with multiple prerequisites stays blocked until every prerequisite is completed.
  - Action: Bind Task A to prerequisites Task B and Task C, complete only Task B, then attempt to complete Task A and edit its title.
  - Expected: Task A remains blocked — completing is prevented and title/deadline stay unmodifiable while Task C is still incomplete.

- [ ] CS-06: Dependency gating is released once the prerequisite is completed.
  - Action: Complete Task B (prerequisite of blocked Task A), then click "Complete" on Task A and edit its title/deadline.
  - Expected: Task A can now be completed and fully edited (title/deadline modifiable); all previous restrictions are gone.

## Interaction
- [ ] IX-01: Edit/Complete buttons gray out while blocked and re-enable after the prerequisite completes.
  - Action: View Task A while its prerequisite Task B is incomplete; then complete Task B and view Task A again.
  - Expected: Task A's "Edit" and "Complete" buttons appear grayed out/disabled while Task B is incomplete, and appear enabled/normal after Task B is completed.

- [ ] IX-02: Dependent tasks are visually connected by a dashed line.
  - Action: View Task A (dependent) and Task B (prerequisite) in the task list.
  - Expected: A dashed line is drawn connecting Task A and Task B.

- [ ] IX-03: Hovering a dependency connection opens a pop-up window.
  - Action: Hover the mouse cursor over the dashed line connecting Task A and Task B.
  - Expected: A pop-up window appears near the connection while the cursor hovers over the line.

## Content
- [ ] CT-01: Blocked task shows the exact label "Prerequisite Task B Incomplete" next to it.
  - Action: View Task A while its prerequisite Task B is incomplete.
  - Expected: A prominent label stating "Prerequisite Task B Incomplete" (where "Task B" is the title of the incomplete prerequisite task) is displayed next to Task A.

- [ ] CT-02: The connection pop-up shows the details of the dependency chain.
  - Action: Hover over the dashed connection between Task A and Task B and read the pop-up content.
  - Expected: The pop-up shows the dependency chain details — the dependent task and its prerequisite task(s) identified by name, covering every link of the chain (including intermediate tasks in multi-level chains).