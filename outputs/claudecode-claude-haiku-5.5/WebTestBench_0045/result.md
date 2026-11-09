# Test Result

## Functionality
- [X] FT-01: Add a task with title, description, deadline, and priority
  - Action: Click "Add Task", enter title "Test Task A", description "Sample", deadline a future date, priority "High", then save.
  - Expected: "Test Task A" appears in the list with all four values shown as entered.
- [X] FT-02: Add a task without an optional description
  - Action: Click "Add Task", enter title "Test Task B" only, leave description and deadline empty, then save.
  - Expected: The task saves without error and appears in the list.
- [X] FT-03: Edit a task's title, deadline, and priority
  - Action: On an unlocked task, click "Edit", change the title, deadline, and priority, then save.
  - Expected: The list shows the updated values.
- [ ] FT-04: Complete a task and keep it in the list
  - Action: On an unlocked task, click "Complete", then reload the page.
  - Expected: The task remains in the list with a completed status after reload.
  - Bug Report:
    - Issue: Completion Not Persisted After Reload
    - Actual: Clicked Complete on "Buy groceries" (Completed count went from 2 to 3). After reloading the page, "Buy groceries" is back in the Active list and the header reads "5 active, 2 completed".
- [ ] FT-05: Delete a task
  - Action: Click "Delete" on a task and confirm if prompted, then reload the page.
  - Expected: The task is removed and does not reappear after reload.
  - Bug Report:
    - Issue: Deleted Task Reappears After Reload
    - Actual: Clicked Delete on "Buy groceries". No confirmation was shown, the "Task deleted" notice appeared, and the Active count dropped from 5 to 4. After reloading, "Buy groceries" reappears in the Active list and the header reads "5 active, 2 completed".
- [ ] FT-06: Active tasks are listed before completed tasks by default
  - Action: View the default list, which contains both active and completed tasks.
  - Expected: Every active task appears above every completed task.
  - Bug Report:
    - Issue: Default View Excludes Completed Tasks
    - Actual: The default view shows only the 5 active tasks. Completed tasks are not rendered until the "Completed" tab is clicked, so the default list does not contain both kinds of task as the checklist assumes, and the active-above-completed ordering cannot be observed there.
- [X] FT-07: Sort by priority
  - Action: Select the priority sort option.
  - Expected: Tasks are ordered High, then Medium, then Low.
- [X] FT-08: Sort by deadline
  - Action: Select the deadline sort option.
  - Expected: Tasks are ordered from earliest to latest deadline, with tasks lacking a deadline placed last.
- [X] FT-09: Bind multiple prerequisite tasks to one task
  - Action: Click "Edit" on Task A, add Task B and Task C as prerequisites, then save.
  - Expected: Both Task B and Task C are saved and shown as prerequisites of Task A.
- [X] FT-10: Unlock a dependent task when all prerequisites are completed
  - Action: Complete Task B and Task C, then check Task A's "Edit" and "Complete" buttons.
  - Expected: Both buttons are enabled and clickable.

## Constraint
- [ ] CS-01: Block saving a task with an empty title
  - Action: Click "Add Task", leave the title empty, then click save.
  - Expected: Save is blocked, a validation message appears, and no task is created.
  - Bug Report:
    - Issue: Missing Validation Message
    - Actual: With the title empty, the "Create Task" button is disabled and pressing Enter does nothing. No task is created and the dialog stays open. No validation message appears; the only indicator is the "*" next to the Title label.
- [X] CS-02: Lock Edit and Complete on a task whose prerequisite is incomplete
  - Action: With Task B incomplete, view Task A and try to click "Edit" and "Complete".
  - Expected: Both buttons are grayed out and do not respond to clicks, and Task A's status does not change.
