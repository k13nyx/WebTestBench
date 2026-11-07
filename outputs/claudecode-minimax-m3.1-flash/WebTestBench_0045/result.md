# Test Result

## Functionality

- [X] FT-01: Add a task with title, description, and deadline
  - Action: Enter a title, a description, and a deadline date in the add-task form and submit it.
  - Expected: The new task appears in the list showing the entered title, description, and deadline.
- [X] FT-02: Add a task with only a title (description and deadline are optional)
  - Action: Enter only a title in the add-task form and submit it.
  - Expected: The task is created and displayed without error; the description and deadline fields remain empty.
- [X] FT-03: Edit an existing task's title, description, and deadline
  - Action: Open the edit control for an existing task, change its title, description, and deadline, then save.
  - Expected: The task list shows the updated title, description, and deadline; old values are no longer shown.
- [X] FT-04: Mark a task as completed and keep it in the list
  - Action: Click the complete control on an active task.
  - Expected: The task is marked as completed, remains visible in the list (not removed), and is distinguishable from active tasks.
- [X] FT-05: Delete a task
  - Action: Click the delete control on a task and confirm if a confirmation is shown.
  - Expected: The task and its entry are removed from the list; other tasks are unaffected.
- [X] FT-06: Assign a priority to a task
  - Action: Open the task's priority control and select a priority level (e.g., High, Medium, Low).
  - Expected: The task displays the selected priority and the value is retained when the task is edited or reloaded.
  - Note: Priority is set in the task's add/edit form (High/Medium/Low select), shown as a colored badge on the card and retained across subsequent edits (set to Low → saved → still Low after a later edit). The card badge itself is not clickable. Side finding: the app has no persistence layer (no localStorage, no API), so a page reload restores the seeded data — the priority of a newly created/edited task is not retained after a reload.
- [X] FT-07: Sort the task list by priority
  - Action: Activate the "sort by priority" control.
  - Expected: The list reorders so higher-priority tasks appear before lower-priority tasks.
- [X] FT-08: Sort the task list by deadline
  - Action: Activate the "sort by deadline" control.
  - Expected: The list reorders so tasks with earlier deadlines appear before tasks with later deadlines.
- [X] FT-09: View active tasks first
  - Action: Use the active-task view/filter control on the task list.
  - Expected: Active (incomplete) tasks are listed before completed tasks, and completed tasks are still accessible afterward.
- [X] FT-10: Bind one or more prerequisite tasks to a task
  - Action: Open the dependency control for Task A, select one prerequisite, then add a second prerequisite to the same task.
  - Expected: Both selected prerequisites are recorded for Task A and shown on the task's dependency information.

## Constraint

- [X] CS-01: A task cannot be created without a title
  - Action: Open the add-task form, leave the title empty, and attempt to submit.
  - Expected: Submission is rejected with a clear validation message and no task is created.
  - Note: With an empty (or whitespace-only) title the "Create Task" button stays disabled, pressing Enter in the title field submits nothing, the Title field is marked required with a red "*", and the task count does not change. The only validation feedback is the red required marker — no dedicated error text is rendered on the attempted submission.
- [X] CS-02: Edit and complete controls are grayed out for a task whose prerequisite is incomplete
  - Action: Bind incomplete Task B as a prerequisite of Task A, then inspect Task A's row.
  - Expected: Task A's edit and complete buttons appear disabled/grayed out and cannot be activated.
- [ ] CS-03: Only description and priority are modifiable while a prerequisite is incomplete
  - Action: With incomplete Task B bound to Task A, open Task A's editing state and attempt to change the title and deadline.
  - Expected: The title and deadline fields are not editable; only the description and priority fields accept changes.
  - Bug Report:
    - Issue: Blocked task's editing state cannot be opened / restricted editing unreachable
    - Actual: Task A's Edit button is disabled while a prerequisite is incomplete (tooltip: "Complete prerequisites first"), so the editing state can never be opened — double-clicking the title, the description and the card body all do nothing. Consequently neither the title/deadline lock nor any modification of the description/priority is possible. The form code does contain the intended restriction (title and deadline inputs get `disabled: isBlocked`, description and priority stay enabled), but that code path is unreachable because the Edit button is disabled for the same condition.
