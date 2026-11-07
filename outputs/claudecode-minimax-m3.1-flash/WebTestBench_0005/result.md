I have completed the full test sweep. Here is the checklist with results.

# Test Result

## Functionality

- [X] FT-01: User can create a new resume from the main page
  - Action: Click the "Create New Resume" / "New Resume" button on the resume list or header.
  - Expected: A blank resume editor opens with a default title (e.g., "Untitled Resume") and empty sections for contact details, work experience, education, and skills.

- [X] FT-02: User can enter contact details and see them reflected in the resume
  - Action: Fill in name, email, phone, and location fields in the contact details section, then trigger the preview.
  - Expected: All entered contact values appear in the resume preview in the contact area.

- [X] FT-03: User can add, edit, and delete a work experience entry
  - Action: Click "Add" in the Work Experience section, fill in job title, company, dates, and description, then edit the entry and finally delete it.
  - Expected: Each work experience entry appears as a separate item in the editor and in the preview; edits update the preview; deleting removes it from both.

- [X] FT-04: User can add, edit, and delete an education entry
  - Action: Add an education item with institution, degree, and graduation year, modify one field, then remove the entry.
  - Expected: The education entry shows in the editor list and preview, updates after editing, and disappears after deletion.

- [ ] FT-05: User can add, edit, and remove a skill
  - Action: Add skills one at a time (e.g., "Python", "SQL"), rename one skill, then delete another skill.
  - Expected: Skills are listed individually, the renamed skill shows the new text, and the deleted skill no longer appears.
  - Bug Report:
    - Issue: Missing Feature (no skill rename/edit control)
    - Actual: Adding and deleting skills works (Python, SQL, Kubernetes were added and "SQL" was removed from both editor list and preview), but a skill row contains only a static `<span class="font-medium text-sm">` with the skill name, a level `<select>` (Intermediate), and a delete "×" button — there is no edit/rename input, button, or `contentEditable`. Double-clicking the skill name does nothing, and the preview renders skills as non-interactive `<span>` chips. There is no way to rename an existing skill.

- [X] FT-06: User can select a different pre-designed template and see the layout change
  - Action: Open the template/style selector and choose a template other than the current one.
  - Expected: The resume preview immediately re-renders in the selected template's style (visibly different layout/typography/colors), and the selected template is marked as active.

- [X] FT-07: User can change the order of resume sections
  - Action: Use the section ordering controls (move up / move down / drag) to move a section, e.g., place Education above Work Experience.
  - Expected: The preview renders the sections in the new order and the order persists when the preview is refreshed.

- [X] FT-08: User can customize section headings
  - Action: Change a section heading from its default (e.g., "Work Experience" to "Professional Experience").
  - Expected: The new heading text is shown in the editor and in the preview for that section only.

- [X] FT-09: User can preview the resume in a dedicated preview view
  - Action: Click the "Preview" button/tab.
  - Expected: A read-only, formatted rendering of the resume (single-page view, no editable input fields) is shown containing all saved content.
  - Note: accessed via the "Show Preview" / "Hide Preview" toggle in the editor header (no separate Preview tab exists); the rendered preview page contains 0 `input`/`textarea`/`select` elements and shows all saved content.

