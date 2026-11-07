# Test Result

## Functionality
- [X] FT-01: Create a new project with required skills, priority, and expected duration
  - Action: Open "Create Project" form, fill in Project Name, select at least one Required Skill, choose Priority (e.g., High), enter Expected Duration (e.g., 30 days), and click "Create".
  - Expected: A new project is added to the project list and appears with the entered skills, priority, and duration.
  - Actual: Project "Test Project Alpha" was created and appeared in the project list with Priority "High", Duration "10 weeks", and a role carrying the "React" required skill (note: duration is entered in weeks in this app, not days).

- [X] FT-02: Edit an existing project's details
  - Action: Open an existing project (e.g., from the project list) and click "Edit", change the Priority and Expected Duration, then click "Save".
  - Expected: The project's details update to reflect the new Priority and Expected Duration.
  - Actual: After editing, the project's Priority changed "High" → "Medium" and Duration "10 weeks" → "8 weeks", with toast "Project updated successfully".

- [X] FT-03: View the list of employees with their skills and availability
  - Action: Navigate to the "Employees" view.
  - Expected: A list of employees is displayed, each showing name, skills, and availability status.
  - Actual: The Employees view displayed all 8 employees, each with name, title, skills, and availability status (Available / Partially Available / Unavailable).

- [X] FT-04: Search the employee list
  - Action: Type a known employee name (or skill keyword) into the search box and press Enter.
  - Expected: The list shows only employees matching the search term.
  - Actual: Typing "Sarah" and pressing Enter filtered the list to only "Sarah Chen".

- [X] FT-05: Filter the employee list by skill and availability
  - Action: Apply a skill filter (e.g., "Python") and an availability filter (e.g., "Available Only").
  - Expected: The list shows only employees who have the selected skill and are available.
  - Actual: With Availability = "Available" + Skill = "Python", only Lisa Thompson and Anna Petrova (both Available and with Python) remained; all others were excluded.

- [X] FT-06: Assign an employee to a project role
  - Action: Open a project, select an available employee from the employee list, choose a role, and click "Assign".
  - Expected: The employee is added to the project's assigned staff for that role.
  - Actual: Lisa Thompson (Available, 2/2 skill match) was assigned to the DevOps Engineer role of "API Gateway Migration"; project status changed Unstaffed → Partial (1/2).

- [X] FT-07: Reassign an employee to a different project or role
  - Action: Open a project containing an assigned employee, select the employee, change the target project or role, and confirm the reassignment.
  - Expected: The employee is removed from the previous assignment and appears under the new project/role.
  - Actual: Lisa Thompson was unassigned from DevOps Engineer and re-assigned to the Backend Developer role of the same project; she was removed from the old role and now appears under the new one.

- [X] FT-08: View the staffing overview
  - Action: Open the "Overview" (or dashboard) section.
  - Expected: Each project is shown with a staffing status of Fully Staffed, Partially Staffed, or Unstaffed.
  - Actual: The Dashboard "Projects Overview" shows each of the 4 projects with a staffing status label and a "Fully Staffed" summary count.

## Constraint
- [X] CS-01: Cannot create a project with missing required fields
  - Action: Open "Create Project" and click "Create" with the Project Name, Required Skills, Priority, or Expected Duration left empty.
  - Expected: The project is not created and a validation message indicates the missing required field(s).
  - Actual: Clicking "Create" with empty required fields showed "Please fill in all required fields" and the dialog remained open; no project was created.

- [ ] CS-02: Cannot assign an unavailable employee to a project
  - Action: Attempt to assign an employee whose availability status is "Unavailable" to a project role.
  - Expected: The assignment is blocked and a message states the employee is unavailable.
  - Bug Report:
    - Issue: Missing availability validation — unavailable employees are assignable
    - Actual: David Kim is marked "Unavailable", yet clicking "Assign" on him succeeded; toast "Employee assigned successfully" appeared and he was added to the DevOps Engineer role (project became "Fully Staffed"). No blocking message or validation occurred.

- [ ] CS-03: Cannot assign the same employee to an overlapping conflict
  - Action: Attempt to assign an employee who is already assigned to another project role that conflicts with the new assignment.
  - Expected: The assignment is prevented and a conflict/duplicate message is shown.
  - Bug Report:
    - Issue: No conflict / duplicate-assignment prevention
    - Actual: David Kim was already assigned to the DevOps Engineer role of the same project; clicking "Assign" for the Backend Developer role succeeded, placing David Kim in BOTH roles of that project. No conflict or duplicate-assignment warning/error was shown; toast "Employee assigned successfully" appeared.

## Interaction
- [X] IX-01: Show success confirmation after create, edit, assign, or reassign actions
  - Action: Perform a project create, an edit, an assignment, and a reassignment in turn.
  - Expected: A success toast or confirmation message appears after each completed action.
  - Actual: Toasts appeared after each action — "Project created successfully", "Project updated successfully", "Employee assigned successfully", and (for reassignment) "Employee unassigned" + "Employee assigned successfully".

- [X] IX-02: Staffing overview updates dynamically after assignment changes
  - Action: Assign or reassign an employee to a project, then view the Overview without reloading.
  - Expected: The affected project's staffing status (Fully/Partially/Unstaffed) updates immediately.
  - Actual: After assigning Lisa Thompson, the Dashboard updated live (API Gateway Migration went Unstaffed → Partial, "Need Attention" changed to "4 partial, 0 unstaffed", Available Staff 4 → 3) with no page reload.

## Content
- [X] CT-01: Employee entries display relevant skills and availability
  - Action: Review several employee entries in the list.
  - Expected: Each entry shows skills and availability directly relevant to staffing and matches the employee's actual data.
  - Actual: Every employee card shows the employee's skills and availability status (e.g., Sarah Chen: React/TypeScript/GraphQL, Available; David Kim: React/Node.js/TypeScript/SQL, Unavailable), matching the underlying data.

- [X] CT-02: Staffing overview labels are present and correctly reflect project state
  - Action: Compare each project's staffing status label against its assigned vs. required roles.
  - Expected: Labels "Fully Staffed", "Partially Staffed", and "Unstaffed" appear and correctly match each project's actual staffing.
  - Actual: All three states are represented and accurately reflect staffing (e.g., API Gateway Migration correctly showed "Partial" at 1/2 and "Fully Staffed" at 2/2). Note: the app uses the shorthand label "Partial" rather than the full phrase "Partially Staffed", but it correctly conveys the Partially Staffed state.
