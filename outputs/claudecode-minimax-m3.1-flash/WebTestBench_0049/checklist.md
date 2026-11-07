# Test Checklist

## Functionality
- [ ] **FT-01**: Resource list is displayed on page load
  - Action: Open the reservation webpage.
  - Expected: A list of available resources (meeting rooms, projectors, shared workstations) is visible, each with a name/type, and the page shows a form to create a reservation.

- [ ] **FT-02**: Select a resource from the list
  - Action: Click one resource entry in the list (e.g., a meeting room).
  - Expected: The selected resource becomes visibly highlighted/selected and its name appears in the reservation form's resource field.

- [ ] **FT-03**: Choose a reservation date
  - Action: Fill the date field with a valid future date (e.g., a date from the default dataset).
  - Expected: The date is accepted and displayed in the form field without error.

- [ ] **FT-04**: Choose a start and end time
  - Action: Fill the start time and end time fields with a valid time range (e.g., 10:00–11:00).
  - Expected: Both times are accepted and shown in the form; no validation error appears.

- [ ] **FT-05**: Enter a purpose/title
  - Action: Type a short purpose (e.g., "Weekly team sync") into the purpose/title field.
  - Expected: The text appears in the field and is retained.

- [ ] **FT-06**: Submit a valid reservation
  - Action: With resource, date, times, and purpose all filled, click the submit/reserve button.
  - Expected: The reservation is created and a success confirmation (message or new list entry) is shown.

- [ ] **FT-07**: Submitted reservation appears in the upcoming reservations list
  - Action: After a successful submit, view the reservations list section.
  - Expected: A new entry shows the resource name, date, time, and purpose of the reservation just created.

- [ ] **FT-08**: Cancel a reservation
  - Action: Click the cancel button on one reservation in the upcoming list, then confirm.
  - Expected: The reservation is removed from the list and a cancellation confirmation is shown.

- [ ] **FT-09**: Reservation list shows each entry's key details
  - Action: Inspect the entries in the upcoming reservations list.
  - Expected: Each entry displays at least the resource name, reservation date, time range, and purpose/title.

## Constraint
- [ ] **CS-01**: Cannot submit without a selected resource
  - Action: Leave the resource unselected, fill date, time, and purpose, click submit.
  - Expected: Submission is rejected with a visible validation message and no reservation is created.

- [ ] **CS-02**: Cannot submit without a date
  - Action: Select a resource and time, clear the date field, click submit.
  - Expected: Submission is rejected with a visible validation message and no reservation is created.

- [ ] **CS-03**: Cannot submit without a start/end time
  - Action: Select a resource and date, fill purpose, leave time fields empty, click submit.
  - Expected: Submission is rejected with a visible validation message and no reservation is created.

- [ ] **CS-04**: Cannot submit without a purpose/title
  - Action: Select a resource, date, and time, leave the purpose field empty, click submit.
  - Expected: Submission is rejected with a visible validation message and no reservation is created.

- [ ] **CS-05**: End time must be after start time
  - Action: Enter a start time of 14:00 and an end time of 13:00, then submit.
  - Expected: Submission is rejected with a validation message stating the time range is invalid; no reservation is created.

- [ ] **CS-06**: No duplicate booking for the same resource and overlapping time
  - Action: Reserve resource A for a date/time slot, then attempt to reserve the same resource A for an overlapping time.
  - Expected: The second attempt is rejected with a conflict message and the original reservation remains unchanged.

- [ ] **CS-07**: Cancelled reservation frees the resource slot
  - Action: Cancel an existing reservation, then try to book the same resource for the same date/time.
  - Expected: The new reservation is accepted successfully.

## Interaction
- [ ] **IX-01**: Success feedback shown after reservation submission
  - Action: Submit a complete, valid reservation form.
  - Expected: A visible success message/toast appears (and the form resets or the new entry is highlighted) without a page error.

- [ ] **IX-02**: Confirmation feedback shown after cancellation
  - Action: Click cancel on a reservation entry.
  - Expected: A visible confirmation message indicates the reservation was cancelled (and disappears or the entry is removed from the list).

- [ ] **IX-03**: Selected resource is visually distinguished
  - Action: Click different entries in the resource list in turn.
  - Expected: Exactly one entry appears active/selected at a time, and it matches the resource shown in the form.

- [ ] **IX-04**: Cancel asks for confirmation before deleting
  - Action: Click the cancel button on a reservation and observe the response.
  - Expected: A confirmation prompt (dialog or explicit confirm control) is shown, and the reservation is only removed after confirming; dismissing keeps the reservation.

- [ ] **IX-05**: Invalid submission gives actionable feedback and preserves input
  - Action: Submit the form with an empty required field, then fill the missing field and resubmit.
  - Expected: The error message is displayed next to/indicating the invalid field, the entered values remain in the form, and a corrected submission succeeds.

## Content
- [ ] **CT-01**: Resource list shows all three required resource types
  - Action: View the resource list.
  - Expected: Entries for meeting rooms, projectors, and shared workstations are present, each labeled with a distinct, meaningful name.

- [ ] **CT-02**: Reservation list content matches the created reservation
  - Action: Create a reservation with distinctive purpose text (e.g., "Q3 Budget Review") and check the list entry.
  - Expected: The list entry shows the same resource name, date, time, and the exact purpose text "Q3 Budget Review" — no truncation, placeholder, or unrelated content.

- [ ] **CT-03**: Empty state message shown when there are no reservations
  - Action: Cancel all reservations so the list is empty, or load the page in a state with no reservations.
  - Expected: A clear message such as "No upcoming reservations" is displayed instead of a blank area or raw error text.

- [ ] **CT-04**: All visible text is relevant to office resource reservation
  - Action: Read all headings, labels, button text, and messages on the page.
  - Expected: Every label and button is meaningful for the reservation task (resource, date, time, purpose, submit, cancel); no placeholder, lorem ipsum, or unrelated marketing text appears.