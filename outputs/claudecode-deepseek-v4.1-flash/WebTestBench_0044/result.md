Reload reverted to the 4 seed entries — no persistence. I have enough evidence to complete all items. Here is the full report.

# Test Result

## Functionality

- [X] FT-01: User can add a new job application with company, role, and date
  - Action: Click "Add Application", enter Company "Acme Corp", Role "Software Engineer", Date "2026-11-08", and save.
  - Expected: The new entry appears in the application list showing "Acme Corp", "Software Engineer", and "2026-11-08".
  - Verified: New card "Acme Corp / Software Engineer / Nov 8, 2026" added; count went 4 → 5.

- [X] FT-02: User can edit an existing application's details
  - Action: Click "Edit" on an existing entry, change Role to "Senior Engineer", and save.
  - Expected: The entry in the list shows the updated role "Senior Engineer"; company and date remain unchanged.
  - Verified: Acme Corp card updated to "Senior Engineer"; company "Acme Corp" and date "Nov 8, 2026" unchanged.

- [X] FT-03: User can delete an application
  - Action: Click "Delete" on an existing entry and confirm the deletion.
  - Expected: The entry is removed and no longer appears anywhere in the list.
  - Verified: Notion deleted; count 4 → 3, Notion gone. (Note: no confirmation step occurred — see IX-03/CS-04.)

- [X] FT-04: User can assign a status when adding an application
  - Action: Add an application and set its status to "Interviewed" before saving.
  - Expected: The saved entry displays the status "Interviewed".
  - Verified: New "Globex" entry displayed status "Interviewed".

- [ ] FT-05: User can change the status of an existing application
  - Action: Change an entry's status from "Applied" to "Offered" and reload the page.
  - Expected: The entry still displays "Offered" after the page reloads.
  - Bug Report:
    - Issue: No data persistence — state is in-memory only
    - Actual: Acme Corp showed "Offered" before reload; after reloading the page the entire entry disappeared and the list reverted to the original 4 seed records ("4 applications"), so "Offered" is not shown. All changes were lost.

- [X] FT-06: User can add notes to an application
  - Action: Open an application, enter the note "Recruiter: Jane — follow up Friday", and save.
  - Expected: The note is saved and displayed when that application is reopened.
  - Verified: Globex created with note; reopening it via "Edit" showed "Recruiter: Jane — follow up Friday".

- [X] FT-07: User can edit existing notes
  - Action: Open an application that already has a note, change the text, and save.
  - Expected: The updated note text is displayed; the previous text is replaced.
  - Verified: Note replaced with "Updated note: recruiter emailed, interview moved to Monday"; old text gone.

- [ ] FT-08: Saved applications persist after a page reload
  - Action: Add an entry, then refresh the browser.
  - Expected: All previously saved entries and their details are still listed.
  - Bug Report:
    - Issue: No persistence across reload
    - Actual: After adding "Acme Corp" and "Globex" (list showed "6 applications") and reloading, the list reverted to the original 4 seed entries ("4 applications"); every user-added entry and detail was lost.

## Constraint

- [ ] CS-01: Application cannot be saved with empty required fields
  - Action: Leave Company, Role, or Date blank and click save.
  - Expected: The entry is not created and a validation message identifies the missing field(s).
  - Bug Report:
    - Issue: Missing validation message (no feedback on missing fields)
    - Actual: With Company/Role blank the "Add Application" button is simply `disabled`; no validation message identifying the missing field(s) is ever displayed, and no submit response occurs (button cannot be clicked).

- [ ] CS-02: Application cannot be saved with an invalid date
  - Action: Enter an invalid date such as "13/45/2026" in the Date field and save.
  - Expected: The entry is not created and a date validation message is shown.
  - Bug Report:
    - Issue: Missing date validation message
    - Actual: The Date field is a native `type="date"` control that rejects the text outright (input rejected as "Malformed value" / value stays empty); no entry is created, but no date validation message is shown anywhere.

