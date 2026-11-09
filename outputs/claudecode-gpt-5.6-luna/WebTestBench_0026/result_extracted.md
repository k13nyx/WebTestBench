# Test Result

## Functionality

- [ ] FT-01: Team leads can access a single workspace for managing projects, employees, and assignments.
  - Action: Open the project-management page.
  - Expected: The page displays project management, employee management, and staff-assignment areas in the same workspace.
  - Bug Report:
    - Issue: Management areas are separated into different routes.
    - Actual: The application provides separate Projects and Employees pages. Project assignments are available only within individual project detail pages, rather than all three areas being displayed in the same workspace.

- [X] FT-02: Team leads can create a project with all required project details.
  - Action: Select **Create Project**, enter a project name, required skills, priority, and expected duration, then select **Save Project**.
  - Expected: The new project appears in the project list with the entered details.

- [X] FT-03: Team leads can edit an existing project.
  - Action: Select **Edit** for a default project, change its required skills, priority, or expected duration, and save.
  - Expected: The project displays the updated values after saving or reopening it.

- [X] FT-04: The employee list displays employee skills and availability.
  - Action: Review the default employee list.
  - Expected: Each employee record shows the employee name, one or more skills, and a current availability status.

- [ ] FT-05: Team leads can search employees by name or skill.
  - Action: Enter a known default employee name in the employee search field, then repeat using a known skill.
  - Expected: The list shows matching employee records and excludes non-matching records.
  - Bug Report:
    - Issue: Employee search does not search by skill.
    - Actual: Searching for the known skill “React” returned “No employees found,” even though Sarah Chen, David Kim, and James Wilson all display React as a skill. Name search for “Sarah Chen” worked.

- [X] FT-06: Team leads can filter employees by skill and availability.
  - Action: Apply a skill filter and an availability filter using values present in the default data.
  - Expected: Only employees matching all selected filters remain visible.

- [X] FT-07: Team leads can assign an employee to a project role.
  - Action: Open a default project, select an unfilled role, choose an employee, and select **Assign**.
  - Expected: The employee appears in that project role and the assignment is visible in the project details.

- [X] FT-08: Team leads can reassign an employee to a different project role or project.
  - Action: Select an existing assignment, choose a different eligible role or project, and confirm the reassignment.
  - Expected: The employee is removed from the previous assignment and appears in the new assignment.

- [X] FT-09: Team leads can view project staffing summaries.
  - Action: Review the staffing overview.
  - Expected: Projects are grouped or labeled as **Fully Staffed**, **Partially Staffed**, or **Unstaffed**.

- [X] FT-10: Team leads can adjust assignments after project needs change.
  - Action: Edit a default project’s required skills or roles, then review and modify its employee assignments.
  - Expected: The project’s assignments and staffing status reflect the updated project needs.

## Constraint

- [ ] CS-01: A project cannot be saved without its required project details.
  - Action: Open **Create Project** or **Edit Project**, leave the project name, required skills, priority, or expected duration empty, and select **Save Project**.
  - Expected: The project is not saved, and each missing required field is identified with a validation message.
  - Bug Report:
    - Issue: Missing fields are not individually identified.
    - Actual: The project was not saved, but the interface displayed only the generic toast “Please fill in all required fields.” No field-specific validation messages were shown.

- [X] CS-02: Employee search and filters cannot display records that do not match the active criteria.
  - Action: Search for a known employee or apply a known skill/availability filter.
  - Expected: Every visible employee matches the active search and filter criteria.

- [X] CS-03: Staffing status matches the number of filled project roles.
  - Action: Compare projects with no filled roles, some filled roles, and all required roles filled against the staffing overview.
  - Expected: They are labeled **Unstaffed**, **Partially Staffed**, and **Fully Staffed**, respectively.

- [X] CS-04: Reassigning an employee does not leave the employee assigned to both the old and new destination.
  - Action: Reassign an employee who already has a project role.
  - Expected: The employee has only the new assignment unless the interface explicitly supports multiple simultaneous assignments.

## Interaction

- [X] IX-01: Employee results update when search or filters are changed.
  - Action: Enter a search term, apply a filter, change the filter, and then clear the search.
  - Expected: The employee list updates after each change and returns to the unfiltered default list when criteria are cleared.

- [X] IX-02: The interface confirms successful project and assignment changes.
  - Action: Save a valid project edit and complete a valid assignment or reassignment.
  - Expected: A visible success confirmation appears for each completed operation, and the updated state remains displayed.

- [X] IX-03: Staffing indicators update after assignment changes.
  - Action: Assign or remove an employee from a default project.
  - Expected: The project’s staffing label and overview summary update to reflect the new staffing state.

- [ ] IX-04: Project and employee details remain associated with the selected record.
  - Action: Open different projects and employees from their respective lists.
  - Expected: The details and available assignment controls show data for the selected record only.
  - Bug Report:
    - Issue: Employee records do not provide selectable employee detail views.
    - Actual: Project rows opened project-specific detail pages, but employee records on the Employees page were non-interactive cards with no employee detail or assignment-control view to open.

## Content

- [X] CT-01: Project records show all information needed for staffing decisions.
  - Action: Open several default projects.
  - Expected: Each project displays its name, required skills, priority, expected duration, roles, assignments, and staffing status.

- [X] CT-02: Employee information is relevant and internally consistent.
  - Action: Compare employee records in the list with their detail or assignment views.
  - Expected: Employee names, skills, and availability values are consistent in every location.

- [ ] CT-03: Staffing labels and availability values are clear and unambiguous.
  - Action: Review project staffing labels and employee availability indicators.
  - Expected: The interface uses clear text labels such as **Fully Staffed**, **Partially Staffed**, **Unstaffed**, and explicit availability states rather than relying only on color or icons.
  - Bug Report:
    - Issue: Partial staffing labels are inconsistent and abbreviated.
    - Actual: Several project list and detail views displayed “Partial” instead of the explicit “Partially Staffed” label, while other views used “Fully Staffed” and “Unstaffed.” Availability states were explicit text labels.
