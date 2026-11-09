# Test Checklist

## Functionality
- [ ] FT-01: Team lead can create a new project with name, required skills, priority, and expected duration.
  - Action: Click "New Project", enter a name, select at least two required skills, set Priority to "High", enter a duration (e.g., 8 weeks), and click "Save".
  - Expected: The project appears in the project list showing the entered name, skills, priority "High", and duration.
- [ ] FT-02: Team lead can edit an existing project's skills, priority, and duration.
  - Action: Open a default project, click "Edit", change one required skill, set Priority to "Low", change the duration, and click "Save".
  - Expected: The project list and project details show the updated skills, priority "Low", and new duration.
- [ ] FT-03: Employee search returns matching employees by name.
  - Action: Type a full name of a default employee into the "Search employees" field.
  - Expected: The employee list shows only employees whose name matches the search text.
- [ ] FT-04: Skill filter limits the employee list to employees with that skill.
  - Action: Open the "Skill" filter and select a skill held by some default employees (e.g., "Python").
  - Expected: Every listed employee has the selected skill in their skills column, and no employee without that skill is shown.
- [ ] FT-05: Availability filter limits the employee list to employees with the selected availability.
  - Action: Set the "Availability" filter to "Available".
  - Expected: Every listed employee shows availability "Available"; employees marked otherwise are not shown.
- [ ] FT-06: Team lead can assign an available employee to an open project role.
  - Action: Select an unassigned, available employee, click "Assign", choose a project with an open role, and click "Confirm".
  - Expected: The employee is listed under that project role, and the project's filled-role count increases by one.
- [ ] FT-07: Team lead can reassign an assigned employee to a different project role.
  - Action: On an employee already assigned to a role, click "Reassign", select a different project role, and click "Confirm".
  - Expected: The employee no longer appears in the original role and appears only in the new role.
- [ ] FT-08: Overview groups all projects under "Fully staffed", "Partially staffed", and "Unstaffed" headings.
  - Action: Open the staffing overview section on the page.
  - Expected: Three groups are displayed with those exact headings, and every default project appears in exactly one group.

## Constraint
- [ ] CS-01: Project cannot be saved with a blank required field.
  - Action: Click "New Project", leave "Project Name" empty, fill the other fields, and click "Save".
  - Expected: Save is blocked, an inline error "Project name is required" appears, and no project is created.
- [ ] CS-02: Employee marked "Unavailable" cannot be assigned to a project role.
  - Action: Select a default employee whose availability is "Unavailable" and click "Assign".
  - Expected: Assignment is rejected with the message "Employee is unavailable", and the employee is not added to any role.
- [ ] CS-03: A project role cannot hold more employees than its required headcount.
  - Action: Attempt to assign a further employee to a project role that is already at its required headcount.
  - Expected: Assignment is rejected with the message "Role is already fully staffed", and the role's count is unchanged.
- [ ] CS-04: Expected duration must be a positive number.
  - Action: Open "Edit" on a default project, enter "0" in the duration field, and click "Save". Repeat with "-3".
  - Expected: Each save is blocked with the message "Duration must be greater than 0", and the previous duration remains.

## Interaction
- [ ] IX-01: A success toast confirms when a project is saved.
  - Action: Create or edit a project with valid values and click "Save".
  - Expected: A toast reading "Project saved" appears near the top of the page and disappears automatically within about 5 seconds.
- [ ] IX-02: Search with no matches shows an empty-state message, and clearing the search restores the list.
  - Action: Type "zzzz" in "Search employees", then clear the field.
  - Expected: The list shows "No employees match your filters" while the text is entered, and the full employee list returns when the field is cleared.
- [ ] IX-03: Overview status updates immediately after an assignment changes.
  - Action: Assign an employee to the last open role of a "Partially staffed" project without reloading the page.
  - Expected: The project moves to the "Fully staffed" group in the overview, and its status label updates without a page refresh.
- [ ] IX-04: Reassignment asks for confirmation, and cancelling leaves the assignment unchanged.
  - Action: Click "Reassign" on an assigned employee, select a new role, then click "Cancel" in the confirmation dialog.
  - Expected: A dialog reading "Reassign [employee] from [old role] to [new role]?" appears with "Cancel" and "Confirm" buttons, and after cancelling the employee remains in the original role.

## Content
- [ ] CT-01: Employee skills and availability shown in the list match each employee's default profile.
  - Action: Compare the skills and availability of three default employees in the list with their individual profile views.
  - Expected: Skills and availability values are identical in both views for every compared employee.
- [ ] CT-02: Every default project row displays all four fields with no placeholder text.
  - Action: Review the project list for all default projects.
  - Expected: Each row shows a name, at least one required skill, a priority of Low/Medium/High, and a duration; no row contains "undefined", "null", "NaN", or blank values.
- [ ] CT-03: Staffing status labels agree with the number of filled roles for each project.
  - Action: For each default project, compare filled roles against required roles in the project details, then check its label in the overview.
  - Expected: "Fully staffed" when all roles are filled, "Partially staffed" when some are filled, and "Unstaffed" when none are filled; labels match the role counts for every project.
- [ ] CT-04: Skill filter options match the skills held by default employees, with no duplicates.
  - Action: Open the "Skill" filter dropdown and compare its options with the skills listed across all default employees.
  - Expected: Each skill appears exactly once, every option is held by at least one employee, and no employee skill is missing from the options.