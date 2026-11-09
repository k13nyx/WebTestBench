# Test Checklist

## Functionality
- [ ] FT-01: User can create an event with all core fields — title, date, time, location, and category.
  - Action: Open the event creation form, fill in title "Summer Dinner Party", date, time, location "Rooftop Terrace", category "Dinner", and submit.
  - Expected: Event is created and appears with the entered title "Summer Dinner Party" in the events list.
- [ ] FT-02: User can add the optional sections schedule, dress code, and special instructions to an event.
  - Action: While creating/editing an event, fill the optional "Schedule", "Dress Code", and "Special Instructions" fields (e.g., dress code "Cocktail attire") and save.
  - Expected: All three sections are saved and displayed on the event page with the entered text.
- [ ] FT-03: User can define multiple invitation options for one event (e.g., "Dinner only", "Drinks only", "Full evening").
  - Action: In the event editor, add three invitation options named "Dinner only", "Drinks only", and "Full evening", then save.
  - Expected: All three invitation options are listed on the event and selectable when guests RSVP.
- [ ] FT-04: User can add simple preference questions (e.g., meal choice) that guests answer when RSVPing.
  - Action: In the event editor, add a preference question "Meal choice?" with options (e.g., "Veg", "Meat"), save, then view the event's RSVP form as a guest.
  - Expected: The question "Meal choice?" appears on the RSVP form with its options selectable.
- [ ] FT-05: Guest can RSVP as "Yes", "No", or "Maybe" and answer the preference questions in the same flow.
  - Action: On the guest event page, select an invitation option, choose a preference answer, set RSVP to "Maybe", and submit.
  - Expected: RSVP "Maybe" is recorded, shown on the page, and the chosen preference answer is saved with the response.
- [ ] FT-06: Guests can access a shared event page showing the event's details.
  - Action: Open the event's shared/guest link for a created event.
  - Expected: Page shows the event title, date/time, location, category, and the optional sections exactly as configured.
- [ ] FT-07: Guests can vote in the event poll for picking between venue or activity options.
  - Action: On the guest event page, locate the poll and select one of its options (e.g., "Rooftop"), then submit the vote.
  - Expected: The vote is recorded and reflected in the poll results for that option.
- [ ] FT-08: Guests can post a short message or question in the event's comment thread.
  - Action: On the guest event page, type "What time should we arrive?" in the comment box and post it.
  - Expected: The comment appears in the thread attributed to the guest.
- [ ] FT-09: Host can change event details after invites are sent, and the change is visible to guests.
  - Action: After at least one RSVP exists, edit the event's location from "Rooftop Terrace" to "Garden Hall" and save, then reload the guest event page.
  - Expected: Guest page now shows location "Garden Hall".
- [ ] FT-10: Host can close RSVPs at any time.
  - Action: On the host event management view, click the control to close RSVPs (e.g., "Close RSVPs").
  - Expected: RSVP status becomes closed and guests can no longer submit or change a response.
- [ ] FT-11: Host can close the poll at any time.
  - Action: On the host event management view, click the control to close the poll.
  - Expected: Poll status becomes closed; final vote results remain visible but voting is disabled.
- [ ] FT-12: Host can view a summary grouping guests by invitation option, response, and key preferences.
  - Action: With several guests having RSVPed with different invitation options and preference answers, open the event summary view.
  - Expected: Guests are grouped by invitation option (e.g., "Full evening"), by response (Yes/No/Maybe), and their preference answers are visible per group.
- [ ] FT-13: Canceled or past events remain accessible in a separate area with their final RSVP and poll results.
  - Action: Cancel an event that has RSVPs and poll votes (or use an event whose date has passed), then open the past/canceled events area and open that event.
  - Expected: The event is listed in the separate area and its final RSVP responses and final poll results are displayed.

## Constraint
- [ ] CS-01: Event cannot be created with required fields empty.
  - Action: Open the event creation form, leave title/date/location empty, and click the create/submit button.
  - Expected: Submission is blocked and a validation message indicates the missing required fields; no event is created.
- [ ] CS-02: When RSVPs are closed, guests cannot submit or change their response.
  - Action: Close RSVPs on an event, then as a guest attempt to change the RSVP to "Yes" and submit.
  - Expected: The RSVP controls are disabled/absent and no change to the recorded response occurs.
- [ ] CS-03: When the poll is closed, guests cannot vote or change their vote.
  - Action: Close the poll on an event, then as a guest attempt to select a poll option and vote.
  - Expected: Voting controls are disabled/absent and vote counts remain unchanged.

## Interaction
- [ ] IX-01: A newly posted comment appears in the thread immediately without a page reload.
  - Action: As a guest, post the comment "Looking forward to it!" and observe the thread without navigating away.
  - Expected: The comment "Looking forward to it!" appears in the thread right away.
- [ ] IX-02: Poll results update visibly after a guest votes.
  - Action: As a guest, vote for option "Rooftop" in an open poll and observe the poll display.
  - Expected: The count or percentage for "Rooftop" increases immediately to include the new vote.
- [ ] IX-03: The system shows confirmation feedback when a key action succeeds (event created or RSVP submitted).
  - Action: Create an event, then submit an RSVP as a guest, observing the UI after each action.
  - Expected: A visible success indication (e.g., toast or confirmation message) appears for each successful action.

## Content
- [ ] CT-01: The summary view's counts and groupings match the actual RSVP data.
  - Action: With known responses (e.g., 2 "Yes" for "Dinner only", 1 "No"), compare the summary view numbers and group membership against the guest RSVP list.
  - Expected: Each group's guest count and preference breakdown exactly matches the recorded RSVPs.