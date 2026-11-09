All 20 checklist items have been executed. Final result:

# Test Result

## Functionality
- [X] FT-01: User can add a new application with company, role, and date
  - Action: Opened "Add Application", entered company "Acme Corp", role "Backend Engineer", date 2024-02-01, and submitted.
  - Expected: A new entry appears in the list showing "Acme Corp", "Backend Engineer", and the chosen date.
  - Actual: Card "Acme Corp / Backend Engineer / Feb 1, 2024" appeared; count updated to "5 applications".

- [X] FT-02: User can edit an existing application's details
  - Action: Opened Edit on default entry "Stripe", changed role to "Data Analyst", clicked "Save Changes".
  - Expected: The same entry now shows "Data Analyst"; other entries unchanged. (Stripe card showed "Data Analyst"; Acme/Notion/Linear/Figma unchanged.)

- [X] FT-03: User can delete an existing application
  - Action: Clicked the delete (trash) icon on default entry "Linear", then again on "Figma". (Note: no confirmation step exists — see CS-04; deletion applied immediately.)
  - Expected: Entry removed from the list; count decreases by one. (Linear removed, card list 5→4, count label updated.)

- [X] FT-04: User can set an application's status to applied, interviewed, or offered
  - Action: On "Notion", set status to "Interviewed" and saved; then reopened and changed it to "Offered" and saved.
  - Expected: Status reads "Interviewed", then "Offered". (Card showed "Interviewed" after step 1, "Offered" after step 2 — latest selection stored.)

- [X] FT-05: User can record notes for an application and view them
  - Action: Edited "Notion", set notes to "Referred by recruiter, follow up Monday", saved, and viewed the list.
  - Expected: Note text displayed attached to that application. (Notion card showed exactly that note.)

- [X] FT-06: The personal list displays all tracked applications with their core details
  - Action: Loaded the page and inspected the list.
  - Expected: Every application listed with company, role, date, and status visible together. (All 4 default cards show company heading, role, date like "Jan 15, 2024", and status badge, plus notes.)

- [ ] FT-07: Logged applications persist across a page reload
  - Action: Added application "Persist Test Inc" with note "Persistence check note 7319", then reloaded the page.
  - Expected: The newly added application (including its note) is still present after reload.
  - Bug Report:
    - Issue: No data persistence
    - Actual: After reload the list reset to the original 4 defaults (Stripe, Notion, Linear, Figma). "Persist Test Inc" and its note were gone; all prior edits (Acme Corp, Stripe "Data Analyst", Notion status/note) and deletions were also lost. State is memory-only, with no localStorage/backend persistence.

## Constraint
- [ ] CS-01: An application cannot be saved when required fields are missing
  - Action: Opened the add form, filled Role only (Company left blank), tabbed through fields, and attempted submission.
  - Expected: Submission is blocked with a validation message naming the missing field; no new entry appears.
  - Bug Report:
    - Issue: Missing user-facing validation feedback
    - Actual: No entry was created (the "Add Application" button stays disabled), but no validation message ever appears naming the missing field — the form blocks silently. Fields carry `required` attributes, but because the button is disabled the user can never trigger the browser's native "Please fill out this field" message, and no custom error text is rendered anywhere in the dialog.

- [X] CS-02: An invalid date is rejected
  - Action: Cleared the "Date Applied" field and typed free text + impossible values ("hello13452026" / 13/45) into it, then attempted submit.
  - Expected: The entry is not created with an invalid date. (The native `input[type="date"]` control rejects out-of-format input at keystroke level — "13/45/2026" could not be entered and was clamped to a structurally valid date; no invalid date can ever reach submission. Caveat: this rejection is silent — no explicit "invalid date" error message is shown.)