- [ ] CS-03: Restrict edits on a locked task to description and priority
  - Action: With Task B incomplete, change Task A's description and priority, save, then attempt to change its title and deadline.
  - Expected: Description and priority changes save successfully; the title and deadline cannot be changed.
  - Bug Report:
    - Issue: Locked Task Edit Unavailable
    - Actual: On locked "Test Task A" (2 prerequisites incomplete), the Edit button is disabled, so description and priority cannot be changed at all. The allowed-edit path could not be exercised.

## Interaction
- [ ] IX-01: Show the "Prerequisite Task B Incomplete" label next to a locked task
  - Action: View Task A while Task B is incomplete, then complete Task B.
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" appears next to Task A while Task B is incomplete and disappears after Task B is completed.
  - Bug Report:
    - Issue: Label Text Mismatch
    - Actual: A label appears next to locked tasks, but its text is 'Prerequisite "Review project proposal" incomplete' for one prerequisite or "2 prerequisites incomplete" for two. It does not read "Prerequisite Task B Incomplete". After the prerequisites were completed, the incomplete label was replaced by "2 prerequisites completed", which stays visible.
- [ ] IX-02: Show a dashed line connecting each dependent task to its prerequisite
  - Action: View Task A and its prerequisite Task B.
  - Expected: A dashed line visually connects Task A and Task B, with one line per prerequisite link.
  - Bug Report:
    - Issue: Dependency Line Count Mismatch
    - Actual: The DOM has only 3 dashed SVG paths (stroke-dasharray 6px, 4px). The data contains 5 prerequisite links: Test Task A ← Test Task B, Test Task A ← Test Task C, Complete tax filing ← Review project proposal, and Submit final report ← 2 prerequisites. The paths are zero-width vertical strokes at about x=640px, and none could be mapped to the Task A / Task B pair.
- [ ] IX-03: Show a dependency chain pop-up when hovering over a connection
  - Action: Hover the mouse over the dashed line between Task A and Task B, then move the mouse away.
  - Expected: A pop-up appears while hovering and disappears when the mouse leaves.
  - Bug Report:
    - Issue: Dependency Pop-up Missing
    - Actual: Dispatching pointer and mouse enter events on the dashed path produced no tooltip, popover, or dialog element, either during the hover or after the mouse left. This was a DOM-event simulation, not a real pointer hover, and the path has no usable hit area.
- [X] IX-04: Show completed tasks with a visual distinction
  - Action: View a completed task in the list.
  - Expected: The task is visibly distinguished from active tasks, for example with strikethrough or dimming.

## Content
- [ ] CT-01: Show the prerequisite label text exactly as specified
  - Action: View Task A while Task B is incomplete and read the label.
  - Expected: The label reads exactly "Prerequisite Task B Incomplete", with "Task B" replaced by the prerequisite's actual title.
  - Bug Report:
    - Issue: Label Text Format Mismatch
    - Actual: The label reads 'Prerequisite "Review project proposal" incomplete', with the title in quotes and a lowercase "incomplete". The expected form is "Prerequisite Review project proposal Incomplete". With multiple prerequisites the label reads "2 prerequisites incomplete" and does not name the task.
- [X] CT-02: Show each task's title, deadline, and priority without placeholder values
  - Action: View the default task list.
  - Expected: Every task shows its title, deadline in a readable date format, and priority; no field shows "undefined", "null", "NaN", or is blank when a value exists.
- [ ] CT-03: Show accurate task names and statuses in the dependency chain pop-up
  - Action: Hover over a dashed connection and read the pop-up.
  - Expected: The pop-up lists the correct task names in dependency order (for example, Task B → Task A) with each task's current completed or incomplete status matching the list.
  - Bug Report:
    - Issue: Dependency Pop-up Missing
    - Actual: No pop-up opens when hovering over the dashed connections, so the dependency chain's names and statuses cannot be read.

---

**Run notes (not part of the checklist):** The app keeps all data in memory only. A page reload restores the seeded data and discards tasks I created, edited, completed, or deleted. Because of this, FT-04 and FT-05 fail, and I avoided further reloads so the remaining tests could run on consistent state. Tool calls used: about 70 of the 100 budget.