# Test Checklist

## Functionality
- [ ] FT-01: User can add a new application entry via the add form.
  - Action: Fill in the new-application form with a company name, role, and date, then click the "Add" button.
  - Expected: A new entry appears in the applications list displaying the entered company, role, and date.
- [ ] FT-02: User can edit an existing application entry.
  - Action: Click "Edit" on an existing entry, change its company/role/date values, and save the changes.
  - Expected: The entry in the list is updated to show the new values.
- [ ] FT-03: User can delete an application entry.
  - Action: Click "Delete" on an existing entry.
  - Expected: The entry is removed from the applications list.
- [ ] FT-04: User can set the status of an application to "Applied", "Interviewed", or "Offered".
  - Action: On an entry, select the "Offered" status option.
  - Expected: The entry displays the status "Offered".
- [ ] FT-05: User can save brief notes for an application.
  - Action: Enter text into the notes field of an entry and save.
  - Expected: The entered note text is stored and displayed for that entry.

## Constraint
- [ ] CS-01: An application cannot be saved without a company, role, and date.
  - Action: Leave company, role, or date empty and submit the add form.
  - Expected: The entry is not created and a validation message indicates the missing required field.
- [ ] CS-02: Status is restricted to the allowed values (Applied, Interviewed, Offered).
  - Action: Inspect the status control on an entry and attempt to set a value outside the three allowed statuses.
  - Expected: Only "Applied", "Interviewed", and "Offered" can be selected; no other value can be assigned to a status.
- [ ] CS-03: Deleting one entry does not affect other entries.
  - Action: Note the list contents, delete one entry, then review the remaining entries.
  - Expected: All other entries remain present with their company, role, date, status, and notes unchanged.
- [ ] CS-04: Editing an entry preserves its unchanged fields.
  - Action: Edit an entry and modify only the role, saving without touching notes or status.
  - Expected: The notes, status, company, and date of that entry remain unchanged after saving.

## Interaction
- [ ] IX-01: Confirmation is required before deleting an entry.
  - Action: Click "Delete" on an entry.
  - Expected: A confirmation prompt appears and the entry is deleted only after confirming; cancelling the prompt leaves the entry intact.
- [ ] IX-02: The applications list updates immediately after add, edit, or delete.
  - Action: Perform an add, then an edit, then a delete, observing the list after each action.
  - Expected: The list reflects each change right after the action completes, without requiring a manual page reload.
- [ ] IX-03: Canceling an edit discards the changes.
  - Action: Click "Edit" on an entry, change a value, then click "Cancel".
  - Expected: The entry displays its original values and no change is saved.

## Content
- [ ] CT-01: Each entry displays its company, role, and date as entered.
  - Action: Create an entry with a known company, role, and date, then view the list.
  - Expected: The list shows the exact company name, role, and date that were entered.
- [ ] CT-02: The status shown on an entry matches the status that was set.
  - Action: Set an entry's status to "Interviewed" and view the entry in the list.
  - Expected: The entry clearly displays "Interviewed" as its status.
- [ ] CT-03: The notes shown for an entry match the notes that were entered.
  - Action: Save a known note text for an entry and view the entry.
  - Expected: The entry displays exactly the note text that was entered, with no truncation or content from another entry.