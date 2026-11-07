# Test Result

## Functionality

- [X] FT-01: User can create a new resume
  - Action: On the resume-builder page, click the "New Resume" (or "+") button and confirm creation.
  - Expected: A new blank resume opens in the editor, and it appears in the saved resumes list with a default title (e.g., "Untitled Resume").

- [X] FT-02: User can enter and save contact details
  - Action: In the Contact/Contact Details section, fill in Full Name, Email, Phone, and Location, then click "Save".
  - Expected: All four values persist after saving and are displayed in the resume preview.

- [X] FT-03: User can add a work experience entry
  - Action: In the "Work Experience" section, click "Add" and enter Job Title, Company, Start Date, End Date, and a description; click "Save".
  - Expected: The new entry appears as a listed work experience item and is rendered in the preview with all entered values.

- [X] FT-04: User can add education and skills entries
  - Action: In the "Education" section, click "Add" and enter School, Degree, and Year; then in the "Skills" section, click "Add" and enter a skill.
  - Expected: The education entry and the skill are both added to their sections and rendered in the preview.

- [X] FT-05: User can edit previously entered information
  - Action: Reopen a saved resume, change the Job Title of an existing work experience entry, and click "Save".
  - Expected: The edited value is saved and shown in the preview; only that value changed.

- [X] FT-06: User can choose a template style
  - Action: Open the template selector and select a second template (different from the current one).
  - Expected: The resume preview immediately adopts the selected template's style, and the selection is indicated as active and persists after saving.

- [X] FT-07: User can reorder resume sections
  - Action: In the layout/section-order control, move "Skills" above "Education".
  - Expected: The section order in the preview matches the new order (Skills appears before Education) and persists after saving.

- [X] FT-08: User can customize a section heading
  - Action: Edit the heading of the "Work Experience" section to "Professional Experience".
  - Expected: The preview displays "Professional Experience" as that section's heading and the custom heading persists after saving.

- [X] FT-09: User can preview the resume
  - Action: With contact details, one experience entry, one education entry, and one skill entered, click "Preview".
  - Expected: A resume preview is displayed containing all entered content, arranged in the configured section order, using the selected template.

- [X] FT-10: User can save a resume with a specific title
  - Action: Set the resume title to "Software Engineer Resume" and click "Save".
  - Expected: The resume is saved and listed as "Software Engineer Resume" in the saved resumes list.

- [X] FT-11: User can duplicate a saved resume
  - Action: In the saved resumes list, click "Duplicate" on any existing default resume.
  - Expected: A new entry appears in the list, containing the same content as the source resume, with a distinguishing title (e.g., "Resume (Copy)" or "Resume 2").

- [X] FT-12: User can rename a saved resume or version
  - Action: Click "Rename" on a saved resume, enter "Marketing Manager Version", and confirm.
  - Expected: The list entry's title updates to "Marketing Manager Version" and remains changed after reopening.

- [ ] FT-13: User can search saved resumes by title and filter by date created
  - Action: Type a word contained in one default resume's title (e.g., "Engineer") into the search box; then clear it and apply the date-created filter/sort to the default list.
  - Expected: Searching shows only resumes whose titles contain that word; clearing it restores the full list. The date filter/sort returns only resumes created within the selected date range.
  - Bug Report:
    - Issue: Missing date-created filter control
    - Actual: Search works correctly (typing "Engineer" reduced the list to only "Software Engineer Resume"; clearing the box restored all 6 resumes). However, there is no date-created *filter* / date-range control anywhere on the page — the only control next to the search box is a sort dropdown offering "Newest First", "Oldest First", "Title A-Z", "Title Z-A". Selecting "Oldest First" only re-orders the list (Software Engineer Resume Jan 20 2024 → Marketing Manager Resume Feb 10 2024 → Product Designer Resume Feb 25 2024 → ...); it never removes resumes outside a date range, so no result set is ever filtered by creation date.

## Constraint

- [X] CS-01: Editing a duplicated resume does not change the original
  - Action: Duplicate a default resume, open the copy, change its Job Title, and save; then open the original.
  - Expected: The copy shows the new Job Title and the original still shows its original Job Title and all other unchanged content.

