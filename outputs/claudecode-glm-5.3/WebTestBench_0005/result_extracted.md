# Test Result

## Functionality

- [X] FT-01: User can create a new resume using a pre-designed template
  - Action: Click the "Create New Resume" (or equivalent) button and select any template from the template gallery.
  - Expected: A new resume is created and opens in the editor using the selected template, appearing in the list of saved resumes.
  - (Verified: Clicked "New Resume" → editor opened; selected "Classic" in the Template gallery → checkmark moved to Classic and the list badge showed "classic"; resume appeared in the saved list.)

- [ ] FT-02: User can enter contact details
  - Action: Open a resume in the editor, fill in contact fields (e.g., full name, email, phone), and save.
  - Expected: The entered contact details are stored and displayed in the resume (editor and preview) after saving and reloading.
  - Bug Report:
    - Issue: Data Loss on Reload / Missing Persistence Layer
    - Actual: Contact details (Alex Johnson, alex.johnson@email.com, (555) 987-6543, San Francisco, CA) displayed correctly in the editor and Live Preview, and survived editor→dashboard→editor navigation, but after a page reload the entire resume ("QA Engineer Resume") vanished from the list and all its data was lost. localStorage, sessionStorage, and cookies were all empty during the session and no backend/API requests were made (0 fetch/XHR entries in performance resource log) — there is no persistence mechanism, so nothing is "stored" beyond the in-memory session.

- [X] FT-03: User can add and edit work experience entries
  - Action: In the editor, add a work experience entry (job title, company, dates, description), save, then edit one field of that entry and save again.
  - Expected: The work experience entry appears in the resume with the entered values, and the edited change is persisted.
  - (Verified: Added "Senior QA Engineer" @ TechCorp Solutions, Mar 2021–Present with description; then edited job title to "Lead QA Engineer" — the preview updated and the edited value persisted after saving and reopening the resume from the dashboard.)

- [X] FT-04: User can add and edit education and skills entries
  - Action: Add an education entry (degree, institution, dates) and at least one skill; save the resume.
  - Expected: The education and skills sections display the added entries with correct values after saving.
  - (Verified: Education "University of California, Berkeley", "Bachelor of Science in Computer Science", Sep 2015 – May 2019, GPA 3.8 and skill "Automated Testing" (Intermediate) both displayed with correct values in the preview after saving and reopening.)

- [X] FT-05: User can choose/change the template style
  - Action: Open a resume in the editor and switch to a different template from the available template options.
  - Expected: The resume's visual style changes to the newly selected template while the entered content (contact, experience, education, skills) is preserved.
  - (Verified: Switched Classic → Minimal; DOM computed styles confirm the style change (name heading: `font-serif` 30px centered with `border-b-2` → `font-light` 24px left-aligned, no border) while all entered content remained intact in the preview.)

- [X] FT-06: User can reorder resume sections
  - Action: Use the section order control (e.g., drag handles or up/down buttons) to move one section (e.g., Skills above Work Experience) and save.
  - Expected: The sections appear in the newly specified order in the preview and after saving.
  - (Verified: Used the "↑" buttons on the Skills section twice; preview immediately showed Skills above Work Experience, and the new order persisted after saving and reopening the resume.)

- [X] FT-07: User can customize section headings
  - Action: Edit a section heading (e.g., change "Work Experience" to "Professional Experience") and save.
  - Expected: The custom heading replaces the default heading in the preview and persists after saving.
  - (Verified: Changed the "Work Experience" heading textbox to "Professional Experience"; the preview heading updated immediately and persisted after saving and reopening.)

- [X] FT-08: User can preview the resume
  - Action: Open the preview mode for a resume that contains entered data.
  - Expected: A full resume preview is displayed showing all sections (contact, work experience, education, skills) with the entered content and the applied template style.
  - (Verified: The "Live Preview" panel displays the full resume — contact header (name, email, phone, location, links), Professional Summary, Skills, Professional Experience, and Education — with all entered content in the applied template style; the "Hide Preview"/"Show Preview" toggle works.)

- [X] FT-09: User can duplicate a saved resume
  - Action: Use the "Duplicate" action on a saved resume (default data).
  - Expected: A copy of the resume is created (e.g., titled "Copy of [original title]") with identical content, and both the original and the copy appear in the saved resumes list.
  - (Verified: Card menu → Duplicate created "Product Designer Resume (Copy)"; opened both and confirmed identical content — Jordan Rivera contact info, same summary, both experience entries, same skills and education; both listed.)

