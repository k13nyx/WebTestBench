# Test Result

## Functionality

- [X] FT-01: User can create a new resume from a pre-designed template.
  - Action: On the resume dashboard, click "New Resume" and select any available template.
  - Expected: A new editable resume opens, pre-populated with the selected template's default sections.

- [X] FT-02: User can enter contact details.
  - Action: In the contact section, enter full name, email, phone, and location.
  - Expected: Each field accepts and retains the typed value.

- [X] FT-03: User can add work experience entries.
  - Action: In the Work Experience section, add an entry with job title, company, dates, and description.
  - Expected: The new entry is saved and listed under Work Experience with the entered details.

- [X] FT-04: User can add education entries.
  - Action: In the Education section, add an entry with degree, institution, and dates.
  - Expected: The new entry is saved and listed under Education with the entered details.

- [X] FT-05: User can add skills.
  - Action: In the Skills section, add at least three skills.
  - Expected: All added skills appear in the Skills list.

- [X] FT-06: User can choose a template style.
  - Action: Open the template selector and pick a different template.
  - Expected: The resume re-renders with the newly selected template style while keeping the entered data.

- [X] FT-07: User can reorder resume sections.
  - Action: Drag or use controls to move the Education section above Work Experience.
  - Expected: Sections appear in the new order in both the editor and the preview.

- [X] FT-08: User can edit section headings.
  - Action: Change the "Work Experience" heading to "Professional Experience".
  - Expected: The heading updates to the edited text in the preview.

- [X] FT-09: User can preview the resume.
  - Action: Click "Preview".
  - Expected: A preview opens displaying the resume with the current data, template, and layout.

- [X] FT-10: User can duplicate a saved resume version.
  - Action: Open a saved resume and click "Duplicate".
  - Expected: A new copy of that resume is created and listed separately from the original.

- [X] FT-11: User can rename a resume version.
  - Action: Use the rename option on a saved resume and enter a new title.
  - Expected: The resume appears under the new title in the saved list.

- [X] FT-12: User can save multiple variations for different job applications.
  - Action: Save two resumes with different titles and distinct content.
  - Expected: Both are stored and independently retrievable from the saved list.

- [X] FT-13: User can search saved resumes by title.
  - Action: In the saved-resumes search box, type a title that matches one saved resume.
  - Expected: Only the matching resume(s) are displayed.

- [ ] FT-14: User can filter saved resumes by date created.
  - Action: Apply the date-created filter and select a date range.
  - Expected: Only resumes created within the selected range are displayed.
  - Bug Report:
    - Issue: Missing Feature — No date-created filter control
    - Actual: The only filter/sort control on the dashboard is a dropdown ("Newest First") that offers sort options only ("Newest First", "Oldest First", "Title A-Z", "Title Z-A"). There is no date-created filter and no date-range selector (0 date inputs exist on the dashboard; only a free-text "Search resumes..." box). Selecting a date range is therefore impossible.

## Constraint

- [X] CS-01: Editing a duplicated resume does not alter the original.
  - Action: Duplicate a saved resume, change its contact details, then open the original.
  - Expected: The original retains its previous details unchanged.

- [X] CS-02: Renaming a resume to a blank title is rejected.
  - Action: Attempt to save a rename with an empty title field.
  - Expected: The save is blocked and the previous title is retained.

- [X] CS-03: Search with no matching title returns an empty state, not all resumes.
  - Action: Search for a title string not present in any saved resume.
  - Expected: A "no results" state shows and no unrelated resumes are listed.

## Interaction

- [X] IX-01: Preview updates immediately when resume content changes.
  - Action: Edit a field (e.g., contact name) while the preview is open.
  - Expected: The preview reflects the change without a manual refresh.

- [ ] IX-02: Confirmation feedback appears after saving a resume.
  - Action: Click "Save" on an edited resume.
  - Expected: A success confirmation (e.g., toast or message) is displayed.
  - Bug Report:
    - Issue: Missing Save Control / No Confirmation Feedback
    - Actual: The resume editor contains no "Save" button (header holds only Back, Title, and "Hide Preview"; edits persist silently via auto-save). No success confirmation (toast or message) is displayed after editing a field, and the "Notifications (F8)" toast region remains empty. Even the rename dialog's "Save" button produces no confirmation toast.

- [X] IX-03: Selected template is visibly indicated.
  - Action: Select a template in the template selector.
  - Expected: The chosen template is highlighted/marked as the active selection.

## Content

- [ ] CT-01: Displayed template thumbnails represent resume layouts.
  - Action: Inspect the template selector thumbnails.
  - Expected: Each thumbnail shows a resume-style layout relevant to the resume-building purpose.
  - Bug Report:
    - Issue: Missing Content — No template layout thumbnails
    - Actual: The template selector (Template tab) renders each option as only a heading + a one-line text description ("Modern — Clean design with accent colors…", "Classic — Traditional layout…", "Minimal — Simple and elegant…"). No image/thumbnail is present in any template card (the only `img`/svg shown is the checkmark on the currently-selected template). No resume-style layout thumbnail is displayed. Dashboard resume cards likewise show only a generic document icon, not a layout thumbnail.

- [X] CT-02: Default placeholder text is resume-relevant.
  - Action: Create a new resume and inspect unfilled fields.
  - Expected: Placeholders use resume terminology (e.g., "Job Title", "Company", "Degree") with no unrelated text.

- [X] CT-03: Section labels and icons match their content.
  - Action: Review the section headings and any accompanying icons in the editor.
  - Expected: Each label/icon (contact, experience, education, skills) matches the content it represents.
