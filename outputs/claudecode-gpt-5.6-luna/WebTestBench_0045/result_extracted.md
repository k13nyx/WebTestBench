# Test Result

## Functionality

- [X] **FT-01: Add a task with a title, optional description, deadline, and priority**
  - **Action:** Use the task-entry form to enter a title, leave the description empty, set a deadline and priority, then save.
  - **Expected:** The task appears in the task list with the entered title, deadline, and priority; the empty description is accepted.

- [X] **FT-02: Edit an existing task**
  - **Action:** Select **Edit** for an available task, change its title, description, deadline, or priority, and save.
  - **Expected:** The task displays the updated values and no longer shows the previous values.

- [X] **FT-03: Mark a task as completed without deleting it**
  - **Action:** Select **Complete** for an active task.
  - **Expected:** The task remains in the list and is visibly marked as completed.

- [X] **FT-04: Delete a task**
  - **Action:** Select **Delete** for an available task and confirm the deletion if prompted.
  - **Expected:** The task is removed from the task list and is no longer available as an active or completed task.

- [X] **FT-05: View active tasks first**
  - **Action:** Use the available active-task view, filter, or ordering control.
  - **Expected:** Active tasks are shown before completed tasks, or completed tasks are excluded when an active-only view is selected.

- [X] **FT-06: Sort tasks by priority**
  - **Action:** Select the priority sorting option.
  - **Expected:** Tasks are displayed in the order defined by the available priority levels.

- [X] **FT-07: Sort tasks by deadline**
  - **Action:** Select the deadline sorting option.
  - **Expected:** Tasks are displayed in chronological deadline order.

- [X] **FT-08: Assign one or more prerequisite tasks**
  - **Action:** Create or edit a task and select one or more existing tasks as prerequisites, then save.
  - **Expected:** The selected prerequisite relationships are saved and displayed for the dependent task.

- [X] **FT-09: Unlock a dependent task after prerequisites are completed**
  - **Action:** Complete every prerequisite task for a dependent task.
  - **Expected:** The dependent task becomes available for editing and completion.

## Constraint

- [X] **CS-01: Prevent saving a task without a title**
  - **Action:** Open the task-entry form, leave the title empty, and attempt to save.
  - **Expected:** The task is not saved, and the interface identifies the title as required.

- [ ] **CS-02: Restrict an incomplete dependent task**
  - **Action:** For Task A with an incomplete prerequisite Task B, inspect and attempt to use Task A’s controls.
  - **Expected:** Task A’s **Edit** and **Complete** buttons are grayed out; only its description and priority fields remain available for modification.
  - **Bug Report:**
    - **Issue:** Dependent task fields are not available for the permitted modifications.
    - **Actual:** For an incomplete dependent task, both the Complete and Edit buttons were disabled. The task could not be opened to modify its description or priority; only the Delete control remained enabled.

- [X] **CS-03: Keep a task locked while any prerequisite is incomplete**
  - **Action:** For a task with multiple prerequisites, leave at least one prerequisite incomplete and inspect the dependent task.
  - **Expected:** The dependent task remains unavailable for editing and completion until all prerequisites are completed.

- [X] **CS-04: Prevent completion before prerequisites are complete**
  - **Action:** Attempt to complete a dependent task while at least one prerequisite is incomplete.
  - **Expected:** The task does not become completed.

## Interaction

- [ ] **IX-01: Display the incomplete-prerequisite label**
  - **Action:** View Task A while prerequisite Task B is incomplete.
  - **Expected:** A prominent label reading exactly **“Prerequisite Task B Incomplete”** appears next to Task A.
  - **Bug Report:**
    - **Issue:** Incomplete-prerequisite label text does not match the required wording.
    - **Actual:** The interface displayed labels such as `Prerequisite "Schedule dentist appointment" incomplete` and `Prerequisite "Review project proposal" incomplete`, rather than the exact required format `Prerequisite Task B Incomplete`.

- [X] **IX-02: Update dependency controls after prerequisite completion**
  - **Action:** Complete Task B while viewing dependent Task A.
  - **Expected:** Task A’s grayed-out **Edit** and **Complete** buttons become enabled without requiring a page refresh.

- [ ] **IX-03: Show visual connections between dependent tasks**
  - **Action:** View tasks that have prerequisite relationships.
  - **Expected:** The related tasks are connected by visible dashed lines.
  - **Bug Report:**
    - **Issue:** Dependency connections are not rendered as dashed lines.
    - **Actual:** DOM inspection found no dashed borders, dashed SVG strokes, connector elements, or visible line elements connecting the related tasks.

- [X] **IX-04: Open dependency details on hover**
  - **Action:** Hover over the dashed connection between dependent tasks.
  - **Expected:** A pop-up window appears showing the dependency chain details.

## Content

- [X] **CT-01: Preserve task information accurately**
  - **Action:** Compare each task’s displayed title, description, deadline, priority, and completion state with the values entered or saved.
  - **Expected:** Every displayed value matches the corresponding task data.

- [ ] **CT-02: Show accurate dependency-chain details**
  - **Action:** Hover over a dependency connection and inspect the pop-up contents.
  - **Expected:** The pop-up identifies the correct dependent task, prerequisite task or tasks, and their current completion states.
  - **Bug Report:**
    - **Issue:** Dependency-chain pop-up omits required task identity and completion-state information.
    - **Actual:** The tooltip listed prerequisite names such as `Review project proposal` and `Complete tax filing`, but did not identify the dependent task or display the current completion states of the tasks.
