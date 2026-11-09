All tests are complete (75 slots for the unknown-participant meeting: Mon–Fri, 9:00 AM–5:00 PM — generic business hours ✓). Here is the full checklist with updated statuses:

# Test Result

## Functionality
- [X] FT-01: Availability profile stores the user's preferred working hours.
  - Action: Open the availability profile, set preferred working hours (e.g., 09:00–17:00), and save.
  - Expected: The profile shows the working hours exactly as entered.

- [X] FT-02: Availability profile stores typical break times.
  - Action: Add a typical break time (e.g., 12:00–13:00) in the availability profile and save.
  - Expected: The break time is saved and listed in the profile.

- [X] FT-03: Availability profile stores days the user never meets.
  - Action: Mark days as never-meet days (e.g., Saturday, Sunday) in the availability profile and save.
  - Expected: The selected days are saved and displayed as never-meet days.

- [X] FT-04: Creating a meeting auto-generates suggested time slots within the chosen date range.
  - Action: Create a meeting with a title and a start/end date range.
  - Expected: A list of suggested time slots is generated automatically, and every slot falls on a date inside the chosen range.

- [X] FT-05: Organizer can add participants by name and email.
  - Action: Enter a participant's name and email and add them to the meeting.
  - Expected: The participant appears in the meeting's participant list showing the entered name and email.

- [ ] FT-06: Known participants (ones with an availability profile) shape the suggested slots.
  - Action: Create a meeting and add a participant from the app's default data who already has an availability profile with restrictive preferences (e.g., working hours 10:00–15:00).
  - Expected: Every suggested slot conforms to that participant's saved preferences (e.g., all slots lie within 10:00–15:00).
  - Bug Report:
    - Issue: Suggested Slots Violate Participant's Saved Break Preferences
    - Actual: With known participant Jordan Chen (saved preferences: working hours 10:00–18:00, break 13:00–14:00), the generated slots "Mon, Nov 9 • 12:30 PM - 1:30 PM", "Mon, Nov 9 • 1:00 PM - 2:00 PM", and "Mon, Nov 9 • 1:30 PM - 2:30 PM" overlap his saved break time (the app itself flags them "3 conflicts", "2 conflicts", "2 conflicts"). Working hours were respected (all slots lie within 10:00 AM–5:00 PM), but not every suggested slot conforms to that participant's saved preferences.

- [X] FT-07: Unknown participants (no availability profile) fall back to generic business-hour slots.
  - Action: Create a meeting whose participant is a name/email not present in the app (no profile).
  - Expected: Suggested slots are generic business-hour slots (weekday daytime) instead of personalized preferences.

- [X] FT-08: Participants can adjust availability per meeting with "preferred" and "last resort" marks.
  - Action: As a participant, open the meeting and mark one suggested slot "preferred" and another "last resort".
  - Expected: Both marks are saved and shown on the corresponding slots for that meeting.

- [X] FT-09: Organizer sees candidate times ranked best-first with scores.
  - Action: Open the meeting's candidate time list as the organizer.
  - Expected: Candidate slots are listed in ranked order (best score first) with a visible score for each.

- [X] FT-10: Organizer can confirm one candidate time.
  - Action: Select a candidate time and confirm it for the meeting.
  - Expected: The meeting is confirmed and displays the selected time as the meeting time.

- [X] FT-11: Organizer can reopen the meeting and select a different time.
  - Action: Reopen the confirmed meeting and confirm a different candidate time.
  - Expected: The meeting's confirmed time changes to the newly selected time.

## Constraint
- [X] CS-01: No suggested slot falls on a never-meet day.
  - Action: Review every suggested slot for a meeting whose date range includes a never-meet day from an applied profile.
  - Expected: No slot is offered on that day.

- [X] CS-02: No suggested slot falls outside preferred working hours.
  - Action: Compare every suggested slot against the working hours in the profiles applied to the meeting.
  - Expected: Every slot starts and ends within the preferred working hours.

