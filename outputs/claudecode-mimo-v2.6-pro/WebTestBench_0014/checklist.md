# Test Checklist

## Functionality
- [ ] FT-01: Create a new event with the required fields filled in.
  - Action: Open the create-event form, enter Title "Team Offsite Dinner", Date & time, Location "Grand Hall", Category "Social" (leave optional sections empty) and save.
  - Expected: The event is created and appears in the active events list.
- [ ] FT-02: Add the optional sections to an event.
  - Action: On an event's create/edit form, fill in Schedule, Dress code, and Special instructions, then save.
  - Expected: The event saves successfully and all three optional sections are retained.
- [ ] FT-03: Define multiple invitation options for an event.
  - Action: On the event form, add the invitation options "Dinner only", "Drinks only", and "Full evening", then save.
  - Expected: All three invitation options appear as selectable choices on the guest RSVP form.
- [ ] FT-04: Define a preference question for an event.
  - Action: Add the preference question "Meal choice" with the options "Chicken" and "Vegetarian", then save.
  - Expected: The question and both answer choices are presented to guests on the RSVP form.
- [ ] FT-05: Guest submits an RSVP of "Yes".
  - Action: On a default event's shared page, select response "Yes", choose one of the event's invitation options (e.g., "Full evening"), answer each preference question, and submit.
  - Expected: The RSVP is recorded with status "Yes", the selected invitation option, and the preference answers.
- [ ] FT-06: Guest submits an RSVP of "No" or "Maybe".
  - Action: As one guest, submit an RSVP selecting "No"; as a second guest, submit an RSVP selecting "Maybe".
  - Expected: Both RSVPs are recorded with their selected response statuses.
- [ ] FT-07: Create a poll on the shared event page.
  - Action: As event owner, add the poll "Which venue do you prefer?" with the options "Rooftop", "Garden", and "Beach", then save.
  - Expected: The poll with all three options appears on the shared event page.
- [ ] FT-08: Guest votes in the poll.
  - Action: As a guest, select one poll option (e.g., "Rooftop") and submit the vote.
  - Expected: The vote is recorded and counted in the poll's results.
- [ ] FT-09: Guest posts a comment in the comment thread.
  - Action: In the event's comment thread, enter "Can I bring a plus-one?" and post it.
  - Expected: The comment is saved and listed in the comment thread with its full text.
- [ ] FT-10: Change event details after invites are sent.
  - Action: Open a default event that already has RSVPs, change its Location and Date & time, and save.
  - Expected: The updated details are saved and shown on the shared event page; previously recorded RSVPs remain intact.
- [ ] FT-11: Close RSVPs and the poll at any time.
  - Action: As event owner, use the "Close RSVPs" control and the "Close poll" control on the event.
  - Expected: The event's RSVPs and the poll are both set to a closed state in the owner's event controls.
- [ ] FT-12: View the guest summary.
  - Action: Open the event's summary view after several guests have responded.
  - Expected: Guests are grouped by invitation option and by response ("Yes"/"No"/"Maybe"), showing each guest's key preference answers.
- [ ] FT-13: Access canceled and past events in their separate area.
  - Action: Open the separate area for canceled/past events and open one listed event.
  - Expected: The event is listed in that area (not in the active events) and shows its final RSVP and poll results.

## Constraint
- [ ] CS-01: An event cannot be saved with a missing required field.
  - Action: Attempt to save an event with Title empty, then repeat with Date & time, Location, and Category empty in turn.
  - Expected: Every save attempt is blocked with a validation message and no incomplete event is created.
- [ ] CS-02: An RSVP cannot be submitted incomplete.
  - Action: Attempt to submit an RSVP with no response selected; then with "Yes" but no invitation option; then with "Yes" and an option but a preference question unanswered.
  - Expected: All three attempts are blocked with a validation message and no RSVP is recorded.
- [ ] CS-03: Closed RSVPs and a closed poll accept no further input.
  - Action: After closing RSVPs, attempt to submit an RSVP; after closing the poll, attempt to submit a vote.
  - Expected: Both attempts are rejected with a closed message and no RSVP or vote is recorded.

## Interaction
- [ ] IX-01: Submitting an RSVP shows confirmation feedback.
  - Action: Submit a valid RSVP ("Yes" with invitation option and preference answers) and observe the page immediately after submission.
  - Expected: A success confirmation appears stating that the RSVP was recorded.
- [ ] IX-02: The shared event page visibly indicates closed RSVPs and a closed poll.
  - Action: Open the shared event page after RSVPs and the poll have been closed.
  - Expected: RSVP response controls and poll voting controls are disabled or hidden, with a visible "closed" indication.

## Content
- [ ] CT-01: The shared event page content matches the event data exactly.
  - Action: Open a default event's shared page and compare title, date & time, location, category, and any optional sections against the saved event data.
  - Expected: Every displayed value matches the event data exactly, with no missing or altered fields.
- [ ] CT-02: Archived final results match the recorded responses and votes.
  - Action: In the canceled/past events area, open an event and compare its final RSVP and poll results with its recorded guest responses and poll votes.
  - Expected: Final RSVP results and poll results match the recorded data exactly.