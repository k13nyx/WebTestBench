# Test Checklist

## Functionality
- [ ] FT-01: Availability profile stores the user's preferred working hours.
  - Action: Open the availability profile, set preferred working hours (e.g., 09:00–17:00), and save.
  - Expected: The profile shows the working hours exactly as entered.

- [ ] FT-02: Availability profile stores typical break times.
  - Action: Add a typical break time (e.g., 12:00–13:00) in the availability profile and save.
  - Expected: The break time is saved and listed in the profile.

- [ ] FT-03: Availability profile stores days the user never meets.
  - Action: Mark days as never-meet days (e.g., Saturday, Sunday) in the availability profile and save.
  - Expected: The selected days are saved and displayed as never-meet days.

- [ ] FT-04: Creating a meeting auto-generates suggested time slots within the chosen date range.
  - Action: Create a meeting with a title and a start/end date range.
  - Expected: A list of suggested time slots is generated automatically, and every slot falls on a date inside the chosen range.

- [ ] FT-05: Organizer can add participants by name and email.
  - Action: Enter a participant's name and email and add them to the meeting.
  - Expected: The participant appears in the meeting's participant list showing the entered name and email.

- [ ] FT-06: Known participants (ones with an availability profile) shape the suggested slots.
  - Action: Create a meeting and add a participant from the app's default data who already has an availability profile with restrictive preferences (e.g., working hours 10:00–15:00).
  - Expected: Every suggested slot conforms to that participant's saved preferences (e.g., all slots lie within 10:00–15:00).

- [ ] FT-07: Unknown participants (no availability profile) fall back to generic business-hour slots.
  - Action: Create a meeting whose participant is a name/email not present in the app (no profile).
  - Expected: Suggested slots are generic business-hour slots (weekday daytime) instead of personalized preferences.

- [ ] FT-08: Participants can adjust availability per meeting with "preferred" and "last resort" marks.
  - Action: As a participant, open the meeting and mark one suggested slot "preferred" and another "last resort".
  - Expected: Both marks are saved and shown on the corresponding slots for that meeting.

- [ ] FT-09: Organizer sees candidate times ranked best-first with scores.
  - Action: Open the meeting's candidate time list as the organizer.
  - Expected: Candidate slots are listed in ranked order (best score first) with a visible score for each.

- [ ] FT-10: Organizer can confirm one candidate time.
  - Action: Select a candidate time and confirm it for the meeting.
  - Expected: The meeting is confirmed and displays the selected time as the meeting time.

- [ ] FT-11: Organizer can reopen the meeting and select a different time.
  - Action: Reopen the confirmed meeting and confirm a different candidate time.
  - Expected: The meeting's confirmed time changes to the newly selected time.

## Constraint
- [ ] CS-01: No suggested slot falls on a never-meet day.
  - Action: Review every suggested slot for a meeting whose date range includes a never-meet day from an applied profile.
  - Expected: No slot is offered on that day.

- [ ] CS-02: No suggested slot falls outside preferred working hours.
  - Action: Compare every suggested slot against the working hours in the profiles applied to the meeting.
  - Expected: Every slot starts and ends within the preferred working hours.

- [ ] CS-03: No suggested slot overlaps a typical break time.
  - Action: Compare every suggested slot against the break times in the profiles applied to the meeting.
  - Expected: No slot overlaps any break time.

- [ ] CS-04: A participant cannot be added with a missing or invalid name/email.
  - Action: Attempt to add a participant with an empty name, an empty email, or a malformed email (e.g., "user@"), then click Add.
  - Expected: The participant is not added and a validation error is shown.

- [ ] CS-05: The same participant cannot be added twice.
  - Action: Add a participant, then try to add the same email again (with any name).
  - Expected: The duplicate is rejected and the participant list contains that person only once.

- [ ] CS-06: A confirmed meeting's time cannot be changed without reopening it.
  - Action: While the meeting is confirmed, attempt to apply a different candidate time without using Reopen.
  - Expected: The change is blocked; only reopening the meeting enables selecting a different time.

## Interaction
- [ ] IX-01: Ranked candidate list updates when a participant's availability changes.
  - Action: As a participant, change a slot mark (e.g., set a slot to "preferred"), then view the organizer's ranked list for the same meeting.
  - Expected: Scores and ranking in the list are recalculated and displayed to reflect the change, without recreating the meeting.

## Content
- [ ] CT-01: Per-meeting availability marks are labeled "preferred" and "last resort".
  - Action: Open the per-meeting availability controls on any suggested slot.
  - Expected: The two mark options are labeled exactly "preferred" and "last resort".

- [ ] CT-02: Ranked list accurately indicates conflicts, partial overlaps, and tied scores.
  - Action: Inspect ranked entries for a meeting with conflicting, partially matching, and equally scored slots.
  - Expected: Each entry shows its time and score; conflicting entries are flagged as conflicts, partial matches are flagged as partial overlaps, and entries with equal scores are indicated as tied.