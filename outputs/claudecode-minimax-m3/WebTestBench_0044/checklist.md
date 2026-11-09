# Test Checklist

## Functionality
- [ ] FT-01: User can add a new job application with company, role, date, status, and notes.
  - Action: Click "Add Application" (or equivalent), fill in Company, Role, Date, Status, and Notes fields, then save.
  - Expected: The new application appears in the list with all entered details displayed correctly.

- [ ] FT-02: User can edit an existing job application entry.
  - Action: Click the edit button on an existing application, modify Company/Role/Date/Status/Notes, then save.
  - Expected: The updated entry reflects the new values in the list.

- [ ] FT-03: User can delete an existing job application entry.
  - Action: Click the delete button on an existing application and confirm deletion.
  - Expected: The application is removed from the list and no longer visible.

- [ ] FT-04: User can mark/change an application status to one of the predefined values.
  - Action: Change the status of an existing application to "Applied", "Interviewed", or "Offered".
  - Expected: The status of that application is updated and displayed accordingly in the list.

- [ ] FT-05: User can add or update brief notes for an application.
  - Action: Enter text in the Notes field when creating or editing an application, then save.
  - Expected: The note text is saved and displayed alongside the application entry.

- [ ] FT-06: User can view the complete list of logged job applications.
  - Action: Navigate to the main page of the application.
  - Expected: All previously added applications are visible in a list format with their Company, Role, Date, Status, and Notes shown.

## Constraint
- [ ] CS-01: Application cannot be saved without required fields (Company, Role, Date).
  - Action: Attempt to save a new application with Company, Role, or Date left blank.
  - Expected: Save action is blocked and an error/validation message indicates which required fields are missing.

- [ ] CS-02: Status field is restricted to the predefined values: Applied, Interviewed, Offered.
  - Action: Open the status selector (dropdown/radio) when creating or editing an application.
  - Expected: Only "Applied", "Interviewed", and "Offered" options are available; no other values can be selected or entered.

- [ ] CS-03: Deleted application cannot be recovered unless undo functionality is provided.
  - Action: Delete an application, then refresh or revisit the page.
  - Expected: The deleted application does not reappear in the list (unless an explicit undo option is offered before page exit).

## Interaction
- [ ] IX-01: Visual feedback is shown after adding a new application.
  - Action: Successfully save a new application.
  - Expected: A confirmation message/toast appears confirming the application was added, and the new entry becomes visible without manual refresh.

- [ ] IX-02: Visual feedback is shown after editing an application.
  - Action: Successfully save edits to an existing application.
  - Expected: A confirmation message/toast appears confirming the update, and the list reflects the changes without manual refresh.

- [ ] IX-03: Visual feedback is shown after deleting an application.
  - Action: Successfully delete an application.
  - Expected: A confirmation message/toast appears confirming the deletion, and the entry disappears from the list.

- [ ] IX-04: Status change is immediately reflected in the application list view.
  - Action: Change the status of an application and observe the list.
  - Expected: The list entry's status indicator updates instantly without requiring a page reload.

## Content
- [ ] CT-01: Default sample applications (if present) are relevant to the job application tracking theme.
  - Action: Load the application on first visit with default data.
  - Expected: Any pre-existing entries contain realistic Company, Role, Date, Status, and Notes data appropriate to job applications (not random/unrelated content).

- [ ] CT-02: All status labels displayed match the defined values (Applied, Interviewed, Offered).
  - Action: Review all entries in the list and any status filters/legends.
  - Expected: Status labels read exactly "Applied", "Interviewed", and/or "Offered" with consistent capitalization.

- [ ] CT-03: Field labels and form instructions are clearly worded and relevant.
  - Action: Read the form labels and helper text on the Add/Edit application form.
  - Expected: Labels such as "Company", "Role", "Date", "Status", and "Notes" are clearly displayed and self-explanatory.