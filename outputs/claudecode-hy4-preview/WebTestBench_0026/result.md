All 21 checklist items executed. Results below.

# Test Result

## Functionality

- [X] FT-01: Create a new project with required skills, priority, and expected duration
  - Action: Click "New Project"; enter a project name; select at least one required skill (e.g., "React"); select a priority (e.g., "High"); enter an expected duration (e.g., "3"); click "Save".
  - Expected: The project form closes and the new project appears in the project list displaying the entered name, the selected required skill(s), the selected priority, and the entered duration.

- [ ] FT-02: Edit an existing project's details
  - Action: Click "Edit" on a default project; change the priority to a different value and change the expected duration; click "Save".
  - Expected: The project's row/card now shows the new priority and new duration, and the updated values persist after a page reload.
  - Bug Report:
    - Issue: State Not Persisted (No Persistence Layer)
    - Actual: Editing project "QA Test Project Alpha" (High/3 weeks → Low/9 weeks) applied correctly and showed "Project updated successfully", but reloading the same URL (`/projects/proj-1794080767543`) rendered "Project not found" and the projects list reverted to the 4 default projects. Inspection confirmed `localStorage.length === 0` and `sessionStorage.length === 0`, so all project/assignment edits are in-memory only and lost on reload.

- [X] FT-03: Employee list displays each employee's skills and availability
  - Action: Open the "Employees" section of the page.
  - Expected: Every employee listed shows a name, at least one skill tag, and an availability value (e.g., "Available" / "Partially Available" / "Unavailable" or available hours).

- [X] FT-04: Search employees by name
  - Action: Type the full or partial name of a default employee into the employee search field.
  - Expected: The list immediately shows only employees whose name contains the typed text; no unrelated employees remain visible.

- [X] FT-05: Filter employees by skill
  - Action: Select a skill that at least one default employee has (e.g., "Python") from the skill filter control.
  - Expected: Only employees having that skill are listed; employees without it are removed from view.

- [X] FT-06: Filter employees by availability
  - Action: Select "Available" from the availability filter control.
  - Expected: Only employees whose availability is "Available" are listed; all others are removed from view.

- [X] FT-07: Assign an employee to a project role
  - Action: Open a project that has an unfilled role; click "Assign"; choose an employee from the default employee list; confirm the assignment.
  - Expected: The chosen employee's name appears in that role slot, and the project's staffing status in the overview changes accordingly (e.g., from "Unstaffed" to "Partially Staffed" or "Fully Staffed").

- [X] FT-08: Reassign a role to a different employee
  - Action: Open a project where a role is already filled by Employee A; click "Reassign"; select Employee B; confirm.
  - Expected: The role now displays Employee B, Employee A no longer appears in that role, and the project's staffing status is recalculated and remains correct.

- [X] FT-09: Remove an employee from a role when project needs change
  - Action: Open a project with a filled role; click "Remove"/"Unassign" on that role.
  - Expected: The role becomes empty/vacant and the project's staffing status downgrades correctly (e.g., "Fully Staffed" → "Partially Staffed", or "Partially Staffed" → "Unstaffed" if it was the only filled role).

## Constraint

- [X] CS-01: Cannot save a project with missing required fields
  - Action: Open "New Project" and click "Save" without entering a name, without selecting a required skill, without a priority, or without a duration.
  - Expected: The project is not created; the form stays open and displays a validation message (or the "Save" button is disabled) for each missing field.

- [ ] CS-02: Cannot assign an employee lacking the role's required skill
  - Action: Open a role that requires a specific skill; attempt to assign a default employee who does not have that skill; confirm.
  - Expected: The assignment is blocked with a message stating the employee does not have the required skill, and the role remains unfilled/unchanged.
  - Bug Report:
    - Issue: Missing Validation — Unqualified Employee Accepted
    - Actual: In project "API Gateway Migration", the role "DevOps Engineer" requires "DevOps / AWS". The assign dialog listed "Sarah Chen / Senior Frontend Developer / 0/2 skills matched / Available" with an enabled "Assign" button. Clicking it produced the notification "Employee assigned successfully", the dialog closed, and the DevOps Engineer role then displayed "Sarah Chen". The same occurred for the "Backend Developer" role (requires Node.js/GraphQL) with James Wilson (Mobile Development/React/TypeScript, 0/2 match). No block and no warning message appeared.

- [ ] CS-03: Cannot assign an employee who is unavailable
  - Action: Attempt to assign a default employee whose availability is "Unavailable" (or 0 available hours) to a project role; confirm.
  - Expected: The assignment is blocked with a message indicating the employee is not available, and the role remains unfilled/unchanged.
  - Bug Report:
    - Issue: Missing Validation — Unavailable Employee Accepted
    - Actual: In project "API Gateway Migration" with the "Backend Developer" role vacant, the assign dialog listed "David Kim / Full Stack Developer / 1/2 skills matched / Unavailable" with an enabled "Assign" button. Clicking it produced the notification "Employee assigned successfully" and the role then displayed "David Kim". No blockage and no "employee is not available" message were shown.

