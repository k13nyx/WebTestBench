# Test Checklist

## Functionality
- [ ] FT-01: Resource list offers the required office resources for selection
  - Action: Open the reservation page and inspect the resource selection list.
  - Expected: The list includes at least a meeting room, a projector, and a shared workstation, each selectable.
- [ ] FT-02: User can choose a reservation date
  - Action: Pick a resource, then select a date using the date field.
  - Expected: The chosen date is displayed in the date field and is retained when submitting.
- [ ] FT-03: User can choose a reservation time range
  - Action: Select a start time and an end time for the chosen date.
  - Expected: Both selected times are displayed in their respective fields.
- [ ] FT-04: User can enter a purpose/title for the reservation
  - Action: Type a short purpose (e.g., "Sprint planning") into the purpose/title field.
  - Expected: The typed text appears in the field.
- [ ] FT-05: Valid reservation can be submitted
  - Action: With a resource, date, time range, and purpose all filled in, click the submit/reserve button.
  - Expected: The reservation is created and appears in the upcoming reservations list.
- [ ] FT-06: Upcoming reservations list shows reservation details
  - Action: View the upcoming reservations list after submitting a reservation.
  - Expected: The list shows the resource name, date, start–end time, and purpose matching what was entered.
- [ ] FT-07: User can cancel an upcoming reservation
  - Action: Click the cancel action on an existing upcoming reservation.
  - Expected: The reservation is cancelled and no longer appears as upcoming.

## Constraint
- [ ] CS-01: Submission blocked when no resource is selected
  - Action: Leave the resource unselected, fill the other fields, and click submit.
  - Expected: No reservation is created; an error/prompt indicates a resource must be selected.
- [ ] CS-02: Submission blocked when date or time is missing
  - Action: Leave the date or time fields empty and click submit.
  - Expected: No reservation is created; an error/prompt indicates date and time are required.
- [ ] CS-03: Submission blocked when purpose/title is empty
  - Action: Clear the purpose/title field and click submit.
  - Expected: No reservation is created; an error/prompt indicates the purpose/title is required.
- [ ] CS-04: Submission blocked when end time is not after start time
  - Action: Set an end time earlier than or equal to the start time and click submit.
  - Expected: No reservation is created; an error indicates the time range is invalid.
- [ ] CS-05: Conflicting reservation for an already-booked slot is rejected
  - Action: Attempt to reserve a resource for a date/time slot already occupied by an existing reservation.
  - Expected: The submission is rejected with a message indicating the resource is already booked for that slot.
- [ ] CS-06: Past date/time cannot be reserved
  - Action: Select a date/time fully in the past and click submit.
  - Expected: No reservation is created; an error indicates the slot must be in the future.

## Interaction
- [ ] IX-01: Success feedback shown after submitting a reservation
  - Action: Submit a valid reservation.
  - Expected: A visible success confirmation (e.g., toast/message) appears stating the reservation was created.
- [ ] IX-02: Cancel action gives feedback and updates the list immediately
  - Action: Cancel an upcoming reservation.
  - Expected: A confirmation of cancellation appears and the reservation is removed from the list without a page reload.
- [ ] IX-03: Selected resource is visually indicated in the list
  - Action: Click on a resource in the resource list.
  - Expected: The clicked resource becomes visibly highlighted/selected as the active choice.

## Content
- [ ] CT-01: All resources shown match the office-resource theme
  - Action: Review the resource list names and any descriptions.
  - Expected: Every listed item is an office resource (meeting room, projector, shared workstation, or similar); no irrelevant items.
- [ ] CT-02: Reservation details displayed are accurate and readable
  - Action: Compare a submitted reservation's entry in the upcoming list with the values entered at submission.
  - Expected: Resource name, date, time range, and purpose text match the input exactly and are formatted readably (e.g., ISO or clear date format).