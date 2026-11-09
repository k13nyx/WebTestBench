# Test Result

## Functionality

- [ ] FT-01: Organizer can create an event with all required and optional details
  - Action: Click "Create Event". Enter Title, Date, Start Time, Location, and Category. Fill in Schedule, Dress Code, and Special Instructions. Click "Save".
  - Expected: The event saves and appears in the event list. Its event page shows every entered value, and the optional sections display their content.
  - Bug Report:
    - Issue: Created Event Missing From Event List
    - Actual: The event page for "QA Test Gala" showed every entered value (Wedding, Tuesday, December 15, 2026, 6:30 PM, Harbor Hall, address, Black tie, "Park in the north lot", and the "Cocktail hour" schedule item). However, after a full page load of the dashboard the list shows "3 events" (Marcus's 40th Birthday Bash, Sarah & James's Garden Wedding, Summer Backyard BBQ). "QA Test Gala" is not listed. I did not check the list before reloading.
- [X] FT-02: Organizer can add multiple invitation options and preference questions to an event
  - Action: Open a default event and add invitation options "Dinner only", "Drinks only", and "Full evening". Add a preference question "Meal choice" and a question "Activity preference". Save.
  - Expected: All three invitation options and both preference questions are listed on the event and appear on its RSVP form.
- [ ] FT-03: Guest can RSVP "Yes" with an invitation option and preference answers
  - Action: Open a default event's RSVP page. Select "Yes", choose "Full evening", answer each preference question, and click "Submit RSVP".
  - Expected: A confirmation shows response "Yes", option "Full evening", and the selected preference answers.
  - Bug Report:
    - Issue: No Confirmation Of Submitted Response
    - Actual: After selecting Yes, Full evening, Chicken, and Dancing, the page showed only the toast "RSVP updated successfully!". No confirmation shows the response, option, or answers. The form keeps the selected values, but nothing summarizes them. The submit button is labeled "Update RSVP", not "Submit RSVP".
- [X] FT-04: Guest can change an existing RSVP from "Yes" to "No" and then to "Maybe"
  - Action: After FT-03, reopen the RSVP, select "No", and submit. Reopen, select "Maybe", and submit.
  - Expected: Each change replaces the previous response. The guest has one RSVP showing the latest response, "Maybe".
- [ ] FT-05: Guest can vote in a poll on the shared event page
  - Action: Open a default event's shared page. Select one option in the poll and click "Vote".
  - Expected: The vote is recorded and a confirmation appears. The selected option's vote count increases by 1.
  - Bug Report:
    - Issue: No Vote Control; Vote Recorded On Click Without Confirmation
    - Actual: The poll has no "Vote" button. Clicking "\"Perfect\" - Ed Sheeran" changed its count from 0 to 1 vote (33%), but no confirmation appeared. The same guest's earlier "\"At Last\" - Etta James" vote dropped from 2 to 1 with no notice.
- [ ] FT-06: Organizer can edit event details after invitations are sent
  - Action: Open a default event with sent invites. Change Date, Start Time, and Location. Click "Save".
  - Expected: The new values appear on the event page and the shared guest page. The old values are no longer shown.
  - Bug Report:
    - Issue: Edit Not Persisted
    - Actual: Save showed "Event updated successfully!" and the event page displayed Thursday, December 10, 2026, 4:00 PM - 11:00 PM, and Moonlight Terrace. After a full page load of event 1, it displays Wednesday, December 9, 2026, 3:00 PM - 11:00 PM, and Rosewood Gardens again. The dashboard card also shows the old values.
- [ ] FT-07: Organizer can view a summary grouping guests by invitation option, response, and preferences
  - Action: Open a default event's "Summary" view.
  - Expected: Guests are grouped under each invitation option. Within each group, they are sorted by response (Yes, No, Maybe), and each guest's preference answers are shown.
  - Bug Report:
    - Issue: Incomplete Summary Grouping
    - Actual: The "By Option" tab lists "Full Celebration (2)" with names only (Michael Chen, Emily Watson). It shows no response labels, no Yes/No/Maybe ordering, and no preference answers. Guests without an option (Lisa Thompson, David Park, Robert Kim) are not listed. The "Preferences" tab shows aggregate tallies only (e.g., "Filet mignon 1 (50%)"), not each guest's answers.
- [ ] FT-08: Organizer can cancel an event, and the canceled event appears in the Canceled/Past area with its final RSVP and poll results
  - Action: Open a default event and click "Cancel Event", then confirm. Go to the "Canceled/Past" area and open the event.
  - Expected: The event is listed there with status "Canceled". Its page shows the final RSVP counts by response and the final poll results.
  - Bug Report:
    - Issue: Canceled Event Missing From Archive
    - Actual: On "Marcus's 40th Birthday Bash", "Cancel Event" and the confirmation dialog worked. The event page then showed a "Canceled" badge and final by-status counts (Attending 2, Pending 1) with poll results. However, the Archive page (nav label "Archive", not "Canceled/Past") shows "Canceled (0)", and that tab reads "No canceled events". After a full page load, the dashboard still lists the event as "Active" under Upcoming Events.
- [X] FT-09: Guest can post a short comment in the event's comment thread
  - Action: Open a default event's shared page. Type "Will there be parking?" in the comment box and click "Post".
  - Expected: The comment appears in the thread with the guest's name and a timestamp.

## Constraint

- [ ] CS-01: Event cannot be saved when required fields are empty
  - Action: Click "Create Event". Leave Title, Date, Location, and Category blank. Click "Save".
  - Expected: The event is not saved. Each blank required field shows an error message, and the form stays open.
  - Bug Report:
    - Issue: Missing Field Error Messages
    - Actual: Clicking "Create Event" with blank fields kept the page on /create, so nothing was saved. The DOM contains no error text (no "required" messages). Only native browser validation applies: the Title input receives focus, and four inputs (Title, Start Date, Start Time, Venue Name) are `:invalid`. The Category field defaults to "🎉 Social", so it could not be left blank.
