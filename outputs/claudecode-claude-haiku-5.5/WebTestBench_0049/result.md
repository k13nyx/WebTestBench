# Test Result

## Functionality
- [X] FT-01: Resource list shows office resources available for booking
  - Action: Open the reservation page and view the resource list.
  - Expected: The list shows the default meeting rooms, projectors, and shared workstations, each with a name and type.
- [X] FT-02: Valid reservation is created and saved
  - Action: Select a resource, choose a future date, set a start and end time, enter the title "QA Test Booking", and click the submit button.
  - Expected: The reservation is saved and appears in the "My Upcoming Reservations" list.
- [X] FT-03: Upcoming list shows only the current user's future reservations, sorted by date and time
  - Action: Open the "My Upcoming Reservations" list.
  - Expected: Only the logged-in user's reservations with a future start time are listed, in ascending date and time order.
- [X] FT-04: Cancelling a reservation removes it from the list
  - Action: Click "Cancel" on the reservation created in FT-02 and confirm the cancellation.
  - Expected: The reservation is removed from the upcoming list.

## Constraint
- [ ] CS-01: Submission is blocked when a required field is empty
  - Action: Leave the resource, date, time, or title empty and click the submit button.
  - Expected: Submission is blocked, the empty field is flagged with an error message, and no reservation is created.
  - Bug Report:
    - Issue: Missing Field-Level Validation Feedback
    - Actual: With the title empty and no date, Reserve shows only a transient toast ("Please select a date"). With a date selected and the title empty, it shows only a transient toast ("Please enter a title"). Neither input gets an inline error or `aria-invalid`. Submission is blocked and no reservation is created. The resource cannot be left empty because the form only appears after a resource card is clicked.
- [X] CS-02: Title containing only spaces is rejected
  - Action: Enter three spaces as the title, choose a valid resource, date, and time, and click the submit button.
  - Expected: Submission is blocked with a message that a title is required, and no reservation is created.
- [X] CS-03: Past dates cannot be reserved
  - Action: Attempt to select yesterday's date and submit a reservation.
  - Expected: Past dates are unselectable or submission is blocked with a past-date error, and no reservation is created.
- [X] CS-04: End time before start time is rejected
  - Action: Set the start time to 14:00 and the end time to 13:00, then submit.
  - Expected: Submission is blocked with an end-time-must-be-after-start-time error, and no reservation is created.
- [ ] CS-05: Overlapping booking of an already reserved resource is prevented
  - Action: Identify a default reservation for a resource. Attempt to book the same resource for a time range overlapping it and submit.
  - Expected: Submission is blocked with a message that the resource is already reserved for that time, and no duplicate reservation is created.
  - Bug Report:
    - Issue: Overlapping Booking Accepted (Double Booking)
    - Actual: Booking Skyline Conference Room for Nov 10, 2026, 09:30–10:30 while "QA Test Booking" (09:00–10:00) existed showed "Reservation created! Skyline Conference Room booked for Nov 10, 2026", and both appeared in the list. No default reservation was visible to test against, so the existing FT-02 booking was used as the reserved slot.
- [X] CS-06: Double-clicking submit creates only one reservation
  - Action: Fill in a valid reservation and double-click the submit button quickly.
  - Expected: Exactly one reservation appears in the upcoming list.
- [X] CS-07: Time slot becomes bookable again after cancellation
  - Action: Cancel the reservation from FT-04, then book the same resource for the same date and time.
  - Expected: The new reservation is accepted and saved.

## Interaction
- [ ] IX-01: Success message appears and the form resets after a valid submission
  - Action: Submit a valid reservation.
  - Expected: A "Reservation confirmed" message appears, and the form fields return to their empty default state.
  - Bug Report:
    - Issue: Incorrect Success Message
    - Actual: The toast reads "Reservation created!" with the text "Skyline Conference Room booked for Nov 10, 2026", not "Reservation confirmed". The form closes and returns to the "Select a Resource" empty state.
- [ ] IX-02: Cancel requires confirmation before the reservation is removed
  - Action: Click "Cancel" on a reservation, then click "Keep" or close the dialog.
  - Expected: A dialog titled "Cancel reservation?" appears with confirm and keep options. Choosing "Keep" leaves the reservation in the list unchanged.
  - Bug Report:
    - Issue: Missing Cancellation Confirmation Dialog
    - Actual: Clicking the reservation's remove control removed it immediately. No "Cancel reservation?" dialog appeared, and there was no "Keep" option. This happened twice. The control is an icon-only button with no accessible name, so it cannot be located by the "Cancel" label the test uses.
- [ ] IX-03: Cancellation shows a success notice and updates the list without a page reload
  - Action: Click "Cancel" on a reservation and confirm.
  - Expected: A "Reservation cancelled" message appears, and the reservation disappears from the list while the page stays in place.
  - Bug Report:
    - Issue: Missing Cancellation Success Notice
    - Actual: The reservation was removed from the list, but no "Reservation cancelled" message was present in the status region in either check (the toast list was empty immediately after the click).
- [X] IX-04: Selecting a resource highlights it and shows it in the form
  - Action: Click a resource in the resource list.
  - Expected: The clicked row is visually highlighted, only that row is highlighted, and the resource name appears in the reservation form.

## Content
- [X] CT-01: Each resource's name and icon match its type
  - Action: View the resource list and compare each item's name and icon.
  - Expected: Meeting rooms, projectors, and shared workstations each have a name and icon matching their type, with no mismatched icons.
- [X] CT-02: Upcoming reservation details match the submitted values
  - Action: Compare the resource, date, start and end time, and title shown in the upcoming list with those entered in FT-02.
  - Expected: Every displayed value matches the entered value exactly.
- [ ] CT-03: Dates and times are shown in a consistent, readable format
  - Action: Review the date and time shown in the reservation form and the upcoming list.
  - Expected: Dates and times use one consistent format across both views, for example "Mon, Nov 9, 2026 · 10:00–11:00".
  - Bug Report:
    - Issue: Inconsistent Date/Time Format
    - Actual: The form shows the date as "November 10th, 2026" and times as "09:00"/"10:00" (24-hour inputs). The upcoming list shows "Nov 10, 2026" and "09:00 - 10:00". The date formats differ between the two views, and neither uses the weekday format in the example.
- [X] CT-04: The page has no placeholder, broken, or irrelevant content
  - Action: Review the full reservation page, including headings, labels, icons, and default resource entries.
  - Expected: The page shows a relevant heading such as "Reserve Office Resources", all labels are meaningful, and there are no broken images, placeholder text, or unrelated content.

---

**Notes**
- FT-03: The app has no login, so the "only the logged-in user's" part could not be verified. Sorting and display were verified (ascending by date and time).
- FT-04 and IX-02: Removal was verified as an outcome. There was no confirmation step to perform.
- Test data left behind: "QA Test Booking" for Skyline Conference Room (Nov 10, 2026, 09:00–10:00) and "QA Test Booking" for Focus Pod A (Nov 11, 2026, 13:00–14:00). The CS-05 overlapping booking was removed during testing.
- Tool calls used: about 42 of 100.