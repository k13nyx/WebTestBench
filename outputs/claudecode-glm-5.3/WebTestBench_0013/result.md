All checklist items executed. Here is the complete test result:

# Test Result

## Functionality

- [X] FT-01: User can save preferred working hours in the personal availability profile
  - Action: Open the availability profile, set preferred working hours (e.g., start 09:00, end 17:00), click "Save".
  - Expected: Profile saves and 09:00–17:00 is shown as the saved preferred working hours.
  - (Set Start 09:00 / End 17:00, clicked "Save Changes" → toast "Profile updated successfully"; profile displays Start Time 09:00, End Time 17:00.)

- [X] FT-02: User can save typical break times in the profile
  - Action: In the profile, set a typical break window (e.g., 12:00–13:00), click "Save".
  - Expected: The break window is saved and displayed in the profile.
  - (Set break 12:00–13:00, saved → toast shown; break row "12:00 to 13:00" persists under Break Times.)

- [X] FT-03: User can save days they never meet
  - Action: In the profile, mark days as never-meet (e.g., Saturday and Sunday), click "Save".
  - Expected: The selected days are saved and listed as never-meet days in the profile.
  - (Saturday and Sunday checked under Days Off, saved → both remain checked/listed after save.)

- [X] FT-04: Creating a meeting with a chosen date range auto-generates suggested slots
  - Action: Create a meeting with a title and a chosen date range (e.g., next Monday through Friday).
  - Expected: The meeting is created and suggested time slots are automatically generated, every slot falling inside the chosen date range and showing its date and start–end time.
  - (Created "Sprint Planning", range Mon Nov 9 – Fri Nov 13, 2026 → "Meeting created successfully!"; 10 suggested slots generated, all "Mon, Nov 9 • 9:00 AM - 10:00 AM" … "1:30 PM - 2:30 PM" — all within Nov 9–13, each showing date and start–end time.)

