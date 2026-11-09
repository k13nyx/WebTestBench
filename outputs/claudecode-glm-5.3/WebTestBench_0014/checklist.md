# Test Checklist

## Functionality
- [ ] FT-01: Organizer can create a new event with core fields
  - Action: Open the event creation page and fill in Title, Date & Time, Location, and Category, then click the "Create Event" button.
  - Expected: Event is created and appears in the events list with all four entered values displayed correctly.

- [ ] FT-02: Optional sections (schedule, dress code, special instructions) can be added to an event
  - Action: While creating (or editing) an event, fill in the optional Schedule, Dress Code, and Special Instructions sections and save.
  - Expected: The event saves successfully and each optional section's content is stored and shown on the event page.

- [ ] FT-03: Organizer can define multiple invitation options for an event
  - Action: In the event editor, add three invitation options (e.g., "Dinner only", "Drinks only", "Full evening") and save the event.
  - Expected: All three invitation options appear on the event's guest page and are selectable during RSVP.

- [ ] FT-04: Organizer can define preference questions for an event
  - Action: In the event editor, add a preference question (e.g., "Meal choice" with options, or "Activity preference") and save the event.
  - Expected: The preference question and its answer choices appear on the event's guest page as part of the RSVP flow.

- [ ] FT-05: Guest can RSVP with "Yes", "No", or "Maybe" and pick an invitation option
  - Action: Open an existing event's shared page as a guest, select an invitation option, choose the "Yes" (or "No"/"Maybe") response, and submit.
  - Expected: The RSVP is recorded with the selected response and invitation option.

- [ ] FT-06: Guest can answer preference questions during RSVP
  - Action: While completing an RSVP (responding "Yes"), select an answer for the preference question (e.g., a meal choice) and submit.
  - Expected: The selected preference answer is saved together with the RSVP.

- [ ] FT-07: Guest can vote in the event poll
  - Action: On an existing event's shared page, vote for one of the poll options (e.g., a venue or activity option).
  - Expected: The vote is recorded and reflected in the poll's results.

- [ ] FT-08: Guest can post a message in the comment thread
  - Action: On an existing event's shared page, type a short message into the comment input and post it.
  - Expected: The message is posted and visible in the event's comment thread.

- [ ] FT-09: Organizer can change event details after invites are sent
  - Action: Open an existing event that already has guest responses, edit its details (e.g., change the time or location), and save.
  - Expected: The change is saved and the updated detail is shown on the event page; existing RSVPs/poll votes are not lost.

- [ ] FT-10: Organizer can view a summary grouped by invitation option, response, and preferences
  - Action: Open an existing event's summary/results view.
  - Expected: The summary lists guests grouped by invitation option, by RSVP response (Yes/No/Maybe), and by their preference answers.

- [ ] FT-11: Canceled or past events are accessible in a separate area with final results
  - Action: Open the separate area for canceled/past events and select one of them.
  - Expected: The event is viewable there, showing its final RSVP results and final poll results.

## Constraint
- [ ] CS-01: Event cannot be created without required fields
  - Action: On the creation page, leave Title (or Date/Location/Category) empty and attempt to save.
  - Expected: The event is not created and a validation message identifies the missing required field(s).

- [ ] CS-02: Closed RSVPs reject new responses
  - Action: As organizer, close RSVPs for an event, then as a guest attempt to submit an RSVP.
  - Expected: The RSVP cannot be submitted; the RSVP section shows it is closed.

- [ ] CS-03: Closed poll rejects new votes
  - Action: As organizer, close the poll for an event, then as a guest attempt to vote.
  - Expected: The vote is not recorded; the poll shows results but voting is disabled.

- [ ] CS-04: Empty comment cannot be posted
  - Action: On an event page, click the comment post button with an empty comment input.
  - Expected: No comment is added to the thread (a validation message may appear).

## Interaction
- [ ] IX-01: Creating an event shows a success confirmation
  - Action: Fill all required fields on the creation page and click "Create Event".
  - Expected: A success message (or clear confirmation) appears and the user is directed to the new event page.

- [ ] IX-02: Poll results update immediately after a guest votes
  - Action: On an event page, vote for a poll option.
  - Expected: The poll's displayed vote counts/results update instantly to include the new vote without a page reload error.

- [ ] IX-03: Posted comment appears in the thread immediately
  - Action: Post a comment on an event page.
  - Expected: The new comment appears at the top/bottom of the thread right away, without needing to leave and return to the page.

## Content
- [ ] CT-01: Event page displays all details exactly as entered
  - Action: Open an existing event page and compare Title, Date & Time, Location, Category, Schedule, Dress Code, and Special Instructions against what was entered/saved.
  - Expected: Every field's content matches the saved values with no truncation, placeholder text, or missing sections.

- [ ] CT-02: Guest page content matches the organizer's definitions
  - Action: On an existing event's guest page, verify the invitation options, preference questions, and poll choices shown to guests.
  - Expected: The labels and choices shown to guests exactly match those the organizer defined for that event, with no extra or missing options.