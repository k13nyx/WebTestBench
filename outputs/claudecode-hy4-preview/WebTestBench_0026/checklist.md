# Test Checklist

## Functionality
- [ ] FT-01: Create a new project with required skills, priority, and expected duration
  - Action: Click "New Project"; enter a project name; select at least one required skill (e.g., "React"); select a priority (e.g., "High"); enter an expected duration (e.g., "3"); click "Save".
  - Expected: The project form closes and the new project appears in the project list displaying the entered name, the selected required skill(s), the selected priority, and the entered duration.

- [ ] FT-02: Edit an existing project's details
  - Action: Click "Edit" on a default project; change the priority to a different value and change the expected duration; click "Save".
  - Expected: The project's row/card now shows the new priority and new duration, and the updated values persist after a page reload.

- [ ] FT-03: Employee list displays each employee's skills and availability
  - Action: Open the "Employees" section of the page.
  - Expected: Every employee listed shows a name, at least one skill tag, and an availability value (e.g., "Available" / "Partially Available" / "Unavailable" or available hours).

- [ ] FT-04: Search employees by name
  - Action: Type the full or partial name of a default employee into the employee search field.
  - Expected: The list immediately shows only employees whose name contains the typed text; no unrelated employees remain visible.

- [ ] FT-05: Filter employees by skill
  - Action: Select a skill that at least one default employee has (e.g., "Python") from the skill filter control.
  - Expected: Only employees having that skill are listed; employees without it are removed from view.

- [ ] FT-06: Filter employees by availability
  - Action: Select "Available" from the availability filter control.
  - Expected: Only employees whose availability is "Available" are listed; all others are removed from view.

- [ ] FT-07: Assign an employee to a project role
  - Action: Open a project that has an unfilled role; click "Assign"; choose an employee from the default employee list; confirm the assignment.
  - Expected: The chosen employee's name appears in that role slot, and the project's staffing status in the overview changes accordingly (e.g., from "Unstaffed" to "Partially Staffed" or "Fully Staffed").

- [ ] FT-08: Reassign a role to a different employee
  - Action: Open a project where a role is already filled by Employee A; click "Reassign"; select Employee B; confirm.
  - Expected: The role now displays Employee B, Employee A no longer appears in that role, and the project's staffing status is recalculated and remains correct.

- [ ] FT-09: Remove an employee from a role when project needs change
  - Action: Open a project with a filled role; click "Remove"/"Unassign" on that role.
  - Expected: The role becomes empty/vacant and the project's staffing status downgrades correctly (e.g., "Fully Staffed" → "Partially Staffed", or "Partially Staffed" → "Unstaffed" if it was the only filled role).

## Constraint
- [ ] CS-01: Cannot save a project with missing required fields
  - Action: Open "New Project" and click "Save" without entering a name, without selecting a required skill, without a priority, or without a duration.
  - Expected: The project is not created; the form stays open and displays a validation message (or the "Save" button is disabled) for each missing field.

- [ ] CS-02: Cannot assign an employee lacking the role's required skill
  - Action: Open a role that requires a specific skill; attempt to assign a default employee who does not have that skill; confirm.
  - Expected: The assignment is blocked with a message stating the employee does not have the required skill, and the role remains unfilled/unchanged.

- [ ] CS-03: Cannot assign an employee who is unavailable
  - Action: Attempt to assign a default employee whose availability is "Unavailable" (or 0 available hours) to a project role; confirm.
  - Expected: The assignment is blocked with a message indicating the employee is not available, and the role remains unfilled/unchanged.

- [ ] CS-04: Search or filter with no matching results shows an empty state, not stale data
  - Action: Type a nonsense string (e.g., "zzzzqqq") into the employee search field, or select a skill filter combination no employee matches.
  - Expected: No employee rows are displayed and an empty-state message (e.g., "No employees found") is shown instead of previously loaded results.

- [ ] CS-05: Staffing status invariant — displayed status always matches filled roles
  - Action: Inspect every project in the overview and compare its status label with its filled vs. required roles.
  - Expected: Each project shows "Fully Staffed" only when all required roles are filled, "Partially Staffed" when some but not all are filled, and "Unstaffed" when none are filled; no project shows a contradictory status.

## Interaction
- [ ] IX-01: Editing a project pre-fills the form with its current values
  - Action: Click "Edit" on a default project and inspect the form fields without changing anything.
  - Expected: The name, required skills, priority, and expected duration fields are pre-populated with that project's existing values.

- [ ] IX-02: Success feedback appears after an assignment is saved
  - Action: Complete a valid employee-to-role assignment (FT-07) or reassignment (FT-08) and observe the page.
  - Expected: A confirmation/success notification (e.g., a toast or inline message) appears confirming the assignment, and the assignment list updates without a manual page reload.

- [ ] IX-03: Clearing search text and resetting filters restores the full employee list
  - Action: After applying a search term and a skill filter, clear the search field and reset/clear the filters.
  - Expected: The full default employee list is displayed again with no rows missing.

- [ ] IX-04: Selecting a project from the overview opens its role and assignment detail
  - Action: Click a project entry in the overview section.
  - Expected: That project's detail panel opens/becomes visible showing all its roles, the required skill for each role, and the employees currently assigned (or "Unfilled"/"Vacant" for empty roles).

## Content
- [ ] CT-01: Project cards display correct, complete project data
  - Action: Review each project card/row in the list for its name, required skills, priority, and expected duration.
  - Expected: All fields show real, readable values with no "undefined", "NaN", "null", or placeholder text, and every project's data matches the project's stored details.

- [ ] CT-02: Employee records show accurate skills and availability values
  - Action: Review each employee entry's displayed skill tags and availability value.
  - Expected: Skills and availability are real, non-empty values belonging to that employee; no employee shows blank skills or a generic placeholder for availability.

- [ ] CT-03: Staffing terminology and counts are consistent and correctly rendered
  - Action: Compare the overview labels, counts (e.g., "2 of 3 roles filled"), and status terminology against the project detail view; check that any icons/avatars render.
  - Expected: The labels "Fully Staffed", "Partially Staffed", and "Unstaffed" are used consistently and match the filled-role counts, and no broken-image or missing-icon placeholders appear next to employees or projects.