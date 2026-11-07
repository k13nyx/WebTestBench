# Test Checklist

## Functionality

- [ ] FT-01: Create an event with all required fields
  - Action: On the event creation page, fill Title, Date and Time, Location, select a Category, then save.
  - Expected: Event is saved and appears in the events list showing that title, date/time, location and category.

- [ ] FT-02: Add optional sections (schedule, dress code, special instructions)
  - Action: In the create form, enter content into Schedule, Dress Code and Special Instructions, then save and open the shared event page.
  - Expected: All three sections render on the shared page with the exact content entered.

- [ ] FT-03: Define multiple invitation options for an event
  - Action: In the event form, add three invitation options: "Dinner only", "Drinks only", "Full evening"; save and open the shared event page.
  - Expected: All three named options are listed and selectable in the guest RSVP area.

- [ ] FT-04: Define preference questions for an event
  - Action: In the event form, add a preference question (e.g., "Meal choice") with at least two choices; save and open the shared event page.
  - Expected: The question and its choices are presented in the RSVP form for the guest to answer.

- [ ] FT-05: Guest RSVPs "Yes" with an invitation option and preference answers
  - Action: On the shared page, as a guest, select "Yes", choose one invitation option, answer the preference question, and submit the RSVP.
  - Expected: RSVP is recorded as "Yes" and the guest is listed under the chosen invitation option with the preference answer saved.

- [ ] FT-06: Guest RSVPs "No" and "Maybe"
  - Action: As a second guest select "No" and submit; as a third guest select "Maybe" and submit.
  - Expected: Both responses are recorded with statuses "No" and "Maybe"; neither requires an invitation option or preference answer.

- [ ] FT-07: Guest votes in the event poll
  - Action: On the shared event page, in the poll section, select one of the listed venue/activity options and submit the vote.
  - Expected: The vote is counted and the poll results show updated counts/percentages per option including the new vote.

- [ ] FT-08: Guest posts a message in the comment thread
  - Action: In the comment thread section, type a short message/question and post it.
  - Expected: The message appears in the thread with the guest's name and remains visible on reload of the shared page.

- [ ] FT-09: Organizer edits event details after invites are sent
  - Action: Open an event that already has guest RSVPs, change the Location and Time, and save.
  - Expected: The shared event page displays the updated location and time for guests.

- [ ] FT-10: Organizer views the grouped guest summary
  - Action: Open the summary/dashboard view for an event that has multiple guest responses.
  - Expected: Guests are grouped by invitation option, by response (Yes/No/Maybe), and key preference answers are listed with counts.

- [ ] FT-11: Organizer closes RSVPs and polls at any time
  - Action: From the organizer controls, close RSVPs for the event, then close the poll.
  - Expected: Both the RSVP section and the poll display a "Closed" status in the organizer and shared views.

- [ ] FT-12: Canceled/past events are accessible in a separate area with final results
  - Action: Cancel an event (or open an event whose date has passed), then open the Past/Canceled events area.
  - Expected: The event is listed there (not in the active list) and shows final RSVP results by response/invitation option plus final poll results.

## Constraint

- [ ] CS-01: Event cannot be saved without required fields
  - Action: On the creation form, leave Title and Date and Time empty and attempt to save.
  - Expected: Save is blocked, inline validation messages appear for Title and Date and Time, and no event is created.

- [ ] CS-02: Closed RSVPs and polls reject further guest input
  - Action: On an event where RSVPs and the poll were closed, open the shared page as a guest and attempt to submit an RSVP and a poll vote.
  - Expected: RSVP options (Yes/No/Maybe) and poll options are disabled or not selectable, and no response or vote is recorded.

- [ ] CS-03: Editing event details does not clear existing guest data
  - Action: Note the current RSVP list, poll vote counts and comments; edit the event title/description and save; re-check those areas.
  - Expected: All existing RSVPs, poll votes and comments remain unchanged after the edit.

- [ ] CS-04: Empty comment cannot be posted
  - Action: In the comment thread, submit with an empty or whitespace-only message.
  - Expected: No new entry is added to the thread (post control disabled or submission rejected).

## Interaction

- [ ] IX-01: Selecting "Yes" reveals invitation option and preference questions
  - Action: On the shared page RSVP area, select "No", then change the selection to "Yes".
  - Expected: Choosing "Yes" displays the invitation option selector and the preference questions; "No" does not show them as required inputs.

- [ ] IX-02: Confirmation feedback is shown after an RSVP is submitted
  - Action: As a guest on the shared page, submit an RSVP response.
  - Expected: A confirmation message/notice appears indicating the response was recorded, and the RSVP area reflects the submitted response.

## Content

- [ ] CT-01: Shared event page shows correct event identity content
  - Action: Open the shared page of an existing default event and compare displayed details with the event's stored details.
  - Expected: Title, date and time, location and category are all displayed and match the event record exactly.

- [ ] CT-02: Optional sections appear only when they have content
  - Action: Open the shared page of a default event that has no Schedule/Dress Code/Special Instructions entered.
  - Expected: No empty "Schedule", "Dress Code" or "Special Instructions" headings or placeholder text are displayed.