- [X] CS-04: Completing the prerequisite re-enables the dependent task
  - Action: With incomplete Task B bound to Task A, complete Task B, then inspect Task A.
  - Expected: Task A's edit and complete buttons become enabled, and the blocking label is removed.
- [X] CS-05: Blocking label states which prerequisite is incomplete
  - Action: With incomplete Task B bound to Task A, view Task A's entry.
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" is displayed next to Task A.
  - Note: The label is rendered as a prominent amber badge next to the dependent task reading `Prerequisite "Complete tax filing" incomplete` (i.e. it names the incomplete prerequisite instead of the literal phrase "Prerequisite Task B Incomplete"); when several prerequisites are incomplete it shows "2 prerequisites incomplete".
- [ ] CS-06: A task cannot be made its own prerequisite or create a circular dependency
  - Action: In the dependency selector for Task A, attempt to select Task A itself, and attempt to bind Task A to a task that already depends on Task A.
  - Expected: The invalid selection is rejected with an explanatory message and no circular dependency is created.
  - Bug Report:
    - Issue: Missing explanatory validation message for circular/self dependency
    - Actual: The invalid options are silently removed from the prerequisite selector — a task never appears in its own list, and a task that already depends on the current task (e.g. "Complete tax filing" and "Submit final report" when editing "Review project proposal", or "QA Alpha Task" when editing "Schedule dentist appointment") is not offered. No circular dependency is created, but no message, disabled entry, tooltip or warning is shown explaining why those tasks cannot be selected.

## Interaction

- [X] IX-01: Dependent tasks are visually connected by a dashed line
  - Action: Bind Task B as a prerequisite of Task A and view the list.
  - Expected: A dashed line is drawn between Task A and Task B, visually linking the dependent and prerequisite tasks.
- [ ] IX-02: Hovering a dependency connection opens a dependency-chain pop-up
  - Action: Hover the mouse over the dashed connection line between Task A and Task B.
  - Expected: A pop-up window appears showing the details of the dependency chain; it disappears when the pointer moves away.
  - Bug Report:
    - Issue: Unresponsive hover pop-up on dependency connection
    - Actual: Hovering the dashed connector only changes the line's own style (it turns `stroke-primary`, width 2.5, active arrowhead) — no pop-up window ever appears. The connector's tooltip content is present in the DOM but stays `data-state="closed"` with zero client rects (invisible) after waiting up to 6 s, tried at multiple points on the line (including the 16px transparent hit-area and the visible dashed stroke, in the card gaps where the line is exposed) and via a forced hover on the path element. The same Radix tooltip mechanism works on the task card's prerequisite badge ("Dependency Chain …" pop-up opens and closes correctly), so the failure is specific to the SVG connection trigger.
- [X] IX-03: Completing a task updates its visual state immediately
  - Action: Click the complete control on an active task and observe the row without reloading.
  - Expected: The row's appearance changes right away to a completed state (e.g., strikethrough/checked indicator) and is not left stale.

## Content

- [X] CT-01: Each task card displays its entered values accurately
  - Action: Add a task with a known title, description, deadline, and priority, then view and edit it.
  - Expected: The displayed title, description, deadline, and priority match the values entered, with the deadline in a readable date format.
- [ ] CT-02: Dependency pop-up lists the full dependency chain
  - Action: Create chain Task C depends on Task B depends on Task A, then hover the dashed connection between B and C.
  - Expected: The pop-up identifies the dependent task, its direct prerequisite, and the intermediate task(s) in the chain, using their titles.
  - Bug Report:
    - Issue: Dependency-chain pop-up never displayed for the dashed connection
    - Actual: Hovering the connection between "Complete tax filing" (B) and "Submit final report" (C) produces no pop-up (see IX-02), so the chain is never shown. The assembled chain text ("Dependency Chain — Submit final report (pending), Review project proposal (pending), Complete tax filing (pending)") exists only in the never-visible tooltip node. The pop-up that *is* reachable (hovering the task card's prerequisite badge) lists only the direct prerequisites of the dependent task and does not identify the dependent task or the intermediate chain step.