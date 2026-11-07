# Test Checklist

## Functionality
- [ ] FT-01: User can create and save a personal availability profile with working hours, breaks, and no-meet days
  - Action: Open the availability profile page, set preferred working hours (e.g., 09:00–17:00), add a typical break (e.g., 12:00–13:00), select at least one "never meet" day, and save.
  - Expected: Profile saves successfully and the saved values are displayed when the profile page is reopened.

- [ ] FT-02: Organizer can create a meeting with a date range and get auto-generated suggested time slots
  - Action: Create a new meeting, enter a title, choose a start date and end date, and trigger slot generation.
  - Expected: A list of suggested time slots appears, and every slot falls within the chosen date range.

- [ ] FT-03: Organizer can add a participant by name and email
  - Action: In the meeting's participant section, enter a name and email address and add the participant.
  - Expected: The participant appears in the participant list showing both the entered name and email.

- [ ] FT-04: Suggested slots respect the preferences of all known participants (those with a saved profile)
  - Action: Create a meeting with a date range, add two participants whose emails match existing saved profiles with different working hours, then generate slots.
  - Expected: Every suggested slot falls inside the overlapping availability of the organizer's and both known participants' working hours, and excludes their break times and no-meet days.

- [ ] FT-05: Unknown participants (no saved profile) fall back to generic business-hour slots
  - Action: Add a participant using a name/email that has no saved availability profile, then generate slots.
  - Expected: Slots are still generated using generic business hours for that participant, and a label marks that participant as having no profile / using default availability.

- [ ] FT-06: Participant can adjust availability per meeting and mark slots "preferred" or "last resort"
  - Action: Open the meeting as a participant, mark one suggested slot as "Preferred" and another as "Last resort", and save.
  - Expected: Both slots display their "Preferred" and "Last resort" markers in the meeting view after saving.

- [ ] FT-07: Organizer sees a ranked list of candidate times with scores
  - Action: As the organizer, open the meeting's candidate-times view after participants have responded.
  - Expected: Candidate times are displayed in ranked order (best first) with a visible score or rank value for each, and the top-ranked slot is the one with the most "preferred" responses.

- [ ] FT-08: Organizer can confirm one candidate time
  - Action: Select a candidate time from the ranked list and confirm it.
  - Expected: The meeting shows a confirmed status with the chosen date/time, and the confirmed time is the one that was selected.

- [ ] FT-09: Confirmed meeting can be reopened and a different time selected
  - Action: On a confirmed meeting, use the reopen action, then select a different candidate time and confirm it again.
  - Expected: The meeting's confirmed time updates to the newly selected time, and the previously confirmed time is no longer shown as the meeting time.

## Constraint
- [ ] CS-01: Availability profile rejects invalid time ranges
  - Action: In the profile, set preferred working hours end time earlier than the start time (e.g., 17:00–09:00) and attempt to save.
  - Expected: The profile is not saved and a validation message is shown; the previously saved profile remains unchanged.

- [ ] CS-02: Days marked as "never meet" are excluded from generated slots
  - Action: Set a "never meet" day (e.g., Friday) in the profile, then generate slots for a date range containing that weekday.
  - Expected: No suggested slot falls on the marked "never meet" day.

- [ ] CS-03: Typical break times are excluded from suggested slots
  - Action: Set a typical break (e.g., 12:00–13:00) in the profile, then generate slots.
  - Expected: No suggested slot overlaps the configured break window.

- [ ] CS-04: Participant cannot be added with missing or invalid details
  - Action: Attempt to add a participant with an empty name, then with an empty email, then with a malformed email (e.g., "not-an-email").
  - Expected: Each attempt is rejected with a validation message and no participant is added to the list.

- [ ] CS-05: Meeting date range must be valid
  - Action: Create a meeting with an end date earlier than the start date and attempt to generate slots.
  - Expected: Slot generation is blocked and a validation message is shown; no slots are produced.

- [ ] CS-06: Confirmation requires a selected candidate time
  - Action: Open the candidate-times view without selecting any time and attempt to confirm.
  - Expected: The confirm action is unavailable or blocked, and the meeting does not enter a confirmed state.

## Interaction
- [ ] IX-01: Ranked list updates dynamically when a participant marks preferences
  - Action: Note the current rank order as organizer, then have a participant mark a lower-ranked slot as "Preferred" and save, and refresh/reopen the organizer's candidate view.
  - Expected: The newly preferred slot moves up in the ranked list relative to its previous position.

- [ ] IX-02: Adding or removing a participant regenerates the suggested slots
  - Action: On an existing meeting, add an additional known participant (or remove one) and regenerate/view the slots.
  - Expected: The suggested slot list refreshes to reflect the updated participant set rather than showing the previous list unchanged.

- [ ] IX-03: Reopened meeting exposes prior responses and allows re-selection
  - Action: Reopen a confirmed meeting and view the candidate list.
  - Expected: Previously submitted participant responses (preferred / last resort) are still displayed and each candidate time is selectable again.

## Content
- [ ] CT-01: Availability profile fields match the stated purpose with no placeholder text
  - Action: Open the availability profile page and read all field labels, helper text, and headings.
  - Expected: Labels clearly correspond to preferred working hours, typical break times, and days never available for meetings; no lorem ipsum, "TODO", or unrelated sample text is present.

- [ ] CT-02: Candidate-time rows show complete, relevant scheduling information
  - Action: As organizer, inspect each row of the ranked candidate-times list for a meeting with at least two participants, one having a conflict.
  - Expected: Each row shows the date and time range plus indicators for full conflicts, partial overlaps, and tied scores where applicable, with no missing or blank values.