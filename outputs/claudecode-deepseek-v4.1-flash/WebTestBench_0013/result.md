I have completed all checks. Here is the full checklist with results.

# Test Result

## Functionality

- [ ] FT-01: Users can save preferred working hours in their availability profile.
  - Action: Open the availability profile and set a preferred working hours range (e.g., 09:00–17:00), then save.
  - Expected: The profile saves and displays the entered working hours on reload.
  - Bug Report:
    - Issue: Data persistence failure — saved profile is not persisted.
    - Actual: Set Start Time to 08:00 / 07:15 and End Time 16:00, clicked "Save Changes" (toast "Profile updated successfully"), then reloaded the page. The fields reverted to the defaults 09:00–17:00. Saved working hours do not survive a reload.

- [ ] FT-02: Users can save typical break times and "days they never meet."
  - Action: Add a break time (e.g., 12:00–13:00) and mark at least one weekday as a never-meet day, then save.
  - Expected: Both the break time and the never-meet day persist and are shown in the profile.
  - Bug Report:
    - Issue: Data persistence failure — never-meet day selection is not persisted.
    - Actual: Marked Friday as a "Days Off" never-meet day (checkbox became checked) and clicked "Save Changes" (toast "Profile updated successfully"). After reload, Friday reverted to unchecked (only the default Sunday/Saturday remained). The saved never-meet day does not persist.

- [X] FT-03: Creating a meeting within a chosen date range generates suggested time slots.
  - Action: Create a meeting, choose a start and end date, and generate suggestions.
  - Expected: A list of suggested time slots within the date range is produced.

- [X] FT-04: Organizer can add participants by name and email.
  - Action: In the meeting, add a participant with a name and email address.
  - Expected: The participant appears in the meeting's participant list with the correct name and email.

- [ ] FT-05: Suggested slots respect the stated preferences of known participants.
  - Action: Add a known participant whose saved working hours/break/no-meet days are restrictive, then generate suggestions.
  - Expected: Suggested slots fall only within every known participant's working hours and avoid their breaks and never-meet days.
  - Bug Report:
    - Issue: Incorrect scheduling logic — known participants' break times are not avoided.
    - Actual: With known participant Taylor Swift (break 11:30–12:30) and Alex (break 12:00–13:00), the generated list included break-overlapping slots: "11:00 AM - 12:00 PM (1 conflict)", "11:30 AM - 12:30 PM (2 conflicts)", "12:00 PM - 1:00 PM (2 conflicts)", "12:30 PM - 1:30 PM (1 conflict)". Slots that fall inside a known participant's declared break are still suggested (only score-penalized). Working-hours intersection (start 10:00 for Jordan) and never-meet days were respected, but breaks were not.

- [X] FT-06: Unknown participants fall back to generic business-hour slots.
  - Action: Add a participant with no saved profile, then generate suggestions.
  - Expected: Suggestions use generic business-hour slots for that participant rather than a personal profile.

- [X] FT-07: Participants can adjust availability per meeting and mark slots "preferred" or "last resort."
  - Action: As a participant, open the meeting, mark one slot as "preferred" and another as "last resort."
  - Expected: The chosen slots display the assigned "preferred"/"last resort" labels for that meeting only.

- [X] FT-08: Organizer can see a ranked list of candidate times.
  - Action: Generate suggestions and open the candidate times list.
  - Expected: Candidate times are listed in ranked order by score.

- [X] FT-09: Organizer can confirm one time for the meeting.
  - Action: Select a candidate time and confirm it.
  - Expected: The meeting is set to that confirmed time and shows a confirmed status.

- [X] FT-10: Organizer can reopen the meeting and select a different time.
  - Action: Reopen a confirmed meeting, then choose and confirm a different candidate time.
  - Expected: The meeting reopens for time selection and updates to the newly confirmed time.

## Constraint

- [ ] CS-01: Meeting cannot be created without required fields.
  - Action: Attempt to create a meeting leaving the title, date range, or required field empty.
  - Expected: Creation is blocked and a validation message identifies the missing required field.
  - Bug Report:
    - Issue: Missing validation message.
    - Actual: With the "Meeting Title" empty, the "Next" button is rendered disabled and clicking it does nothing; no validation message or error text is displayed anywhere identifying the missing required field. Creation is blocked, but no message identifies the missing field.

- [X] CS-02: Suggested slots never fall on a never-meet day.
  - Action: Generate suggestions for a known participant who marked a weekday as a never-meet day.
  - Expected: No suggested slot occurs on that weekday.

- [ ] CS-03: Suggested slots avoid a known participant's declared break times.
  - Action: Generate suggestions for a known participant with a declared break window.
  - Expected: No suggested slot overlaps the participant's break window.
  - Bug Report:
    - Issue: Incorrect scheduling logic — break windows are not excluded from suggestions.
    - Actual: For known participant Taylor Swift (break 11:30–12:30) the suggestions included "Mon, Nov 9 • 11:30 AM - 12:30 PM (2 conflicts)" and "12:00 PM - 1:00 PM (2 conflicts)" — slots that overlap the declared break window. Break-overlapping slots are returned rather than excluded.

- [X] CS-04: Participant cannot be added with a missing or invalid email.
  - Action: Attempt to add a participant with an empty or malformed email address.
  - Expected: The participant is rejected and an email-format error is shown.

- [X] CS-05: Duplicate participants (same email) are prevented.
  - Action: Add a participant, then add another participant using the same email address.
  - Expected: The duplicate is rejected or blocked and does not create a second entry.

- [X] CS-06: Empty result is handled when no valid slot exists.
  - Action: Generate suggestions for the smallest possible date range where every candidate is excluded by preferences.
  - Expected: The app shows a clear "no available slots" message instead of an empty or broken list.

## Interaction

- [ ] IX-01: Ranked list indicates conflicts, partial overlaps, and tied scores.
  - Action: Generate candidates with participants whose preferences conflict partially or fully, including two equal-score slots.
  - Expected: The list labels each candidate as full conflict, partial overlap, or tie where applicable.
  - Bug Report:
    - Issue: Missing "partial overlap" indication.
    - Actual: The list correctly rendered conflict badges ("1 conflict", "2 conflicts", "3 conflicts") and tie badges ("Tied"), but no candidate was ever labeled as a partial overlap. Partial-overlap status is neither computed nor displayed anywhere in the candidate list.

- [X] IX-02: Ranking updates when participation changes after reopening.
  - Action: Reopen a meeting, add or remove a participant or change a participant's per-meeting availability, and regenerate.
  - Expected: The ranked candidate list recalculates to reflect the updated participation.

## Content

- [X] CT-01: Availability profile fields match the scheduling theme.
  - Action: Open the availability profile page.
  - Expected: Fields are labeled for working hours, break times, and never-meet days, with no unrelated content.

- [X] CT-02: Candidate times display within the chosen date range and use valid times.
  - Action: Inspect the suggested/ranked candidate times.
  - Expected: Each listed time falls within the selected date range and shows a valid, correctly formatted time-of-day.

---

### Summary
- **Passed (14):** FT-03, FT-04, FT-06, FT-07, FT-08, FT-09, FT-10, CS-02, CS-04, CS-05, CS-06, IX-02, CT-01, CT-02
- **Failed (6):** FT-01, FT-02 (profile changes don't persist across reload), FT-05 & CS-03 (break windows not excluded from suggestions), CS-01 (no required-field validation message), IX-01 (no partial-overlap labeling)

Note: The app stores all state in memory (`useState(mockProfiles)` / `useState(mockMeetings)`), so any edit — profile changes and created meetings — is lost on page reload, which is the root cause of the FT-01/FT-02 failures.