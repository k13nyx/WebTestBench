All checklist items have been executed with DOM-verified evidence. Final report:

# Test Result

## Functionality
- [X] FT-01: Team lead can create a new project with all required attributes
  - Action: Opened "New Project" dialog on /projects, entered name "Inventory Sync Platform" + description, selected priority "High", set duration 10 weeks, created role "Backend Engineer" with skills Node.js + SQL, and submitted.
  - Expected: The new project is saved and now appears in the projects list/overview with the entered skills, priority, and duration.
  - Verified: New row appeared ("High", "10 weeks", "0/1", "Unstaffed"); detail page showed the "Backend Engineer — Node.js, SQL" role. (Note: creating required clicking "Add Role" first; a role must exist to submit.)

- [X] FT-02: Team lead can edit an existing project's attributes
  - Action: Clicked "Edit" on "Data Analytics Dashboard", changed priority Medium → High, added required skill "GraphQL" (via new role "Analytics Engineer"), and saved.
  - Expected: The project detail/list re-displays the updated priority and the added skill; the change persists when the page is revisited.
  - Verified: Detail showed "High", "1/3 roles filled", Analytics Engineer/GraphQL; navigating to the list and back re-displayed "High" and the added role/skill. (Caveat observed: state is session-only in memory — a full browser reload reverts all edits/projects/assignments to defaults, which also caused the new project from FT-01 to disappear.)

- [X] FT-03: Employee list displays each employee's skills and availability
  - Action: Opened /employees and inspected all 8 employee cards.
  - Expected: Every employee entry shows a skills list and an availability status, not blank or placeholder values.
  - Verified: Each card shows name, title, email, a "Skills" chip list (e.g., React/TypeScript/GraphQL), and an availability badge ("Available" / "Partially Available" / "Unavailable").

- [X] FT-04: Employee list is searchable by name
  - Action: Typed "Mic" into "Search by name, email, or title...".
  - Expected: The list narrows to matching employee(s) only; the typed name match is visible in the results.
  - Verified: List narrowed to exactly one card: "Michael Brown" (live filtering, no submit needed).

- [X] FT-05: Employee list is filterable by skill and/or availability
  - Action: Selected skill filter "React" from the "All Skills" combobox.
  - Expected: Only employees matching the selected filter remain, and each result visibly possesses that skill.
  - Verified: Only Sarah Chen, David Kim, and James Wilson remained; each card visibly lists "React" among skills. (An "All Availability" filter also exists.)

- [X] FT-06: Lead can assign an employee to a project role
  - Action: On "Data Analytics Dashboard" (partially staffed), clicked "Assign Employee" on the open Frontend Developer role, picked available "Sarah Chen" (2/2 skills matched), confirmed.
  - Expected: The role row now shows the assigned employee's name; the project is listed under that employee's assignments.
  - Verified: Role card showed "Sarah Chen / Senior Frontend Developer", count updated to 2/3, and her /employees card listed "Current Projects: Data Analytics Dashboard".

- [ ] FT-07: Lead can reassign an employee to a different role or project
  - Action: Took Michael Brown (default assignee of "Backend Developer" on Data Analytics Dashboard), opened the assignment dialog for "Backend Developer" on API Gateway Migration and clicked Assign (the only cross-project control — no dedicated "Reassign" button exists; the assigned-row icon buttons are "open assign dialog" and "Unassign").
  - Expected: The employee appears only in the new role; the original role reverts to "unfilled/open."
  - Bug Report:
    - Issue: Missing reassignment semantics — cross-project assignment does not release the original role; employee ends up double-assigned.
    - Actual: After assigning Michael to API Gateway, the Projects list still showed Data Analytics Dashboard at "1/2 Partial", and its detail page still showed "Michael Brown" in the Backend Developer role while he also appeared in API Gateway's role. The original role reverted to open only after manually clicking "Unassign".

- [X] FT-08: Staffing overview shows the three staffing states for projects
  - Action: Opened the Dashboard with projects in differing staffing levels (2/3, 2/3, 2/2, 1/2, and earlier 0/2).
  - Expected: Each project is visibly labeled "Fully Staffed," "Partially Staffed," or "Unstaffed," and at least projects in differing staffing levels are shown with the correct label relative to their filled vs. open roles.
  - Verified: Every overview card carries a staffing badge matching its filled/open ratio: "Fully Staffed" (2/2), "Partial" (2/3, 1/2), "Unstaffed" (0/2), plus summary tiles (Total 4, Fully Staffed 1, Need Attention "3 partial, 0 unstaffed"). Note: the partially-staffed badge renders as "Partial" (also on the projects table), an abbreviation of "Partially Staffed" used consistently across the app.

## Constraint
- [ ] CS-01: Project cannot be saved while required fields are empty
  - Action: Opened "New Project", left Project Name/Description (and all other fields) empty, clicked "Create Project".
  - Expected: Submission is blocked, an inline validation message names the missing field(s), and no incomplete project appears in the list.
  - Bug Report:
    - Issue: Missing field-level/inline validation feedback.
    - Actual: Submission was correctly blocked (dialog stayed open, no project added), but the only feedback was a generic toast "Please fill in all required fields". DOM inspection of the dialog confirmed no inline error messages, no `aria-invalid` attributes, and no error-styled field borders identifying which fields are missing.

- [X] CS-02: Staffing status recalculates automatically when assignments change
  - Action: On "Data Analytics Dashboard", assigned employees until all roles were filled (2/3 → 3/3), then clicked "Unassign" on one employee.
  - Expected: The project's overview label changes to "Fully Staffed" when the last role is filled, and back to "Partially Staffed" after the unassignment — without requiring a manual refresh step.
  - Verified: On the last assign, badge changed in place "Partial" → "Fully Staffed" and count 2/3 → 3/3; after unassign, "Fully Staffed" → "Partial" and 3/3 → 2/3. No reload or refresh performed. (State recalculates live; fully-staffed label exact, partial shown as "Partial" as in FT-08.)