- [ ] CS-03: Status is limited to the allowed values
  - Action: Open the status selector for an application.
  - Expected: Only "Applied", "Interviewed", and "Offered" are selectable; no other status can be saved.
  - Bug Report:
    - Issue: Extra status value available
    - Actual: The status listbox offers four options — "Applied", "Interviewed", "Offered", and an additional "Rejected" — which is selectable and is also shown on the existing "Figma" entry.

- [ ] CS-04: Cancelling a delete preserves the entry
  - Action: Click "Delete" on an entry and choose "Cancel" in the confirmation prompt.
  - Expected: The entry remains in the list, unchanged.
  - Bug Report:
    - Issue: No confirmation prompt — delete is immediate and irreversible
    - Actual: Clicking "Delete" on "Notion" removed it instantly with a "Application deleted" toast; no confirmation prompt and no "Cancel" option appeared, so the entry could not be preserved.

- [ ] CS-05: Whitespace-only input is rejected
  - Action: Enter only spaces in the Company field and save.
  - Expected: The entry is not created and a required-field validation message is shown.
  - Bug Report:
    - Issue: Missing validation message (no feedback)
    - Actual: Entering only spaces in Company (and Role) keeps the "Add Application" button `disabled` and no entry is created, but no required-field validation message is displayed.

## Interaction

- [X] IX-01: Success confirmation appears after adding an application
  - Action: Add a valid application and save.
  - Expected: A success message (e.g., "Application added") is displayed.
  - Verified: Toast "Application added — Acme Corp has been added to your list." displayed.

- [X] IX-02: Edit form opens pre-filled with current values
  - Action: Click "Edit" on an entry that has a company, role, date, status, and note.
  - Expected: The form opens with every field populated with that entry's existing values.
  - Verified: "Edit Application" opened with Company "Globex", Role "Data Analyst", Date "2026-11-08", Status "Interviewed", Notes populated.

- [ ] IX-03: Delete requires an explicit confirmation step
  - Action: Click "Delete" on an entry.
  - Expected: A confirmation prompt appears with "Confirm" and "Cancel" options before anything is removed.
  - Bug Report:
    - Issue: No confirmation step before deletion
    - Actual: Clicking "Delete" immediately removed the entry; no confirmation prompt with "Confirm"/"Cancel" options was shown.

- [X] IX-04: Add form clears after a successful save
  - Action: Add a valid application and save.
  - Expected: The form fields are emptied or the form closes, so the same data is not accidentally resubmitted.
  - Verified: The "Add New Application" dialog closed after saving.

## Content

- [X] CT-01: All required fields are clearly labeled
  - Action: Open the add/edit application form.
  - Expected: Visible labels exist for "Company", "Role", "Date", "Status", and "Notes".
  - Verified: Visible labels present — "Company", "Role", "Date Applied", "Status", "Notes".

- [ ] CT-02: Status options use the exact expected terms
  - Action: Inspect the status options in the form.
  - Expected: The options read exactly "Applied", "Interviewed", and "Offered".
  - Bug Report:
    - Issue: Unexpected extra status option
    - Actual: Options read "Applied", "Interviewed", "Offered", and additionally "Rejected" — a fourth term not in the expected set.

- [X] CT-03: Listed content is relevant and accurately displayed
  - Action: Review the application list and an application's notes.
  - Expected: Every entry shows real application data with no placeholder/lorem text, and notes are shown in full without truncation.
  - Verified: Entries show real company/role/date data (Stripe, Notion, Linear, Figma, plus added ones); notes render in full (e.g., "Had a great call with the hiring manager. Technical interview scheduled for next week.") with no placeholder/lorem text and no truncation.

---

### Summary
- **Failures (7):** FT-05, FT-08 (no persistence across reload); CS-01, CS-02, CS-05 (validation messages never shown — prevention via disabled button / native date input instead); CS-03, CT-02 (extra "Rejected" status value beyond the required three); CS-04, IX-03 (no delete confirmation — deletion is immediate and irreversible).
- **Passes (11):** FT-01, FT-02, FT-03, FT-04, FT-06, FT-07, IX-01, IX-02, IX-04, CT-01, CT-03.

The three most impactful defects: **(1)** no persistence — all saved applications are lost on reload; **(2)** delete is destructive with no confirmation; **(3)** the status set contains an extra "Rejected" value not in the allowed list.