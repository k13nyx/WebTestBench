# Test Checklist

## Functionality
- [ ] FT-01: Create a new task with a title, assignee, and due date
  - Action: Click the create-task control, enter Title "QA Smoke Test Task", choose any teammate as Assignee, set Due Date to a future date, and save.
  - Expected: The task appears as a card in the first column (e.g., "To Do") showing the title, the chosen assignee, and the due date.
- [ ] FT-02: Move a task between columns to update its status
  - Action: Drag the card "QA Smoke Test Task" from "To Do" to "In Progress", then reload the page.
  - Expected: The card sits in "In Progress" before and after reload, and the detail view shows Status = "In Progress".
- [ ] FT-03: Open a task to view its full details
  - Action: Click any card on the board, for example a default task.
  - Expected: A detail view opens showing title, description, assignee, due date, status, and the notes/status-update history.
- [ ] FT-04: Edit task information and save
  - Action: Open "QA Smoke Test Task", change the title to "QA Edited Task", change the assignee and due date, then click Save.
  - Expected: The card on the board and the detail view both show the new title, assignee, and due date.
- [ ] FT-05: Add a short status update or note to a task
  - Action: Open a task, type "Halfway done" in the note/status-update field, and submit.
  - Expected: The note appears in the task's history list with the author's name and a timestamp.
- [ ] FT-06: Filter the board by assignee
  - Action: Open the Assignee filter and select one teammate.
  - Expected: Only tasks assigned to that teammate remain visible; all other cards are hidden.
- [ ] FT-07: Filter the board by status
  - Action: Open the Status filter and select "Done".
  - Expected: Only cards in the "Done" column are visible.
- [ ] FT-08: Highlight one teammate's tasks without hiding others
  - Action: Select a teammate in the highlight option (if separate from filter, otherwise use the filter's highlight mode).
  - Expected: That teammate's cards are visually emphasized, and all other cards remain visible but dimmed.

## Constraint
- [ ] CS-01: Block saving a task with an empty title
  - Action: Click the create-task control, leave Title blank, fill other fields, and click Save.
  - Expected: Save is blocked, a "Title is required" message appears next to the Title field, and no new card is created.
- [ ] CS-02: Restrict assignment to existing teammates only
  - Action: Open the Assignee field on the create form and try to type a name not in the teammate list (e.g., "Unknown Person").
  - Expected: The field offers only existing teammates from the list; the unknown name cannot be selected or saved.
- [ ] CS-03: Discard unsaved edits on cancel
  - Action: Open a task, click Edit, change the title to "Should Not Save", then click Cancel.
  - Expected: The edit mode closes, and the card and detail view still show the original title.
- [ ] CS-04: Block submitting an empty status update or note
  - Action: Open a task, leave the note field empty, and click its submit button.
  - Expected: Submission is blocked, the note is not added to the history, and the validation message is shown.

## Interaction
- [ ] IX-01: Show drag feedback while moving a card
  - Action: Press and hold the card "QA Smoke Test Task", drag it over a different column, and release.
  - Expected: The card follows the cursor during the drag, the hovered target column is visually highlighted, and the card drops into it.
- [ ] IX-02: Show a confirmation message after saving a task
  - Action: Create a task with valid details and click Save.
  - Expected: A "Task created" toast appears for a few seconds, and it disappears on its own or on dismissal.
- [ ] IX-03: Visually flag overdue tasks
  - Action: Look at the default board for a card whose due date is before today's date (2026-11-09), or edit a card's due date to 2026-11-01.
  - Expected: The due date on that card is displayed in a warning style (e.g., red text or badge) that is absent on cards with future due dates.
- [ ] IX-04: Show an active-filter indicator and count
  - Action: Select an assignee filter, then read the board header.
  - Expected: The filter shows as active (e.g., a chip or badge with the teammate's name) and the count reads "Showing X of Y tasks", where X matches the visible cards.

## Content
- [ ] CT-01: Default board content is relevant and complete
  - Action: Load the board without creating any data and review all columns and cards.
  - Expected: Column names and default tasks are relevant to team task management, every card has a title, assignee, and due date, and no placeholder text (e.g., "Lorem ipsum", "undefined", "null") appears.
- [ ] CT-02: Card data matches the detail view
  - Action: Note the assignee, due date, and status on a card, then open that task.
  - Expected: The detail view shows the same assignee, due date, and status as the card.
- [ ] CT-03: Note author and timestamp are correct
  - Action: Add the note "Test note" to "QA Smoke Test Task" and review its history entry.
  - Expected: The entry shows the logged-in user's name, a timestamp close to the current time, and the exact text "Test note".