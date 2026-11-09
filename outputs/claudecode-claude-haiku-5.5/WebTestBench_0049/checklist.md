# Test Checklist

## Functionality
- [ ] FT-01: Resource list shows office resources available for booking
  - Action: Open the reservation page and view the resource list.
  - Expected: The list shows the default meeting rooms, projectors, and shared workstations, each with a name and type.
- [ ] FT-02: Valid reservation is created and saved
  - Action: Select a resource, choose a future date, set a start and end time, enter the title "QA Test Booking", and click the submit button.
  - Expected: The reservation is saved and appears in the "My Upcoming Reservations" list.
- [ ] FT-03: Upcoming list shows only the current user's future reservations, sorted by date and time
  - Action: Open the "My Upcoming Reservations" list.
  - Expected: Only the logged-in user's reservations with a future start time are listed, in ascending date and time order.
- [ ] FT-04: Cancelling a reservation removes it from the list
  - Action: Click "Cancel" on the reservation created in FT-02 and confirm the cancellation.
  - Expected: The reservation is removed from the upcoming list.

## Constraint
- [ ] CS-01: Submission is blocked when a required field is empty
  - Action: Leave the resource, date, time, or title empty and click the submit button.
  - Expected: Submission is blocked, the empty field is flagged with an error message, and no reservation is created.
- [ ] CS-02: Title containing only spaces is rejected
  - Action: Enter three spaces as the title, choose a valid resource, date, and time, and click the submit button.
  - Expected: Submission is blocked with a message that a title is required, and no reservation is created.
- [ ] CS-03: Past dates cannot be reserved
  - Action: Attempt to select yesterday's date and submit a reservation.
  - Expected: Past dates are unselectable or submission is blocked with a past-date error, and no reservation is created.
- [ ] CS-04: End time before start time is rejected
  - Action: Set the start time to 14:00 and the end time to 13:00, then submit.
  - Expected: Submission is blocked with an end-time-must-be-after-start-time error, and no reservation is created.
- [ ] CS-05: Overlapping booking of an already reserved resource is prevented
  - Action: Identify a default reservation for a resource. Attempt to book the same resource for a time range overlapping it and submit.
  - Expected: Submission is blocked with a message that the resource is already reserved for that time, and no duplicate reservation is created.
- [ ] CS-06: Double-clicking submit creates only one reservation
  - Action: Fill in a valid reservation and double-click the submit button quickly.
  - Expected: Exactly one reservation appears in the upcoming list.
- [ ] CS-07: Time slot becomes bookable again after cancellation
  - Action: Cancel the reservation from FT-04, then book the same resource for the same date and time.
  - Expected: The new reservation is accepted and saved.

## Interaction
- [ ] IX-01: Success message appears and the form resets after a valid submission
  - Action: Submit a valid reservation.
  - Expected: A "Reservation confirmed" message appears, and the form fields return to their empty default state.
- [ ] IX-02: Cancel requires confirmation before the reservation is removed
  - Action: Click "Cancel" on a reservation, then click "Keep" or close the dialog.
  - Expected: A dialog titled "Cancel reservation?" appears with confirm and keep options. Choosing "Keep" leaves the reservation in the list unchanged.
- [ ] IX-03: Cancellation shows a success notice and updates the list without a page reload
  - Action: Click "Cancel" on a reservation and confirm.
  - Expected: A "Reservation cancelled" message appears, and the reservation disappears from the list while the page stays in place.
- [ ] IX-04: Selecting a resource highlights it and shows it in the form
  - Action: Click a resource in the resource list.
  - Expected: The clicked row is visually highlighted, only that row is highlighted, and the resource name appears in the reservation form.

## Content
- [ ] CT-01: Each resource's name and icon match its type
  - Action: View the resource list and compare each item's name and icon.
  - Expected: Meeting rooms, projectors, and shared workstations each have a name and icon matching their type, with no mismatched icons.
- [ ] CT-02: Upcoming reservation details match the submitted values
  - Action: Compare the resource, date, start and end time, and title shown in the upcoming list with those entered in FT-02.
  - Expected: Every displayed value matches the entered value exactly.
- [ ] CT-03: Dates and times are shown in a consistent, readable format
  - Action: Review the date and time shown in the reservation form and the upcoming list.
  - Expected: Dates and times use one consistent format across both views, for example "Mon, Nov 9, 2026 · 10:00–11:00".
- [ ] CT-04: The page has no placeholder, broken, or irrelevant content
  - Action: Review the full reservation page, including headings, labels, icons, and default resource entries.
  - Expected: The page shows a relevant heading such as "Reserve Office Resources", all labels are meaningful, and there are no broken images, placeholder text, or unrelated content.