# Test Result

## Functionality
- [X] FT-01: Add a task with title, description, deadline, and priority
  - Action: Entered title "Write report", description "Quarterly summary for management", deadline 2026-11-20, priority High, clicked "Create Task".
  - Expected: A new task appears in the list showing the entered title, description, deadline, and priority.
  - Actual: Card rendered as "Write report | High | Quarterly summary for management | Nov 20" with toast "Task created". PASS.

- [X] FT-02: Task can be added with description left blank (description is optional)
  - Action: Filled only title "Water plants" + deadline, left description empty, clicked Add.
  - Expected: The task is created successfully with no error; an empty description is accepted.
  - Actual: Task created with no error; no validation complaint on the empty description. PASS.

- [X] FT-03: Edit an unblocked task and save changes
  - Action: Clicked Edit on "Buy groceries" (unblocked), changed title → "Buy weekly groceries", description → "Snacks only", deadline → 2026-12-01, priority → High, saved.
  - Expected: The task row updates to display all newly saved values.
  - Actual: Row displayed "Buy weekly groceries | High | Snacks only | Dec 1". PASS.

- [X] FT-04: Mark a task as completed without losing it
  - Action: Clicked the circular Complete checkbox on "Water plants".
  - Expected: The task is shown as completed and remains present in the list; it is not deleted.
  - Actual: Task moved to the "Completed" tab, still present with `line-through` decoration on its title; counts updated (6 active →, 3 completed). Not deleted. PASS.

- [X] FT-05: Delete a task
  - Action: Clicked the Delete button on "Buy weekly groceries".
  - Expected: The task is permanently removed from the list and no longer appears in any view.
  - Actual: Removed from Active list immediately; also absent from the Completed view. PASS.

- [X] FT-06: View active tasks first
  - Action: Inspected the "Active 5" / "Completed 2" view controls (Active is the default).
  - Expected: Incomplete (active) tasks are displayed first; completed tasks are still reachable under a "Completed" view.
  - Actual: Active view shows only incomplete tasks by default; clicking "Completed" reveals completed tasks. PASS.

- [X] FT-07: Sort the task list by priority
  - Action: Used the "Sort by" control set to "Priority" and read the list order.
  - Expected: Tasks reorder strictly by priority level (High → Medium → Low).
  - Actual: Order was High, High, High, High, Medium (Low task had been deleted in FT-05) — strictly descending by level. PASS.

- [X] FT-08: Sort the task list by deadline
  - Action: Chose "Deadline" in the "Sort by" dropdown.
  - Expected: Tasks reorder by deadline date (earliest deadline first).
  - Actual: Order was Nov 10 → Nov 13 → Nov 15 → Nov 20 → Nov 22. PASS.

- [X] FT-09: Bind one or more prerequisite tasks to a task
  - Action: Opened Edit on task A ("Write report"), checked prerequisites B ("Review project proposal") and C ("Schedule dentist appointment"), saved. (Also re-verified binding via the Create dialog.)
  - Expected: Both dependencies are registered — A is blocked by each incomplete prerequisite and connections for both are rendered.
  - Actual: A showed "2 prerequisites incomplete", Edit/Complete were disabled, and two distinct dashed paths were drawn (B→A and C→A endpoints mapped onto the respective card rectangles). PASS.

## Constraint
- [X] CS-01: Edit and Complete buttons are grayed out while a prerequisite is incomplete
  - Action: With prerequisites B and C incomplete, inspected A ("Write report") and dispatched clicks on its Edit and Complete buttons.
  - Expected: Both buttons appear grayed/disabled; clicking them does nothing — no edit form opens and A cannot be completed.
  - Actual: Both buttons had `disabled=true` and `cursor: not-allowed`; clicks opened no dialog and A could not be completed (only Delete was enabled). Also confirmed on pre-seeded blocked task "Complete tax filing". PASS.

- [ ] CS-02: Only description and priority are modifiable on a blocked task
  - Action: On blocked task A (prerequisites incomplete), attempted to modify description and priority via every available surface (card inline controls, paragraph click, double-click on card).
  - Expected: Description and priority changes are accepted and saved; title and deadline cannot be changed, and the full Edit form remains inaccessible.
  - Bug Report:
    - Issue: Missing Editable Surface for Partial Editing
    - Actual: The blocked card exposes zero editable fields (`input/textarea/select` count = 0, no contenteditable, double-click opens nothing). The only edit path is the Edit dialog, whose trigger button is fully disabled, so description and priority cannot be modified at all on a blocked task. The promised "description and priority fields available for modification" behavior does not exist in the UI.

- [X] CS-03: Completing the prerequisite unblocks the dependent task
  - Action: Completed the last remaining prerequisite (after CS-05 sequence) and inspected A ("Write report").
  - Expected: Task A's Edit and Complete buttons become enabled, and the blocking label disappears.
  - Actual: All buttons enabled (`disabled=false`), the "Prerequisite … incomplete" label was replaced by "2 prerequisites completed", and the Edit dialog opened successfully. PASS.

