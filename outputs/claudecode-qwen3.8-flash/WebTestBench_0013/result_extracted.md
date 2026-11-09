# Test Result

## Functionality
- [X] FT-01: Organizer can create and save a personal availability profile
  - Action: Opened the availability profile editor ("My Availability"); set working hours 09:00–17:00, break 12:00–13:00, no-meet day Friday; clicked "Save Changes".
  - Expected: Save succeeds; reopening the profile shows all three settings exactly as entered.
  - Verified: toast "Profile updated successfully"; after navigating away (Meetings) and back, inputs read 09:00 / 17:00, break 12:00–13:00, Friday checkbox checked. (Observation, not part of the test criteria: state lives only in memory — a full browser reload resets the profile to seed values.)

- [X] FT-02: Creating a meeting auto-generates suggested slots within the chosen date range
  - Action: Clicked "New Meeting", entered title "QA Sprint Sync", date range Nov 9–15, 2026 (7 days), submitted through the wizard ("Create Meeting").
  - Expected: A list of suggested time slots is generated automatically, all falling inside the chosen range.
  - Verified: Meeting page shows "Suggested Times — Ranked by availability scores" with 10 generated slots, all Mon, Nov 9 (inside Nov 9–15).

- [X] FT-03: Organizer can add participants by name and email
  - Action: In the meeting wizard's participant step, added "Jordan Lee / jordan.lee@example.com" and "Casey Nguyen / casey@external-corp.com" via "Add Participant".
  - Expected: Both appear in the participant list with their names and emails.
  - Verified: "Invited Participants" list shows both entries with name and email (badged "External").

- [X] FT-04: Slots for known participants respect all profile preferences
  - Action: Saved a profile with working hours 10:00–16:00 and break 12:00–13:00, then created "QA Constraint Test" adding that profile's owner as a known participant (alex.morgan@company.com, badged "Known"); slots generated.
  - Expected: All suggested slots fit inside every known participant's working hours (intersection), not only generic hours.
  - Verified: All 10 slots fall between 10:00 AM and 3:30 PM (inside the 10:00–16:00 window), whereas the same range with only unknown participants produced slots starting at 9:00 AM — proving the known-participant hours (intersection) are applied, not generic hours.

- [X] FT-05: Unknown participants receive generic business-hour slots
  - Action: Created "QA Sprint Sync" with an email having no profile (casey@external-corp.com, badged "External"); generated slots.
  - Expected: Slots for/including that participant use standard business hours (e.g., 09:00–17:00) instead of personal preferences.
  - Verified: Slots began at 9:00 AM (standard business hours), within the 9–17 band, with no narrowing from any personal profile.

- [X] FT-06: Participant can mark a slot as "Preferred" or "Last Resort"
  - Action: Opened the participant response view ("Respond to: Q4 Planning Session") as participant Jordan Chen, marked "Wed, Dec 18 • 2:00 PM" as Preferred and "Tue, Dec 17 • 10:00 AM" as Last Resort, clicked "Save My Availability".
  - Expected: Both markers are saved and visibly displayed on those slots.
  - Verified: Toast "Your availability has been saved!"; organizer slot cards then showed "2 preferred" on Wed Dec 18 and "1 last resort" on Tue Dec 17.

- [X] FT-07: Organizer sees a ranked list of candidate times
  - Action: After the participant response above, opened the organizer's meeting view ("Suggested Times — Ranked by availability scores").
  - Expected: A list of candidate times is shown ordered by score (best first).
  - Verified: List ordered 100 → 85 → 45, best first.

- [X] FT-08: Organizer confirms one candidate time
  - Action: Selected the top candidate (Wed, Dec 18 • 2:00–3:00 PM) via its "Confirm" control.
  - Expected: The meeting status changes to "Confirmed" and shows the selected date/time.
  - Verified: Status badge "Confirmed"; section "Confirmed Time — Wed, Dec 18 • 2:00 PM - 3:00 PM". (Note: confirmation is done by the per-slot "Confirm" button; there is no separate global "Confirm Time" control.)

- [X] FT-09: Confirmed meeting can be reopened and a different time selected
  - Action: Clicked "Reopen" on the confirmed meeting, then confirmed a different candidate (Tue, Dec 17 • 10:00–11:00 AM).
  - Expected: The meeting returns to an open state and is re-confirmed with the new time displayed.
  - Verified: Status became "Reopened" with Confirm buttons restored (3); after re-confirmation, status "Confirmed" and "Confirmed Time — Tue, Dec 17 • 10:00 AM - 11:00 AM".

## Constraint
- [X] CS-01: No slots are suggested on a participant's no-meet days
  - Action: Created meetings spanning Nov 9–15, 2026 (includes Friday Nov 13) with a known participant whose profile marks Friday as a no-meet day.
  - Expected: Zero suggested slots fall on any Friday in the range.
  - Verified: All generated slots were on Monday; zero Friday (and zero weekend) slots appeared.

