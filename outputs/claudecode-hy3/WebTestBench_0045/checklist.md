# Test Checklist

## Functionality
- [ ] FT-01: Add a task with a title, optional description, and deadline
  - Action: Fill in a title, optional description, and a deadline, then click "Add Task"
  - Expected: The task appears in the list showing the entered title, description, and deadline

- [ ] FT-02: Edit an existing task
  - Action: Click "Edit" on a task, change its fields, and save
  - Expected: The task updates to reflect the new details

- [ ] FT-03: Mark a task as completed without deleting it
  - Action: Click "Complete" on a task
  - Expected: The task is marked completed (e.g., strikethrough/check) and remains visible in the list

- [ ] FT-04: Delete a task
  - Action: Click "Delete" on a task and confirm
  - Expected: The task is removed from the list

- [ ] FT-05: Assign a priority to a task
  - Action: Set a priority (e.g., Low/Medium/High) on a task during create or edit
  - Expected: The task displays the assigned priority

- [ ] FT-06: Bind one or more prerequisite tasks to a task
  - Action: On a task, select one or more existing tasks as prerequisites, then save
  - Expected: The task is recorded as dependent on the selected prerequisite task(s)

- [ ] FT-07: View active tasks first
  - Action: Activate the "Active first" / active-tasks view or filter
  - Expected: Incomplete tasks are listed before completed tasks

- [ ] FT-08: Sort the list by priority
  - Action: Select the "Sort by priority" option
  - Expected: Tasks are ordered by their priority

- [ ] FT-09: Sort the list by deadline
  - Action: Select the "Sort by deadline" option
  - Expected: Tasks are ordered by deadline (earliest first)

## Constraint
- [ ] CS-01: Block completion of a task whose prerequisite is incomplete
  - Action: Attempt to click "Complete" on Task A while its prerequisite Task B is incomplete
  - Expected: The task cannot be completed (action is prevented)

- [ ] CS-02: Lock non-permitted fields when prerequisite is incomplete
  - Action: Open edit on Task A while Task B is incomplete
  - Expected: Only description and priority are editable; all other fields are locked

- [ ] CS-03: Require ALL prerequisites complete before unlocking
  - Action: With Task A dependent on multiple prerequisites, complete only some of them
  - Expected: Task A remains locked until every prerequisite is completed

## Interaction
- [ ] IX-01: Disable Edit/Complete buttons when prerequisite incomplete
  - Action: View Task A while its prerequisite Task B is incomplete
  - Expected: The Edit and Complete buttons are grayed out / disabled

- [ ] IX-02: Draw dashed-line connections between dependent tasks
  - Action: View a list containing a dependent task relationship
  - Expected: A dashed line visually connects Task A to its prerequisite(s)

- [ ] IX-03: Show dependency details popup on connection hover
  - Action: Hover over the dashed connection line between Task A and Task B
  - Expected: A popup appears showing the details of the dependency chain

## Content
- [ ] CT-01: Display "Prerequisite [Task] Incomplete" label
  - Action: View Task A while prerequisite Task B is incomplete
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" (with the actual task name) appears next to Task A