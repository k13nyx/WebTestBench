# Test Checklist

## Functionality
- [ ] FT-01: Switch between multiple projects
  - Action: Click the project selector dropdown and select a different project from the list.
  - Expected: The Kanban board, project summary metrics, and chat panel update to display the selected project's data.
- [ ] FT-02: Create a task with due date, priority, and assignee
  - Action: Click the "New Task" button, enter a task title, select a due date, choose a priority level (e.g., High), select an assignee, and click "Create".
  - Expected: A new task card appears in the default Kanban column displaying the entered title, due date, priority tag, and assignee name/avatar.
- [ ] FT-03: Drag and drop task between Kanban columns
  - Action: Drag an existing task card from the "To Do" column and drop it into the "In Progress" column.
  - Expected: The task card stays in the "In Progress" column and its status updates to reflect the new column.
- [ ] FT-04: Filter tasks by assignee
  - Action: Select a specific team member from the "Assignee" filter dropdown.
  - Expected: Only tasks assigned to the selected team member remain visible on the Kanban board; all other tasks are hidden.
- [ ] FT-05: Filter tasks by status
  - Action: Select a specific status (e.g., "Done") from the status filter control.
  - Expected: Only tasks matching the selected status remain visible across the Kanban board.
- [ ] FT-06: Search tasks by keyword
  - Action: Type a specific keyword into the task search input field.
  - Expected: Only task cards with titles or descriptions matching the keyword remain visible on the board.
- [ ] FT-07: Update task progress
  - Action: Open a task card, update its progress indicator (e.g., adjust progress slider or mark percentage), and click "Save".
  - Expected: The task card updates immediately on the board to display the new progress value.
- [ ] FT-08: Send message in project chat panel
  - Action: Type a message into the project chat input box and click the "Send" button.
  - Expected: The message appears immediately in the project chat history with the sender's name and current timestamp.

## Constraint
- [ ] CS-01: Prevent task creation without required title
  - Action: Open the "New Task" form, leave the task title field blank while setting a due date and assignee, and click "Create".
  - Expected: The task is not created, and an inline error message indicates that the title is required.
- [ ] CS-02: Prevent sending empty chat messages
  - Action: Leave the chat input field completely blank (or with whitespace only) and click the "Send" button.
  - Expected: The message is not submitted, and no blank message bubble is added to the chat history.
- [ ] CS-03: Maintain chat isolation between projects
  - Action: Send a message in Project A's chat panel, then switch to Project B using the project selector.
  - Expected: The message sent in Project A does not appear in Project B's chat panel.
- [ ] CS-04: Handle search with no matching results
  - Action: Enter an unmatchable string (e.g., "xyznonexistent") into the task search bar.
  - Expected: All Kanban columns show zero tasks and display a "No tasks found" message.

## Interaction
- [ ] IX-01: Visual feedback during task card drag operation
  - Action: Click and hold a task card, then drag it over an adjacent Kanban column.
  - Expected: The dragged card displays an elevated/semi-transparent state, and the target column highlights to indicate a valid drop target.
- [ ] IX-02: Toggle chat panel visibility
  - Action: Click the chat panel collapse/expand button.
  - Expected: The chat panel smoothly collapses or expands without breaking the layout of the Kanban board.
- [ ] IX-03: Reset active filters
  - Action: Click the "Clear Filters" button while an assignee filter and search keyword are active.
  - Expected: All filter dropdowns and search inputs reset to their default blank state, and all Kanban task cards reappear.

## Content
- [ ] CT-01: Project overall status summary display
  - Action: View the overall status summary section at the top of the active project page.
  - Expected: Summary displays accurate metrics, including total task count, completed task count, and overall project completion percentage.
- [ ] CT-02: Kanban task card metadata display
  - Action: Inspect any populated task card on the Kanban board.
  - Expected: The card clearly displays the task title, assigned team member avatar/name, due date, priority badge, and current progress indicator.
- [ ] CT-03: Chat panel message details display
  - Action: Review existing messages in the active project chat panel.
  - Expected: Each message item displays the sender's name/avatar, message timestamp, and message body text.