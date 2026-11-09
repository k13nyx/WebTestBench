# Test Result

## Functionality

- [X] FT-01: Employee can view the available office resources.
  - Action: Open the reservation page and inspect the resource list.
  - Expected: The list displays selectable resources, including meeting rooms, projectors, and shared workstations.

- [X] FT-02: Employee can select a resource.
  - Action: Select one available resource from the resource list.
  - Expected: The selected resource is visibly identified as the active selection.

- [X] FT-03: Employee can choose a reservation date and time.
  - Action: Select a valid date and start/end time using the date and time controls.
  - Expected: The selected date and time remain displayed in the reservation form.

- [X] FT-04: Employee can enter a reservation purpose or title.
  - Action: Enter a short value in the “Purpose or title” field.
  - Expected: The entered text remains visible in the field and is included in the reservation submission.

- [X] FT-05: Employee can submit a valid reservation.
  - Action: Select a resource, choose a valid date and time, enter a purpose or title, and activate “Submit reservation.”
  - Expected: The reservation is created successfully and appears in the employee’s upcoming reservations.

- [X] FT-06: Employee can view upcoming reservations.
  - Action: Open or inspect the upcoming reservations list after a reservation exists.
  - Expected: Each upcoming reservation displays its resource, date, time, and purpose or title.

- [X] FT-07: Employee can cancel an upcoming reservation.
  - Action: Activate “Cancel” for an upcoming reservation and complete the cancellation action if prompted.
  - Expected: The selected reservation is removed from the upcoming reservations list.

## Constraint

- [X] CS-01: Reservation submission requires all required details.
  - Action: Leave the resource, date, time, or purpose/title field empty one at a time, then activate “Submit reservation.”
  - Expected: The reservation is not created, and the incomplete field is identified for correction.

- [X] CS-02: The system prevents invalid date or time selections.
  - Action: Attempt to submit a reservation with a past date, missing time, or an end time that is not later than the start time.
  - Expected: Submission is blocked and the invalid date or time is identified.

- [ ] CS-03: A resource cannot be reserved for an overlapping time.
  - Action: Using an existing upcoming reservation, attempt to reserve the same resource for an overlapping date and time.
  - Expected: The conflicting reservation is rejected and the employee is informed that the resource is unavailable for that period.
  - Bug Report:
    - Issue: Overlapping reservation accepted
    - Actual: A second reservation for Skyline Conference Room on Nov 14, 2026 from 09:30–09:45 was created even though an existing reservation for the same resource occupied 09:00–10:00. The interface displayed “Reservation created!” instead of rejecting the conflict.

- [X] CS-04: Canceling one reservation does not cancel another.
  - Action: With at least two upcoming reservations listed, cancel one reservation.
  - Expected: Only the selected reservation is removed; the other reservation remains unchanged.

## Interaction

- [X] IX-01: The form responds when a resource is selected.
  - Action: Select different resources from the resource list.
  - Expected: The active selection changes immediately, and only the chosen resource is associated with the form.

- [X] IX-02: Successful submission provides clear feedback.
  - Action: Submit a valid reservation.
  - Expected: The interface shows a clear confirmation that the reservation was created and updates the upcoming reservations list.

- [ ] IX-03: Cancellation provides clear feedback and updates the list.
  - Action: Cancel an upcoming reservation.
  - Expected: The interface confirms the cancellation and removes the canceled reservation from the list without requiring a page reload.
  - Bug Report:
    - Issue: Missing cancellation confirmation
    - Actual: The canceled reservation was removed from the list without a visible confirmation message or notification that the cancellation succeeded.

- [ ] IX-04: Validation feedback appears next to the relevant field.
  - Action: Submit the form with one or more invalid or missing values.
  - Expected: The form remains available for editing, and each invalid or missing value has visible, actionable feedback.
  - Bug Report:
    - Issue: Validation feedback is not associated with fields
    - Actual: Validation messages such as “Please select a date,” “Please enter a title,” and “End time must be after start time” appeared only as notifications at the top of the page rather than next to the relevant fields.

## Content

- [X] CT-01: Resource names and reservation details are relevant and accurate.
  - Action: Review the resource list and each displayed upcoming reservation.
  - Expected: Resource names are limited to office resources, and each reservation shows the correct resource, date, time, and purpose or title.

- [X] CT-02: Upcoming reservations are clearly distinguishable from other content.
  - Action: Inspect the page containing the reservation form and upcoming reservations list.
  - Expected: The heading or label for upcoming reservations clearly identifies the list, and each reservation’s details are readable without relying on ambiguous icons alone.
