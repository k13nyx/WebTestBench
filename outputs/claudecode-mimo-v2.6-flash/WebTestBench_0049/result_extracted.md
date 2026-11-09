# Test Result

## Functionality
- [X] FT-01: Resource list offers the required office resources for selection
  - Action: Open the reservation page and inspect the resource selection list.
  - Expected: The list includes at least a meeting room, a projector, and a shared workstation, each selectable.
  - Actual: List contains 3 Meeting Rooms (Skyline Conference Room, Focus Pod A, Innovation Lab), 2 Projectors (Epson Pro 4K, Portable Mini Projector), and 3 Workstations (Design Station Alpha, Developer Hub 1, Quiet Corner Desk). Clicking a meeting room, a projector, and a workstation each opened the "Make Reservation" form for that resource.

- [X] FT-02: User can choose a reservation date
  - Action: Pick a resource, then select a date using the date field.
  - Expected: The chosen date is displayed in the date field and is retained when submitting.
  - Actual: After picking Nov 12 in the calendar, the date button displayed "November 12th, 2026"; the created reservation was stored with "Nov 12, 2026".

- [X] FT-03: User can choose a reservation time range
  - Action: Select a start time and an end time for the chosen date.
  - Expected: Both selected times are displayed in their respective fields.
  - Actual: Start Time field showed 10:00 and End Time field showed 11:00 after entry; the reservation was recorded as "10:00 - 11:00".

- [X] FT-04: User can enter a purpose/title for the reservation
  - Action: Type a short purpose (e.g., "Sprint planning") into the purpose/title field.
  - Expected: The typed text appears in the field.
  - Actual: The Purpose / Title textbox contained "Sprint planning" after typing.

- [X] FT-05: Valid reservation can be submitted
  - Action: With a resource, date, time range, and purpose all filled in, click the submit/reserve button.
  - Expected: The reservation is created and appears in the upcoming reservations list.
  - Actual: Clicking "Reserve" created the reservation and it appeared under "Your Reservations".

- [X] FT-06: Upcoming reservations list shows reservation details
  - Action: View the upcoming reservations list after submitting a reservation.
  - Expected: The list shows the resource name, date, start–end time, and purpose matching what was entered.
  - Actual: Entry showed purpose "Sprint planning" (heading), resource "Skyline Conference Room", date "Nov 12, 2026", time "10:00 - 11:00".

- [X] FT-07: User can cancel an upcoming reservation
  - Action: Click the cancel action on an existing upcoming reservation.
  - Expected: The reservation is cancelled and no longer appears as upcoming.
  - Actual: Clicking the cancel (X) button removed the reservation from the "Your Reservations" list immediately; repeated cancels emptied the list.

## Constraint
- [ ] CS-01: Submission blocked when no resource is selected
  - Action: Leave the resource unselected, fill the other fields, and click submit.
  - Expected: No reservation is created; an error/prompt indicates a resource must be selected.
  - Bug Report:
    - Issue: Missing Validation Prompt / Action Not Executable (submit control absent without resource)
    - Actual: When no resource is selected, the booking form is not rendered at all — DOM inspection shows 0 Reserve buttons, 0 forms, and 0 inputs (only the static "Select a Resource / Click on a resource card to start booking" placeholder). The action "fill the other fields and click submit" cannot be performed, and no error/prompt ever indicates that a resource must be selected. (No reservation is created, but the required feedback is missing.)

- [ ] CS-02: Submission blocked when date or time is missing
  - Action: Leave the date or time fields empty and click submit.
  - Expected: No reservation is created; an error/prompt indicates date and time are required.
  - Bug Report:
    - Issue: Missing Time Validation / Incorrect Form Submission
    - Actual: With the date set but the Start Time field cleared, clicking "Reserve" succeeded: toast "Reservation created! Skyline Conference Room booked for Nov 13, 2026" and a list entry was created displaying a missing start time as "Nov 13, 2026 - 11:00". (Empty date alone is blocked with "Please select a date", but an empty time field is not validated.)

