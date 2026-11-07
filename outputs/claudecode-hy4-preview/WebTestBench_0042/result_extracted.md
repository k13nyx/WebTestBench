# Test Result

## Functionality

- [X] FT-01: Multiple projects are listed and each opens its own kanban board
  - Action: On the project management page, note the number of default projects in the project list; click a project name (e.g., the second project in the list).
  - Expected: At least two projects are listed, and clicking one opens a kanban board area displaying that project's kanban board with its columns and task cards.

- [X] FT-02: User can create a task with due date, priority, and assignee
  - Action: On an open project's board, click "Add Task"/"+", fill in title, due date, priority, and assignee, then submit.
  - Expected: The new task card appears in the board's first/selected column and its saved detail shows the exact title, due date, priority, and assignee entered.

- [ ] FT-03: Task can be dragged between kanban columns
  - Action: Drag an existing task card from its current column and drop it into a different column (e.g., from "To Do" to "In Progress").
  - Expected: The card is displayed in the target column, its status in the task detail equals the target column's status, and it remains there after a page reload.
  - Bug Report:
    - Issue: State Not Persisted Across Reload
    - Actual: The drag itself worked correctly — "QA Verify Login Flow" moved from To Do to In Progress (To Do: 3→2, In Progress: 1→2) and the Edit Task dialog confirmed Status = "In Progress". However, after `page.reload()` the board reset to defaults: the app reverted to project "Website Redesign", and Mobile App Launch showed only its 5 default tasks (To Do 2 / In Progress 1 / Review 0 / Done 2) with the dragged card absent entirely. All board/app state is held in memory and is discarded on reload, so the move does not survive a page reload.

- [X] FT-04: Tasks can be filtered by status
  - Action: Set the status filter to one status (e.g., "In Progress") using the board's filter control.
  - Expected: Only cards matching that status are displayed; all cards of other statuses are hidden.

- [X] FT-05: Tasks can be filtered by assignee
  - Action: Set the assignee filter to one default team member.
  - Expected: Only cards assigned to that member are displayed; cards assigned to others or unassigned are hidden.

- [X] FT-06: Tasks can be searched by keyword
  - Action: Type a word that exists in a default task's title into the search box.
  - Expected: Only cards whose title contains that keyword are displayed; non-matching cards are hidden.

- [X] FT-07: Progress can be marked on a task
  - Action: Open an existing task and set its progress (e.g., move the progress control to 50% or toggle a progress/step control), then save/close.
  - Expected: The card displays the updated progress value, and the value persists after reopening the task.

- [X] FT-08: Concise project status summary is displayed
  - Action: Open a default project and locate the project summary area.
  - Expected: The summary shows the project's overall status concisely — total tasks, count per status, and a completion percentage that matches the board's card data.

- [X] FT-09: User can post a message in the project chat panel
  - Action: In the chat panel of the open project, type "Status update from QA" and send it.
  - Expected: The message appears in the chat panel's message list with the sender name and is visible immediately after sending.

