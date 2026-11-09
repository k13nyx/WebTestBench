# Test Checklist

## Functionality
- [ ] FT-01: User can add a new job application with company, role, and date
  - Action: Click "Add Application", enter Company "Acme Corp", Role "Software Engineer", Date "2026-11-08", and save.
  - Expected: The new entry appears in the application list showing "Acme Corp", "Software Engineer", and "2026-11-08".

- [ ] FT-02: User can edit an existing application's details
  - Action: Click "Edit" on an existing entry, change Role to "Senior Engineer", and save.
  - Expected: The entry in the list shows the updated role "Senior Engineer"; company and date remain unchanged.

- [ ] FT-03: User can delete an application
  - Action: Click "Delete" on an existing entry and confirm the deletion.
  - Expected: The entry is removed and no longer appears anywhere in the list.

- [ ] FT-04: User can assign a status when adding an application
  - Action: Add an application and set its status to "Interviewed" before saving.
  - Expected: The saved entry displays the status "Interviewed".

- [ ] FT-05: User can change the status of an existing application
  - Action: Change an entry's status from "Applied" to "Offered" and reload the page.
  - Expected: The entry still displays "Offered" after the page reloads.

- [ ] FT-06: User can add notes to an application
  - Action: Open an application, enter the note "Recruiter: Jane — follow up Friday", and save.
  - Expected: The note is saved and displayed when that application is reopened.

- [ ] FT-07: User can edit existing notes
  - Action: Open an application that already has a note, change the text, and save.
  - Expected: The updated note text is displayed; the previous text is replaced.

- [ ] FT-08: Saved applications persist after a page reload
  - Action: Add an entry, then refresh the browser.
  - Expected: All previously saved entries and their details are still listed.

## Constraint
- [ ] CS-01: Application cannot be saved with empty required fields
  - Action: Leave Company, Role, or Date blank and click save.
  - Expected: The entry is not created and a validation message identifies the missing field(s).

- [ ] CS-02: Application cannot be saved with an invalid date
  - Action: Enter an invalid date such as "13/45/2026" in the Date field and save.
  - Expected: The entry is not created and a date validation message is shown.

- [ ] CS-03: Status is limited to the allowed values
  - Action: Open the status selector for an application.
  - Expected: Only "Applied", "Interviewed", and "Offered" are selectable; no other status can be saved.

- [ ] CS-04: Cancelling a delete preserves the entry
  - Action: Click "Delete" on an entry and choose "Cancel" in the confirmation prompt.
  - Expected: The entry remains in the list, unchanged.

- [ ] CS-05: Whitespace-only input is rejected
  - Action: Enter only spaces in the Company field and save.
  - Expected: The entry is not created and a required-field validation message is shown.

## Interaction
- [ ] IX-01: Success confirmation appears after adding an application
  - Action: Add a valid application and save.
  - Expected: A success message (e.g., "Application added") is displayed.

- [ ] IX-02: Edit form opens pre-filled with current values
  - Action: Click "Edit" on an entry that has a company, role, date, status, and note.
  - Expected: The form opens with every field populated with that entry's existing values.

- [ ] IX-03: Delete requires an explicit confirmation step
  - Action: Click "Delete" on an entry.
  - Expected: A confirmation prompt appears with "Confirm" and "Cancel" options before anything is removed.

- [ ] IX-04: Add form clears after a successful save
  - Action: Add a valid application and save.
  - Expected: The form fields are emptied or the form closes, so the same data is not accidentally resubmitted.

## Content
- [ ] CT-01: All required fields are clearly labeled
  - Action: Open the add/edit application form.
  - Expected: Visible labels exist for "Company", "Role", "Date", "Status", and "Notes".

- [ ] CT-02: Status options use the exact expected terms
  - Action: Inspect the status options in the form.
  - Expected: The options read exactly "Applied", "Interviewed", and "Offered".

- [ ] CT-03: Listed content is relevant and accurately displayed
  - Action: Review the application list and an application's notes.
  - Expected: Every entry shows real application data with no placeholder/lorem text, and notes are shown in full without truncation.