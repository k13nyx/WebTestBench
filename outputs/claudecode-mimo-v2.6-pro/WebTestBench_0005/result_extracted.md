# Test Result

## Functionality
- [X] FT-01: Create a new resume with a title.
  - Action: Click "New Resume" (or equivalent), enter a title, and confirm creation.
  - Expected: A new resume entry is created and appears in the saved resumes list with the entered title.
- [X] FT-02: Enter and edit contact details.
  - Action: Fill in the contact section fields (full name, email, phone, address/links), save, and reopen the resume.
  - Expected: All entered contact details are saved and shown again unchanged when the resume is reopened.
- [X] FT-03: Add work experience entries.
  - Action: Add one work experience entry with job title, company, dates, and description; then add a second entry.
  - Expected: Both entries appear in the work experience section with all fields as entered, in the order added.
- [X] FT-04: Add education entries.
  - Action: Add an education entry with degree, institution, and dates.
  - Expected: The entry appears in the education section with all fields as entered.
- [X] FT-05: Add skills.
  - Action: Enter multiple skills in the skills section.
  - Expected: All entered skills are listed in the skills section without duplicates or dropped items.
- [X] FT-06: Choose a template style.
  - Action: Open the template picker and select a different pre-designed template.
  - Expected: The selected template is applied to the resume and remains selected after saving and reopening.
- [X] FT-07: Reorder sections.
  - Action: Move a section (e.g., Education) above another (e.g., Work Experience) using the section order control.
  - Expected: The new section order is saved and reflected in the resume layout.
- [X] FT-08: Customize section headings.
  - Action: Rename a section heading (e.g., change "Work Experience" to "Employment History") and save.
  - Expected: The custom heading is displayed in place of the default one and persists after reopening.
- [X] FT-09: Preview the resume.
  - Action: Open the preview for an edited resume.
  - Expected: A full resume preview is displayed showing all sections with the entered data and the chosen template.
- [X] FT-10: Duplicate a resume version.
  - Action: Use "Duplicate" on an existing resume.
  - Expected: A new resume entry (e.g., "… copy") is created containing the same content and template as the original.
- [X] FT-11: Rename a resume version.
  - Action: Use "Rename" on a saved resume, enter a new title, and confirm.
  - Expected: The saved resumes list shows the new title; no other resume data changes.
- [ ] FT-12: Save multiple variations for different job applications.
  - Action: Save three resumes with different titles and content, then reload the page.
  - Expected: All three resumes are listed after reload with their respective content intact.
  - Bug Report:
    - Issue: Data Persistence Failure — saved resumes are not persisted across page reloads (in-memory state only; no storage writes)
    - Actual: After creating "QA Test Resume Alpha", "QA Test Resume Beta", and "QA Test Resume Gamma" (all visible in the list beforehand), a page reload left only the 3 pre-existing resumes ("Product Designer Resume", "Marketing Manager Resume", "Software Engineer Resume"). All user-created resumes and their content were lost, and `window.localStorage` is completely empty — the app never writes resume data to storage, so every reload re-seeds only the 3 mock resumes.
- [X] FT-13: Search saved resumes by title.
  - Action: Type a title keyword (or partial title) into the search field.
  - Expected: Only saved resumes whose title contains the keyword are listed; clearing the field restores the full list.
- [ ] FT-14: Filter saved resumes by date created.
  - Action: Apply the date-created filter (e.g., select a date or range matching one saved resume).
  - Expected: Only resumes created within the selected date criteria are listed.
  - Bug Report:
    - Issue: Missing Feature — no date-created filter control exists on the saved resumes page
    - Actual: The only filter/sort control next to the search field is a combobox containing exactly four sort orders ("Newest First", "Oldest First", "Title A-Z", "Title Z-A"). There is no date picker, date-range selector, or any control to filter resumes by creation date criteria; the action cannot be performed.

## Constraint
- [ ] CS-01: Cannot save a resume with empty required fields.
  - Action: Leave the title and full name fields empty and attempt to save.
  - Expected: The save is blocked and a validation message indicates the missing required field(s).
  - Bug Report:
    - Issue: Missing Validation — empty required fields (title, full name) are accepted and saved without any validation message
    - Actual: Creating a new resume immediately persists it as "Untitled Resume" with no title prompt. Clearing the title to an empty string and confirming silently reverts to "Untitled Resume", the Full Name field remains empty ("") and is accepted, no "Save" button exists (the editor auto-saves), and no validation message appears anywhere. On returning to the list, the empty resume was saved and listed as "Untitled Resume" — the save was not blocked.

## Interaction
- [X] IX-01: Preview reflects edits immediately.
  - Action: Change a field (e.g., full name) and switch to the preview.
  - Expected: The preview shows the updated value without requiring a separate refresh step.
- [ ] IX-02: Search and filter results update as criteria change.
  - Action: Type into the search field and change the date filter one after the other.
  - Expected: The saved resumes list updates immediately after each keystroke/selection with no manual refresh button needed.
  - Bug Report:
    - Issue: Missing Element — the required date filter control does not exist, so the action cannot be fully executed
    - Actual: Typing into the search field updates the list immediately on every keystroke (verified: "Alpha" → 1 result, "zzz" → "No resumes found", clearing → full list, no refresh button involved). However, the "change the date filter" step cannot be performed: the only adjacent control is the sort combobox ("Newest First"/"Oldest First"/"Title A-Z"/"Title Z-A") — there is no date filter to change. (Sort selections themselves do update the list immediately.)

## Content
- [X] CT-01: Pre-designed templates are present and visually distinct.
  - Action: Open the template picker and compare the available templates side by side.
  - Expected: Multiple templates are offered, each rendered with a clearly different layout/style, and all are selectable and functional.
- [ ] CT-02: Saved resume list metadata is accurate.
  - Action: Compare each entry in the saved resumes list with the resume's actual title and creation time.
  - Expected: Each entry displays the exact current title and the correct date created.
  - Bug Report:
    - Issue: Incorrect Metadata — list entries display the last-updated timestamp (labeled "Updated") instead of the date created
    - Actual: Each card renders "Updated <date>" (e.g., "QA Renamed Resume — Updated Nov 8, 2026"). The underlying resume data contains two distinct timestamps — `createdAt: "2026-11-08T08:26:08.481Z"` and `updatedAt: "2026-11-08T08:26:33.245Z"` — and the card displays the `updatedAt` value; the date created is never shown anywhere in the list. Titles are displayed exactly and correctly (verified through a rename), but the creation-date requirement is not met.
