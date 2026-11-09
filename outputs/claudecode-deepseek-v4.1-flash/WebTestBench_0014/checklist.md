# Test Checklist

## Functionality
- [ ] FT-01: User can create an event with title, date and time, location, and category.
  - Action: Open "Create Event", fill Title, Date/Time, Location, and Category fields, then save.
  - Expected: A new event is created and appears with all four values displayed correctly.

- [ ] FT-02: User can add optional sections for schedule, dress code, and special instructions.
  - Action: In the event form, fill the Schedule, Dress Code, and Special Instructions sections, then save.
  - Expected: Each provided section is saved and shown on the event page; omitted sections are simply not displayed.

- [ ] FT-03: User can define multiple invitation options for one event.
  - Action: Add invitation options "Dinner only", "Drinks only", and "Full evening" to an event.
  - Expected: All three options are saved and available for guests to choose from when RSVPing.

- [ ] FT-04: User can define preference questions for an event.
  - Action: Add a preference question (e.g., "Meal choice" or "Activity preference") with answer choices.
  - Expected: The preference question and its choices are saved and presented to guests during RSVP.

- [ ] FT-05: Guest can RSVP with Yes, No, or Maybe along with an invitation option and preference answers.
  - Action: As a guest, on the shared event page select "Yes", choose an invitation option, answer the preference question, and submit.
  - Expected: The RSVP is recorded with the selected response, invitation option, and preference answers.

- [ ] FT-06: Shared event page displays event details plus dynamic poll and comment sections.
  - Action: Open the shared event page as a guest.
  - Expected: Event details, a poll, and a comment thread are all visible on the page.

- [ ] FT-07: Guest can vote in the poll to choose between venue or activity options.
  - Action: On the shared event page, select one poll option and submit the vote.
  - Expected: The vote is recorded and reflected in the poll results.

- [ ] FT-08: Guest can post a short message or question in the comment thread.
  - Action: Enter text in the comment field on the shared event page and post it.
  - Expected: The comment appears in the thread attributed to the guest.

- [ ] FT-09: User can change event details after invitations are sent.
  - Action: Edit the title, date/time, location, or category of an event that already has invited guests, then save.
  - Expected: Updated details are saved and shown to guests on the shared event page.

- [ ] FT-10: User can view a summary grouping guests by invitation option, response, and key preferences.
  - Action: Open the event summary view.
  - Expected: Guests are grouped by invitation option, by response (Yes/No/Maybe), and by their preference answers.

- [ ] FT-11: Canceled or past events remain accessible in a separate area with their final RSVP and poll results.
  - Action: Open the "Canceled/Past Events" area and select a canceled or past event.
  - Expected: The event is listed there and shows its final RSVP results and final poll results.

## Constraint
- [ ] CS-01: Event cannot be created while any required field is empty.
  - Action: Attempt to create an event leaving Title, Date/Time, Location, or Category blank.
  - Expected: Creation is blocked and the missing required field is indicated.

- [ ] CS-02: Guests cannot submit an RSVP after RSVPs are closed.
  - Action: Close RSVPs for an event, then open the shared page as a guest and attempt to RSVP.
  - Expected: RSVP submission is disabled/blocked once RSVPs are closed.

- [ ] CS-03: Guests cannot vote in a poll after the poll is closed.
  - Action: Close the poll, then attempt to cast a vote as a guest.
  - Expected: Voting is disabled/blocked once the poll is closed.

- [ ] CS-04: RSVP of "Yes" requires selecting an invitation option and answering the preference question.
  - Action: Select "Yes" and submit without choosing an invitation option or answering the preference question.
  - Expected: Submission is blocked until the required option and preference answer are provided.

## Interaction
- [ ] IX-01: A confirmation is shown after an event is successfully created.
  - Action: Submit a valid new event.
  - Expected: A success confirmation appears and the new event is shown in the events list.

- [ ] IX-02: Poll results update immediately after a guest votes.
  - Action: Cast a vote on the shared event page.
  - Expected: The poll results reflect the new vote without a manual page reload.

- [ ] IX-03: Closing RSVPs or the poll updates the shared page state immediately.
  - Action: Close RSVPs (and separately, the poll) from the event management view, then view the shared page.
  - Expected: The shared page shows RSVP and/or poll as closed with inputs disabled.

## Content
- [ ] CT-01: The shared event page text matches the event's saved details.
  - Action: Compare the displayed title, date/time, location, category, and any provided optional sections against the entered values.
  - Expected: All displayed text matches the saved event details with no missing or mismatched fields.

- [ ] CT-02: All displayed sections and options are relevant to the specific event.
  - Action: Review the shared event page's poll options, invitation options, preference questions, and comments.
  - Expected: Every displayed item relates directly to the event's planning content (no unrelated or placeholder content).