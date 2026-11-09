# Test Checklist

## Functionality
- [ ] FT-01: Create a detailed event with core fields
  - Action: Create a new event entering title, date and time, location, and category, then save.
  - Expected: The event is saved and appears in the active events list with all entered details.
- [ ] FT-02: Include optional sections in an event
  - Action: Create/edit an event filling in schedule, dress code, and special instructions, then open its shared event page.
  - Expected: The shared page displays the schedule, dress code, and special instructions sections with the entered content.
- [ ] FT-03: Define multiple invitation options for an event
  - Action: While creating an event, add invitation options "Dinner only," "Drinks only," and "Full evening," save, then open the shared event page.
  - Expected: All three invitation options are listed and selectable in the RSVP form.
- [ ] FT-04: Guest completes an RSVP with response, invitation option, and preference answers
  - Action: On the shared event page, select RSVP "Yes," choose an invitation option, answer the preference questions (e.g., meal choice), and submit.
  - Expected: The RSVP is recorded with the response, chosen invitation option, and preference answers; the page confirms the submission.
- [ ] FT-05: Guest posts a message in the comment thread
  - Action: Type a short message in the comment box on the shared event page and post it.
  - Expected: The comment appears in the thread with its text visible to all viewers.
- [ ] FT-06: Create a poll and collect votes
  - Action: As host, create a poll with options (e.g., "Rooftop bar" vs "Garden terrace"), then as a guest vote for one option.
  - Expected: The poll shows all options on the shared page, the guest's vote is recorded, and results display vote counts per option.
- [ ] FT-07: Edit event details after invites are sent
  - Action: Change an already-invited event's location and date, save, then reload the shared event page.
  - Expected: The shared event page shows the updated location and date.
- [ ] FT-08: View the RSVP summary
  - Action: Open the event summary view after several guests have RSVPed with different responses, invitation options, and preferences.
  - Expected: Guests are grouped by invitation option, by Yes/No/Maybe response, and by their key preference answers.
- [ ] FT-09: Access canceled or past events in a separate area
  - Action: Navigate to the canceled/past events area and open a canceled (or past) event.
  - Expected: The event is listed in that separate area and its final RSVP summary and final poll results are displayed.

## Constraint
- [ ] CS-01: Prevent creating an event with missing required fields
  - Action: Attempt to save a new event with empty title, date/time, location, or category.
  - Expected: The event is not saved and an error indicates which required field is missing.
- [ ] CS-02: Require a valid RSVP response
  - Action: In the RSVP form, select an invitation option and answers but leave the Yes/No/Maybe response unselected, then submit.
  - Expected: Submission is blocked with a message telling the guest to choose Yes, No, or Maybe.
- [ ] CS-03: Block RSVPs after RSVPs are closed
  - Action: As host close RSVPs, then attempt to submit or change an RSVP as a guest on the shared page.
  - Expected: The submission is rejected and the RSVP form is no longer submittable.
- [ ] CS-04: Block voting after a poll is closed
  - Action: As host close the poll, then attempt to vote or change an existing vote as a guest.
  - Expected: The vote is rejected and voting controls are unavailable.
- [ ] CS-05: Prevent posting an empty comment
  - Action: Click the comment post button with an empty or whitespace-only message box.
  - Expected: No comment is posted and a message prompts for a non-empty message.

## Interaction
- [ ] IX-01: Confirm event creation to the host
  - Action: Save a new valid event.
  - Expected: A visible success confirmation (toast/message) appears stating the event was created.
- [ ] IX-02: Visibly indicate closed RSVP and closed poll states
  - Action: As host, close RSVPs and close a poll, then view the shared event page as a guest.
  - Expected: The page clearly shows both the RSVP section and the poll as closed, with voting/RSVP controls disabled.
- [ ] IX-03: Update poll results immediately after voting
  - Action: As a guest, select a poll option and submit the vote.
  - Expected: The poll's vote counts/percentages update immediately to include the new vote, with the chosen option highlighted.

## Content
- [ ] CT-01: Display entered event details accurately on the shared page
  - Action: Create an event with specific title, date/time, location, and category, then open its shared event page.
  - Expected: The page shows the exact title, date/time, location, and category as entered, with no missing or mismatched values.
- [ ] CT-02: Show optional sections only when content was provided
  - Action: Create one event with a dress code filled in and another with it left blank; open both shared pages.
  - Expected: The first page shows the dress code content; the second shows no dress code section or an explicitly empty placeholder, never stale/incorrect text.
- [ ] CT-03: Keep summary counts consistent with actual responses
  - Action: Compare the summary's grouped guest counts and preference tallies against the individual RSVP records on the same event.
  - Expected: Every guest appears exactly once in the correct groups and all counts match the underlying RSVP data.