# Test Checklist

## Functionality
- [ ] FT-01: Create a new resume using a pre-designed template
  - Action: Click "Create New Resume", select a template style (e.g., "Modern") from the gallery, and click "Use Template".
  - Expected: The resume editor opens with the layout and formatting of the selected "Modern" template.
- [ ] FT-02: Enter and save core resume information
  - Action: Fill in valid text for "Contact Details", "Work Experience", "Education", and "Skills" sections, then click "Save".
  - Expected: All entered information is saved and reflected in the resume draft.
- [ ] FT-03: Reorder resume sections
  - Action: Use the reorder control to move the "Skills" section above the "Work Experience" section.
  - Expected: The "Skills" section is positioned above "Work Experience" in the editor and resume output.
- [ ] FT-04: Customize section headings
  - Action: Edit the default heading text "Work Experience" to "Professional Experience" and save.
  - Expected: The section heading displays "Professional Experience" in both the editor and preview.
- [ ] FT-05: Preview resume
  - Action: Click the "Preview" button in the resume editor.
  - Expected: A full-page preview opens displaying the formatted resume with all populated sections.
- [ ] FT-06: Duplicate an existing resume
  - Action: Click the "Duplicate" button on a saved resume in the dashboard.
  - Expected: A new copy of the resume appears in the saved resumes list with "Copy" appended to its title.
- [ ] FT-07: Rename a saved resume
  - Action: Click "Rename" on a saved resume, enter "Senior Developer Resume", and click "Confirm".
  - Expected: The resume title updates to "Senior Developer Resume" across the dashboard.
- [ ] FT-08: Save multiple resume variations
  - Action: Modify an existing resume's content, click "Save As Variation", and enter "Marketing Specialist Variant".
  - Expected: A new separate resume entry titled "Marketing Specialist Variant" is created without overwriting the original.
- [ ] FT-09: Search saved resumes by title
  - Action: Type an existing resume title (e.g., "Software Engineer") into the search input.
  - Expected: The resume list updates to display only resumes matching "Software Engineer".
- [ ] FT-10: Filter saved resumes by creation date
  - Action: Select a specific date range from the "Date Created" filter dropdown.
  - Expected: The resume list updates to show only resumes created within the specified date range.

## Constraint
- [ ] CS-01: Prevent saving resume with an empty title
  - Action: Clear the resume title field in the editor and click "Save".
  - Expected: The save action is blocked and an error message "Resume title is required" is displayed.
- [ ] CS-02: Validate email address format in contact details
  - Action: Enter "invalid-email-string" into the Email field and click "Save".
  - Expected: The form highlights the Email input and displays "Please enter a valid email address".
- [ ] CS-03: Empty search state display
  - Action: Enter a non-existent title query (e.g., "XYZ123NonExistent") into the search bar.
  - Expected: The list displays zero resumes along with a "No resumes found" message.

## Interaction
- [ ] IX-01: Real-time preview update during content editing
  - Action: Type text into the "Full Name" input field while viewing the split preview pane.
  - Expected: The preview pane dynamically renders the typed characters simultaneously without requiring a page reload.
- [ ] IX-02: Visual drag-and-drop indicator during section reordering
  - Action: Click and drag a section handle to reposition it within the layout.
  - Expected: A highlighted placeholder line indicates the new drop placement while dragging.
- [ ] IX-03: Confirmation notification on successful save
  - Action: Click the "Save" button after editing resume details.
  - Expected: A temporary toast notification stating "Resume saved successfully" appears in the corner.

## Content
- [ ] CT-01: Template gallery options and structure
  - Action: Open the template selection menu.
  - Expected: Displays selectable pre-designed template cards with preview thumbnails, template names, and professional formatting.
- [ ] CT-02: Saved resume card metadata display
  - Action: Navigate to the saved resumes dashboard.
  - Expected: Each resume card clearly displays its title, date created, associated template name, and thumbnail preview.