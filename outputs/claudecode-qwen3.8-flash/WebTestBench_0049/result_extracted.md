# Test Result

## Functionality
- [X] FT-01: Resource list is displayed with selectable items
  - Action: Load the page and locate the resource list/section.
  - Expected: A list of reservable resources is shown (meeting rooms, projectors, shared workstations), each selectable or paired with a "Reserve"/"Book" control.
  - Verified: "Available Resources" section shows 8 resource cards, each a clickable button (Skyline Conference Room, Focus Pod A, Innovation Lab, Epson Pro 4K, Portable Mini Projector, Design Station Alpha, Developer Hub 1, Quiet Corner Desk), plus category filter buttons (All/Rooms/Projectors/Workstations).

- [X] FT-02: User can choose a resource and open the reservation form
  - Action: Click/select the first meeting room in the resource list.
  - Expected: A reservation form appears (or is focused) with the selected resource reflected in the form (e.g., its name shown as selected).
  - Verified: Clicking "Skyline Conference Room" opened the "Make Reservation" form showing "Skyline Conference Room / Floor 12, East Wing" with Purpose, Date, Start/End Time fields and Cancel/Reserve buttons.

- [X] FT-03: User can pick a date and time for the reservation
  - Action: In the reservation form, set the date field to 2026-11-15 and a start time (and end time if the field exists).
  - Expected: Date and time fields accept the values and display them correctly after input.
  - Verified: Date picker selected 15 Nov 2026 → button displays "November 15th, 2026"; time inputs accepted 10:00 / 11:00 (confirmed via DOM values `["10:00","11:00"]`).

- [X] FT-04: User can enter a purpose/title for the reservation
  - Action: Type "Sprint Planning" into the purpose/title field.
  - Expected: The text is accepted and displayed in the field.
  - Verified: "Purpose / Title" input value read back as "Sprint Planning".

- [X] FT-05: Submitting a valid reservation creates it
  - Action: Complete the form with a resource, date 2026-11-15, a time, and title "Sprint Planning", then click the submit/"Reserve" button.
  - Expected: The submission succeeds and the new reservation appears in the upcoming reservations list with its resource, date, time, and title.
  - Verified: After clicking Reserve, toast "Reservation created! Skyline Conference Room booked for Nov 15, 2026" appeared and a new card "Sprint Planning / Skyline Conference Room / Nov 15, 2026 / 10:00 - 11:00" appeared in "Your Reservations".

- [X] FT-06: Upcoming reservations list is visible with details
  - Action: Locate the "My Reservations"/"Upcoming Reservations" section after creating a reservation (or check default data).
  - Expected: A list of upcoming reservations is shown, each displaying at minimum: resource name, date, time, and title/purpose.
  - Verified: "Your Reservations" section lists each reservation with title (h4), resource name, date (Nov 15, 2026), time range (10:00 - 11:00), and location. Empty state ("No upcoming reservations") shown before any booking.

- [X] FT-07: User can cancel a reservation
  - Action: Click the "Cancel" control on one reservation in the upcoming list and confirm if prompted.
  - Expected: The reservation is removed from the upcoming reservations list.
  - Verified: Clicking the delete (trash) button on the "Desk Work Session" reservation removed it immediately (no confirmation prompt required); count of that heading went from 1 → 0 while the other reservation remained. Note: the icon-only cancel button has no aria-label/title (minor accessibility issue, behavior itself is correct).

## Constraint
- [X] CS-01: Reservation cannot be submitted without a purpose/title
  - Action: Fill resource, date, and time, leave the title/purpose field empty, then click submit.
  - Expected: The reservation is NOT created and does not appear in the upcoming list.
  - Verified: Submitting with empty title produced toast "Please enter a title"; no new reservation appeared in the list.

- [X] CS-02: Reservation cannot be submitted without date/time
  - Action: Select a resource and enter a title, but leave the date (or time) field empty, then click submit.
  - Expected: The reservation is NOT created and does not appear in the upcoming list.
  - Verified: With title "No Time Test" and both time fields cleared, submission was rejected with toast "End time must be after start time"; reservation list unchanged.

