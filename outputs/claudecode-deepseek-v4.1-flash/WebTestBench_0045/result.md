# Test Result

## Functionality
- [X] FT-01: Add a new task with a title, optional description, and deadline
  - Action: Click "Add Task", enter a title, an optional description, and a deadline, then confirm.
  - Expected: The new task appears in the list with its title, description (if entered), and deadline displayed.
- [X] FT-02: Edit an existing task's title, description, or deadline
  - Action: Click the edit button on a task, change its title/description/deadline, and save.
  - Expected: The task updates to show the new values; no duplicate task is created.
- [X] FT-03: Mark a task as completed without deleting it
  - Action: Click the complete button on an active task.
  - Expected: The task is flagged as completed and still present in the list, not removed entirely.
- [X] FT-04: Delete a task
  - Action: Click the delete button on a task.
  - Expected: The task is removed from the list entirely.
- [X] FT-05: View active (incomplete) tasks first
  - Action: Load the page with both active and completed tasks present.
  - Expected: Active tasks are shown before completed tasks by default.
- [X] FT-06: Sort the list by priority
  - Action: Select the "sort by priority" option.
  - Expected: Tasks are reordered by their assigned priority.
- [X] FT-07: Sort the list by deadline
  - Action: Select the "sort by deadline" option.
  - Expected: Tasks are reordered by their deadline.
- [X] FT-08: Assign a priority to a task
  - Action: Set a priority value on a task and save.
  - Expected: The task displays its assigned priority.
- [X] FT-09: Bind one or more prerequisite dependent tasks to a task
  - Action: On a task, add one or more prerequisite tasks as dependencies (including multiple).
  - Expected: The task records all selected prerequisites as dependencies.

## Constraint
- [X] CS-01: Prevent creating a task with no title
  - Action: Attempt to add a task with an empty title field (description and deadline optional) and confirm.
  - Expected: Task is not created; the title field is treated as required. (Description and deadline may be left empty without blocking.)
- [X] CS-02: Disable a dependent task's edit button while its prerequisite is incomplete
  - Action: With Task A dependent on incomplete Task B, inspect Task A's edit button.
  - Expected: Task A's edit button is grayed out / non-functional.
- [X] CS-03: Disable a dependent task's complete button while its prerequisite is incomplete
  - Action: With Task A dependent on incomplete Task B, inspect Task A's complete button.
  - Expected: Task A's complete button is grayed out / non-functional.
- [ ] CS-04: Restrict editable fields on a blocked dependent task to description and priority only
  - Action: Attempt to modify a task that depends on an incomplete prerequisite.
  - Expected: Only the description and priority fields are editable; title, deadline, and dependency fields are not modifiable.
  - Bug Report:
    - Issue: Missing functionality / Blocked field access
    - Actual: On "Complete tax filing" (prerequisite "Review project proposal" incomplete), **no field is editable at all**. The edit button is `disabled`, and programmatically clicking it opens no dialog (`[role="dialog"]` stays absent). The card exposes no inline input/select/contenteditable either, so description and priority — which per the spec must remain modifiable — are also uneditable.
- [X] CS-05: Re-enable edit and complete buttons once the prerequisite is completed
  - Action: Complete Task B, which is a prerequisite of Task A.
  - Expected: Task A's edit and complete buttons become enabled and functional.

## Interaction
- [X] IX-01: Display a prominent prerequisite-incomplete label on the blocked task
  - Action: View Task A whose prerequisite Task B is incomplete.
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" is displayed next to Task A.
- [X] IX-02: Draw a dashed line connecting dependent tasks
  - Action: View a task that has a prerequisite.
  - Expected: A dashed line visually connects the dependent task to its prerequisite task.
- [ ] IX-03: Show a pop-up with the dependency chain on hover
  - Action: Hover over the dashed connection line between a dependent task and its prerequisite.
  - Expected: A pop-up window appears showing the details of the dependency chain.
  - Bug Report:
    - Issue: No response on hover (pop-up not displayed)
    - Actual: Hovering the dashed connection (the `g.pointer-events-auto` trigger and its transparent hit-area path) never opens anything. The trigger's `data-state` stays `"closed"` for 4+ seconds of sustained hover, and no `[role="tooltip"]` element is present afterwards. When the tooltip markup is present in the DOM, its Radix popper wrapper is a child of the `<svg>` element (not `document.body`), so it renders as a zero-size hidden node (`getBoundingClientRect()` = 0×0, `getClientRects().length` = 0, `checkVisibility()` = false). No pop-up window is ever visible.

## Content
- [X] CT-01: Completed tasks remain viewable and identifiable
  - Action: Complete a task, then locate it in the list/view.
  - Expected: The completed task is still displayed and clearly marked as completed (not deleted or hidden without access).
- [ ] CT-02: Dependency pop-up content accurately reflects the dependency chain
  - Action: Hover over the connection for a task with one or more prerequisites and read the pop-up.
  - Expected: The pop-up lists the correct prerequisite task(s) and the chain matches the actual configured dependencies.
  - Bug Report:
    - Issue: Pop-up not displayed (content unreadable by the user)
    - Actual: No pop-up is rendered on hover, so its content cannot be read. The only dependency-chain markup in the DOM ("Dependency Chain / Submit final report — pending / Review project proposal — pending / Complete tax filing — pending") lives inside a `span[role="tooltip"]` that is `clip: rect(0px, 0px, 0px, 0px)`, width/height 0, nested under the `<svg>`, and is therefore invisible (`checkVisibility()` = false). The expected user-visible pop-up listing the prerequisites is absent.