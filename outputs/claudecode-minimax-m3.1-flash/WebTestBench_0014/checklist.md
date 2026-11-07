# Test Checklist

## Functionality
- [ ] FT-01: Host can create a new event with core details
  - Action: Open the app, click "Create Event", fill in Title, Date, Time, Location, and Category (using a default/pre-seeded event's data pattern), and save.
  - Expected: The event is saved and appears in the active/upcoming events list, and its title, date, time, location, and category are shown on the event's detail page.
- [ ] FT-02: Host can add optional schedule, dress code, and special instructions sections
  - Action: On the created event, fill the optional fields "Schedule", "Dress Code", and "Special Instructions" and save.
  - Expected: All three values are saved and rendered on the event detail/shared page under their respective labels.
- [ ] FT-03: Host can define multiple invitation options on an event
  - Action: In the event's invitation options editor, add three options named "Dinner only", "Drinks only", and "Full evening", then save.
  - Expected: All three options are listed on the event page and are selectable by guests during RSVP.
- [ ] FT-04: Host can add simple preference questions to an event
  - Action: Add a preference question "Meal choice" (e.g., options "Vegetarian", "Meat") and a question "Activity preference" (e.g., "Swimming", "Hiking"), then save.
  - Expected: Both questions appear on the RSVP form and each guest's answer is stored and shown in the event summary.
- [ ] FT-05: Guest can RSVP with Yes, No, or Maybe and select an invitation option and preferences
  - Action: Open the event's shared page, select RSVP response "Yes", choose invitation option "Full evening", answer "Meal choice" = "Vegetarian" and "Activity preference" = "Hiking", and submit.
  - Expected: The RSVP is recorded and the guest appears in the summary with response Yes, option "Full evening", and the chosen preferences; the RSVP control shows the saved response.
- [ ] FT-06: Guest can vote in a venue/activity poll on the shared event page
  - Action: On the shared event page, find the poll section and select one of the available options (e.g., a venue or activity choice), then submit the vote.
  - Expected: The selected option is marked as the guest's vote and the option's vote count/tally increases by one.
- [ ] FT-07: Guest can post a short message in the comment thread
  - Action: In the comments section of the shared event page, type a short message (e.g., "Can I bring a plus one?") and post it.
  - Expected: The message appears immediately in the thread with the author's name and timestamp, and is visible to other viewers of the page.
- [ ] FT-08: Host can edit event details after invitations have been sent
  - Action: On an event that already has RSVPs, edit the time and location and save.
  - Expected: The changes are reflected on the shared event page and in the event list, and existing RSVPs/comments/poll votes are retained.
- [ ] FT-09: Host can view a guest summary grouped by invitation option, response, and key preferences
  - Action: Open the event's summary/view-guests view for the event with existing RSVPs.
  - Expected: Guests are grouped by invitation option, a separate grouping or breakdown by response (Yes/No/Maybe) is shown, and each guest's preference answers are listed.
- [ ] FT-10: Canceled or past events remain accessible in a separate area with final RSVP and poll results
  - Action: Cancel an event (or use a default past event), then open the "Past / Canceled" (archive) area and select that event.
  - Expected: The archived event opens read-only with its details, the final RSVP list, and the final poll tallies/results visible.

## Constraint
- [ ] CS-01: Required event fields are enforced on create/edit
  - Action: Open "Create Event" and attempt to save with Title empty, then with Date/Time empty, then with Location empty.
  - Expected: Each attempt is rejected with a visible validation error on the offending field, and no event is created or updated.
- [ ] CS-02: Event cannot be saved with an invalid or impossible date/time
  - Action: Enter an end time earlier than the start time (or a malformed date) and attempt to save.
  - Expected: Saving is blocked with a clear validation message and the invalid value is not stored.
- [ ] CS-03: RSVP submissions are blocked after the host closes RSVP
  - Action: As host, close RSVP for the event (e.g., "Close RSVPs" toggle/button); then as a guest open the shared page and try to submit or change an RSVP.
  - Expected: The RSVP options are disabled/read-only, a notice states that RSVPs are closed, and no new or changed response is recorded.
- [ ] CS-04: Poll voting is blocked after the host closes the poll
  - Action: As host, close the poll on the event; then as a guest open the shared page and attempt to select an option and vote.
  - Expected: The poll options are non-selectable, a notice states that the poll is closed, and the vote count/tally does not change.
- [ ] CS-05: A "Yes" RSVP requires an invitation option selection
  - Action: On the RSVP form, choose "Yes" and submit without selecting an invitation option (and without answering required preference questions).
  - Expected: Submission is blocked with a validation message naming the missing field, and no RSVP is recorded.
- [ ] CS-06: Guest cannot submit an empty comment or an over-long one
  - Action: Attempt to post a comment with blank text, then with text beyond the allowed length.
  - Expected: Both attempts are rejected with a clear message, and neither an empty nor an over-long comment appears in the thread.
- [ ] CS-07: Existing responses are preserved when an event is edited
  - Action: Edit an event's title and time/schedule after RSVPs, comments, and poll votes exist, then open the summary and comment thread.
  - Expected: All prior RSVVP responses, preference answers, poll votes, and comments remain present and associated with the correct guests.

## Interaction
- [ ] IX-01: Creating an event gives immediate feedback
  - Action: Save a newly created event.
  - Expected: A success message/toast (e.g., "Event created") appears and the app navigates to or shows the new event.
- [ ] IX-02: Editing an event gives immediate feedback
  - Action: Save changes to an existing event's details.
  - Expected: A confirmation message (e.g., "Event updated") appears and the event page shows the new values.
- [ ] IX-03: RSVP response buttons reflect the current selection
  - Action: Click "Yes", then switch to "No", then to "Maybe" on the RSVP form.
  - Expected: Exactly one response is highlighted/selected at any time, and the currently selected option is visually distinct.
- [ ] IX-04: Poll results update dynamically after voting
  - Action: Vote for a poll option and observe the poll results/tallies without reloading the page.
  - Expected: The chosen option's count and percentage increase, and the option is visibly marked as the guest's selection.
- [ ] IX-05: Closing RSVP or poll updates the shared page state immediately
  - Action: As host, close RSVP (and separately close the poll) and then reload/refresh the shared event page.
  - Expected: The shared page reflects the closed state: RSVP controls disabled with a "RSVPs closed" message and poll controls disabled with a "Poll closed" message.
- [ ] IX-06: Comment posting clears the input and appends the new comment to the top/bottom of the thread
  - Action: Post a comment, then type another message in the same input field.
  - Expected: After posting, the input field is empty, the first comment is visible in the thread, and the second typed message is not posted until explicitly submitted.

## Content
- [ ] CT-01: Event page displays all saved details with correct labels and values
  - Action: Open an event with title, date/time, location, category, schedule, dress code, and special instructions filled in.
  - Expected: Each field appears on the shared event page under its correct label (Title, Date/Time, Location, Category, Schedule, Dress Code, Special Instructions) with the exact saved value.
- [ ] CT-02: Invitation options, preference questions, poll choices, and comments show the host/guest-entered text
  - Action: Compare the invitation option names, preference question text and their answer choices, poll option names, and posted comments on the shared page against what was entered.
  - Expected: All names, question texts, choice labels, and comment messages appear verbatim with no truncation or placeholder text.
- [ ] CT-03: Summary view content is relevant and complete
  - Action: Open the guest summary for an event with Yes/No/Maybe responses and multiple invitation options.
  - Expected: The summary shows the event title and date, group headings for each invitation option and each response type, guest names, and each guest's preference answers — with no blank, "undefined", "null", or irrelevant placeholder entries.