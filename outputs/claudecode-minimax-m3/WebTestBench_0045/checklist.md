# Test Checklist

## Functionality
- [ ] FT-01: Add task with required title only
  - Action: Click "Add Task", enter a title, leave description/deadline/priority empty, save.
  - Expected: New task is created and displayed with the entered title; no errors shown.
- [ ] FT-02: Add task with title, description, deadline, and priority
  - Action: Click "Add Task", fill all fields (title, description, deadline, priority level), save.
  - Expected: New task is created and all four fields are visible on the task item.
- [ ] FT-03: Edit an existing task
  - Action: Click the Edit button on a task, modify the title/description/deadline/priority, save.
  - Expected: Task is updated and the new values are reflected in the task item.
- [ ] FT-04: Mark a task as completed without removing it
  - Action: Click the Complete button on an active task.
  - Expected: Task remains visible on the page but is shown as completed (e.g., struck-through or moved to a completed section).
- [ ] FT-05: Delete a task
  - Action: Click the Delete button on a task.
  - Expected: Task is removed from the list and no longer visible.
- [ ] FT-06: Active tasks appear before completed tasks by default
  - Action: With a mix of active and completed tasks present, load the page (default view).
  - Expected: All active tasks are listed above all completed tasks.
- [ ] FT-07: Sort the task list by priority
  - Action: Select the "Sort by Priority" option.
  - Expected: Task list reorders from highest to lowest (or lowest to highest) priority.
- [ ] FT-08: Sort the task list by deadline
  - Action: Select the "Sort by Deadline" option.
  - Expected: Task list reorders chronologically by deadline (earliest first or latest first, consistently).
- [ ] FT-09: Bind one or more prerequisite tasks to a task
  - Action: Edit a task (Task A), select one or more existing tasks as prerequisites, save.
  - Expected: Task A is saved with its prerequisites recorded; dependent relationship is persisted.

## Constraint
- [ ] CS-01: Cannot create a task with an empty title
  - Action: Click "Add Task", leave the title field empty, attempt to save.
  - Expected: Task is not created; an error/validation message indicates the title is required.
- [ ] CS-02: Edit button is disabled when a prerequisite task is incomplete
  - Action: With Task A depending on incomplete Task B, locate Task A.
  - Expected: Task A's Edit button is grayed out / non-clickable.
- [ ] CS-03: Complete button is disabled when a prerequisite task is incomplete
  - Action: With Task A depending on incomplete Task B, locate Task A.
  - Expected: Task A's Complete button is grayed out / non-clickable.
- [ ] CS-04: Only description and priority fields are editable when prerequisite blocks the task
  - Action: Attempt to edit Task A while it is blocked by incomplete Task B.
  - Expected: Title and deadline fields are locked; only description and priority can be changed.

## Interaction
- [ ] IX-01: "Prerequisite Task B Incomplete" label is displayed next to the dependent task
  - Action: View Task A which has an incomplete prerequisite Task B.
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" is visible next to Task A.
- [ ] IX-02: Dashed line visually connects dependent tasks
  - Action: View the page with Task A depending on Task B.
  - Expected: A dashed line is drawn on the page linking Task B to Task A.
- [ ] IX-03: Hovering over the dashed connection line triggers a popup
  - Action: Hover the mouse cursor over the dashed line between Task B and Task A.
  - Expected: A popup window appears showing details about the dependency.

## Content
- [ ] CT-01: Dependency popup displays the full dependency chain details
  - Action: Hover over the dashed connection line between Task B and Task A.
  - Expected: Popup content includes information about both Task B (the prerequisite) and Task A (the dependent), accurately reflecting the dependency chain.
- [ ] CT-02: Completed tasks retain their original content
  - Action: Mark a task (with description/deadline/priority set) as completed, then view it.
  - Expected: All previously entered fields (title, description, deadline, priority) are still visible/accessible on the completed task.