- [ ] CS-02: RSVP cannot be submitted without a response and an invitation option
  - Action: Open a default event's RSVP page. Without selecting a response, click "Submit RSVP". Then select "Yes" without choosing an invitation option and click "Submit RSVP".
  - Expected: Submission is blocked both times. Messages "Please select a response" and "Please select an invitation option" are shown.
  - Bug Report:
    - Issue: Missing Validation On RSVP Submit
    - Actual: With no response selected, "Update RSVP" showed the toast "RSVP updated successfully!", and "Please select a response" never appeared. Selecting "Yes" and submitting also succeeded with no "Please select an invitation option" message. The invitation option "Full Celebration" was already pre-selected, so the option could not be left empty.
- [ ] CS-03: Guests cannot RSVP after the organizer closes RSVPs
  - Action: As organizer, open a default event and click "Close RSVPs", then confirm. As a guest, open that event's RSVP page and attempt to select "Yes" and submit.
  - Expected: The RSVP form is disabled and the message "RSVPs are closed" is shown. No response is recorded.
  - Bug Report:
    - Issue: RSVP Form Removed Instead Of Disabled; Message Wording Differs
    - Actual: On "Marcus's 40th Birthday Bash" (event 2), "Close RSVPs" took effect immediately. The Yes/No/Maybe buttons, attendance options, and "Update RSVP" were removed entirely, so the form is not disabled. The message shown is "RSVPs are currently closed for this event.", not "RSVPs are closed". Guests could not submit a response.
- [ ] CS-04: Guests cannot vote after the organizer closes a poll
  - Action: As organizer, open a default event's poll and click "Close Poll". As a guest, open the shared page and attempt to select an option and click "Vote".
  - Expected: Voting is disabled and the message "Poll is closed" is shown. The vote count does not change.
  - Bug Report:
    - Issue: Missing "Poll is closed" Message
    - Actual: After "Close Poll" on event 1, the poll options are disabled, the status badge reads "Closed", and the button becomes "Reopen Poll". A DOM text check found no "Poll is closed" anywhere on the page. The counts (2/1/0) did not change.

## Interaction

- [ ] IX-01: Closing RSVPs requires confirmation and updates the button state
  - Action: As organizer, open a default event and click "Close RSVPs". In the dialog, click "Cancel", then click "Close RSVPs" again and click "Confirm".
  - Expected: After "Cancel", RSVPs stay open. After "Confirm", the dialog closes and the button changes to "RSVPs Closed".
  - Bug Report:
    - Issue: No Confirmation Dialog For Close RSVPs
    - Actual: Clicking "Close RSVPs" on event 2 closed RSVPs immediately, with the toast "RSVPs are now closed". No dialog appeared, so the "Cancel" and "Confirm" steps could not be performed. The button changed to "Open RSVPs", not "RSVPs Closed". (The "Cancel Event" action on the same page does show a confirmation dialog.)
- [X] IX-02: New comments appear at the top of the thread immediately after posting
  - Action: Open a default event's shared page. Type "See you there!" in the comment box and click "Post". Leave the box empty and check whether "Post" is enabled.
  - Expected: The new comment appears at the top of the thread without a page reload, and the input box clears. With an empty box, "Post" is disabled.
- [X] IX-03: Poll results update immediately after a vote
  - Action: Open a default event's poll, note the vote counts, and vote for an option.
  - Expected: Without reloading, the vote count and percentage bar for the chosen option update, and the other options' percentages adjust to match.

## Content

- [X] CT-01: Event cards in the event list match the details on each event's page
  - Action: On the event list, note the title, date, time, location, and category of each default event. Open each event and compare.
  - Expected: Every value on the card matches the value on the event page. No card shows a different date, time, or location.
- [X] CT-02: Summary counts are consistent with the individual RSVP records
  - Action: Open a default event's Summary view. Compare the totals for "Yes", "No", and "Maybe" with the full RSVP list.
  - Expected: The "Yes", "No", and "Maybe" totals add up to the number of RSVPs. Each invitation option's count matches the guests listed under it.
- [X] CT-03: Poll percentages are accurate and total 100%
  - Action: Open a default event's poll and note the vote count for each option and its percentage.
  - Expected: Each percentage equals that option's votes divided by total votes. All percentages add up to 100%.
- [X] CT-04: The Canceled/Past area lists only canceled or past events
  - Action: Open the "Canceled/Past" area. Compare its listed events with the upcoming events in the main event list.
  - Expected: Every listed event is either canceled or has a date before today. No upcoming, non-canceled event appears in this area.

---

## Run Notes

- **Result:** 6 of 26 pass (FT-02, FT-04, FT-09, IX-02, IX-03, CT-04). CT-01, CT-02, and CT-03 also pass but were judged on a fresh page load, where the data was the seeded state.
- **Cross-cutting defect, likely root cause of most failures:** Changes don't survive a full page load. Edits, RSVPs, votes, comments, cancellations, close states, and the new event all revert on reload. In one case, saving event 1's details also reset its RSVPs, poll votes, and the invitation options and questions I had added in FT-02, back to their seeded values. Results marked PASS reflect in-session behavior only.
- **Ambiguities I resolved:** The "Submit RSVP" and "Save" buttons are labeled "Update RSVP" and "Save Changes"; I used them as the submit controls. The "Canceled/Past" area is the page at `/archive`. The "Summary" is the "Guest Summary" panel on the event page.
- **Budget:** About 85 of 100 tool calls used.