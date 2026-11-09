# Test Checklist

## Functionality
- [ ] FT-01: Add a new application with basic details
  - Action: Open the "Add Application" form, enter Company "Acme Corp", Role "Frontend Developer", Date "2026-11-01", and submit.
  - Expected: A new entry appears in the list showing "Acme Corp", "Frontend Developer", and the date 2026-11-01.
- [ ] FT-02: Edit an existing entry's details
  - Action: Click "Edit" on the "Acme Corp" entry, change the Role to "Senior Frontend Developer", and save.
  - Expected: The list entry now displays Role "Senior Frontend Developer"; other fields remain unchanged.
- [ ] FT-03: Delete an entry
  - Action: Click "Delete" on the "Acme Corp" entry and confirm (if a confirmation is shown).
  - Expected: The "Acme Corp" entry is removed from the list and no longer visible.
- [ ] FT-04: Change an application's status
  - Action: On an entry, set its status to "Interviewed" via the status control (dropdown, button, or selector).
  - Expected: The entry displays the status "Interviewed".
- [ ] FT-05: All three status options are selectable
  - Action: On an entry, cycle the status through "Applied", "Interviewed", and "Offered".
  - Expected: Each of the three statuses can be selected and is correctly displayed on the entry.
- [ ] FT-06: Add a brief note to an application
  - Action: Open the notes field/section for an entry and type "Recruiter call went well, follow up Friday", then save.
  - Expected: The note text is saved and displayed for that entry.
- [ ] FT-07: Edit an existing note
  - Action: Open the note of the same entry, change the text to "Second round scheduled for Nov 20", and save.
  - Expected: The entry now shows the updated note text.
- [ ] FT-08: Edited details persist after page reload
  - Action: Add an entry "Beta Inc / QA Engineer", set status "Offered", add a note, then reload the page.
  - Expected: After reload, the entry is still present with the same company, role, date, status, and note.
- [ ] FT-09: Deleted entry does not reappear after reload
  - Action: Delete an entry, then reload the page.
  - Expected: The deleted entry remains absent after the reload.

## Constraint
- [ ] CS-01: Company field cannot be submitted empty
  - Action: Open the add form, leave Company blank, fill Role and Date, and submit.
  - Expected: Submission is rejected with a visible validation message; no entry is created.
- [ ] CS-02: Role field cannot be submitted empty
  - Action: Open the add form, leave Role blank, fill Company and Date, and submit.
  - Expected: Submission is rejected with a visible validation message; no entry is created.
- [ ] CS-03: Status is restricted to defined values
  - Action: Open the status control on an entry and inspect the available options.
  - Expected: Only defined statuses (e.g., "Applied", "Interviewed", "Offered") are offered; an arbitrary free-text status cannot be entered.
- [ ] CS-04: Date field requires a valid date
  - Action: In the add form, enter an invalid or empty date (if editable as text) and submit.
  - Expected: Submission is rejected with a visible validation message; no entry is created.

## Interaction
- [ ] IX-01: New entry appears immediately after submission
  - Action: Submit a valid new application via the add form.
  - Expected: The list updates immediately to include the new entry without requiring a page reload.
- [ ] IX-02: Edit form pre-fills with current values
  - Action: Click "Edit" on an existing entry.
  - Expected: The edit form opens showing the entry's current Company, Role, Date, Status, and Notes values.
- [ ] IX-03: Delete requires confirmation or gives clear feedback
  - Action: Click "Delete" on an entry.
  - Expected: Either a confirmation prompt appears before removal, or a visible confirmation (e.g., toast) indicates the entry was deleted; the list updates accordingly.
- [ ] IX-04: Status change is reflected instantly with clear visual state
  - Action: Change an entry's status to "Offered".
  - Expected: The status label updates immediately on the entry, visually distinguished (e.g., badge/tag color) from other statuses.

## Content
- [ ] CT-01: Entry displays all core details
  - Action: Add an entry with Company "Gamma Ltd", Role "Data Analyst", Date "2026-10-15" and view it in the list.
  - Expected: The entry shows the company name, role title, and application date exactly as entered.
- [ ] CT-02: Saved notes content matches what was typed
  - Action: Save the note "Salary range discussed: 80-95k" on an entry and inspect the displayed note.
  - Expected: The displayed note text matches exactly, with no truncation that loses meaning and no corrupted characters.
- [ ] CT-03: Page content is relevant to job application tracking
  - Action: Load the main page and review headings, labels, and placeholder text.
  - Expected: All visible text relates to job application logging (e.g., "Applications", "Company", "Role", "Status", "Notes"); no irrelevant or lorem-ipsum content remains.