- [ ] FT-10: Chat panel updates in real time without a manual refresh
  - Action: With the project page open, have a second team member (or a second browser session) post a message in the same project's chat; do not reload the first page.
  - Expected: The new message appears in the first page's chat panel automatically without refreshing or re-navigating.
  - Bug Report:
    - Issue: No Cross-Session Real-Time Synchronization
    - Actual: A second page was opened in the same browser context, "Mobile App Launch" was selected and the message "REALTIME PROBE from second session" was sent successfully (it rendered in the second page's message list). The first page — never reloaded or re-navigated — did not receive it: its chat panel still ended at "Final scroll test message". Chat state lives only in each page's in-memory React state, with no shared store or push channel, so messages never propagate between sessions.

## Constraint

- [ ] CS-01: Task cannot be created with an empty title
  - Action: Open the task creation form and submit it with the title field left empty.
  - Expected: The task is not created, no empty card is added to the board, and a required-field indication is shown on the title field.
  - Bug Report:
    - Issue: Missing Required-Field Indication
    - Actual: Submitting with an empty title correctly did not create a task — the "Create Task" dialog stayed open and the To Do column count remained 2. However, no required-field indication is shown on the title field: its DOM is `<input class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 ..." placeholder="Task title..." value="">` with `required=false`, `aria-required=null`, `aria-invalid=null`, no error class, and the dialog text contains no validation message (full dialog text remained "Create Task / Title / Description / Status / To Do / Priority / medium / Due Date / Assignee / Unassigned / Progress / 0% / Tags / Cancel / Create / Close"). The rejection is silent.

- [ ] CS-02: Filter/search with no matches shows an empty result state
  - Action: Enter a nonsense keyword (e.g., "zzzznotarealtask") in the search box.
  - Expected: No task cards are displayed and an explicit "no tasks"/"no results" empty-state message is shown instead of stale results.
  - Bug Report:
    - Issue: Missing Empty-State Message
    - Actual: Entering "zzzznotarealtask" correctly hid every card (all four columns report 0 cards). However, no "no tasks"/"no results" message is rendered anywhere in the board: `main.innerText` was "…All Status | All Members | TO DO | 0 | IN PROGRESS | 0 | REVIEW | 0 | DONE | 0", and a scan of every leaf element for /no task|no result|nothing found|no matching|empty/i returned zero matches. The user sees four empty columns with no explanation.

- [X] CS-03: Empty chat message cannot be sent
  - Action: In the chat input, leave the field empty (or only spaces) and attempt to send.
  - Expected: The send action is disabled or rejected, and no empty message bubble is added to the conversation.

- [X] CS-04: Multiple filters applied together return only tasks matching all criteria
  - Action: Apply a status filter and an assignee filter together where at least one task matches both.
  - Expected: Only cards satisfying both the status and the assignee criteria are displayed.

- [X] CS-05: Tasks are scoped to the selected project
  - Action: Note the task titles in Project A's board, then switch to a different default project (Project B).
  - Expected: None of Project A's task titles appear in Project B's board; only Project B's tasks are shown.

## Interaction

- [X] IX-01: Drag operation shows a drop indicator in the target column
  - Action: Start dragging a task card and hover it over a different column without releasing.
  - Expected: The target column displays a visible drop indicator/placeholder, and the dragged card is visually distinguished from the others.
  - Notes: Mid-drag DOM capture confirmed both behaviors. The In Progress drop zone switched to `class="flex-1 space-y-3 min-h-[100px] rounded-lg transition-colors bg-primary/5 ring-2 ring-dashed"` (dashed ring + tinted background), and the dragged card carried `class="group bg-card border rounded-lg p-4 cursor-pointer transition-all duration-200 hover:border-primary/30 hover:shadow-md shadow-xl rotate-2"` (drop shadow + 2° rotation) versus its resting `border-border` style.

- [X] IX-02: Filters and search apply immediately without a page reload
  - Action: Change the status filter and then type in the search box while watching the board.
  - Expected: The visible cards update instantly on each change, with no full page reload or loss of the current project view.
  - Notes: Verified with a `window.__qaMarker = 'alive'` sentinel set before the filter and search interactions — the marker survived all updates, and `performance.getEntriesByType('navigation').length` stayed at 1, proving no reload. Card lists refreshed instantly on both the status change and the search change, with the Mobile App Launch view retained.

- [ ] IX-03: New chat message is scrolled into view after sending
  - Action: Send a message in a project chat whose history is long enough to scroll.
  - Expected: The chat list auto-scrolls so the newly sent message is visible at the bottom, and the input field is cleared and refocused.
  - Bug Report:
    - Issue: Input Not Refocused After Send
    - Actual: Auto-scroll and clearing both work. After building a scrollable history, the message container measured `{scrollTop: 290, scrollHeight: 864, clientHeight: 574}` — 290 is exactly the maximum scroll offset (864−574) — and after the next send `{scrollTop: 362, scrollHeight: 936, clientHeight: 574}`, again exactly maximum (936−574), so the newest message is pinned at the bottom. The input was cleared (`inputValueAfterSend: ""`). However, focus was not returned to the input: `document.activeElement` resolved to `BODY` rather than the "Type a message..." field, so the user cannot continue typing without clicking back into the box.

## Content

- [X] CT-01: Each task card displays title, due date, priority, and assignee
  - Action: Inspect three default task cards on a project board.
  - Expected: Every card displays its title, a due date, a priority indication, and an assignee name/avatar matching the values in its detail view.
  - Notes: "Push notifications setup" → Medium / Feb 15 / avatar alt "James Wilson"; "App store submission prep" → Low / Mar 1 / no assignee (matches its Unassigned detail state); "Setup React Native project" → High / Jan 20 / avatar alt "Sarah Miller".

- [X] CT-02: Kanban columns are labeled with statuses and contain the project's default tasks
  - Action: Observe the column headers and the cards within them on an open project board.
  - Expected: Each column has a distinct status label, all default tasks of the project are present in exactly one column, and the labels match the statuses available in the status filter.
  - Notes: Columns are To Do / In Progress / Review / Done (droppable ids `todo`, `in-progress`, `review`, `done`); the status filter options are "All Status, To Do, In Progress, Review, Done" — an exact match. On Mobile App Launch, all 5 default tasks appeared in exactly one column each (2+1+0+2).

- [X] CT-03: Chat messages show sender and timestamp and belong to the current project
  - Action: Inspect the chat panel messages in Project A, then switch to Project B and inspect its chat.
  - Expected: Every message shows a sender name and a timestamp, and Project B's chat contains no messages that appeared only in Project A's chat.
  - Notes: Website Redesign chat = "You 17:30 / Sarah Miller 18:15 / James Wilson 21:00". Mobile App Launch chat = "Sarah Miller 16:00 / You 20:30". Every message carries both a sender name and a timestamp, and neither project's chat contains any message from the other.
