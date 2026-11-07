# Test Checklist

## Functionality
- [ ] FT-01: User can create a new resume
  - Action: Click the "New Resume" button and select a starting template.
  - Expected: A new editable resume document opens with default sections (contact, work experience, education, skills).

- [ ] FT-02: User can enter and edit contact details
  - Action: Fill in the contact fields (name, email, phone, address) and click "Save" or move to another field.
  - Expected: Entered contact information is stored and displayed in the resume.

- [ ] FT-03: User can add and edit work experience entries
  - Action: Click "Add Experience", enter job title/company/dates/description, then save.
  - Expected: The work experience entry appears in the resume with the entered data.

- [ ] FT-04: User can add and edit education entries
  - Action: Click "Add Education", enter school/degree/dates, then save.
  - Expected: The education entry appears in the resume with the entered data.

- [ ] FT-05: User can add and edit skills
  - Action: Enter skill items into the skills section and save.
  - Expected: Listed skills appear in the resume skills section.

- [ ] FT-06: User can choose a template style
  - Action: Open the "Template" selector and pick a different pre-designed style.
  - Expected: The resume layout/visual style updates to the selected template.

- [ ] FT-07: User can reorder resume sections
  - Action: Use the section reorder control to change the order of sections (e.g., move Skills above Education).
  - Expected: Sections appear in the new order in the resume.

- [ ] FT-08: User can edit section headings
  - Action: Rename a section heading (e.g., change "Work Experience" to "Professional History").
  - Expected: The updated heading is shown in the resume.

- [ ] FT-09: User can preview the resume
  - Action: Click the "Preview" button.
  - Expected: A formatted preview of the resume is displayed reflecting current content and template.

- [ ] FT-10: User can duplicate a resume version
  - Action: Open a saved resume's menu and click "Duplicate".
  - Expected: A new copy of the resume is created and listed alongside the original.

- [ ] FT-11: User can rename a resume version
  - Action: Open a resume's menu, click "Rename", and enter a new title.
  - Expected: The resume is listed under the new title.

- [ ] FT-12: User can save multiple resume variations
  - Action: Save two or more resumes with different content/templates and distinct titles.
  - Expected: All saved variations are listed and individually retrievable.

- [ ] FT-13: User can search saved resumes by title
  - Action: Type a title keyword into the search box.
  - Expected: Only saved resumes whose title matches the keyword are shown.

- [ ] FT-14: User can filter saved resumes by date created
  - Action: Set the "Date Created" filter (e.g., newest first / a date range).
  - Expected: The saved-resume list is reordered or narrowed to match the selected date criteria.

## Constraint
- [ ] CS-01: Rename cannot be left empty
  - Action: Open "Rename", clear the title field, and submit.
  - Expected: The rename is rejected with a message and the original title is retained.

- [ ] CS-02: Section reorder must preserve all sections
  - Action: Reorder sections and verify the section set.
  - Expected: No section is lost, duplicated, or omitted after reordering.

## Interaction
- [ ] IX-01: Live update of preview as the user edits
  - Action: Edit a field (e.g., change the name) while preview is open.
  - Expected: The preview reflects the change without a full page reload.

- [ ] IX-02: Confirmation after saving a resume
  - Action: Click "Save" on a resume.
  - Expected: A success confirmation (toast or message) appears indicating the resume was saved.

## Content
- [ ] CT-01: Available templates are pre-designed professional styles
  - Action: Open the template selector.
  - Expected: Displayed options are distinct, professionally designed resume templates (not blank/raw).

- [ ] CT-02: Resume content sections match the intended theme
  - Action: Inspect the default resume structure.
  - Expected: Sections present are relevant to a professional resume (contact, work experience, education, skills) with no unrelated content.