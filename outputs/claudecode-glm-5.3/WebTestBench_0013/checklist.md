# Test Checklist

## Functionality

- [ ] FT-01: User can save preferred working hours in the personal availability profile
  - Action: Open the availability profile, set preferred working hours (e.g., start 09:00, end 17:00), click "Save".
  - Expected: Profile saves and 09:00–17:00 is shown as the saved preferred working hours.

- [ ] FT-02: User can save typical break times in the profile
  - Action: In the profile, set a typical break window (e.g., 12:00–13:00), click "Save".
  - Expected: The break window is saved and displayed in the profile.

- [ ] FT-03: User can save days they never meet
  - Action: In the profile, mark days as never-meet (e.g., Saturday and Sunday), click "Save".
  - Expected: The selected days are saved and listed as never-meet days in the profile.

- [ ] FT-04: Creating a meeting with a chosen date range auto-generates suggested slots
  - Action: Create a meeting with a title and a chosen date range (e.g., next Monday through Friday).
  - Expected: The meeting is created and suggested time slots are automatically generated, every slot falling inside the chosen date range and showing its date and start–end time.

- [ ] FT-05: Organizer can add a participant by name and email
  - Action: As organizer, enter a participant's name and email and click "Add Participant".
  - Expected: The participant appears in the meeting's participant list.

- [ ] FT-06: Suggested slots respect all known participants' stated preferences
  - Action: View suggestions for a meeting that includes default participants who have profiles (with working hours, breaks, and never-meet days) within the range.
  - Expected: Every suggested slot lies inside each known participant's working hours and avoids their break windows and never-meet days.

- [ ] FT-07: Unknown participants are handled with generic business-hour slots
  - Action: Add a participant by name/email who has no profile (unknown), then view the meeting's suggested slots.
  - Expected: That participant's availability is treated as generic business hours (weekdays, e.g., 09:00–17:00) and suggestions reflect those hours, not any personal profile.

- [ ] FT-08: Participant can adjust availability per meeting, marking slots "Preferred" or "Last resort"
  - Action: Open a default meeting as one of its participants, mark one suggested slot "Preferred" and a different slot "Last resort", save.
  - Expected: Both markings are saved on that meeting and visible on the respective slots.

- [ ] FT-09: Organizer sees a ranked list of candidate times
  - Action: As organizer, open the candidate times view for a meeting whose participants have marked slots.
  - Expected: Candidate times are listed in ranked order (best score first) based on participant markings and preferences.

- [ ] FT-10: Organizer can confirm one candidate time
  - Action: As organizer, click "Confirm" on one candidate time in the ranked list.
  - Expected: The selected time is recorded as the meeting's confirmed time.

- [ ] FT-11: Organizer can reopen a confirmed meeting and select a different time
  - Action: On a confirmed meeting, click "Reopen", then confirm a different candidate time.
  - Expected: The meeting returns to the scheduling state and the new time becomes the confirmed time.

## Constraint

- [ ] CS-01: Working hours with end time before start time are rejected
  - Action: In the profile, set working hours start 17:00 / end 09:00, click "Save".
  - Expected: Save is blocked with a validation error and the invalid hours are not stored.

- [ ] CS-02: Participant cannot be added without a name and a valid email
  - Action: Try adding a participant with an empty name, then with an invalid email ("not-an-email").
  - Expected: Both attempts are blocked with errors; no participant entry is created.

- [ ] CS-03: Date range with end date before start date is rejected
  - Action: Create a meeting with an end date earlier than the start date (or leave the range empty).
  - Expected: Creation is blocked with a validation error; no meeting and no suggested slots are generated.

- [ ] CS-04: Confirmed time cannot be changed without reopening the meeting
  - Action: On a confirmed meeting, attempt to select or confirm another candidate time before clicking "Reopen".
  - Expected: The confirmed time remains unchanged; selecting a new time is possible only after the meeting is reopened.

## Interaction

- [ ] IX-01: Success feedback appears after saving the profile
  - Action: Edit any profile field (e.g., working hours) and click "Save".
  - Expected: A success message (e.g., "Profile saved") appears on screen.

- [ ] IX-02: Ranked candidate list updates after a participant changes a marking
  - Action: While the organizer views the ranked list, have a participant change a slot's marking (e.g., to "Preferred"), then reopen the candidate list.
  - Expected: Scores and rank order update to reflect the new marking, without creating a new meeting.

- [ ] IX-03: Confirmation feedback appears after a time is confirmed
  - Action: As organizer, confirm one candidate time.
  - Expected: A success confirmation appears and the meeting status changes to "Confirmed" with the confirmed time shown.

## Content

- [ ] CT-01: Ranked list indicates conflicts, partial overlaps, and tied scores
  - Action: Inspect the ranked candidate list on a meeting containing conflicting and partially overlapping participant availability.
  - Expected: Each candidate shows the correct indicators — conflict marks, partial-overlap marks, and tied-score marks where two candidates have equal scores — matching the participants' actual availability.

- [ ] CT-02: Participant names and emails are displayed exactly as entered
  - Action: Compare each participant's displayed name and email in the participant list against the values entered when added.
  - Expected: Every name and email matches exactly, with no truncation or alteration.