# Test Checklist

## Functionality
- [ ] FT-01: Resource list is visible and selectable
  - Action: Open the reservation page and locate the resource list.
  - Expected: Default office resources (meeting rooms, projectors, shared workstations) are listed and each entry can be clicked/selected.
- [ ] FT-02: User can select a resource for reservation
  - Action: Click one default resource (e.g., a meeting room) in the list.
  - Expected: The resource is marked as selected and its name appears as the chosen resource in the reservation form.
- [ ] FT-03: User can choose a reservation date
  - Action: Pick a future date using the date field/picker in the reservation form.
  - Expected: The selected date is shown in the date field.
- [ ] FT-04: User can choose a reservation time
  - Action: Pick a time (start time, and end time if provided) in the reservation form.
  - Expected: The selected time is shown in the time field(s).
- [ ] FT-05: User can provide a short purpose/title
  - Action: Type a short purpose (e.g., "Team sync") into the purpose/title field.
  - Expected: The typed text is displayed in the field.
- [ ] FT-06: User can submit a reservation
  - Action: Fill resource, date, time, and title with valid values and click the submit button (e.g., "Reserve").
  - Expected: The reservation is created and appears in the upcoming reservations list with the entered details.
- [ ] FT-07: Upcoming reservations list displays existing reservations
  - Action: View the upcoming reservations section.
  - Expected: Default upcoming reservations are listed, each showing resource name, date/time, and title.
- [ ] FT-08: User can cancel a reservation
  - Action: Click the "Cancel" button on one upcoming reservation.
  - Expected: The reservation is removed from the upcoming reservations list (or clearly marked as cancelled) and is no longer bookable-blocked.

## Constraint
- [ ] CS-01: Cannot submit a reservation with empty required fields
  - Action: Click the submit button with one or more required fields (resource, date, time, title) left empty.
  - Expected: No reservation is created; a validation message indicates which fields are required.
- [ ] CS-02: Cannot double-book the same resource at the same date/time
  - Action: Attempt to reserve the same resource for the same date and time as an existing reservation.
  - Expected: The reservation is rejected with a conflict/error message and is not added to the list.
- [ ] CS-03: Cannot reserve a resource for a past date/time
  - Action: Attempt to enter or submit a reservation with a past date/time.
  - Expected: Past date/time cannot be selected or the submission is rejected with an error; no reservation is created.

## Interaction
- [ ] IX-01: Success feedback is shown after creating a reservation
  - Action: Submit a valid reservation.
  - Expected: A success message/toast (e.g., "Reservation created") appears near the form or page top.
- [ ] IX-02: Feedback is shown after cancelling a reservation
  - Action: Cancel an upcoming reservation.
  - Expected: A confirmation prompt appears before cancelling and/or a message confirms the cancellation; the list updates without a full reload error state.
- [ ] IX-03: Validation errors are displayed inline and form input is preserved
  - Action: Submit an invalid or conflicting reservation.
  - Expected: An error message appears near the relevant field/button, and previously entered values remain in the form.

## Content
- [ ] CT-01: Resource list contains only relevant office resources
  - Action: Inspect every entry in the resource list.
  - Expected: All listed items are office resources (meeting rooms, projectors, shared workstations); no irrelevant or placeholder entries exist.
- [ ] CT-02: Each reservation entry shows complete and accurate details
  - Action: Compare a newly created reservation's row against what was submitted.
  - Expected: Resource name, date, time, and purpose/title in the list exactly match the entered values.
- [ ] CT-03: Page labels and headings match the reservation theme
  - Action: Read the page title, section headings, and field labels.
  - Expected: Texts clearly relate to office resource reservation (e.g., resource list, date/time, purpose, upcoming reservations); no unrelated or placeholder text is shown.