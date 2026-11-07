I've completed all checklist items. Here are the results:

# Test Result

## Functionality

- [X] FT-01: Create an event with all required fields
  - Action: On the event creation page, fill Title, Date and Time, Location, select a Category, then save.
  - Expected: Event is saved and appears in the events list showing that title, date/time, location and category.

- [X] FT-02: Add optional sections (schedule, dress code, special instructions)
  - Action: In the create form, enter content into Schedule, Dress Code and Special Instructions, then save and open the shared event page.
  - Expected: All three sections render on the shared page with the exact content entered.

- [X] FT-03: Define multiple invitation options for an event
  - Action: In the event form, add three invitation options: "Dinner only", "Drinks only", "Full evening"; save and open the shared event page.
  - Expected: All three named options are listed and selectable in the guest RSVP area.

- [X] FT-04: Define preference questions for an event
  - Action: In the event form, add a preference question (e.g., "Meal choice") with at least two choices; save and open the shared event page.
  - Expected: The question and its choices are presented in the RSVP form for the guest to answer.

- [ ] FT-05: Guest RSVPs "Yes" with an invitation option and preference answers
  - Action: On the shared page, as a guest, select "Yes", choose one invitation option, answer the preference question, and submit the RSVP.
  - Expected: RSVP is recorded as "Yes" and the guest is listed under the chosen invitation option with the preference answer saved.
  - Bug Report:
    - Issue: RSVP not persisted (Incorrect Form Submission / Success toast without data write)
    - Actual: On the newly created "QA Grand Gala" event, selecting "Yes" + invitation option "Dinner only" + preference "Steak" and clicking "Submit RSVP" produced the toast "RSVP updated successfully!", but no guest was recorded: Guest Summary showed "Attending (0) / Not Attending (0) / Maybe (0) / Pending (0) — No guests", the "By Option" and "Preferences" tabs were empty, the dashboard card still read "0 yes", and the button remained "Submit RSVP" instead of switching to "Update RSVP". The same flow on a seeded event (event/2) does persist, so newly created events (which have no guest roster) silently drop RSVPs.

- [ ] FT-06: Guest RSVPs "No" and "Maybe"
  - Action: As a second guest select "No" and submit; as a third guest select "Maybe" and submit.
  - Expected: Both responses are recorded with statuses "No" and "Maybe"; neither requires an invitation option or preference answer.
  - Bug Report:
    - Issue: Missing guest identity switching + RSVP not recorded on newly created events
    - Actual: The shared page exposes no control to act as a second or third guest — the only name input on the page is "Your name" inside the Discussion (comment) block, not the RSVP form; the responding guest is fixed by the app. Additionally, any RSVP submitted on a newly created event is not recorded (Guest Summary stays at 0 in every status), so no "No" or "Maybe" response could be recorded there. On seeded events the fixed guest's response does persist (e.g. event/2 changed Attending(2)/Not Attending(0) → Attending(1)/Not Attending(1), then → Maybe(1)), but there is still no way to add distinct second/third guests.

- [X] FT-07: Guest votes in the event poll
  - Action: On the shared event page, in the poll section, select one of the listed venue/activity options and submit the vote.
  - Expected: The vote is counted and the poll results show updated counts/percentages per option including the new vote.

- [X] FT-08: Guest posts a message in the comment thread
  - Action: In the comment thread section, type a short message/question and post it.
  - Expected: The message appears in the thread with the guest's name and remains visible on reload of the shared page.

- [X] FT-09: Organizer edits event details after invites are sent
  - Action: Open an event that already has guest RSVPs, change the Location and Time, and save.
  - Expected: The shared event page displays the updated location and time for guests.

- [X] FT-10: Organizer views the grouped guest summary
  - Action: Open the summary/dashboard view for an event that has multiple guest responses.
  - Expected: Guests are grouped by invitation option, by response (Yes/No/Maybe), and key preference answers are listed with counts.

- [X] FT-11: Organizer closes RSVPs and polls at any time
  - Action: From the organizer controls, close RSVPs for the event, then close the poll.
  - Expected: Both the RSVP section and the poll display a "Closed" status in the organizer and shared views.

- [X] FT-12: Canceled/past events are accessible in a separate area with final results
  - Action: Cancel an event (or open an event whose date has passed), then open the Past/Canceled events area.
  - Expected: The event is listed there (not in the active list) and shows final RSVP results by response/invitation option plus final poll results.

## Constraint

- [ ] CS-01: Event cannot be saved without required fields
  - Action: On the creation form, leave Title and Date and Time empty and attempt to save.
  - Expected: Save is blocked, inline validation messages appear for Title and Date and Time, and no event is created.
  - Bug Report:
    - Issue: Missing inline validation messages (validation relies only on native HTML5 `required`)
    - Actual: Clicking "Create Event" with Title and Start Date/Start Time empty did block submission and no event was created (URL stayed on /create), but no inline validation text was rendered anywhere in the DOM — a scan for error text (`required|please|must|cannot|invalid`) returned an empty list and `aria-invalid="true"` matched 0 elements. Blocking comes solely from the native `required` attribute on the `title`, `date`, `time` and `location` inputs, so no per-field inline messages are shown for Title and Date and Time.

