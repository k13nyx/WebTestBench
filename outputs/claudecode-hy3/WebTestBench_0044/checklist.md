# Test Checklist

## Functionality
- [ ] FT-01: Add a new job application to the personal list
  - Action: Open the add form and enter a company, role, date, status, and notes, then submit.
  - Expected: A new entry appears in the list with the entered details.

- [ ] FT-02: View all logged applications in a personal list
  - Action: Open the application's main page.
  - Expected: All previously logged applications are displayed in a single list.

- [ ] FT-03: Edit an existing application entry
  - Action: Select the edit option on an entry and change one or more details, then save.
  - Expected: The entry in the list updates to reflect the changes.

- [ ] FT-04: Delete an application entry
  - Action: Select the delete option on an entry and confirm.
  - Expected: The entry is removed from the list and no longer appears.

- [ ] FT-05: Set or change an application's status
  - Action: Set an entry's status to Applied, Interviewed, or Offered.
  - Expected: The entry displays the selected status.

- [ ] FT-06: Add or edit notes for an application
  - Action: Open an entry and enter brief notes, then save.
  - Expected: The notes are stored and associated with that application.

## Constraint
- [ ] CS-01: Add form blocks submission with missing required fields
  - Action: Attempt to submit the add form leaving company, role, or date empty.
  - Expected: Submission is blocked and a validation message indicates required fields.

- [ ] CS-02: Status is restricted to the defined values
  - Action: Attempt to set an entry's status to any value other than Applied, Interviewed, or Offered.
  - Expected: Only the three defined statuses are selectable; invalid values are rejected.

## Interaction
- [ ] IX-01: Show success confirmation after adding an application
  - Action: Submit a valid new application.
  - Expected: A success message or indicator confirms the entry was added.

- [ ] IX-02: Show success confirmation after editing an application
  - Action: Save changes to an existing entry.
  - Expected: A success message or indicator confirms the update was saved.

- [ ] IX-03: Confirm before deleting an application
  - Action: Select the delete option on an entry.
  - Expected: A confirmation prompt appears before the entry is removed.

## Content
- [ ] CT-01: Each list entry shows company, role, and date
  - Action: Inspect any entry in the list.
  - Expected: The entry displays the company name, role, and application date.

- [ ] CT-02: Status options labeled exactly as defined
  - Action: Open the status selector on an entry or the add form.
  - Expected: The options read exactly "Applied", "Interviewed", and "Offered".

- [ ] CT-03: Notes are visible and relevant per application
  - Action: Open an entry that has notes saved.
  - Expected: The saved notes are displayed and correspond to that application only.