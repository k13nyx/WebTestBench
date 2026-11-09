All filter combinations verified. The full test pass is complete; here are the results.

# Test Result

## Functionality
- [X] FT-01: User can create a new task with title, assignee, and due date
  - Action: Click the "Add Task" / "New Task" button, fill in title, select a teammate, set a due date, and submit.
  - Expected: A new task card with that title, assignee, and due date appears on the board (in the initial/"To Do" column).
  - Note: Created "Sprint retro planning" (Marcus Johnson, Dec 1) — card appeared in "To Do" (badge 3→4) with title, avatar `alt="Marcus Johnson"`, and due date.

- [X] FT-02: Task can be assigned to a specific teammate
  - Action: Open the task detail view and change the assignee to another teammate, then save.
  - Expected: The task card on the board displays the new teammate's name/avatar; the old assignee is no longer shown.
  - Note: Sarah Kim → Alex Chen; card avatar changed to `alt="Alex Chen"` immediately, reopened detail shows "Alex Chen", old assignee gone. Minor defect observed: the assignee field inside the *open* dialog keeps showing the stale value ("Sarah Kim") until the dialog is reopened.

- [X] FT-03: Task status changes by moving it between columns
  - Action: Drag a task card from the "To Do" column to the "In Progress" (or "Done") column.
  - Expected: The card is now displayed under the target column, and its status reflects the new column.
  - Note: Dragged "Update onboarding flow" To Do → In Progress; card moved and detail view Status combobox showed "In Progress".

- [X] FT-04: User can open a task to see its details
  - Action: Click on an existing default task card.
  - Expected: A detail view/modal opens showing title, description, assignee, due date, status, and notes for that task.
  - Note: Modal "Design new dashboard layout" showed title, description paragraph, Assignee (Sarah Kim), Due Date (2025-12-18), Status (To Do), and "Notes & Updates (1)" with a seeded note.

- [ ] FT-05: User can edit a task's information
  - Action: From the open task detail view, change the title and due date, then save.
  - Expected: Changes persist — the updated title and due date are shown on the task card and reopen correctly in the detail view.
  - Bug Report:
    - Issue: Missing Edit Capability (task title is not editable anywhere in the detail view)
    - Actual: The due date edit works (set to 2026-01-05; card showed "Jan 5" and reopened detail showed 2026-01-05), but the title renders as a static `<h2>` with no input, no contenteditable, and no edit button — the title portion of the expected edit cannot be performed at all.

- [X] FT-06: User can add a status update or short note to a task
  - Action: In the task detail view, type a note (e.g., "Waiting on design review") into the notes field and submit.
  - Expected: The note is appended to the task's notes/activity list and is visible when the task is reopened.
  - Note: "Waiting on design review" was recorded and visible on reopen (list grew to "Notes & Updates (3)", card comment counter 1→3). Minor defect: the notes list inside the open dialog does not live-update after submit; entries appear only after reopening the dialog.

- [X] FT-07: Board can be filtered by assignee
  - Action: Select a specific teammate from the assignee filter control.
  - Expected: Only tasks assigned to that teammate remain visible on the board; all other task cards are hidden.
  - Note: "Sarah Kim" filter → exactly her 3 cards visible (Design new dashboard layout, Create component library docs, Mobile responsive fixes); all others hidden.

- [X] FT-08: Board can be filtered or highlighted by status
  - Action: Select a status filter (e.g., "In Progress").
  - Expected: Only tasks with that status are shown, or tasks of that status are visually highlighted while others are dimmed.
  - Note: "In Progress" chip → only "Implement user authentication" and "API rate limiting" remained visible; other columns emptied to 0.

- [X] FT-09: Filters can be combined and cleared
  - Action: Apply an assignee filter and a status filter together, then clear/reset the filters.
  - Expected: Both filters apply simultaneously (intersection of results); after clearing, all default tasks are visible again.
  - Note: Marcus Johnson + In Progress → exactly 1 card ("API rate limiting"); Sarah Kim + In Progress → 0 (intersection correct). "Clear" button (appears when filters active) restored all 8 tasks.

## Constraint
- [X] CS-01: Task creation requires a title
  - Action: Click "Add Task", leave the title field empty, select assignee and due date, and attempt to submit.
  - Expected: Submission is blocked and a validation message indicates the title is required; no new card is created.
  - Note: With assignee + due date set but title empty, the "Create Task" button remained disabled; a forced click created no card (8→8). The required-ness is indicated by the "Title *" label (no separate error text, but submission is properly gated).

- [X] CS-02: Assignee must be an existing teammate
  - Action: Open the assignee selector on the task creation form or detail view.
  - Expected: Only the names of existing team members are offered as options; no free-text or nonexistent teammate can be assigned.
  - Note: Both the create-form and detail-view assignee selectors are closed dropdown lists with exactly "Unassigned" + the 4 existing members (Alex Chen, Sarah Kim, Marcus Johnson, Emma Wilson); no free-text input possible.

- [X] CS-03: Due date must be a valid date
  - Action: Enter an invalid date (e.g., "13/32/2026" or non-date text) in the due date field and attempt to save.
  - Expected: The invalid date is rejected with a validation message, or the date picker prevents entry of impossible dates.
  - Note: Native `input[type="date"]`: typing "13/32/2026" left the detail-view value unchanged (2025-12-18); in the create form the impossible segments were clamped to a valid date (2026-12-31). Impossible dates cannot be entered.

