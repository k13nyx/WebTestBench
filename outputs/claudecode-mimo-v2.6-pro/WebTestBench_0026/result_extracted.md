# Test Result

## Functionality
- [X] FT-01: Create a new project with required skills, priority, and expected duration
  - Action: Fill the project form (name, required skills, priority, expected duration) and click "Create"/"Save"
  - Expected: New project appears in the project list with the entered values
- [X] FT-02: Edit an existing project
  - Action: Open an existing (default) project, change priority and expected duration, save
  - Expected: Updated values are shown in the project's details
- [ ] FT-03: Search employees by keyword
  - Action: Type a term matching an existing employee's name or skill into the employee search box
  - Expected: Employee list shows only matching employees
  - Bug Report:
    - Issue: Incomplete Search Implementation (skill keywords not matched)
    - Actual: Name search works ("Sarah" → only "Sarah Chen" listed), but typing a skill term that matches existing employees ("GraphQL", a skill of Sarah Chen and Michael Brown) returns zero results and shows the "No employees found – Try adjusting your search or filters" empty state. The search box only matches name/email/title (its placeholder reads "Search by name, email, or title...") and does not match skills as the test action requires.
- [X] FT-04: Filter employees by skill
  - Action: Select a skill filter that matches at least one existing employee's skill
  - Expected: Only employees holding that skill are listed
- [X] FT-05: Filter employees by availability
  - Action: Select the "Available" availability filter
  - Expected: Only employees with available status are listed
- [X] FT-06: Assign an employee to an empty project role
  - Action: On an existing project, assign an available employee to an unfilled role
  - Expected: The role shows the employee as its assignee
- [X] FT-07: Reassign a project role to a different employee
  - Action: Change the assignee of a filled role to another employee
  - Expected: Role shows the new employee; the previous assignee is no longer on that role
- [X] FT-08: Remove an employee from a project role
  - Action: Unassign the employee from a filled role
  - Expected: The role becomes empty/unassigned
- [X] FT-09: Staffing overview classifies each project correctly
  - Action: View the overview with default projects at different fill levels (all roles filled / some filled / none filled)
  - Expected: Each project is shown as fully staffed, partially staffed, or unstaffed, matching its actual role fill state

## Constraint
- [X] CS-01: Project cannot be saved with missing required fields
  - Action: Submit the project form with an empty name or no required skills selected
  - Expected: Save is blocked with a validation error; no project is created
- [ ] CS-02: Expected duration must be a valid positive value
  - Action: Enter 0, a negative number, or non-numeric text as expected duration and save
  - Expected: Save is blocked with a validation error on the duration field
  - Bug Report:
    - Issue: Missing Duration Validation (invalid values accepted / no field-level error)
    - Actual: Entering 0 as expected duration does NOT block save — the project is created without any validation error (value silently normalized to "1 weeks" in the list: "Duration Test Project | Automated QA validation | Medium | 1 weeks"). A negative value (-5) is blocked, but only by a generic toast "Please fill in all required fields" with no error on the duration field (no aria-invalid, no field error text). Non-numeric text cannot even be entered into the number input (typing "abc" leaves value "1"), which then saves successfully. No case produces a validation error on the duration field for 0.
- [ ] CS-03: The same employee cannot hold two roles at once
  - Action: Assign an employee to a second role while they are already assigned to another role
  - Expected: The assignment is rejected/blocked; the employee remains on only one role
  - Bug Report:
    - Issue: Unenforced Single-Role Constraint (duplicate assignment accepted)
    - Actual: Clicking "Assign" for Marcus Johnson while he was already the Backend Developer of the same project succeeded ("Employee assigned successfully" toast, button was enabled) and he simultaneously held two roles — "Lead Frontend Developer → Marcus Johnson" and "Backend Developer → Marcus Johnson". The default data likewise shows David Kim assigned to two projects (Customer Portal Redesign and Mobile App Launch) at once, confirming no blocking exists.

## Interaction
- [X] IX-01: Mutating actions give confirmation feedback
  - Action: Create a project, edit a project, and assign an employee
  - Expected: Each action displays a success confirmation message; no page reload occurs
- [X] IX-02: Employee search and filters update the list without reload
  - Action: Type in the search box and change the skill/availability filters
  - Expected: Employee list updates immediately; a clear empty state appears when nothing matches
- [X] IX-03: Staffing overview updates immediately after assignment changes
  - Action: Assign or unassign an employee, then look at the overview
  - Expected: The affected project's staffing category changes immediately (e.g., unstaffed → partially staffed)
- [X] IX-04: Project edit form is pre-populated with current data
  - Action: Open the edit view of an existing project
  - Expected: Name, required skills, priority, and expected duration show the project's current values

## Content
- [X] CT-01: Employee list shows name, skills, and availability
  - Action: View the default employee list
  - Expected: Every employee row displays name, their skills, and an availability status
- [X] CT-02: Project details show required skills, priority, and expected duration
  - Action: View details of an existing project
  - Expected: Required skills, priority level, and expected duration are displayed for the project
- [ ] CT-03: Overview lists the three staffing categories with their projects
  - Action: View the staffing overview section
  - Expected: Fully staffed, partially staffed, and unstaffed categories are visible, each listing the correct project names from the default data
  - Bug Report:
    - Issue: Missing Staffing Category Sections in Overview
    - Actual: The dashboard "Projects Overview" shows only aggregate stat tiles ("Total Projects 4", "Fully Staffed 0", "Need Attention 4 – 3 partial, 1 unstaffed") plus a single flat list of project cards with per-project status badges (Partial/Unstaffed). There are no "Fully staffed", "Partially staffed", and "Unstaffed" category sections that list project names (the only headings rendered are "Dashboard" and "Projects Overview"); the fully-staffed category lists no projects at all and is only visible as a count of 0.
