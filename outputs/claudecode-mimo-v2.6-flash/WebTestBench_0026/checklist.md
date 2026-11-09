# Test Checklist

## Functionality
- [ ] FT-01: Create a new project with all required details
  - Action: Open the project creation form, enter a project name, required skills, priority, and expected duration, then save.
  - Expected: The new project appears in the project list with the entered skills, priority, and duration.
- [ ] FT-02: Edit an existing project's details
  - Action: Open an existing project, change its required skills, priority, and expected duration, then save.
  - Expected: The project list reflects the updated skills, priority, and duration.
- [ ] FT-03: Search the employee list
  - Action: Type a known employee name into the employee search box.
  - Expected: The list narrows to only employees whose names match the query.
- [ ] FT-04: Filter the employee list
  - Action: Apply a skill filter (e.g., a skill held by some employees) and/or an availability filter.
  - Expected: Only employees matching all selected filters are displayed, showing their skills and availability.
- [ ] FT-05: Assign an employee to a project role
  - Action: Open a project's role assignment, select an available employee, and assign them.
  - Expected: The employee is listed under that project role, and their availability is reflected in the employee list.
- [ ] FT-06: Reassign an employee to a different project role
  - Action: Change an already-assigned employee's role or replace them with another employee.
  - Expected: The role shows the new assignment, and the previous assignment no longer lists that employee.
- [ ] FT-07: Staffing overview categorizes projects
  - Action: View the project overview section.
  - Expected: Each project is shown under exactly one of: fully staffed, partially staffed, or unstaffed, matching its current assignments.
- [ ] FT-08: Adjusting assignments updates staffing status
  - Action: Assign an employee to the last open role of a partially staffed project, then remove an employee from a fully staffed project.
  - Expected: The project moves to fully staffed after the first change and back to partially staffed (or unstaffed) after the second.

## Constraint
- [ ] CS-01: Project creation requires all mandatory fields
  - Action: Attempt to save a new project with name, required skills, priority, or expected duration left empty.
  - Expected: The project is not saved, and an error message identifies the missing required field(s).
- [ ] CS-02: Invalid project input is rejected
  - Action: Attempt to save a project with an invalid expected duration (e.g., zero, negative, or non-numeric) or an invalid priority value.
  - Expected: The project is not saved, and an error message explains the invalid value.
- [ ] CS-03: Cannot assign an unavailable employee
  - Action: Attempt to assign an employee marked unavailable (or already fully allocated) to a project role.
  - Expected: The assignment is blocked or the option is not selectable, with an explanation of why.
- [ ] CS-04: Cannot fill a role with two employees
  - Action: Attempt to assign a second employee to a role that already has an occupant without first reassigning.
  - Expected: The action is rejected or explicitly replaces the current assignee; the role never shows two employees at once.
- [ ] CS-05: Editing preserves data integrity
  - Action: Cancel a project edit after modifying fields without saving.
  - Expected: The project's original values remain unchanged.

## Interaction
- [ ] IX-01: Saving a project gives clear feedback
  - Action: Successfully create or edit a project.
  - Expected: A visible success confirmation (e.g., toast or message) appears, and the project list updates immediately without a manual refresh.
- [ ] IX-02: Validation errors are shown inline
  - Action: Submit a form with missing or invalid fields.
  - Expected: Error messages appear next to the offending fields and the form remains open with entered data preserved.
- [ ] IX-03: Search and filters respond immediately
  - Action: Type in the search box and toggle filters.
  - Expected: The employee list updates reactively as input changes, with no page reload required.
- [ ] IX-04: Assignment changes give immediate feedback
  - Action: Assign, reassign, or remove an employee.
  - Expected: The role list, employee availability, and staffing overview all update immediately and a confirmation message is shown.

## Content
- [ ] CT-01: Employee cards show complete, accurate details
  - Action: Inspect the employee list (e.g., after clearing filters).
  - Expected: Every employee entry displays their name, skills, and availability status, and the data matches their actual assignment state.
- [ ] CT-02: Project list displays all specified attributes
  - Action: View the project list and open a project.
  - Expected: Each project clearly shows its required skills, priority level, and expected duration, consistent between the list and detail/edit views.
- [ ] CT-03: Staffing overview labels are unambiguous
  - Action: Review the overview section.
  - Expected: The three categories (fully staffed, partially staffed, unstaffed) are clearly labeled, and each project appears under the correct category with its role-fill status visible (e.g., "3/4 roles filled").