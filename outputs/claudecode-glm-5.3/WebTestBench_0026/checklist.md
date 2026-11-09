# Test Checklist

## Functionality
- [ ] FT-01: Team lead can create a new project with all required attributes
  - Action: Open the "New Project" form, enter a project name, select at least one required skill, set a priority (e.g., High/Medium/Low), enter an expected duration (e.g., 6 weeks), and submit.
  - Expected: The project is created and appears in the project list displaying the entered name, skills, priority, and duration exactly as entered.

- [ ] FT-02: Team lead can edit an existing project's details
  - Action: Select an existing project from the list, change its priority and expected duration, and save.
  - Expected: The project list shows the updated priority and duration for that project after saving.

- [ ] FT-03: Team lead can search the employee list
  - Action: Type the name (or partial name) of an existing employee into the employee search box.
  - Expected: The employee list narrows to show only employees matching the search text; the matching employee is visible.

- [ ] FT-04: Team lead can filter the employee list by skill and availability
  - Action: Apply a skill filter (e.g., a skill that at least one default employee has) and an availability filter (e.g., "Available").
  - Expected: Only employees with the selected skill and the selected availability status are shown; employees not matching are hidden.

- [ ] FT-05: Team lead can assign an available employee to a project role
  - Action: Open a project with an unfilled role and assign an employee who is marked available and has a matching skill.
  - Expected: The employee is listed as the assignee for that role on the project.

- [ ] FT-06: Team lead can reassign an employee from one project role to another
  - Action: Remove (or change) an existing assignment so the employee moves from their current project role to a different unfilled role.
  - Expected: The employee appears under the new role and no longer appears under the previous role.

- [ ] FT-07: Team lead can unassign an employee from a project role
  - Action: Remove an assigned employee from a project role.
  - Expected: The role shows as unfilled and the employee no longer appears as assigned to that project; the employee shows as available again.

- [ ] FT-08: Project overview reflects correct staffing status after each change
  - Action: Check a project with all roles filled, one with some roles filled, and one with no roles filled.
  - Expected: The overview labels them "Fully Staffed", "Partially Staffed", and "Unstaffed" respectively.

## Constraint
- [ ] CS-01: Project cannot be created with empty required fields
  - Action: Open the "New Project" form and submit it with the name, required skills, priority, or duration left empty.
  - Expected: The project is not created, is not added to the project list, and the empty fields are indicated as required.

- [ ] CS-02: Employee cannot be assigned to a role while unavailable
  - Action: Attempt to assign an employee whose availability status is not "Available" to an unfilled project role.
  - Expected: The assignment is rejected and the employee is not added to the role; the system indicates the employee is unavailable.

- [ ] CS-03: The same employee cannot be assigned to the same project role twice
  - Action: Attempt to assign an employee who already fills a role on the same project to that role again (or a second slot of the same role).
  - Expected: The duplicate assignment is rejected and the employee appears only once in the project's assignments.

- [ ] CS-04: Project staffing status cannot exceed its defined roles
  - Action: Attempt to assign more employees to a project than it has defined roles.
  - Expected: No assignment beyond the number of defined roles is possible; the project's assignment count does not exceed its role count.

- [ ] CS-05: Employee cannot hold conflicting simultaneous assignments beyond availability
  - Action: Attempt to assign an already fully-assigned employee to an additional project role.
  - Expected: The additional assignment is blocked and the employee's existing assignments remain unchanged.

## Interaction
- [ ] IX-01: Confirmation feedback is shown after creating or editing a project
  - Action: Create a new project (then edit it) with valid data.
  - Expected: A visible success message (toast/banner) confirms the project was created and then updated.

- [ ] IX-02: Staffing status label updates immediately after an assignment change
  - Action: On a "Partially Staffed" project, fill its last open role.
  - Expected: The project's status label changes to "Fully Staffed" without requiring a page reload.

- [ ] IX-03: Employee search updates results dynamically
  - Action: Type a search term with no matches, then clear the search box.
  - Expected: A "no results" indicator appears for the unmatched term, and clearing the search restores the full employee list.

- [ ] IX-04: Assignment changes are reflected on the employee list
  - Action: Assign an employee to a project role, then view the employee list.
  - Expected: That employee's availability/status is updated (e.g., shown as assigned/busy) without a manual refresh.

## Content
- [ ] CT-01: Each employee entry shows complete, relevant details
  - Action: Inspect every default employee in the employee list.
  - Expected: Each entry displays the employee's name, their skills, and their current availability status; no employee entry is missing any of these.

- [ ] CT-02: Each project entry shows complete, relevant details
  - Action: Inspect every project in the project list/overview.
  - Expected: Each project displays its name, required skills, priority, expected duration, and staffing status; no project entry is missing any of these.

- [ ] CT-03: Staffing status labels match actual assignment state
  - Action: Compare each project's staffing label against its filled vs. total roles in the default data.
  - Expected: Projects with all roles filled are labeled "Fully Staffed", projects with some roles filled are labeled "Partially Staffed", and projects with no filled roles are labeled "Unstaffed" — with no mismatches.