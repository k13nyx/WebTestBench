# Test Result

## Functionality
- [X] FT-01: Create an event with core fields, optional sections, invitation options, and preference questions
  - Action: Fill in Title, Date and Time, Location, Category, add optional Schedule, Dress Code, and Special Instructions, define invitation tiers ("Dinner only", "Full evening"), add a preference question ("Meal Choice"), and click "Create Event".
  - Expected: The event is successfully created and appears in the active events list.
- [ ] FT-02: Submit an RSVP response with invitation option and preference answers
  - Action: Navigate to the shared event page, select "Yes" as the RSVP status, select an invitation option ("Full evening"), answer the preference question, and click "Submit RSVP".
  - Expected: The RSVP is recorded and a confirmation message is displayed.
  - Bug Report:
    - Issue: Incorrect Form Submission
    - Actual: While clicking "Submit RSVP" triggers a toast notification stating "RSVP updated successfully!", the guest response is not recorded in the event data or Guest Summary. The guest summary continues to display Attending (0), Not Attending (0), Maybe (0), Pending (0) with "No guests", because `updateGuestRSVP` only maps over existing guest IDs and fails to register a guest entry when RSVPing to newly created events.
- [X] FT-03: Cast a vote in the shared event poll
  - Action: On the shared event page, select an option in the activity/venue poll and click "Vote".
  - Expected: The vote is submitted and updated poll results are displayed.
- [X] FT-04: Post a message in the guest comment thread
  - Action: Type a message into the comment text field and click "Post Comment".
  - Expected: The message is added to the event comment thread with author name and timestamp.
- [X] FT-05: Edit event details after creation
  - Action: Open an existing event, update the Location and Date/Time fields, and click "Save Changes".
  - Expected: Event details update successfully and changes are reflected on the shared event page.
- [X] FT-06: Close RSVPs for an active event
  - Action: In the event management controls, click "Close RSVPs".
  - Expected: Event RSVP status updates to closed, preventing further guest RSVP submissions.
- [X] FT-07: Close an active poll
  - Action: In the poll management controls, click "Close Poll".
  - Expected: Poll status updates to closed, preventing further votes.
- [X] FT-08: View event summary grouped by invitation option, response, and preferences
  - Action: Navigate to the event summary dashboard for a selected event.
  - Expected: Guest responses are displayed grouped by invitation option, RSVP status ("Yes", "No", "Maybe"), and key preference answers with total counts.
- [X] FT-09: Access past and canceled events in a dedicated section
  - Action: Navigate to the "Past and Canceled Events" area and select an archived event.
  - Expected: The archived event page opens showing its details along with final RSVP counts and poll results.

## Constraint
- [X] CS-01: Prevent event creation when required fields are missing
  - Action: Leave the Title and Date/Time fields empty and click "Create Event".
  - Expected: Form submission is blocked and validation error messages appear for the missing required fields.
- [X] CS-02: Block RSVP submissions when RSVPs are closed
  - Action: Open the shared event page for an event where RSVPs are closed and attempt to interact with the RSVP form.
  - Expected: RSVP input options and submission button are disabled, and a notice indicates RSVPs are closed.
- [X] CS-03: Block voting when a poll is closed
  - Action: Attempt to select a poll choice and submit a vote on a closed poll.
  - Expected: Voting controls are disabled and a message displays stating the poll is closed.
- [X] CS-04: Prevent posting an empty comment
  - Action: Leave the comment input field blank (or whitespace only) and click "Post Comment".
  - Expected: The comment is not submitted and an error or disabled button state prevents empty posts.

## Interaction
- [X] IX-01: Dynamically expand optional sections during event creation
  - Action: Toggle or click to add "Schedule", "Dress Code", and "Special Instructions" sections in the event form.
  - Expected: The respective input fields expand and display inline without a page reload.
- [X] IX-02: Dynamically display invitation options and preference questions based on RSVP response
  - Action: On the shared event page, select "No" for RSVP, then switch selection to "Yes".
  - Expected: Invitation options and preference questions are hidden when "No" is selected, and dynamically revealed when "Yes" is selected.
- [X] IX-03: Update poll tally immediately after voting
  - Action: Select an option in an open poll and click "Vote".
  - Expected: The selected option's vote count and percentage bar update instantly on the page without a full reload.

## Content
- [X] CT-01: Display all configured event details on the shared event page
  - Action: Navigate to the shared event page of a fully configured event.
  - Expected: Title, date and time, location, category, schedule timeline, dress code instructions, and special notes are all clearly visible and accurate.
- [X] CT-02: Display finalized metrics on past and canceled events
  - Action: Open a canceled or past event record from the archive area.
  - Expected: Event status indicator ("Canceled" or "Past"), final RSVP breakdown, and final poll vote distribution are accurately displayed.
