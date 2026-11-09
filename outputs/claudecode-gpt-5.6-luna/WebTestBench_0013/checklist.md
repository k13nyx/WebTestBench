# Test Checklist

## Functionality
- [ ] **FT-01: Maintain the personal availability profile**
  - **Action:** Open the **Availability Profile** page, set preferred working hours, typical break times, and days never meeting, then save and reopen the profile.
  - **Expected:** All saved working hours, break times, and no-meeting days are displayed unchanged.

- [ ] **FT-02: Create a meeting and generate date-range suggestions**
  - **Action:** Use the default meeting data to create a meeting, select a start and end date, and open the suggested time slots.
  - **Expected:** The meeting is created and suggested slots are generated only for the selected date range.

- [ ] **FT-03: Add a known participant**
  - **Action:** In the meeting’s **Participants** section, add the preloaded participant whose profile exists by entering the displayed name and email.
  - **Expected:** The participant is added and generated suggestions account for that participant’s availability profile.

- [ ] **FT-04: Add an unknown participant**
  - **Action:** Add the preloaded participant who has no availability profile by entering the displayed name and email.
  - **Expected:** The participant is added and suggestions for that participant use the application’s generic business-hour availability.

- [ ] **FT-05: Adjust availability for an individual meeting**
  - **Action:** Open the meeting-level availability controls for a participant and mark specific slots as **Preferred** and other slots as **Last resort**.
  - **Expected:** The selected slots display the corresponding availability status for that meeting.

- [ ] **FT-06: Confirm and change the selected meeting time**
  - **Action:** Confirm a candidate time, reopen the confirmed meeting, select a different candidate time, and confirm the change.
  - **Expected:** The meeting first shows the original confirmed time and then shows only the newly selected time after the change.

## Constraint
- [ ] **CS-01: Prevent invalid personal availability hours**
  - **Action:** In **Availability Profile**, enter a working-hours end time earlier than its start time or leave a required time value empty, then attempt to save.
  - **Expected:** The profile is not saved and a validation message identifies the invalid or missing time field.

- [ ] **CS-02: Exclude breaks and no-meeting days from compatible suggestions**
  - **Action:** Generate suggestions using a profile with configured break times and no-meeting days.
  - **Expected:** No suggestion is scheduled during a configured break or on a configured no-meeting day.

- [ ] **CS-03: Keep every suggestion inside the selected date range**
  - **Action:** Generate suggestions for a date range with defined start and end dates.
  - **Expected:** Every displayed candidate falls on or between the selected start and end dates; no candidate appears outside the range.

- [ ] **CS-04: Apply all known participant preferences**
  - **Action:** Generate suggestions for a meeting containing multiple participants with existing profiles and compare candidates with each profile’s working hours, breaks, and no-meeting days.
  - **Expected:** A candidate marked fully compatible does not violate any known participant’s stated availability.

- [ ] **CS-05: Apply generic business hours only to participants without profiles**
  - **Action:** Generate suggestions for a meeting containing an unknown participant and inspect the candidate times against the application’s generic business-hour window.
  - **Expected:** The unknown participant contributes generic business-hour constraints and does not receive profile-specific preference treatment.

- [ ] **CS-06: Keep meeting overrides separate from the personal profile**
  - **Action:** Change a participant’s availability for one meeting, then reopen the participant’s personal **Availability Profile**.
  - **Expected:** The meeting override is applied to that meeting only; the personal profile remains unchanged.

## Interaction
- [ ] **IX-01: Refresh suggestions after scheduling inputs change**
  - **Action:** Change the meeting date range or participant list after suggestions are displayed.
  - **Expected:** The suggestion list updates to reflect the latest date range and participants without requiring a separate manual calculation step.

- [ ] **IX-02: Provide clear preferred and last-resort slot states**
  - **Action:** Toggle a meeting slot between normal, **Preferred**, and **Last resort** states.
  - **Expected:** Each toggle immediately changes the slot’s visible state, and only the currently selected state is shown.

- [ ] **IX-03: Display ranked candidates with availability details**
  - **Action:** Review the generated candidate list using participants with full matches, partial overlaps, and conflicts.
  - **Expected:** Candidates are ordered by score/rank and visibly identify conflicts, partial overlaps, and tied scores; tied candidates show the same rank or score.

- [ ] **IX-04: Show confirmation state after selecting a candidate**
  - **Action:** Select a candidate and use the **Confirm** control.
  - **Expected:** The selected date and time become visibly marked as confirmed and the meeting displays a confirmation response.

- [ ] **IX-05: Make the confirmed meeting reopenable**
  - **Action:** Open a confirmed meeting after participant availability changes.
  - **Expected:** A visible control such as **Reopen**, **Change time**, or equivalent returns the meeting to candidate selection instead of forcing creation of a separate meeting.

## Content
- [ ] **CT-01: Label availability settings clearly**
  - **Action:** Review the personal profile and meeting-level availability controls.
  - **Expected:** The interface clearly labels preferred working hours, break times, no-meeting days, preferred slots, and last-resort slots.

- [ ] **CT-02: Show complete candidate information**
  - **Action:** Inspect each candidate row in the ranked suggestions list.
  - **Expected:** Each row displays the candidate’s date, time, rank or score, and applicable availability indicators for conflicts, partial overlaps, ties, or compatibility.

- [ ] **CT-03: Show accurate participant and confirmation details**
  - **Action:** Review the meeting summary before and after confirming or changing a time.
  - **Expected:** The summary shows the correct participant names and email addresses and displays the currently selected date and time.