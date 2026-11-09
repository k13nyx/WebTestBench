# Test Result

## Functionality
- [X] FT-01: User can select a resource from the resource list.
  - Action: Open the reservation page and click one resource entry in the resource list.
  - Expected: The clicked resource becomes selected (highlighted/marked as chosen) and is used as the reservation's resource.

- [X] FT-02: User can enter a date and time for the reservation.
  - Action: Interact with the date field and time field(s) in the reservation form.
  - Expected: The date and time fields accept input and display the chosen values.

- [X] FT-03: User can enter a short purpose or title.
  - Action: Type "Quarterly planning" into the purpose/title field.
  - Expected: The field displays the entered text.

- [X] FT-04: User can submit a valid reservation.
  - Action: Select a resource, choose a future date and time, enter a title, then click the submit button ("Reserve" / "Submit").
  - Expected: The reservation is created successfully and appears in the upcoming reservations list.

- [X] FT-05: Upcoming reservations list shows the employee's reservations with full details.
  - Action: View the upcoming reservations list after submitting a reservation.
  - Expected: The list shows the reservation with its resource name, date, time, and title, matching the submitted values.

- [X] FT-06: User can cancel an upcoming reservation.
  - Action: Click the cancel button/link on one entry in the upcoming reservations list.
  - Expected: The reservation is canceled and no longer appears in the upcoming reservations list.

- [ ] FT-07: Upcoming reservations list contains only future reservations.
  - Action: View the upcoming reservations list using the application's default data.
  - Expected: Every listed reservation has a date/time in the future; no past reservations are shown.
  - Bug Report:
    - Issue: Incorrect List Filtering / Missing Default Data
    - Actual: The application ships no default reservation data (the list shows the empty state "No upcoming reservations" at load; localStorage is empty), and the "Your Reservations" list does not restrict itself to future reservations: the past entry "CS04 test — Focus Pod A — Nov 8, 2026 00:00 - 00:30" (submitted at 17:54 on Nov 8, 2026) remained displayed in the upcoming reservations list, so a past reservation is shown.

## Constraint
- [ ] CS-01: Reservation cannot be submitted without a selected resource.
  - Action: Leave the resource unselected, fill all other fields with valid values, click submit.
  - Expected: Submission is blocked and an error indicates a resource must be selected.
  - Bug Report:
    - Issue: Unreachable Submission Path / Missing Error Message
    - Actual: With no resource selected the booking form is not rendered at all — the panel shows only "Select a Resource / Click on a resource card to start booking." There are no fields to fill and no submit button to click, so the prescribed action cannot be executed, and no error message indicating a resource must be selected is ever displayed. The constraint is enforced structurally without the required error feedback.

- [X] CS-02: Reservation cannot be submitted with an empty purpose/title.
  - Action: Select a resource and valid date/time, leave the title field empty, click submit.
  - Expected: Submission is blocked and an error indicates the title is required.

- [ ] CS-03: Reservation cannot be submitted with a missing date or time.
  - Action: Select a resource and enter a title, leave date and/or time empty, click submit.
  - Expected: Submission is blocked and an error indicates date and time are required.
  - Bug Report:
    - Issue: Incomplete/Incorrect Validation Messaging for Missing Fields
    - Actual: Submission is blocked, but no error indicates that date AND time are required. With date and both time fields empty, only the toast "Please select a date" appears (silent about the missing time). With only the time fields cleared (date set), the toast reads "End time must be after start time" — a misleading message; the app never indicates that the time fields are required.

- [ ] CS-04: Reservation cannot be made in the past.
  - Action: Enter a date and time earlier than the current date/time, fill other fields validly, click submit.
  - Expected: Submission is blocked and an error indicates the date/time must be in the future.
  - Bug Report:
    - Issue: Missing Past-Date/Time Validation (Incorrect Form Submission)
    - Actual: With date Nov 8, 2026 and time 00:00–00:30 (current time 17:54 on Nov 8, 2026), submission succeeded — toast "Reservation created! Focus Pod A booked for Nov 8, 2026" — and the past entry "CS04 test — Focus Pod A — Nov 8, 2026 00:00 - 00:30" was added to the list. No error about the date/time being in the past was shown. (Past calendar days are disabled in the picker, but past times on the current date are accepted unchecked.)

- [X] CS-05: End time must be after start time.
  - Action: Enter an end time equal to or earlier than the start time on the same date, click submit.
  - Expected: Submission is blocked and an error indicates the end time must be later than the start time.

- [ ] CS-06: A resource cannot be reserved for a time slot that is already taken.
  - Action: Select a resource and enter the exact date/time of an existing reservation for that resource (from the default upcoming reservations), then click submit.
  - Expected: Submission is blocked and an error indicates the resource is already reserved for that time.
  - Bug Report:
    - Issue: Missing Conflict Detection (Double Booking Allowed)
    - Actual: The application has no default reservations (list was empty at load), so the test used an earlier-created reservation (Skyline Conference Room, Nov 12, 2026, 14:30–15:30). Submitting the identical slot again succeeded with toast "Reservation created! Skyline Conference Room booked for Nov 12, 2026" and created a second entry "Team sync — Skyline Conference Room — Nov 12, 2026 14:30 - 15:30" alongside "Quarterly planning" at the exact same slot. No conflict error was shown.

## Interaction
- [X] IX-01: A success confirmation is shown after a reservation is submitted.
  - Action: Submit a valid reservation (as in FT-04).
  - Expected: A visible success message/toast (e.g., "Reservation confirmed") is displayed.

- [ ] IX-02: A confirmation is shown after canceling a reservation.
  - Action: Cancel a reservation (as in FT-06).
  - Expected: A visible message/toast (e.g., "Reservation canceled") is displayed.
  - Bug Report:
    - Issue: Missing Confirmation Message
    - Actual: After clicking the entry's cancel button the reservation is removed silently — no toast or message of any kind appears (no "Reservation canceled" confirmation). Only the entry disappearing from the list indicates the action occurred.

- [ ] IX-03: Validation errors are shown near the offending field.
  - Action: Click submit with an empty title field.
  - Expected: An error message appears at/under the title field (not only a generic page-level message).
  - Bug Report:
    - Issue: Validation Error Not Displayed Near Field
    - Actual: With an empty title the only feedback is the page-level toast "Please enter a title". The title field's container contains only its label and input (no error element), and the form panel shows no error text at/under the title field — the error is displayed only as a generic page-level toast.

- [X] IX-04: The upcoming reservations list updates immediately after submit and cancel.
  - Action: Submit a new reservation, then cancel it, without reloading the page.
  - Expected: The list gains the new entry right after submit and removes it right after cancel, with no manual page refresh.

## Content
- [X] CT-01: Resource list includes all three resource types.
  - Action: View the resource list.
  - Expected: The list contains meeting rooms, projectors, and shared workstations, each labeled with a clear name.

- [X] CT-02: Reservation entries display accurate booking details.
  - Action: Compare each entry in the upcoming reservations list with the values entered when it was created.
  - Expected: Resource name, date, time, and title shown in each entry exactly match the submitted data.
