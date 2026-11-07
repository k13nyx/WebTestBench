# Test Result

## Functionality

- [X] FT-01: Default applications are listed on page load
  - Action: Open the application list page.
  - Expected: Existing default entries are displayed, each showing its company, role, date, status, and notes.

- [X] FT-02: New application can be added with company, role, and date
  - Action: Click the add button, enter a company, a role, and a date, then submit.
  - Expected: The form submits successfully and the new entry is created.

- [X] FT-03: Newly added application appears in the list
  - Action: After adding an entry, view the list.
  - Expected: The new entry is listed with the company, role, and date that were entered.

- [X] FT-04: An existing application can be edited
  - Action: Open the edit view for any listed entry, change the company and role, then save.
  - Expected: The saved entry displays the updated company and role in the list.

- [X] FT-05: An application can be deleted
  - Action: Delete any listed entry.
  - Expected: The entry is removed from the list and is no longer shown anywhere on the page.

- [X] FT-06: Status can be changed for an application
  - Action: Change the status of a listed entry to "interviewed", then to "offered".
  - Expected: The entry displays the newly selected status each time.

- [X] FT-07: Notes can be added to an application and are shown
  - Action: Open an entry and enter note text such as "Recruiter called on Monday", then save.
  - Expected: The entered note text is displayed for that entry.

- [ ] FT-08: Application data persists after a page reload
  - Action: Add an entry with a note and a status, then reload the page.
  - Expected: The entry is still present with the same company, role, date, status, and note.
  - Bug Report:
    - Issue: Data is not persisted (state resets to defaults on reload)
    - Actual: Added "Persistence Test Co / Data Engineer / 2026-05-01 / Offered / 'Persistence check note.'" — the list then showed it and the header read "4 applications". After `page.reload()` the list reverted to the four seeded defaults ("Stripe, Notion, Linear, Figma") and "Persistence check note." was no longer present anywhere. The same happened earlier: a deleted entry ("Stripe") reappeared and a changed status (Notion → Offered) reverted to "Applied" after reload. No localStorage/sessionStorage keys are ever written.

## Constraint

- [ ] CS-01: Company is required when adding an application
  - Action: Open the add form, leave company empty, fill role and date, then submit.
  - Expected: Submission is blocked, no new entry is created, and the company field is flagged.
  - Bug Report:
    - Issue: Missing validation feedback / field not flagged
    - Actual: Submission was blocked (the dialog's "Add Application" button stays `disabled` and pressing Enter does nothing) and no entry was created (list stayed at 4), but the company field is not flagged in any way: no error text, no `aria-invalid`, no error styling, and no message identifying the missing field (dialog innerText contains only "Company / Role / Date Applied / Status / Notes / Cancel / Add Application / Close").

- [ ] CS-02: Role is required when adding an application
  - Action: Open the add form, leave role empty, fill company and date, then submit.
  - Expected: Submission is blocked, no new entry is created, and the role field is flagged.
  - Bug Report:
    - Issue: Missing validation feedback / field not flagged
    - Actual: Submission was blocked via the disabled submit button and no entry was created, but the role field carries no flag — no error message, no `aria-invalid` attribute, no error border — so the user is never told the role is the missing field.

- [ ] CS-03: Date is required and must be a valid date when adding an application
  - Action: Open the add form, leave date empty (then repeat with an invalid date value), fill company and role, then submit.
  - Expected: Submission is blocked in both cases, no entry is created, and the date field is flagged.
  - Bug Report:
    - Issue: Missing validation feedback / field not flagged
    - Actual: With the date cleared the submit button became disabled and no entry was created; an invalid date ("13/13/2024") is normalized by the native date widget to 2024-12-13 (or rejected outright as malformed by the input). In both cases the date field is never flagged — no error message, no `aria-invalid`, no invalid styling — so the requirement "date field is flagged" is not met.

- [ ] CS-04: Status is limited to the defined set of values
  - Action: Inspect the status control for any application.
  - Expected: Only the options applied, interviewed, and offered are selectable, and every entry holds one of these three values.
  - Bug Report:
    - Issue: Extra status value outside the allowed set
    - Actual: The status control exposes four options — "Applied", "Interviewed", "Offered" and "Rejected" (option values applied/interviewed/offered/rejected), and the default entry "Figma" holds the status "Rejected", which is outside the defined set.

## Interaction

- [X] IX-01: Add form can be opened and dismissed
  - Action: Click the add button, then close/dismiss the form without saving.
  - Expected: The form opens on click and closes on dismiss, leaving the list unchanged.

- [ ] IX-02 placeholder skipped — see IX-02 below

- [X] IX-02: Success feedback is shown after adding an application
  - Action: Add a valid application.
  - Expected: A success confirmation (message or highlight) appears and the form resets or closes.

- [ ] IX-03: Validation feedback is shown on an invalid submission
  - Action: Submit the add form with a required field empty.
  - Expected: A visible error message identifies the missing field; the form stays open so it can be corrected.
  - Bug Report:
    - Issue: No validation error message shown
    - Actual: With company/role/date missing, the "Add Application" button is simply `disabled` and no error message is rendered anywhere in the dialog — no `role="alert"` node, no error element, no field-level text — so the missing field is never identified. The form does stay open, but there is no visible error feedback.

- [X] IX-04: Edit form is pre-filled with the entry's current values
  - Action: Open the edit view for an existing entry.
  - Expected: The form fields show the entry's saved company, role, date, status, and notes.

- [ ] IX-05: Deleting an entry requires a confirmation step
  - Action: Click delete on an entry, then dismiss/cancel the confirmation.
  - Expected: The entry is not removed when the action is cancelled.
  - Bug Report:
    - Issue: Missing confirmation step — destructive action executes immediately
    - Actual: Clicking the card's delete button removed the entry immediately: no native `confirm` dialog fired (page dialog handler recorded none), no `[role="alertdialog"]`/`[role="dialog"]` appeared, and the list dropped from 4 to 3 entries with only a toast "Application deleted — The application has been removed from your list." There is no cancel option, so a mis-click cannot be aborted.

## Content

- [X] CT-01: Default list entries contain complete, job-application-relevant details
  - Action: Review every default entry shown on page load.
  - Expected: Each shows a company name, a role, a date, a status, and notes text; no placeholder or filler text such as "Lorem ipsum" appears.

- [ ] CT-02: Status values are labeled exactly as applied, interviewed, and offered
  - Action: Read the status labels on entries and in the status control.
  - Expected: Labels use these exact words and match the status shown on each entry.
  - Bug Report:
    - Issue: Status label outside the defined set
    - Actual: Besides "Applied", "Interviewed" and "Offered", the status control also lists a "Rejected" option and the default entry "Figma" displays the label "Rejected"; the labels therefore do not use only the three specified words.

- [ ] CT-03: Saved notes are displayed in full
  - Action: Save a long multi-line note on an entry, then view the entry.
  - Expected: The full note text is readable and is not truncated, hidden, or replaced by placeholder text.
  - Bug Report:
    - Issue: Note text truncated in the list view
    - Actual: After saving a 3-line note ("Recruiter called on Monday. / Second phone screen scheduled for Friday at 10am with two engineers from the platform team. / They emphasized ownership of the whole frontend pipeline, design systems work, and close collaboration with product design."), the card's note paragraph renders with class `line-clamp-2` (computed `overflow: hidden`, `scrollHeight: 120px` vs `clientHeight: 40px`), so only the first two lines are visible and the rest is cut off. There is no expand/"show more" control, so the full note cannot be read from the entry view.