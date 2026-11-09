# Test Result

## Functionality
- [X] FT-01: Create a new project with all required details
  - Action: Opened the project creation form, entered project name "AI Chat Support", description, required skills (Python, Node.js on the "Backend Engineer" role), priority High, and expected duration 10 weeks, then saved.
  - Expected: The new project appears in the project list with the entered skills, priority, and duration.
- [X] FT-02: Edit an existing project's details
  - Action: Opened "AI Chat Support" → Edit, removed the old role, added role "Full Stack Engineer" with skills React + TypeScript, changed priority to Medium and duration to 14 weeks, then saved.
  - Expected: The project list reflects the updated skills, priority, and duration. (List showed Medium / 14 weeks; updated skills verified in the project detail view; toast "Project updated successfully" shown.)
- [X] FT-03: Search the employee list
  - Action: Typed "Sarah" into the employee search box.
  - Expected: The list narrows to only employees whose names match the query. (Only "Sarah Chen" remained.)
- [X] FT-04: Filter the employee list
  - Action: Cleared search, applied Availability filter "Available" and Skill filter "Python".
  - Expected: Only employees matching all selected filters are displayed, showing their skills and availability. (Only Lisa Thompson and Anna Petrova shown, each with skills + availability badge.)
- [X] FT-05: Assign an employee to a project role
  - Action: Opened AI Chat Support → "Assign Employee" on the Full Stack Engineer role and assigned Sarah Chen (Available, 2/2 skills matched).
  - Expected: The employee is listed under that project role, and their availability is reflected in the employee list. (Role shows Sarah Chen; employee list changed her from "Available" to "Partially Available" with "AI Chat Support" under Current Projects.)
