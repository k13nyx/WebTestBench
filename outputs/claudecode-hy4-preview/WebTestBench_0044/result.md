# Test Result

## Functionality

- [X] FT-01: The application list loads and displays all existing entries with their details
  - Action: Open the website's main page and observe the list of job applications.
  - Expected: At least one default entry is visible, and each entry row/card shows a company name, role title, date, and a status. No error or blank page appears.

- [ ] FT-02: User can add a new application with company, role, and date
  - Action: Click the add button ("Add Application" / "New Application" / "+"), fill in Company = "Acme Corp", Role = "Backend Engineer", Date = today's date, then submit/save.
  - Expected: A new entry appears in the list showing "Acme Corp", "Backend Engineer", and today's date, and it remains visible after a page refresh.
  - Bug Report:
    - Issue: Data not persisted (lost on refresh)
    - Actual: After saving, the "Acme Corp / Backend Engineer / Nov 8, 2026" card appeared and the header changed to "5 applications", but after `page.reload()` the list reverted to the original 4 default entries and "Acme Corp" was gone (header back to "4 applications"). Verified twice, including with a 2.5s wait before reload. `localStorage` and `sessionStorage` are both empty, so the list lives only in React in-memory state.

- [X] FT-03: User can set the status when adding a new application
  - Action: Add a new application with Company = "Globex", Role = "Designer", Date = today, Status = "Interviewed", then save.
  - Expected: The new "Globex" entry displays the status "Interviewed" in the list.

- [X] FT-04: User can add and view notes for an application
  - Action: Add a new application with notes text "Recruiter call on Monday at 10am", save, then open/view that entry.
  - Expected: The saved notes text is displayed for that entry exactly as entered (not truncated or lost).

- [ ] FT-05: User can edit an existing application's details
  - Action: Open a default entry, change its Role to "Senior Analyst", then save.
  - Expected: That entry now displays "Senior Analyst" as the role, and the change persists after a page refresh.
  - Bug Report:
    - Issue: Edit not persisted (lost on refresh)
    - Actual: Editing the Stripe entry's role updated the card to "Senior Analyst" immediately, but after a page refresh the entry showed its original role "Senior Frontend Engineer" again.

- [ ] FT-06: User can change the status of an existing application
  - Action: Open a default entry whose status is "Applied" and change its status to "Offered", then save.
  - Expected: That entry now displays the status "Offered" in the list, and the change persists after a page refresh.
  - Bug Report:
    - Issue: Status change not persisted (lost on refresh)
    - Actual: The Notion entry changed from "Applied" to "Offered" immediately after save, but after a page refresh it reverted to "Applied".

- [ ] FT-07: User can delete an application
  - Action: Note the total number of entries, then delete one default entry and confirm the deletion.
  - Expected: That entry disappears from the list immediately, the total count decreases by one, and it is still absent after a page refresh.
  - Bug Report:
    - Issue: Delete not persisted; no confirmation step exists
    - Actual: Clicking the delete (trash) button on the "Figma" entry removed it instantly and the count went from 4 to 3, with **no confirmation prompt shown at all** (no `role=alertdialog`/`dialog` appeared). After a page refresh, the list returned to 4 entries and "Figma" was present again.

## Constraint

- [ ] CS-01: Cannot save an application without a company name
  - Action: Open the add form, leave Company empty, fill Role and Date, then submit.
  - Expected: The application is not created — no new entry appears in the list and the form stays open with a validation message referencing the company field.
  - Bug Report:
    - Issue: Missing validation message on required field
    - Actual: With Company empty and Role/Date filled, the "Add Application" submit button was `disabled`, so the form could not be submitted (no new entry was created and the dialog stayed open). However, the dialog contained **no validation/error message referencing the company field** — the entire dialog text was "Add New Application | Company | Role | Date Applied | Status | Applied | Interviewed | Offered | Rejected | Notes | Cancel | Add Application | Close". The input only carries HTML5 `required`, which renders no visible in-page message.

- [ ] CS-02: Cannot save an application without a role
  - Action: Open the add form, leave Role empty, fill Company and Date, then submit.
  - Expected: The application is not created, and a validation message referencing the role field is shown.
  - Bug Report:
    - Issue: Missing validation message on required field
    - Actual: With Role empty and Company/Date filled, the submit button was `disabled` (no entry created, dialog stayed open), but no validation message referencing the role field appeared anywhere in the dialog DOM.

- [ ] CS-03: Cannot save an application without a date
  - Action: Open the add form, leave Date empty, fill Company and Role, then submit.
  - Expected: The application is not created, and a validation message referencing the date field is shown.
  - Bug Report:
    - Issue: Missing validation message on required field
    - Actual: With Date cleared and Company/Role filled, the submit button was `disabled` (no entry created, dialog stayed open), but no validation message referencing the date field appeared in the dialog.

