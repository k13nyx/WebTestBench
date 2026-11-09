# Test Result

## Functionality
- [X] FT-01: User can enter contact details and see them on the resume
  - Action: Open a resume, fill contact fields (full name, email, phone) with valid values, and save.
  - Expected: The entered contact details are stored and displayed in the resume preview.
- [X] FT-02: User can add a work experience entry
  - Action: In the work experience section, add an entry with job title, company, and dates, then save.
  - Expected: The new work experience entry appears in the resume preview with all filled fields.
- [X] FT-03: User can add an education entry
  - Action: In the education section, add an entry with degree/school and dates, then save.
  - Expected: The education entry appears in the resume preview with all filled fields.
- [X] FT-04: User can add skills
  - Action: In the skills section, add at least one skill, then save.
  - Expected: The added skills appear listed in the resume preview.
- [X] FT-05: User can choose a template style
  - Action: Select a different pre-designed template from the template options.
  - Expected: The resume preview re-renders using the selected template's visual style, keeping the entered content.
- [X] FT-06: User can change section order
  - Action: Change the order of two sections (e.g., move Education above Work Experience).
  - Expected: The preview displays the sections in the newly configured order.
- [X] FT-07: User can rename a section heading
  - Action: Edit a section heading (e.g., change "Work Experience" to "Professional Experience") and save.
  - Expected: The preview displays the customized heading text in place of the default one.
- [X] FT-08: User can duplicate a resume version
  - Action: Use the duplicate action on an existing saved resume.
  - Expected: A new resume appears in the saved list as a copy, containing the same content as the source.
- [X] FT-09: User can rename a resume version
  - Action: Rename an existing resume to a new unique title and confirm.
  - Expected: The saved list shows the resume under its new title.
- [X] FT-10: User can save multiple resume variations
  - Action: Create/save at least two resumes with different titles and different content, then open each one.
  - Expected: Both resumes appear in the saved list, and opening each loads its own distinct content.
- [X] FT-11: User can search saved resumes by title
  - Action: Enter a title word that exists in one of the saved resumes into the search field.
  - Expected: The list is narrowed to resumes whose title contains the query text.
- [X] FT-12: User can filter saved resumes by date created
  - Action: Apply the date-created filter/sort option on the saved resumes list.
  - Expected: The list is filtered/ordered by creation date as selected.

## Constraint
- [X] CS-01: Editing one saved resume does not affect other saved resumes
  - Action: Open one saved resume, modify a field (e.g., change the phone number), save, then open a different saved resume.
  - Expected: The other resume's content is unchanged; only the edited resume contains the modification.
- [X] CS-02: Editing a duplicated copy leaves the original unchanged
  - Action: Duplicate a resume, edit a field in the duplicate, save it, then open the original.
  - Expected: The original resume still shows its pre-duplication content.
- [X] CS-03: A search with no matching title shows an empty state instead of unrelated resumes
  - Action: Enter a query in the title search that matches no saved resume (e.g., "zzzz").
  - Expected: The list shows an explicit no-results/empty state and no non-matching resumes are displayed.

## Interaction
- [X] IX-01: Preview reflects edits to the form
  - Action: Type a new value into a contact field (e.g., full name) and observe the preview.
  - Expected: The preview updates to display the newly entered value without reloading the page.
- [ ] IX-02: Saving a resume gives visible confirmation
  - Action: Make an edit and click the save action.
  - Expected: A visible success confirmation (e.g., "Saved" toast or status indicator) appears after saving.
  - Bug Report:
    - Issue: Missing Save Confirmation (no save action / silent auto-save)
    - Actual: No save button exists anywhere in the editor; edits auto-save silently. After editing contact fields, 5 polls over 1.25s found no toast/status element (notifications region empty), Ctrl+S produced nothing, and the rename dialog's "Save" click also produced no confirmation toast. Only the list's "Updated" date changes, which is not visible in the editor at save time.
- [X] IX-03: The currently selected template is visually indicated
  - Action: Open the template chooser.
  - Expected: The active template is clearly highlighted/marked as selected, distinct from the other templates.

## Content
- [X] CT-01: Switching templates does not lose or replace entered content with placeholder text
  - Action: With data already entered, switch between pre-designed templates.
  - Expected: Every template displays the user's actual entered content; no lorem-ipsum/placeholder text appears in place of user data.
- [X] CT-02: Saved resumes list shows accurate titles and creation dates
  - Action: Inspect the saved resumes list (default data plus any saved resumes).
  - Expected: Each entry displays a relevant resume title and a creation date matching that resume's actual data.
