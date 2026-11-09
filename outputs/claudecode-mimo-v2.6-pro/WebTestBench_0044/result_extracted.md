# Test Result

## Functionality
- [X] FT-01: User can add a new application entry via the add form.
  - Action: Fill in the new-application form with a company name, role, and date, then click the "Add" button.
  - Expected: A new entry appears in the applications list displaying the entered company, role, and date.
- [X] FT-02: User can edit an existing application entry.
  - Action: Click "Edit" on an existing entry, change its company/role/date values, and save the changes.
  - Expected: The entry in the list is updated to show the new values.
- [X] FT-03: User can delete an application entry.
  - Action: Click "Delete" on an existing entry.
  - Expected: The entry is removed from the applications list.
- [X] FT-04: User can set the status of an application to "Applied", "Interviewed", or "Offered".
  - Action: On an entry, select the "Offered" status option.
  - Expected: The entry displays the status "Offered".
- [X] FT-05: User can save brief notes for an application.
  - Action: Enter text into the notes field of an entry and save.
  - Expected: The entered note text is stored and displayed for that entry.

## Constraint
- [ ] CS-01: An application cannot be saved without a company, role, and date.
  - Action: Leave company, role, or date empty and submit the add form.
  - Expected: The entry is not created and a validation message indicates the missing required field.
  - Bug Report:
    - Issue: Missing Validation Message
    - Actual: With company/role empty (and separately with the date cleared), the "Add Application" submit button remains disabled and pressing Enter in the form fields produces no response — the entry is correctly not created, but no validation message appears anywhere in the dialog indicating the missing required field (DOM scan for `[role="alert"]`, `.error`, and error-class elements returned zero messages in every tested state).
- [ ] CS-02: Status is restricted to the allowed values (Applied, Interviewed, Offered).
  - Action: Inspect the status control on an entry and attempt to set a value outside the three allowed statuses.
  - Expected: Only "Applied", "Interviewed", and "Offered" can be selected; no other value can be assigned to a status.
  - Bug Report:
    - Issue: Unrestricted Status Values (Invalid Option Selectable)
    - Actual: The status control's dropdown lists four options — "Applied", "Interviewed", "Offered", and "Rejected". Selecting the out-of-range value "Rejected" succeeded: the edit form's Status control displayed "Rejected" as the set value, and the pre-existing Figma entry displays status "Rejected", proving a value outside the three allowed statuses can be assigned.
- [X] CS-03: Deleting one entry does not affect other entries.
  - Action: Note the list contents, delete one entry, then review the remaining entries.
  - Expected: All other entries remain present with their company, role, date, status, and notes unchanged.
- [X] CS-04: Editing an entry preserves its unchanged fields.
  - Action: Edit an entry and modify only the role, saving without touching notes or status.
  - Expected: The notes, status, company, and date of that entry remain unchanged after saving.

## Interaction
- [ ] IX-01: Confirmation is required before deleting an entry.
  - Action: Click "Delete" on an entry.
  - Expected: A confirmation prompt appears and the entry is deleted only after confirming; cancelling the prompt leaves the entry intact.
  - Bug Report:
    - Issue: Missing Delete Confirmation Prompt
    - Actual: Clicking the Delete button on the "Acme International" entry deleted it immediately in the same action — the toast "Application deleted: The application has been removed from your list." appeared and the header count changed from "5 applications" to "4 applications" with no confirmation prompt displayed at any point; the entry is deleted without any confirmation and there is no prompt to cancel.
- [X] IX-02: The applications list updates immediately after add, edit, or delete.
  - Action: Perform an add, then an edit, then a delete, observing the list after each action.
  - Expected: The list reflects each change right after the action completes, without requiring a manual page reload.
- [X] IX-03: Canceling an edit discards the changes.
  - Action: Click "Edit" on an entry, change a value, then click "Cancel".
  - Expected: The entry displays its original values and no change is saved.

## Content
- [X] CT-01: Each entry displays its company, role, and date as entered.
  - Action: Create an entry with a known company, role, and date, then view the list.
  - Expected: The list shows the exact company name, role, and date that were entered.
- [X] CT-02: The status shown on an entry matches the status that was set.
  - Action: Set an entry's status to "Interviewed" and view the entry in the list.
  - Expected: The entry clearly displays "Interviewed" as its status.
- [X] CT-03: The notes shown for an entry match the notes that were entered.
  - Action: Save a known note text for an entry and view the entry.
  - Expected: The entry displays exactly the note text that was entered, with no truncation or content from another entry.
