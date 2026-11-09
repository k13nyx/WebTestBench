# Test Result

## Functionality

- [X] FT-01: Create a new project with all required attributes
  - Action: Click "Create Project", enter a name, select required skills, set priority, and enter expected duration, then submit.
  - Expected: New project appears in the project list containing the entered name, skills, priority, and duration.

- [X] FT-02: Edit an existing project's details and persist changes
  - Action: Open a default project, click "Edit", change its priority and expected duration, then save.
  - Expected: Project list shows the updated priority and duration for that project.

- [X] FT-03: View employee list with skills and availability
  - Action: Open the employees list view.
  - Expected: Each default employee row displays their name, a list of skills, and an availability value.

- [X] FT-04: Search employees by name or skill
  - Action: Type a default employee's name (or a known skill) into the search box.
  - Expected: List narrows to only employees matching the entered name or skill.

- [X] FT-05: Filter employees by skill and availability
  - Action: Apply a skill filter and an availability filter from the filter controls.
  - Expected: List shows only employees matching the selected skill and availability criteria.

- [X] FT-06: Assign an employee to a project role
  - Action: On a project, click "Assign", select a default employee and a role, then confirm.
  - Expected: The employee appears under that project role and the project's staffing status reflects the added member.

- [X] FT-07: Reassign an employee to a different role or project
  - Action: On an existing assignment, click "Reassign", choose a different role or project, then confirm.
  - Expected: The employee is removed from the old role/project and appears under the newly selected role/project.

- [X] FT-08: View staffing overview with counts per status
  - Action: Open the overview section showing all default projects.
  - Expected: Each project is labeled fully staffed, partially staffed, or unstaffed, with a count of filled vs. required roles.

- [X] FT-09: Remove an assignment when needs change
  - Action: On a filled role, click "Remove assignment" (or unassign) for an employee.
  - Expected: The employee is removed from that role and the project's staffing status updates accordingly.

## Constraint

- [ ] CS-01: Prevent project creation with missing required fields
  - Action: Click "Create Project" and submit with an empty name (and/or no required skills, no priority, or no duration).
  - Expected: Submission is blocked with a validation message naming each missing required field; no project is created.
  - Bug Report:
    - Issue: Vague/generic validation message — does not name the missing required field(s)
    - Actual: Submission is blocked and no project is created (correct), but the only feedback is the generic toast "Please fill in all required fields". When submitting with the name filled and the description empty, the same generic message appears and the word "Description" (nor any other field name) is never shown; no per-field inline errors are rendered either. The validation therefore does not "name each missing required field".

- [X] CS-02: Staffing status is derived correctly from filled vs. required roles
  - Action: Compare a project with all roles filled, one with some filled, and one with none against their displayed status.
  - Expected: All-filled shows "Fully Staffed", some-filled shows "Partially Staffed", none-filled shows "Unstaffed".

- [ ] CS-03: Prevent assigning an unavailable employee
  - Action: Attempt to assign a default employee whose availability indicates they are unavailable (or already at full capacity) to a project role.
  - Expected: Assignment is blocked or the employee is flagged as unavailable; the employee is not added to the role.
  - Bug Report:
    - Issue: Unavailable employee can be assigned (no enforcement of availability constraint)
    - Actual: In the "Assign Employee to QA Engineer" dialog, David Kim was clearly labeled "Unavailable" but his "Assign" button was enabled. Clicking it produced the toast "Employee assigned successfully" and David Kim was added under the QA Engineer role (project moved from 2/3 "Partial" to 3/3 "Fully Staffed"). The employee was added to the role despite being flagged unavailable.

- [X] CS-04: Show empty state when search or filter yields no matches
  - Action: Search for a string or apply a filter combination matching no default employees.
  - Expected: A "No employees found" message is shown and no unrelated employee rows are displayed.

## Interaction

- [X] IX-01: Confirm successful project creation
  - Action: Create a project with valid values and submit.
  - Expected: A success notification (e.g., toast or confirmation message) is displayed indicating the project was created.

- [X] IX-02: Overview updates immediately after an assignment change
  - Action: Assign or remove an employee on a project while the overview is visible.
  - Expected: The project's staffing status and counts refresh without a full page reload.

- [X] IX-03: Filter and search results update without page reload
  - Action: Type in the search box and toggle filter controls on the employee list.
  - Expected: The employee list refreshes in place immediately as the search term or filters change.

## Content

- [X] CT-01: Employee skills and availability match their profile data
  - Action: Open a default employee's details and compare against the skills and availability shown in the list.
  - Expected: Displayed skills and availability are identical to the employee's stored profile values.

- [X] CT-02: Staffing status labels use the required terminology
  - Action: Inspect the overview labels for fully, partially, and unstaffed projects.
  - Expected: Labels read "Fully Staffed", "Partially Staffed", and "Unstaffed" respectively (or unmistakable equivalents).

- [X] CT-03: All displayed content is relevant to project and staff management
  - Action: Review the page for text, images, and icons.
  - Expected: Every displayed element relates to projects, skills, employees, or assignments; no placeholder, broken, or off-theme content appears.
