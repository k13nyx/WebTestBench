# Test Checklist

## Functionality

- [ ] FT-01: User can create a new resume using a pre-designed template
  - Action: Click the "Create New Resume" (or equivalent) button and select any template from the template gallery.
  - Expected: A new resume is created and opens in the editor using the selected template, appearing in the list of saved resumes.

- [ ] FT-02: User can enter contact details
  - Action: Open a resume in the editor, fill in contact fields (e.g., full name, email, phone), and save.
  - Expected: The entered contact details are stored and displayed in the resume (editor and preview) after saving and reloading.

- [ ] FT-03: User can add and edit work experience entries
  - Action: In the editor, add a work experience entry (job title, company, dates, description), save, then edit one field of that entry and save again.
  - Expected: The work experience entry appears in the resume with the entered values, and the edited change is persisted.

- [ ] FT-04: User can add and edit education and skills entries
  - Action: Add an education entry (degree, institution, dates) and at least one skill; save the resume.
  - Expected: The education and skills sections display the added entries with correct values after saving.

- [ ] FT-05: User can choose/change the template style
  - Action: Open a resume in the editor and switch to a different template from the available template options.
  - Expected: The resume's visual style changes to the newly selected template while the entered content (contact, experience, education, skills) is preserved.

- [ ] FT-06: User can reorder resume sections
  - Action: Use the section order control (e.g., drag handles or up/down buttons) to move one section (e.g., Skills above Work Experience) and save.
  - Expected: The sections appear in the newly specified order in the preview and after saving.

- [ ] FT-07: User can customize section headings
  - Action: Edit a section heading (e.g., change "Work Experience" to "Professional Experience") and save.
  - Expected: The custom heading replaces the default heading in the preview and persists after saving.

- [ ] FT-08: User can preview the resume
  - Action: Open the preview mode for a resume that contains entered data.
  - Expected: A full resume preview is displayed showing all sections (contact, work experience, education, skills) with the entered content and the applied template style.

- [ ] FT-09: User can duplicate a saved resume
  - Action: Use the "Duplicate" action on a saved resume (default data).
  - Expected: A copy of the resume is created (e.g., titled "Copy of [original title]") with identical content, and both the original and the copy appear in the saved resumes list.

- [ ] FT-10: User can rename a saved resume
  - Action: Use the "Rename" action on a saved resume, enter a new title, and confirm.
  - Expected: The resume's title is updated in the saved resumes list, and its content is unchanged.

- [ ] FT-11: User can save multiple resume variations
  - Action: Duplicate an existing resume, modify its content (e.g., change the job title or summary), and save.
  - Expected: Both variations exist independently in the saved resumes list — the edit appears only in the duplicated version, not in the original.

- [ ] FT-12: User can search saved resumes by title
  - Action: Type the exact title (or a distinctive part of a title) of an existing saved resume into the search box.
  - Expected: Only resumes whose titles match the search text are shown; non-matching resumes are hidden.

- [ ] FT-13: User can filter saved resumes by date created
  - Action: Apply a date filter (e.g., "Last 7 days" or a specific date range) on the saved resumes list.
  - Expected: Only resumes whose creation dates fall within the selected filter are displayed; resumes outside the range are hidden.

## Constraint

- [ ] CS-01: Cannot save a resume with a missing required title
  - Action: Attempt to save or create a resume while leaving the resume title field empty.
  - Expected: The save is blocked and a validation message (e.g., "Title is required") is shown; no untitled resume is added to the saved list.

- [ ] CS-02: Search with no matches returns an empty state, not the full list
  - Action: Enter a search query that does not match any saved resume title (e.g., "zzzzz").
  - Expected: No resumes are listed and a "no results" indicator is shown; the list does not display all resumes.

- [ ] CS-03: Reordering preserves all sections exactly once
  - Action: Reorder multiple sections, save the resume, and reopen it.
  - Expected: Every original section appears exactly once (none missing, none duplicated) and in the specified order.

## Interaction

- [ ] IX-01: Preview updates in real time as content is edited
  - Action: With the preview visible, type a character into any resume field (e.g., change the name).
  - Expected: The preview immediately reflects the new value without requiring a page reload or manual refresh.

- [ ] IX-02: Save action shows a success confirmation
  - Action: Click the "Save" button after making a valid change.
  - Expected: A visible success indicator (e.g., toast/message "Resume saved") appears; no error is shown.

- [ ] IX-03: Selecting a template immediately updates the resume appearance
  - Action: In the editor or template picker, click a different template thumbnail.
  - Expected: The resume/preview instantly re-renders in the selected style without needing to save first.

## Content

- [ ] CT-01: All offered templates are professionally designed resume layouts
  - Action: Browse the full template gallery and inspect each template.
  - Expected: Every template is a legitimate resume layout (header, structured sections); no broken, blank, or non-resume designs appear.

- [ ] CT-02: Resume content matches entered data and the resume theme
  - Action: Open the preview of a resume with entered data and inspect all sections and labels.
  - Expected: All displayed text, labels, and values are relevant to a professional resume and exactly match the data entered in the editor; no placeholder/dummy text appears where the user entered real content.