# Test Checklist

## Functionality
- [ ] FT-01: Organizer can create an event with all required and optional details
  - Action: Click "Create Event". Enter Title, Date, Start Time, Location, and Category. Fill in Schedule, Dress Code, and Special Instructions. Click "Save".
  - Expected: The event saves and appears in the event list. Its event page shows every entered value, and the optional sections display their content.
- [ ] FT-02: Organizer can add multiple invitation options and preference questions to an event
  - Action: Open a default event and add invitation options "Dinner only", "Drinks only", and "Full evening". Add a preference question "Meal choice" and a question "Activity preference". Save.
  - Expected: All three invitation options and both preference questions are listed on the event and appear on its RSVP form.
- [ ] FT-03: Guest can RSVP "Yes" with an invitation option and preference answers
  - Action: Open a default event's RSVP page. Select "Yes", choose "Full evening", answer each preference question, and click "Submit RSVP".
  - Expected: A confirmation shows response "Yes", option "Full evening", and the selected preference answers.
- [ ] FT-04: Guest can change an existing RSVP from "Yes" to "No" and then to "Maybe"
  - Action: After FT-03, reopen the RSVP, select "No", and submit. Reopen, select "Maybe", and submit.
  - Expected: Each change replaces the previous response. The guest has one RSVP showing the latest response, "Maybe".
- [ ] FT-05: Guest can vote in a poll on the shared event page
  - Action: Open a default event's shared page. Select one option in the poll and click "Vote".
  - Expected: The vote is recorded and a confirmation appears. The selected option's vote count increases by 1.
- [ ] FT-06: Organizer can edit event details after invitations are sent
  - Action: Open a default event with sent invites. Change Date, Start Time, and Location. Click "Save".
  - Expected: The new values appear on the event page and the shared guest page. The old values are no longer shown.
- [ ] FT-07: Organizer can view a summary grouping guests by invitation option, response, and preferences
  - Action: Open a default event's "Summary" view.
  - Expected: Guests are grouped under each invitation option. Within each group, they are sorted by response (Yes, No, Maybe), and each guest's preference answers are shown.
- [ ] FT-08: Organizer can cancel an event, and the canceled event appears in the Canceled/Past area with its final RSVP and poll results
  - Action: Open a default event and click "Cancel Event", then confirm. Go to the "Canceled/Past" area and open the event.
  - Expected: The event is listed there with status "Canceled". Its page shows the final RSVP counts by response and the final poll results.
- [ ] FT-09: Guest can post a short comment in the event's comment thread
  - Action: Open a default event's shared page. Type "Will there be parking?" in the comment box and click "Post".
  - Expected: The comment appears in the thread with the guest's name and a timestamp.

## Constraint
- [ ] CS-01: Event cannot be saved when required fields are empty
  - Action: Click "Create Event". Leave Title, Date, Location, and Category blank. Click "Save".
  - Expected: The event is not saved. Each blank required field shows an error message, and the form stays open.
- [ ] CS-02: RSVP cannot be submitted without a response and an invitation option
  - Action: Open a default event's RSVP page. Without selecting a response, click "Submit RSVP". Then select "Yes" without choosing an invitation option and click "Submit RSVP".
  - Expected: Submission is blocked both times. Messages "Please select a response" and "Please select an invitation option" are shown.
- [ ] CS-03: Guests cannot RSVP after the organizer closes RSVPs
  - Action: As organizer, open a default event and click "Close RSVPs", then confirm. As a guest, open that event's RSVP page and attempt to select "Yes" and submit.
  - Expected: The RSVP form is disabled and the message "RSVPs are closed" is shown. No response is recorded.
- [ ] CS-04: Guests cannot vote after the organizer closes a poll
  - Action: As organizer, open a default event's poll and click "Close Poll". As a guest, open the shared page and attempt to select an option and click "Vote".
  - Expected: Voting is disabled and the message "Poll is closed" is shown. The vote count does not change.

## Interaction
- [ ] IX-01: Closing RSVPs requires confirmation and updates the button state
  - Action: As organizer, open a default event and click "Close RSVPs". In the dialog, click "Cancel", then click "Close RSVPs" again and click "Confirm".
  - Expected: After "Cancel", RSVPs stay open. After "Confirm", the dialog closes and the button changes to "RSVPs Closed".
- [ ] IX-02: New comments appear at the top of the thread immediately after posting
  - Action: Open a default event's shared page. Type "See you there!" in the comment box and click "Post". Leave the box empty and check whether "Post" is enabled.
  - Expected: The new comment appears at the top of the thread without a page reload, and the input box clears. With an empty box, "Post" is disabled.
- [ ] IX-03: Poll results update immediately after a vote
  - Action: Open a default event's poll, note the vote counts, and vote for an option.
  - Expected: Without reloading, the vote count and percentage bar for the chosen option update, and the other options' percentages adjust to match.

## Content
- [ ] CT-01: Event cards in the event list match the details on each event's page
  - Action: On the event list, note the title, date, time, location, and category of each default event. Open each event and compare.
  - Expected: Every value on the card matches the value on the event page. No card shows a different date, time, or location.
- [ ] CT-02: Summary counts are consistent with the individual RSVP records
  - Action: Open a default event's Summary view. Compare the totals for "Yes", "No", and "Maybe" with the full RSVP list.
  - Expected: The "Yes", "No", and "Maybe" totals add up to the number of RSVPs. Each invitation option's count matches the guests listed under it.
- [ ] CT-03: Poll percentages are accurate and total 100%
  - Action: Open a default event's poll and note the vote count for each option and its percentage.
  - Expected: Each percentage equals that option's votes divided by total votes. All percentages add up to 100%.
- [ ] CT-04: The Canceled/Past area lists only canceled or past events
  - Action: Open the "Canceled/Past" area. Compare its listed events with the upcoming events in the main event list.
  - Expected: Every listed event is either canceled or has a date before today. No upcoming, non-canceled event appears in this area.