- [ ] FT-10: User can rename a saved resume version
  - Action: Use the rename option on a saved resume (e.g., from the list's row menu or a title field) and enter a new title such as "Acme Corp - Software Engineer".
  - Expected: The new title replaces the old one everywhere it is displayed (list, header, preview title) and is persisted after a page reload.
  - Bug Report:
    - Issue: Data Not Persisted / Resume Title Missing From Preview
    - Actual: Renaming works in-session (row menu → Rename dialog → Save, and inline header edit), and the list and header show the new title, but (1) after a page reload all user-created/renamed resumes are gone and the list resets to only the 3 seeded resumes ("Product Designer Resume", "Marketing Manager Resume", "Software Engineer Resume") — nothing is persisted (no localStorage/IndexedDB/API writes exist), and (2) the preview never displays the resume title at all — the preview `<h1>` renders the contact name (e.g. "Jane Q. Tester" / "Your Name"), so the title is missing from the preview.

- [X] FT-11: User can duplicate a saved resume version
  - Action: Click "Duplicate" on an existing saved resume.
  - Expected: A new copy appears in the saved list with a distinguishable title (e.g., original name + "Copy") and identical content, while the original remains unchanged.

- [X] FT-12: User can save multiple resume variations for different job applications
  - Action: Create and save two resumes with different titles and content, then view the saved resumes list.
  - Expected: Both resumes are listed independently and each opens with its own content, template, and layout settings.

- [X] FT-13: User can search saved resumes by title
  - Action: Type a keyword that appears in one resume's title but not another's into the search box.
  - Expected: Only the matching resume (or resumes whose titles contain the keyword) is shown; non-matching resumes are hidden.

- [X] FT-14: User can filter saved resumes by date created
  - Action: Use the date filter/sort control to select a date range or a sort-by-date option in the saved resumes list.
  - Expected: The list is narrowed/ordered according to the selected date criteria, and each listed resume shows a date created value.
  - Note: only date sorting is offered ("Newest First" / "Oldest First" / "Title A-Z" / "Title Z-A"); the list re-orders correctly and every card shows a human-readable date (labelled "Updated &lt;date&gt;").

## Constraint

- [ ] CS-01: Required contact fields are validated before saving
  - Action: Clear or leave empty a required field (e.g., full name / email) and attempt to save the resume.
  - Expected: Saving is blocked or an inline validation/error message names the missing field, and no invalid resume is stored.
  - Bug Report:
    - Issue: Missing Form Validation
    - Actual: A new resume created with Full Name left empty was silently stored and appeared in the saved list as "Untitled Resume"; no inline error message, no `aria-invalid` attribute, and no validation styling (border color remained `rgb(225, 231, 239)`) were present.

- [ ] CS-02: Invalid email format is rejected
  - Action: Enter "not-an-email" in the email field and attempt to save.
  - Expected: An email-format validation error is shown and the resume is not saved with the invalid value.
  - Bug Report:
    - Issue: Missing Form Validation (email format)
    - Actual: "not-an-email" was accepted without any error, was persisted, and was re-displayed in both the Contact editor field and the resume preview ("Your Name / not-an-email"). No email-format validation message appeared anywhere.

- [ ] CS-03: Resume title is required and must be non-empty
  - Action: Clear the resume title field and attempt to save or attempt to duplicate the resume.
  - Expected: The save/duplicate is blocked with a prompt requiring a title.
  - Bug Report:
    - Issue: Missing Form Validation (required title)
    - Actual: Using the list row menu → Rename → clearing the title → clicking "Save" was accepted with no prompt; the resume was stored with an empty title and the saved list rendered a card whose `<h3>` is completely empty (""). (Only the inline header editor happens to revert an emptied title back to "Untitled Resume" — no error is shown and no blocking occurs.)

- [X] CS-04: Section reorder controls cannot move a section outside the valid list boundaries
  - Action: Attempt to move the first section up and the last section down using the ordering controls.
  - Expected: The first section remains first and the last remains last; no duplicate or removed section results.

- [X] CS-05: Duplicate operation does not overwrite the source resume
  - Action: Duplicate a resume, then edit the duplicate's title and contact details and save.
  - Expected: The original resume's title and content are unchanged and it still exists separately in the list.

- [X] CS-06: Deleting a saved resume requires confirmation and is not performed accidentally
  - Action: Click "Delete" on a saved resume.
  - Expected: A confirmation prompt appears; cancelling leaves the resume intact, confirming removes it from the list.

- [X] CS-07: A search/filter with no matching results shows an explicit empty state rather than a blank or broken list
  - Action: Search for a title keyword that matches no saved resume.
  - Expected: A clear "no resumes found"/empty-state message is displayed and no incorrect resume cards are displayed.

## Interaction

- [X] IX-01: Preview updates live as content is edited
  - Action: Type a new value into any field (e.g., change job title in work experience) while the preview is visible.
  - Expected: The preview re-renders to show the new value without requiring a manual save or refresh.

- [X] IX-02: Switching template visibly re-styles the resume and indicates the active selection
  - Action: Click through two or more template options in the template picker.
  - Expected: The preview restyles on each click and the currently selected template is highlighted/selected in the picker.

- [X] IX-03: Add / remove controls provide immediate visual feedback
  - Action: Click "Add" for a work experience entry and click the remove (×) control on that entry.
  - Expected: A new empty entry appears immediately in the editor list and the removed entry disappears immediately.

- [ ] IX-04: Saving shows a clear success confirmation
  - Action: Click "Save" on the editor.
  - Expected: A success notification (toast or status message) appears confirming the resume was saved, and it disappears or is dismissible.
  - Bug Report:
    - Issue: Missing Save Action / No Success Notification
    - Actual: The editor has no "Save" button at all — an exhaustive enumeration of every `<button>` in the editor returned only the back button, title button, "Hide Preview" toggle, the 7 section tabs, and the section/item controls. Edits are applied straight to in-memory state. The only "Save" button in the app is inside the Rename dialog, and clicking it produces no toast: the sonner notification container (`<ol class="fixed top-0 z-[100] ...">`) remained empty (innerHTML = "") after rename, duplicate, and delete actions. No success message or status indicator is shown.

- [ ] IX-05: Unsaved-change state is indicated when navigating away from edited content
  - Action: Edit a field, then attempt to leave the editor or switch resume.
  - Expected: The app indicates unsaved changes (e.g., dirty-state marker or confirmation prompt) before discarding them.
  - Bug Report:
    - Issue: Missing Unsaved-Change Indicator
    - Actual: After editing the Phone field, the header contained no dirty marker (no asterisk, dot, or "Unsaved" text — a regex scan of the page for /unsaved|\*/ matched nothing), and clicking the back button navigated straight to the list with no confirmation prompt or dialog. (There is no dirty state at all, since edits are applied directly to the in-memory model, which is also never persisted.)

## Content

- [X] CT-01: All section labels and headings are clear and resume-appropriate
  - Action: Inspect the editor and preview headings (Contact, Work Experience, Education, Skills, plus customizable headings).
  - Expected: Labels use professional, standard resume terminology with no placeholder lorem-ipsum text, raw field codes, or developer artifacts.

- [X] CT-02: Preview content matches exactly what the user entered
  - Action: Enter distinctive values (e.g., email "qa.probe@example.com", company "TestNova Corp", skill "Kubernetes") and open the preview.
  - Expected: Each distinctive value appears verbatim, spelled as entered, with no truncation, reordering, or placeholder substitution.

- [X] CT-03: Template choices are displayed with meaningful previews and names
  - Action: Open the template selection area.
  - Expected: Each template has a name and a visual preview/thumbnail representing its style, and the number of templates offered is greater than one.

- [ ] CT-04: Empty sections and empty states display helpful text rather than blank areas
  - Action: View a newly created empty resume and a list with no saved resumes (after filtering to no matches).
  - Expected: Guidance text (e.g., "No work experience added yet") is shown; no unlabeled blank gaps or broken characters appear.
  - Bug Report:
    - Issue: Missing Empty-State Guidance Text
    - Actual: The saved-list empty state and the Skills tab are correct ("No resumes found / Try a different search term" and "No skills added yet. Add your first skill above!"), but the Experience and Education tabs of an empty resume show only a heading and an add button ("Work Experience" + "Add Experience", "Education" + "Add Education") with no guidance text, and the empty resume preview renders as `"Your Name"` followed by four completely empty `<div>` blocks — unlabeled blank gaps with no "No work experience added yet"-style hints and no broken characters.

- [X] CT-05: Saved resume list displays title and date created for each resume
  - Action: View the saved resumes list.
  - Expected: Each entry shows its title and a human-readable date created, with no blank or missing metadata.
  - Note: the date is rendered as "Updated Nov 7, 2026" / "Updated Feb 25, 2024" (update date, not an explicit "created" label); no entry has blank metadata.