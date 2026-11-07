# Test Checklist

## Functionality
- [ ] FT-01: Default applications are listed on page load
  - Action: Open the application list page.
  - Expected: Existing default entries are displayed, each showing its company, role, date, status, and notes.

- [ ] FT-02: New application can be added with company, role, and date
  - Action: Click the add button, enter a company, a role, and a date, then submit.
  - Expected: The form submits successfully and the new entry is created.

- [ ] FT-03: Newly added application appears in the list
  - Action: After adding an entry, view the list.
  - Expected: The new entry is listed with the company, role, and date that were entered.

- [ ] FT-04: An existing application can be edited
  - Action: Open the edit view for any listed entry, change the company and role, then save.
  - Expected: The saved entry displays the updated company and role in the list.

- [ ] FT-05: An application can be deleted
  - Action: Delete any listed entry.
  - Expected: The entry is removed from the list and is no longer shown anywhere on the page.

- [ ] FT-06: Status can be changed for an application
  - Action: Change the status of a listed entry to "interviewed", then to "offered".
  - Expected: The entry displays the newly selected status each time.

- [ ] FT-07: Notes can be added to an application and are shown
  - Action: Open an entry and enter note text such as "Recruiter called on Monday", then save.
  - Expected: The entered note text is displayed for that entry.

- [ ] FT-08: Application data persists after a page reload
  - Action: Add an entry with a note and a status, then reload the page.
  - Expected: The entry is still present with the same company, role, date, status, and note.

## Constraint
- [ ] CS-01: Company is required when adding an application
  - Action: Open the add form, leave company empty, fill role and date, then submit.
  - Expected: Submission is blocked, no new entry is created, and the company field is flagged.

- [ ] CS-02: Role is required when adding an application
  - Action: Open the add form, leave role empty, fill company and date, then submit.
  - Expected: Submission is blocked, no new entry is created, and the role field is flagged.

- [ ] CS-03: Date is required and must be a valid date when adding an application
  - Action: Open the add form, leave date empty (then repeat with an invalid date value), fill company and role, then submit.
  - Expected: Submission is blocked in both cases, no entry is created, and the date field is flagged.

- [ ] CS-04: Status is limited to the defined set of values
  - Action: Inspect the status control for any application.
  - Expected: Only the options applied, interviewed, and offered are selectable, and every entry holds one of these three values.

## Interaction
- [ ] IX-01: Add form can be opened and dismissed
  - Action: Click the add button, then close/dismiss the form without saving.
  - Expected: The form opens on click and closes on dismiss, leaving the list unchanged.

- [ ] IX-02: Success feedback is shown after adding an application
  - Action: Add a valid application.
  - Expected: A success confirmation (message or highlight) appears and the form resets or closes.

- [ ] IX-03: Validation feedback is shown on an invalid submission
  - Action: Submit the add form with a required field empty.
  - Expected: A visible error message identifies the missing field; the form stays open so it can be corrected.

- [ ] IX-04: Edit form is pre-filled with the entry's current values
  - Action: Open the edit view for an existing entry.
  - Expected: The form fields show the entry's saved company, role, date, status, and notes.

- [ ] IX-05: Deleting an entry requires a confirmation step
  - Action: Click delete on an entry, then dismiss/cancel the confirmation.
  - Expected: The entry is not removed when the action is cancelled.

## Content
- [ ] CT-01: Default list entries contain complete, job-application-relevant details
  - Action: Review every default entry shown on page load.
  - Expected: Each shows a company name, a role, a date, a status, and notes text; no placeholder or filler text such as "Lorem ipsum" appears.

- [ ] CT-02: Status values are labeled exactly as applied, interviewed, and offered
  - Action: Read the status labels on entries and in the status control.
  - Expected: Labels use these exact words and match the status shown on each entry.

- [ ] CT-03: Saved notes are displayed in full
  - Action: Save a long multi-line note on an entry, then view the entry.
  - Expected: The full note text is readable and is not truncated, hidden, or replaced by placeholder text.