- [ ] CS-04: A moved task exists in exactly one column
  - Action: Drag a task card from "To Do" to "Done", then inspect both columns and refresh/reopen the task.
  - Expected: The card appears only under "Done" — no duplicate remains in "To Do", and the status change persisted.
  - Bug Report:
    - Issue: Missing Persistence (state resets on refresh)
    - Actual: Before refresh the move was correct ("Create component library docs" appeared only under "Done", 0 duplicates, 10 total cards). After refreshing the page, the card returned to "To Do" and ALL prior changes (created tasks, moved task, edits, notes) reverted to the seed data — the status change did not persist across refresh.

- [X] CS-05: Empty notes/status updates are not recorded
  - Action: Open the notes field on a task and submit it with no text (or whitespace only).
  - Expected: No empty note entry is added to the task's notes/activity list.
  - Note: With empty text the submit button is disabled; filling whitespace-only ("   ") also kept the button disabled, so no empty entry could be recorded (list stayed at "Notes & Updates (1)").

## Interaction
- [ ] IX-01: Confirmation feedback after task creation
  - Action: Create a new task successfully.
  - Expected: A visible confirmation (toast message or the new card appearing highlighted) indicates the task was created; the creation form/modal closes.
  - Bug Report:
    - Issue: Missing Confirmation Feedback
    - Actual: The creation modal closed (that part is fine), but no toast appeared — the notification regions stayed empty across ~2.1s of polling (also empty at 0.9s) — and the new card carried only the generic `animate-fade-in` shared by all cards with no highlight ring (boxShadow "none"). No visible confirmation that the task was created.

- [X] IX-02: Drag-and-drop affordances on the board
  - Action: Begin dragging a task card and hover it over a different column.
  - Expected: The card shows a drag preview and the target column is visually highlighted as a valid drop zone; dropping elsewhere returns the card to its original column.
  - Note: Mid-drag the "In Progress" column gained a drop-zone class (`ring-2 ring-primary/30 bg-primary/5` vs idle), the dragged card got a drag transform offset; releasing over a non-board area (toolbar) returned the card to "To Do" unchanged.

- [X] IX-03: Task detail view opens and closes without side effects
  - Action: Click a task card to open the detail view, then close it via the "X" button or backdrop, without editing.
  - Expected: The modal closes, the board is still fully visible, and the task's data is unchanged.
  - Note: Opened "Update onboarding flow" detail, clicked "Close" — dialog removed, all 4 columns with all cards still rendered, column membership identical before/after the open-close cycle.

- [X] IX-04: Empty-state feedback when a filter matches no tasks
  - Action: Apply a filter combination (e.g., teammate with no tasks in the selected status).
  - Expected: The board shows a clear "no tasks match" message or empty columns rather than a broken/blank page.
  - Note: Sarah Kim + In Progress (0 matches) → every column badge showed "0" with an explicit "No tasks yet" message and a "Clear" button; board chrome fully intact.

## Content
- [X] CT-01: Board loads with default team tasks and data
  - Action: Open the page fresh and inspect the board and detail views of seeded tasks.
  - Expected: Multiple status columns (e.g., "To Do", "In Progress", "Done") are present, each seeded with relevant sample tasks having assignees, due dates, and at least one task containing notes.
  - Note: Fresh load showed 4 columns ("To Do" ×3, "In Progress" ×2, "Review" ×1, "Done" ×2 = 8 seeded tasks), all with assignee avatars and due dates; "Design new dashboard layout" contained a seeded note ("Initial sketches approved by the team…", 4 other cards showed comment counts).

- [X] CT-02: Task cards display complete key information
  - Action: Inspect any task card on the board.
  - Expected: Each card shows the task title, assignee identifier (name/avatar), and due date — no missing, placeholder ("Lorem ipsum"), or broken fields.
  - Note: All cards show a real title (h4), an assignee avatar with the teammate's name (`alt="Sarah Kim"`, etc.), and a due date (e.g., "Dec 18"). No placeholder text found. Minor cosmetic note: avatars load from an external service (api.dicebear.com); until loaded they render initials — identifiers remain present either way.

- [X] CT-03: Teammate content is consistent across the app
  - Action: Compare the names in the assignee filter and assignee dropdown with the names shown on task cards.
  - Expected: The same set of teammate names appears everywhere; no mismatched or duplicated teammate entries.
  - Note: Team filter buttons (Alex Chen, Sarah Kim, Marcus Johnson, Emma Wilson), header "4 members", assignee dropdowns in both create form and detail view (same 4 names + "Unassigned"), and card avatar names all match exactly — no duplicates or mismatches.

---
**Summary: 18 PASS / 3 FAIL.** Defects: FT-05 (title not editable from detail view), CS-04 (no persistence — all board changes revert on refresh), IX-01 (no visible creation confirmation). Minor observations worth logging: stale assignee/date labels inside an open detail dialog until reopen, notes list not live-appending, and no explicit error text for the required-title constraint (disabled button + "Title *" only).