- [ ] CS-03: No suggested slot overlaps a typical break time.
  - Action: Compare every suggested slot against the break times in the profiles applied to the meeting.
  - Expected: No slot overlaps any break time.
  - Bug Report:
    - Issue: Suggested Slots Overlap Saved Break Times (Constraint Violation)
    - Actual: Suggested slots such as "Mon, Nov 9 • 11:30 AM - 12:30 PM" and "Mon, Nov 9 • 12:00 PM - 1:00 PM" overlap the profile's 12:00–13:00 break, and "Mon, Nov 9 • 1:00 PM - 2:00 PM" overlaps the 13:00–14:00 break. These slots are offered anyway — the app flags them "1 conflict", "2 conflicts", "3 conflicts" on their ranked entries, confirming the overlap.

- [ ] CS-04: A participant cannot be added with a missing or invalid name/email.
  - Action: Attempt to add a participant with an empty name, an empty email, or a malformed email (e.g., "user@"), then click Add.
  - Expected: The participant is not added and a validation error is shown.
  - Bug Report:
    - Issue: Insufficient Email Validation on Participant Form
    - Actual: Entering Name "Bad Email" with the malformed email "user@" and clicking Add Participant adds the person to the meeting's participant list ("Bad Email / user@ / External") with no validation error. (The empty name+email case is correctly rejected with "Please enter both name and email", and empty name with a valid email is not added — but the malformed email is accepted.)

- [ ] CS-05: The same participant cannot be added twice.
  - Action: Add a participant, then try to add the same email again (with any name).
  - Expected: The duplicate is rejected and the participant list contains that person only once.
  - Bug Report:
    - Issue: Duplicate Participant Accepted
    - Actual: Via the meeting page's "Add Participant" dialog, adding "Jordan Dup" with the already-present email jordan.chen@company.com succeeds — the participant list then contains both "Jordan Chen / jordan.chen@company.com" and "Jordan Dup / jordan.chen@company.com" (same email twice), with no duplicate rejection. (The create-meeting wizard does reject duplicates with "This participant is already added", but the meeting page's Add dialog does not, so the constraint is not enforced.)

- [X] CS-06: A confirmed meeting's time cannot be changed without reopening it.
  - Action: While the meeting is confirmed, attempt to apply a different candidate time without using Reopen.
  - Expected: The change is blocked; only reopening the meeting enables selecting a different time.

## Interaction
- [X] IX-01: Ranked candidate list updates when a participant's availability changes.
  - Action: As a participant, change a slot mark (e.g., set a slot to "preferred"), then view the organizer's ranked list for the same meeting.
  - Expected: Scores and ranking in the list are recalculated and displayed to reflect the change, without recreating the meeting.

## Content
- [X] CT-01: Per-meeting availability marks are labeled "preferred" and "last resort".
  - Action: Open the per-meeting availability controls on any suggested slot.
  - Expected: The two mark options are labeled exactly "preferred" and "last resort".

- [ ] CT-02: Ranked list accurately indicates conflicts, partial overlaps, and tied scores.
  - Action: Inspect ranked entries for a meeting with conflicting, partially matching, and equally scored slots.
  - Expected: Each entry shows its time and score; conflicting entries are flagged as conflicts, partial matches are flagged as partial overlaps, and entries with equal scores are indicated as tied.
  - Bug Report:
    - Issue: Missing Partial-Overlap Indicator in Ranked List
    - Actual: Ranked entries show their time and score and carry "1/2/3 conflicts" and "Tied" flags correctly, but no partial-overlap flag exists in any meeting inspected ("QA Known Meeting", "QA Unknown Meeting", "Q4 Planning Session", "Design Review"). Partially-matching slots are never generated (slots are clamped to every profile's full working hours) and no "partial overlap" indicator is ever rendered, so the ranked list cannot indicate partial overlaps as required.