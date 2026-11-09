# Test Checklist

## Functionality
- [ ] FT-01: User can choose a pre-designed template and open it in the resume editor.
  - Action: From the template gallery, select any template thumbnail and click "Use Template".
  - Expected: The resume editor opens with the selected template applied and the section fields visible.
- [ ] FT-02: User can enter contact details and they persist after saving.
  - Action: In "Contact", enter Full Name, Email, Phone, and Location, then click "Save". Reload the page and reopen the resume.
  - Expected: All four values are still displayed exactly as entered.
- [ ] FT-03: User can add a work experience entry.
  - Action: In "Work Experience", click "Add Experience", enter Job Title, Company, Start Date, End Date, and a description, then click "Save".
  - Expected: The entry appears in the Work Experience list with all entered values.
- [ ] FT-04: User can add an education entry and a skill.
  - Action: In "Education", click "Add Education" and enter School, Degree, and Graduation Year. In "Skills", add the skill "Project Management". Click "Save".
  - Expected: The education entry and the skill both appear in their sections.
- [ ] FT-05: User can reorder resume sections and the preview reflects the new order.
  - Action: Move "Skills" above "Education" using the section move controls, then click "Preview".
  - Expected: In the preview, "Skills" appears above "Education".
- [ ] FT-06: User can rename a section heading and the new heading is shown.
  - Action: Change the "Work Experience" heading to "Professional Experience", save, and open "Preview".
  - Expected: The heading shows "Professional Experience" in both the editor and the preview.
- [ ] FT-07: User can duplicate an existing saved resume into an independent copy.
  - Action: On an existing saved resume in the list, click "Duplicate". Open the new copy, change its Full Name, and save. Reopen the original.
  - Expected: The copy appears in the list as a new entry with the same content. The original's Full Name is unchanged.
- [ ] FT-08: User can rename a saved resume version.
  - Action: On a saved resume in the list, click "Rename", enter "Software Engineer - Acme", and confirm.
  - Expected: The list shows the new title, and it persists after page reload.
- [ ] FT-09: User can search saved resumes by title.
  - Action: Type part of an existing resume title (for example, "Engineer") into the "Search" box.
  - Expected: Only resumes whose titles contain the typed text are listed.
- [ ] FT-10: User can filter saved resumes by date created.
  - Action: Set the "Created" date filter to a range that includes some but not all default resumes, then apply it.
  - Expected: Only resumes created within the selected range are listed.

## Constraint
- [ ] CS-01: Resume cannot be saved when required contact fields are blank.
  - Action: Clear the "Full Name" field (marked with *) and click "Save".
  - Expected: Save is blocked, the message "Full Name is required" appears under the field, and the resume is not updated.
- [ ] CS-02: Invalid email format is rejected.
  - Action: Enter "john@" in the "Email" field and click "Save".
  - Expected: Save is blocked, and the message "Enter a valid email address" appears under the field.
- [ ] CS-03: Work experience cannot have an end date earlier than its start date.
  - Action: In a work experience entry, set Start Date to 06/2024 and End Date to 01/2023, then click "Save".
  - Expected: Save is blocked, and the message "End Date must be after Start Date" appears.
- [ ] CS-04: Resume title cannot be renamed to an empty value.
  - Action: Click "Rename" on a saved resume, clear the title field entirely, and click "Confirm".
  - Expected: The rename is blocked, the message "Title is required" appears, and the original title remains.
- [ ] CS-05: Leaving the editor with unsaved changes requires confirmation.
  - Action: Change the Full Name in an existing resume without saving, then click the "Back to Resumes" link.
  - Expected: A dialog titled "Unsaved changes" appears with "Discard" and "Keep Editing" options. "Keep Editing" returns to the editor with the change still present.

## Interaction
- [ ] IX-01: A success notification appears after a resume is saved.
  - Action: Edit any field in an existing resume and click "Save".
  - Expected: A toast notification reading "Resume saved" appears in the top-right corner for a few seconds.
- [ ] IX-02: Search results update as the user types, and an empty result shows a message.
  - Action: Type "zzzz" into the "Search" box, then clear the box.
  - Expected: While typing, the list updates immediately. For "zzzz", the list shows "No resumes found". Clearing the box restores the full list.
- [ ] IX-03: Preview shows the current unsaved edits and returns to the editor without losing them.
  - Action: In an open resume, change the Phone field without saving, click "Preview", then click "Back to Editor".
  - Expected: The preview displays the new Phone value. Returning to the editor keeps the edited Phone value in the field.

## Content
- [ ] CT-01: Template gallery thumbnails and icons load and are relevant to professional resumes.
  - Action: Open the template gallery and scroll through all template thumbnails.
  - Expected: Every thumbnail and icon loads with no broken images, and no lorem ipsum or unrelated imagery appears.
- [ ] CT-02: Preview displays the entered information accurately.
  - Action: Open an existing resume with contact, work experience, education, and skills data, then click "Preview".
  - Expected: Name, email, job titles, company names, dates, school names, and skills match the editor data exactly.
- [ ] CT-03: Saved resume list shows a populated title and a valid created date for every entry.
  - Action: Open the saved resumes list and review each row.
  - Expected: Every row shows a non-blank title and a readable created date (for example, "Nov 9, 2026"), with no "undefined" or "null" text.