# Test Result

## Functionality

- [X] **FT-01: Maintain the personal availability profile**
  - **Action:** Open the **Availability Profile** page, set preferred working hours, typical break times, and days never meeting, then save and reopen the profile.
  - **Expected:** All saved working hours, break times, and no-meeting days are displayed unchanged.

- [X] **FT-02: Create a meeting and generate date-range suggestions**
  - **Action:** Use the default meeting data to create a meeting, select a start and end date, and open the suggested time slots.
  - **Expected:** The meeting is created and suggested slots are generated only for the selected date range.

- [ ] **FT-03: Add a known participant**
  - **Action:** In the meeting’s **Participants** section, add the preloaded participant whose profile exists by entering the displayed name and email.
  - **Expected:** The participant is added and generated suggestions account for that participant’s availability profile.
  - **Bug Report:**
    - **Issue:** Known participant is not added as a known participant.
    - **Actual:** The preloaded known participants observed were Jordan Chen and Sam Rivera. The participant added during the test, Alex Morgan, was classified as “External,” so the known participant availability profile was not applied.

- [X] **FT-04: Add an unknown participant**
  - **Action:** Add the preloaded participant who has no availability profile by entering the displayed name and email.
  - **Expected:** The participant is added and suggestions for that participant use the application’s generic business-hour availability.

- [ ] **FT-05: Adjust availability for an individual meeting**
  - **Action:** Open the meeting-level availability controls for a participant and mark specific slots as **Preferred** and other slots as **Last resort**.
  - **Expected:** The selected slots display the corresponding availability status for that meeting.
  - **Bug Report:**
    - **Issue:** Missing meeting-level participant availability controls.
    - **Actual:** Participant rows only exposed participant information and an unlabeled action button. No controls were available to mark individual slots as “Preferred” or “Last resort.”

- [X] **FT-06: Confirm and change the selected meeting time**
  - **Action:** Confirm a candidate time, reopen the confirmed meeting, select a different candidate time, and confirm the change.
  - **Expected:** The meeting first shows the original confirmed time and then shows only the newly selected time after the change.

## Constraint

- [ ] **CS-01: Prevent invalid personal availability hours**
  - **Action:** In **Availability Profile**, enter a working-hours end time earlier than its start time or leave a required time value empty, then attempt to save.
  - **Expected:** The profile is not saved and a validation message identifies the invalid or missing time field.
  - **Bug Report:**
    - **Issue:** Invalid availability hours are accepted.
    - **Actual:** Saving a start time of `18:00` and an end time of `09:00` succeeded and displayed the toast “Profile updated successfully.” No validation message was shown.

- [ ] **CS-02: Exclude breaks and no-meeting days from compatible suggestions**
  - **Action:** Generate suggestions using a profile with configured break times and no-meeting days.
  - **Expected:** No suggestion is scheduled during a configured break or on a configured no-meeting day.
  - **Bug Report:**
    - **Issue:** Suggestions overlap configured break times.
    - **Actual:** With a break configured for `11:30–12:00`, candidate slots including `11:00 AM–12:00 PM` and `11:30 AM–12:30 PM` were displayed.

- [X] **CS-03: Keep every suggestion inside the selected date range**
  - **Action:** Generate suggestions for a date range with defined start and end dates.
  - **Expected:** Every displayed candidate falls on or between the selected start and end dates; no candidate appears outside the range.

- [X] **CS-04: Apply all known participant preferences**
  - **Action:** Generate suggestions for a meeting containing multiple participants with existing profiles and compare candidates with each profile’s working hours, breaks, and no-meeting days.
  - **Expected:** A candidate marked fully compatible does not violate any known participant’s stated availability.

- [X] **CS-05: Apply generic business hours only to participants without profiles**
  - **Action:** Generate suggestions for a meeting containing an unknown participant and inspect the candidate times against the application’s generic business-hour window.
  - **Expected:** The unknown participant contributes generic business-hour constraints and does not receive profile-specific preference treatment.

- [ ] **CS-06: Keep meeting overrides separate from the personal profile**
  - **Action:** Change a participant’s availability for one meeting, then reopen the participant’s personal **Availability Profile**.
  - **Expected:** The meeting override is applied to that meeting only; the personal profile remains unchanged.
  - **Bug Report:**
    - **Issue:** Meeting-specific availability override controls are unavailable.
    - **Actual:** No participant-level meeting override interface was exposed, so an override could not be applied or verified separately from the personal profile.

## Interaction

- [X] **IX-01: Refresh suggestions after scheduling inputs change**
  - **Action:** Change the meeting date range or participant list after suggestions are displayed.
  - **Expected:** The suggestion list updates to reflect the latest date range and participants without requiring a separate manual calculation step.

- [ ] **IX-02: Provide clear preferred and last-resort slot states**
  - **Action:** Toggle a meeting slot between normal, **Preferred**, and **Last resort** states.
  - **Expected:** Each toggle immediately changes the slot’s visible state, and only the currently selected state is shown.
  - **Bug Report:**
    - **Issue:** Slot state toggle controls are missing.
    - **Actual:** Candidate rows displayed existing indicators such as “1 preferred” and “1 last resort,” but no control was available to toggle a slot between normal, Preferred, and Last resort states.

- [ ] **IX-03: Display ranked candidates with availability details**
  - **Action:** Review the generated candidate list using participants with full matches, partial overlaps, and conflicts.
  - **Expected:** Candidates are ordered by score/rank and visibly identify conflicts, partial overlaps, and tied scores; tied candidates show the same rank or score.
  - **Bug Report:**
    - **Issue:** Candidate ranking and availability-state details are incomplete.
    - **Actual:** The known-participant candidate list displayed scores in the order `85`, `90`, `60`, which is not descending rank order. It also displayed preferred, last-resort, and conflict indicators but did not visibly identify partial overlaps.

- [X] **IX-04: Show confirmation state after selecting a candidate**
  - **Action:** Select a candidate and use the **Confirm** control.
  - **Expected:** The selected date and time become visibly marked as confirmed and the meeting displays a confirmation response.

- [X] **IX-05: Make the confirmed meeting reopenable**
  - **Action:** Open a confirmed meeting after participant availability changes.
  - **Expected:** A visible control such as **Reopen**, **Change time**, or equivalent returns the meeting to candidate selection instead of forcing creation of a separate meeting.

## Content

- [ ] **CT-01: Label availability settings clearly**
  - **Action:** Review the personal profile and meeting-level availability controls.
  - **Expected:** The interface clearly labels preferred working hours, break times, no-meeting days, preferred slots, and last-resort slots.
  - **Bug Report:**
    - **Issue:** Meeting-level availability settings are not clearly exposed.
    - **Actual:** The personal profile labels “Working Hours,” “Break Times,” and “Days Off,” and candidate rows show preferred/last-resort indicators. However, no clearly labeled meeting-level controls for Preferred or Last resort slots were available.

- [X] **CT-02: Show complete candidate information**
  - **Action:** Inspect each candidate row in the ranked suggestions list.
  - **Expected:** Each row displays the candidate’s date, time, rank or score, and applicable availability indicators for conflicts, partial overlaps, ties, or compatibility.

- [X] **CT-03: Show accurate participant and confirmation details**
  - **Action:** Review the meeting summary before and after confirming or changing a time.
  - **Expected:** The summary shows the correct participant names and email addresses and displays the currently selected date and time.