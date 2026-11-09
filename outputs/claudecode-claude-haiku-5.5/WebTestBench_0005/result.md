# Test Result

## Functionality
- [ ] FT-01: User can choose a pre-designed template and open it in the resume editor.
  - Action: From the template gallery, select any template thumbnail and click "Use Template".
  - Expected: The resume editor opens with the selected template applied and the section fields visible.
  - Bug Report:
    - Issue: Missing Element (Template Gallery / "Use Template" button)
    - Actual: "New Resume" opened the editor directly. No template gallery or "Use Template" button exists anywhere in the app. The editor's "Template" tab shows three text-only style cards (Modern, Classic, Minimal) with no thumbnails. The editor opened with section fields visible, but the gallery step in the Action cannot be performed.
- [ ] FT-02: User can enter contact details and they persist after saving.
  - Action: In "Contact", enter Full Name, Email, Phone, and Location, then click "Save". Reload the page and reopen the resume.
  - Expected: All four values are still displayed exactly as entered.
  - Bug Report:
    - Issue: Data Not Persisted / Missing Element (Save button)
    - Actual: The editor has no "Save" button. Values entered as "Jane Smith", "jane.smith@example.com", "(555) 867-5309", and "Austin, TX" appeared in the editor and live preview. After a page reload, the resume was gone from the list and could not be reopened, so the values were not retained.
- [X] FT-03: User can add a work experience entry.
  - Action: In "Work Experience", click "Add Experience", enter Job Title, Company, Start Date, End Date, and a description, then click "Save".
  - Expected: The entry appears in the Work Experience list with all entered values.
  - Note: The entry showed the correct title, company, date range ("Jan 2020 - Jun 2023"), and description in the editor and preview. There is no "Save" button, and the entry was lost on reload (see FT-02). Date fields are month inputs and need YYYY-MM entry.
- [X] FT-04: User can add an education entry and a skill.
  - Action: In "Education", click "Add Education" and enter School, Degree, and Graduation Year. In "Skills", add the skill "Project Management". Click "Save".
  - Expected: The education entry and the skill both appear in their sections.
  - Note: Both appeared in their sections and in the preview. There is no "Graduation Year" field (End Date was used), and there is no "Save" button. Minor defect: with an empty Field of Study, the preview reads "Bachelor of Science in". Lost on reload (see FT-02).
- [X] FT-05: User can reorder resume sections and the preview reflects the new order.
  - Action: Move "Skills" above "Education" using the section move controls, then click "Preview".
  - Expected: In the preview, "Skills" appears above "Education".
  - Note: After the move, the preview order was Work Experience, Skills, Education. The preview is a persistent side panel, so no separate "Preview" click was needed.
- [X] FT-06: User can rename a section heading and the new heading is shown.
  - Action: Change the "Work Experience" heading to "Professional Experience", save, and open "Preview".
  - Expected: The heading shows "Professional Experience" in both the editor and the preview.
  - Note: The section-name input and the preview heading both showed "Professional Experience" (verified in the DOM).
- [X] FT-07: User can duplicate an existing saved resume into an independent copy.
  - Action: On an existing saved resume in the list, click "Duplicate". Open the new copy, change its Full Name, and save. Reopen the original.
  - Expected: The copy appears in the list as a new entry with the same content. The original's Full Name is unchanged.
  - Note: "Software Engineer Resume (Copy)" appeared at the top of the list with identical content. Changing the copy's Full Name to "Alex Morgan (Copy)" left the original's Full Name as "Alex Morgan". Duplicates were lost on reload (see FT-08).
- [ ] FT-08: User can rename a saved resume version.
  - Action: On a saved resume in the list, click "Rename", enter "Software Engineer - Acme", and confirm.
  - Expected: The list shows the new title, and it persists after page reload.
  - Bug Report:
    - Issue: Data Not Persisted
    - Actual: The rename to "Software Engineer - Acme" showed in the list during the session. After a page reload, the list showed "Software Engineer Resume" again, so the rename was not persisted. The dialog's button is labeled "Save", not "Confirm".
- [X] FT-09: User can search saved resumes by title.
  - Action: Type part of an existing resume title (for example, "Engineer") into the "Search" box.
  - Expected: Only resumes whose titles contain the typed text are listed.
  - Note: Searching "Engineer" listed only "Software Engineer Resume".
- [ ] FT-10: User can filter saved resumes by date created.
  - Action: Set the "Created" date filter to a range that includes some but not all default resumes, then apply it.
  - Expected: Only resumes created within the selected range are listed.
  - Bug Report:
    - Issue: Missing Element (Created date filter)
    - Actual: No "Created" date filter exists. The DOM has no date inputs and no "Created" label. The only controls are the "Search resumes..." box and a "Newest First" sort dropdown.

## Constraint
- [ ] CS-01: Resume cannot be saved when required contact fields are blank.
  - Action: Clear the "Full Name" field (marked with *) and click "Save".
  - Expected: Save is blocked, the message "Full Name is required" appears under the field, and the resume is not updated.
  - Bug Report:
    - Issue: Missing Validation (Required Field)
    - Actual: The Full Name was cleared and no "Full Name is required" message appeared (DOM check negative). There is no "Save" button, and the blank value was applied to the resume immediately. The value was restored afterward.
- [ ] CS-02: Invalid email format is rejected.
  - Action: Enter "john@" in the "Email" field and click "Save".
  - Expected: Save is blocked, and the message "Enter a valid email address" appears under the field.
  - Bug Report:
    - Issue: Missing Validation (Email Format)
    - Actual: The email "john@" was accepted. The text "Enter a valid email address" did not appear, and no error element was rendered. There is no "Save" button.
