# Test Result

## Functionality

- [X] FT-01: Create a task with title, description, and deadline
  - Action: Enter title "Buy groceries", description "Milk and eggs", pick a deadline date, click the Add/Create Task button.
  - Expected: A new task appears in the list displaying that title, description, and deadline.

- [X] FT-02: Create a task with a title only (description and deadline optional)
  - Action: Enter only the title "Call dentist", leave description and deadline empty, click Add Task.
  - Expected: Task is created with no error; it appears with its title and empty/blank description and deadline fields.

- [X] FT-03: Edit all fields of a task that has no incomplete prerequisites
  - Action: Click Edit on a default task, change its title, description, and deadline, then save.
  - Expected: The task row shows the updated title, description, and deadline.

- [X] FT-04: Mark a task complete and confirm it is not lost
  - Action: Click Complete on an active default task.
  - Expected: The task remains in the list, is visually marked as completed (e.g., strikethrough or dimmed), and is not deleted.

- [X] FT-05: Delete a task
  - Action: Click Delete on a task (confirm if a prompt appears).
  - Expected: The task is removed from the list and does not reappear in the active or completed view.

- [X] FT-06: Assign a priority to a task
  - Action: Open the priority control on a default task, select "High", and save/apply.
  - Expected: The task now displays "High" as its priority.

- [X] FT-07: Sort the list by priority
  - Action: Choose the "Sort by Priority" option.
  - Expected: Tasks are reordered by priority (e.g., High → Medium → Low); completed tasks stay grouped after active ones.

- [X] FT-08: Sort the list by deadline
  - Action: Choose the "Sort by Deadline" option.
  - Expected: Tasks are reordered by deadline with the earliest deadline first; tasks with no deadline appear last.

- [X] FT-09: Active tasks are shown before completed tasks
  - Action: Mark one default task complete, then view the default list ordering.
  - Expected: Every incomplete (active) task is listed above every completed task.

- [X] FT-10: Bind one or more prerequisite tasks to a task
  - Action: On Task A, open the dependency/prerequisite selector and add Task B; then add a second prerequisite Task C to the same Task A.
  - Expected: Task A records both Task B and Task C as prerequisites, and both are displayed as its dependencies.

## Constraint

- [X] CS-01: Edit and Complete are disabled on a task whose prerequisite is incomplete
  - Action: With Task A dependent on the incomplete Task B, click Task A's Edit button and its Complete button.
  - Expected: Both buttons appear grayed out/disabled and neither action occurs (no edit form opens, task is not marked complete).

- [ ] CS-02: Only description and priority are modifiable on a blocked task
  - Action: Open the edit area of the blocked Task A (prerequisite Task B incomplete).
  - Expected: Description and Priority fields are editable; Title and Deadline fields are locked/not editable.
  - Bug Report:
    - Issue: Blocked-task fields not modifiable — edit area cannot be opened at all
    - Actual: On the blocked task "Complete tax filing" (prerequisite "Review project proposal" incomplete), the Edit button carries `disabled` and is grayed out (`cursor-not-allowed text-muted-foreground/40`), so no edit form/dialog opens. Dispatching a click on it produced 0 dialogs, and clicking the description paragraph and the priority badge produced 0 inputs/textareas. The row's only enabled control is Delete. Thus description and priority — the two fields the spec says must stay modifiable — cannot be edited at all; there is no view in which title/deadline are locked while description/priority are open.

- [X] CS-03: "Prerequisite <task> Incomplete" warning label is displayed
  - Action: View Task A while its prerequisite Task B is incomplete.
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" (using the prerequisite's actual title) is displayed next to Task A.

- [X] CS-04: Block is released once the prerequisite is completed
  - Action: Mark prerequisite Task B as complete.
  - Expected: Task A's Edit and Complete buttons become enabled and the "Prerequisite Task B Incomplete" label disappears.

- [X] CS-05: A task with multiple prerequisites stays blocked until all are complete
  - Action: Give Task A two prerequisites (Task B, Task C), complete only Task B, then inspect Task A.
  - Expected: Task A's Edit and Complete remain disabled, and it still shows a "Prerequisite Task C Incomplete" label for the remaining one.

## Interaction

- [X] IX-01: Dashed connector line visually links dependent tasks
  - Action: With Task A dependent on Task B, view the task list area.
  - Expected: A dashed line is drawn connecting Task A and Task B, and it is visually distinguishable as dashed rather than solid.

- [X] IX-02: Hovering the connector opens a dependency-chain pop-up
  - Action: Hover the mouse over the dashed connector between Task A and Task B, then move the pointer away.
  - Expected: A pop-up appears showing the dependency chain details (e.g., involved task titles and their completion status), and it closes when the pointer leaves.

- [X] IX-03: A newly added task appears in the list immediately without a page refresh
  - Action: Add a task with title "New immediate task" while staying on the same page.
  - Expected: The task appears in the list right away, in the correct position for the current sort, without a manual reload.

## Content

- [X] CT-01: Each task row shows its full data
  - Action: Inspect any default task in the list.
  - Expected: The row displays the task's title, its description (or an empty state), its deadline, and its assigned priority.

- [X] CT-02: All page content is to-do themed
  - Action: Read the page heading, form labels, buttons, and empty-state text.
  - Expected: All text and labels relate to managing tasks (title, description, deadline, priority, complete, delete, dependencies); no unrelated or placeholder content such as lorem ipsum or product listings.