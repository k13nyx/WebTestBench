# Test Result

## Functionality
- [X] FT-01: Resource list is visible and selectable
  - Action: Open the reservation page and locate the resource list.
  - Expected: Default office resources (meeting rooms, projectors, shared workstations) are listed and each entry can be clicked/selected.
- [X] FT-02: User can select a resource for reservation
  - Action: Click one default resource (e.g., a meeting room) in the list.
  - Expected: The resource is marked as selected and its name appears as the chosen resource in the reservation form.
- [X] FT-03: User can choose a reservation date
  - Action: Pick a future date using the date field/picker in the reservation form.
  - Expected: The selected date is shown in the date field.
- [X] FT-04: User can choose a reservation time
  - Action: Pick a time (start time, and end time if provided) in the reservation form.
  - Expected: The selected time is shown in the time field(s).
- [X] FT-05: User can provide a short purpose/title
  - Action: Type a short purpose (e.g., "Team sync") into the purpose/title field.
  - Expected: The typed text is displayed in the field.
- [X] FT-06: User can submit a reservation
  - Action: Fill resource, date, time, and title with valid values and click the submit button (e.g., "Reserve").
  - Expected: The reservation is created and appears in the upcoming reservations list with the entered details.
- [X] FT-07: Upcoming reservations list displays existing reservations
  - Action: View the upcoming reservations section.
  - Expected: Default upcoming reservations are listed, each showing resource name, date/time, and title.
- [X] FT-08: User can cancel a reservation
  - Action: Click the "Cancel" button on one upcoming reservation.
  - Expected: The reservation is removed from the upcoming reservations list (or clearly marked as cancelled) and is no longer bookable-blocked.

## Constraint
- [X] CS-01: Cannot submit a reservation with empty required fields
  - Action: Click the submit button with one or more required fields (resource, date, time, title) left empty.
  - Expected: No reservation is created; a validation message indicates which fields are required.
- [ ] CS-02: Cannot double-book the same resource at the same date/time
  - Action: Attempt to reserve the same resource for the same date and time as an existing reservation.
  - Expected: The reservation is rejected with a conflict/error message and is not added to the list.
  - Bug Report:
    - Issue: Missing booking conflict detection (double-booking allowed)
    - Actual: With an existing reservation ("Team sync", Skyline Conference Room, Nov 12, 2026, 14:00 – 15:30) in the list, submitting an identical reservation for the same resource on the same date with the same time slot (14:00 – 15:30) was ACCEPTED. A success toast "Reservation created! Skyline Conference Room booked for Nov 12, 2026" was shown and a second reservation ("Duplicate booking", Skyline Conference Room, Nov 12, 2026, 14:00 - 15:30) was added to the upcoming reservations list. No conflict/error message appeared and the reservation was not rejected.
- [ ] CS-03: Cannot reserve a resource for a past date/time
  - Action: Attempt to enter or submit a reservation with a past date/time.
  - Expected: Past date/time cannot be selected or the submission is rejected with an error; no reservation is created.
  - Bug Report:
    - Issue: Past time validation missing (past date/times can be booked)
    - Actual: Past dates are correctly blocked in the calendar (November 1–7, 2026 render as disabled, non-clickable gridcells), but a reservation for a fully past time on today's date was accepted: with the current time at 07:28 AM on Nov 8, 2026, submitting Skyline Conference Room for Nov 8, 2026, 06:00 – 07:00 succeeded with the toast "Reservation created! Skyline Conference Room booked for Nov 8, 2026", and the reservation "Past time attempt" (Nov 8, 2026, 06:00 - 07:00) was added to the list. No rejection error was shown.

## Interaction
- [X] IX-01: Success feedback is shown after creating a reservation
  - Action: Submit a valid reservation.
  - Expected: A success message/toast (e.g., "Reservation created") appears near the form or page top.
- [ ] IX-02: Feedback is shown after cancelling a reservation
  - Action: Cancel an upcoming reservation.
  - Expected: A confirmation prompt appears before cancelling and/or a message confirms the cancellation; the list updates without a full reload error state.
  - Bug Report:
    - Issue: Missing cancellation confirmation and feedback message
    - Actual: Clicking the cancel (X) button on a reservation card removes the reservation immediately and silently. No confirmation prompt/dialog appears before the cancellation, and no message/toast confirms the cancellation afterwards (verified twice: cancelling "Duplicate booking" and "Past time attempt" both produced no prompt and no notification). The list does update smoothly without a page reload or error state, but the expected confirmation prompt/feedback message never appears.
- [X] IX-03: Validation errors are displayed inline and form input is preserved
  - Action: Submit an invalid or conflicting reservation.
  - Expected: An error message appears near the relevant field/button, and previously entered values remain in the form.

## Content
- [X] CT-01: Resource list contains only relevant office resources
  - Action: Inspect every entry in the resource list.
  - Expected: All listed items are office resources (meeting rooms, projectors, shared workstations); no irrelevant or placeholder entries exist.
- [X] CT-02: Each reservation entry shows complete and accurate details
  - Action: Compare a newly created reservation's row against what was submitted.
  - Expected: Resource name, date, time, and purpose/title in the list exactly match the entered values.
- [X] CT-03: Page labels and headings match the reservation theme
  - Action: Read the page title, section headings, and field labels.
  - Expected: Texts clearly relate to office resource reservation (e.g., resource list, date/time, purpose, upcoming reservations); no unrelated or placeholder text is shown.