- [X] FT-10: User can rename a saved resume
  - Action: Use the "Rename" action on a saved resume, enter a new title, and confirm.
  - Expected: The resume's title is updated in the saved resumes list, and its content is unchanged.
  - (Verified: Card menu → Rename opened a dialog; entered "Senior Product Designer Resume" and clicked Save — the list title updated and the resume's content was unchanged when reopened.)

- [X] FT-11: User can save multiple resume variations
  - Action: Duplicate an existing resume, modify its content (e.g., change the job title or summary), and save.
  - Expected: Both variations exist independently in the saved resumes list — the edit appears only in the duplicated version, not in the original.
  - (Verified: Modified the copy's first job title to "Senior Product Designer"; the copy shows the new title while the original still shows "Product Designer" — both variations exist independently in the list.)

- [X] FT-12: User can search saved resumes by title
  - Action: Type the exact title (or a distinctive part of a title) of an existing saved resume into the search box.
  - Expected: Only resumes whose titles match the search text are shown; non-matching resumes are hidden.
  - (Verified: Typing "Marketing" into the search box filtered the list to only "Marketing Manager Resume"; the other 3 resumes were hidden.)

- [ ] FT-13: User can filter saved resumes by date created
  - Action: Apply a date filter (e.g., "Last 7 days" or a specific date range) on the saved resumes list.
  - Expected: Only resumes whose creation dates fall within the selected filter are displayed; resumes outside the range are hidden.
  - Bug Report:
    - Issue: Missing Feature — No Date Filter Available
    - Actual: The saved-resumes list offers no date filtering. The only date-related control is a sort dropdown whose options are "Newest First", "Oldest First", "Title A-Z", "Title Z-A" — these only reorder the list; all resumes (e.g., the Nov 8, 2026 copy and the Jan/Feb 2024 samples) remain visible regardless of any selection. No "Last 7 days"/date-range option or any other date-filter UI exists on the page.

## Constraint

- [ ] CS-01: Cannot save a resume with a missing required title
  - Action: Attempt to save or create a resume while leaving the resume title field empty.
  - Expected: The save is blocked and a validation message (e.g., "Title is required") is shown; no untitled resume is added to the saved list.
  - Bug Report:
    - Issue: Missing Validation — Untitled Resume Silently Added to Saved List
    - Actual: Creating a resume via "New Resume" without entering a title is not blocked: the resume is auto-titled "Untitled Resume" and IS added to the saved resumes list (observed as a card "Untitled Resume, Updated Nov 8, 2026, modern"). Clearing the title textbox and pressing Enter silently reverts the title to "Untitled Resume" with no validation message ("Title is required" or similar never appears anywhere).

- [X] CS-02: Search with no matches returns an empty state, not the full list
  - Action: Enter a search query that does not match any saved resume title (e.g., "zzzzz").
  - Expected: No resumes are listed and a "no results" indicator is shown; the list does not display all resumes.
  - (Verified: Searching "zzzzz" replaced the list with an empty state: heading "No resumes found" and text "Try a different search term".)

- [X] CS-03: Reordering preserves all sections exactly once
  - Action: Reorder multiple sections, save the resume, and reopen it.
  - Expected: Every original section appears exactly once (none missing, none duplicated) and in the specified order.
  - (Verified: After moving Skills up twice, saving, and reopening, the Sections tab listed exactly Contact Information, Professional Summary, Skills, Professional Experience, Education — each appearing exactly once, none missing, none duplicated, in the specified order.)

## Interaction

- [X] IX-01: Preview updates in real time as content is edited
  - Action: With the preview visible, type a character into any resume field (e.g., change the name).
  - Expected: The preview immediately reflects the new value without requiring a page reload or manual refresh.
  - (Verified: Filling Full Name "Alex Johnson" and all contact fields instantly updated the Live Preview header (name, email, phone, location, links) with no reload; subsequent edits to job title, summary, headings, and section order were likewise reflected immediately.)

- [ ] IX-02: Save action shows a success confirmation
  - Action: Click the "Save" button after making a valid change.
  - Expected: A visible success indicator (e.g., toast/message "Resume saved") appears; no error is shown.
  - Bug Report:
    - Issue: Missing Save Control / No Save Feedback
    - Actual: The editor has no "Save" button at all — its only controls are the back button, the title button, the "Hide Preview" toggle, and the seven editor tabs; content changes are applied silently. The one existing "Save" button (in the Rename Resume dialog) was clicked after a valid change and produced no success indicator (the toast/notifications region stayed empty). No "Resume saved" message or any confirmation ever appears.

- [X] IX-03: Selecting a template immediately updates the resume appearance
  - Action: In the editor or template picker, click a different template thumbnail.
  - Expected: The resume/preview instantly re-renders in the selected style without needing to save first.
  - (Verified: Clicking the "Minimal" template card instantly moved the selection checkmark and re-rendered the Live Preview — DOM computed styles confirm the change from Classic (serif 30px centered, bordered header) to Minimal (light 24px left-aligned) with no save action involved.)

## Content

- [X] CT-01: All offered templates are professionally designed resume layouts
  - Action: Browse the full template gallery and inspect each template.
  - Expected: Every template is a legitimate resume layout (header, structured sections); no broken, blank, or non-resume designs appear.
  - (Verified: The gallery offers exactly 3 templates — "Modern" ("Clean design with accent colors and clear hierarchy"), "Classic" ("Traditional layout perfect for corporate roles"), "Minimal" ("Simple and elegant with focus on content"); each renders a proper resume layout with a header (name/contact) and structured sections, as observed in the Live Preview renders of all three.)

- [X] CT-02: Resume content matches entered data and the resume theme
  - Action: Open the preview of a resume with entered data and inspect all sections and labels.
  - Expected: All displayed text, labels, and values are relevant to a professional resume and exactly match the data entered in the editor; no placeholder/dummy text appears where the user entered real content.
  - (Verified: The preview of the entered resume exactly matched all editor inputs — "Alex Johnson", alex.johnson@email.com, (555) 987-6543, San Francisco, CA, linkedin/website links, summary text, "Lead QA Engineer" @ TechCorp Solutions (Mar 2021 – Present) with description, "University of California, Berkeley" / Bachelor of Science in Computer Science / GPA 3.8, and skill "Automated Testing", with the custom heading "Professional Experience" — no placeholder text appeared anywhere real content was entered.)
