# Test Checklist

## Functionality
- [ ] FT-01: User can save a personal availability profile with preferred working hours
  - Action: Open the availability profile settings, set preferred working hours (e.g., 09:00–17:00), and save.
  - Expected: The profile displays the saved working hours after saving, and they persist after reloading the page.

- [ ] FT-02: User can record typical break times in their profile
  - Action: In the availability profile, add a break time (e.g., 12:00–13:00) and save.
  - Expected: The break time is listed in the profile and persists after reload.

- [ ] FT-03: User can mark days they never meet
  - Action: In the availability profile, mark one weekday (e.g., Friday) as a "never meet" day and save.
  - Expected: Friday is shown as a never-meet day in the profile and persists after reload.

- [ ] FT-04: Organizer can create a meeting within a chosen date range and receives suggested slots
  - Action: Create a new meeting with a title and a date range (e.g., 2026-11-10 to 2026-11-14).
  - Expected: The meeting is created and a list of suggested time slots is generated within that date range.

- [ ] FT-05: Organizer can add participants by name and email
  - Action: In the meeting, add a participant with a name and email address.
  - Expected: The participant appears in the meeting's participant list with the entered name and email.

- [ ] FT-06: Suggested slots respect the preferences of known participants
  - Action: Add a participant whose email matches an existing profile (profile prefers 09:00–17:00, never meets Friday) and view suggested slots.
  - Expected: All suggested slots fall within 09:00–17:00, avoid the profile's break times, and contain no slots on Friday.

- [ ] FT-07: Unknown participants get generic business-hour slots
  - Action: Add a participant whose email has no profile, then view suggested slots.
  - Expected: Slots for that participant are generated within generic business hours (e.g., 09:00–17:00 on weekdays) rather than any personal profile.

- [ ] FT-08: Participant can adjust availability for a specific meeting
  - Action: As a participant, open the meeting and change availability for one of the suggested slots (e.g., mark it unavailable).
  - Expected: The change is saved for this meeting only and is reflected in the slot list.

- [ ] FT-09: Participant can mark a slot as "preferred"
  - Action: As a participant, mark one suggested slot as "preferred".
  - Expected: The slot is labeled "preferred" and the label persists after reload.

- [ ] FT-10: Participant can mark a slot as "last resort"
  - Action: As a participant, mark one suggested slot as "last resort".
  - Expected: The slot is labeled "last resort" and the label persists after reload.

- [ ] FT-11: Organizer sees a ranked candidate list after participants respond
  - Action: As the organizer, open the meeting's candidate times view.
  - Expected: Candidate times are displayed in ranked (best-first) order with a score for each.

- [ ] FT-12: Organizer can confirm one time for the meeting
  - Action: Select a candidate time and confirm it.
  - Expected: The meeting shows the confirmed time and its status changes to confirmed/scheduled.

- [ ] FT-13: Organizer can reopen a confirmed meeting and pick a different time
  - Action: Open the confirmed meeting, reopen it, and select a different candidate time.
  - Expected: The meeting reopens, the new time can be selected, and confirming updates the meeting to the new time.

## Constraint
- [ ] CS-01: Suggested slots never fall on a participant's never-meet day
  - Action: With a participant whose profile excludes a specific day, generate slots across a date range including that day.
  - Expected: No suggested slot is offered on the excluded day.

- [ ] CS-02: Suggested slots never overlap a participant's break times
  - Action: With a participant who has a break (e.g., 12:00–13:00), generate slots.
  - Expected: No suggested slot overlaps the break window.

- [ ] CS-03: Slot conflict indicators are shown when participants are unavailable
  - Action: Create a meeting where at least one participant is unavailable for a candidate slot.
  - Expected: That candidate is marked as a conflict in the organizer's ranked list.

- [ ] CS-04: Partial overlaps are distinguished from full conflicts
  - Action: Create a situation where a slot only partially overlaps a participant's availability.
  - Expected: The candidate is marked as a partial overlap, not as a full conflict.

- [ ] CS-05: Meeting creation requires a valid date range with participants
  - Action: Attempt to create a meeting with an end date before the start date, or with no participants.
  - Expected: The meeting is not created and an error message explains what is missing or invalid.

## Interaction
- [ ] IX-01: Tied scores are visibly indicated in the ranked list
  - Action: View a ranked list containing at least two candidates with equal scores.
  - Expected: The tied candidates are shown with an explicit tie indicator (e.g., "Tied") and share the same rank or are grouped together.

- [ ] IX-02: UI provides clear feedback when availability or meeting changes are saved
  - Action: Save a profile change, a per-meeting availability change, and a meeting confirmation.
  - Expected: Each action shows immediate visible feedback (e.g., confirmation message or updated state) so the user knows it succeeded.

## Content
- [ ] CT-01: Participant and meeting data displays match what was entered
  - Action: Add a participant "alice@example.com" and a meeting with a specific title and date range; review all views.
  - Expected: Names, emails, titles, dates, break times, and day exclusions are displayed exactly as entered, with no placeholder or mismatched data.