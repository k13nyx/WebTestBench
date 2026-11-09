# Test Result

## Functionality
- [X] FT-01: Add a new application with company, role, and date
  - Action: Click "Add Application", enter Company "Acme Corp", Role "QA Engineer", Date 2026-11-01, then click "Save".
  - Expected: A new row shows Acme Corp, QA Engineer, and 2026-11-01.
- [X] FT-02: Add an application with a selected status and notes
  - Action: Click "Add Application", enter Company "Beta Inc", Role "Frontend Developer", a valid date, Status "Interviewed", and Notes "Recruiter call Monday", then click "Save".
  - Expected: The new row shows status "Interviewed", and the notes "Recruiter call Monday" are visible on that entry (in the row or its detail view).
- [X] FT-03: Edit an existing application
  - Action: Click "Edit" on the "Acme Corp" row, change Role to "Senior QA Engineer", then click "Save".
  - Expected: The row shows "Senior QA Engineer", and Company and Date are unchanged.
- [X] FT-04: Delete an application
  - Action: Click "Delete" on the "Beta Inc" row, then confirm the deletion.
  - Expected: The "Beta Inc" row is removed from the list.
- [X] FT-05: Change an application's status to each allowed value
  - Action: On the "Acme Corp" row, change the status dropdown to "Offered", then to "Applied", then back to "Offered".
  - Expected: The row shows each selected status in turn, with no error.
- [ ] FT-06: Changes persist after page reload
  - Action: After FT-03 and FT-05, reload the page.
  - Expected: The "Acme Corp" row still shows "Senior QA Engineer" and status "Offered".
  - Bug Report:
    - Issue: Data Not Persisted After Reload
    - Actual: After reloading http://localhost:6044/, the list reverted to the 4 default rows (Stripe, Notion, Linear, Figma). The "Acme Corp" row was gone, so it no longer showed "Senior QA Engineer" or "Offered". The header read "4 applications".

## Constraint
- [ ] CS-01: Company and Role are required
  - Action: Click "Add Application", leave Company blank, enter Role "QA Engineer" and a valid date, then click "Save". Repeat with Company filled and Role blank.
  - Expected: Each attempt is blocked with a message such as "Company is required" or "Role is required", and no new row is added.
  - Bug Report:
    - Issue: Missing Required-Field Message
    - Actual: With Company blank, the "Add Application" button stayed disabled and the dialog contained no "Company is required" text. With Company "Gamma Co" and Role blank, the button stayed disabled and no "Role is required" text appeared. No row was added in either case.
- [ ] CS-02: Date is required and must be a valid calendar date
  - Action: Click "Add Application", fill Company and Role, leave Date blank, and click "Save". Then enter Date 2026-02-30 and click "Save".
  - Expected: Each attempt is blocked with a date error message, and no new row is added.
  - Bug Report:
    - Issue: Missing Date Validation Message
    - Actual: With Date blank, "Add Application" stayed disabled and no date error text appeared. The date input rejected "2026-02-30" ("Malformed value"), leaving the field empty. "Add Application" stayed disabled and no error text appeared. No row was added.
- [ ] CS-03: Status can only be chosen from the predefined options
  - Action: Click the status control on any row, then try to type free text into it.
  - Expected: The control offers only "Applied", "Interviewed", and "Offered", and free text cannot be entered.
  - Bug Report:
    - Issue: Extra Status Option Offered
    - Actual: The status control (in the Add/Edit dialog; rows have no status control) lists four options: "Applied", "Interviewed", "Offered", and "Rejected". "Rejected" is not among the allowed values. Free text cannot be typed into the control.
- [ ] CS-04: Deleting requires confirmation, and cancelling keeps the entry
  - Action: Click "Delete" on the "Beta Inc" row, then click "Cancel" in the confirmation.
  - Expected: The "Beta Inc" row remains unchanged in the list.
  - Bug Report:
    - Issue: Unconfirmed Deletion
    - Actual: Clicking "Delete" on the "Beta Inc" row removed the entry immediately, with an "Application deleted" notification. No confirmation dialog appeared, so there was no "Cancel" to click, and the row was not kept.

## Interaction
- [X] IX-01: Success message appears after saving a new application
  - Action: Add a valid application (for example, FT-01 data) and click "Save".
  - Expected: A confirmation message is displayed without a page reload, and the new row appears in the list.
- [X] IX-02: Edit form is pre-filled with the current values
  - Action: Click "Edit" on the "Acme Corp" row.
  - Expected: The form shows the current Company, Role, Date, Status, and Notes for that entry.
- [X] IX-03: Cancelling an edit discards the changes
  - Action: Click "Edit" on the "Acme Corp" row, change Company to "Temp Name", then click "Cancel".
  - Expected: The form closes, and the row still shows "Acme Corp".
- [X] IX-04: Status change is reflected immediately on the row
  - Action: Change the status dropdown on any row to a different value.
  - Expected: The row's status display updates to the new value without a page reload.

## Content
- [X] CT-01: Displayed date matches the entered date
  - Action: Add or edit an application with Date 2026-11-01 and view its row.
  - Expected: The row shows November 1, 2026 (or 2026-11-01) with no off-by-one day shift.
- [ ] CT-02: Status labels are spelled and capitalized consistently
  - Action: Open the status dropdown on any row and compare it with the status label shown on the row.
  - Expected: Both use exactly "Applied", "Interviewed", and "Offered".
  - Bug Report:
    - Issue: Unexpected Status Label
    - Actual: The labels "Applied", "Interviewed", and "Offered" are spelled and capitalized consistently. The default "Figma" row and the dropdown also show "Rejected", which is not one of the expected labels.
- [X] CT-03: Default entries show complete, relevant job application data
  - Action: Load the main page and review every default row.
  - Expected: Each row shows Company, Role, Date, and Status with real values. No "undefined", "null", placeholder, or lorem ipsum text appears.
- [ ] CT-04: Notes display in full with line breaks preserved
  - Action: Edit the notes of a default entry to "Line one" followed by a new line "Line two", save, and view the entry.
  - Expected: Both lines are shown in full, on separate lines, with no truncation.
  - Bug Report:
    - Issue: Line Breaks Not Preserved
    - Actual: The saved notes contain "Line one\nLine two", but the notes element uses `white-space: normal`. It renders as "Line one Line two" on a single 20px line.
- [X] CT-05: Page heading identifies the page as a job application tracker
  - Action: Load the main page and read the page title and main heading.
  - Expected: The title or heading clearly refers to job applications (for example, "Job Application Tracker").

---

**Execution notes**
- The row has no inline status dropdown. Status changes were made through the Edit dialog, and the row updated immediately on save without a reload. FT-05 and IX-04 are marked PASS on that basis.
- FT-04 has no confirmation step, so only the expected outcome (row removed) was verified. The missing confirmation is recorded under CS-04.
- The Beta Inc entry used for FT-04/CS-04 was recreated after the reload lost the original data. Its role is "QA Engineer" rather than "Frontend Developer."