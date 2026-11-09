# Test Checklist

## Functionality
- [ ] FT-01: Add a task with title, description, deadline, and priority
  - Action: Click "Add Task", enter title "Test Task A", description "Sample", deadline a future date, priority "High", then save.
  - Expected: "Test Task A" appears in the list with all four values shown as entered.
- [ ] FT-02: Add a task without an optional description
  - Action: Click "Add Task", enter title "Test Task B" only, leave description and deadline empty, then save.
  - Expected: The task saves without error and appears in the list.
- [ ] FT-03: Edit a task's title, deadline, and priority
  - Action: On an unlocked task, click "Edit", change the title, deadline, and priority, then save.
  - Expected: The list shows the updated values.
- [ ] FT-04: Complete a task and keep it in the list
  - Action: On an unlocked task, click "Complete", then reload the page.
  - Expected: The task remains in the list with a completed status after reload.
- [ ] FT-05: Delete a task
  - Action: Click "Delete" on a task and confirm if prompted, then reload the page.
  - Expected: The task is removed and does not reappear after reload.
- [ ] FT-06: Active tasks are listed before completed tasks by default
  - Action: View the default list, which contains both active and completed tasks.
  - Expected: Every active task appears above every completed task.
- [ ] FT-07: Sort by priority
  - Action: Select the priority sort option.
  - Expected: Tasks are ordered High, then Medium, then Low.
- [ ] FT-08: Sort by deadline
  - Action: Select the deadline sort option.
  - Expected: Tasks are ordered from earliest to latest deadline, with tasks lacking a deadline placed last.
- [ ] FT-09: Bind multiple prerequisite tasks to one task
  - Action: Click "Edit" on Task A, add Task B and Task C as prerequisites, then save.
  - Expected: Both Task B and Task C are saved and shown as prerequisites of Task A.
- [ ] FT-10: Unlock a dependent task when all prerequisites are completed
  - Action: Complete Task B and Task C, then check Task A's "Edit" and "Complete" buttons.
  - Expected: Both buttons are enabled and clickable.

## Constraint
- [ ] CS-01: Block saving a task with an empty title
  - Action: Click "Add Task", leave the title empty, then click save.
  - Expected: Save is blocked, a validation message appears, and no task is created.
- [ ] CS-02: Lock Edit and Complete on a task whose prerequisite is incomplete
  - Action: With Task B incomplete, view Task A and try to click "Edit" and "Complete".
  - Expected: Both buttons are grayed out and do not respond to clicks, and Task A's status does not change.
- [ ] CS-03: Restrict edits on a locked task to description and priority
  - Action: With Task B incomplete, change Task A's description and priority, save, then attempt to change its title and deadline.
  - Expected: Description and priority changes save successfully; the title and deadline cannot be changed.

## Interaction
- [ ] IX-01: Show the "Prerequisite Task B Incomplete" label next to a locked task
  - Action: View Task A while Task B is incomplete, then complete Task B.
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" appears next to Task A while Task B is incomplete and disappears after Task B is completed.
- [ ] IX-02: Show a dashed line connecting each dependent task to its prerequisite
  - Action: View Task A and its prerequisite Task B.
  - Expected: A dashed line visually connects Task A and Task B, with one line per prerequisite link.
- [ ] IX-03: Show a dependency chain pop-up when hovering over a connection
  - Action: Hover the mouse over the dashed line between Task A and Task B, then move the mouse away.
  - Expected: A pop-up appears while hovering and disappears when the mouse leaves.
- [ ] IX-04: Show completed tasks with a visual distinction
  - Action: View a completed task in the list.
  - Expected: The task is visibly distinguished from active tasks, for example with strikethrough or dimming.

## Content
- [ ] CT-01: Show the prerequisite label text exactly as specified
  - Action: View Task A while Task B is incomplete and read the label.
  - Expected: The label reads exactly "Prerequisite Task B Incomplete", with "Task B" replaced by the prerequisite's actual title.
- [ ] CT-02: Show each task's title, deadline, and priority without placeholder values
  - Action: View the default task list.
  - Expected: Every task shows its title, deadline in a readable date format, and priority; no field shows "undefined", "null", "NaN", or is blank when a value exists.
- [ ] CT-03: Show accurate task names and statuses in the dependency chain pop-up
  - Action: Hover over a dashed connection and read the pop-up.
  - Expected: The pop-up lists the correct task names in dependency order (for example, Task B → Task A) with each task's current completed or incomplete status matching the list.