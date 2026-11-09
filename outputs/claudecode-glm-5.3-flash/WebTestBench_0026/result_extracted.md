# Test Result

## Functionality
- [X] FT-01: Create a new project with required fields
  - Action: Open the "Create Project" form, enter project name, select at least one required skill, set a priority (e.g., High) and an expected duration, then submit.
  - Expected: The new project appears in the projects list with the entered name, skill(s), priority, and duration.
  - Note: Created "QA Automation Project" (High, 10 weeks, role "Frontend Developer" with React/TypeScript); it appeared immediately in the list and detail view showed the required skills. However, the project was **lost after a full page reload** — the list reverted to the 4 default projects, indicating created data is not persisted.
- [X] FT-02: Edit an existing project's details
  - Action: Open an existing default project's edit form, change its priority (e.g., Medium → High) and expected duration, then save.
  - Expected: The project list/detail view immediately reflects the updated priority and duration.
- [X] FT-03: View searchable list of employees
  - Action: Type a known employee's name (from default data) into the employee search box.
  - Expected: Only matching employees are listed; the list updates as the query is typed.
- [X] FT-04: Filter employees by skill and availability
  - Action: Apply a skill filter (e.g., "React") and an availability filter (e.g., "Available") to the employee list.
  - Expected: Only employees possessing that skill and matching the availability state are shown.
- [X] FT-05: Assign an employee to a project role
  - Action: From a project's detail/assignment view, assign an available employee from default data to an open project role.
  - Expected: The employee now appears under that project's role, and the project's staffing status updates accordingly.
- [ ] FT-06: Reassign an employee to a different project
  - Action: Select an employee already assigned to Project A and reassign them to Project B.
  - Expected: The employee is removed from Project A's roster and appears in Project B's roster.
  - Bug Report:
    - Issue: Missing reassignment function / assignment duplication
    - Actual: There is no cross-project "reassign" control (employee cards have no reassign action; only role-level edit). Assigning Marcus Johnson (already on Customer Portal Redesign) to API Gateway Migration's Backend Developer role succeeded without removing him from Customer Portal Redesign — he remained listed on both project rosters simultaneously instead of being moved.
- [X] FT-07: Remove/unassign an employee from a project
  - Action: Remove an assigned employee from one of their project roles.
  - Expected: The employee no longer appears on that project's roster, and their availability status is updated.
- [X] FT-08: Staffing status overview is displayed for all projects
  - Action: View the overview section listing all default projects with their staffing states.
  - Expected: Each project is labeled as one of "Fully Staffed", "Partially Staffed", or "Unstaffed" consistent with its current assignments.

## Constraint
- [X] CS-01: Cannot create a project without required fields
  - Action: Attempt to submit the Create Project form leaving the name, skill, priority, or duration empty.
  - Expected: Submission is blocked and a validation message identifies the missing required field(s).
  - Note: Empty submission was blocked with the message "Please fill in all required fields"; submission with name/description but no role/skill was also blocked. The message is generic (fields are marked with asterisks rather than named individually).
- [ ] CS-02: Cannot assign an unavailable employee
  - Action: Attempt to assign an employee whose availability status is "Unavailable" to a project role.
  - Expected: The assignment is prevented (control disabled or an error message shown) and the employee is not added to the roster.
  - Bug Report:
    - Issue: Missing validation on employee availability
    - Actual: David Kim, whose status is "Unavailable", was listed in the assignment dialog with an enabled "Assign" button; clicking it assigned him to the Frontend Developer role of Data Analytics Dashboard with no warning or error. The roster showed "David Kim / Full Stack Developer" and the role was filled.
- [ ] CS-03: Employee cannot hold conflicting assignments on the same project role
  - Action: Attempt to assign an already-assigned employee to the same project role that is already filled.
  - Expected: The system blocks the duplicate assignment or requires explicit reassignment; the role is not double-filled.
  - Bug Report:
    - Issue: Duplicate assignment not blocked
    - Actual: The assignment dialog lists employees already assigned to the same project (e.g., Marcus Johnson on Customer Portal Redesign) with enabled "Assign" buttons. Assigning Marcus Johnson to a second role (UX Designer) on the same project succeeded — he appeared twice on the same project's roster with no block, warning, or reassignment prompt.
- [X] CS-04: Fully staffed projects show no open roles available for assignment
  - Action: Open a project whose staffing status is "Fully Staffed" and look for open/assignable roles.
  - Expected: No unfilled roles remain, or further assignment into the project is not offered.

## Interaction
- [X] IX-01: Confirmation feedback after assignment action
  - Action: Assign or reassign an employee to a project.
  - Expected: A visible success indicator (toast/message) confirms the assignment, and the roster updates without a page reload.
- [X] IX-02: Filters and search combine in real time
  - Action: With a search term already entered, additionally change a filter (skill or availability).
  - Expected: The employee list updates immediately to reflect both the search term and the filter simultaneously.
  - Note: Verified with search "David" + skill "React" + availability "Available" → "No employees found" (David has React but is Unavailable), proving all three conditions combine.
- [X] IX-03: Staffing overview updates live after assignment changes
  - Action: While the overview is visible, fill the last open role of an "Unstaffed"/"Partially Staffed" project.
  - Expected: That project's status label changes to "Fully Staffed" in the overview without reloading the page.

## Content
- [X] CT-01: Employee entries display complete relevant data
  - Action: Inspect several employees in the default employee list.
  - Expected: Each employee shows their name, their skills, and their current availability status; no placeholder or empty skill/availability fields.
- [ ] CT-02: Project entries display complete relevant data
  - Action: Inspect the projects list/overview.
  - Expected: Each project shows its name, required skills, priority, expected duration, and current staffing status; no placeholder or missing values.
  - Bug Report:
    - Issue: Missing data in list/overview display
    - Actual: The Projects table shows name, priority, duration, roles-filled (e.g., "2/3"), and status, but **required skills are not displayed anywhere in the list or dashboard overview** — they are only visible after opening the project's detail page.