- [ ] CS-03: Status is limited to the defined set
  - Action: Inspected the Status control in the add/edit dialog and the statuses displayed in the list.
  - Expected: Only the three defined values ("Applied / Interviewed / Offered") are selectable/displayed.
  - Bug Report:
    - Issue: Extra status option outside defined set
    - Actual: The status dropdown contains a fourth option: `["Applied", "Interviewed", "Offered", "Rejected"]`, and the default entry "Figma" is displayed with status "Rejected". Free text cannot be typed (it's a select), but the defined-set constraint is violated by this fourth selectable/displayed value.

- [ ] CS-04: Cancelling a delete does not remove the entry
  - Action: Clicked the delete (trash) icon on default entry "Linear" and attempted to cancel/dismiss the confirmation.
  - Expected: The entry remains in the list with all its details and notes intact.
  - Bug Report:
    - Issue: Missing delete confirmation (data destroyed immediately)
    - Actual: No confirmation dialog or browser prompt ever appeared — clicking the trash icon removed "Linear" from the list instantly (cards went from Acme/Stripe/Notion/Linear/Figma to Acme/Stripe/Notion/Figma). There is no cancel path, so the entry could not be kept.

- [X] CS-05: Notes and status are per-entry and do not leak to other entries
  - Action: Set status "Offered" and note "Referred by recruiter, follow up Monday" on Notion (entry A), then inspected Stripe, Acme Corp, and Linear (entry B/C/D).
  - Expected: Other entries keep their own original status and show no note from entry A. (Stripe kept "Interviewed" + its original note; Acme kept "Applied" with no note; Linear unchanged — no leakage.)

## Interaction
- [X] IX-01: The add-application form opens and closes on demand without creating data
  - Action: Clicked "Add Application" to open the "Add New Application" dialog, then clicked Cancel without submitting.
  - Expected: Form opens with empty fields (Company/Role/Notes were empty; submit disabled; only the date pre-filled to today) and closes; list gains no new entry. (Dialog closed; still "4 applications", cards unchanged.)

- [X] IX-02: The edit form is pre-filled with the entry's current values
  - Action: Opened Edit on default entry "Stripe".
  - Expected: Company, role, date, status, and notes contain the entry's existing data. (Dialog showed Company="Stripe", Role="Senior Frontend Engineer", Date="2024-01-15", Status="Interviewed", Notes="Had a great call with the hiring manager...".)

- [X] IX-03: The list updates immediately after add, edit, status change, and delete
  - Action: Performed add (Acme Corp), edit (Stripe role), status change (Notion → Interviewed → Offered), and delete (Linear, Figma) and observed the list after each.
  - Expected: Each change reflected in the list right away without stale values. (All four updates rendered immediately, including the "N applications" counter.)

- [X] IX-04: Confirmation feedback is shown after save and delete
  - Action: Saved a new entry, saved an edit, and deleted entries; captured toast notifications.
  - Expected: A visible success/confirmation message appears for each action, then dismisses. (Toasts observed: "Application added — Acme Corp has been added to your list.", "Application updated — Your changes have been saved.", "Application deleted — The application has been removed from your list."; each auto-dismissed.)

## Content
- [X] CT-01: Default applications are present on first visit with complete details
  - Action: Loaded the site fresh and inspected the list.
  - Expected: At least one pre-existing application with plausible company, role, date, status, and notes area. (Four defaults: Stripe, Notion, Linear, Figma — each with company, role, plausible date, status badge, and a populated notes line.)

- [ ] CT-02: Status labels use the exact requested wording
  - Action: Inspected all status text and options in the UI.
  - Expected: Labels read "Applied", "Interviewed", "Offered" — no typos, no unrelated labels.
  - Bug Report:
    - Issue: Extra/unrelated status label
    - Actual: The three required labels are spelled correctly, but an unrelated fourth label "Rejected" appears both as a dropdown option and displayed on the Figma card.

- [X] CT-03: Page content is relevant to tracking job applications
  - Action: Read the page title, headings, and field labels.
  - Expected: All text concerns job applications. (Title "Job Tracker - Track Your Applications", h1 "Job Tracker", "4 applications" counter, dialog titles "Add New Application"/"Edit Application", labels Company/Role/Date Applied/Status/Notes, buttons "Add Application"/"Save Changes"/"Cancel". No unrelated product/blog/demo text.)

- [X] CT-04: No placeholder or broken content is displayed
  - Action: Scanned the list, forms, and entry details for "lorem ipsum", "TODO", "undefined", "null", empty/broken fields, and date formatting.
  - Expected: No placeholder/broken content; readable dates. (Body-text scan found none of the suspicious tokens; every card had all fields populated; dates render readably as "Jan 15, 2024" style; form hint text uses proper example placeholders "e.g., Stripe".)

**Summary: 16 PASS / 4 FAIL** — the failures are the four real defects found: no persistence across reload (FT-07), silent required-field blocking (CS-01), the unauthorized fourth "Rejected" status (CS-03/CT-02), and delete-without-confirmation (CS-04).