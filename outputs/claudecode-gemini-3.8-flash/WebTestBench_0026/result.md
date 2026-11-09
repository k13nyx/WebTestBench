# Test Result

## Functionality
- [X] FT-01: Create a new project with required metadata
  - Action: Click "Create Project", enter a project name, select required skills, set priority level, enter expected duration, and click "Save".
  - Expected: The new project is created and appears in the project list with the entered skills, priority, and duration.
- [X] FT-02: Edit an existing project's configuration
  - Action: Click "Edit" on an existing project, modify its priority, expected duration, and required skills, then click "Update".
  - Expected: The project details update immediately to display the revised priority, duration, and required skills.
- [ ] FT-03: Search employee roster by keyword
  - Action: Type a specific employee name or skill keyword into the employee search input field.
  - Expected: The employee list dynamically updates to display only employees whose names or skill profiles match the entered query.
  - Bug Report:
    - Issue: Search filtering does not include employee skill profiles
    - Actual: Typing an employee name filters the roster as expected, but typing a skill keyword (such as "Figma" or "GraphQL") returns "No employees found" despite employees having those skills. The search filter only checks `employee.name`, `employee.email`, and `employee.title`, omitting employee skill tags from search evaluation.
- [X] FT-04: Filter employee roster by skills and availability
  - Action: Select a specific skill from the skill filter dropdown and set the availability filter to "Available".
  - Expected: The list displays only employees who possess the selected skill and currently have "Available" status.
- [X] FT-05: Assign an available employee to a project role
  - Action: In an open project role slot, select an available employee from the assignment dropdown and confirm.
  - Expected: The employee is assigned to the specified project role and appears in the project's assigned staff list.
- [ ] FT-06: Reassign an employee to a different project role
  - Action: Click "Reassign" on an already assigned employee in a project and select a new target role.
  - Expected: The employee is moved to the newly selected role, and the previous role slot becomes vacant.
  - Bug Report:
    - Issue: Missing role reassignment functionality
    - Actual: There is no "Reassign" button or workflow to move an assigned employee to a new target role. The edit icon button on an assigned employee only opens an "Assign Employee to [current role]" modal to replace or unassign the employee within the current role, with no mechanism to select another role in the project.
- [X] FT-07: Unassign an employee from a project
  - Action: Click the "Remove" or "Unassign" button next to an assigned employee in a project.
  - Expected: The employee is removed from the project role and their availability status updates back to available.

## Constraint
- [X] CS-01: Prevent project creation with missing mandatory fields
  - Action: Click "Create Project", leave project name, priority, or required skills empty, and click "Save".
  - Expected: The form submission is blocked, and validation error messages indicate the required fields that must be filled.
- [ ] CS-02: Prevent assigning an unavailable employee to a role
  - Action: Attempt to select and assign an employee marked as "Unavailable" to a project role.
  - Expected: The system disables selection for that employee or displays an error indicating the employee is unavailable.
  - Bug Report:
    - Issue: Ineffective constraint on unavailable employee assignment
    - Actual: The system does not disable the "Assign" button for employees with "Unavailable" status, nor does it display an error upon selection. Clicking "Assign" on David Kim (marked "Unavailable") assigned him to the role and displayed a success notification ("Employee assigned successfully").
- [ ] CS-03: Reject non-positive or non-numeric values in project duration
  - Action: Enter a negative number (e.g., "-5") or "0" into the expected duration field and submit.
  - Expected: The form rejects the input with a validation error stating duration must be a positive number.
  - Bug Report:
    - Issue: Missing validation error for non-positive duration values
    - Actual: When entering "0" into the duration field and submitting, the form did not reject the input or display any validation error. Instead, the application silently defaulted the value to 1 (`parseInt(value) || 1`) and submitted the update successfully.

## Interaction
- [X] IX-01: Real-time update of project staffing status badge
  - Action: Assign an employee to the final remaining vacant role of a "Partially Staffed" project.
  - Expected: The project's status indicator automatically updates from "Partially Staffed" to "Fully Staffed" without requiring a page refresh.
- [X] IX-02: Open and dismiss project edit modal without saving
  - Action: Click "Edit" on a project card, modify a field, and click the "Cancel" or "Close" button.
  - Expected: The modal closes immediately and all changes are discarded without updating the project.

## Content
- [X] CT-01: Display staffing status overview summary counters
  - Action: View the top staffing overview panel on the main page.
  - Expected: The panel displays accurate aggregate counters for "Fully Staffed", "Partially Staffed", and "Unstaffed" projects.
- [X] CT-02: Display complete employee card details
  - Action: Inspect any employee card or row in the roster view.
  - Expected: The entry clearly displays the employee's full name, list of technical/domain skills, and current availability status.
- [ ] CT-03: Display project card attributes and staffing breakdown
  - Action: Inspect any project card in the project management view.
  - Expected: The card clearly presents the project title, priority badge, expected duration, list of required skills, and current staffing status.
  - Bug Report:
    - Issue: Missing required skills on project cards and list rows
    - Actual: Project overview cards on the dashboard and project rows in the project list display project title, priority badge, expected duration, and staffing status, but omit the list of required skills entirely. Required skills are only visible inside individual role slots on the project detail view.