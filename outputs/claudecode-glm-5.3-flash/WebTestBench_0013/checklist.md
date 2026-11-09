# Test Checklist

## Functionality
- [ ] FT-01: User can create and save a personal availability profile containing preferred working hours, typical break times, and never-meet days, and the saved values persist after page reload.
  - Action: Open the availability profile page, set working hours (e.g., 09:00–17:00), add a break (e.g., 12:00–13:00), mark a day (e.g., Friday) as "never meet", click "Save Profile", then reload the page.
  - Expected: Profile page shows the saved working hours, break time, and never-meet day unchanged after reload.
- [ ] FT-02: Creating a meeting with a date range automatically generates suggested time slots inside that range based on the organizer's profile.
  - Action: Create a new meeting with a date range (e.g., Mon–Wed next week) and a duration, using default organizer profile data.
  - Expected: A list of suggested slots is generated automatically; all slots fall within the chosen date range and inside the organizer's preferred working hours, excluding their break times and never-meet days.
- [ ] FT-03: When a participant with an existing profile is added (name + email), suggested slots respect that participant's preferences.
  - Action: In a new meeting, add a known participant from the default data (name + email matching an existing profile) whose working hours are e.g. 10:00–16:00 with a never-meet day.
  - Expected: Regenerated suggestions exclude the participant's break times, out-of-hours periods, and never-meet days.
- [ ] FT-04: When a participant without a profile is added, suggestions use generic business-hour slots.
  - Action: In a new meeting, add a participant by name + email that does not match any existing profile.
  - Expected: Suggestions include slots within generic business hours (e.g., 09:00–17:00 weekdays) for that participant; the participant is identifiable as "unknown"/no-profile in the participant list.
- [ ] FT-05: A participant can mark a specific suggested slot as "preferred" for that meeting.
  - Action: Open a meeting as a participant, select one suggested slot, and set it to "preferred", then save/submit.
  - Expected: The slot is stored and displayed as "preferred" for that participant in that meeting.
- [ ] FT-06: A participant can mark a specific suggested slot as "last resort" for that meeting.
  - Action: Open a meeting as a participant, select a different slot, set it to "last resort", and save/submit.
  - Expected: The slot is stored and displayed as "last resort" for that participant in that meeting.
- [ ] FT-07: The organizer can view a ranked list of candidate times ordered from best to worst.
  - Action: As organizer, open the candidate times view for a meeting with at least one participant response.
  - Expected: Candidates are displayed as a ranked list (rank 1, 2, 3, …) sorted by score from highest to lowest.
- [ ] FT-08: The organizer can confirm one candidate time for the meeting.
  - Action: In the candidate list, select the top-ranked slot and click "Confirm" (or equivalent).
  - Expected: The meeting shows the confirmed date/time and a confirmed status.
- [ ] FT-09: The organizer can reopen a confirmed meeting and select a different time.
  - Action: Open the confirmed meeting, click "Reopen" (or equivalent), choose a different candidate slot, and confirm again.
  - Expected: The meeting's confirmed time updates to the newly selected slot.

## Constraint
- [ ] CS-01: The profile cannot be saved with invalid working hours (e.g., end time earlier than or equal to start time, or empty required fields).
  - Action: In the profile form, set working hours start 14:00 and end 09:00 (and/or leave a required field empty), then click "Save Profile".
  - Expected: Save is rejected with a clear validation message; no invalid profile is stored.
- [ ] CS-02: No suggested slot falls on a day marked as "never meet" in any known participant's profile (including the organizer's).
  - Action: With a profile whose never-meet day lies inside the meeting date range, generate suggestions.
  - Expected: Zero suggested slots occur on that never-meet day.
- [ ] CS-03: No suggested slot overlaps a break-time window of a known participant or the organizer.
  - Action: With a break of 12:00–13:00 in a profile, generate suggestions for a range covering that window.
  - Expected: No suggested slot's start or end intersects 12:00–13:00 on any day.
- [ ] CS-04: A participant cannot be added with an empty or malformed email address.
  - Action: In the "Add participant" form, enter a name with an invalid email (e.g., "john@" or blank email) and submit.
  - Expected: The participant is not added; an error message identifies the invalid email.
- [ ] CS-05: The organizer cannot confirm a meeting without selecting a candidate time slot.
  - Action: Open the confirmation action with no slot selected.
  - Expected: Confirmation is blocked with a message prompting slot selection; meeting status remains unconfirmed.

## Interaction
- [ ] IX-01: Saving the availability profile gives immediate success feedback.
  - Action: Fill valid profile data and click "Save Profile".
  - Expected: A visible success indicator (toast/message, e.g., "Profile saved") appears without requiring a page reload.
- [ ] IX-02: Marking a slot as "preferred" or "last resort" updates its visual state immediately.
  - Action: As a participant, click the "preferred" then "last resort" control on two different slots.
  - Expected: Each slot immediately shows its badge/highlight (e.g., "Preferred", "Last resort") reflecting the current selection.
- [ ] IX-03: Selecting or hovering a candidate time reveals per-participant availability details for that slot.
  - Action: In the ranked candidate list, click (or hover) one candidate slot.
  - Expected: Detail view shows which participants are available, conflicted, or partially overlapping for that slot.
- [ ] IX-04: Reopening a confirmed meeting visibly changes its status from confirmed back to open/pending.
  - Action: Click "Reopen" on a confirmed meeting.
  - Expected: Status label changes immediately (e.g., "Confirmed" → "Open"/"Scheduling") and the candidate list becomes selectable again.

## Content
- [ ] CT-01: The ranked candidate list explicitly indicates conflicts (a participant is fully unavailable) with a visible label or icon on affected slots.
  - Action: Review the candidate list for a meeting where at least one participant is unavailable at some slots.
  - Expected: Slots where a participant cannot attend display a conflict indicator (e.g., "Conflict" label or warning icon).
- [ ] CT-02: The ranked candidate list distinguishes partial overlaps and tied scores with distinct visible labels.
  - Action: Review the candidate list for a meeting producing a partially-overlapping slot and two slots with equal scores.
  - Expected: Partially overlapping slots are labeled (e.g., "Partial overlap") and equal-score slots are marked as tied (e.g., "Tie" / equal rank noted), visibly distinct from normal slots.