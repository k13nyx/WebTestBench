# Test Checklist

## Functionality
- [ ] FT-01: Users can save preferred working hours in their availability profile.
  - Action: Open the availability profile and set a preferred working hours range (e.g., 09:00–17:00), then save.
  - Expected: The profile saves and displays the entered working hours on reload.

- [ ] FT-02: Users can save typical break times and "days they never meet."
  - Action: Add a break time (e.g., 12:00–13:00) and mark at least one weekday as a never-meet day, then save.
  - Expected: Both the break time and the never-meet day persist and are shown in the profile.

- [ ] FT-03: Creating a meeting within a chosen date range generates suggested time slots.
  - Action: Create a meeting, choose a start and end date, and generate suggestions.
  - Expected: A list of suggested time slots within the date range is produced.

- [ ] FT-04: Organizer can add participants by name and email.
  - Action: In the meeting, add a participant with a name and email address.
  - Expected: The participant appears in the meeting's participant list with the correct name and email.

- [ ] FT-05: Suggested slots respect the stated preferences of known participants.
  - Action: Add a known participant whose saved working hours/break/no-meet days are restrictive, then generate suggestions.
  - Expected: Suggested slots fall only within every known participant's working hours and avoid their breaks and never-meet days.

- [ ] FT-06: Unknown participants fall back to generic business-hour slots.
  - Action: Add a participant with no saved profile, then generate suggestions.
  - Expected: Suggestions use generic business-hour slots for that participant rather than a personal profile.

- [ ] FT-07: Participants can adjust availability per meeting and mark slots "preferred" or "last resort."
  - Action: As a participant, open the meeting, mark one slot as "preferred" and another as "last resort."
  - Expected: The chosen slots display the assigned "preferred"/"last resort" labels for that meeting only.

- [ ] FT-08: Organizer can see a ranked list of candidate times.
  - Action: Generate suggestions and open the candidate times list.
  - Expected: Candidate times are listed in ranked order by score.

- [ ] FT-09: Organizer can confirm one time for the meeting.
  - Action: Select a candidate time and confirm it.
  - Expected: The meeting is set to that confirmed time and shows a confirmed status.

- [ ] FT-10: Organizer can reopen the meeting and select a different time.
  - Action: Reopen a confirmed meeting, then choose and confirm a different candidate time.
  - Expected: The meeting reopens for time selection and updates to the newly confirmed time.

## Constraint
- [ ] CS-01: Meeting cannot be created without required fields.
  - Action: Attempt to create a meeting leaving the title, date range, or required field empty.
  - Expected: Creation is blocked and a validation message identifies the missing required field.

- [ ] CS-02: Suggested slots never fall on a never-meet day.
  - Action: Generate suggestions for a known participant who marked a weekday as a never-meet day.
  - Expected: No suggested slot occurs on that weekday.

- [ ] CS-03: Suggested slots avoid a known participant's declared break times.
  - Action: Generate suggestions for a known participant with a declared break window.
  - Expected: No suggested slot overlaps the participant's break window.

- [ ] CS-04: Participant cannot be added with a missing or invalid email.
  - Action: Attempt to add a participant with an empty or malformed email address.
  - Expected: The participant is rejected and an email-format error is shown.

- [ ] CS-05: Duplicate participants (same email) are prevented.
  - Action: Add a participant, then add another participant using the same email address.
  - Expected: The duplicate is rejected or blocked and does not create a second entry.

- [ ] CS-06: Empty result is handled when no valid slot exists.
  - Action: Generate suggestions for the smallest possible date range where every candidate is excluded by preferences.
  - Expected: The app shows a clear "no available slots" message instead of an empty or broken list.

## Interaction
- [ ] IX-01: Ranked list indicates conflicts, partial overlaps, and tied scores.
  - Action: Generate candidates with participants whose preferences conflict partially or fully, including two equal-score slots.
  - Expected: The list labels each candidate as full conflict, partial overlap, or tie where applicable.

- [ ] IX-02: Ranking updates when participation changes after reopening.
  - Action: Reopen a meeting, add or remove a participant or change a participant's per-meeting availability, and regenerate.
  - Expected: The ranked candidate list recalculates to reflect the updated participation.

## Content
- [ ] CT-01: Availability profile fields match the scheduling theme.
  - Action: Open the availability profile page.
  - Expected: Fields are labeled for working hours, break times, and never-meet days, with no unrelated content.

- [ ] CT-02: Candidate times display within the chosen date range and use valid times.
  - Action: Inspect the suggested/ranked candidate times.
  - Expected: Each listed time falls within the selected date range and shows a valid, correctly formatted time-of-day.