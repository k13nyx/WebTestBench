# Test Result

## Functionality

- [X] FT-01: Resource list displays bookable office resources from all three categories
  - Action: Open the reservation page and view the resource list section.
  - Expected: A list of resources is visible and contains at least one meeting room, one projector, and one shared workstation.

- [X] FT-02: User can select a resource from the list
  - Action: Click on any resource in the resource list (e.g., a meeting room).
  - Expected: That resource becomes the selected resource for the reservation.

- [X] FT-03: User can choose a reservation date
  - Action: Open the date field and pick a future date.
  - Expected: The chosen date is accepted and shown as the selected reservation date.

- [X] FT-04: User can choose a reservation time
  - Action: Open the time field and select a start time.
  - Expected: The chosen time is accepted and shown as the selected reservation time.

- [X] FT-05: User can enter a short purpose or title
  - Action: Type "Team Sync" into the purpose/title field.
  - Expected: The text is entered and retained in the field.

- [X] FT-06: Submitting creates a reservation that appears in the upcoming reservations list
  - Action: Select a resource, pick a future date and time, enter "Team Sync", then click the submit/reserve button.
  - Expected: A new reservation entry appears in the "Upcoming Reservations" list showing the same resource, date, time, and purpose "Team Sync".

- [X] FT-07: User can cancel an existing upcoming reservation
  - Action: From the upcoming reservations list, click the Cancel action on one existing (default) reservation and confirm.
  - Expected: That reservation is removed from the upcoming reservations list.

## Constraint

- [ ] CS-01: Cannot submit a reservation with an empty purpose/title
  - Action: Select a resource, date and time, leave the purpose/title field empty, click submit.
  - Expected: Submission is blocked, a validation message about the required purpose/title is shown, and no new reservation is added to the list.
  - Bug Report:
    - Issue: Missing validation feedback (silent failure)
    - Actual: With "Focus Pod A" selected, date = November 14th, 2026, times 11:00/12:00 and the "Purpose / Title" field left empty, clicking "Reserve" produced no error/toast/validation text and no inline message in the form. The "Reserve" button remained enabled (`isDisabled() === false`) and the input has no `required` / `aria-invalid` attributes. The reservation list stayed at 2 entries (submission was blocked), but the user receives no indication of why — the expected validation message about the required purpose/title was never displayed.

- [ ] CS-02: Cannot submit a reservation without selecting a resource
  - Action: Leave the resource unselected, choose a date and time, enter "Team Sync", click submit.
  - Expected: Submission is blocked, a validation message about selecting a resource is shown, and no new reservation is added.
  - Bug Report:
    - Issue: Missing validation message / no feedback path
    - Actual: With no resource selected the booking panel shows only "Select a Resource" / "Click on a resource card to start booking." — there is no date field, no time field and no "Reserve" button at all (`getByRole('button', {name:'Reserve'}).count() === 0`). Submission is blocked, but it is impossible to enter a date/time/purpose without first selecting a resource, and no validation message about selecting a resource is ever shown. The list remained unchanged (2 entries).

- [X] CS-03: Cannot submit a reservation without both a date and a time
  - Action: Select a resource, enter "Team Sync", leave the date (or time) empty, click submit.
  - Expected: Submission is blocked, a validation message about the missing date/time is shown, and no new reservation is added.

- [ ] CS-04: Cannot book a resource for a time slot that is already reserved
  - Action: Note the resource/date/time of an existing reservation in the list; submit a new reservation for the same resource, same date, and same/overlapping time with purpose "Overlap Test".
  - Expected: Submission is rejected with a conflict/unavailable message and no duplicate reservation is added.
  - Bug Report:
    - Issue: Missing double-booking / conflict validation
    - Actual: An existing reservation "Conflict Base" (Focus Pod A, Nov 20, 2026, 09:00–10:00) was created, then a second reservation "Overlap Test" for the same resource, same date and overlapping time 09:30–10:30 was submitted. It was accepted with the success toast "Reservation created! Focus Pod A booked for Nov 20, 2026". No conflict/unavailable message appeared and both entries now appear in the list ("Conflict Base" Nov 20, 2026 09:00 - 10:00 and "Overlap Test" Nov 20, 2026 09:30 - 10:30), i.e. a duplicate overlapping booking was added.

- [X] CS-05: Cannot select a date in the past
  - Action: Attempt to pick a date earlier than today in the date field.
  - Expected: Past dates are not selectable (disabled or rejected); the reservation cannot be submitted with a past date.

## Interaction

- [X] IX-01: Selecting a resource visually marks it as the selected one
  - Action: Click resource A, then click resource B in the resource list.
  - Expected: Resource B appears as selected (highlighted/checked) and resource A no longer appears selected.

- [X] IX-02: A success confirmation is shown after a reservation is submitted
  - Action: Complete and submit a valid reservation.
  - Expected: A success message/confirmation (e.g., "Reservation created" or toast) appears on screen.

- [ ] IX-03: Cancelling asks for confirmation before removing the reservation
  - Action: Click the Cancel action on an existing upcoming reservation.
  - Expected: A confirmation prompt/dialog appears; the reservation is only removed after the user confirms, and is kept if the user declines.
  - Bug Report:
    - Issue: Missing confirmation step on destructive action
    - Actual: Clicking the cancel (trash icon) button on the reservation "Team Sync" (Skyline Conference Room, Nov 20, 2026, 14:00–15:00) deleted it instantly. No confirmation dialog, prompt, or toast appeared, and the list immediately switched to the empty state ("No upcoming reservations"). There is no way for the user to decline, so a mis-click permanently removes a reservation.

- [X] IX-04: The reservation form is reset after a successful submission
  - Action: Submit a valid reservation, then inspect the resource/date/time/purpose fields.
  - Expected: All input fields return to their empty/default state (no leftover purpose text or selected resource).

- [X] IX-05: An empty-state message is shown when there are no upcoming reservations
  - Action: Cancel every reservation in the upcoming reservations list (or load the page with no reservations).
  - Expected: A message such as "No upcoming reservations" is displayed instead of an empty/blank list.

## Content

- [X] CT-01: Page heading identifies the page as an office resource reservation page
  - Action: Read the main heading/title at the top of the page.
  - Expected: The heading clearly relates to reserving office resources (e.g., "Office Resource Reservation"); no unrelated or generic heading.

- [X] CT-02: Every listed resource belongs to one of the three resource categories
  - Action: Read through all entries in the resource list.
  - Expected: Each entry is a meeting room, projector, or shared workstation; no unrelated items (e.g., office supplies, vehicles) appear.

- [X] CT-03: No broken images/icons or placeholder text on the page
  - Action: Visually inspect the entire page including resource list, form, and reservations list.
  - Expected: All images/icons load correctly (no broken-image placeholders) and no placeholder text such as "Lorem ipsum", "TODO", or "Sample" is visible.

- [X] CT-04: The reservations list is labeled and contains only upcoming (future) reservations
  - Action: Read the section heading above the reservations list and check the dates of all listed entries.
  - Expected: The section is labeled "Upcoming Reservations" (or equivalent) and every listed reservation has a date/time that is in the future.
