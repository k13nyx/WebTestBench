# Test Checklist

## Functionality
- [ ] FT-01: User can open a project from the project list and view its kanban board.
  - Action: On the project list page, click the name of the first default project.
  - Expected: The kanban board opens with status columns, and each existing task card appears in its matching column.
- [ ] FT-02: User can create a task with title, due date, priority, and assignee.
  - Action: On the board, click "New Task" in the "To Do" column. Enter Title "QA Checklist Task", set Due Date to a future date, set Priority to "High", set Assignee to a team member, and click "Save".
  - Expected: A card titled "QA Checklist Task" appears in "To Do" showing the due date, High priority, and the selected assignee.
- [ ] FT-03: User can drag a task card to another column and the new status persists after reload.
  - Action: Drag the "QA Checklist Task" card from "To Do" to "In Progress", then reload the page.
  - Expected: After reload, the card is still in "In Progress" and is not in "To Do".
- [ ] FT-04: User can mark progress on a task, and the progress is saved.
  - Action: Click the "QA Checklist Task" card, set its progress to 50% (or the app's progress control), and click "Save". Reload the page and reopen the card.
  - Expected: The card shows the updated progress, and the value is still 50% after reload.
- [ ] FT-05: User can view a concise summary of the project's overall status.
  - Action: Open the summary panel or header of the default project.
  - Expected: The summary shows a total task count and per-status counts (To Do, In Progress, Done) that match the number of cards in each column.
- [ ] FT-06: User can filter tasks by status.
  - Action: In the Status filter, select "In Progress".
  - Expected: Only tasks in "In Progress" are visible. Clearing the filter restores all tasks.
- [ ] FT-07: User can filter tasks by assignee.
  - Action: In the Assignee filter, select one team member who has at least one task.
  - Expected: Only tasks assigned to that member are visible.
- [ ] FT-08: User can search tasks by keyword.
  - Action: Type the first word of an existing task title in the search box and press Enter.
  - Expected: Only tasks whose title or description contains that keyword are visible. Clearing the search restores all tasks.
- [ ] FT-09: User can send a message in the project chat panel.
  - Action: In the project chat panel, type "Checklist test message" and click "Send".
  - Expected: The message appears at the end of the chat with the sender's name and a timestamp, and the input field clears.
- [ ] FT-10: Chat messages appear in real time for other team members.
  - Action: Open the same project in two browser windows, signed in as two different team members. Send a message from window A.
  - Expected: The message appears in window B without refreshing the page.

## Constraint
- [ ] CS-01: Task cannot be saved without a title.
  - Action: Open the New Task form, leave Title empty, fill in the other fields, and click "Save".
  - Expected: The task is not created, a required-field error appears on Title, and no new card appears on the board.
- [ ] CS-02: Assignee and priority are limited to valid options.
  - Action: Open the Assignee and Priority fields in the New Task form.
  - Expected: Assignee lists only the project's team members. Priority offers only the predefined levels (High, Medium, Low), and no other value can be entered.
- [ ] CS-03: An empty chat message cannot be sent.
  - Action: Leave the chat input empty, or enter only spaces, and click "Send" or press Enter.
  - Expected: No message is posted, and the chat history stays unchanged.
- [ ] CS-04: Tasks and chat messages are isolated per project.
  - Action: Note a task title and a chat message in the first default project. Switch to the second default project.
  - Expected: The second project's board and chat do not show the first project's tasks or messages.

## Interaction
- [ ] IX-01: The target column is highlighted while a card is dragged over it.
  - Action: Drag a task card over the "Done" column without releasing the mouse button. Then move the cursor out of the column.
  - Expected: "Done" shows a visible drop highlight while the card hovers over it, and the highlight disappears when the cursor leaves.
- [ ] IX-02: Clicking a task card opens its detail view.
  - Action: Click any task card on the board.
  - Expected: A detail panel or modal opens showing title, description, due date, priority, assignee, and progress. It closes when the "X" is clicked.
- [ ] IX-03: A success toast appears after a task is created.
  - Action: Create a task with valid Title, Due Date, Priority, and Assignee, and click "Save".
  - Expected: A toast reading "Task created" appears and disappears automatically after a few seconds.
- [ ] IX-04: The chat scrolls to the newest message when a new message is sent.
  - Action: Scroll the chat history up to the oldest messages, then send a new message.
  - Expected: The chat scrolls to the bottom so the newly sent message is visible.

## Content
- [ ] CT-01: Due dates display the same value and format on the card and in the detail view.
  - Action: Compare the due date on the "QA Checklist Task" card with the due date in its detail view.
  - Expected: Both show the same date in the same format, with no blank values or "Invalid Date".
- [ ] CT-02: Assignee names on cards are real team members.
  - Action: Review the assignee shown on each task card on the default project's board.
  - Expected: Every card shows a named team member from the project's team list, with no placeholder text such as "undefined", "null", or "User 1".
- [ ] CT-03: Existing chat messages show correct sender names and timestamps.
  - Action: Review the existing messages in the default project's chat panel.
  - Expected: Each message shows a real team member name and a valid timestamp, with no blank or "undefined" values.