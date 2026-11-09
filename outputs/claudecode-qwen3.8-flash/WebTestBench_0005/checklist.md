# Test Checklist

## Functionality
- [ ] FT-01: User can create a new resume from a pre-designed template
  - Action: Click "New Resume" (or equivalent), select a template from the offered styles, and confirm.
  - Expected: A new blank resume based on the chosen template opens in the editor.

- [ ] FT-02: User can enter and save contact details
  - Action: Fill the contact fields (name, email, phone, location) on the default resume and click "Save".
  - Expected: All contact values are retained and displayed in the resume document after saving.

- [ ] FT-03: User can add entries for work experience, education, and skills
  - Action: Use the "Add" controls to create one work experience entry (role, company, dates, description), one education entry (degree, school, dates), and add at least two skills.
  - Expected: Each entry is accepted and appears under its respective section in the resume.

- [ ] FT-04: User can edit an existing entry
  - Action: Open a default entry (e.g., an existing work experience item), change the job title text, and save.
  - Expected: The edited text is shown in the resume; old value no longer appears.

- [ ] FT-05: User can switch the resume to a different template style
  - Action: From the template picker, select a second template for an existing resume containing data.
  - Expected: The resume re-renders in the new template style with all previously entered data intact.

- [ ] FT-06: User can customize layout options (section order and headings)
  - Action: Move the "Skills" section above "Education" using the reorder control, and rename the heading "Work Experience" to "Professional Experience".
  - Expected: Sections display in the new order and the renamed heading appears in the resume.

- [ ] FT-07: User can preview the resume
  - Action: Click the "Preview" button/toggle while editing the default resume.
  - Expected: A formatted full resume view (as the template would output) is shown with all sections and entered data.

- [ ] FT-08: User can rename a saved resume version
  - Action: From the saved-resume list, use "Rename" on the default resume, set the title to "Marketing Resume", and confirm.
  - Expected: The list and editor header show "Marketing Resume"; other resumes are unaffected.

- [ ] FT-09: User can duplicate a saved resume version
  - Action: Click "Duplicate" on a saved resume.
  - Expected: A new copy (e.g., titled "Copy of …") appears in the saved list containing identical content.

- [ ] FT-10: User can save multiple variations for different applications
  - Action: Create/duplicate two resumes, give each distinct content, and save both; then save again after a further edit to one of them.
  - Expected: Both variations appear independently in the saved list; the latest edit persists on reload.

- [ ] FT-11: User can search saved resumes by title
  - Action: Type a keyword matching one saved resume's title (e.g., "Marketing") into the search box; then clear it.
  - Expected: Only resumes whose titles contain the keyword are listed; clearing restores the full list.

- [ ] FT-12: User can filter/sort saved resumes by date created
  - Action: Apply the "Date Created" filter/sort control in the saved-resume list.
  - Expected: Resumes are limited/reordered strictly by creation date (newest or oldest first, per the selected option).

## Constraint
- [ ] CS-01: Cannot save a resume with empty required fields
  - Action: Clear the resume title (and a required contact field such as name) and click "Save".
  - Expected: Save is blocked and a visible validation message identifies the missing field(s); no partial/blank-titled entry is created.

- [ ] CS-02: Duplicate is independent of the original
  - Action: Duplicate a resume, then edit the duplicate (change its name field) and save.
  - Expected: The original resume's content and title remain exactly unchanged.

- [ ] CS-03: Customization state persists across sessions
  - Action: Apply a section reorder and heading rename (FT-06), save, then reload the page and reopen that resume.
  - Expected: The custom section order and heading are still applied (state invariant holds after reload).

## Interaction
- [ ] IX-01: Template selection gives immediate visual feedback
  - Action: Hover over and click a different template in the template picker.
  - Expected: The selected template is visibly highlighted (selected state), and the preview updates to reflect it without a page reload.

- [ ] IX-02: Success feedback after save, duplicate, and rename
  - Action: Perform each of: save an edit, duplicate a resume, rename a resume.
  - Expected: Each action produces a clear confirmation (toast/message such as "Saved"/"Duplicated") and the list updates automatically.

- [ ] IX-03: Reorder control responds immediately to user action
  - Action: Drag a section (or use the up/down reorder control) in the layout options panel.
  - Expected: The section list visibly moves to the new position during/immediately after the action, with no page reload required.

## Content
- [ ] CT-01: Template gallery shows multiple relevant professional templates
  - Action: Open the template selection area.
  - Expected: At least two pre-designed resume templates are listed, each with a distinct name and a representative preview/thumbnail appropriate for professional resumes (no broken images or placeholder gibberish).

- [ ] CT-02: Default saved resumes display complete, accurate metadata
  - Action: Open the saved-resume library and inspect the pre-existing (default) resume entries.
  - Expected: Each entry card shows a title, creation date, and template/section summary that match the content opened when selecting that resume; no empty or contradictory fields.