- [ ] CS-04: Status is limited to the defined values only
  - Action: Open the status control on the add form and on an existing entry, and list all selectable status options.
  - Expected: The only selectable statuses are "Applied", "Interviewed", and "Offered"; no free-text or other status value can be entered or saved.
  - Bug Report:
    - Issue: Undefined status value offered/selectable
    - Actual: The status control (Radix combobox) exposes four selectable options: "Applied", "Interviewed", "Offered", **"Rejected"**. The fourth value is also used by a seeded default entry (Figma = "Rejected"), so a status outside the three defined values can be both selected and rendered.

- [X] CS-05: Notes are optional when saving an application
  - Action: Add a new application with Company = "Initech", Role = "QA Engineer", Date = today, leaving the notes field empty, then save.
  - Expected: The entry is created successfully and appears in the list; no error is shown about the empty notes field.

- [X] CS-06: Editing an entry does not create a duplicate entry
  - Action: Note the total number of entries, edit one entry's company name, and save.
  - Expected: The total number of entries is unchanged; the edited entry is updated in place rather than a new row/card being added.
  - Note: Verified with the Stripe role edit (8 → 8 cards) and an explicit company rename Initech → "Initech LLC" (8 → 8 cards, exactly one card showing the new name).

- [ ] CS-07: Deletion requires confirmation and can be cancelled
  - Action: Start deleting an entry, then choose "Cancel" / "No" in the confirmation prompt.
  - Expected: The entry remains in the list unchanged, and it is still present after a page refresh.
  - Bug Report:
    - Issue: Missing delete confirmation dialog
    - Actual: Clicking the delete control on an entry immediately deletes it — no confirmation prompt of any kind is displayed (`[role=alertdialog]`/`[role=dialog]` count = 0), so there is no "Cancel"/"No" option to choose. The entry was removed from the list right away.

## Interaction

- [X] IX-01: The add form opens and closes correctly around a create action
  - Action: Click the add button, then click "Save"/"Submit" after filling valid details.
  - Expected: The add form (or modal/panel) closes and returns to the list view, with the new entry visible.

- [X] IX-02: Each status is shown as a distinct visual status indicator on every entry
  - Action: Locate entries with different statuses and compare their status indicators (badge/label/pill).
  - Expected: Every entry shows a visible status indicator, and entries with "Applied", "Interviewed", and "Offered" use visually distinguishable styling (different color, label, or icon).
  - Note: Verified via computed styles — Applied: `status-applied`, blue (`rgb(219,234,254)` bg); Interviewed: `status-interviewed`, amber (`rgb(254,243,199)` bg); Offered: `status-offered`, green (`rgb(209,250,229)` bg). Every card renders a pill badge.

- [X] IX-03: Cancelling an edit discards unsaved changes
  - Action: Open an entry, change its company name, then click "Cancel" instead of saving.
  - Expected: The form closes and the entry still shows its original company name, unchanged.
  - Note: Changed Notion → "Cancelled Co", clicked Cancel: dialog closed, "Notion" still present and "Cancelled Co" absent.

- [X] IX-04: Each entry provides access to its edit, delete, and notes controls
  - Action: Inspect any entry in the list (hover over or expand it if needed).
  - Expected: Controls to edit the entry, delete the entry, and view/edit its notes are visible and clickable for that entry.
  - Note: Every card renders a visible, enabled "Edit" button and a visible, enabled icon-only delete button (destructive styling). Notes are shown inline on the card and are viewable/editable through the Edit form, which contains the labeled "Notes" field.

## Content

- [X] CT-01: The page is clearly identified as a job application tracker with correctly labeled fields
  - Action: Read the page heading/title and the labels on the list columns and the add/edit form fields.
  - Expected: The heading identifies job application tracking (e.g., "Job Applications"), and the fields/columns are labeled "Company", "Role", "Date", "Status", and "Notes" with no placeholder or lorem-ipsum text.
  - Note: `<h1>` = "Job Tracker" with "N applications" subtitle; browser title "Job Tracker - Track Your Applications". Form labels: "Company", "Role", "Date Applied", "Status", "Notes". No lorem-ipsum content.

- [X] CT-02: An informative empty state is shown when the list has no entries
  - Action: Delete all entries from the list (or view the list in its empty state if it starts empty).
  - Expected: A message related to job applications is shown (e.g., "No applications yet" with guidance to add one) instead of a blank area or an error.
  - Note: After deleting all entries, the list area showed: "No applications yet" / "Start tracking your job search by adding your first application." plus an "Add Your First Application" button.

- [X] CT-03: Dates are displayed in a consistent, readable format
  - Action: Compare the date shown on at least two different list entries.
  - Expected: Every date is rendered in the same human-readable format (e.g., "Nov 8, 2026" or "2026-11-08") with no raw timestamps, "Invalid Date", "NaN", or "undefined" text.
  - Note: Observed "Jan 15, 2024", "Jan 10, 2024", "Jan 8, 2024", "Jan 5, 2024", and newly added "Nov 8, 2026" — all in the same "MMM D, YYYY" format.