- [X] FT-06: Reassign an employee to a different project role
  - Action: In the occupied Full Stack Engineer role, assigned Sarah Chen while David Kim was the occupant (replacement flow), then inspected the role and employee list.
  - Expected: The role shows the new assignment, and the previous assignment no longer lists that employee. (Role shows only Sarah Chen, 1/1; David Kim's employee card no longer lists AI Chat Support.)
- [X] FT-07: Staffing overview categorizes projects
  - Action: Viewed the project overview section on the Dashboard before and after assignment changes.
  - Expected: Each project is shown under exactly one of: fully staffed, partially staffed, or unstaffed, matching its current assignments. (Each card carries exactly one status badge matching its role fill: 2/3 Partial, 2/3 Partial, 1/2 Partial, 0/2 Unstaffed, 1/1 Fully Staffed, 0/1 Unstaffed; counts "Fully Staffed 1 / 3 partial / 2 unstaffed" are consistent.)
- [X] FT-08: Adjusting assignments updates staffing status
  - Action: Assigned James Wilson to the last open role of the partially staffed Data Analytics Dashboard (1/2), then removed him from the now fully staffed project.
  - Expected: The project moves to fully staffed after the first change and back to partially staffed (or unstaffed) after the second. (Status changed Partial → "Fully Staffed" 2/2 → "Partial" 1/2, immediately reflected on the project page and dashboard.)

## Constraint
- [ ] CS-01: Project creation requires all mandatory fields
  - Action: Attempted to save a new project with name and description left empty (role added so role validation passes).
  - Expected: The project is not saved, and an error message identifies the missing required field(s).
  - Bug Report:
    - Issue: Non-specific validation message / missing field identification
    - Actual: Save was blocked, but only a generic toast "Please fill in all required fields" appeared — it does not identify WHICH required field(s) are missing (Project Name vs. Description), and no per-field indication is shown.
- [ ] CS-02: Invalid project input is rejected
  - Action: Entered expected duration "0" (all other fields valid) and submitted the create form.
  - Expected: The project is not saved, and an error message explains the invalid value.
  - Bug Report:
    - Issue: Invalid input accepted (no validation of duration)
    - Actual: The project was saved successfully — toast "Project created successfully" appeared and a new project "Invalid Duration Test" was created with duration "1 weeks". No error message was shown for the zero/invalid duration.
- [ ] CS-03: Cannot assign an unavailable employee
  - Action: In the assign dialog, clicked "Assign" for David Kim, who is marked "Unavailable".
  - Expected: The assignment is blocked or the option is not selectable, with an explanation of why.
  - Bug Report:
    - Issue: Unavailable employee assignable (constraint not enforced)
    - Actual: David Kim's Assign button was enabled; clicking it succeeded with toast "Employee assigned successfully" and he was placed in the role (project became 1/1 Fully Staffed). No block, disabled state, or explanation was provided.
- [X] CS-04: Cannot fill a role with two employees
  - Action: With David Kim occupying the Full Stack Engineer role, opened the role's assign dialog and clicked "Assign" for Sarah Chen without unassigning first.
  - Expected: The action is rejected or explicitly replaces the current assignee; the role never shows two employees at once.
- [X] CS-05: Editing preserves data integrity
  - Action: Opened Edit on "AI Chat Support", changed name to "ZZZ Temp Name", duration to 99 and priority to Low, then clicked Cancel without saving.
  - Expected: The project's original values remain unchanged. (Detail view and list still showed AI Chat Support / High / 10 weeks with original role skills.)

## Interaction
- [X] IX-01: Saving a project gives clear feedback
  - Action: Created and later edited a project successfully.
  - Expected: A visible success confirmation (e.g., toast or message) appears, and the project list updates immediately without a manual refresh. ("Project created successfully" and "Project updated successfully" toasts appeared; new/updated rows rendered immediately.)
- [ ] IX-02: Validation errors are shown inline
  - Action: Submitted the create form with missing required fields (empty name/description) and with an invalid duration.
  - Expected: Error messages appear next to the offending fields and the form remains open with entered data preserved.
  - Bug Report:
    - Issue: Validation errors not shown inline next to fields
    - Actual: No error text appeared next to any field — only a generic toast "Please fill in all required fields" (and for invalid duration, no message at all). The form did remain open with entered data preserved, but errors are not displayed at the offending fields and do not name them.
- [X] IX-03: Search and filters respond immediately
  - Action: Typed character-by-character in the employee search box and toggled availability/skill filters.
  - Expected: The employee list updates reactively as input changes, with no page reload required. (List filtered live on each keystroke/selection; URL stayed /employees with no reload.)
- [X] IX-04: Assignment changes give immediate feedback
  - Action: Assigned, replaced, and removed employees on project roles.
  - Expected: The role list, employee availability, and staffing overview all update immediately and a confirmation message is shown. (Toasts "Employee assigned successfully" / "Employee unassigned"; role cards, "x/y roles filled", status badges, dashboard counts and Available Staff 4→3 all updated instantly.)

## Content
- [X] CT-01: Employee cards show complete, accurate details
  - Action: Inspected the employee list (before and after clearing filters and after assignment changes).
  - Expected: Every employee entry displays their name, skills, and availability status, and the data matches their actual assignment state. (All 8 employees show name, title, email, skills, availability badge and Current Projects; e.g., Sarah Chen updated to "Partially Available / AI Chat Support" after assignment, James Wilson's Data Analytics assignment removed after unassign.)
- [ ] CT-02: Project list displays all specified attributes
  - Action: Viewed the project list and opened detail/edit views of a project (including reopening Edit after a cancelled edit).
  - Expected: Each project clearly shows its required skills, priority level, and expected duration, consistent between the list and detail/edit views.
  - Bug Report:
    - Issue: Missing data in list + stale/inconsistent edit view
    - Actual: (1) The project list table shows only Priority, Duration, Roles and Status — required skills are never displayed in the list, only per-role in the detail view. (2) After cancelling an edit (name "ZZZ Temp Name", Low, 99 weeks), reopening Edit showed those discarded values (Low / 99 weeks) while the list and detail view showed the actual values (High / 10 weeks) — list and edit views are inconsistent.
- [X] CT-03: Staffing overview labels are unambiguous
  - Action: Reviewed the Dashboard overview section (stat cards and Projects Overview cards).
  - Expected: The three categories (fully staffed, partially staffed, unstaffed) are clearly labeled, and each project appears under the correct category with its role-fill status visible (e.g., "3/4 roles filled"). (Labels "Fully Staffed" / "Partial" / "Unstaffed" plus summary counts "Fully Staffed: 1", "5 — 3 partial, 2 unstaffed"; every card shows role-fill status such as "2/3 roles filled", "1/1 roles filled".)
