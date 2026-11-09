# Test Checklist

## Functionality
- [ ] FT-01: Add a task with title, description, and deadline
  - Action: Enter title "Write report", description "Q3 summary", deadline "2026-11-20", click "Add Task"
  - Expected: Task appears in the list with the title, description, and deadline displayed
- [ ] FT-02: Add a task with only a title (description and deadline optional)
  - Action: Enter title "Buy milk" only, click "Add Task"
  - Expected: Task is created and appears in the list without a description or deadline
- [ ] FT-03: Edit an existing task's fields
  - Action: Click "Edit" on a task, change title to "Write report v2" and deadline to "2026-11-25", save
  - Expected: Task card shows the updated title and deadline
- [ ] FT-04: Complete a task without losing it
  - Action: Click "Complete" on an active task
  - Expected: Task is marked completed (e.g., strikethrough/checked style) but remains visible in the list
- [ ] FT-05: Delete a task
  - Action: Click "Delete" on a task
  - Expected: Task is removed from the list entirely
- [ ] FT-06: Active tasks display before completed tasks
  - Action: Create 2 tasks, complete one of them
  - Expected: The active task appears above the completed task in the list
- [ ] FT-07: Bind a prerequisite task to a task
  - Action: Open Task A's edit form, select Task B as its prerequisite, save
  - Expected: Task A is saved with the dependency to Task B
- [ ] FT-08: Sort the list by priority
  - Action: Create tasks with priorities High/Medium/Low, choose sort by "Priority"
  - Expected: List orders tasks from highest priority to lowest
- [ ] FT-09: Sort the list by deadline
  - Action: Create tasks with deadlines 2026-11-10, 2026-11-05, and one with no deadline, choose sort by "Deadline"
  - Expected: List orders tasks from earliest to latest deadline (tasks without a deadline sort last)
- [ ] FT-10: Complete the prerequisite unlocks the dependent task
  - Action: Complete Task B (the prerequisite), then check Task A's buttons
  - Expected: Task A's "Edit" and "Complete" buttons become enabled, and the "Prerequisite Task B Incomplete" label disappears
- [ ] FT-11: Hover over a dashed dependency line shows dependency chain popup
  - Action: Hover over the dashed line connecting Task A and Task B
  - Expected: A pop-up window appears showing the dependency chain details (e.g., "Task A depends on Task B") and disappears when the hover ends

## Constraint
- [ ] CS-01: Cannot add a task with an empty title
  - Action: Leave title empty, click "Add Task"
  - Expected: Task is not created; a validation message is shown (title is required)
- [ ] CS-02: Complete button is disabled for a task whose prerequisite is incomplete
  - Action: Bind Task A to incomplete Task B, then inspect Task A's "Complete" button
  - Expected: The "Complete" button is grayed out (disabled); clicking it does nothing
- [ ] CS-03: Edit button is disabled for a task whose prerequisite is incomplete, but description and priority remain editable
  - Action: With Task B incomplete, open Task A's edit form
  - Expected: The "Edit" button is grayed out (disabled); if the edit form is accessible, only description and priority fields are modifiable, and title/deadline are locked
- [ ] CS-04: Cannot complete a task when any of its multiple prerequisites is incomplete
  - Action: Bind Task A to two prerequisites (Task B and Task C), complete only Task B
  - Expected: Task A's "Complete" and "Edit" buttons remain disabled until Task C is also completed
- [ ] CS-05: A task cannot be bound as its own prerequisite
  - Action: Open Task A's dependency selector and attempt to select Task A itself
  - Expected: Task A is not selectable in the prerequisite list (or the selection is rejected)

## Interaction
- [ ] IX-01: Prominent label "Prerequisite Task B Incomplete" appears next to Task A
  - Action: Bind Task A to incomplete Task B and view the list
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" is displayed next to Task A's card
- [ ] IX-02: Dashed lines visually connect dependent tasks
  - Action: Bind Task A to Task B and view the page
  - Expected: A dashed line is drawn between Task A and Task B, indicating the dependency visually

## Content
- [ ] CT-01: Each task card displays its assigned priority
  - Action: Create a task with priority "High" and view its card
  - Expected: The priority "High" is displayed on the task card
- [ ] CT-02: The dependency chain popup shows the correct task names
  - Action: Hover over the dependency line between Task A (dependent) and Task B (prerequisite) and read the popup
  - Expected: The popup text names the actual task titles, showing Task B as the prerequisite of Task A