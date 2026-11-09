# Test Checklist

## Functionality
- [ ] FT-01: Contact details can be entered and saved
  - Action: Open a resume, fill in the contact fields (name, email, phone, address/links) and click **Save Resume**.
  - Expected: All entered contact values are retained and re-displayed on the resume in both the editor and the preview.

- [ ] FT-02: A work experience entry can be added
  - Action: Click **Add Experience**, then enter job title, company, dates, and description.
  - Expected: The new entry appears as a separate, editable block in the Experience section of the editor and in the preview.

- [ ] FT-03: An education entry can be added
  - Action: Click **Add Education**, then enter institution, degree, and dates.
  - Expected: The new entry appears as a separate, editable block in the Education section of the editor and in the preview.

- [ ] FT-04: Skills can be added and removed
  - Action: Click **Add Skill**, type a skill name, confirm; then delete one skill entry.
  - Expected: Each added skill is listed in the Skills section, and the deleted skill disappears from both the editor list and the preview.

- [ ] FT-05: A template style can be selected and is applied
  - Action: In the **Templates** panel, click a template different from the one currently active, then open **Preview**.
  - Expected: The preview renders using the newly chosen template, and the previously active template is no longer applied.

- [ ] FT-06: Section order can be customized
  - Action: Reorder sections (e.g., move Education above Work Experience) using the section order/reorder control.
  - Expected: The sections are listed in the new order in the editor and rendered in that same order in the preview.

- [ ] FT-07: Section headings can be renamed
  - Action: Change a section heading (e.g., "Work Experience" to "Professional History") in the heading input.
  - Expected: The new heading text replaces the old one in the editor and is shown as the heading in the preview.

- [ ] FT-08: The resume can be previewed
  - Action: Click **Preview** after entering contact details, experience, education, and skills.
  - Expected: A preview of the resume is displayed showing all entered content with the selected template, section order, and custom headings applied.

- [ ] FT-09: A saved resume can be duplicated
  - Action: Select a saved resume and click **Duplicate**.
  - Expected: A second copy of that resume is created and shown as a separate item in the saved resume list.

- [ ] FT-10: A saved resume can be renamed
  - Action: Select a saved resume, click **Rename**, and enter a new title.
  - Expected: The saved list shows the new title for that resume, and the old title no longer appears.

- [ ] FT-11: Multiple resume variations can be saved
  - Action: Create and save a resume, duplicate it, rename the copy (e.g., "Marketing CV" and "Sales CV"), and make a different edit in each.
  - Expected: Both variations remain listed and each one opens with its own title and its own distinct content, unaffected by edits made to the other.

- [ ] FT-12: Saved resumes can be searched by title
  - Action: Type a keyword that matches the title of one saved resume into the search field.
  - Expected: Only the matching resume(s) are displayed in the saved list; non-matching resumes are hidden.

- [ ] FT-13: Saved resumes can be filtered by date created
  - Action: Use the **Date Created** filter to select a specific date range or sort order.
  - Expected: The saved list shows only the resumes created within that range, in the requested order.

## Constraint
- [ ] CS-01: A resume cannot be saved while required fields are empty
  - Action: Start a new resume, leave the name field empty, and click **Save Resume**.
  - Expected: Saving is blocked with a clear validation message identifying the missing required field(s), and no empty resume is added to the saved list.

- [ ] CS-02: Saved settings survive reload without corrupting state
  - Action: Save a resume with a specific template, custom section order, renamed headings, and entries; then reload the page and reopen that resume.
  - Expected: The template, section order, headings, and all entered content are identical to what was saved, and the duplicated copy still holds its own independent content.

## Interaction
- [ ] IX-01: Saving gives immediate confirmation
  - Action: Click **Save Resume** and observe the page without reloading.
  - Expected: A success confirmation (toast/message) appears within a second, and the saved resume is listed in the saved resume panel.

- [ ] IX-02: Search filters the saved list as the user types
  - Action: Click into the search field and type a title keyword character by character, then clear the field.
  - Expected: The list updates live with each character with no page reload, and clearing the field restores the full list.

- [ ] IX-03: Selecting a saved variation loads it into the editor and preview
  - Action: In the saved resume list, click a different saved variation than the one currently open.
  - Expected: The editor fields and the preview immediately switch to that variation's title, content, template, and section order.

## Content
- [ ] CT-01: Each template is visually distinct
  - Action: Select two different templates and compare their previews.
  - Expected: The two previews differ visibly in layout/styling (e.g., fonts, colors, header treatment, section arrangement) — they are not the same design with only a color change.

- [ ] CT-02: The preview contains only the user's own information
  - Action: Fill in contact details, one experience entry, one education entry, and one skill, then open **Preview**.
  - Expected: All text in the preview matches what was entered; no placeholder, "Lorem ipsum", "Your Name Here", or sample-data text remains.