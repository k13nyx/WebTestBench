I have completed all checklist items. Here is the full report.

# Test Result

## Functionality
- [X] FT-01: Resource list is displayed with selectable resources
  - Action: Load the reservation page and view the resource selection area
  - Expected: A list containing meeting rooms, projectors, and shared workstations is shown, each selectable

- [X] FT-02: A resource can be selected from the list
  - Action: Click a resource (e.g., a meeting room) in the list
  - Expected: The chosen resource is visibly marked as selected

- [X] FT-03: A date can be chosen
  - Action: Use the date field to pick a date
  - Expected: The selected date is entered and displayed in the field

- [X] FT-04: A time can be chosen
  - Action: Use the time field to pick a start time
  - Expected: The selected time is entered and displayed in the field

- [X] FT-05: A short purpose/title can be entered
  - Action: Type text (e.g., "Team sync") into the purpose/title field
  - Expected: The entered text appears in the field

- [X] FT-06: A reservation can be submitted successfully
  - Action: Fill all fields with valid values and click the submit button (e.g., "Reserve")
  - Expected: The reservation is created and accepted by the system

- [X] FT-07: Upcoming reservations are listed
  - Action: View the "Upcoming Reservations" section
  - Expected: The newly created reservation appears in the list

- [X] FT-08: An upcoming reservation can be cancelled
  - Action: Click the cancel action (e.g., "Cancel") on a listed reservation
  - Expected: The reservation is removed from the upcoming reservations list

## Constraint
- [ ] CS-01: Reservation cannot be submitted without a selected resource
  - Action: Leave resource unselected, fill other fields, and click submit
  - Expected: Submission is blocked and a resource-required message is shown
  - Bug Report:
    - Issue: Missing validation state / action not executable — no resource-required message element exists
    - Actual: With no resource selected, the right panel renders only the "Select a Resource" placeholder and the "Your Reservations" list. No Purpose/Date/Time inputs and no "Reserve" button are rendered at all (submission is impossible by design), so the described action ("fill other fields and click submit") cannot be performed, and no resource-required message is ever displayed.

- [X] CS-02: Reservation cannot be submitted without a date or time
  - Action: Leave date and/or time empty, fill other fields, and click submit
  - Expected: Submission is blocked and a date/time-required message is shown

- [X] CS-03: Reservation cannot be submitted with an empty purpose/title
  - Action: Leave the purpose/title field empty, fill other fields, and click submit
  - Expected: Submission is blocked and a purpose-required message is shown

- [ ] CS-04: A resource cannot be double-booked for the same date and time
  - Action: Reserve a resource for a date/time, then attempt a second reservation for the same resource, date, and time
  - Expected: The second submission is rejected with a conflict/availability message
  - Bug Report:
    - Issue: Double-booking allowed — no conflict/availability check
    - Actual: "Skyline Conference Room" was first booked for Nov 9, 2026, 14:00–15:00. A second reservation for the same resource, same date, and same time was accepted with the toast "Reservation created! Skyline Conference Room booked for Nov 9, 2026"; the list then showed two overlapping entries ("Team sync" and "Conflict test"). No conflict/availability message was shown.

- [ ] CS-05: A past date or time cannot be reserved
  - Action: Attempt to select a past date or time and submit
  - Expected: The past selection is rejected or unavailable
  - Bug Report:
    - Issue: Past time accepted (partial enforcement — past dates are disabled, past times are not)
    - Actual: Past dates in the calendar (Nov 1–7) are correctly disabled/unselectable, but a reservation for the current day (Nov 8, 2026) with a start time of 08:00–09:00 was accepted ("Reservation created! Innovation Lab booked for Nov 8, 2026"), even though the time (08:00) was already in the past (current time was 13:15). No validation error was shown.

## Interaction
- [X] IX-01: Success confirmation appears after a valid submission
  - Action: Submit a valid reservation
  - Expected: A success message/toast confirms the reservation was created

- [X] IX-02: The form resets after a successful submission
  - Action: Submit a valid reservation and observe the form
  - Expected: Input fields are cleared/reset for the next entry

- [ ] IX-03: Cancelling a reservation gives feedback
  - Action: Cancel a listed reservation
  - Expected: A confirmation prompt or message indicates the cancellation succeeded
  - Bug Report:
    - Issue: Silent cancellation — no confirmation prompt or feedback message
    - Actual: Clicking the cancel (trash icon) button removed the reservation from the list immediately, reverting to "No upcoming reservations", but no confirmation dialog (no native dialog, no `role="dialog"`/`role="alertdialog"`) and no success toast (`role="status"` list stayed empty) was shown.

## Content
- [X] CT-01: Resource list content matches the reservation theme
  - Action: Review the resource list entries
  - Expected: All entries are office resources (meeting rooms, projectors, shared workstations) with no unrelated items

- [X] CT-02: Reservation entries display the correct details
  - Action: Review a reservation in the upcoming reservations list
  - Expected: It shows the resource name, date/time, and the entered purpose/title accurately

---

### Summary

| ID | Result | Note |
|----|--------|------|
| FT-01 … FT-08 | PASS | Core reservation lifecycle works (list, select, date, time, purpose, submit, list, cancel) |
| CS-01 | **FAIL** | No resource-required message; form/submit does not exist without a selected resource |
| CS-02 | PASS | "Please select a date" toast blocks submission |
| CS-03 | PASS | "Please enter a title" toast blocks submission |
| CS-04 | **FAIL** | Double-booking of same resource/date/time is accepted |
| CS-05 | **FAIL** | Past time (today 08:00) is accepted; past dates are correctly disabled |
| IX-01 | PASS | Success toast shown |
| IX-02 | PASS | Form closes/resets after submit |
| IX-03 | **FAIL** | Cancellation gives no prompt or feedback |
| CT-01 | PASS | Resources are on-theme |
| CT-02 | PASS | Reservation shows title, resource, date, and time correctly |

**Defects found:** CS-04 (double-booking), CS-05 (past time accepted), IX-03 (silent cancellation), and CS-01 (no resource-required message / non-executable action).