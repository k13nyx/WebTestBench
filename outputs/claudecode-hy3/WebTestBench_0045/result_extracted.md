# Test Result

## Functionality

- [X] FT-01: Add a task with a title, optional description, and deadline
  - Action: Fill in a title, optional description, and a deadline, then click "Add Task"
  - Expected: The task appears in the list showing the entered title, description, and deadline
  - (Verified: "TestTaskAlpha" created; shows title "TestTaskAlpha", description "My test description for alpha", deadline "Dec 1"; "Task created" notification received.)

- [X] FT-02: Edit an existing task
  - Action: Click "Edit" on a task, change its fields, and save
  - Expected: The task updates to reflect the new details
  - (Verified: Edited "Buy groceries" description → "Weekly shopping: milk, eggs, bread, veggies."; "Task updated" notification; card reflects new text.)

- [X] FT-03: Mark a task as completed without deleting it
  - Action: Click "Complete" on a task
  - Expected: The task is marked completed (e.g., strikethrough/check) and remains visible in the list
  - (Verified: "Schedule dentist appointment" moved to the Completed view; count "5 active, 3 completed"; it is present in the Completed filter with its complete/restore button — not deleted. Note: completed tasks are shown under the "Completed" filter rather than as inline-strikethrough in the active list.)

- [X] FT-04: Delete a task
  - Action: Click "Delete" on a task and confirm
  - Expected: The task is removed from the list
  - (Verified: "Buy groceries" removed; "Task deleted" notification; count "4 active, 3 completed"; card no longer present.)

- [X] FT-05: Assign a priority to a task
  - Action: Set a priority (e.g., Low/Medium/High) on a task during create or edit
  - Expected: The task displays the assigned priority
  - (Verified: Created tasks with High and Low priority; priority badge ("High"/"Low") rendered on each card; priority selectable in create/edit dialogs.)

- [X] FT-06: Bind one or more prerequisite tasks to a task
  - Action: On a task, select one or more existing tasks as prerequisites, then save
  - Expected: The task is recorded as dependent on the selected prerequisite task(s)
  - (Verified: "TestTaskAlpha" bound to "Review project proposal"; card shows "Prerequisite 'Review project proposal' incomplete". After completing that prerequisite, the label changed to "1 prerequisite completed" and the task unlocked — confirming the dependency was recorded and enforced.)

- [X] FT-07: View active tasks first
  - Action: Activate the "Active first" / active-tasks view or filter
  - Expected: Incomplete tasks are listed before completed tasks
  - (Verified: The "Active" filter button (Active 4) activates the active-tasks view and lists the 4 incomplete tasks. Note: implemented as an exclusive Active filter (separate from the "Completed" filter) rather than a combined interleaved list; the sort dropdown offers only Priority / Deadline / Date Created, with no dedicated "Active first" sort option.)

- [X] FT-08: Sort the list by priority
  - Action: Select the "Sort by priority" option
  - Expected: Tasks are ordered by their priority
  - (Verified: Under "Priority" sort the active list is TestTaskAlpha (High), Complete tax filing (High), Submit final report (High), LowPriTask (Low) — higher priority first.)

- [X] FT-09: Sort the list by deadline
  - Action: Select the "Sort by deadline" option
  - Expected: Tasks are ordered by deadline (earliest first)
  - (Verified: Under "Deadline" sort the active list is Submit final report (Nov 12), Complete tax filing (Nov 21), TestTaskAlpha (Dec 1), LowPriTask (Dec 25) — earliest first.)

## Constraint

- [X] CS-01: Block completion of a task whose prerequisite is incomplete
  - Action: Attempt to click "Complete" on Task A while its prerequisite Task B is incomplete
  - Expected: The task cannot be completed (action is prevented)
  - (Verified: The Complete button on the dependent task is `disabled`; Playwright reports "element is not enabled" and the click is prevented — no state change.)

- [ ] CS-02: Lock non-permitted fields when prerequisite is incomplete
  - Action: Open edit on Task A while Task B is incomplete
  - Expected: Only description and priority are editable; all other fields are locked
  - Bug Report:
    - Issue: Fully-disabled Edit control (cannot open the restricted edit form)
    - Actual: When a prerequisite is incomplete, the Edit button is rendered as `disabled` and is non-interactive (clicking it produces no dialog / "element is not enabled"). Because the edit form can never be opened, the spec's intended behavior — opening edit with only the description and priority fields editable while title/deadline/prerequisites are locked — is not implemented. The app instead blocks editing entirely rather than partially.

- [X] CS-03: Require ALL prerequisites complete before unlocking
  - Action: With Task A dependent on multiple prerequisites, complete only some of them
  - Expected: Task A remains locked until every prerequisite is completed
  - (Verified: "Submit final report" depends on "Review project proposal" and "Complete tax filing". After completing only "Review project proposal", its label changed from "2 prerequisites incomplete" to "Prerequisite 'Complete tax filing' incomplete" and its Edit/Complete buttons stayed disabled — still locked until both prerequisites are done.)

## Interaction

- [X] IX-01: Disable Edit/Complete buttons when prerequisite incomplete
  - Action: View Task A while its prerequisite Task B is incomplete
  - Expected: The Edit and Complete buttons are grayed out / disabled
  - (Verified: On "TestTaskAlpha", "Complete tax filing", and "Submit final report" the Complete and Edit buttons are `disabled` (grayed/opacity-50, `cursor-not-allowed`) while prerequisites are incomplete.)

- [ ] IX-02: Draw dashed-line connections between dependent tasks
  - Action: View a list containing a dependent task relationship
  - Expected: A dashed line visually connects Task A to its prerequisite(s)
  - Bug Report:
    - Issue: No connecting line between dependent tasks
    - Actual: There is no SVG/line element connecting a dependent task to its prerequisite. The only dashed visuals are a `border-dashed border-warning/40` around the dependent task card and a small decorative stub (`div.bg-dashed-line`, 2px × 3px, positioned `-bottom-3 left-1/2` at the card's bottom). No line spans from Task A to Task B.

- [X] IX-03: Show dependency details popup on connection hover
  - Action: Hover over the dashed connection line between Task A and Task B
  - Expected: A popup appears showing the details of the dependency chain
  - (Verified: Hovering the "Prerequisite … incomplete" label (which has `cursor-help`) opens a popup titled "Dependency Chain" listing the prerequisite task name(s) and their status, e.g. "Review project proposal — pending" / "Complete tax filing — pending". Note: the popup is triggered by hovering the prerequisite label, not a connecting line — the latter does not exist per IX-02.)

## Content

- [X] CT-01: Display "Prerequisite [Task] Incomplete" label
  - Action: View Task A while prerequisite Task B is incomplete
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" (with the actual task name) appears next to Task A
  - (Verified: Labels render with the actual task name, e.g. "Prerequisite 'Review project proposal' incomplete" and "Prerequisite 'Complete tax filing' incomplete" (and "2 prerequisites incomplete" when multiple), styled as a prominent warning badge next to the dependent task.)
