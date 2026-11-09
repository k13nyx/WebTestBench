# Test Result

**Run summary:** Ran about 90 Playwright tool calls against http://localhost:6026/. Several items could not be run exactly as written, so I mapped them to the nearest UI control and noted it. Side effects: I created "QA Test Project", set Customer Portal Redesign to Low and a 1-week duration, changed its UX Designer role to DevOps, and left Sarah Chen assigned to Data Analytics Dashboard. Michael Brown was unassigned during testing.

## Functionality

- [ ] FT-01: Team lead can create a new project with name, required skills, priority, and expected duration.
  - Action: Click "New Project", enter a name, select at least two required skills, set Priority to "High", enter a duration (e.g., 8 weeks), and click "Save".
  - Expected: The project appears in the project list showing the entered name, skills, priority "High", and duration.
  - Bug Report:
    - Issue: Missing Data Display (skills not shown in list)
    - Actual: The project was created and the row shows "QA Test Project", "High", and "8 weeks". The row has no skills text. The dialog's button is "Create Project", not "Save". Skills were entered at role level (React, TypeScript), and the project detail page was not checked for the new project.
- [X] FT-02: Team lead can edit an existing project's skills, priority, and duration.
  - Action: Open a default project, click "Edit", change one required skill, set Priority to "Low", change the duration, and click "Save".
  - Expected: The project list and project details show the updated skills, priority "Low", and new duration.
- [X] FT-03: Employee search returns matching employees by name.
  - Action: Type a full name of a default employee into the "Search employees" field.
  - Expected: The employee list shows only employees whose name matches the search text.
- [X] FT-04: Skill filter limits the employee list to employees with that skill.
  - Action: Open the "Skill" filter and select a skill held by some default employees (e.g., "Python").
  - Expected: Every listed employee has the selected skill in their skills column, and no employee without that skill is shown.
- [X] FT-05: Availability filter limits the employee list to employees with the selected availability.
  - Action: Set the "Availability" filter to "Available".
  - Expected: Every listed employee shows availability "Available"; employees marked otherwise are not shown.
- [X] FT-06: Team lead can assign an available employee to an open project role.
  - Action: Select an unassigned, available employee, click "Assign", choose a project with an open role, and click "Confirm".
  - Expected: The employee is listed under that project role, and the project's filled-role count increases by one.
- [ ] FT-07: Team lead can reassign an assigned employee to a different project role.
  - Action: On an employee already assigned to a role, click "Reassign", select a different project role, and click "Confirm".
  - Expected: The employee no longer appears in the original role and appears only in the new role.
  - Bug Report:
    - Issue: Missing Feature (no reassign control)
    - Actual: No "Reassign" control exists. Each assigned employee's role offers only an assignment dialog for that same role, with an "Unassign" button, and a second icon that unassigns immediately. No option to pick a different role was found.
- [ ] FT-08: Overview groups all projects under "Fully staffed", "Partially staffed", and "Unstaffed" headings.
  - Action: Open the staffing overview section on the page.
  - Expected: Three groups are displayed with those exact headings, and every default project appears in exactly one group.
  - Bug Report:
    - Issue: Missing Element (no group headings)
    - Actual: The Projects page and Dashboard "Projects Overview" show a flat table or card list with no "Fully staffed", "Partially staffed", or "Unstaffed" group headings. Only per-project status labels appear.

## Constraint

- [ ] CS-01: Project cannot be saved with a blank required field.
  - Action: Click "New Project", leave "Project Name" empty, fill the other fields, and click "Save".
  - Expected: Save is blocked, an inline error "Project name is required" appears, and no project is created.
  - Bug Report:
    - Issue: Incorrect Validation Message
    - Actual: Save was blocked and no project was created. The message was a toast, "Please fill in all required fields", not an inline "Project name is required" error.
- [ ] CS-02: Employee marked "Unavailable" cannot be assigned to a project role.
  - Action: Select a default employee whose availability is "Unavailable" and click "Assign".
  - Expected: Assignment is rejected with the message "Employee is unavailable", and the employee is not added to any role.
  - Bug Report:
    - Issue: Constraint Not Enforced
    - Actual: David Kim (Unavailable) was assigned to the "Frontend Developer" role of Data Analytics Dashboard. The toast read "Employee assigned successfully" and the role showed 2/2. The assignment was later undone with Unassign.
