I now have complete data for all 20 checklist items. The canceled event in the archive displays its final poll results ("Favorite color?" with Blue/Red vote tallies) and RSVP counts — CT-02 verified. Below is the full test report.

# Test Result

## Functionality

- [X] FT-01: Create an event with all required fields
  - Action: Fill in Title, Date & Time, Location, and Category, then click "Create Event".
  - Expected: Event is created and appears in the organizer's event list.

- [X] FT-02: Add optional sections to an event
  - Action: In the event editor, enter text for Schedule, Dress Code, and Special Instructions, then save.
  - Expected: Optional sections are saved and later displayed on the event page.

- [X] FT-03: Define multiple invitation options for an event
  - Action: Add options such as "Dinner only", "Drinks only", and "Full evening" to the event, then save.
  - Expected: All defined invitation options are stored and shown on the RSVP form.

- [X] FT-04: Define preference questions for an event
  - Action: Add simple preference questions (e.g., "Meal choice", "Activity preference"), then save.
  - Expected: Questions are stored and presented to guests during RSVP.

- [X] FT-05: Guest submits RSVP with a response and answers preference questions
  - Action: As a guest, select "Yes"/"No"/"Maybe" and answer the preference questions, then click "Submit RSVP".
  - Expected: RSVP is recorded with the chosen response and answered preferences.

- [X] FT-06: Guest votes in the event poll
  - Action: On the shared event page, select one venue/activity option and submit the poll vote.
  - Expected: Vote is recorded and counted in the poll results.

- [X] FT-07: Guest posts a message in the comment thread
  - Action: On the shared event page, type a short message in the comment box and click "Post".
  - Expected: The message appears in the comment thread.

- [X] FT-08: Organizer edits event details after invites are sent
  - Action: After sending invites, open the event and change Title/Location/Category, then save.
  - Expected: Updated details are saved and reflected on the shared event page.

- [X] FT-09: Organizer closes RSVPs or polls at any time
  - Action: Click "Close RSVP" and "Close Poll" on the event management view.
  - Expected: RSVP and poll controls become disabled/closed for guests.

- [ ] FT-10: Organizer views summary grouped by invitation option, response, and preference
  - Action: Open the event summary view.
  - Expected: Guests are grouped by invitation option, RSVP response (Yes/No/Maybe), and key preferences.
  - Bug Report:
    - Issue: Guest RSVPs not reflected in the grouped summary
    - Actual: After a guest submitted a valid RSVP (Yes / "Full evening" / Chicken / Hiking) with an "RSVP updated successfully!" confirmation, the Guest Summary tabs (By Status, By Option, Preferences) all show "No guests" / "(0)" and 0% for every preference option. The summary structure exists but contains no data for any guest who RSVP'd via the shared page, so the organizer cannot see guests grouped by option/response/preference.

- [X] FT-11: Guest accesses the shared event page
  - Action: Open the shared event page link as a guest.
  - Expected: Page loads showing event details, poll, and comment thread.

## Constraint

- [ ] CS-01: Event cannot be created with missing required fields
  - Action: Leave Title, Date & Time, Location, or Category empty and click "Create Event".
  - Expected: Creation is blocked with a validation message identifying the missing field(s).
  - Bug Report:
    - Issue: No validation message shown for missing required fields
    - Actual: Clicking "Create Event" with Title, Start Date, Start Time, and Venue Name all empty does block creation (page stays on /create, focus moves to the Title field), but no error text or toast is displayed identifying the missing field(s).

- [X] CS-02: RSVP response must be Yes, No, or Maybe
  - Action: Attempt to submit an RSVP with any value outside Yes/No/Maybe.
  - Expected: Submission is rejected; only Yes/No/Maybe are accepted.

- [X] CS-03: Closed RSVP blocks new or changed responses
  - Action: After organizer closes RSVP, attempt to submit or change a guest RSVP.
  - Expected: RSVP submission is prevented (form disabled or error shown).

- [X] CS-04: Closed poll blocks new or changed votes
  - Action: After organizer closes the poll, attempt to cast or change a vote.
  - Expected: Voting is prevented (poll disabled or error shown).

## Interaction

- [X] IX-01: Comment appears in thread without full page reload
  - Action: Post a comment as a guest.
  - Expected: The new comment is dynamically added to the thread immediately.

- [X] IX-02: Poll results update dynamically after voting
  - Action: Cast a vote in the poll.
  - Expected: Poll tallies update live to reflect the new vote.

- [X] IX-03: Confirmation feedback after closing RSVP or poll
  - Action: Click "Close RSVP" / "Close Poll".
  - Expected: A success toast or confirmation message is shown.

## Content

- [X] CT-01: Event page displays all created fields accurately
  - Action: Open the shared event page for an event with all fields and optional sections filled.
  - Expected: Title, Date & Time, Location, Category, Schedule, Dress Code, and Special Instructions all display correctly and match input.

- [X] CT-02: Canceled/past events area shows final RSVP and poll results
  - Action: Open the separate canceled/past events area and select a closed event.
  - Expected: Event is listed there and displays its final RSVP counts (by response) and final poll results.

---

## Additional Findings (defects not captured by a single checklist item)

1. **Non‑persistence of created events (Critical).** Events created in the app exist only in client-side memory. After any full page reload/navigation (e.g., a `page.goto` to another route), the event returns **"Event Not Found"** and the Dashboard reverts to only the original 3 seed events. This means a created event disappears from the organizer's event list after a refresh, undermining the durability of FT‑01's expectation.

2. **Spurious empty poll created.** When an event is created with a poll, a second, empty poll (no question, two empty options) is also generated and displayed to guests on both the live event page and in the archive. Observed during CT‑01/CT‑02 verification.

3. **Inconsistent close confirmation (minor).** "Close RSVP" shows a success toast ("RSVPs are now closed"), whereas "Close Poll" only updates the status to "Closed" with disabled vote buttons (no toast). Both still provide confirmation, so IX‑03 passes, but the behavior is inconsistent.

**Summary:** 17 PASS / 3 FAIL (FT‑10, CS‑01, plus the persistence defect noted above as a critical finding). The core creation, RSVP, poll, comment, edit, close, and archive flows work; the main gaps are the missing required-field validation message, the summary not counting walk‑in guest RSVPs, and the lack of data persistence across reloads.