- [ ] CS-02: Slots never overlap known participants' break times
  - Action: Created "QA Constraint Test" including a known participant (and organizer) with break 12:00–13:00; generated slots.
  - Expected: No suggested slot overlaps 12:00–13:00 on any date.
  - Bug Report:
    - Issue: Constraint Violation — break-time slots are suggested instead of excluded
    - Actual: Slots "Mon, Nov 9 • 11:30 AM - 12:30 PM", "Mon, Nov 9 • 12:00 PM - 1:00 PM" (fully inside the break), and "Mon, Nov 9 • 12:30 PM - 1:30 PM" appear in Suggested Times, only flagged "2 conflicts" yet still scored 100 and offered for confirmation. Same pattern in "QA Sprint Sync" ("12:00 PM - 1:00 PM" suggested with "1 conflict").
- [X] CS-03: Participant addition is blocked for missing or invalid email
  - Action: Entered name only (no email) → "Add Participant"; then name + "abc@" → "Add Participant".
  - Expected: Both attempts are rejected with a validation message; no participant is added.
  - Verified: Toasts "Please enter both name and email" and "Please enter a valid email address"; list remained "No participants added yet" after both attempts.

- [ ] CS-04: A meeting cannot be confirmed without exactly one selected time
  - Action: Searched for a "Confirm Time" control to click with no candidate selected, in both open (Reopened) and polling states of meeting views.
  - Expected: Confirmation is blocked with a prompt to select a time; meeting stays unconfirmed.
  - Bug Report:
    - Issue: Missing Control — the specified validation flow does not exist
    - Actual: There is no global "Confirm Time" button; every candidate slot has its own "Confirm" button (buttons present: Reopen/Add plus per-slot Confirm), so confirmation always carries an implicit single selection and the "confirm with nothing selected" prompt scenario is unreachable.
- [X] CS-05: Candidate times are locked once the meeting is confirmed
  - Action: With meeting-1 confirmed, attempted to change the time / click slot actions without reopening.
  - Expected: Editing is disabled/blocked until "Reopen Meeting" is used.
  - Verified: All "Confirm" buttons disappear in Confirmed state (0 found on re-click attempt); only the "Reopen" control remains; time is unchangeable until reopened (re-confirmed only after clicking Reopen).

## Interaction
- [X] IX-01: Ranking updates immediately when participants change availability
  - Action: Noted pre-change order (Tue 85, Wed 90, Thu 60); as participant Jordan Chen switched "Tue, Dec 17" from Preferred to Last Resort and set "Wed, Dec 18" to Preferred, saved, and returned to the organizer view.
  - Expected: The ranked list reflects the new scores/order without a manual reload error or stale data.
  - Verified: Organizer list re-rendered automatically as Wed 100 → Tue 85 → Thu 45 with updated badges; no reload, no stale values, no error.

- [X] IX-02: Confirmation produces visible feedback
  - Action: Confirmed a candidate time (Wed, Dec 18 slot).
  - Expected: A success message/toast appears, and the meeting card updates to the confirmed state.
  - Verified: Toast "Meeting time confirmed!" appeared; card switched to "Confirmed" status with "Confirmed Time" section.

- [X] IX-03: Reopen control transitions the meeting state visibly
  - Action: Clicked "Reopen" on the confirmed meeting.
  - Expected: The UI switches from locked view back to editable candidate list with selection controls enabled.
  - Verified: Status badge changed "Confirmed" → "Reopened", the "Confirmed Time" block disappeared, and the three slot "Confirm" controls reappeared.

## Content
- [ ] CT-01: Ranked list labels conflicts, partial overlaps, and tied scores
  - Action: Inspected ranked candidate lists with varied responses ("QA Constraint Test", "QA Sprint Sync", meeting-1 after re-ranking).
  - Expected: Each candidate displays conflict or partial-overlap indicators per participant, and equal-scoring candidates are explicitly marked as tied.
  - Bug Report:
    - Issue: Missing Content — no partial-overlap indicators; conflicts not attributed per participant
    - Actual: Slots show only aggregate badges ("Tied" ✓, "N conflict(s)", "N preferred", "N last resort"). No partial-overlap label appears anywhere (e.g., the 11:30–12:30 slot that only partly overlaps the 12:00–13:00 break is labeled identically to the full-overlap 12:00–13:00 slot: "2 conflicts"), and conflict badges carry participant counts, not per-participant identification.
- [X] CT-02: Default data contains both profiled and non-profiled participants
  - Action: Opened the app / default meetings on first load and the participant invite flow (known/unknown recognition).
  - Expected: At least one pre-existing participant with a saved availability profile and at least one recognizable contact without a profile are available for testing.
  - Verified: Seed meetings show profiled participants "Jordan Chen" (jordan.chen@company.com) and "Sam Rivera" (sam.rivera@company.com) badged "Known" with saved profiles and existing responses, plus profile-less "External Client" (client@external.com) badged "External".
- [X] CT-03: Generated slots display complete, relevant date/time content
  - Action: Viewed suggested slot lists for the generated meetings.
  - Expected: Every slot shows a readable day, date, start–end time (with duration consistent with the meeting), and no placeholder or empty text appears.
  - Verified: All slots rendered as e.g. "Mon, Nov 9 • 9:00 AM - 10:00 AM" (60-minute meetings → 1-hour spans) and "Wed, Dec 18 • 10:00 AM - 10:30 AM" for the 30-minute meeting; no empty/placeholder text observed.
