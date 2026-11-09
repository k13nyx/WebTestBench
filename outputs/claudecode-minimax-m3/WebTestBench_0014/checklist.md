The working directory is empty (no app source to inspect), so I'll generate the checklist directly from the instruction, decomposing each requirement into binary, debuggable items.

# Test Checklist

> **Test data note:** Use the application's default/pre-seeded events, guests, and responses wherever they exist. Only create a new event where an item explicitly tests event creation (FT-01, FT-02) or where no default event is available to exercise a flow.

## Functionality

- [ ] **FT-01**: Organizer can create an event with title, date, time, location, and category
  - Action: Open the event creation form; enter a title, a date, a time, a location, and select a category; save the event.
  - Expected: The event is created and appears in the event list/area with the title, date, time, location, and category as entered.

- [ ] **FT-02**: Organizer can add the optional schedule, dress code, and special instructions sections to an event
  - Action: Create or edit an event and fill in Schedule, Dress code, and Special instructions; save.
  - Expected: All three optional values are stored and re-displayed on the event's detail/shared page; they do not appear when left blank.

- [ ] **FT-03**: Organizer can define multiple invitation options for one event
  - Action: On an event, add invitation options named "Dinner only", "Drinks only", and "Full evening".
  - Expected: All three options are listed under that event with the exact names entered, and each remains individually selectable by guests.

- [ ] **FT-04**: Organizer can add simple preference questions to an event
  - Action: On an event, add a preference question (e.g., "Meal choice" with options "Vegan" / "Standard", and "Activity preference" with options "Hiking" / "Dinner").
  - Expected: Both questions with their answer choices are saved and shown on the event's shared page.

- [ ] **FT-05**: Guest can RSVP with a Yes, No, or Maybe response and select an invitation option
  - Action: Open the shared event page, select response "Yes", pick invitation option "Dinner only", and submit the RSVP.
  - Expected: The RSVP is recorded for that guest with response "Yes" and invitation option "Dinner only"; repeating with "No" and "Maybe" records those responses instead.

- [ ] **FT-06**: Guest answers the event's preference questions when RSVPing
  - Action: RSVP to an event that has preference questions, choosing an answer for each question, and submit.
  - Expected: The RSVP is accepted and each selected preference answer is stored against that guest's RSVP.

- [ ] **FT-07**: Guest can vote in the event's poll for venue/activity options
  - Action: Open the shared event page, find the poll section, and select one poll option (e.g., "Rooftop terrace" vs "Garden hall").
  - Expected: The guest's vote is counted for the selected option and the poll reflects the guest's choice.

- [ ] **FT-08**: Guest can post a short message or question in the event's comment thread
  - Action: On the shared event page, type a short message in the comment box and submit.
  - Expected: The message is added to the comment thread and is visible to guests viewing the same event page.

- [ ] **FT-09**: Organizer can change event details after invitations have been sent
  - Action: On an event that already has RSVPs, change the location and time, then save.
  - Expected: The update saves successfully and the shared event page shows the new location and time instead of the previous values.

- [ ] **FT-10**: Organizer can view a summary grouping guests by invitation option, response, and key preferences
  - Action: Open the summary/report view for an event that has guests with varied invitation options, Yes/No/Maybe responses, and answered preference questions.
  - Expected: The summary lists guests grouped under each invitation option, under each response value (Yes, No, Maybe), and shows each guest's preference answers.

- [ ] **FT-11**: Past and canceled events remain accessible in a separate area with their final RSVP and poll results
  - Action: Cancel one event and/or move to an event whose date has passed, then open the separate past/canceled events area.
  - Expected: The event is listed in that separate area, is no longer shown as an active upcoming event, and displays its final RSVP tally and poll results per option.

## Constraint

- [ ] **CS-01**: An event cannot be saved while required fields are empty
  - Action: Open the event form, leave Title, Date, Time, Location, or Category blank, and attempt to save.
  - Expected: Saving is blocked and a validation message identifies each missing required field; no event is created.

- [ ] **CS-02**: Closing RSVP prevents guests from submitting or changing an RSVP
  - Action: As organizer, close RSVPs for an event; then as a guest attempt to submit a new RSVP and attempt to change an existing one.
  - Expected: Both RSVP attempts are rejected or the RSVP controls are disabled, and the guest's stored response remains unchanged.

- [ ] **CS-03**: Closing the poll prevents further votes
  - Action: As organizer, close the poll; then as a guest attempt to select a poll option and submit a vote.
  - Expected: The vote is rejected or the poll options are non-selectable, and the previously recorded vote count does not change.

- [ ] **CS-04**: Editing an event after invites are sent preserves existing RSVPs, guest data, and poll votes
  - Action: On an event with at least one RSVP and one poll vote, change the event's title and save; then open the summary and the poll.
  - Expected: The existing guest RSVP responses, invitation option selections, preference answers, and poll votes are all still present and unchanged.

## Interaction

- [ ] **IX-01**: Saving a new event confirms success and places the event in the list
  - Action: Create an event with a distinct title and save it.
  - Expected: A success confirmation message appears and the new event is immediately listed among the organizer's events.

- [ ] **IX-02**: A guest's selected RSVP response is visibly active and summary counts update without a manual page reload
  - Action: As a guest submit an RSVP of "Yes"; observe the RSVP control and the summary counts.
  - Expected: The "Yes" option shows as the selected/active state (and No/Maybe show as unselected), and the summary's Yes count increments immediately.

- [ ] **IX-03**: Poll voting and comment posting give immediate on-screen feedback
  - Action: Vote for one poll option, then post a comment; observe the poll section and the comment thread.
  - Expected: The voted option becomes marked as the guest's choice and its vote count increases, and the new comment appears in the thread immediately with the guest's name.

## Content

- [ ] **CT-01**: The shared event page shows the event's core details exactly as entered
  - Action: Create an event with distinctive values for title, date, time, location, and category, then open its shared page.
  - Expected: The page displays the exact title, date, time, location, and category text entered, with no truncation, reformatting, or placeholder text.

- [ ] **CT-02**: The shared event page shows the optional sections, invitation options, and preference questions verbatim
  - Action: Open the shared page of an event that has schedule, dress code, special instructions, three invitation options, and two preference questions.
  - Expected: Schedule, dress code, and special instructions show the entered content; the invitation options appear as "Dinner only", "Drinks only", "Full evening"; each preference question appears with its exact wording and answer choices.

- [ ] **CT-03**: The summary and the archived events area display the correct guest, RSVP, preference, and poll-result data
  - Action: Open the summary for an event with guests across multiple invitation options and Yes/No/Maybe responses, and open a past/canceled event in the separate area.
  - Expected: Each guest's name appears under the correct invitation option and the correct response group with their preference answers; the archived event shows its final RSVP tally per response and its poll result per option.