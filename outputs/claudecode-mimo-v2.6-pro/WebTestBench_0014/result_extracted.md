# Test Result

## Functionality
- [X] FT-01: Create a new event with the required fields filled in.
  - Action: Open the create-event form, enter Title "Team Offsite Dinner", Date & time, Location "Grand Hall", Category "Social" (leave optional sections empty) and save.
  - Expected: The event is created and appears in the active events list.
- [X] FT-02: Add the optional sections to an event.
  - Action: On an event's create/edit form, fill in Schedule, Dress code, and Special instructions, then save.
  - Expected: The event saves successfully and all three optional sections are retained.
- [X] FT-03: Define multiple invitation options for an event.
  - Action: On the event form, add the invitation options "Dinner only", "Drinks only", and "Full evening", then save.
  - Expected: All three invitation options appear as selectable choices on the guest RSVP form.
- [ ] FT-04: Define a preference question for an event.
  - Action: Add the preference question "Meal choice" with the options "Chicken" and "Vegetarian", then save.
  - Expected: The question and both answer choices are presented to guests on the RSVP form.
  - Bug Report:
    - Issue: Missing Element – Preference Question Not Rendered on RSVP Form
    - Actual: The question "Meal choice" with options "Chicken" and "Vegetarian" is saved and retained in the event's edit form, but it never appears on the guest RSVP form. With response "Yes" selected, the RSVP card shows only "Will you attend?" and "Select your attendance option (Dinner only / Drinks only / Full evening)" followed directly by "Submit RSVP" — no question and none of its answer choices are presented to guests ("Meal choice", "Chicken", "Vegetarian" appear nowhere on the shared page).
- [X] FT-05: Guest submits an RSVP of "Yes".
  - Action: On a default event's shared page, select response "Yes", choose one of the event's invitation options (e.g., "Full evening"), answer each preference question, and submit.
  - Expected: The RSVP is recorded with status "Yes", the selected invitation option, and the preference answers.
