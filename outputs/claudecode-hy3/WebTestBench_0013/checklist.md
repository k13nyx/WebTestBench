# Test Checklist

## Functionality
- [ ] FT-01: User can maintain a personal availability profile
  - Action: Open the availability profile, set preferred working hours, add a typical break time, select days you never meet, then click Save.
  - Expected: Profile saves and all settings persist (reloading shows the same values).

- [ ] FT-02: Organizer can create a meeting with a chosen date range
  - Action: Create a new meeting and specify a start date and end date for the date range, then generate.
  - Expected: A meeting is created and displays the chosen date range.

- [ ] FT-03: App auto-generates suggested time slots within the date range
  - Action: After creating a meeting with a date range, view the suggested slots.
  - Expected: Time slot suggestions are generated that fall within the chosen date range.

- [ ] FT-04: Organizer can add participants by name and email
  - Action: In the meeting, enter a participant's name and email and click Add.
  - Expected: The participant appears in the participant list with the entered name and email.

- [ ] FT-05: Known participants' preferences are respected in suggestions
  - Action: Add a participant who has a saved profile and generate suggestions.
  - Expected: Suggested slots respect that participant's stated working hours, breaks, and days-never-meet.

- [ ] FT-06: Unknown participants use generic business-hour slots
  - Action: Add a participant with no saved profile and generate suggestions.
  - Expected: Suggested slots for that participant use generic business hours only.

- [ ] FT-07: Participants can adjust availability per meeting (preferred / last resort)
  - Action: As a participant, open the meeting and mark one slot "preferred" and another "last resort".
  - Expected: Slots are tagged "preferred"/"last resort" and saved for this meeting only.

- [ ] FT-08: Organizer can confirm one candidate time
  - Action: In the ranked candidate list, select a candidate time and click Confirm.
  - Expected: The selected time is confirmed and recorded as the meeting time.

- [ ] FT-09: Organizer can reopen a meeting and pick a different time
  - Action: Reopen a confirmed meeting, select a different candidate time, and confirm.
  - Expected: Meeting returns to editable state and the newly selected time replaces the previous confirmed time.

## Constraint
- [ ] CS-01: No slots on days the user never meets
  - Action: With a profile marking certain days as "never meet," generate suggestions.
  - Expected: No suggested slot falls on a day marked as never meet.

- [ ] CS-02: Slots respect working hours and exclude breaks (known participants)
  - Action: With profile working hours and break times set, generate suggestions for a known participant.
  - Expected: No suggested slot falls outside working hours or overlaps a break time.

- [ ] CS-03: Unknown participants never inherit profile preferences
  - Action: Add an unknown participant and review their suggested slots.
  - Expected: Slots use generic business hours and do not apply any profile-based preference.

- [ ] CS-04: Per-meeting adjustments do not overwrite the global profile
  - Action: Adjust a participant's availability for a meeting, then open their global profile.
  - Expected: The saved global profile is unchanged by the per-meeting adjustment.

- [ ] CS-05: Confirmed time cannot change without reopening
  - Action: With a meeting confirmed, attempt to change the time without reopening.
  - Expected: The time cannot be changed until the meeting is reopened.

## Interaction
- [ ] IX-01: Success confirmation after saving profile
  - Action: Save the availability profile.
  - Expected: A success toast/message appears confirming the profile was saved.

- [ ] IX-02: Ranked list indicates conflict, partial overlap, and tied scores
  - Action: View the ranked candidate list with mixed participant availability.
  - Expected: Each candidate clearly shows conflict, partial overlap, or tied-score status.

- [ ] IX-03: Availability changes update the ranking in real time
  - Action: Mark a slot "preferred" or "last resort" for a participant.
  - Expected: The ranked list re-ranks immediately without a page reload.

## Content
- [ ] CT-01: Profile form shows correct field labels
  - Action: Open the availability profile form.
  - Expected: Fields are labeled "Preferred working hours," "Typical break times," and "Days they never meet."

- [ ] CT-02: Ranked list shows accurate participant and status content
  - Action: Review the ranked candidate list.
  - Expected: Each participant's name and email plus conflict/overlap/tie status text match actual availability.

- [ ] CT-03: Meeting creation shows labeled date range inputs
  - Action: Open the meeting creation screen.
  - Expected: Date range inputs are clearly labeled (e.g., "Start date," "End date") and relevant to scheduling.