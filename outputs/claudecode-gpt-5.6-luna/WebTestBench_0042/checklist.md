# Test Checklist

## Functionality
- [ ] **FT-01: View and select multiple projects**
  - **Action:** Open the project management page and select each existing project from the project list.
  - **Expected:** Every existing project is displayed and can be selected successfully.

- [ ] **FT-02: Display a separate kanban board for each project**
  - **Action:** Select two different existing projects one at a time.
  - **Expected:** Each project displays its own kanban columns and task cards; tasks from one project do not appear in another.

- [ ] **FT-03: Create a task with required task details**
  - **Action:** In an existing project, click **Create Task**, enter a task title, due date, priority, and existing team-member assignee, then click **Save Task**.
  - **Expected:** The new task appears on the selected project’s kanban board with the entered due date, priority, and assignee.

- [ ] **FT-04: Move a task between kanban columns**
  - **Action:** Drag an existing task card from its current column to another status column.
  - **Expected:** The task appears in the destination column and its status reflects the destination column.

- [ ] **FT-05: Filter tasks by status**
  - **Action:** Select a value from the **Status** filter.
  - **Expected:** Only tasks with the selected status remain visible.

- [ ] **FT-06: Filter tasks by assignee**
  - **Action:** Select an existing team member from the **Assignee** filter.
  - **Expected:** Only tasks assigned to that team member remain visible.

- [ ] **FT-07: Search tasks by keyword**
  - **Action:** Enter a keyword from an existing task title into the **Search tasks** field.
  - **Expected:** Tasks matching the keyword remain visible and non-matching tasks are hidden.

- [ ] **FT-08: Combine task filters and search**
  - **Action:** Apply a status filter, an assignee filter, and a keyword search together.
  - **Expected:** Only tasks matching all active criteria are displayed.

- [ ] **FT-09: Mark progress on a task**
  - **Action:** Use the task’s progress control to update its progress value.
  - **Expected:** The task displays the updated progress value and the change remains after leaving and reopening the project.

- [ ] **FT-10: View the project status summary**
  - **Action:** Open an existing project and locate its project status summary.
  - **Expected:** The summary shows a concise overview of the project’s current task status and progress.

- [ ] **FT-11: Send a project chat message**
  - **Action:** In the selected project’s chat panel, enter a message and click **Send**.
  - **Expected:** The message appears in that project’s chat conversation with the entered text.

- [ ] **FT-12: Preserve separate chat conversations per project**
  - **Action:** Send or view messages in one project, switch to another project, and open its chat panel.
  - **Expected:** The chat panel shows only the conversation associated with the currently selected project.

## Constraint
- [ ] **CS-01: Prevent incomplete task creation**
  - **Action:** Open **Create Task**, leave the task title empty, and click **Save Task**.
  - **Expected:** The task is not created and the title field displays a required-field validation message.

- [ ] **CS-02: Reject an invalid due date**
  - **Action:** Enter an invalid date format in the **Due date** field and attempt to save the task.
  - **Expected:** The task is not saved and the due-date field displays a validation message.

- [ ] **CS-03: Keep filtered results consistent with task state**
  - **Action:** Apply a **Status** or **Assignee** filter, then move a visible task to a status or assignee that no longer matches the filter.
  - **Expected:** The task is removed from the filtered results immediately.

## Interaction
- [ ] **IX-01: Provide drag-and-drop feedback**
  - **Action:** Drag a task card over a different kanban column without dropping it, then release it.
  - **Expected:** The destination column visibly indicates it can receive the task during dragging, and the task moves only after it is released.

- [ ] **IX-02: Update the interface after task changes**
  - **Action:** Create or move a task, then inspect the board and project summary without manually refreshing the page.
  - **Expected:** The board and relevant summary values update immediately to reflect the change.

- [ ] **IX-03: Deliver chat messages in real time**
  - **Action:** Open the same project’s chat panel in two active sessions, send a message from one session, and observe the other.
  - **Expected:** The message appears in the other session’s chat panel without a page refresh.

## Content
- [ ] **CT-01: Display complete task information**
  - **Action:** Inspect task cards on an existing project board.
  - **Expected:** Each task card displays its title, due date, priority, assignee, current status, and progress when those values exist.

- [ ] **CT-02: Match the project summary to board data**
  - **Action:** Compare the project status summary with the visible task statuses and progress values.
  - **Expected:** Summary labels and values accurately represent the selected project’s current tasks.

- [ ] **CT-03: Identify chat messages clearly**
  - **Action:** Inspect messages in a project’s chat panel.
  - **Expected:** Each message displays its content and identifiable sender information, and all displayed messages belong to the selected project.