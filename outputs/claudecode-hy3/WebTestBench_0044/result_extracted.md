# Test Result

## Functionality
- [X] FT-01: Add a new job application to the personal list
  - Action: Open the add form and enter a company, role, date, status, and notes, then submit.
  - Expected: A new entry appears in the list with the entered details.

- [X] FT-02: View all logged applications in a personal list
  - Action: Open the application's main page.
  - Expected: All previously logged applications are displayed in a single list.

- [X] FT-03: Edit an existing application entry
  - Action: Select the edit option on an entry and change one or more details, then save.
  - Expected: The entry in the list updates to reflect the changes.

- [X] FT-04: Delete an application entry
  - Action: Select the delete option on an entry and confirm.
  - Expected: The entry is removed from the list and no longer appears.

- [X] FT-05: Set or change an application's status
  - Action: Set an entry's status to Applied, Interviewed, or Offered.
  - Expected: The entry displays the selected status.

- [X] FT-06: Add or edit notes for an application
  - Action: Open an entry and enter brief notes, then save.
  - Expected: The notes are stored and associated with that application.

## Constraint
- [ ] CS-01: Add form blocks submission with missing required fields
  - Action: Attempt to submit the add form leaving company, role, or date empty.
  - Expected: Submission is blocked and a validation message indicates required fields.
  - Bug Report:
    - Issue: Missing validation/required-field message (silent block)
    - Actual: Submission is blocked because the "Add Application" submit button is rendered `disabled` when required fields are empty, but no validation message, error text, or aria-invalid indicator appears. DOM inspection shows `hasRequiredMsg: false` and the dialog text contains no "required"/"invalid" notice — the user receives no explicit feedback about which required fields are missing.

- [ ] CS-02: Status is restricted to the defined values
  - Action: Attempt to set an entry's status to any value other than Applied, Interviewed, or Offered.
  - Expected: Only the three defined statuses are selectable; invalid values are rejected.
  - Bug Report:
    - Issue: Invalid status value is selectable
    - Actual: The status selector (both Add and Edit forms) offers a fourth option "Rejected" in addition to Applied, Interviewed, and Offered. A value outside the three defined statuses is therefore selectable and not rejected.

## Interaction
- [X] IX-01: Show success confirmation after adding an application
  - Action: Submit a valid new application.
  - Expected: A success message or indicator confirms the entry was added.

- [X] IX-02: Show success confirmation after editing an application
  - Action: Save changes to an existing entry.
  - Expected: A success message or indicator confirms the update was saved.

- [ ] IX-03: Confirm before deleting an application
  - Action: Select the delete option on an entry.
  - Expected: A confirmation prompt appears before the entry is removed.
  - Bug Report:
    - Issue: No confirmation prompt (immediate destructive action)
    - Actual: Clicking the delete button removed the entry immediately. The application count dropped from 5 to 4 and a success toast "Application deleted — The application has been removed from your list." appeared, with no confirmation dialog/prompt shown before removal.

## Content
- [X] CT-01: Each list entry shows company, role, and date
  - Action: Inspect any entry in the list.
  - Expected: The entry displays the company name, role, and application date.

- [ ] CT-02: Status options labeled exactly as defined
  - Action: Open the status selector on an entry or the add form.
  - Expected: The options read exactly "Applied", "Interviewed", and "Offered".
  - Bug Report:
    - Issue: Extra status option present (deviation from "exactly")
    - Actual: The status selector lists four options — "Applied", "Interviewed", "Offered", and an additional "Rejected" — so the options do not read exactly the three defined values.

- [X] CT-03: Notes are visible and relevant per application
  - Action: Open an entry that has notes saved.
  - Expected: The saved notes are displayed and correspond to that application only.
