All checklist items have been executed and verified. Final results below.

# Test Result

## Functionality

- [X] **FT-01**: Organizer can create an event with title, date, time, location, and category
  - Action: Open the event creation form; enter a title, a date, a time, a location, and select a category; save the event.
  - Expected: The event is created and appears in the event list/area with the title, date, time, location, and category as entered.

- [X] **FT-02**: Organizer can add the optional schedule, dress code, and special instructions sections to an event
  - Action: Create or edit an event and fill in Schedule, Dress code, and Special instructions; save.
  - Expected: All three optional values are stored and re-displayed on the event's detail/shared page; they do not appear when left blank.

- [X] **FT-03**: Organizer can define multiple invitation options for one event
  - Action: On an event, add invitation options named "Dinner only", "Drinks only", and "Full evening".
  - Expected: All three options are listed under that event with the exact names entered, and each remains individually selectable by guests.

- [X] **FT-04**: Organizer can add simple preference questions to an event
  - Action: On an event, add a preference question (e.g., "Meal choice" with options "Vegan" / "Standard", and "Activity preference" with options "Hiking" / "Dinner").
  - Expected: Both questions with their answer choices are saved and shown on the event's shared page.

- [X] **FT-05**: Guest can RSVP with a Yes, No, or Maybe response and select an invitation option
  - Action: Open the shared event page, select response "Yes", pick invitation option "Dinner only", and submit the RSVP.
  - Expected: The RSVP is recorded for that guest with response "Yes" and invitation option "Dinner only"; repeating with "No" and "Maybe" records those responses instead.

- [X] **FT-06**: Guest answers the event's preference questions when RSVPing
  - Action: RSVP to an event that has preference questions, choosing an answer for each question, and submit.
  - Expected: The RSVP is accepted and each selected preference answer is stored against that guest's RSVP.

- [X] **FT-07**: Guest can vote in the event's poll for venue/activity options
  - Action: Open the shared event page, find the poll section, and select one poll option (e.g., "Rooftop terrace" vs "Garden hall").
  - Expected: The guest's vote is counted for the selected option and the poll reflects the guest's choice.

- [X] **FT-08**: Guest can post a short message or question in the event's comment thread
  - Action: On the shared event page, type a short message in the comment box and submit.
  - Expected: The message is added to the comment thread and is visible to guests viewing the same event page.

- [X] **FT-09**: Organizer can change event details after invitations have been sent
  - Action: On an event that already has RSVPs, change the location and time, then save.
  - Expected: The update saves successfully and the shared event page shows the new location and time instead of the previous values.

- [X] **FT-10**: Organizer can view a summary grouping guests by invitation option, response, and key preferences
  - Action: Open the summary/report view for an event that has guests with varied invitation options, Yes/No/Maybe responses, and answered preference questions.
  - Expected: The summary lists guests grouped under each invitation option, under each response value (Yes, No, Maybe), and shows each guest's preference answers.