- [ ] FT-06: Guest submits an RSVP of "No" or "Maybe".
  - Action: As one guest, submit an RSVP selecting "No"; as a second guest, submit an RSVP selecting "Maybe".
  - Expected: Both RSVPs are recorded with their selected response statuses.
  - Bug Report:
    - Issue: Missing Guest Identity – RSVP Form Permanently Bound to a Single Guest (Unresponsive to Guest Identity)
    - Actual: The RSVP form has no name field or guest selector; its submit button always updates one hard-coded guest ("Update RSVP", pre-filled with Michael Chen's saved answers). Submitting "No" and then "Maybe" overwrites the same single RSVP — only one RSVP is recorded (ending as "Maybe"), so both RSVPs are never recorded together. Typing different names ("Guest Alpha", "Guest Beta", "David Park") into the "Your name" field does not change the target guest — all submissions update Michael Chen's RSVP. On a newly created event (no guests yet), submissions show "RSVP updated successfully!" but record nothing at all (summary remains "No guests").
- [X] FT-07: Create a poll on the shared event page.
  - Action: As event owner, add the poll "Which venue do you prefer?" with the options "Rooftop", "Garden", and "Beach", then save.
  - Expected: The poll with all three options appears on the shared event page.
- [X] FT-08: Guest votes in the poll.
  - Action: As a guest, select one poll option (e.g., "Rooftop") and submit the vote.
  - Expected: The vote is recorded and counted in the poll's results.
- [X] FT-09: Guest posts a comment in the comment thread.
  - Action: In the event's comment thread, enter "Can I bring a plus-one?" and post it.
  - Expected: The comment is saved and listed in the comment thread with its full text.
- [X] FT-10: Change event details after invites are sent.
  - Action: Open a default event that already has RSVPs, change its Location and Date & time, and save.
  - Expected: The updated details are saved and shown on the shared event page; previously recorded RSVPs remain intact.
- [X] FT-11: Close RSVPs and the poll at any time.
  - Action: As event owner, use the "Close RSVPs" control and the "Close poll" control on the event.
  - Expected: The event's RSVPs and the poll are both set to a closed state in the owner's event controls.
- [ ] FT-12: View the guest summary.
  - Action: Open the event's summary view after several guests have responded.
  - Expected: Guests are grouped by invitation option and by response ("Yes"/"No"/"Maybe"), showing each guest's key preference answers.
  - Bug Report:
    - Issue: Missing Information – Per-Guest Preference Answers Not Shown
    - Actual: The summary groups guests by response ("By Status": Attending (2) Michael Chen, Emily Watson; Not Attending (1) Lisa Thompson; Maybe (1) David Park; Pending (1) Robert Kim) and by invitation option ("By Option": Full Celebration (2), Reception Only (0), Ceremony Only (0)), but the "Preferences" tab shows only aggregate percentages per answer choice (e.g., "Herb-crusted salmon 1 (50%)", "Gluten-free 2 (100%)") — no guest's individual key preference answers are displayed anywhere in the summary.
- [X] FT-13: Access canceled and past events in their separate area.
  - Action: Open the separate area for canceled/past events and open one listed event.
  - Expected: The event is listed in that area (not in the active events) and shows its final RSVP and poll results.

## Constraint
- [ ] CS-01: An event cannot be saved with a missing required field.
  - Action: Attempt to save an event with Title empty, then repeat with Date & time, Location, and Category empty in turn.
  - Expected: Every save attempt is blocked with a validation message and no incomplete event is created.
  - Bug Report:
    - Issue: Missing Validation – Incomplete Event Created (Category Not Validated)
    - Actual: With Title empty, and with Date & time empty, and with Location empty, saves are blocked (form stays on /create, focus moves to the invalid field with the browser's native "Please fill out this field" message, fields are marked `required`). However, with Category empty, clicking "Create Event" succeeds with "Event created successfully!" and creates an event with no category: the event page shows no category chip (unlike other events) and the edit form falls back to the first category "Birthday". An incomplete event is therefore created with no validation message for Category (the category select is not `required`).
- [ ] CS-02: An RSVP cannot be submitted incomplete.
  - Action: Attempt to submit an RSVP with no response selected; then with "Yes" but no invitation option; then with "Yes" and an option but a preference question unanswered.
  - Expected: All three attempts are blocked with a validation message and no RSVP is recorded.
  - Bug Report:
    - Issue: Missing Validation Message / Incomplete RSVP Accepted
    - Actual: (1) With no response selected the "Submit RSVP" button is disabled — the attempt is silently blocked with no validation message. (2) With "Yes" but no invitation option, "Submit RSVP" is likewise disabled with no validation message. (3) With "Yes" and an option but the preference question unanswered, the submission is accepted outright: "Submit RSVP" is enabled and clicking it shows "RSVP updated successfully!" — no validation is triggered (and the preference question is not even rendered, see FT-04). On the default event the form is pre-filled and "Update RSVP" accepts submissions from every intermediate state with a success toast. No validation message appears in any of the three attempts.
- [X] CS-03: Closed RSVPs and a closed poll accept no further input.
  - Action: After closing RSVPs, attempt to submit an RSVP; after closing the poll, attempt to submit a vote.
  - Expected: Both attempts are rejected with a closed message and no RSVP or vote is recorded.

## Interaction
- [X] IX-01: Submitting an RSVP shows confirmation feedback.
  - Action: Submit a valid RSVP ("Yes" with invitation option and preference answers) and observe the page immediately after submission.
  - Expected: A success confirmation appears stating that the RSVP was recorded.
- [X] IX-02: The shared event page visibly indicates closed RSVPs and a closed poll.
  - Action: Open the shared event page after RSVPs and the poll have been closed.
  - Expected: RSVP response controls and poll voting controls are disabled or hidden, with a visible "closed" indication.

## Content
- [X] CT-01: The shared event page content matches the event data exactly.
  - Action: Open a default event's shared page and compare title, date & time, location, category, and any optional sections against the saved event data.
  - Expected: Every displayed value matches the event data exactly, with no missing or altered fields.
- [X] CT-02: Archived final results match the recorded responses and votes.
  - Action: In the canceled/past events area, open an event and compare its final RSVP and poll results with its recorded guest responses and poll votes.
  - Expected: Final RSVP results and poll results match the recorded data exactly.
