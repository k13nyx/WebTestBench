# Test Result

## Functionality

- [X] FT-01: Create an event with complete core details and optional planning sections.
  - Action: Open the event creation form and enter a title, date, time, location, category, schedule, dress code, and special instructions. Save the event.
  - Expected: The event is saved and displays all entered details accurately.

- [X] FT-02: Define multiple invitation options and preference questions for an event.
  - Action: Add invitation options such as “Dinner only,” “Drinks only,” and “Full evening,” then add preference questions such as meal choice and activity preference. Save the event configuration.
  - Expected: All invitation options and preference questions are available for guest responses.

- [X] FT-03: Configure a poll with several venue or activity options.
  - Action: Add a poll to the event with at least two venue or activity choices and publish the event page.
  - Expected: The poll and every configured option are visible on the shared event page.

- [X] FT-04: Display a shared event page with event details and configured sections.
  - Action: Open the guest-facing event page for the event.
  - Expected: The page displays the title, date, time, location, category, configured schedule, dress code, special instructions, invitation options, preference questions, poll, and comment thread.

- [ ] FT-05: Submit guest RSVP responses with invitation and preference selections.
  - Action: As a guest, select an invitation option, submit each available RSVP response—“Yes,” “No,” and “Maybe”—and answer the displayed preference questions for each response.
  - Expected: Each RSVP response, invitation option, and preference answer is saved and shown for that guest.
  - Bug Report:
    - Issue: Incomplete RSVP preference flow
    - Actual: Preference questions and invitation options were displayed for “Yes,” but switching to “No” removed those controls, and the “Maybe” response was not completed and verified. The form only describes preference questions as applying to “Yes.”

- [X] FT-06: Submit a vote in the event poll.
  - Action: Select one of the venue or activity options in the poll and submit the vote.
  - Expected: The selected poll response is recorded and the updated poll result is displayed.

- [X] FT-07: Post a short message or question in the comment thread.
  - Action: Enter a short guest message or question in the comment field and submit it.
  - Expected: The submitted text appears in the event’s comment thread.

- [ ] FT-08: Update event details after invitations have been sent.
  - Action: As the event owner, change an existing event detail such as the location, date, schedule, or special instructions after invites are sent, then save.
  - Expected: The updated details appear on the owner view and shared guest page without removing existing invitations, RSVPs, poll votes, or comments.
  - Bug Report:
    - Issue: RSVP data is not preserved in the event summary after editing
    - Actual: After submitting an RSVP and updating the venue, the updated event retained the poll vote and comment, but the Guest Summary displayed zero guests for all RSVP statuses.

- [ ] FT-09: View a guest summary grouped by invitation option, RSVP response, and preferences.
  - Action: Open the event summary after guests have submitted different invitation options, RSVP responses, and preference answers.
  - Expected: Guests are grouped and identifiable by invitation option, “Yes,” “No,” or “Maybe” response, and recorded key preferences.
  - Bug Report:
    - Issue: Guest summary does not reflect submitted RSVP data
    - Actual: After a successful RSVP submission, the Guest Summary showed Attending (0), Not Attending (0), Maybe (0), and Pending (0), with no guest, invitation option, or preference data listed.

- [ ] FT-10: Access canceled and past events in a separate area with final results.
  - Action: Open the canceled-events or past-events area and select an event that has been canceled or has passed.
  - Expected: The event is accessible separately from active events and displays its final RSVP and poll results.
  - Bug Report:
    - Issue: Archived event does not display poll results
    - Actual: The past event was accessible and displayed final RSVP counts, but its event page contained no poll section or final poll results.

## Constraint

- [ ] CS-01: Prevent event creation when required core fields are missing.
  - Action: Leave the title, date, time, location, or category empty and attempt to save the event.
  - Expected: The event is not saved, and each missing required field is identified for correction.
  - Bug Report:
    - Issue: Category is not enforced as a required field
    - Actual: The form prevented submission for empty title, start date, start time, and venue, but the category combobox had no required attribute and was not identified as a missing required field.

- [X] CS-02: Allow optional planning sections to be omitted.
  - Action: Create or save an event with no schedule, dress code, or special instructions.
  - Expected: The event saves successfully, and omitted optional sections do not appear as empty required content.

- [X] CS-03: Prevent RSVP changes after RSVPs are closed.
  - Action: Close RSVPs for an event, then attempt to submit or change a guest RSVP.
  - Expected: The RSVP controls no longer accept submissions or changes, and existing RSVP results remain available.

- [X] CS-04: Prevent poll votes after a poll is closed.
  - Action: Close the event poll, then attempt to submit or change a poll vote.
  - Expected: The poll no longer accepts votes, and its existing results remain viewable.

## Interaction

- [X] IX-01: Show configured dynamic sections only when they are part of the event.
  - Action: Compare the shared page for an event with configured schedule, dress code, special instructions, poll, and comments against an event without those sections.
  - Expected: Configured sections are displayed, while omitted sections are not shown as blank or misleading placeholders.

- [X] IX-02: Update the RSVP form based on the selected response and invitation option.
  - Action: Change the selected invitation option and switch among “Yes,” “No,” and “Maybe.”
  - Expected: The form visibly reflects the current selections and presents the preference questions needed to complete that RSVP.

- [X] IX-03: Refresh poll results after a successful vote.
  - Action: Submit a poll vote and observe the poll without leaving the event page.
  - Expected: The selected option and updated result state are shown immediately after submission.

- [X] IX-04: Reflect RSVP and poll closure in the event controls.
  - Action: Close RSVPs and the poll separately, then view the shared event page.
  - Expected: Each closed feature is visibly marked as closed and its corresponding submission control is unavailable.

## Content

- [ ] CT-01: Display event and response content accurately and consistently.
  - Action: Compare the shared page, RSVP form, and event summary with the configured event title, date, time, location, category, invitation options, questions, and poll choices.
  - Expected: Every displayed label and value matches the configured event data, with no unrelated or missing content.
  - Bug Report:
    - Issue: Event summary omits submitted response content
    - Actual: The event page and RSVP form displayed the configured event data, invitation options, questions, and poll choices, but the Guest Summary remained empty after RSVP submission and did not display the guest’s response, invitation option, or preferences.

- [ ] CT-02: Preserve final RSVP and poll information for canceled or past events.
  - Action: Open a canceled or past event after RSVP and poll activity is complete.
  - Expected: The page shows the final guest responses, invitation-option groupings, key preferences, poll choices, and final poll results rather than resetting or omitting them.
  - Bug Report:
    - Issue: Archived event omits poll information
    - Actual: The selected past event showed final RSVP groupings, including two attending guests and one non-attending guest, but did not show poll choices or final poll results.
