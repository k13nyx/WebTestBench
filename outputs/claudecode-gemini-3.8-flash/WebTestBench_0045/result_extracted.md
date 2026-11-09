# Test Result

## Functionality
- [X] FT-01: Add a new task with title, description, deadline, and priority
  - Action: Enter a task title, enter a description, select a deadline date, choose a priority level, and click the "Add Task" button.
  - Expected: The new task is added to the task list displaying the entered title, description, deadline, and priority badge.
- [ ] FT-02: Mark an unconstrained task as completed
  - Action: Click the "Complete" button on an active default task that has no incomplete prerequisites.
  - Expected: The task state updates to completed (e.g., checked or struck through) and remains visible in the task list.
  - Bug Report:
    - Issue: Premature Task Removal on Completion
    - Actual: Clicking the "Complete" button immediately removes the task from the active task list instead of keeping it visible in the list with a completed or struck-through state.
- [X] FT-03: Delete an existing task
  - Action: Click the "Delete" button on a default task.
  - Expected: The task is immediately removed from the task list.
- [ ] FT-04: Display active tasks before completed tasks
  - Action: Observe the default task list containing both active and completed tasks.
  - Expected: All active tasks are listed above the completed tasks.
  - Bug Report:
    - Issue: Segregated Views Instead of Unified Priority-Ordered List
    - Actual: The default task list only displays active tasks; completed tasks are completely excluded from the default view. They are only viewable by switching to the "Completed" tab, which in turn hides all active tasks, preventing active and completed tasks from appearing together in the same list.
- [X] FT-05: Sort task list by deadline
  - Action: Select the "Deadline" option from the sort control.
  - Expected: Tasks are reordered chronologically according to their deadline dates.
- [X] FT-06: Sort task list by priority
  - Action: Select the "Priority" option from the sort control.
  - Expected: Tasks are reordered according to their priority levels (e.g., High to Low).
- [X] FT-07: Unblock dependent task upon prerequisite completion
  - Action: Click the "Complete" button on prerequisite Task B.
  - Expected: Task A's edit and complete buttons become active/clickable, and the incomplete prerequisite warning disappears.

## Constraint
- [X] CS-01: Prevent completion of task with incomplete prerequisite
  - Action: Attempt to click the "Complete" button on Task A while prerequisite Task B is incomplete.
  - Expected: The "Complete" button is grayed out and does not trigger task completion.
- [ ] CS-02: Restrict title and deadline editing on task with incomplete prerequisite
  - Action: Open the edit mode for Task A while prerequisite Task B is incomplete, and attempt to modify its title or deadline.
  - Expected: The edit button is grayed out for core task updates, and the title and deadline fields are disabled/locked from editing.
  - Bug Report:
    - Issue: Edit Mode Inaccessible for Restricted Task
    - Actual: The edit button on Task A has the `disabled` attribute and its click handler is blocked (`!isBlocked && onEdit(task)`), preventing the user from opening the edit mode altogether while prerequisite Task B is incomplete.
- [ ] CS-03: Prevent task creation with an empty title
  - Action: Leave the title field blank, fill in optional description and deadline, and click "Add Task".
  - Expected: The task is not added, and an input validation error appears on the title field.
  - Bug Report:
    - Issue: Missing Input Validation Error
    - Actual: Although the "Create Task" button is disabled and prevents task submission, no input validation error message or error state is displayed on or beside the title field.

## Interaction
- [ ] IX-01: Open dependency chain pop-up on dashed line hover
  - Action: Hover the mouse cursor over the dashed line connecting Task B and Task A.
  - Expected: A pop-up window appears displaying the details of the dependency chain between the connected tasks.
  - Bug Report:
    - Issue: Pop-up Rendering Failure and Element Occlusion
    - Actual: The pop-up container (`TooltipContent`) is placed directly inside the `<svg>` DOM tree without a `<foreignObject>` wrapper or portal, rendering as an invalid SVG node with 0x0 dimensions and opacity 0. Furthermore, the dashed line between Task B (Task 1) and Task A (Task 4) is occluded by the overlapping dashed line connecting Task 1 to Task 7.
- [ ] IX-02: Dismiss dependency chain pop-up on mouse leave
  - Action: Move the mouse cursor away from the dashed line and pop-up window.
  - Expected: The dependency chain pop-up window disappears from the screen.
  - Bug Report:
    - Issue: Dependent Test Failure
    - Actual: Because the dependency chain pop-up fails to visibly open and render on screen upon hovering the dashed line, dismissing an active pop-up window on mouse leave cannot be performed or verified.
- [ ] IX-03: Modify allowed fields on a restricted dependent task
  - Action: Update the description text and change the priority dropdown on Task A (while Task B is incomplete), then save.
  - Expected: The updated description and priority are successfully saved and reflected on Task A without error.
  - Bug Report:
    - Issue: Inability to Open Edit Interface on Restricted Task
    - Actual: The edit button for Task A is completely disabled (`disabled` attribute and inert click handler) when prerequisite Task B is incomplete, making it impossible to open the edit dialog and update the allowed description and priority fields.

## Content
- [X] CT-01: Display incomplete prerequisite warning label
  - Action: Locate Task A when prerequisite Task B is incomplete.
  - Expected: A prominent label stating "Prerequisite Task B Incomplete" is visibly displayed next to Task A.
- [X] CT-02: Visual dashed line connection between dependent tasks
  - Action: Observe the visual relationship between prerequisite Task B and dependent Task A in the task view.
  - Expected: A distinct dashed line is drawn connecting Task B to Task A.
- [X] CT-03: Display task metadata and priority indicator
  - Action: Inspect any task card in the task list.
  - Expected: The task card accurately displays the task title, description text, deadline date, and priority level.