- [ ] CS-03: Work experience cannot have an end date earlier than its start date.
  - Action: In a work experience entry, set Start Date to 06/2024 and End Date to 01/2023, then click "Save".
  - Expected: Save is blocked, and the message "End Date must be after Start Date" appears.
  - Bug Report:
    - Issue: Missing Validation (Date Range)
    - Actual: Start 2024-06 and End 2023-01 were accepted. The preview displayed "Jun 2024 - Jan 2023", and the message "End Date must be after Start Date" did not appear. The original dates were restored afterward.
- [ ] CS-04: Resume title cannot be renamed to an empty value.
  - Action: Click "Rename" on a saved resume, clear the title field entirely, and click "Confirm".
  - Expected: The rename is blocked, the message "Title is required" appears, and the original title remains.
  - Bug Report:
    - Issue: Validation Bypass (Empty Title Saved)
    - Actual: The title was cleared and "Save" was clicked (the dialog's button is "Save", not "Confirm"). The dialog closed with no "Title is required" message, and the list row's title became blank. The original title was not kept.
- [ ] CS-05: Leaving the editor with unsaved changes requires confirmation.
  - Action: Change the Full Name in an existing resume without saving, then click the "Back to Resumes" link.
  - Expected: A dialog titled "Unsaved changes" appears with "Discard" and "Keep Editing" options. "Keep Editing" returns to the editor with the change still present.
  - Bug Report:
    - Issue: Unsaved Changes Guard Missing
    - Actual: Clicking the back button navigated straight to the list. No dialog appeared (DOM check negative). The Full Name change was auto-saved, and the list row updated to "Updated Nov 9, 2026".

## Interaction
- [ ] IX-01: A success notification appears after a resume is saved.
  - Action: Edit any field in an existing resume and click "Save".
  - Expected: A toast notification reading "Resume saved" appears in the top-right corner for a few seconds.
  - Bug Report:
    - Issue: Missing Feedback (Save Notification)
    - Actual: There is no "Save" button. After several field edits, no "Resume saved" text appeared in the document or the notification region. Edits were applied silently.
- [X] IX-02: Search results update as the user types, and an empty result shows a message.
  - Action: Type "zzzz" into the "Search" box, then clear the box.
  - Expected: While typing, the list updates immediately. For "zzzz", the list shows "No resumes found". Clearing the box restores the full list.
  - Note: "zzzz" showed "No resumes found". Clearing the box restored all four resumes. Per-keystroke updating was not observed separately, because the fill tool sets the full value at once.
- [X] IX-03: Preview shows the current unsaved edits and returns to the editor without losing them.
  - Action: In an open resume, change the Phone field without saving, click "Preview", then click "Back to Editor".
  - Expected: The preview displays the new Phone value. Returning to the editor keeps the edited Phone value in the field.
  - Note: Changing Phone to "(555) 000-1111" and toggling "Hide Preview" / "Show Preview" showed the new phone in the preview, and the editor kept the value. The controls are labeled "Hide Preview" and "Show Preview", with no "Preview" or "Back to Editor" buttons. Behavior matched; labels differ from the Action.

## Content
- [ ] CT-01: Template gallery thumbnails and icons load and are relevant to professional resumes.
  - Action: Open the template gallery and scroll through all template thumbnails.
  - Expected: Every thumbnail and icon loads with no broken images, and no lorem ipsum or unrelated imagery appears.
  - Bug Report:
    - Issue: Missing Element (Template Gallery Thumbnails)
    - Actual: No template gallery or thumbnail images exist. The Template tab shows three text-only style cards. A later attempt to open the Template tab through script did not switch panels, so the image check could not be completed within the test budget.
- [X] CT-02: Preview displays the entered information accurately.
  - Action: Open an existing resume with contact, work experience, education, and skills data, then click "Preview".
  - Expected: Name, email, job titles, company names, dates, school names, and skills match the editor data exactly.
  - Note: For "Software Engineer Resume", the preview matched the editor: Alex Morgan, alex.morgan@email.com, Senior Software Engineer / TechCorp Inc. (Mar 2022 - Present), Software Engineer / StartupXYZ (Jun 2019 - Feb 2022), and skills React, TypeScript, Node.js, Python, AWS. Education editor fields were not separately re-read.
- [X] CT-03: Saved resume list shows a populated title and a valid created date for every entry.
  - Action: Open the saved resumes list and review each row.
  - Expected: Every row shows a non-blank title and a readable created date (for example, "Nov 9, 2026"), with no "undefined" or "null" text.
  - Note: After the reload, all three rows (Product Designer Resume, Marketing Manager Resume, Software Engineer Resume) had titles and readable dates, with no "undefined" or "null" text. During the CS-04 test, a blank title did appear in a row, so the title-validation defect also affects this item.

---

**Key findings**
1. **No persistence across reload (critical):** Every edit made in this session (new resume, duplicate, rename) was lost after a page reload. Only the three seeded resumes remained. This affects FT-02 and FT-08 and makes the save-related behavior unverifiable.
2. **No Save control and no validation feedback:** The editor has no "Save" button. None of the validation messages in the Constraint section appeared, and invalid values (blank name, "john@", reversed dates, blank title) were accepted.
3. **Missing features:** No template gallery or "Use Template" action (FT-01, CT-01), and no "Created" date filter (FT-10).

Test budget: about 100 tool calls were used, so the list was not re-run after the reload to re-verify FT-03 through FT-07.