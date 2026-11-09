# Test Checklist

## Functionality
- [ ] FT-01: User can add a new application with company, role, and date
  - Action: Open the add-entry control, enter company "Acme Corp", role "Backend Engineer", a date, and submit.
  - Expected: A new entry appears in the list showing "Acme Corp", "Backend Engineer", and the chosen date.
- [ ] FT-02: User can edit an existing application's details
  - Action: Open the edit control on a default entry, change the role to "Data Analyst", and save.
  - Expected: The same entry now shows "Data Analyst" in the list; other entries are unchanged.
- [ ] FT-03: User can delete an existing application
  - Action: Trigger delete on one default entry and confirm.
  - Expected: That entry is removed from the list and no longer appears; the total entry count decreases by one.
- [ ] FT-04: User can set an application's status to applied, interviewed, or offered
  - Action: For a default entry, set status to "Interviewed", then change it to "Offered".
  - Expected: The entry's status reads "Interviewed", then "Offered" — the latest selection is stored.
- [ ] FT-05: User can record notes for an application and view them
  - Action: Add the note "Referred by recruiter, follow up Monday" to a default entry, then view the list/entry details.
  - Expected: The note text is displayed attached to that specific application.
- [ ] FT-06: The personal list displays all tracked applications with their core details
  - Action: Load the page and inspect the list.
  - Expected: Every application is listed with company, role, date, and status visible together.
- [ ] FT-07: Logged applications persist across a page reload
  - Action: Add one application with a note, then reload the page.
  - Expected: The newly added application (including its note) is still present after reload.

## Constraint
- [ ] CS-01: An application cannot be saved when required fields are missing
  - Action: Open the add form, leave company (or role/date) blank, and submit.
  - Expected: Submission is blocked with a validation message naming the missing field; no new entry appears.
- [ ] CS-02: An invalid date is rejected
  - Action: Enter an impossible/out-of-format value (e.g. "13/45/2026" or free text) in the date field and submit.
  - Expected: The entry is not created and an error indicates the date is invalid.
- [ ] CS-03: Status is limited to the defined set
  - Action: Attempt to set an entry's status to something outside "Applied / Interviewed / Offered" (typed free text or a fourth option).
  - Expected: No such status can be saved; only the three defined values are selectable/displayed.
- [ ] CS-04: Cancelling a delete does not remove the entry
  - Action: Click delete on a default entry, then cancel/dismiss the confirmation.
  - Expected: The entry remains in the list with all its details and notes intact.
- [ ] CS-05: Notes and status are per-entry and do not leak to other entries
  - Action: Set status "Offered" and a unique note on entry A, then inspect entry B.
  - Expected: Entry B keeps its own original status and shows no note from entry A.

## Interaction
- [ ] IX-01: The add-application form opens and closes on demand without creating data
  - Action: Click the add control to open the form, then cancel/close it without submitting.
  - Expected: The form opens with empty fields and closes; the list gains no new entry.
- [ ] IX-02: The edit form is pre-filled with the entry's current values
  - Action: Open edit on a default entry.
  - Expected: Company, role, date, status, and notes already contain that entry's existing data.
- [ ] IX-03: The list updates immediately after add, edit, status change, and delete
  - Action: Perform each of those four actions on a default entry.
  - Expected: The change is reflected in the list right away, without stale values from before the action.
- [ ] IX-04: Confirmation feedback is shown after save and delete
  - Action: Save a new/edited entry, then delete an entry.
  - Expected: A visible success/confirmation message (toast or inline notice) appears for each action, then dismisses.

## Content
- [ ] CT-01: Default applications are present on first visit with complete details
  - Action: Load the site fresh and inspect the list.
  - Expected: At least one pre-existing application is shown, each with a plausible company, role, date, status, and a notes area.
- [ ] CT-02: Status labels use the exact requested wording
  - Action: Inspect all status text/options in the UI.
  - Expected: The labels read "Applied", "Interviewed", and "Offered" (no typos, no unrelated labels).
- [ ] CT-03: Page content is relevant to tracking job applications
  - Action: Read the page title, headings, and field labels.
  - Expected: All text concerns job applications (e.g. company/role/date/status/notes); no unrelated product, blog, or demo text.
- [ ] CT-04: No placeholder or broken content is displayed
  - Action: Scan the list, forms, and entry details.
  - Expected: No "lorem ipsum", "TODO", "undefined", "null", or empty/broken fields where data should appear; dates render in a readable format.