- [X] FT-05: Organizer can add a participant by name and email
  - Action: As organizer, enter a participant's name and email and click "Add Participant".
  - Expected: The participant appears in the meeting's participant list.
  - (Entered "Taylor Smith" / "not-an-email" in the Add Participant dialog → toast "Participant added"; entry appears in Q4 Planning Session's participant list with "External" badge; count 2→3.)

- [ ] FT-06: Suggested slots respect all known participants' stated preferences
  - Action: View suggestions for a meeting that includes default participants who have profiles (with working hours, breaks, and never-meet days) within the range.
  - Expected: Every suggested slot lies inside each known participant's working hours and avoids their break windows and never-meet days.
  - Bug Report:
    - Issue: Suggested slot outside known participants' working hours (incorrect suggestion generation)
    - Actual: For "Q4 Planning Session" (known participants Jordan Chen — working hours 10:00–18:00, and Sam Rivera — 09:30–17:30), the suggested slot "Thu, Dec 19 • 9:00 AM - 10:00 AM" starts at 9:00 AM, before Jordan's 10:00 AM start and Sam's 09:30 start — it lies inside neither known participant's working hours (the app itself flags it with "1 conflict" and "1 last resort"). Tue/Wed slots do respect hours, breaks and never-meet days, but not every suggested slot does.

- [X] FT-07: Unknown participants are handled with generic business-hour slots
  - Action: Add a participant by name/email who has no profile (unknown), then view the meeting's suggested slots.
  - Expected: That participant's availability is treated as generic business hours (weekdays, e.g., 09:00–17:00) and suggestions reflect those hours, not any personal profile.
  - (Added "Taylor Smith / not-an-email" — no profile, shown as "External" → suggestions regenerated as generic weekday business-hour slots: all "Mon, Dec 16 • 10:00 AM - 3:30 PM" 60-min slots within the 09:00–17:00 default business hours, uniform score 100, no personal-profile markings; slot generation constrains unknown participants to default business hours 09:00–17:00 on non-never-meet weekdays.)

- [X] FT-08: Participant can adjust availability per meeting, marking slots "Preferred" or "Last resort"
  - Action: Open a default meeting as one of its participants, mark one suggested slot "Preferred" and a different slot "Last resort", save.
  - Expected: Both markings are saved on that meeting and visible on the respective slots.
  - (As Jordan Chen on /meeting/meeting-1/respond/part-1: marked Wed Dec 18 "Preferred" and Thu Dec 19 "Last Resort", clicked "Save My Availability" → toast "Your availability has been saved!"; on the meeting, Wed shows "2 preferred" and Thu shows "1 last resort".)

- [X] FT-09: Organizer sees a ranked list of candidate times
  - Action: As organizer, open the candidate times view for a meeting whose participants have marked slots.
  - Expected: Candidate times are listed in ranked order (best score first) based on participant markings and preferences.
  - (After participants' markings were saved, the "Suggested Times — Ranked by availability scores" list shows Tue Dec 17 10:00 (100) → Wed Dec 18 2:00 PM (100, tied) → Thu Dec 19 9:00 AM (45/80) — best score first, scores computed from participant markings.)

- [X] FT-10: Organizer can confirm one candidate time
  - Action: As organizer, click "Confirm" on one candidate time in the ranked list.
  - Expected: The selected time is recorded as the meeting's confirmed time.
  - (Clicked "Confirm" on Tue, Dec 17 • 10:00 AM - 11:00 AM → "Confirmed Time: Tue, Dec 17 • 10:00 AM - 11:00 AM" recorded and displayed.)

- [X] FT-11: Organizer can reopen a confirmed meeting and select a different time
  - Action: On a confirmed meeting, click "Reopen", then confirm a different candidate time.
  - Expected: The meeting returns to the scheduling state and the new time becomes the confirmed time.
  - (Clicked "Reopen" → toast "Meeting reopened for rescheduling", status "Reopened", Confirm buttons restored; confirmed Wed, Dec 18 • 2:00 PM - 3:00 PM → status "Confirmed" and Confirmed Time now "Wed, Dec 18 • 2:00 PM - 3:00 PM".)

## Constraint

- [ ] CS-01: Working hours with end time before start time are rejected
  - Action: In the profile, set working hours start 17:00 / end 09:00, click "Save".
  - Expected: Save is blocked with a validation error and the invalid hours are not stored.
  - Bug Report:
    - Issue: Missing validation — invalid working hours accepted and stored
    - Actual: With Start Time 17:00 / End Time 09:00, clicking "Save Changes" shows the success toast "Profile updated successfully"; no validation error appears anywhere in the DOM, and the profile stores/displays 17:00–09:00 (end before start).

- [ ] CS-02: Participant cannot be added without a name and a valid email
  - Action: Try adding a participant with an empty name, then with an invalid email ("not-an-email").
  - Expected: Both attempts are blocked with errors; no participant entry is created.
  - Bug Report:
    - Issue: Missing email validation — participant created with invalid email
    - Actual: The empty-name attempt is correctly blocked with "Please enter both name and email"; however, submitting name "Taylor Smith" with email "not-an-email" succeeds — toast "Participant added", and the participant entry "Taylor Smith / not-an-email" is created in the participant list (count 2 → 3). No email-format error is shown.

- [X] CS-03: Date range with end date before start date is rejected
  - Action: Create a meeting with an end date earlier than the start date (or leave the range empty).
  - Expected: Creation is blocked with a validation error; no meeting and no suggested slots are generated.
  - (An inverted range cannot be constructed — the calendar picker auto-normalizes (clicking an earlier date resets the start); leaving the range empty makes the "Next" button disabled, blocking creation — no meeting and no suggested slots were generated.)

- [X] CS-04: Confirmed time cannot be changed without reopening the meeting
  - Action: On a confirmed meeting, attempt to select or confirm another candidate time before clicking "Reopen".
  - Expected: The confirmed time remains unchanged; selecting a new time is possible only after the meeting is reopened.
  - (While confirmed, all "Confirm" buttons are removed from the candidate list (0 found) and slot cards are not selectable; confirmed time stayed "Tue, Dec 17 • 10:00 AM - 11:00 AM"; only after clicking "Reopen" did Confirm buttons reappear and a different time could be confirmed.)

## Interaction

- [X] IX-01: Success feedback appears after saving the profile
  - Action: Edit any profile field (e.g., working hours) and click "Save".
  - Expected: A success message (e.g., "Profile saved") appears on screen.
  - (On each save, the toast "Profile updated successfully" appears on screen.)

- [X] IX-02: Ranked candidate list updates after a participant changes a marking
  - Action: While the organizer views the ranked list, have a participant change a slot's marking (e.g., to "Preferred"), then reopen the candidate list.
  - Expected: Scores and rank order update to reflect the new marking, without creating a new meeting.
  - (Organizer's list was [Tue 85 → 100, Wed 90, Thu 60/45]; participant Jordan changed the Thu slot marking to "Preferred" and saved; the candidate list then showed Tue 100 (1 preferred), Wed 100 (Tied), Thu 80 ("1 preferred", "1 conflict") — score updated and re-ranked, same meeting, no new meeting created.)

- [X] IX-03: Confirmation feedback appears after a time is confirmed
  - Action: As organizer, confirm one candidate time.
  - Expected: A success confirmation appears and the meeting status changes to "Confirmed" with the confirmed time shown.
  - (Toast "Meeting time confirmed!" appeared; status badge changed to "Confirmed" and a "Confirmed Time — Tue, Dec 17 • 10:00 AM - 11:00 AM" panel is shown.)

## Content

- [ ] CT-01: Ranked list indicates conflicts, partial overlaps, and tied scores
  - Action: Inspect the ranked candidate list on a meeting containing conflicting and partially overlapping participant availability.
  - Expected: Each candidate shows the correct indicators — conflict marks, partial-overlap marks, and tied-score marks where two candidates have equal scores — matching the participants' actual availability.
  - Bug Report:
    - Issue: Missing partial-overlap indicator in the ranked candidate list
    - Actual: Conflict marks are shown correctly ("Thu, Dec 19 • 9:00 AM - 10:00 AM" → "1 conflict" for Sam Rivera) and tied-score marks are shown correctly (Tue 100 and Wed 100 → "Tied" badge on Wed), but no partial-overlap indicator exists anywhere in the candidate list even though partial overlaps exist in participants' actual availability (e.g., the Thu 9:00–10:00 slot starts 30 min before Sam Rivera's 09:30 working-hours start — this partial overlap is not marked).

- [X] CT-02: Participant names and emails are displayed exactly as entered
  - Action: Compare each participant's displayed name and email in the participant list against the values entered when added.
  - Expected: Every name and email matches exactly, with no truncation or alteration.
  - (Verified: "Jordan Chen / jordan.chen@company.com", "Sam Rivera / sam.rivera@company.com" match seeded values exactly, and the added participant "Taylor Smith / not-an-email" is displayed exactly as entered — no truncation or alteration.)