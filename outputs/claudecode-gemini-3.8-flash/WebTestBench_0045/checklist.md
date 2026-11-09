# Test Checklist

## Functionality
- [ ] FT-01: Add a new task with title, description, deadline, and priority
  - Action: Enter a task title, enter a description, select a deadline date, choose a priority level, and click the "Add Task" button.
  - Expected: The new task is added to the task list displaying the entered title, description, deadline, and priority badge.
- [ ] FT-02: Mark an unconstrained task as completed
  - Action: Click the "Complete" button on an active default task that has no incomplete prerequisites.
  - Expected: The task state updates to completed (e.g., checked or struck through) and remains visible in the task list.
- [ ] FT-03: Delete an existing task
  - Action: Click the "Delete" button on a default task.
  - Expected: The task is immediately removed from the task list.
- [ ] FT-04: Display active tasks before completed tasks
  - Action: Observe the default task list containing both active and completed tasks.
  - Expected: All active tasks are listed above the completed tasks.
- [ ] FT-05: Sort task list by deadline
  - Action: Select the "Deadline" option from the sort control.
  - Expected: Tasks are reordered chronologically according to their deadline dates.
- [ ] FT-06: Sort task list by priority
  - Action: Select the "Priority" option from the sort control.
  - Expected: Tasks are reordered according to their priority levels (e.g., High to Low).
- [ ] FT-07: Unblock dependent task upon prerequisite completion
  - Action: Click the "Complete" button on prerequisite Task B.
  - Expected: Task A's edit and complete buttons become active/clickable, and the incomplete prerequisite warning disappears.

## Constraint
- [ ] CS-01: Prevent completion of task with incomplete prerequisite
  - Action: Attempt to click the "Complete" button on Task A while prerequisite Task B is incomplete.
  - Expected: The "Complete" button is grayed out and does not trigger task completion.
- [ ] CS-02: Restrict title and deadline editing on task with incomplete prerequisite
  - Action: Open the edit mode for Task A while prerequisite Task B is incomplete, and attempt to modify its title or deadline.
  - Expected: The edit button is grayed out for core task updates, and the title and deadline fields are disabled/locked from editing.
- [ ] CS-03: Prevent task creation with an empty title
  - Action: Leave the title field blank, fill in optional description and deadline, and click "Add Task".
  - Expected: The task is not added, and an input validation error appears on the title field.

## Interaction
- [ ] IX-01: Open dependency chain pop-up on dashed line hover
  - Action: Hover the mouse cursor over the dashed line connecting Task B and Task A.
  - Expected: A pop-up window appears displaying the details of the dependency chain between the connected tasks.
- [ ] IX-02: Dismiss dependency chain pop-up on mouse leave
  - Action: Move the mouse cursor away from the dashed line and pop-up window.
  - Expected: The dependency chain pop-up window disappears from the screen.
- [ ] IX-03: Modify allowed fields on a restricted dependent task
  - Action: Update the description text and change the priority dropdown on Task A (while Task B is incomplete), then save.
  - Expected: The updated description and priority are successfully saved and reflected on Task A without error.

## Content
- [ ] CT-01: Display incomplete prerequisite warning label
  - Action: Locate Task A when prerequisite Task B is incomplete.
  - Expected: A prominent label stating "Prerequisite Task B Incomplete" is visibly displayed next to Task A.
- [ ] CT-02: Visual dashed line connection between dependent tasks
  - Action: Observe the visual relationship between prerequisite Task B and dependent Task A in the task view.
  - Expected: A distinct dashed line is drawn connecting Task B to Task A.
- [ ] CT-03: Display task metadata and priority indicator
  - Action: Inspect any task card in the task list.
  - Expected: The task card accurately displays the task title, description text, deadline date, and priority level.