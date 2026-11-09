# Test Checklist

## Functionality
- [ ] FT-01: Resource list is displayed with selectable items
  - Action: Load the page and locate the resource list/section.
  - Expected: A list of reservable resources is shown (meeting rooms, projectors, shared workstations), each selectable or paired with a "Reserve"/"Book" control.

- [ ] FT-02: User can choose a resource and open the reservation form
  - Action: Click/select the first meeting room in the resource list.
  - Expected: A reservation form appears (or is focused) with the selected resource reflected in the form (e.g., its name shown as selected).

- [ ] FT-03: User can pick a date and time for the reservation
  - Action: In the reservation form, set the date field to 2026-11-15 and a start time (and end time if the field exists).
  - Expected: Date and time fields accept the values and display them correctly after input.

- [ ] FT-04: User can enter a purpose/title for the reservation
  - Action: Type "Sprint Planning" into the purpose/title field.
  - Expected: The text is accepted and displayed in the field.

- [ ] FT-05: Submitting a valid reservation creates it
  - Action: Complete the form with a resource, date 2026-11-15, a time, and title "Sprint Planning", then click the submit/"Reserve" button.
  - Expected: The submission succeeds and the new reservation appears in the upcoming reservations list with its resource, date, time, and title.

- [ ] FT-06: Upcoming reservations list is visible with details
  - Action: Locate the "My Reservations"/"Upcoming Reservations" section after creating a reservation (or check default data).
  - Expected: A list of upcoming reservations is shown, each displaying at minimum: resource name, date, time, and title/purpose.

- [ ] FT-07: User can cancel a reservation
  - Action: Click the "Cancel" control on one reservation in the upcoming list and confirm if prompted.
  - Expected: The reservation is removed from the upcoming reservations list.

## Constraint
- [ ] CS-01: Reservation cannot be submitted without a purpose/title
  - Action: Fill resource, date, and time, leave the title/purpose field empty, then click submit.
  - Expected: The reservation is NOT created and does not appear in the upcoming list.

- [ ] CS-02: Reservation cannot be submitted without date/time
  - Action: Select a resource and enter a title, but leave the date (or time) field empty, then click submit.
  - Expected: The reservation is NOT created and does not appear in the upcoming list.

- [ ] CS-03: A resource cannot be double-booked for an overlapping time slot
  - Action: Book resource A on 2026-11-15 10:00–11:00, then attempt to book the same resource A on the same date with an overlapping slot (e.g., 10:30–11:30).
  - Expected: The second reservation is rejected — not added to the list; the original booking remains intact.

- [ ] CS-04: Past dates cannot be selected for a reservation
  - Action: Attempt to set the reservation date to a past date (e.g., 2026-11-01, before today 2026-11-08) and submit.
  - Expected: The past date is rejected — the date picker disallows it or submission fails with no reservation created.

- [ ] CS-05: A cancelled time slot becomes bookable again
  - Action: Book resource B for a slot, cancel that reservation, then re-book resource B for the same slot.
  - Expected: The re-booking succeeds and appears in the upcoming list (the cancel fully released the slot).

## Interaction
- [ ] IX-01: Success feedback shown after a reservation is created
  - Action: Submit a valid reservation.
  - Expected: A visible confirmation is displayed (success toast, banner, or message referencing the reservation).

- [ ] IX-02: Error feedback shown on invalid/conflicting submissions
  - Action: Trigger the CS-01 case (empty title) and the CS-03 case (overlapping slot).
  - Expected: A visible error message identifies the problem (e.g., "title required" / "slot already booked") instead of a silent failure.

- [ ] IX-03: Feedback shown after cancelling a reservation
  - Action: Cancel a reservation from the upcoming list.
  - Expected: A visible confirmation (toast/message) indicates the cancellation succeeded, and the list updates without requiring a manual page reload.

## Content
- [ ] CT-01: Default resources cover all three requested types
  - Action: Inspect the resource list names, icons, and category labels.
  - Expected: At least one meeting room, one projector, and one shared workstation are present; all entries are relevant office resources (no placeholder text like "lorem ipsum" or empty/broken items).

- [ ] CT-02: Reservation details displayed match what was entered
  - Action: Create a reservation with resource "Room X", date 2026-11-15, time 10:00, title "Sprint Planning", then read its entry in the upcoming list.
  - Expected: The list entry shows exactly the submitted resource, date, time, and title with no missing or garbled fields.