# Test Result

## Functionality

- [X] FT-01: User can add a new job application with company, role, date, status, and notes.
  - Action: Click "Add Application" (or equivalent), fill in Company, Role, Date, Status, and Notes fields, then save.
  - Expected: The new application appears in the list with all entered details displayed correctly.

- [X] FT-02: User can edit an existing job application entry.
  - Action: Click the edit button on an existing application, modify Company/Role/Date/Status/Notes, then save.
  - Expected: The updated entry reflects the new values in the list.

- [X] FT-03: User can delete an existing job application entry.
  - Action: Click the delete button on an existing application and confirm deletion.
  - Expected: The application is removed from the list and no longer visible.

- [X] FT-04: User can mark/change an application status to one of the predefined values.
  - Action: Change the status of an existing application to "Applied", "Interviewed", or "Offered".
  - Expected: The status of that application is updated and displayed accordingly in the list.

- [X] FT-05: User can add or update brief notes for an application.
  - Action: Enter text in the Notes field when creating or editing an application, then save.
  - Expected: The note text is saved and displayed alongside the application entry.

- [X] FT-06: User can view the complete list of logged job applications.
  - Action: Navigate to the main page of the application.
  - Expected: All previously added applications are visible in a list format with their Company, Role, Date, Status, and Notes shown.

## Constraint

- [ ] CS-01: Application cannot be saved without required fields (Company, Role, Date).
  - Action: Attempt to save a new application with Company, Role, or Date left blank.
  - Expected: Save action is blocked and an error/validation message indicates which required fields are missing.
  - Bug Report:
    - Issue: Missing Validation Error Message (save is blocked, but the user is never told which field is missing)
    - Actual: The save **is** correctly blocked — the "Add Application" submit button renders with the `disabled` attribute whenever Company, Role, or Date is empty, and the three inputs carry native `required` attributes. However, **no error or validation message is ever displayed in the app**. The dialog's innerText while fields were empty contained only `Add New Application / Company / Role / Date Applied / Status / Applied / Interviewed / Offered / Rejected / Notes / Cancel / Add Application / Close` — no element with `role="alert"`, no `[class*="error"]`/`[class*="invalid"]` node, no `aria-invalid` and no `aria-describedby` on any input. Dispatching `blur`/`focusout` on the empty Company field produced no feedback either. The only validation message that exists is the browser-native one (`validationMessage` = "Please fill out this field."), but it is unreachable in the real user flow: with the submit button disabled, clicking it does nothing, and pressing Enter inside the Company field also did not submit, did not move focus to the invalid Role field (`document.activeElement` remained on the Company input), and produced no visible message. Only after forcing `submitBtn.disabled = false` did native validation fire. Net effect: the user sees a greyed-out button with no indication of whether Company, Role, or Date is the culprit.

- [ ] CS-02: Status field is restricted to the predefined values: Applied, Interviewed, Offered.
  - Action: Open the status selector (dropdown/radio) when creating or editing an application.
  - Expected: Only "Applied", "Interviewed", and "Offered" options are available; no other values can be selected or entered.
  - Bug Report:
    - Issue: Unrestricted Status Options (extra selectable value beyond the allowed set)
    - Actual: The status dropdown exposes **four** options instead of three. Opening the Status combobox in both the "Add New Application" and "Edit Application" dialogs rendered a `listbox` containing: `option "Applied" [selected]`, `option "Interviewed"`, `option "Offered"`, and `option "Rejected"`. The backing native `<select>` element's option values were `["applied", "interviewed", "offered", "rejected"]`. "Rejected" is not one of the predefined values and can be freely selected — the seeded Figma entry already carries a "Rejected" status.

- [ ] CS-03: Deleted application cannot be recovered unless undo functionality is provided.
  - Action: Delete an application, then refresh or revisit the page.
  - Expected: The deleted application does not reappear in the list (unless an explicit undo option is offered before page exit).
  - Bug Report:
    - Issue: Data Not Persisted — Deleted Entry Reappears After Reload
    - Actual: Deleted the seeded "Figma" entry (list dropped to "3 applications", toast confirmed "Application deleted"), then reloaded `http://localhost:6044/`. The Figma entry **reappeared** in the list and the counter reset to "4 applications". Root cause: the app has no persistence layer — `localStorage` and `sessionStorage` were both empty (`{}`) after adding, editing and deleting entries, so all state lives in memory and the page reseeds to the default sample set on every load. No undo is offered either: the delete toast contained only the title "Application deleted", the body "The application has been removed from your list.", and an unlabelled dismiss button — a page-wide scan for the string "undo" and for any button whose name matched /undo/i returned zero matches.

## Interaction

- [X] IX-01: Visual feedback is shown after adding a new application.
  - Action: Successfully save a new application.
  - Expected: A confirmation message/toast appears confirming the application was added, and the new entry becomes visible without manual refresh.

- [X] IX-02: Visual feedback is shown after editing an application.
  - Action: Successfully save edits to an existing application.
  - Expected: A confirmation message/toast appears confirming the update, and the list reflects the changes without manual refresh.

- [X] IX-03: Visual feedback is shown after deleting an application.
  - Action: Successfully delete an application.
  - Expected: A confirmation message/toast appears confirming the deletion, and the entry disappears from the list.

- [X] IX-04: Status change is immediately reflected in the application list view.
  - Action: Change the status of an application and observe the list.
  - Expected: The list entry's status indicator updates instantly without requiring a page reload.

## Content

- [X] CT-01: Default sample applications (if present) are relevant to the job application tracking theme.
  - Action: Load the application on first visit with default data.
  - Expected: Any pre-existing entries contain realistic Company, Role, Date, Status, and Notes data appropriate to job applications (not random/unrelated content).

- [ ] CT-02: All status labels displayed match the defined values (Applied, Interviewed, Offered).
  - Action: Review all entries in the list and any status filters/legends.
  - Expected: Status labels read exactly "Applied", "Interviewed", and/or "Offered" with consistent capitalization.
  - Bug Report:
    - Issue: Invalid Status Label Displayed (status value outside the defined set)
    - Actual: The status badge on the "Figma" card reads **"Rejected"** (a `<span>` with classes `inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border s…`), which is not one of the defined values Applied / Interviewed / Offered. The other three entries render correctly ("Interviewed" on Stripe, "Offered" on Notion, "Offered" on Linear) with consistent capitalization, so the deviation is isolated to the "Rejected" label. Note: the page exposes no status filter or legend controls at all — a scan for `nav`, `[class*="filter"]`, `[class*="legend"]`, `[class*="tab"]`, `[role="tablist"]` and any `<select>` outside the modal returned no results — so there were no filter labels to cross-check.

- [X] CT-03: Field labels and form instructions are clearly worded and relevant.
  - Action: Read the form labels and helper text on the Add/Edit application form.
  - Expected: Labels such as "Company", "Role", "Date", "Status", and "Notes" are clearly displayed and self-explanatory.
