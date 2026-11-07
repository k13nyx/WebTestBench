# Test Checklist

## Functionality
- [ ] FT-01: User can view a list of available office resources
  - Action: Open the reservation webpage.
  - Expected: A list is displayed containing meeting rooms, projectors, and shared workstations.

- [ ] FT-02: User can select a resource from the list
  - Action: Click on a resource (e.g., a meeting room).
  - Expected: The resource is selected/highlighted as the reservation target.

- [ ] FT-03: User can choose a date for the reservation
  - Action: Select a date using the date picker.
  - Expected: The chosen date is recorded and shown in the form.

- [ ] FT-04: User can choose a time for the reservation
  - Action: Select a time or time slot.
  - Expected: The chosen time is recorded and shown in the form.

- [ ] FT-05: User can provide a short purpose/title
  - Action: Type text into the purpose/title field.
  - Expected: The entered text appears in the field.

- [ ] FT-06: User can submit the reservation
  - Action: Click the "Submit" / "Reserve" button with all fields filled.
  - Expected: The reservation is created and accepted by the system.

- [ ] FT-07: User can view their upcoming reservations
  - Action: Open or navigate to the upcoming reservations section.
  - Expected: A list of the user's upcoming reservations is displayed.

- [ ] FT-08: User can cancel an upcoming reservation
  - Action: Click "Cancel" on an upcoming reservation.
  - Expected: The reservation is removed from the list.

## Constraint
- [ ] CS-01: Cannot submit a reservation with empty required fields
  - Action: Click "Submit" leaving resource, date, time, or purpose empty.
  - Expected: Submission is blocked and an error indicates the missing required field(s).

- [ ] CS-02: Cannot reserve a resource already booked for the same date/time
  - Action: Submit a reservation for a resource occupied at the same date/time.
  - Expected: Submission is rejected with a conflict message (e.g., "Resource already booked").

## Interaction
- [ ] IX-01: Success confirmation appears after submitting a reservation
  - Action: Submit a valid reservation.
  - Expected: A success toast/message confirms the reservation was created.

- [ ] IX-02: New reservation appears in the upcoming list immediately
  - Action: Submit a valid reservation, then view upcoming reservations.
  - Expected: The new reservation is present in the list.

- [ ] IX-03: Cancelled reservation is removed from the list
  - Action: Cancel a reservation, then view the list.
  - Expected: The cancelled reservation no longer appears.

## Content
- [ ] CT-01: Resource list contains the correct resource categories
  - Action: Inspect the resource list.
  - Expected: Items include meeting rooms, projectors, and shared workstations.

- [ ] CT-02: Upcoming reservations display relevant details
  - Action: Inspect an entry in the upcoming reservations list.
  - Expected: Each entry shows resource name, date, time, and purpose/title.