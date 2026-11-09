# Test Checklist

## Functionality

- [ ] **FT-01: Create a resume from a pre-designed template**
  - **Action:** Select **“Create Resume”**, choose any available template, and open the resume editor.
  - **Expected:** A new editable resume opens using the selected template style.

- [ ] **FT-02: Enter and save contact details**
  - **Action:** Enter a name, email address, phone number, location, and professional link in the **Contact Details** section, then select **“Save.”**
  - **Expected:** All entered contact details are displayed in the resume and remain after reopening it.

- [ ] **FT-03: Add and organize work experience**
  - **Action:** Add a work experience entry with an employer, job title, dates, and description; add a second entry and reorder the entries.
  - **Expected:** Both entries appear with their entered information in the selected order.

- [ ] **FT-04: Add education and skills**
  - **Action:** Enter at least one education record and multiple skills in their respective sections, then save the resume.
  - **Expected:** The education record and all skills appear in the resume and remain after reopening it.

- [ ] **FT-05: Edit existing resume information**
  - **Action:** Open a default saved resume, change an existing field, and select **“Save.”**
  - **Expected:** The updated value replaces the previous value in both the editor and resume preview.

- [ ] **FT-06: Select a different template style**
  - **Action:** Open **“Templates”**, select a different pre-designed template, and apply it to the current resume.
  - **Expected:** The resume uses the newly selected template without losing entered information.

- [ ] **FT-07: Customize section order and headings**
  - **Action:** Move a resume section to a different position and change a section heading, then save.
  - **Expected:** The section appears in the new position with the customized heading in the editor and preview.

- [ ] **FT-08: Preview the resume**
  - **Action:** Select **“Preview.”**
  - **Expected:** A preview displays the resume with the current content, template, section order, and headings.

- [ ] **FT-09: Save multiple resume variations**
  - **Action:** Save the current resume, duplicate it, make a different template or content change in the duplicate, and save both versions.
  - **Expected:** Both variations remain available as separate saved resumes with their respective changes.

- [ ] **FT-10: Duplicate a saved resume**
  - **Action:** Open the actions menu for a saved resume and select **“Duplicate.”**
  - **Expected:** A separate copy is created containing the original resume’s content and formatting.

- [ ] **FT-11: Rename a saved resume**
  - **Action:** Open the actions menu for a saved resume, select **“Rename,”** enter a new title, and confirm.
  - **Expected:** The new title appears in the saved-resume list and identifies the same resume version.

- [ ] **FT-12: Search saved resumes by title**
  - **Action:** Enter a distinctive saved-resume title into the **“Search resumes”** field.
  - **Expected:** Only saved resumes whose titles match the search text remain visible.

- [ ] **FT-13: Filter saved resumes by creation date**
  - **Action:** Use the **“Date created”** filter to select an available date or date range.
  - **Expected:** The list displays only resumes created within the selected date or date range.

## Constraint

- [ ] **CS-01: Prevent saving a resume without required information**
  - **Action:** Open the resume editor, leave required fields empty, and select **“Save.”**
  - **Expected:** The resume is not saved, and each missing required field is identified with a validation message.

- [ ] **CS-02: Keep duplicated resumes independent**
  - **Action:** Duplicate a saved resume, edit the duplicate’s contact details or work experience, and save it.
  - **Expected:** The original resume retains its previous information and the duplicate contains only its own changes.

- [ ] **CS-03: Preserve resume data when changing templates**
  - **Action:** Change the template on a resume containing contact details, work experience, education, and skills.
  - **Expected:** All existing resume information remains present after the template change.

- [ ] **CS-04: Prevent contradictory saved-resume titles**
  - **Action:** Rename a saved resume to an existing saved-resume title and confirm the rename.
  - **Expected:** The application either prevents the duplicate title or clearly requires confirmation before creating an indistinguishable saved version.

## Interaction

- [ ] **IX-01: Show save feedback**
  - **Action:** Edit a resume and select **“Save.”**
  - **Expected:** A visible success indication appears, and the saved-resume state updates without requiring a page refresh.

- [ ] **IX-02: Update preview after editor changes**
  - **Action:** Change a resume field, section order, heading, or template while preview is available.
  - **Expected:** The preview updates to reflect the latest change.

- [ ] **IX-03: Update search results as the query changes**
  - **Action:** Type, modify, and clear text in **“Search resumes.”**
  - **Expected:** Matching results update after each query change, and clearing the field restores the full saved-resume list.

## Content

- [ ] **CT-01: Display entered information accurately**
  - **Action:** Compare the editor values for contact details, work experience, education, and skills with the resume preview.
  - **Expected:** The preview displays the same values without missing, altered, or unrelated content.

- [ ] **CT-02: Display relevant template content and labels**
  - **Action:** Review each available template preview and the applied resume template.
  - **Expected:** Template labels, section headings, icons, and sample content are relevant to professional resume creation.

- [ ] **CT-03: Display complete saved-resume metadata**
  - **Action:** Review every saved resume in the list.
  - **Expected:** Each saved resume displays its title and a usable creation date that can be used by the date filter.