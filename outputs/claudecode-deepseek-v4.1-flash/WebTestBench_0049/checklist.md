# Test Checklist

## Functionality
- [ ] FT-01: Resource list is displayed with selectable resources
  - Action: Load the reservation page and view the resource selection area
  - Expected: A list containing meeting rooms, projectors, and shared workstations is shown, each selectable
- [ ] FT-02: A resource can be selected from the list
  - Action: Click a resource (e.g., a meeting room) in the list
  - Expected: The chosen resource is visibly marked as selected
- [ ] FT-03: A date can be chosen
  - Action: Use the date field to pick a date
  - Expected: The selected date is entered and displayed in the field
- [ ] FT-04: A time can be chosen
  - Action: Use the time field to pick a start time
  - Expected: The selected time is entered and displayed in the field
- [ ] FT-05: A short purpose/title can be entered
  - Action: Type text (e.g., "Team sync") into the purpose/title field
  - Expected: The entered text appears in the field
- [ ] FT-06: A reservation can be submitted successfully
  - Action: Fill all fields with valid values and click the submit button (e.g., "Reserve")
  - Expected: The reservation is created and accepted by the system
- [ ] FT-07: Upcoming reservations are listed
  - Action: View the "Upcoming Reservations" section
  - Expected: The newly created reservation appears in the list
- [ ] FT-08: An upcoming reservation can be cancelled
  - Action: Click the cancel action (e.g., "Cancel") on a listed reservation
  - Expected: The reservation is removed from the upcoming reservations list

## Constraint
- [ ] CS-01: Reservation cannot be submitted without a selected resource
  - Action: Leave resource unselected, fill other fields, and click submit
  - Expected: Submission is blocked and a resource-required message is shown
- [ ] CS-02: Reservation cannot be submitted without a date or time
  - Action: Leave date and/or time empty, fill other fields, and click submit
  - Expected: Submission is blocked and a date/time-required message is shown
- [ ] CS-03: Reservation cannot be submitted with an empty purpose/title
  - Action: Leave the purpose/title field empty, fill other fields, and click submit
  - Expected: Submission is blocked and a purpose-required message is shown
- [ ] CS-04: A resource cannot be double-booked for the same date and time
  - Action: Reserve a resource for a date/time, then attempt a second reservation for the same resource, date, and time
  - Expected: The second submission is rejected with a conflict/availability message
- [ ] CS-05: A past date or time cannot be reserved
  - Action: Attempt to select a past date or time and submit
  - Expected: The past selection is rejected or unavailable

## Interaction
- [ ] IX-01: Success confirmation appears after a valid submission
  - Action: Submit a valid reservation
  - Expected: A success message/toast confirms the reservation was created
- [ ] IX-02: The form resets after a successful submission
  - Action: Submit a valid reservation and observe the form
  - Expected: Input fields are cleared/reset for the next entry
- [ ] IX-03: Cancelling a reservation gives feedback
  - Action: Cancel a listed reservation
  - Expected: A confirmation prompt or message indicates the cancellation succeeded

## Content
- [ ] CT-01: Resource list content matches the reservation theme
  - Action: Review the resource list entries
  - Expected: All entries are office resources (meeting rooms, projectors, shared workstations) with no unrelated items
- [ ] CT-02: Reservation entries display the correct details
  - Action: Review a reservation in the upcoming reservations list
  - Expected: It shows the resource name, date/time, and the entered purpose/title accurately