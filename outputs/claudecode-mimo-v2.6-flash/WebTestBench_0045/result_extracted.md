# Test Result

## Functionality
- [X] FT-01: Add a task with title, description, and deadline
  - Action: Open the add-task form, enter a title, a description, and a deadline, then save.
  - Expected: The new task appears in the list showing its title, description, and deadline.
- [X] FT-02: Add a task without a description (description is optional)
  - Action: Add a task providing only a title and a deadline, leaving the description empty.
  - Expected: The task is created successfully and appears in the list.
- [X] FT-03: Edit an existing task's title, description, and deadline
  - Action: Open the edit form on a task, change its title, description, and deadline, then save.
  - Expected: The task in the list updates to show the new title, description, and deadline.
- [X] FT-04: Mark a task as completed
  - Action: Click the complete button on an active task.
  - Expected: The task is shown as completed (checked/struck through) and is no longer counted as active.
- [X] FT-05: Delete a task
  - Action: Click the delete button on a task in the list.
  - Expected: The task is immediately removed from the list.
- [X] FT-06: Completed tasks are kept, not lost
  - Action: After completing a task, open the completed-tasks view/section.
  - Expected: The completed task is still listed there and can be viewed.
- [X] FT-07: View active tasks first
  - Action: Use the Active-tasks view/filter (or inspect the default list order).
  - Expected: All active (incomplete) tasks are displayed ahead of any completed task.
- [X] FT-08: Assign a priority to a task
  - Action: Create or edit a task and select a priority (e.g., High).
  - Expected: The task's priority is saved and reflected as the selected value.
- [X] FT-09: Sort the list by priority
  - Action: Select the sort-by-priority option.
  - Expected: Tasks are ordered from highest to lowest priority (e.g., High → Medium → Low).
- [X] FT-10: Sort the list by deadline
  - Action: Select the sort-by-deadline option.
  - Expected: Tasks are ordered by deadline with the earliest deadline first.
- [X] FT-11: Bind one or more prerequisite tasks to a task
  - Action: On Task A, assign Task B (and optionally a second task) as prerequisite(s) and save.
  - Expected: Task A lists Task B (and the second task) as its prerequisite(s).

## Constraint
- [X] CS-01: Edit and complete buttons are grayed out while a prerequisite is incomplete
  - Action: With Task A dependent on not-yet-completed Task B, inspect Task A's buttons and try clicking them.
  - Expected: Task A's edit and complete buttons are grayed out/disabled and do not respond to clicks.
- [ ] CS-02: Only description and priority are modifiable while a prerequisite is incomplete
  - Action: On Task A (prerequisite Task B incomplete), change its description and priority, then attempt to change its title and deadline.
  - Expected: Description and priority changes save successfully; title and deadline cannot be modified (locked/disabled).
  - Bug Report:
    - Issue: Missing editing affordance — description/priority cannot be modified at all while a prerequisite is incomplete
    - Actual: Task A's edit button is fully disabled (opens no dialog: force-click produced dialog count 0), and there is no alternative editing path: clicking the priority pill (no dropdown/options, text unchanged), clicking the description (no textarea, contentEditable=inherit), single/double-clicking the card body and description all leave dialog count 0 and input count 0. Nothing is modifiable, so the expected "description and priority changes save successfully" can never occur (title/deadline are only trivially "locked" because every field is unreachable).
- [X] CS-03: Completing the prerequisite restores Task A's controls
  - Action: Mark prerequisite Task B as completed, then inspect Task A.
  - Expected: Task A's edit and complete buttons become enabled and usable again.

## Interaction
- [X] IX-01: Dependent tasks are connected by a dashed line
  - Action: With Task A dependent on Task B, view the task list.
  - Expected: A dashed line visually connects Task A to Task B.
- [X] IX-02: Hovering the dashed connection shows a dependency-chain popup
  - Action: Hover the mouse over the dashed line between Task A and Task B.
  - Expected: A popup window appears showing the dependency chain details (which task depends on which, with their statuses).

## Content
- [X] CT-01: Prerequisite-incomplete label is displayed next to Task A
  - Action: With Task B bound as prerequisite of Task B's dependent Task A, leave Task B incomplete and locate Task A.
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" (using the prerequisite's title) is displayed next to Task A.
- [X] CT-02: Each task card shows its assigned priority label
  - Action: Inspect the task cards in the list.
  - Expected: Every task displays a clear priority label matching its assigned priority (e.g., "High", "Medium", "Low").