- [ ] CS-02: Cannot save a resume with an empty title
  - Action: Clear the resume title field and click "Save".
  - Expected: Saving is blocked, an inline error (e.g., "Title is required") appears near the title field, and no blank-titled entry is added to the saved list.
  - Bug Report:
    - Issue: Missing validation on empty resume title
    - Actual: In the "Rename Resume" dialog the title field was cleared and "Save" clicked — the dialog closed without any error message and the saved-resumes list now contains an entry whose title is completely blank (card renders as an empty level-3 heading with only "Updated Nov 8, 2026" and "modern" beneath it). No inline error such as "Title is required" was displayed anywhere on the page (page text contains no "required" string). When the same test was done on the inline editor title, the blank value was silently discarded and reverted to the previous title — again with no error message.

- [ ] CS-03: Cannot add a section entry with required fields blank
  - Action: In "Work Experience", click "Add" and submit with Job Title and Company left empty.
  - Expected: The entry is not created; a validation error is shown and no empty item appears in the section or preview.
  - Bug Report:
    - Issue: Missing required-field validation on section entries
    - Actual: Clicking "Add Experience" with Job Title and Company left blank immediately created a second entry card ("Position 2") with empty Company/Position/Date/Description fields. No validation error or warning was displayed, and the blank entry was rendered in the resume preview as an empty item (empty heading, a bare "–" date separator, two empty paragraphs) inside the "Professional Experience" section.

## Interaction

- [X] IX-01: Preview updates in response to edits without a page reload
  - Action: With the editor open, type a new value into the Full Name field.
  - Expected: The preview reflects the new value without a page refresh or leaving the page.

- [ ] IX-02: Confirmation feedback appears after save, duplicate, and rename
  - Action: Perform a "Save", then a "Duplicate", then a "Rename".
  - Expected: Each action shows a brief confirmation (e.g., a toast/notification reading "Saved" / "Duplicated" / "Renamed") that disappears without user action.
  - Bug Report:
    - Issue: No confirmation/toast feedback after save, duplicate, or rename
    - Actual: The page contains an empty toast container (`region "Notifications (F8)"` with an empty `list`), and it stayed empty after every action. A Duplicate action added "Product Designer Resume (Copy)" / "QA Test Resume (Copy)" / "Software Engineer Resume (Copy)" to the list, and a Rename changed a card to "Marketing Manager Version", but no toast, snackbar, or status message ("Saved", "Duplicated", "Renamed") ever appeared — a MutationObserver attached to the notification list recorded zero toast elements across a duplicate action. Additionally, the editor exposes no "Save" button at all (header contains only back, inline title, and "Hide Preview"), so no "Saved" confirmation can be produced; changes are committed automatically.

## Content

- [X] CT-01: Section headings and field labels are resume-relevant and correct
  - Action: Inspect all section headings and form field labels in the editor (Contact, Work Experience, Education, Skills).
  - Expected: Every label is spelled correctly and directly relates to resume content; no placeholder, sample, or lorem ipsum text is displayed as default content.

- [ ] CT-02: Template options and saved-resume entries display correct, working content
  - Action: View the template selector thumbnails and the saved resumes list.
  - Expected: Each template option displays a labeled, professional resume preview that loads fully (no broken/missing images), and each saved-resume entry shows its title and its creation date.
  - Bug Report:
    - Issue: Template options have no preview thumbnail; saved entries show "Updated" date instead of creation date
    - Actual: The template selector ("Template Style" tab) renders each option as only a name plus a one-line description — "Modern / Clean design with accent colors and clear hierarchy", "Classic / Traditional layout perfect for corporate roles", "Minimal / Simple and elegant with focus on content" — with no resume preview thumbnail or layout mock-up at all (the only graphic is the check-mark icon shown on the selected option). Separately, each saved-resume card displays its title and a date labeled "Updated <date>" (e.g., "Updated Feb 25, 2024"), not a creation date. No broken images were found (the page uses inline SVG icons; zero broken `<img>` elements).

### Cross-cutting note
The editor has no explicit "Save" button — edits (contact details, entries, template, section order/headings, title) are committed to state automatically and persist when returning to the list and reopening the resume. FT-02…FT-10 were evaluated against their stated Expected results (values persist and render), which were met.