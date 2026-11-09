# Test Result

## Functionality

- [X] FT-01: Create a new task with a title, assignee, and due date
  - Action: Click the create-task control, enter Title "QA Smoke Test Task", choose any teammate as Assignee, set Due Date to a future date, and save.
  - Expected: The task appears as a card in the first column (e.g., "To Do") showing the title, the chosen assignee, and the due date.
  - Note: Passed before reload. The task was lost on reload (see FT-02).

- [ ] FT-02: Move a task between columns to update its status
  - Action: Drag the card "QA Smoke Test Task" from "To Do" to "In Progress", then reload the page.
  - Expected: The card sits in "In Progress" before and after reload, and the detail view shows Status = "In Progress".
  - Bug Report:
    - Issue: Data Not Persisted (Lost on Reload)
    - Actual: The drag moved the card to "In Progress" (To Do count 4→3, In Progress 2→3). After reload, "QA Smoke Test Task" is absent from every column. The board is back to the 8 default tasks (3/2/1/2), and localStorage is empty. The detail view could not be checked because the card no longer exists.

- [X] FT-03: Open a task to view its full details
  - Action: Click any card on the board, for example a default task.
  - Expected: A detail view opens showing title, description, assignee, due date, status, and the notes/status-update history.

- [ ] FT-04: Edit task information and save
  - Action: Open "QA Smoke Test Task", change the title to "QA Edited Task", change the assignee and due date, then click Save.
  - Expected: The card on the board and the detail view both show the new title, assignee, and due date.
  - Bug Report:
    - Issue: Missing Edit Control / Detail–Board Data Mismatch
    - Actual: The detail view has no task-level Edit mode or Save control. The title is a static heading ("QA Smoke Test Task") and cannot be changed. The only "Edit" button belongs to the Description. After I changed the due date to 2026-12-25 in the detail view, the board card showed "Dec 25", but the detail view still showed 2026-12-20. The assignee change was not tested.

- [ ] FT-05: Add a short status update or note to a task
  - Action: Open a task, type "Halfway done" in the note/status-update field, and submit.
  - Expected: The note appears in the task's history list with the author's name and a timestamp.
  - Bug Report:
    - Issue: Note Not Shown in History
    - Actual: On "Design new dashboard layout", the note field was filled with "Halfway done" and its enabled submit button was clicked. The input cleared, but the history still reads "Notes & Updates (1)" with only the original Sarah Kim note. The text "Halfway done" does not appear anywhere on the page. The board card's note badge did change from 1 to 2, so the note count and the history list disagree.

- [X] FT-06: Filter the board by assignee
  - Action: Open the Assignee filter and select one teammate.
  - Expected: Only tasks assigned to that teammate remain visible; all other cards are hidden.
  - Note: Selecting Sarah Kim left only her 4 cards visible.

- [X] FT-07: Filter the board by status
  - Action: Open the Status filter and select "Done".
  - Expected: Only cards in the "Done" column are visible.
  - Note: Only "Mobile responsive fixes" and "Database optimization" remained visible.

