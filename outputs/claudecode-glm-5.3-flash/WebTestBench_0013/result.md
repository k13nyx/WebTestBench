All testing is complete. Final verification summary: the app runs entirely on in-memory state (confirmed via localStorage being empty and source inspection — everything resets on reload), slot generation flags but does not exclude break conflicts, and the candidate list shows stored order with no rank numbers.

# Test Result

## Functionality
- [ ] FT-01: User can create and save a personal availability profile containing preferred working hours, typical break times, and never-meet days, and the saved values persist after page reload.
  - Action: Open the availability profile page, set working hours (e.g., 09:00–17:00), add a break (e.g., 12:00–13:00), mark a day (e.g., Friday) as "never meet", click "Save Profile", then reload the page.
  - Expected: Profile page shows the saved working hours, break time, and never-meet day unchanged after reload.
  - Bug Report:
    - Issue: Data Not Persisted
    - Actual: "Profile updated successfully" toast appears, but after reload Friday is unchecked again. A valid change (End Time 17:00→18:00) also reverted to 17:00 after reload. App state is in-memory only (localStorage empty) — no profile value persists across reloads.
- [ ] FT-02: Creating a meeting with a date range automatically generates suggested time slots inside that range based on the organizer's profile.
  - Action: Create a new meeting with a date range (e.g., Mon–Wed next week) and a duration, using default organizer profile data.
  - Expected: A list of suggested slots is generated automatically; all slots fall within the chosen date range and inside the organizer's preferred working hours, excluding their break times and never-meet days.
  - Bug Report:
    - Issue: Break-Time Exclusion Missing (slots generated automatically ✓, range/hours respected ✓)
    - Actual: For range Nov 9–11 with organizer break 12:00–13:00, suggested slots "Mon, Nov 9 • 11:30 AM - 12:30 PM", "12:00 PM - 1:00 PM" and "12:30 PM - 1:30 PM" overlap the break. They carry a "1 conflict" badge but are still offered as suggestions.
- [ ] FT-03: When a participant with an existing profile is added (name + email), suggested slots respect that participant's preferences.
  - Action: In a new meeting, add a known participant from the default data (name + email matching an existing profile) whose working hours are e.g. 10:00–16:00 with a never-meet day.
  - Expected: Regenerated suggestions exclude the participant's break times, out-of-hours periods, and never-meet days.
  - Bug Report:
    - Issue: Known-Participant Break Times Not Excluded
    - Actual: Adding Jordan Chen (jordan.chen@company.com, "Known" badge, hours 10:00–18:00, break 13:00–14:00) correctly shifted the slot window to start at 10:00 AM, but slots "1:00 PM - 1:30 PM" and "1:30 PM - 2:00 PM" (inside his 13:00–14:00 break) are still suggested with only a "1 conflict" badge. Never-meet exclusion was verified separately (CS-02).
- [X] FT-04: When a participant without a profile is added, suggestions use generic business-hour slots.
  - Action: In a new meeting, add a participant by name + email that does not match any existing profile.
  - Expected: Suggestions include slots within generic business hours (e.g., 09:00–17:00 weekdays) for that participant; the participant is identifiable as "unknown"/no-profile in the participant list.
- [X] FT-05: A participant can mark a specific suggested slot as "preferred" for that meeting.
  - Action: Open a meeting as a participant, select one suggested slot, and set it to "preferred", then save/submit.
  - Expected: The slot is stored and displayed as "preferred" for that participant in that meeting.
  - (Note: works via deep-link participant response page /meeting/:id/respond/:participantId; no organizer-view link to it. State resets on reload — systemic issue reported in FT-01.)
- [X] FT-06: A participant can mark a specific suggested slot as "last resort" for that meeting.
  - Action: Open a meeting as a participant, select a different slot, set it to "last resort", and save/submit.
  - Expected: The slot is stored and displayed as "last resort" for that participant in that meeting.
- [ ] FT-07: The organizer can view a ranked list of candidate times ordered from best to worst.
  - Action: As organizer, open the candidate times view for a meeting with at least one participant response.
  - Expected: Candidates are displayed as a ranked list (rank 1, 2, 3, …) sorted by score from highest to lowest.
  - Bug Report:
    - Issue: List Not Ranked / Not Sorted on Open
    - Actual: No rank numbers (1, 2, 3…) are displayed anywhere. On simply opening meeting-1 the list shows stored order "85, 90, 60" (Wed 2:00 PM 90 listed after Tue 10:00 AM 85 — neither descending nor ascending). The list only becomes score-sorted (100→85→45) after a participant response triggers re-generation; a plain page load shows the seed order. Header claims "Ranked by availability scores" but the displayed order contradicts it.
- [X] FT-08: The organizer can confirm one candidate time for the meeting.
  - Action: In the candidate list, select the top-ranked slot and click "Confirm" (or equivalent).
  - Expected: The meeting shows the confirmed date/time and a confirmed status.
- [X] FT-09: The organizer can reopen a confirmed meeting and select a different time.
  - Action: Open the confirmed meeting, click "Reopen" (or equivalent), choose a different candidate slot, and confirm again.
  - Expected: The meeting's confirmed time updates to the newly selected slot.

