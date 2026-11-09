# Test Checklist

## Functionality
- [ ] FT-01: Team lead can create a new project with all required attributes
  - Action: Open the "New Project" (or equivalent "Create Project") form, enter a project name, select/add required skills, choose a priority, set an expected duration, and submit.
  - Expected: The new project is saved and now appears in the projects list/overview with the entered skills, priority, and duration.

- [ ] FT-02: Team lead can edit an existing project's attributes
  - Action: Open the edit control (e.g., "Edit") on a default project, change its priority and add one required skill, and save.
  - Expected: The project detail/list re-displays the updated priority and the added skill; the change persists when the page is revisited.

- [ ] FT-03: Employee list displays each employee's skills and availability
  - Action: Navigate to the staff/employee list view and inspect several default employee rows/cards.
  - Expected: Every employee entry shows a skills list and an availability status (e.g., "Available" / "Busy" / a percentage or date), not blank or placeholder values.

- [ ] FT-04: Employee list is searchable by name
  - Action: Type the first few characters of a known default employee's name into the search box and apply/trigger the search.
  - Expected: The list narrows to matching employee(s) only; the typed name match is visible in the results.

- [ ] FT-05: Employee list is filterable by skill and/or availability
  - Action: Select a filter (e.g., skill = "React", or availability = "Available") from the filter control.
  - Expected: Only employees matching the selected filter remain in the list, and each result visibly possesses that skill/availability.

- [ ] FT-06: Lead can assign an employee to a project role
  - Action: On a default unstaffed/partially staffed project, use the assignment control (e.g., "Assign" next to an open role), pick an available default employee, and confirm.
  - Expected: The role row now shows the assigned employee's name; the project is listed under that employee's assignments.

- [ ] FT-07: Lead can reassign an employee to a different role or project
  - Action: Take a default employee already assigned to a role, use the reassign control, and move them to a different open role on another project.
  - Expected: The employee appears only in the new role; the original role reverts to "unfilled/open."

- [ ] FT-08: Staffing overview shows the three staffing states for projects
  - Action: Open the overview/dashboard section with default data present.
  - Expected: Each project is visibly labeled "Fully Staffed," "Partially Staffed," or "Unstaffed," and at least projects in differing staffing levels are shown with the correct label relative to their filled vs. open roles.

## Constraint
- [ ] CS-01: Project cannot be saved while required fields are empty
  - Action: Open the "New Project" form, leave required fields (e.g., name, required skills, priority) empty, and attempt to submit.
  - Expected: Submission is blocked, an inline validation message names the missing field(s), and no incomplete project appears in the list.

- [ ] CS-02: Staffing status recalculates automatically when assignments change
  - Action: Starting from a default "Partially Staffed" project, assign employees until all roles are filled, then unassign one employee.
  - Expected: The project's overview label changes to "Fully Staffed" when the last role is filled, and back to "Partially Staffed" after the unassignment — without requiring a manual refresh step.

- [ ] CS-03: An employee cannot remain doubly assigned after reassignment
  - Action: Reassign a default employee from Role A (Project 1) to Role B (Project 2), then inspect both roles and the employee record.
  - Expected: The employee is listed only under Role B; Role A shows no assignment (or "Open"), and the employee record shows exactly one active project assignment.

- [ ] CS-04: Search and filter combine correctly and handle no-match cases
  - Action: With a skill filter active, type a non-existent employee name (e.g., "zzzqqq") in the search box; then clear both.
  - Expected: The list shows an explicit "no results" (or empty-state) message rather than stale rows or an error, and clearing restores the full employee list.

## Interaction
- [ ] IX-01: Success feedback is shown after creating/updating a project
  - Action: Save the "New Project" form, then save an edit on an existing project.
  - Expected: A confirmation appears each time (e.g., success toast/message such as "Project created" / "Project updated") and disappears without requiring a page reload.

- [ ] IX-02: Edit dialog is pre-filled with the project's current values
  - Action: Click "Edit" on a default project and inspect the form before changing anything.
  - Expected: The form opens (modal or inline panel) with the project's current name, skills, priority, and duration already populated; canceling leaves the project unchanged.

- [ ] IX-03: Assignment changes reflect in the UI immediately
  - Action: Assign an employee to a role from the assignment control, then unassign them.
  - Expected: The role row and any staffing label/count update in place right after each action (no stale display, no manual reload required).

- [ ] IX-04: Staffing states are visually distinguishable
  - Action: View the overview with default projects in all three states.
  - Expected: "Fully Staffed," "Partially Staffed," and "Unstaffed" are rendered as distinct visual indicators (e.g., colored badges: green/yellow/red), not identical plain text.

## Content
- [ ] CT-01: Default data is present and relevant on first load
  - Action: Open the page fresh, without adding any data.
  - Expected: At least a few projects (with role slots) and a staff list of multiple employees are pre-loaded, and all content relates to internal project/staff management (no lorem ipsum, no "TODO" placeholders).

- [ ] CT-02: Projects display required skills and expected duration meaningfully
  - Action: Inspect a default project's detail view or list row.
  - Expected: Required skills are shown as concrete, readable skill names (e.g., "SQL," "UX Design") and duration as a value with a unit (e.g., "6 weeks"), not empty or numeric-only fields.

- [ ] CT-03: Priority values are rendered as human-readable labels
  - Action: Check the projects list and the create/edit form.
  - Expected: Priority appears as readable labels (e.g., "High" / "Medium" / "Low") rather than raw codes like "p1"/"0", and the labels used in the form match those shown in the list.