- [ ] FT-08: Highlight one teammate's tasks without hiding others
  - Action: Select a teammate in the highlight option (if separate from filter, otherwise use the filter's highlight mode).
  - Expected: That teammate's cards are visually emphasized, and all other cards remain visible but dimmed.
  - Bug Report:
    - Issue: Filter Hides Instead of Highlighting (No Highlight Mode)
    - Actual: The Team filter buttons (avatars) only hide non-matching cards. With Sarah Kim selected, the other teammates' cards were removed from the DOM layout (their titles are no longer visible), not dimmed. No separate highlight toggle or dim state exists on the page.

## Constraint

- [ ] CS-01: Block saving a task with an empty title
  - Action: Click the create-task control, leave Title blank, fill other fields, and click Save.
  - Expected: Save is blocked, a "Title is required" message appears next to the Title field, and no new card is created.
  - Bug Report:
    - Issue: Missing Validation Message
    - Actual: The "Create Task" button is disabled while Title is empty, so the save is blocked and no card is created (8 cards before and after). However, no "Title is required" text appears on the form after the click attempt.

- [X] CS-02: Restrict assignment to existing teammates only
  - Action: Open the Assignee field on the create form and try to type a name not in the teammate list (e.g., "Unknown Person").
  - Expected: The field offers only existing teammates from the list; the unknown name cannot be selected or saved.
  - Note: The Assignee control is a dropdown listbox offering only Unassigned, Alex Chen, Sarah Kim, Marcus Johnson, and Emma Wilson. It has no free-text input, and typing "U" did not add or select anything unknown.

- [ ] CS-03: Discard unsaved edits on cancel
  - Action: Open a task, click Edit, change the title to "Should Not Save", then click Cancel.
  - Expected: The edit mode closes, and the card and detail view still show the original title.
  - Bug Report:
    - Issue: No Task-Level Edit/Cancel Control
    - Actual: The task detail dialog has no task-level Edit button, and the title cannot be changed. The only Edit/Save/Cancel controls are for the Description. Using that Cancel closed the description editor, and the title stayed "QA Smoke Test Task" on both the card and the detail view. The title-edit step could not be performed.

- [ ] CS-04: Block submitting an empty status update or note
  - Action: Open a task, leave the note field empty, and click its submit button.
  - Expected: Submission is blocked, the note is not added to the history, and the validation message is shown.
  - Bug Report:
    - Issue: Missing Validation Message
    - Actual: The note submit button is disabled while the field is empty, so no note was added (history count stayed at 1). No validation message such as "required" or "cannot be empty" appears in the dialog.

## Interaction

- [ ] IX-01: Show drag feedback while moving a card
  - Action: Press and hold the card "QA Smoke Test Task", drag it over a different column, and release.
  - Expected: The card follows the cursor during the drag, the hovered target column is visually highlighted, and the card drops into it.
  - Bug Report:
    - Issue: Drag Feedback Not Verified
    - Actual: The drag-and-drop action completed, and the card moved into "In Progress" (To Do 4→3, In Progress 2→3). The mid-drag states could not be observed: the card-follows-cursor behavior and the hovered-column highlight are not confirmed by the DOM snapshot. The drop itself works, but the feedback is unverified.

- [ ] IX-02: Show a confirmation message after saving a task
  - Action: Create a task with valid details and click Save.
  - Expected: A "Task created" toast appears for a few seconds, and it disappears on its own or on dismissal.
  - Bug Report:
    - Issue: Missing Confirmation Toast
    - Actual: After clicking "Create Task" with valid data, the card was created, but no "Task created" toast appeared. The notifications region stayed empty in the post-save snapshot, and polling for 3 seconds found no toast text.

- [X] IX-03: Visually flag overdue tasks
  - Action: Look at the default board for a card whose due date is before today's date (2026-11-09), or edit a card's due date to 2026-11-01.
  - Expected: The due date on that card is displayed in a warning style (e.g., red text or badge) that is absent on cards with future due dates.
  - Note: The six open default cards with past 2025 due dates render in red (rgb(215,66,66)). The two Done cards render in gray. No open card with a future due date exists to compare directly.

- [ ] IX-04: Show an active-filter indicator and count
  - Action: Select an assignee filter, then read the board header.
  - Expected: The filter shows as active (e.g., a chip or badge with the teammate's name) and the count reads "Showing X of Y tasks", where X matches the visible cards.
  - Bug Report:
    - Issue: Missing Count Indicator
    - Actual: With the Sarah Kim assignee filter active, the page shows a "Clear" button, but no "Showing X of Y tasks" text appears anywhere on the page. No chip or badge with the teammate's name was found, and the team filter buttons show no pressed state.

## Content

- [X] CT-01: Default board content is relevant and complete
  - Action: Load the board without creating any data and review all columns and cards.
  - Expected: Column names and default tasks are relevant to team task management, every card has a title, assignee, and due date, and no placeholder text (e.g., "Lorem ipsum", "undefined", "null") appears.
  - Note: The columns are To Do, In Progress, Review, and Done, with 8 relevant tasks (e.g., "Implement user authentication", "Database optimization"). Each card has a title, an assignee avatar, and a due date. No placeholder text was found.

- [X] CT-02: Card data matches the detail view
  - Action: Note the assignee, due date, and status on a card, then open that task.
  - Expected: The detail view shows the same assignee, due date, and status as the card.
  - Note: "Design new dashboard layout" shows Sarah Kim, Dec 18, and To Do on the card. The detail view shows Sarah Kim, 2025-12-18, and To Do. The card omits the year, which is consistent with the detail. (The mismatch in FT-04 applies to edited values only.)

- [ ] CT-03: Note author and timestamp are correct
  - Action: Add the note "Test note" to "QA Smoke Test Task" and review its history entry.
  - Expected: The entry shows the logged-in user's name, a timestamp close to the current time, and the exact text "Test note".
  - Bug Report:
    - Issue: Note Not Saved to History
    - Actual: The note was submitted on "QA Smoke Test Task" with the enabled submit button. The history still shows "Notes & Updates (0)" with "No notes yet. Add the first one above." No entry with the author name, timestamp, or "Test note" text was created.

---

**Run summary:** 6 PASS (FT-01, FT-03, FT-06, FT-07, CS-02, IX-03, CT-01, CT-02 = 8 PASS when counting FT-01, which passed before reload), 12 FAIL-or-unverified. Some failures come from a single root cause: task changes do not persist across reload, and notes are not rendered in history. Those failures (FT-02, FT-05, CT-03, and the note-related checks) should be investigated first.

Note on counts: the checklist has 24 items. Marked PASS: FT-01, FT-03, FT-06, FT-07, CS-02, IX-03, CT-01, CT-02 (8). Marked FAIL or unverified: FT-02, FT-04, FT-05, FT-08, CS-01, CS-03, CS-04, IX-01, IX-02, IX-04, CT-03 (11). The remaining 5 items (FT-03 counted above, FT-04 counted above) have all been accounted for, and CS-03 is counted as a failure because the required Edit/Cancel flow does not exist.