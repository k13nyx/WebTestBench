# Test Checklist

## Functionality
- [ ] FT-01: Add a task with title, description, deadline, and priority
  - Action: Enter a title (e.g., "Write report"), a description, pick a deadline date, select a priority (e.g., High), then click the Add/Submit button.
  - Expected: A new task appears in the list showing the entered title, description, deadline, and priority.

- [ ] FT-02: Task can be added with description left blank (description is optional)
  - Action: Fill in only the title (and optionally deadline/priority), leave the description field empty, click Add.
  - Expected: The task is created successfully with no error; an empty description is accepted.

- [ ] FT-03: Edit an unblocked task and save changes
  - Action: Click the Edit button on a task that has no incomplete prerequisites; modify its title, description, deadline, and priority; save.
  - Expected: The task row updates to display all newly saved values.

- [ ] FT-04: Mark a task as completed without losing it
  - Action: Click the Complete button/checkbox on an independent task.
  - Expected: The task is shown as completed (e.g., checked/strikethrough) and remains present in the list; it is not deleted.

- [ ] FT-05: Delete a task
  - Action: Click the Delete button on any task.
  - Expected: The task is permanently removed from the list and no longer appears in any view.

- [ ] FT-06: View active tasks first
  - Action: Use the provided view control (e.g., "Active" tab/filter or default ordering).
  - Expected: Incomplete (active) tasks are displayed above/first; completed tasks are still reachable (e.g., under a "Completed" view) rather than hidden permanently.

- [ ] FT-07: Sort the task list by priority
  - Action: Choose the "Sort by Priority" option.
  - Expected: Tasks reorder strictly by priority level (e.g., High → Medium → Low).

- [ ] FT-08: Sort the task list by deadline
  - Action: Choose the "Sort by Deadline" option.
  - Expected: Tasks reorder by deadline date (earliest deadline first).

- [ ] FT-09: Bind one or more prerequisite tasks to a task
  - Action: For default task A, use the dependency control to bind prerequisite task B and also prerequisite task C; save.
  - Expected: Both dependencies are registered — A is blocked by each incomplete prerequisite and connections for both are rendered.

## Constraint
- [ ] CS-01: Edit and Complete buttons are grayed out while a prerequisite is incomplete
  - Action: With task B incomplete, inspect dependent task A and attempt to click A's Edit and Complete buttons.
  - Expected: Both buttons appear grayed/disabled; clicking them does nothing — no edit form opens and A cannot be completed.

- [ ] CS-02: Only description and priority are modifiable on a blocked task
  - Action: On blocked task A (prerequisite B incomplete), attempt to modify the description and priority, then attempt title/deadline changes.
  - Expected: Description and priority changes are accepted and saved; title and deadline cannot be changed, and the full Edit form remains inaccessible.

- [ ] CS-03: Completing the prerequisite unblocks the dependent task
  - Action: Complete prerequisite task B.
  - Expected: Task A's Edit and Complete buttons become enabled, and the "Prerequisite Task B Incomplete" label next to A disappears.

- [ ] CS-04: Task cannot be added without a title
  - Action: Leave the title field empty and click Add.
  - Expected: Submission is rejected with a visible validation message; no new task is created.

- [ ] CS-05: A task unlocks only when ALL its prerequisites are completed
  - Action: With A bound to prerequisites B and C (both incomplete), complete only B and inspect A; then complete C and inspect A again.
  - Expected: After B alone is completed, A remains blocked (label still shown, buttons disabled); only after C is also completed does A unlock.

## Interaction
- [ ] IX-01: Dependent tasks are visually connected by dashed lines
  - Action: With task A bound to prerequisite B, view the task list/graph area.
  - Expected: A dashed line is drawn connecting task B's entry to task A's entry, clearly distinguishing the dependency link from normal content.

- [ ] IX-02: Hovering over a dashed connection opens a dependency pop-up
  - Action: Hover the mouse cursor over the dashed line between B and A; then move the cursor away.
  - Expected: A pop-up window appears showing the dependency chain details (the prerequisite → dependent relationship); the pop-up closes when the hover ends.

## Content
- [ ] CT-01: Prominent blocking label with exact wording
  - Action: View dependent task A while prerequisite task B is incomplete.
  - Expected: A prominent label reading "Prerequisite Task B Incomplete" (referencing the prerequisite task's title) is displayed next to task A, visually distinct (e.g., bold/colored).

- [ ] CT-02: Task card displays all required fields accurately
  - Action: Inspect a default task's row after adding/editing.
  - Expected: Title, description, deadline, and priority are all displayed and match exactly what was entered — no missing, truncated, or placeholder content.

- [ ] CT-03: Dependency pop-up content is relevant and correct
  - Action: Hover the dashed connection between B and A and read the pop-up contents.
  - Expected: The pop-up shows the actual tasks in the chain (B and A titles) and their completion status — information directly relevant to that dependency, with no unrelated or placeholder text.