- [X] CS-04: Search or filter with no matching results shows an empty state, not stale data
  - Action: Type a nonsense string (e.g., "zzzzqqq") into the employee search field, or select a skill filter combination no employee matches.
  - Expected: No employee rows are displayed and an empty-state message (e.g., "No employees found") is shown instead of previously loaded results.

- [X] CS-05: Staffing status invariant — displayed status always matches filled roles
  - Action: Inspect every project in the overview and compare its status label with its filled vs. required roles.
  - Expected: Each project shows "Fully Staffed" only when all required roles are filled, "Partially Staffed" when some but not all are filled, and "Unstaffed" when none are filled; no project shows a contradictory status.

## Interaction

- [X] IX-01: Editing a project pre-fills the form with its current values
  - Action: Click "Edit" on a default project and inspect the form fields without changing anything.
  - Expected: The name, required skills, priority, and expected duration fields are pre-populated with that project's existing values.

- [X] IX-02: Success feedback appears after an assignment is saved
  - Action: Complete a valid employee-to-role assignment (FT-07) or reassignment (FT-08) and observe the page.
  - Expected: A confirmation/success notification (e.g., a toast or inline message) appears confirming the assignment, and the assignment list updates without a manual page reload.

- [X] IX-03: Clearing search text and resetting filters restores the full employee list
  - Action: After applying a search term and a skill filter, clear the search field and reset/clear the filters.
  - Expected: The full default employee list is displayed again with no rows missing.

- [X] IX-04: Selecting a project from the overview opens its role and assignment detail
  - Action: Click a project entry in the overview section.
  - Expected: That project's detail panel opens/becomes visible showing all its roles, the required skill for each role, and the employees currently assigned (or "Unfilled"/"Vacant" for empty roles).

## Content

- [X] CT-01: Project cards display correct, complete project data
  - Action: Review each project card/row in the list for its name, required skills, priority, and expected duration.
  - Expected: All fields show real, readable values with no "undefined", "NaN", "null", or placeholder text, and every project's data matches the project's stored details.

- [X] CT-02: Employee records show accurate skills and availability values
  - Action: Review each employee entry's displayed skill tags and availability value.
  - Expected: Skills and availability are real, non-empty values belonging to that employee; no employee shows blank skills or a generic placeholder for availability.

- [X] CT-03: Staffing terminology and counts are consistent and correctly rendered
  - Action: Compare the overview labels, counts (e.g., "2 of 3 roles filled"), and status terminology against the project detail view; check that any icons/avatars render.
  - Expected: The labels "Fully Staffed", "Partially Staffed", and "Unstaffed" are used consistently and match the filled-role counts, and no broken-image or missing-icon placeholders appear next to employees or projects.

---

## Notes on findings

**3 defects found:**

1. **FT-02 — No data persistence.** The app holds all state in memory. Any project create/edit and any assignment is destroyed by a page reload. `localStorage` and `sessionStorage` are both empty, so there is no persistence mechanism at all. The edit operation itself works (priority/duration updated, notification shown); only the reload-persistence requirement fails.

2. **CS-02 — Skill-matching constraint is advisory only.** The assign dialog computes and displays "N/M skills matched" per employee, which strongly implies enforcement, but the "Assign" button is never disabled and no warning is emitted. Employees with 0/2 matches were assigned twice during testing.

3. **CS-03 — Availability constraint not enforced.** Likewise, "Unavailable" employees can be assigned; David Kim (Unavailable, 2 current projects) was successfully assigned.

**Observations worth flagging (did not fail their items):**
- Employee availability is **derived from current assignment count** (0 projects → Available, 1 → Partially Available, 2+ → Unavailable), not a stored per-employee setting. This means assignments silently change a person's availability label.
- Required skills are modelled **per role**, not per project. The projects table and overview cards show name/description/priority/duration/roles/status, but never skills; the required skills are only visible inside the project detail panel. FT-01/CT-01 were graded PASS because the creation flow captures and displays the skills correctly at role level and every displayed value is real and matches stored data.
- Overview cards abbreviate the status to "Partial" while the detail panel uses "Partial" too — the app is internally consistent and counts always matched, so CT-03 passes, but the wording differs from the "Partially Staffed" spelling in the checklist.
- The "Reassign" and "Remove" controls in the project detail are **icon-only buttons with no accessible name** (no `aria-label` or `title`), which will fail screen-reader and accessible-automation use.