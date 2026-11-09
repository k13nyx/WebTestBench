# Test Checklist

## Functionality
- [ ] FT-01: User can select a resource from the resource list.
  - Action: Open the reservation page and click one resource entry in the resource list.
  - Expected: The clicked resource becomes selected (highlighted/marked as chosen) and is used as the reservation's resource.

- [ ] FT-02: User can enter a date and time for the reservation.
  - Action: Interact with the date field and time field(s) in the reservation form.
  - Expected: The date and time fields accept input and display the chosen values.

- [ ] FT-03: User can enter a short purpose or title.
  - Action: Type "Quarterly planning" into the purpose/title field.
  - Expected: The field displays the entered text.

- [ ] FT-04: User can submit a valid reservation.
  - Action: Select a resource, choose a future date and time, enter a title, then click the submit button ("Reserve" / "Submit").
  - Expected: The reservation is created successfully and appears in the upcoming reservations list.

- [ ] FT-05: Upcoming reservations list shows the employee's reservations with full details.
  - Action: View the upcoming reservations list after submitting a reservation.
  - Expected: The list shows the reservation with its resource name, date, time, and title, matching the submitted values.

- [ ] FT-06: User can cancel an upcoming reservation.
  - Action: Click the cancel button/link on one entry in the upcoming reservations list.
  - Expected: The reservation is canceled and no longer appears in the upcoming reservations list.

- [ ] FT-07: Upcoming reservations list contains only future reservations.
  - Action: View the upcoming reservations list using the application's default data.
  - Expected: Every listed reservation has a date/time in the future; no past reservations are shown.

## Constraint
- [ ] CS-01: Reservation cannot be submitted without a selected resource.
  - Action: Leave the resource unselected, fill all other fields with valid values, click submit.
  - Expected: Submission is blocked and an error indicates a resource must be selected.

- [ ] CS-02: Reservation cannot be submitted with an empty purpose/title.
  - Action: Select a resource and valid date/time, leave the title field empty, click submit.
  - Expected: Submission is blocked and an error indicates the title is required.

- [ ] CS-03: Reservation cannot be submitted with a missing date or time.
  - Action: Select a resource and enter a title, leave date and/or time empty, click submit.
  - Expected: Submission is blocked and an error indicates date and time are required.

- [ ] CS-04: Reservation cannot be made in the past.
  - Action: Enter a date and time earlier than the current date/time, fill other fields validly, click submit.
  - Expected: Submission is blocked and an error indicates the date/time must be in the future.

- [ ] CS-05: End time must be after start time.
  - Action: Enter an end time equal to or earlier than the start time on the same date, click submit.
  - Expected: Submission is blocked and an error indicates the end time must be later than the start time.

- [ ] CS-06: A resource cannot be reserved for a time slot that is already taken.
  - Action: Select a resource and enter the exact date/time of an existing reservation for that resource (from the default upcoming reservations), then click submit.
  - Expected: Submission is blocked and an error indicates the resource is already reserved for that time.

## Interaction
- [ ] IX-01: A success confirmation is shown after a reservation is submitted.
  - Action: Submit a valid reservation (as in FT-04).
  - Expected: A visible success message/toast (e.g., "Reservation confirmed") is displayed.

- [ ] IX-02: A confirmation is shown after canceling a reservation.
  - Action: Cancel a reservation (as in FT-06).
  - Expected: A visible message/toast (e.g., "Reservation canceled") is displayed.

- [ ] IX-03: Validation errors are shown near the offending field.
  - Action: Click submit with an empty title field.
  - Expected: An error message appears at/under the title field (not only a generic page-level message).

- [ ] IX-04: The upcoming reservations list updates immediately after submit and cancel.
  - Action: Submit a new reservation, then cancel it, without reloading the page.
  - Expected: The list gains the new entry right after submit and removes it right after cancel, with no manual page refresh.

## Content
- [ ] CT-01: Resource list includes all three resource types.
  - Action: View the resource list.
  - Expected: The list contains meeting rooms, projectors, and shared workstations, each labeled with a clear name.

- [ ] CT-02: Reservation entries display accurate booking details.
  - Action: Compare each entry in the upcoming reservations list with the values entered when it was created.
  - Expected: Resource name, date, time, and title shown in each entry exactly match the submitted data.