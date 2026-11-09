# Test Checklist

## Functionality
- [ ] FT-01: Create a new project with required skills, priority, and expected duration
  - Action: Fill the project form (name, required skills, priority, expected duration) and click "Create"/"Save"
  - Expected: New project appears in the project list with the entered values
- [ ] FT-02: Edit an existing project
  - Action: Open an existing (default) project, change priority and expected duration, save
  - Expected: Updated values are shown in the project's details
- [ ] FT-03: Search employees by keyword
  - Action: Type a term matching an existing employee's name or skill into the employee search box
  - Expected: Employee list shows only matching employees
- [ ] FT-04: Filter employees by skill
  - Action: Select a skill filter that matches at least one existing employee's skill
  - Expected: Only employees holding that skill are listed
- [ ] FT-05: Filter employees by availability
  - Action: Select the "Available" availability filter
  - Expected: Only employees with available status are listed
- [ ] FT-06: Assign an employee to an empty project role
  - Action: On an existing project, assign an available employee to an unfilled role
  - Expected: The role shows the employee as its assignee
- [ ] FT-07: Reassign a project role to a different employee
  - Action: Change the assignee of a filled role to another employee
  - Expected: Role shows the new employee; the previous assignee is no longer on that role
- [ ] FT-08: Remove an employee from a project role
  - Action: Unassign the employee from a filled role
  - Expected: The role becomes empty/unassigned
- [ ] FT-09: Staffing overview classifies each project correctly
  - Action: View the overview with default projects at different fill levels (all roles filled / some filled / none filled)
  - Expected: Each project is shown as fully staffed, partially staffed, or unstaffed, matching its actual role fill state

## Constraint
- [ ] CS-01: Project cannot be saved with missing required fields
  - Action: Submit the project form with an empty name or no required skills selected
  - Expected: Save is blocked with a validation error; no project is created
- [ ] CS-02: Expected duration must be a valid positive value
  - Action: Enter 0, a negative number, or non-numeric text as expected duration and save
  - Expected: Save is blocked with a validation error on the duration field
- [ ] CS-03: The same employee cannot hold two roles at once
  - Action: Assign an employee to a second role while they are already assigned to another role
  - Expected: The assignment is rejected/blocked; the employee remains on only one role

## Interaction
- [ ] IX-01: Mutating actions give confirmation feedback
  - Action: Create a project, edit a project, and assign an employee
  - Expected: Each action displays a success confirmation message; no page reload occurs
- [ ] IX-02: Employee search and filters update the list without reload
  - Action: Type in the search box and change the skill/availability filters
  - Expected: Employee list updates immediately; a clear empty state appears when nothing matches
- [ ] IX-03: Staffing overview updates immediately after assignment changes
  - Action: Assign or unassign an employee, then look at the overview
  - Expected: The affected project's staffing category changes immediately (e.g., unstaffed → partially staffed)
- [ ] IX-04: Project edit form is pre-populated with current data
  - Action: Open the edit view of an existing project
  - Expected: Name, required skills, priority, and expected duration show the project's current values

## Content
- [ ] CT-01: Employee list shows name, skills, and availability
  - Action: View the default employee list
  - Expected: Every employee row displays name, their skills, and an availability status
- [ ] CT-02: Project details show required skills, priority, and expected duration
  - Action: View details of an existing project
  - Expected: Required skills, priority level, and expected duration are displayed for the project
- [ ] CT-03: Overview lists the three staffing categories with their projects
  - Action: View the staffing overview section
  - Expected: Fully staffed, partially staffed, and unstaffed categories are visible, each listing the correct project names from the default data