- [ ] **FT-11**: Past and canceled events remain accessible in a separate area with their final RSVP and poll results
  - Action: Cancel one event and/or move to an event whose date has passed, then open the separate past/canceled events area.
  - Expected: The event is listed in that separate area, is no longer shown as an active upcoming event, and displays its final RSVP tally and poll results per option.
  - Bug Report:
    - Issue: Missing Data / Incomplete Render in Archive View (poll results per option not displayed)
    - Actual: Canceling "Marcus's 40th Birthday Bash" produced the toast "Event canceled" and the badge changed to "Canceled"; the event was removed from the Dashboard "Upcoming Events" list (Active Events dropped from 3 to 2, `marcusOnDashboard: false`) and appeared in Archive → "Canceled (2)" with the final RSVP tally "2 yes · 1 pending". However the archived card renders no poll results: the event's own detail page shows the poll "What decade's music should dominate the dance floor?" with per-option results ("80s Classics 1 vote (50%)", "90s Hits 0 votes (0%)", "2000s Bangers 1 vote (50%)", "Mix it up! 0 votes (0%)", "2 total votes"), while the Archive page text contains no "votes (" / "total votes" for any card (`canceledHasPollWords: false`) even though its own heading reads "View past and canceled events with their final RSVP and poll results." The same is true for the Past Events card ("Annual Company Holiday Party", Completed, "2 yes"), which shows no poll result per option.

## Constraint

- [ ] **CS-01**: An event cannot be saved while required fields are empty
  - Action: Open the event form, leave Title, Date, Time, Location, or Category blank, and attempt to save.
  - Expected: Saving is blocked and a validation message identifies each missing required field; no event is created.
  - Bug Report:
    - Issue: Missing / Non-identifying Validation Message (only native browser validation bubble, no in-app field-level feedback)
    - Actual: Submitting the empty Create Event form was blocked (path stayed "/create", form still rendered, no event created), but no in-app validation message was rendered and no toast appeared (`toasts: []` after submit — the app's own "Please fill in all required fields" toast never fires because native validation stops the submit handler). The only feedback was the browser's native bubble "Please fill out this field." on the first empty field, with focus moved to `#title`; the DOM showed 4 invalid fields — `#title`, `#date`, `#time`, `#location` — each carrying the same generic message "Please fill out this field.", so no message identifies each missing required field. Additionally the Category cannot be left blank as the checklist action assumes: its label has no required marker and its Radix combobox is pre-set to "🎉 Social", so it is never part of the required-field validation set.

- [X] **CS-02**: Closing RSVP prevents guests from submitting or changing an RSVP
  - Action: As organizer, close RSVPs for an event; then as guest attempt to submit a new RSVP and attempt to change an existing one.
  - Expected: Both RSVP attempts are rejected or the RSVP controls are disabled, and the guest's stored response remains unchanged.

- [X] **CS-03**: Closing the poll prevents further votes
  - Action: As organizer, close the poll; then as guest attempt to select a poll option and submit a vote.
  - Expected: The vote is rejected or the poll options are non-selectable, and the previously recorded vote count does not change.

- [X] **CS-04**: Editing an event after invites are sent preserves existing RSVPs, guest data, and poll votes
  - Action: On an event with at least one RSVP and one poll vote, change the event's title and save; then open the summary and the poll.
  - Expected: The existing guest RSVP responses, invitation option selections, preference answers, and poll votes are all still present and unchanged.

## Interaction

- [X] **IX-01**: Saving a new event confirms success and places the event in the list
  - Action: Create an event with a distinct title and save it.
  - Expected: A success confirmation message appears and the new event is immediately listed among the organizer's events.

- [X] **IX-02**: A guest's selected RSVP response is visibly active and summary counts update without a manual page reload
  - Action: As a guest submit an RSVP of "Yes"; observe the RSVP control and the summary counts.
  - Expected: The "Yes" option shows as the selected/active state (and No/Maybe show as unselected), and the summary's Yes count increments immediately.

- [X] **IX-03**: Poll voting and comment posting give immediate on-screen feedback
  - Action: Vote for one poll option, then post a comment; observe the poll section and the comment thread.
  - Expected: The voted option becomes marked as the guest's choice and its vote count increases, and the new comment appears in the thread immediately with the guest's name.

## Content

- [X] **CT-01**: The shared event page shows the event's core details exactly as entered
  - Action: Create an event with distinctive values for title, date, time, location, and category, then open its shared page.
  - Expected: The page displays the exact title, date, time, location, and category text entered, with no truncation, reformatting, or placeholder text.

- [X] **CT-02**: The shared event page shows the optional sections, invitation options, and preference questions verbatim
  - Action: Open the shared page of an event that has schedule, dress code, special instructions, three invitation options, and two preference questions.
  - Expected: Schedule, dress code, and special instructions show the entered content; the invitation options appear as "Dinner only", "Drinks only", "Full evening"; each preference question appears with its exact wording and answer choices.

- [ ] **CT-03**: The summary and the archived events area display the correct guest, RSVP, preference, and poll-result data
  - Action: Open the summary for an event with guests across multiple invitation options and Yes/No/Maybe responses, and open a past/canceled event in the separate area.
  - Expected: Each guest's name appears under the correct invitation option and the correct response group with their preference answers; the archived event shows its final RSVP tally per response and its poll result per option.
  - Bug Report:
    - Issue: Missing Data in Archived Events View (poll results per option absent; guest names/preferences also not shown in archive)
    - Actual: The event-page summary is correct — "Guest Summary" tabs "By Status" / "By Option" / "Preferences" list guest names under the correct group (e.g. Attending (2): Amanda Foster, Chris Johnson; Pending (1): Nina Patel; options and preference answers listed per guest). But in the separate archived area the poll results are never rendered: Archive → Canceled shows "Sarah & James's Garden Wedding (Updated)" with the per-response tally "2 yes · 1 maybe · 1 pending" and "Marcus's 40th Birthday Bash" with "2 yes · 1 pending", yet no card shows any per-option poll result (no "votes (" / "total votes" text anywhere in the Archive page), even though the same event's poll on its detail page shows "80s Classics 1 vote (50%) … 2 total votes". The archived area also renders only the RSVP tally — no guest names, invitation-option grouping, or preference answers — so the archived "final RSVP and poll results" area is missing the poll-result and guest-detail data the checklist requires.

---

**Execution notes (evidence context, not a summary of the above):**
- The app is a purely client-side React/Vite SPA: state is seeded from `src/data/mockEvents.ts`, with no backend API and no `localStorage`/`sessionStorage`. A full page load therefore discards all runtime changes, so every mutation was performed with in-app (client-side) navigation only; one event created early in the run was lost by an unavoidable reload and was re-created.
- RSVP/poll/comment mutations were exercised on the pre-seeded event `Marcus's 40th Birthday Bash` (`/event/2`), which is the only seeded event with guests bound to a guest id, poll votes and comments; a runtime-created event has no guest records, so a guest RSVP submitted on it produces a success toast ("RSVP updated successfully!") but is never stored (Guest Summary shows "No guests" in all four groups).
- Radix widgets needed real input events: `TabsTrigger` activates on `mousedown` (JS `.click()` does not switch tabs), and the Category control is a Radix combobox, not a `<select>`.
- Key DOM evidence gathered: create-form submit on empty fields (4 `:invalid` inputs, focus on `#title`, zero toasts), created-event detail text ("Zephyr Lakeside Picnic / Saturday, December 5, 2026 / 11:00 AM - 3:00 PM / Zephyr Lakeside Pavilion / ✨ Celebration / Dress Code / Special Instructions / Schedule 11:30 Picnic Lunch"), dashboard card for the new event, cancel flow dialog ("Cancel this event? … Keep Event / Cancel Event", toast "Event canceled"), archive tab counts ("Past Events (1)", "Canceled (2)") and full card text.