- [X] CS-02: Closed RSVPs and polls reject further guest input
  - Action: On an event where RSVPs and the poll were closed, open the shared page as a guest and attempt to submit an RSVP and a poll vote.
  - Expected: RSVP options (Yes/No/Maybe) and poll options are disabled or not selectable, and no response or vote is recorded.

- [X] CS-03: Editing event details does not clear existing guest data
  - Action: Note the current RSVP list, poll vote counts and comments; edit the event title/description and save; re-check those areas.
  - Expected: All existing RSVPs, poll votes and comments remain unchanged after the edit.

- [X] CS-04: Empty comment cannot be posted
  - Action: In the comment thread, submit with an empty or whitespace-only message.
  - Expected: No new entry is added to the thread (post control disabled or submission rejected).

## Interaction

- [X] IX-01: Selecting "Yes" reveals invitation option and preference questions
  - Action: On the shared page RSVP area, select "No", then change the selection to "Yes".
  - Expected: Choosing "Yes" displays the invitation option selector and the preference questions; "No" does not show them as required inputs.

- [X] IX-02: Confirmation feedback is shown after an RSVP is submitted
  - Action: As a guest on the shared page, submit an RSVP response.
  - Expected: A confirmation message/notice appears indicating the response was recorded, and the RSVP area reflects the submitted response.

## Content

- [X] CT-01: Shared event page shows correct event identity content
  - Action: Open the shared page of an existing default event and compare displayed details with the event's stored details.
  - Expected: Title, date and time, location and category are all displayed and match the event record exactly.

- [X] CT-02: Optional sections appear only when they have content
  - Action: Open the shared page of a default event that has no Schedule/Dress Code/Special Instructions entered.
  - Expected: No empty "Schedule", "Dress Code" or "Special Instructions" headings or placeholder text are displayed.

---

### Notes on verified evidence

- **FT-01** – Card read: `🎂 Birthday | Active | QA Minimal Event | Tuesday, December 15, 2026 | 6:00 PM | QA Minimal Hall`.
- **FT-02** – Shared page rendered `Dress Code → Black tie elegant`, `Special Instructions → Valet parking at the north entrance only.`, `Schedule → 19:30 / Welcome reception / Drinks on arrival`.
- **FT-04** – RSVP form rendered `Meal choice | Steak | Vegetarian` as radio inputs (event record confirmed to store them — the Edit form is correctly pre-populated with "Meal choice").
- **FT-07** – Poll before: `90s Hits 0 votes (0%)`; after clicking it: `90s Hits 1 vote (50%)` with `2 total votes`.
- **FT-08** – Thread showed `AF | Amanda Foster | less than a minute ago | QA test message: what time should we arrive?` and still present after leaving and re-opening the page.
- **FT-09** – `The Skyline Lounge` → `QA Updated Hall`; `7:00 PM - 1:00 AM` → `8:00 PM - 1:00 AM`.
- **FT-10** – By Status: Attending (2) Michael Chen, Emily Watson / Not Attending (1) Lisa Thompson / Maybe (1) David Park / Pending (1) Robert Kim. By Option: Full Celebration (2) / Reception Only (0) / Ceremony Only (0). Preferences: `Meal preference — Filet mignon 1 (50%), Wild mushroom risotto (V) 1 (50%)`, etc.
- **FT-11** – Poll badge `Open` → `Closed`; organizer shows `Open RSVPs` + `RSVPs are currently closed for this event.`; closed RSVP card replaced the Yes/No/Maybe controls entirely.
- **FT-12** – Archive → "Canceled (1)" filter shows `🎉 Social | Canceled | Summer Backyard BBQ … 2 yes`; absent from the active dashboard list; detail shows Attending (2) Jake Williams, Sarah Miller; By Option `All Day (2)`; poll `Cornhole 2 (50%) / Volleyball 1 (25%) / Giant Jenga 1 (25%) / Croquet 0 (0%), 4 total votes`.
- **CS-02** – Poll option button `"Perfect" - Ed Sheeran` reported `disabled`, and poll totals stayed at `3 total votes` after the click attempt; no RSVP controls were present to click.
- **CS-03** – After the edit, poll stayed at `2 total votes`, comment thread at `(1)` Amanda Foster, schedule/dress code intact, and RSVPs unchanged (Attending 1 Chris Johnson, Pending 1 Nina Patel).

### Environment caveat
The app keeps all data in memory: a hard browser reload resets it to the three seeded events, so "reload" for FT-08 was exercised as leaving and re-entering the shared page via in-app navigation.