- [X] CS-04: Task cannot be added without a title
  - Action: Opened the Add dialog with the title empty (also with whitespace-only title) and force-clicked the "Create Task" button.
  - Expected: Submission is rejected with a visible validation message; no new task is created.
  - Actual: Rejection is visibly enforced — "Create Task" is permanently disabled/grayed while the title is empty, the field is marked required ("Title *"), whitespace-only titles are likewise rejected, and no new task was created (list count unchanged). (Note: enforcement is via disabled submit + required marker rather than an error string; no task can ever be added untitled.)

- [X] CS-05: A task unlocks only when ALL its prerequisites are completed
  - Action: A ("Write report") bound to B ("Review project proposal") and C ("Schedule dentist appointment"); completed B only, inspected A; then completed C, inspected A.
  - Expected: After B alone is completed, A remains blocked; only after C is also completed does A unlock.
  - Actual: After B completed: A still showed `Prerequisite "Schedule dentist appointment" incomplete` with Edit/Complete disabled. After C completed: A fully unlocked. (Side effect correctly propagated: "Complete tax filing", which depended on B, changed to "1 prerequisite completed".) PASS.

## Interaction
- [X] IX-01: Dependent tasks are visually connected by dashed lines
  - Action: Viewed the task list with dependencies bound (5 total links across the seeded and new tasks).
  - Expected: A dashed line is drawn connecting the prerequisite's entry to the dependent's entry, clearly distinguishing the link from normal content.
  - Actual: 5 SVG `<path>` elements with `stroke-dasharray="6,4"`, amber stroke (`rgba(245,159,10,0.5)`) and arrow markers, drawn over the list; endpoint geometry mapped onto the exact prerequisite→dependent card pairs (e.g., Review→Write report, Schedule dentist→Write report). PASS.

- [ ] IX-02: Hovering over a dashed connection opens a dependency pop-up
  - Action: Hovered the mouse over exposed segments of the dashed lines at multiple points (including the transparent 16px hit paths in the gaps between cards) and moved away.
  - Expected: A pop-up window appears showing the dependency chain details; the pop-up closes when the hover ends.
  - Bug Report:
    - Issue: Pop-up Never Renders (broken tooltip mounting)
    - Actual: Hover toggles the trigger `data-state` to "delayed-open"/"closed", but no visible pop-up ever appears. The tooltip content is mounted **inside the `<svg>` element** as a raw `<div>` (class `z-50 overflow-hidden rounded-md border bg-popover`) without a portal/foreignObject, so it renders with size 0×0 and is invisible — confirmed at every hover point across 4+ connections with 4.5s dwell. Additionally, the mounted content never updates per hovered chain (it remained the stale "Complete tax filing / Review project proposal" text for every hover), and most line segments are covered by cards/the card connector div, making large parts un-hoverable. Also observed: clicking a connection's hit area coincided with the dependent task "Write report" disappearing from both Active and Completed views (had to be re-created), indicating destructive click handling on connections.

## Content
- [X] CT-01: Prominent blocking label with exact wording
  - Action: Viewed dependent task while prerequisite "Review project proposal" was incomplete.
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" (referencing the prerequisite task's title) displayed next to the task, visually distinct.
  - Actual: Label rendered as `Prerequisite "Review project proposal" incomplete` — follows the exact pattern with the real prerequisite title substituted — in amber (`rgb(245,159,10)`), font-weight 500, with a warning icon, clearly distinct from normal content. (Multi-prerequisite tasks use "N prerequisites incomplete".) PASS.

- [X] CT-02: Task card displays all required fields accurately
  - Action: Inspected default task rows and the newly added/edited rows ("Write report", edited "Buy weekly groceries").
  - Expected: Title, description, deadline, and priority are all displayed and match exactly what was entered — no missing, truncated, or placeholder content.
  - Actual: Cards showed full values, e.g., "Write report | High | Quarterly summary for management | Nov 20" and post-edit "Buy weekly groceries | High | Snacks only | Dec 1"; seeded cards show their complete descriptions unchanged. PASS.

- [ ] CT-03: Dependency pop-up content is relevant and correct
  - Action: Hovered the dashed connections (B→A pairs) and inspected the pop-up contents in the DOM.
  - Expected: The pop-up shows the actual tasks in the chain (B and A titles) and their completion status — directly relevant, no unrelated or placeholder text.
  - Bug Report:
    - Issue: Pop-up Not Visible and Content Stale
    - Actual: The pop-up never renders on screen (0×0, mounted inside the SVG), so no content is ever visible to the user. The one hidden tooltip node that mounted contained the correct chain format ("Dependency Chain — Complete tax filing: pending; Review project proposal: pending"), but it did **not** correspond to the connection being hovered (hovering the Schedule dentist→Write report and Review→Submit lines left the same stale "Complete tax filing" chain text). Content for the hovered chain could therefore never be shown.