- [ ] CS-03: A resource cannot be double-booked for an overlapping time slot
  - Action: Book resource A on 2026-11-15 10:00–11:00, then attempt to book the same resource A on the same date with an overlapping slot (e.g., 10:30–11:30).
  - Expected: The second reservation is rejected — not added to the list; the original booking remains intact.
  - Bug Report:
    - Issue: Missing double-booking/overlap validation
    - Actual: With "Sprint Planning" already booked for Skyline Conference Room Nov 15, 2026, 10:00–11:00, submitting "Conflict Test" for the SAME room, same date, 10:30–11:30 (overlapping) was ACCEPTED: toast "Reservation created! Skyline Conference Room booked for Nov 15, 2026" appeared and the overlapping reservation was added to the list. No conflict check exists.

- [X] CS-04: Past dates cannot be selected for a reservation
  - Action: Attempt to set the reservation date to a past date (e.g., 2026-11-01, before today 2026-11-08) and submit.
  - Expected: The past date is rejected — the date picker disallows it or submission fails with no reservation created.
  - Verified: Date picker disables all past days: Nov 1–7 gridcells are `[disabled]` in November 2026, and navigating to October 2026 shows every day `[disabled]` — 2026-11-01 cannot be selected, so no reservation can be created for it.

- [X] CS-05: A cancelled time slot becomes bookable again
  - Action: Book resource B for a slot, cancel that reservation, then re-book resource B for the same slot.
  - Expected: The re-booking succeeds and appears in the upcoming list (the cancel fully released the slot).
  - Verified: Booked "Desk Work Session" for Focus Pod A, Nov 15, 2026, 14:00–15:00 → cancelled it → re-booked "Re-booked Session" for Focus Pod A, Nov 15, 2026, 14:00–15:00 → succeeded ("Reservation created!" toast) and appeared in the list.

## Interaction
- [X] IX-01: Success feedback shown after a reservation is created
  - Action: Submit a valid reservation.
  - Expected: A visible confirmation is displayed (success toast, banner, or message referencing the reservation).
  - Verified: Status toast in the Notifications region: "Reservation created! Skyline Conference Room booked for Nov 15, 2026" (repeated for each successful booking, with the resource name and date).

- [ ] IX-02: Error feedback shown on invalid/conflicting submissions
  - Action: Trigger the CS-01 case (empty title) and the CS-03 case (overlapping slot).
  - Expected: A visible error message identifies the problem (e.g., "title required" / "slot already booked") instead of a silent failure.
  - Bug Report:
    - Issue: Missing conflict error feedback (CS-03 case)
    - Actual: Empty-title case correctly showed error toast "Please enter a title". However, the overlapping-slot case produced NO error — the app accepted the double booking and displayed the success toast "Reservation created!" instead of any "slot already booked" message, so the conflict half of this check fails.

- [ ] IX-03: Feedback shown after cancelling a reservation
  - Action: Cancel a reservation from the upcoming list.
  - Expected: A visible confirmation (toast/message) indicates the cancellation succeeded, and the list updates without requiring a manual page reload.
  - Bug Report:
    - Issue: Missing cancellation feedback
    - Actual: The list did update in place without a page reload (requirement partially met), but NO confirmation toast/message was displayed after cancelling — the Notifications regions ("Notifications (F8)" and "Notifications alt+T") remained completely empty immediately after cancellation and on re-inspection (checked 400 ms after click and again later; zero toast elements in DOM).

## Content
- [X] CT-01: Default resources cover all three requested types
  - Action: Inspect the resource list names, icons, and category labels.
  - Expected: At least one meeting room, one projector, and one shared workstation are present; all entries are relevant office resources (no placeholder text like "lorem ipsum" or empty/broken items).
  - Verified: 3 Meeting Rooms (Skyline Conference Room, Focus Pod A, Innovation Lab), 2 Projectors (Epson Pro 4K, Portable Mini Projector), 3 Workstations (Design Station Alpha, Developer Hub 1, Quiet Corner Desk). Each card has an icon, category label, description, and location/capacity; no placeholder or empty items.

- [X] CT-02: Reservation details displayed match what was entered
  - Action: Create a reservation with resource "Room X", date 2026-11-15, time 10:00, title "Sprint Planning", then read its entry in the upcoming list.
  - Expected: The list entry shows exactly the submitted resource, date, time, and title with no missing or garbled fields.
  - Verified: Submitted Skyline Conference Room (app's first meeting room) on Nov 15, 2026, 10:00–11:00 with title "Sprint Planning"; list entry rendered heading "Sprint Planning", "Skyline Conference Room", "Nov 15, 2026", "10:00 - 11:00", "Floor 12, East Wing" — all fields intact and matching input.
