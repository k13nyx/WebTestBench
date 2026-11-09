# Test Checklist

## Functionality
- [ ] FT-01: Personal profile saves preferred working hours, break times, and never-meet days.
  - Action: Open the profile page. Set working hours to 09:00–17:00, break to 12:00–13:00, and check Saturday and Sunday as never-meet days. Click "Save Profile", then reload the page.
  - Expected: A "Profile saved" message appears. After reload, all four values are still shown as entered.
- [ ] FT-02: Organizer creates a meeting and generates suggested time slots within a date range.
  - Action: Click "New Meeting". Enter title "Sprint Review", start date 2026-11-16, end date 2026-11-20. Click "Generate Suggestions".
  - Expected: A list of suggested slots appears. Every slot falls on or between 2026-11-16 and 2026-11-20.
- [ ] FT-03: Organizer adds a participant by name and email.
  - Action: In "Participants", enter Name "Dana Lee" and Email "dana.lee@example.com" (use default data if Dana exists; otherwise use any valid new entry). Click "Add Participant".
  - Expected: A row shows the name and email exactly as entered.
- [ ] FT-04: Suggested slots for a known participant respect their saved profile.
  - Action: Add a participant whose email already has a saved profile in default data. Set the meeting range to 5 days and click "Generate Suggestions".
  - Expected: No slot falls outside that participant's working hours, inside their break time, or on a never-meet day.
- [ ] FT-05: Participant marks specific slots as "Preferred" or "Last resort" for this meeting.
  - Action: Open the availability view for the participant on this meeting. Click the first slot and choose "Preferred". Click a different slot and choose "Last resort".
  - Expected: Each slot displays its chosen label. The labels persist after switching views and returning.
- [ ] FT-06: Organizer's ranked list orders candidate times by score, highest first.
  - Action: With at least two participants added, open the "Ranked Candidates" list.
  - Expected: Rank 1 has the highest score. Scores are non-increasing down the list.
- [ ] FT-07: Organizer confirms one candidate time.
  - Action: Click the rank 1 candidate, then click "Confirm Time".
  - Expected: The meeting status changes to "Confirmed" and shows the selected date and time. The candidate list is no longer editable.
- [ ] FT-08: Organizer reopens a confirmed meeting and selects a different time.
  - Action: On the confirmed meeting, click "Reopen Meeting". Select a different candidate and click "Confirm Time".
  - Expected: The status returns to "Reopened" while editing, then shows "Confirmed" with the new time. The previous time no longer appears as the confirmed time.
- [ ] FT-09: Suggested slots for an unknown participant use generic business hours.
  - Action: Add a participant with a name and an email that has no saved profile. Click "Generate Suggestions".
  - Expected: Every slot for this participant falls on Monday–Friday, 09:00–17:00, the business-hour window the app displays for unknown participants.

## Constraint
- [ ] CS-01: Suggestions cannot be generated when the end date is before the start date.
  - Action: Set start date 2026-11-20 and end date 2026-11-16. Click "Generate Suggestions".
  - Expected: Generation does not run. An error reads "End date must be on or after start date", and no slots are listed.
- [ ] CS-02: Participant cannot be added with a missing name or an invalid email.
  - Action: Attempt to add a participant with a blank name and a valid email. Then attempt with a valid name and the email "dana.lee@".
  - Expected: Each attempt is blocked with a field-level error ("Name is required" / "Enter a valid email address"). No row is added.
- [ ] CS-03: Profile cannot be saved with a working-hours start time that is not earlier than the end time.
  - Action: On the profile page, set working hours start 17:00 and end 09:00. Click "Save Profile".
  - Expected: Save is blocked with the error "Start time must be before end time". The previously saved hours remain unchanged.
- [ ] CS-04: Per-meeting availability changes do not modify the participant's personal profile.
  - Action: Mark a slot as "Last resort" on one meeting. Open the same participant's profile and then a different meeting.
  - Expected: The profile hours and never-meet days are unchanged. The "Last resort" label does not appear on the other meeting.
- [ ] CS-05: A single slot cannot be marked both "Preferred" and "Last resort" at the same time.
  - Action: Mark a slot "Preferred". Then select the same slot and choose "Last resort".
  - Expected: The slot shows only "Last resort". The "Preferred" label is removed from that slot.

## Interaction
- [ ] IX-01: Hovering over a candidate row shows each participant's availability for that slot.
  - Action: Move the mouse over any candidate row in "Ranked Candidates" and hold for one second.
  - Expected: A tooltip lists each participant by name with "Available", "Preferred", "Last resort", or "Unavailable" next to their name.
- [ ] IX-02: Removing a participant from a confirmed meeting shows a reopen notice.
  - Action: On a confirmed meeting, click "Remove" next to a participant and confirm the dialog.
  - Expected: A banner reads "Participants changed. Reopen the meeting to select a different time." The meeting status stays "Confirmed" until reopened.

## Content
- [ ] CT-01: Candidate rows are labeled "Conflict" or "Partial overlap" accurately.
  - Action: Generate suggestions for a meeting with at least three participants whose availability differs. Compare each row's label against each participant's availability.
  - Expected: A row labeled "Conflict" has at least one unavailable participant. A row labeled "Partial overlap" has some but not all participants available. Rows with all available have neither label.
- [ ] CT-02: Tied candidate scores are shown with equal scores and a "Tie" marker.
  - Action: Generate suggestions for a meeting where at least two candidate slots have identical scores (for example, two participants with identical profile hours).
  - Expected: Tied rows show the same numeric score and both display "Tie". Non-tied rows do not display "Tie".
- [ ] CT-03: Each participant row shows the correct source tag.
  - Action: Add one participant with a saved profile and one without. View the participant list.
  - Expected: The profile participant shows "Profile found". The other shows "No profile (business hours)".
- [ ] CT-04: Confirmed meeting summary matches the selected candidate exactly.
  - Action: Confirm a candidate with a specific date and time. Read the meeting summary.
  - Expected: The title, date, start time, and end time match the confirmed candidate row exactly.