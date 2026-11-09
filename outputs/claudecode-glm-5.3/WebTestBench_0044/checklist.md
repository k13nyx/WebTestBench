# Test Checklist

## Functionality
- [ ] FT-01: User can view the personal list of job applications
  - Action: Open the website's main page
  - Expected: The list displays the pre-existing default entries, each showing company, role, date, and status

- [ ] FT-02: User can add a new application entry
  - Action: Fill in the company, role, and date fields and click the add/save button
  - Expected: A new entry is created and visible in the list with the entered company, role, and date

- [ ] FT-03: User can edit an existing entry
  - Action: Click the edit control on a default entry, change the role (e.g., to "Senior Engineer"), and save
  - Expected: The entry shows the updated role value in the list

- [ ] FT-04: User can delete an entry
  - Action: Click the delete control on a default entry and confirm deletion
  - Expected: The entry is removed from the list

- [ ] FT-05: User can mark an entry with a status
  - Action: Change a default entry's status (e.g., to "Offered")
  - Expected: The entry displays the selected status value

- [ ] FT-06: User can save a brief note on an entry
  - Action: Type a short note (e.g., "Recruiter said 2-week turnaround") into an entry's notes field and save
  - Expected: The note is stored and displayed with that entry

- [ ] FT-07: Entries persist after page reload
  - Action: Reload the page after adding/editing an entry
  - Expected: All entries and their details are still present in the list unchanged

## Constraint
- [ ] CS-01: Cannot create an entry with empty required fields
  - Action: Leave the company, role, or date field empty and attempt to save
  - Expected: No entry is created; a validation message or blocked save identifies the missing required field(s)

- [ ] CS-02: Status accepts only the three defined values
  - Action: Open the status selector on any entry and review available options
  - Expected: Only "Applied", "Interviewed", and "Offered" are selectable; no other status values can be entered or chosen

## Interaction
- [ ] IX-01: List updates immediately after user actions
  - Action: Add an entry, then edit and delete it, observing the list after each action
  - Expected: The list reflects each change immediately without requiring a manual page reload

- [ ] IX-02: Edit view pre-fills the entry's current values
  - Action: Click the edit control on a default entry
  - Expected: The edit form opens with that entry's existing company, role, date, status, and note already filled in

## Content
- [ ] CT-01: Displayed entry data matches the saved data
  - Action: Compare each list entry's displayed company, role, date, status, and notes against the values saved for that entry
  - Expected: All displayed text matches exactly, with no truncated notes or mismatched values

- [ ] CT-02: Page content is relevant to job application tracking
  - Action: Inspect the page title, headings, field labels (e.g., "Company", "Role", "Date", "Status", "Notes"), and button texts
  - Expected: All visible text and controls relate to logging job applications, with no unrelated or placeholder content