# Test Checklist

## Functionality
- [ ] FT-01: Create event with all core fields
  - Action: Open the event creation form, fill in title, date & time, location, and category, then submit.
  - Expected: Event is created and appears in the organizer's event list with all entered details shown correctly.

- [ ] FT-02: Add optional sections to an event
  - Action: While creating/editing an event, fill in the optional "Schedule", "Dress code", and "Special instructions" sections and save.
  - Expected: All three sections are displayed on the shared event page with the entered content.

- [ ] FT-03: Define multiple invitation options
  - Action: Add at least two invitation options (e.g., "Dinner only", "Drinks only", "Full evening") to an event and save.
  - Expected: All defined options appear on the event's invitation/RSVP interface for guests to select.

- [ ] FT-04: Add preference questions to an event
  - Action: Create a preference question (e.g., "Meal choice" with options Vegetarian/Non-vegetarian) attached to the event and save.
  - Expected: The question and its answer options are rendered on the RSVP form.

- [ ] FT-05: Guest submits RSVP with response and preferences
  - Action: On the shared event page, open RSVP as "Yes", select an invitation option (e.g., "Full evening"), answer the preference question, and submit.
  - Expected: RSVP is recorded and the guest's response, chosen invitation option, and preference answers are visible in the organizer's summary.

- [ ] FT-06: RSVP "No" and "Maybe" responses
  - Action: Submit two more RSVPs on the same event, one marked "No" and one "Maybe".
  - Expected: Both responses are saved and listed under the correct response group in the summary.

- [ ] FT-07: Guest poll voting
  - Action: On the event page's poll (e.g., venue options "Rooftop Bar" vs "Garden Hall"), select one option and submit the vote.
  - Expected: The vote is recorded and current tallies are displayed for each poll option.

- [ ] FT-08: Comment thread posting
  - Action: Type a short message in the event page's comment input and submit.
  - Expected: The comment appears in the thread with the guest's name/identifier and is visible to other visitors of the page.

- [ ] FT-09: Edit event details after invites are sent
  - Action: Open an existing event with RSVPs already recorded, change the date/time and location, and save.
  - Expected: The shared event page immediately shows the updated details; existing RSVPs, poll votes, and comments are preserved.

- [ ] FT-10: View grouped RSVP summary
  - Action: Open the organizer summary view for an event with multiple guests.
  - Expected: Guests are grouped by invitation option, by response ("Yes"/"No"/"Maybe"), and key preferences (e.g., meal counts) are displayed per group.

- [ ] FT-11: Archive area for canceled/past events
  - Action: Cancel an event (or open one whose date has passed) and navigate to the separate "past/canceled events" area.
  - Expected: The event appears there with its final RSVP counts and final poll results still readable.

## Constraint
- [ ] CS-01: Required fields enforced on event creation
  - Action: Attempt to submit the event form with the title or date/time left empty.
  - Expected: Submission is blocked and a validation message names the missing required field.

- [ ] CS-02: Close RSVPs
  - Action: As organizer, close RSVPs for an open event, then try to submit a new RSVP or change an existing one as a guest.
  - Expected: RSVP form is no longer submittable; the page shows RSVPs are closed, and no new/changed responses are recorded.

- [ ] CS-03: Close poll
  - Action: As organizer, close the event poll, then try to cast or change a vote as a guest.
  - Expected: Voting controls are disabled/hidden, results remain visible, and no new votes are accepted.

- [ ] CS-04: One RSVP per guest, one vote per poll option set
  - Action: Attempt to submit a second RSVP for the same guest, and separately try to select two options in the single-choice poll.
  - Expected: Duplicate RSVP is rejected or replaces the prior one (never creates two entries); poll allows only one selection at a time.

## Interaction
- [ ] IX-01: Confirmation feedback after RSVP submission
  - Action: Submit an RSVP on the shared event page.
  - Expected: A success confirmation (toast/message) appears and the guest's recorded response is shown; error feedback appears if submission fails.

- [ ] IX-02: Live poll result update after voting
  - Action: Cast a vote, then reload/revisit the event page as another guest.
  - Expected: Poll tallies reflect the new vote (bar/counts updated), not the stale pre-vote state.

- [ ] IX-03: Hidden optional sections when empty
  - Action: View a shared event page for an event where schedule, dress code, and special instructions were left blank.
  - Expected: Those sections are not displayed (no empty headings/placeholders) on the guest-facing page.

## Content
- [ ] CT-01: Event details render consistently across views
  - Action: Compare the event's title, date/time, location, and category shown on the shared event page, the RSVP form, and the organizer summary/archive view.
  - Expected: All views show identical, correctly formatted values matching what the organizer entered (no placeholder text like "Lorem ipsum" or broken/undefined values).

- [ ] CT-02: Category options present and relevant
  - Action: Open the category selector on the event form.
  - Expected: A list of event-planning-relevant categories (e.g., Party, Dinner, Wedding, Meeting) is offered, and the chosen category is shown with the event.