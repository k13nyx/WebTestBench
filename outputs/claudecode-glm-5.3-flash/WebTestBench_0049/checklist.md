# Test Checklist

## Functionality
- [ ] FT-01: Resource list displays reservable resources
  - Action: Open the webpage and view the resource selection area.
  - Expected: A list of resources is shown including at least one meeting room, one projector, and one shared workstation.
- [ ] FT-02: User can select a resource from the list
  - Action: Click/tap one resource (e.g., a meeting room) in the list.
  - Expected: The resource becomes visibly selected/highlighted and the selection is reflected in the reservation form.
- [ ] FT-03: User can choose a date for the reservation
  - Action: Use the date input to pick a future date (e.g., tomorrow).
  - Expected: The chosen date is accepted and shown in the form.
- [ ] FT-04: User can choose a time for the reservation
  - Action: Use the time input(s) to pick a valid time (e.g., 14:00).
  - Expected: The chosen time is accepted and shown in the form.
- [ ] FT-05: User can enter a purpose/title and submit a reservation
  - Action: Enter a short title such as "Team sync" and click the submit button (e.g., "Reserve").
  - Expected: The reservation is created successfully (confirmation shown or reservation appears in the list).
- [ ] FT-06: New reservation appears in upcoming reservations list
  - Action: Submit a valid reservation, then view the upcoming reservations list.
  - Expected: The new reservation appears with its resource, date, time, and title/purpose.
- [ ] FT-07: User can cancel an upcoming reservation
  - Action: Click the cancel/remove control next to one of the user's upcoming reservations.
  - Expected: The reservation is removed from the upcoming list (immediately or after a confirm step).

## Constraint
- [ ] CS-01: Cannot submit reservation without a purpose/title
  - Action: Leave the title/purpose field empty and click submit.
  - Expected: Submission is blocked and a validation message is shown (e.g., "Please enter a purpose").
- [ ] CS-02: Cannot submit reservation without a date and time
  - Action: Select a resource and title but leave date/time unset, then click submit.
  - Expected: Submission is blocked with a validation message indicating date/time is required.
- [ ] CS-03: Cannot submit reservation without selecting a resource
  - Action: Fill date, time, and title but do not select any resource, then click submit.
  - Expected: Submission is blocked with a message prompting resource selection.
- [ ] CS-04: Cancel requires confirmation or is not accidental
  - Action: Click cancel on a reservation.
  - Expected: Either a confirmation prompt appears before deletion, or the reservation is removed with no unintended changes to other reservations.

## Interaction
- [ ] IX-01: Submission gives visible success feedback
  - Action: Submit a valid reservation.
  - Expected: A success message, toast, or visible state change confirms the reservation was made.
- [ ] IX-02: Invalid submission gives visible error feedback
  - Action: Submit the form with missing required fields.
  - Expected: An error message or highlighted field appears; the page does not silently fail.
- [ ] IX-03: Reservation list updates after cancellation
  - Action: Cancel a reservation from the upcoming list.
  - Expected: The list refreshes immediately so the cancelled reservation is no longer visible without a page reload being required.
- [ ] IX-04: Selected resource state is visually clear
  - Action: Click different resources one after another in the list.
  - Expected: Only the currently selected resource appears selected/highlighted at any time.

## Content
- [ ] CT-01: Reservation list shows complete details per entry
  - Action: View the upcoming reservations list after creating a reservation.
  - Expected: Each entry displays resource name, date, time, and the purpose/title entered by the user.
- [ ] CT-02: Resource names and types are relevant to office resources
  - Action: Read the resource list.
  - Expected: All listed items are office resources (meeting rooms, projectors, workstations) with correct labels/types — no unrelated items.
- [ ] CT-03: Empty-state message when no upcoming reservations
  - Action: Cancel all reservations (or view list with none existing).
  - Expected: A clear empty-state message is shown (e.g., "No upcoming reservations") instead of a blank or broken area.
- [ ] CT-04: Purpose/title text is preserved exactly as entered
  - Action: Create a reservation with a specific title (e.g., "Q4 Budget Review") and check the list.
  - Expected: The displayed title matches the entered text exactly, with no truncation that loses meaning or corruption.