- [ ] CS-03: An employee cannot remain doubly assigned after reassignment
  - Action: Reassigned Michael Brown from Role A (Data Analytics Dashboard / Backend Developer) to Role B (API Gateway Migration / Backend Developer), then inspected both roles and the employee record.
  - Expected: The employee is listed only under Role B; Role A shows no assignment (or "Open"), and the employee record shows exactly one active project assignment.
  - Bug Report:
    - Issue: Double assignment allowed after cross-project reassignment; no uniqueness enforcement.
    - Actual: Role B displayed "Michael Brown", but Role A also continued displaying "Michael Brown" (proj-3 stayed "1/2 Partial" instead of becoming open/unfilled). The app intentionally treats capacity as "Partially Available" and permits the same employee in multiple simultaneous assignments; his card would show multiple "Current Projects" (e.g., David Kim legitimately lists 2). Role A cleared only via the separate manual "Unassign" action.

- [X] CS-04: Search and filter combine correctly and handle no-match cases
  - Action: With skill filter "React" active, typed "zzzqqq" into the employee search; then cleared the search and set the filter back to "All Skills".
  - Expected: The list shows an explicit "no results" (or empty-state) message rather than stale rows or an error, and clearing restores the full employee list.
  - Verified: Combined state rendered empty with explicit message "No employees found — Try adjusting your search or filters" (0 cards). After clearing, all 8 employee cards were restored.

## Interaction
- [X] IX-01: Success feedback is shown after creating/updating a project
  - Action: Saved the "New Project" form, then saved an edit on "Data Analytics Dashboard".
  - Expected: A confirmation appears each time (e.g., success toast/message such as "Project created" / "Project updated") and disappears without requiring a page reload.
  - Verified: Toast "Project created successfully" appeared, then toast "Project updated successfully" appeared; both were shown in the notification region and auto-dismissed (region empty in later snapshots) with no reload.

- [X] IX-02: Edit dialog is pre-filled with the project's current values
  - Action: Clicked "Edit" on projects and inspected the modal before changing anything.
  - Expected: The form opens (modal or inline panel) with the project's current name, skills, priority, and duration already populated; canceling leaves the project unchanged.
  - Verified: "Edit Project" modal opened pre-filled (e.g., name "Data Analytics Dashboard", Priority "Medium", Duration "8", Start Date "2024-03-01", and existing roles with "Skills: Python, SQL" / "Skills: React, TypeScript" chips). Clicking Cancel closed the dialog and the detail page still showed the original values.

- [X] IX-03: Assignment changes reflect in the UI immediately
  - Action: Assigned Sarah Chen to a role, then used "Unassign" on Emily Rodriguez.
  - Expected: The role row and any staffing label/count update in place right after each action (no stale display, no manual reload required).
  - Verified: After each assign/unassign the dialog closed automatically, the role card swapped between "Assign Employee" and the employee name, and the "x/y roles filled" count plus staffing badge updated instantly in the same view.

- [X] IX-04: Staffing states are visually distinguishable
  - Action: Viewed the Dashboard/Projects with projects in all three states and inspected badge computed styles.
  - Expected: "Fully Staffed," "Partially Staffed," and "Unstaffed" are rendered as distinct visual indicators (e.g., colored badges), not identical plain text.
  - Verified: Rounded badge components with distinct colors — Fully Staffed = green (text rgb(22,162,73), 10% green background), Partial = amber (rgb(245,159,10) / `bg-status-warning`), Unstaffed = red (rgb(239,67,67) / `bg-status-danger`).

## Content
- [X] CT-01: Default data is present and relevant on first load
  - Action: Opened http://localhost:6026/ fresh, without adding any data.
  - Expected: At least a few projects (with role slots) and a staff list of multiple employees are pre-loaded, and all content relates to internal project/staff management.
  - Verified: 4 realistic projects with role slots/descriptions loaded on Dashboard and /projects; /employees showed 8 employees with names, titles, company emails, skills, and assignments. No lorem ipsum or TODO placeholders found in any inspected view.

- [X] CT-02: Projects display required skills and expected duration meaningfully
  - Action: Inspected project list rows and detail pages (e.g., Data Analytics Dashboard, API Gateway Migration).
  - Expected: Required skills are shown as concrete, readable skill names and duration as a value with a unit, not empty or numeric-only fields.
  - Verified: Role cards displayed concrete skills ("Python", "SQL", "React", "TypeScript", "DevOps", "AWS", "Node.js", "GraphQL"); duration displayed as "12 weeks", "8 weeks", "6 weeks", and on detail pages "8 weeks duration".

- [X] CT-03: Priority values are rendered as human-readable labels
  - Action: Checked the projects table/detail badges and the create/edit form's Priority control.
  - Expected: Priority appears as readable labels ("High" / "Medium" / "Low") rather than raw codes, and the labels used in the form match those shown in the list.
  - Verified: List/detail show "High", "Medium", "Low"; the form's Priority dropdown options are exactly High / Medium / Low (default Medium) — consistent labeling everywhere.

**Summary: 14 / 19 PASS.** Key defects: (1) no single-step reassign — cross-project assignment leaves the employee double-assigned (FT-07, CS-03); (2) validation is a generic toast only, with no inline/field-level error messaging (CS-01); (3) observation outside checklist scope: all data is in-memory only — a full page reload discards created/edited projects and assignments (partially impacts the "persists when revisited" expectation of FT-02, which passes for in-app navigation).