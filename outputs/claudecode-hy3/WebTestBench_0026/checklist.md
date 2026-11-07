# Test Checklist

## Functionality
- [ ] FT-01: Create a new project with required skills, priority, and expected duration
  - Action: Open "Create Project" form, fill in Project Name, select at least one Required Skill, choose Priority (e.g., High), enter Expected Duration (e.g., 30 days), and click "Create".
  - Expected: A new project is added to the project list and appears with the entered skills, priority, and duration.

- [ ] FT-02: Edit an existing project's details
  - Action: Open an existing project (e.g., from the project list) and click "Edit", change the Priority and Expected Duration, then click "Save".
  - Expected: The project's details update to reflect the new Priority and Expected Duration.

- [ ] FT-03: View the list of employees with their skills and availability
  - Action: Navigate to the "Employees" view.
  - Expected: A list of employees is displayed, each showing name, skills, and availability status.

- [ ] FT-04: Search the employee list
  - Action: Type a known employee name (or skill keyword) into the search box and press Enter.
  - Expected: The list shows only employees matching the search term.

- [ ] FT-05: Filter the employee list by skill and availability
  - Action: Apply a skill filter (e.g., "Python") and an availability filter (e.g., "Available Only").
  - Expected: The list shows only employees who have the selected skill and are available.

- [ ] FT-06: Assign an employee to a project role
  - Action: Open a project, select an available employee from the employee list, choose a role, and click "Assign".
  - Expected: The employee is added to the project's assigned staff for that role.

- [ ] FT-07: Reassign an employee to a different project or role
  - Action: Open a project containing an assigned employee, select the employee, change the target project or role, and confirm the reassignment.
  - Expected: The employee is removed from the previous assignment and appears under the new project/role.

- [ ] FT-08: View the staffing overview
  - Action: Open the "Overview" (or dashboard) section.
  - Expected: Each project is shown with a staffing status of Fully Staffed, Partially Staffed, or Unstaffed.

## Constraint
- [ ] CS-01: Cannot create a project with missing required fields
  - Action: Open "Create Project" and click "Create" with the Project Name, Required Skills, Priority, or Expected Duration left empty.
  - Expected: The project is not created and a validation message indicates the missing required field(s).

- [ ] CS-02: Cannot assign an unavailable employee to a project
  - Action: Attempt to assign an employee whose availability status is "Unavailable" to a project role.
  - Expected: The assignment is blocked and a message states the employee is unavailable.

- [ ] CS-03: Cannot assign the same employee to an overlapping conflict
  - Action: Attempt to assign an employee who is already assigned to another project role that conflicts with the new assignment.
  - Expected: The assignment is prevented and a conflict/duplicate message is shown.

## Interaction
- [ ] IX-01: Show success confirmation after create, edit, assign, or reassign actions
  - Action: Perform a project create, an edit, an assignment, and a reassignment in turn.
  - Expected: A success toast or confirmation message appears after each completed action.

- [ ] IX-02: Staffing overview updates dynamically after assignment changes
  - Action: Assign or reassign an employee to a project, then view the Overview without reloading.
  - Expected: The affected project's staffing status (Fully/Partially/Unstaffed) updates immediately.

## Content
- [ ] CT-01: Employee entries display relevant skills and availability
  - Action: Review several employee entries in the list.
  - Expected: Each entry shows skills and availability directly relevant to staffing and matches the employee's actual data.

- [ ] CT-02: Staffing overview labels are present and correctly reflect project state
  - Action: Compare each project's staffing status label against its assigned vs. required roles.
  - Expected: Labels "Fully Staffed", "Partially Staffed", and "Unstaffed" appear and correctly match each project's actual staffing.