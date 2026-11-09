# Test Checklist

## Functionality
- [ ] FT-01: Create a new resume with a title.
  - Action: Click "New Resume" (or equivalent), enter a title, and confirm creation.
  - Expected: A new resume entry is created and appears in the saved resumes list with the entered title.
- [ ] FT-02: Enter and edit contact details.
  - Action: Fill in the contact section fields (full name, email, phone, address/links), save, and reopen the resume.
  - Expected: All entered contact details are saved and shown again unchanged when the resume is reopened.
- [ ] FT-03: Add work experience entries.
  - Action: Add one work experience entry with job title, company, dates, and description; then add a second entry.
  - Expected: Both entries appear in the work experience section with all fields as entered, in the order added.
- [ ] FT-04: Add education entries.
  - Action: Add an education entry with degree, institution, and dates.
  - Expected: The entry appears in the education section with all fields as entered.
- [ ] FT-05: Add skills.
  - Action: Enter multiple skills in the skills section.
  - Expected: All entered skills are listed in the skills section without duplicates or dropped items.
- [ ] FT-06: Choose a template style.
  - Action: Open the template picker and select a different pre-designed template.
  - Expected: The selected template is applied to the resume and remains selected after saving and reopening.
- [ ] FT-07: Reorder sections.
  - Action: Move a section (e.g., Education) above another (e.g., Work Experience) using the section order control.
  - Expected: The new section order is saved and reflected in the resume layout.
- [ ] FT-08: Customize section headings.
  - Action: Rename a section heading (e.g., change "Work Experience" to "Employment History") and save.
  - Expected: The custom heading is displayed in place of the default one and persists after reopening.
- [ ] FT-09: Preview the resume.
  - Action: Open the preview for an edited resume.
  - Expected: A full resume preview is displayed showing all sections with the entered data and the chosen template.
- [ ] FT-10: Duplicate a resume version.
  - Action: Use "Duplicate" on an existing resume.
  - Expected: A new resume entry (e.g., "… copy") is created containing the same content and template as the original.
- [ ] FT-11: Rename a resume version.
  - Action: Use "Rename" on a saved resume, enter a new title, and confirm.
  - Expected: The saved resumes list shows the new title; no other resume data changes.
- [ ] FT-12: Save multiple variations for different job applications.
  - Action: Save three resumes with different titles and content, then reload the page.
  - Expected: All three resumes are listed after reload with their respective content intact.
- [ ] FT-13: Search saved resumes by title.
  - Action: Type a title keyword (or partial title) into the search field.
  - Expected: Only saved resumes whose title contains the keyword are listed; clearing the field restores the full list.
- [ ] FT-14: Filter saved resumes by date created.
  - Action: Apply the date-created filter (e.g., select a date or range matching one saved resume).
  - Expected: Only resumes created within the selected date criteria are listed.

## Constraint
- [ ] CS-01: Cannot save a resume with empty required fields.
  - Action: Leave the title and full name fields empty and attempt to save.
  - Expected: The save is blocked and a validation message indicates the missing required field(s).
- [ ] CS-02: A duplicated resume is independent of its original.
  - Action: Duplicate a resume, edit a field in the copy, then open the original.
  - Expected: The original's content is unchanged; edits affect only the copy.

## Interaction
- [ ] IX-01: Preview reflects edits immediately.
  - Action: Change a field (e.g., full name) and switch to the preview.
  - Expected: The preview shows the updated value without requiring a separate refresh step.
- [ ] IX-02: Search and filter results update as criteria change.
  - Action: Type into the search field and change the date filter one after the other.
  - Expected: The saved resumes list updates immediately after each keystroke/selection with no manual refresh button needed.

## Content
- [ ] CT-01: Pre-designed templates are present and visually distinct.
  - Action: Open the template picker and compare the available templates side by side.
  - Expected: Multiple templates are offered, each rendered with a clearly different layout/style, and all are selectable and functional.
- [ ] CT-02: Saved resume list metadata is accurate.
  - Action: Compare each entry in the saved resumes list with the resume's actual title and creation time.
  - Expected: Each entry displays the exact current title and the correct date created.