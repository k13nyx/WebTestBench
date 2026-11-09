# Test Result

## Functionality
- [X] FT-01: User can view the personal list of job applications
  - Action: Open the website's main page
  - Expected: The list displays the pre-existing default entries, each showing company, role, date, and status
  - (Verified: 4 default entries loaded — Stripe/Senior Frontend Engineer/Jan 15, 2024/Interviewed, Notion/Product Designer/Jan 10, 2024/Applied, Linear/Full Stack Developer/Jan 8, 2024/Offered, Figma/Software Engineer/Jan 5, 2024/Rejected — each with company, role, date, and status shown, plus notes.)

- [X] FT-02: User can add a new application entry
  - Action: Fill in the company, role, and date fields and click the add/save button
  - Expected: A new entry is created and visible in the list with the entered company, role, and date
  - (Verified: Added Company="Acme Corp", Role="QA Engineer", Date=2026-11-01 → entry appeared immediately as "Acme Corp / QA Engineer / Nov 1, 2026 / Applied"; header counter updated 4 → 5 applications.)

- [X] FT-03: User can edit an existing entry
  - Action: Click the edit control on a default entry, change the role (e.g., to "Senior Engineer"), and save
  - Expected: The entry shows the updated role value in the list
  - (Verified: Edited default entry Stripe, changed role to "Senior Engineer", clicked "Save Changes" → list immediately shows role "Senior Engineer".)

- [X] FT-04: User can delete an entry
  - Action: Click the delete control on a default entry and confirm deletion
  - Expected: The entry is removed from the list
  - (Verified: Clicked delete on default entry Figma → entry removed instantly with "Application deleted" toast; counter 5 → 4. No confirmation dialog is presented — deletion is immediate, but the entry is removed as expected.)

- [X] FT-05: User can mark an entry with a status
  - Action: Change a default entry's status (e.g., to "Offered")
  - Expected: The entry displays the selected status value
  - (Verified: Changed default entry Stripe's status from "Interviewed" to "Offered" via the edit form's status selector → list displays "Offered" badge after save.)

- [X] FT-06: User can save a brief note on an entry
  - Action: Type a short note (e.g., "Recruiter said 2-week turnaround") into an entry's notes field and save
  - Expected: The note is stored and displayed with that entry
  - (Verified: Typed "Recruiter said 2-week turnaround" into Stripe's notes field in the edit form, saved → note displayed with the entry in the list.)

- [ ] FT-07: Entries persist after page reload
  - Action: Reload the page after adding/editing an entry
  - Expected: All entries and their details are still present in the list unchanged
  - Bug Report:
    - Issue: Data Loss on Reload / No Persistence (state kept in memory only)
    - Actual: After reloading http://localhost:6044/, the list reverted to the 4 seed defaults. The added entry "Acme Corp" (QA Engineer, Nov 1, 2026, Applied) vanished; the edited Stripe entry reverted to "Senior Frontend Engineer" / "Interviewed" / original note; and the previously deleted "Figma" entry reappeared. Inspection of `localStorage` returned zero keys — no data is written to any client-side store, so all adds, edits, and deletions are lost on every page load.

## Constraint
- [X] CS-01: Cannot create an entry with empty required fields
  - Action: Leave the company, role, or date field empty and attempt to save
  - Expected: No entry is created; a validation message or blocked save identifies the missing required field(s)
  - (Verified all scenarios: with Company+Role empty the "Add Application" button is disabled; with Company filled + Role empty it remains disabled; with Company+Role filled + Date cleared it remains disabled. The save is blocked whenever a required field is empty and no entry is created; the button only enables once Company, Role, and Date are all filled.)

- [ ] CS-02: Status accepts only the three defined values
  - Action: Open the status selector on any entry and review available options
  - Expected: Only "Applied", "Interviewed", and "Offered" are selectable; no other status values can be entered or chosen
  - Bug Report:
    - Issue: Extra selectable status value in the Status selector
    - Actual: Opening the Status selector (in both the "Add New Application" and "Edit Application" dialogs) shows four options: "Applied", "Interviewed", "Offered", and "Rejected". "Rejected" is an additional status value beyond the three defined ones and can be freely chosen (the pre-seeded Figma entry also displays this fourth status "Rejected").

## Interaction
- [X] IX-01: List updates immediately after user actions
  - Action: Add an entry, then edit and delete it, observing the list after each action
  - Expected: The list reflects each change immediately without requiring a manual page reload
  - (Verified: Add — "Acme Corp" appeared in the list and counter went 4 → 5 instantly; Edit — Stripe's role/status/note updated in place right after "Save Changes"; Delete — Figma disappeared and counter went 5 → 4 instantly, with toast notifications. No manual reload was needed for any change.)

- [X] IX-02: Edit view pre-fills the entry's current values
  - Action: Click the edit control on a default entry
  - Expected: The edit form opens with that entry's existing company, role, date, status, and note already filled in
  - (Verified: Clicking Edit on Stripe opened the "Edit Application" dialog pre-filled with Company="Stripe", Role="Senior Frontend Engineer", Date="2024-01-15", Status="Interviewed", and the full existing note "Had a great call with the hiring manager. Technical interview scheduled for next week.")

## Content
- [X] CT-01: Displayed entry data matches the saved data
  - Action: Compare each list entry's displayed company, role, date, status, and notes against the values saved for that entry
  - Expected: All displayed text matches exactly, with no truncated notes or mismatched values
  - (Verified: Saved "Acme Corp / QA Engineer / 2026-11-01 / Applied" displayed as "Acme Corp / QA Engineer / Nov 1, 2026 / Applied"; saved Stripe edits ("Senior Engineer", "Offered", "Recruiter said 2-week turnaround") displayed verbatim; default entries (Notion, Linear, Figma) display their full notes word-for-word with no truncation. Date is shown in "MMM D, YYYY" format, consistent with the saved ISO date.)

- [X] CT-02: Page content is relevant to job application tracking
  - Action: Inspect the page title, headings, field labels (e.g., "Company", "Role", "Date", "Status", "Notes"), and button texts
  - Expected: All visible text and controls relate to logging job applications, with no unrelated or placeholder content
  - (Verified: Page title "Job Tracker - Track Your Applications"; H1 "Job Tracker"; application counter; labels "Company", "Role", "Date Applied", "Status", "Notes"; buttons "Add Application", "Edit", "Save Changes", "Cancel"; dialogs "Add New Application" / "Edit Application"; domain-appropriate example placeholders ("e.g., Stripe") and status badges — all content pertains to job application tracking, with no unrelated or filler text.)