- [X] CS-03: Submission blocked when purpose/title is empty
  - Action: Clear the purpose/title field and click submit.
  - Expected: No reservation is created; an error/prompt indicates the purpose/title is required.
  - Actual: Submitting with an empty Purpose / Title (valid date/time) showed error toast "Please enter a title" and no reservation was added.

- [X] CS-04: Submission blocked when end time is not after start time
  - Action: Set an end time earlier than or equal to the start time and click submit.
  - Expected: No reservation is created; an error indicates the time range is invalid.
  - Actual: Submitting start 10:00 / end 10:00 showed error toast "End time must be after start time"; no reservation was created and the form remained.

- [ ] CS-05: Conflicting reservation for an already-booked slot is rejected
  - Action: Attempt to reserve a resource for a date/time slot already occupied by an existing reservation.
  - Expected: The submission is rejected with a message indicating the resource is already booked for that slot.
  - Bug Report:
    - Issue: No Conflict/Double-Booking Detection
    - Actual: "Sprint planning" already occupied Skyline Conference Room on Nov 12, 2026, 10:00-11:00, yet submitting "Conflict test" for the identical slot returned toast "Reservation created!" and added a second overlapping entry — both appear in the list with the same resource, date, and time.

- [ ] CS-06: Past date/time cannot be reserved
  - Action: Select a date/time fully in the past and click submit.
  - Expected: No reservation is created; an error indicates the slot must be in the future.
  - Bug Report:
    - Issue: Missing Past-Slot Validation
    - Actual: With current time Nov 09, 2026 04:14, submitting Nov 9, 2026 01:00-02:00 (fully past) was accepted: toast "Reservation created! Skyline Conference Room booked for Nov 9, 2026" and the entry was added to the list. (Only dates before today are disabled in the picker; past times on the current day pass.)

## Interaction
- [X] IX-01: Success feedback shown after submitting a reservation
  - Action: Submit a valid reservation.
  - Expected: A visible success confirmation (e.g., toast/message) appears stating the reservation was created.
  - Actual: Toast appeared in the notifications region: "Reservation created!" with description "Skyline Conference Room booked for Nov 12, 2026".

- [ ] IX-02: Cancel action gives feedback and updates the list immediately
  - Action: Cancel an upcoming reservation.
  - Expected: A confirmation of cancellation appears and the reservation is removed from the list without a page reload.
  - Bug Report:
    - Issue: Missing Cancellation Feedback/Confirmation
    - Actual: The list updates immediately without reload (card removed in the same React commit), but no confirmation appears: a MutationObserver installed before the cancel captured only the removed node ("No time testSkyline Conference RoomNov 13, 2026 - 11:00Floor 12, East Wing") and zero added nodes — no toast or message was ever rendered; the notifications region stayed empty.

- [X] IX-03: Selected resource is visually indicated in the list
  - Action: Click on a resource in the resource list.
  - Expected: The clicked resource becomes visibly highlighted/selected as the active choice.
  - Actual: The selected card carries `border-primary bg-primary/5` with computed border rgb(36, 99, 235) and a primary focus ring, while unselected cards use `border-border bg-card` (rgb(225, 231, 239)); highlight moved correctly when switching from Skyline to Epson Pro 4K to Design Station Alpha.

## Content
- [X] CT-01: All resources shown match the office-resource theme
  - Action: Review the resource list names and any descriptions.
  - Expected: Every listed item is an office resource (meeting room, projector, shared workstation, or similar); no irrelevant items.
  - Actual: All 8 items are office resources — Skyline Conference Room, Focus Pod A, Innovation Lab (Meeting Room); Epson Pro 4K, Portable Mini Projector (Projector); Design Station Alpha, Developer Hub 1, Quiet Corner Desk (Workstation). No irrelevant items.

- [X] CT-02: Reservation details displayed are accurate and readable
  - Action: Compare a submitted reservation's entry in the upcoming list with the values entered at submission.
  - Expected: Resource name, date, time range, and purpose text match the input exactly and are formatted readably (e.g., ISO or clear date format).
  - Actual: Input (Skyline Conference Room, Nov 12 2026, 10:00/11:00, "Sprint planning") rendered as "Sprint planning / Skyline Conference Room / Nov 12, 2026 / 10:00 - 11:00 / Floor 12, East Wing" — matching and readable.
