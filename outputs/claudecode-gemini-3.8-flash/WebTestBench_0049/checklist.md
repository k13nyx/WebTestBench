# Test Checklist

## Functionality
- [ ] FT-01: Select an office resource from the available options
  - Action: Click on a resource item or select one (e.g., "Meeting Room A") from the resource list.
  - Expected: The selected resource is marked as active or populated into the reservation form.
- [ ] FT-02: Submit a valid reservation
  - Action: Select an available resource, choose a future date and time, enter a title (e.g., "Team Sync") in the purpose field, and click the "Reserve" button.
  - Expected: The reservation is created and appears in the "Upcoming Reservations" list.
- [ ] FT-03: View upcoming reservations list
  - Action: Navigate to or observe the "Upcoming Reservations" section after creating a booking.
  - Expected: The new reservation is listed showing the resource name, title/purpose, and scheduled date and time.
- [ ] FT-04: Cancel an active reservation
  - Action: Click the "Cancel" button on an existing item in the "Upcoming Reservations" list and confirm the action.
  - Expected: The selected reservation is immediately removed from the upcoming reservations list.

## Constraint
- [ ] CS-01: Block reservation submission with missing required fields
  - Action: Leave the purpose input or date/time field empty and click the "Reserve" button.
  - Expected: The form is not submitted, and validation error messages highlight the required empty fields.
- [ ] CS-02: Prevent booking a date and time in the past
  - Action: Select a past date or time from the picker and attempt to submit the reservation.
  - Expected: The system prevents selection or displays an error indicating that past dates and times cannot be reserved.
- [ ] CS-03: Prevent double-booking conflicting time slots for the same resource
  - Action: Attempt to reserve the same resource for a date and time slot that is already booked.
  - Expected: The reservation is rejected, and an alert indicates that the resource is already occupied for the chosen time.

## Interaction
- [ ] IX-01: Display success notification upon reservation submission
  - Action: Fill out all required fields with valid data and click the "Reserve" button.
  - Expected: A temporary success banner or toast message appears stating the reservation was successfully created.
- [ ] IX-02: Show confirmation prompt prior to reservation cancellation
  - Action: Click the "Cancel" button next to an upcoming reservation item.
  - Expected: A confirmation modal or prompt opens asking the user to confirm the cancellation before proceeding.
- [ ] IX-03: Reset reservation form fields after successful creation
  - Action: Submit a valid reservation and inspect the input form.
  - Expected: The resource picker, date/time picker, and purpose text field clear and return to their default empty states.
- [ ] IX-04: Display feedback notification upon cancellation
  - Action: Confirm the cancellation in the prompt dialog.
  - Expected: A notification toast appears confirming the reservation has been successfully canceled.

## Content
- [ ] CT-01: Display required resource categories
  - Action: Inspect the resource selection list on the page.
  - Expected: The list explicitly contains options for meeting rooms, projectors, and shared workstations.
- [ ] CT-02: Display complete reservation details in upcoming list items
  - Action: Inspect an existing entry within the "Upcoming Reservations" list.
  - Expected: The item clearly displays the resource name, reservation title/purpose, and formatted date and time.
- [ ] CT-03: Display empty state message when no reservations exist
  - Action: View the "Upcoming Reservations" section when no reservations are booked (or after all are canceled).
  - Expected: A clear message (e.g., "No upcoming reservations found") is displayed instead of a blank area.