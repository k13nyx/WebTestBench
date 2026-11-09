# Test Checklist

## Functionality
- [ ] FT-01: Organizer can create and save a personal availability profile
  - Action: Open the availability profile editor; set preferred working hours (e.g., 09:00–17:00), typical break times (e.g., 12:00–13:00), and no-meet days (e.g., Friday); click "Save Profile".
  - Expected: Save succeeds; reopening the profile shows all three settings exactly as entered.

- [ ] FT-02: Creating a meeting auto-generates suggested slots within the chosen date range
  - Action: Click "New Meeting", enter a title and a date range spanning at least 3 days, submit.
  - Expected: A list of suggested time slots is generated automatically, all falling inside the chosen range.

- [ ] FT-03: Organizer can add participants by name and email
  - Action: In the meeting's participant section, add two participants (name + email each) via "Add Participant".
  - Expected: Both appear in the participant list with their names and emails.

- [ ] FT-04: Slots for known participants respect all profile preferences
  - Action: Add a participant who has a saved profile with working hours 10:00–16:00 and a break 12:00–13:00; generate slots.
  - Expected: All suggested slots fit inside every known participant's working hours (intersection), not only generic hours.

- [ ] FT-05: Unknown participants receive generic business-hour slots
  - Action: Add a participant with an email that has no profile in the app; generate slots.
  - Expected: Slots for/including that participant use standard business hours (e.g., 09:00–17:00) instead of personal preferences.

- [ ] FT-06: Participant can mark a slot as "Preferred" or "Last Resort"
  - Action: As a participant, open the meeting, adjust availability, mark one slot "Preferred" and another "Last Resort".
  - Expected: Both markers are saved and visibly displayed on those slots.

- [ ] FT-07: Organizer sees a ranked list of candidate times
  - Action: After participants respond, open the organizer's "Candidate Times" view.
  - Expected: A list of candidate times is shown ordered by score (best first).

- [ ] FT-08: Organizer confirms one candidate time
  - Action: In the ranked list, select the top candidate and click "Confirm Time".
  - Expected: The meeting status changes to "Confirmed" and shows the selected date/time.

- [ ] FT-09: Confirmed meeting can be reopened and a different time selected
  - Action: On the confirmed meeting, click "Reopen Meeting", then select a different candidate and confirm again.
  - Expected: The meeting returns to an open state and is re-confirmed with the new time displayed.

## Constraint
- [ ] CS-01: No slots are suggested on a participant's no-meet days
  - Action: Create a meeting whose date range includes Friday; include a known participant whose profile marks Friday as a no-meet day; generate slots.
  - Expected: Zero suggested slots fall on any Friday in the range.

- [ ] CS-02: Slots never overlap known participants' break times
  - Action: Generate slots for a meeting including a participant with break 12:00–13:00.
  - Expected: No suggested slot overlaps 12:00–13:00 on any date.

- [ ] CS-03: Participant addition is blocked for missing or invalid email
  - Action: Enter a name only (no email), then a name with "abc@" as email; click "Add Participant" each time.
  - Expected: Both attempts are rejected with a validation message; no participant is added.

- [ ] CS-04: A meeting cannot be confirmed without exactly one selected time
  - Action: Click "Confirm Time" with no candidate selected.
  - Expected: Confirmation is blocked with a prompt to select a time; meeting stays unconfirmed.

- [ ] CS-05: Candidate times are locked once the meeting is confirmed
  - Action: With the meeting confirmed, try to mark a slot or change the time without reopening.
  - Expected: Editing is disabled/blocked until "Reopen Meeting" is used.

## Interaction
- [ ] IX-01: Ranking updates immediately when participants change availability
  - Action: Note the current order in the ranked list; as a participant, switch a slot from "Preferred" to "Last Resort"; return to the organizer view.
  - Expected: The ranked list reflects the new scores/order without a manual reload error or stale data.

- [ ] IX-02: Confirmation produces visible feedback
  - Action: Confirm a candidate time.
  - Expected: A success message/toast (e.g., "Meeting time confirmed") appears, and the meeting card updates to the confirmed state.

- [ ] IX-03: Reopen control transitions the meeting state visibly
  - Action: Click "Reopen Meeting" on a confirmed meeting.
  - Expected: The UI switches from locked view back to editable candidate list with selection controls enabled.

## Content
- [ ] CT-01: Ranked list labels conflicts, partial overlaps, and tied scores
  - Action: Inspect the organizer's ranked candidate list with varied participant responses.
  - Expected: Each candidate displays conflict or partial-overlap indicators per participant, and equal-scoring candidates are explicitly marked as tied.

- [ ] CT-02: Default data contains both profiled and non-profiled participants
  - Action: Open the app's participant directory / default data on first load.
  - Expected: At least one pre-existing participant with a saved availability profile and at least one recognizable contact without a profile are available for testing.

- [ ] CT-03: Generated slots display complete, relevant date/time content
  - Action: View the suggested slot list for a meeting.
  - Expected: Every slot shows a readable day, date, start–end time (with duration consistent with the meeting), and no placeholder or empty text appears.