# Test Checklist

## Functionality
- [ ] FT-01: View the personal list of job applications
  - Action: Open the website's main page.
  - Expected: A list of job applications is displayed showing company, role, date, status, and notes for each entry.

- [ ] FT-02: Add a new application with basic details
  - Action: Open the "Add application" form, enter company "Acme Corp", role "QA Engineer", date "2026-11-01", and save.
  - Expected: The form saves successfully and a new entry for "Acme Corp" / "QA Engineer" / "2026-11-01" exists in the list.

- [ ] FT-03: Assign a status when creating an application
  - Action: While adding a new application, select status "Applied" and save.
  - Expected: The saved entry displays the status "Applied".

- [ ] FT-04: Add notes to an application
  - Action: While adding a new application, enter the note "Referral from John" and save.
  - Expected: The entry displays the note text "Referral from John".

- [ ] FT-05: Edit an existing application's details
  - Action: Open the edit form for an existing entry, change the role to "Senior QA Engineer" and save.
  - Expected: The list now shows "Senior QA Engineer" for that entry; other fields remain unchanged.

- [ ] FT-06: Change the status of an existing application
  - Action: Edit an entry with status "Applied" and change its status to "Interviewed".
  - Expected: The entry now displays the status "Interviewed".

- [ ] FT-07: Edit an application's notes
  - Action: Edit an existing entry, replace its note with "Second round scheduled for Friday" and save.
  - Expected: The entry now displays exactly "Second round scheduled for Friday".

- [ ] FT-08: Delete an application
  - Action: Click the delete control on an existing entry and confirm.
  - Expected: That entry is removed from the list; all other entries remain.

## Constraint
- [ ] CS-01: Cannot save an application with empty company or role
  - Action: Open the add form, leave Company and/or Role empty, attempt to save.
  - Expected: Saving is blocked and an error message points to the empty required field; no new entry is added.

- [ ] CS-02: Cannot save an application without a date
  - Action: Open the add form, fill company and role but leave the date empty, attempt to save.
  - Expected: Saving is blocked with a validation message for the date; no new entry is added.

- [ ] CS-03: Status is limited to the allowed values
  - Action: Open the add form and inspect the status choices; then attempt to save with no status selected.
  - Expected: Only "Applied", "Interviewed", and "Offered" are selectable, and saving without a status is blocked (or a valid default is applied automatically).

- [ ] CS-04: Cancelled edits do not modify data
  - Action: Open the edit form of an existing entry, change the company name, then click Cancel.
  - Expected: The entry's data in the list is unchanged.

- [ ] CS-05: Deleting removes only the targeted entry
  - Action: With at least two entries present, delete the first one.
  - Expected: Only the first entry disappears; the second entry's company, role, date, status, and notes are unchanged.

## Interaction
- [ ] IX-01: New entry appears immediately after saving
  - Action: Save a newly filled add form.
  - Expected: The new entry appears in the list without reloading the page.

- [ ] IX-02: Edit form is pre-filled with the entry's current data
  - Action: Click edit on an existing entry.
  - Expected: Company, role, date, status, and notes fields show that entry's current values before any change.

- [ ] IX-03: Feedback is shown after add, edit, and delete
  - Action: Perform an add, then an edit, then a delete.
  - Expected: Each action produces a visible confirmation (e.g., success toast/message) identifying that the operation completed.

- [ ] IX-04: Delete asks for confirmation
  - Action: Click the delete control on an entry.
  - Expected: A confirmation prompt appears before removal; cancelling the prompt keeps the entry in the list.

## Content
- [ ] CT-01: Entered data is displayed accurately and verbatim
  - Action: Add an entry with company "Globex", role "Data Analyst", date "2026-10-15", note "Ask about remote policy".
  - Expected: The list row shows exactly "Globex", "Data Analyst", "2026-10-15" (as entered or equivalent unambiguous format), and the note text unchanged, with no missing or garbled characters.

- [ ] CT-02: Status labels use the exact terms
  - Action: Create three entries with statuses "Applied", "Interviewed", and "Offered" and view the list.
  - Expected: Each entry displays its status using exactly one of those three terms, with no abbreviations, codes, or placeholder values.

- [ ] CT-03: Notes field content is fully visible when reviewing an entry
  - Action: Open/view an entry whose note is a multi-sentence line, e.g. "Recruiter called. Team of 6. Next step: take-home task."
  - Expected: The complete note text is readable in the interface without truncation hiding content (scrolling or expansion within the entry is acceptable).