- [ ] CS-03: A project role cannot hold more employees than its required headcount.
  - Action: Attempt to assign a further employee to a project role that is already at its required headcount.
  - Expected: Assignment is rejected with the message "Role is already fully staffed", and the role's count is unchanged.
  - Bug Report:
    - Issue: Unable to Execute (no assign control on filled roles)
    - Actual: Filled roles (e.g., Customer Portal "Lead Frontend Developer", and Data Analytics "Frontend Developer" after assignment) show no "Assign Employee" button. The rejection message could not be triggered or observed.
- [ ] CS-04: Expected duration must be a positive number.
  - Action: Open "Edit" on a default project, enter "0" in the duration field, and click "Save". Repeat with "-3".
  - Expected: Each save is blocked with the message "Duration must be greater than 0", and the previous duration remains.
  - Bug Report:
    - Issue: Constraint Not Enforced
    - Actual: Entering "0" on Customer Portal Redesign showed "Project updated successfully". The detail page then showed "1 weeks duration" instead of the prior 10 weeks. The "-3" case was not run because of the call budget.

## Interaction

- [ ] IX-01: A success toast confirms when a project is saved.
  - Action: Create or edit a project with valid values and click "Save".
  - Expected: A toast reading "Project saved" appears near the top of the page and disappears automatically within about 5 seconds.
  - Bug Report:
    - Issue: Incorrect Toast Text
    - Actual: Toasts read "Project created successfully" on create and "Project updated successfully" on edit, not "Project saved". The toast appeared at the top right. Auto-dismiss timing was not measured.
- [ ] IX-02: Search with no matches shows an empty-state message, and clearing the search restores the list.
  - Action: Type "zzzz" in "Search employees", then clear the field.
  - Expected: The list shows "No employees match your filters" while the text is entered, and the full employee list returns when the field is cleared.
  - Bug Report:
    - Issue: Incorrect Empty-State Message
    - Actual: The list shows "No employees found" with "Try adjusting your search or filters", not "No employees match your filters". Clearing the field restored all 8 employees.
- [X] IX-03: Overview status updates immediately after an assignment changes.
  - Action: Assign an employee to the last open role of a "Partially staffed" project without reloading the page.
  - Expected: The project moves to the "Fully staffed" group in the overview, and its status label updates without a page refresh.
- [ ] IX-04: Reassignment asks for confirmation, and cancelling leaves the assignment unchanged.
  - Action: Click "Reassign" on an assigned employee, select a new role, then click "Cancel" in the confirmation dialog.
  - Expected: A dialog reading "Reassign [employee] from [old role] to [new role]?" appears with "Cancel" and "Confirm" buttons, and after cancelling the employee remains in the original role.
  - Bug Report:
    - Issue: Missing Confirmation Dialog
    - Actual: No "Reassign" action or confirmation dialog exists. The second icon on an assigned employee's card unassigned Michael Brown immediately, with a toast "Employee unassigned" and no confirmation.

## Content

- [ ] CT-01: Employee skills and availability shown in the list match each employee's default profile.
  - Action: Compare the skills and availability of three default employees in the list with their individual profile views.
  - Expected: Skills and availability values are identical in both views for every compared employee.
  - Bug Report:
    - Issue: Missing View (no individual profile)
    - Actual: Clicking an employee's name or card does nothing (the URL stays on /employees). No individual profile view was found, so the comparison could not be made.
- [ ] CT-02: Every default project row displays all four fields with no placeholder text.
  - Action: Review the project list for all default projects.
  - Expected: Each row shows a name, at least one required skill, a priority of Low/Medium/High, and a duration; no row contains "undefined", "null", "NaN", or blank values.
  - Bug Report:
    - Issue: Missing Data Display (required skills not in rows)
    - Actual: Rows show name, description, priority, duration, roles, and status, but no required skills. No "undefined", "null", "NaN", or blank values were found.
- [X] CT-03: Staffing status labels agree with the number of filled roles for each project.
  - Action: For each default project, compare filled roles against required roles in the project details, then check its label in the overview.
  - Expected: "Fully staffed" when all roles are filled, "Partially staffed" when some are filled, and "Unstaffed" when none are filled; labels match the role counts for every project.
- [X] CT-04: Skill filter options match the skills held by default employees, with no duplicates.
  - Action: Open the "Skill" filter dropdown and compare its options with the skills listed across all default employees.
  - Expected: Each skill appears exactly once, every option is held by at least one employee, and no employee skill is missing from the options.
