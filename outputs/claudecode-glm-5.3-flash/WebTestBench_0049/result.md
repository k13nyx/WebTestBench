All tests executed. Here is the complete checklist with results:

# Test Result

## Functionality
- [X] FT-01: Resource list displays reservable resources
  - Action: Open the webpage and view the resource selection area.
  - Expected: A list of resources is shown including at least one meeting room, one projector, and one shared workstation.
- [X] FT-02: User can select a resource from the list
  - Action: Click/tap one resource (e.g., a meeting room) in the list.
  - Expected: The resource becomes visibly selected/highlighted and the selection is reflected in the reservation form.
- [X] FT-03: User can choose a date for the reservation
  - Action: Use the date input to pick a future date (e.g., tomorrow).
  - Expected: The chosen date is accepted and shown in the form.
- [X] FT-04: User can choose a time for the reservation
  - Action: Use the time input(s) to pick a valid time (e.g., 14:00).
  - Expected: The chosen time is accepted and shown in the form.
- [X] FT-05: User can enter a purpose/title and submit a reservation
  - Action: Enter a short title such as "Team sync" and click the submit button (e.g., "Reserve").
  - Expected: The reservation is created successfully (confirmation shown or reservation appears in the list).
- [X] FT-06: New reservation appears in upcoming reservations list
  - Action: Submit a valid reservation, then view the upcoming reservations list.
  - Expected: The new reservation appears with its resource, date, time, and title/purpose.
- [X] FT-07: User can cancel an upcoming reservation
  - Action: Click the cancel/remove control next to one of the user's upcoming reservations.
  - Expected: The reservation is removed from the upcoming list (immediately or after a confirm step).

## Constraint
- [X] CS-01: Cannot submit reservation without a purpose/title
  - Action: Leave the title/purpose field empty and click submit.
  - Expected: Submission is blocked and a validation message is shown (e.g., "Please enter a purpose").
- [X] CS-02: Cannot submit reservation without a date and time
  - Action: Select a resource and title but leave date/time unset, then click submit.
  - Expected: Submission is blocked with a validation message indicating date/time is required.
  - Note: Date unset is blocked with toast "Please select a date". Time fields cannot be left unset (pre-filled with valid defaults 09:00/10:00), so the date-required check is the observable behavior.
- [X] CS-03: Cannot submit reservation without selecting a resource
  - Action: Fill date, time, and title but do not select any resource, then click submit.
  - Expected: Submission is blocked with a message prompting resource selection.
  - Note: Submission without a resource is structurally impossible — the reservation form only renders after a resource is selected, and the form's Cancel button clears selection and closes the form entirely. The empty state displays "Click on a resource card to start booking," prompting resource selection.
- [X] CS-04: Cancel requires confirmation or is not accidental
  - Action: Click cancel on a reservation.
  - Expected: Either a confirmation prompt appears before deletion, or the reservation is removed with no unintended changes to other reservations.
  - Note: Cancellation is immediate (no confirm dialog), but the other reservation ("Q4 Budget Review") remained intact — satisfies the second branch of the expectation.

## Interaction
- [X] IX-01: Submission gives visible success feedback
  - Action: Submit a valid reservation.
  - Expected: A success message, toast, or visible state change confirms the reservation was made.
- [X] IX-02: Invalid submission gives visible error feedback
  - Action: Submit the form with missing required fields.
  - Expected: An error message or highlighted field appears; the page does not silently fail.
- [X] IX-03: Reservation list updates after cancellation
  - Action: Cancel a reservation from the upcoming list.
  - Expected: The list refreshes immediately so the cancelled reservation is no longer visible without a page reload being required.
- [X] IX-04: Selected resource state is visually clear
  - Action: Click different resources one after another in the list.
  - Expected: Only the currently selected resource appears selected/highlighted at any time.
  - Note: Verified via DOM classes (`border-primary`/`bg-primary/5` on exactly one card at a time across Skyline → Focus Pod A → Innovation Lab clicks).

## Content
- [X] CT-01: Reservation list shows complete details per entry
  - Action: View the upcoming reservations list after creating a reservation.
  - Expected: Each entry displays resource name, date, time, and the purpose/title entered by the user.
- [X] CT-02: Resource names and types are relevant to office resources
  - Action: Read the resource list.
  - Expected: All listed items are office resources (meeting rooms, projectors, workstations) with correct labels/types — no unrelated items.
- [X] CT-03: Empty-state message when no upcoming reservations
  - Action: Cancel all reservations (or view list with none existing).
  - Expected: A clear empty-state message is shown (e.g., "No upcoming reservations") instead of a blank or broken area.
- [X] CT-04: Purpose/title text is preserved exactly as entered
  - Action: Create a reservation with a specific title (e.g., "Q4 Budget Review") and check the list.
  - Expected: The displayed title matches the entered text exactly, with no truncation that loses meaning or corruption.

**Summary: 18/18 tests passed.** All functional flows (resource selection, date/time picking, submission, listing, cancellation), all constraints, all interaction feedback, and all content requirements work as expected. Minor observations (not failures): time fields are pre-filled with defaults (09:00–10:00), cancellation is immediate with no confirmation dialog, and resource selection is required to even open the reservation form — each consistent with the checklist's expected behavior.