## Constraint
- [ ] CS-01: The profile cannot be saved with invalid working hours (e.g., end time earlier than or equal to start time, or empty required fields).
  - Action: In the profile form, set working hours start 14:00 and end 09:00 (and/or leave a required field empty), then click "Save Profile".
  - Expected: Save is rejected with a clear validation message; no invalid profile is stored.
  - Bug Report:
    - Issue: Missing Form Validation
    - Actual: With Start 14:00 / End 09:00, clicking "Save Changes" shows a success toast "Profile updated successfully" — no validation error is shown. The invalid values do not survive reload, but only because nothing persists at all, not because of validation; the user is told the save succeeded.
- [X] CS-02: No suggested slot falls on a day marked as "never meet" in any known participant's profile (including the organizer's).
  - Action: With a profile whose never-meet day lies inside the meeting date range, generate suggestions.
  - Expected: Zero suggested slots occur on that never-meet day.
  - (Verified twice: organizer-only range Sat Nov 14–Sun Nov 15 → "No time slots available"; range Fri Nov 13–Sat Nov 14 with known participant Taylor Swift (never-meets Fri) → "No time slots available".)
- [ ] CS-03: No suggested slot overlaps a break-time window of a known participant or the organizer.
  - Action: With a break of 12:00–13:00 in a profile, generate suggestions for a range covering that window.
  - Expected: No suggested slot's start or end intersects 12:00–13:00 on any day.
  - Bug Report:
    - Issue: Break-Conflict Slots Still Suggested
    - Actual: Slots intersecting the organizer's 12:00–13:00 break are offered (e.g., "12:00 PM - 12:30 PM", "12:30 PM - 1:00 PM" with "1 conflict"; "11:30 AM - 12:30 PM" also intersects). Jordan's 13:00–14:00 break slots ("1:00 PM - 1:30 PM", "1:30 PM - 2:00 PM", "2 conflicts") are likewise offered. Conflicts are flagged with a badge but never excluded from the suggestions.
- [ ] CS-04: A participant cannot be added with an empty or malformed email address.
  - Action: In the "Add participant" form, enter a name with an invalid email (e.g., "john@" or blank email) and submit.
  - Expected: The participant is not added; an error message identifies the invalid email.
  - Bug Report:
    - Issue: Missing Email Validation
    - Actual: "Test Person" with email "john@" was added successfully — no error message, dialog closed, and the participant appears in the list with the malformed email and an "External" badge.
- [X] CS-05: The organizer cannot confirm a meeting without selecting a candidate time slot.
  - Action: Open the confirmation action with no slot selected.
  - Expected: Confirmation is blocked with a message prompting slot selection; meeting status remains unconfirmed.
  - (Confirmation is per-slot only; a meeting with zero generated slots exposes no Confirm control at all and its status remains "Polling Participants" — confirmation without a selected slot is impossible.)

## Interaction
- [X] IX-01: Saving the availability profile gives immediate success feedback.
  - Action: Fill valid profile data and click "Save Profile".
  - Expected: A visible success indicator (toast/message, e.g., "Profile saved") appears without requiring a page reload.
- [X] IX-02: Marking a slot as "preferred" or "last resort" updates its visual state immediately.
  - Action: As a participant, click the "preferred" then "last resort" control on two different slots.
  - Expected: Each slot immediately shows its badge/highlight (e.g., "Preferred", "Last resort") reflecting the current selection.
- [ ] IX-03: Selecting or hovering a candidate time reveals per-participant availability details for that slot.
  - Action: In the ranked candidate list, click (or hover) one candidate slot.
  - Expected: Detail view shows which participants are available, conflicted, or partially overlapping for that slot.
  - Bug Report:
    - Issue: No Detail View / Unresponsive Slot Row
    - Actual: Clicking the slot row produced no DOM change at all (145 nodes before and after; text identical), and hovering revealed nothing. Only summary badges ("1 preferred", "1 conflict") are visible; no per-participant availability breakdown exists for any slot.
- [X] IX-04: Reopening a confirmed meeting visibly changes its status from confirmed back to open/pending.
  - Action: Click "Reopen" on a confirmed meeting.
  - Expected: Status label changes immediately (e.g., "Confirmed" → "Open"/"Scheduling") and the candidate list becomes selectable again.

## Content
- [X] CT-01: The ranked candidate list explicitly indicates conflicts (a participant is fully unavailable) with a visible label or icon on affected slots.
  - Action: Review the candidate list for a meeting where at least one participant is unavailable at some slots.
  - Expected: Slots where a participant cannot attend display a conflict indicator (e.g., "Conflict" label or warning icon).
- [ ] CT-02: The ranked candidate list distinguishes partial overlaps and tied scores with distinct visible labels.
  - Action: Review the candidate list for a meeting producing a partially-overlapping slot and two slots with equal scores.
  - Expected: Partially overlapping slots are labeled (e.g., "Partial overlap") and equal-score slots are marked as tied (e.g., "Tie" / equal rank noted), visibly distinct from normal slots.
  - Bug Report:
    - Issue: Missing "Partial overlap" Label
    - Actual: Tied scores are correctly marked with a "Tied" badge (e.g., consecutive 100-score slots), but no "Partial overlap" (or any overlap-related) label is rendered anywhere — the UI only shows "N conflict(s)", "N preferred", "N last resort" and "Tied" badges. Slots whose window falls outside a participant's working hours (scored as partial overlaps internally) appear with no distinguishing label.

---
**Systemic observation:** the entire application keeps state in memory only (localStorage is empty); any page reload restores seed data, discarding profile edits, participant responses, confirmations, and newly created meetings. The participant response page is reachable only via a hand-typed deep link (`/meeting/:meetingId/respond/:participantId`) — no UI element links to it.