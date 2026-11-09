All tests executed. Here is the complete checklist with results:

# Test Result

## Functionality

- [X] FT-01: User can create an event with all core fields — title, date, time, location, and category.
  - Action: Open the event creation form, fill in title "Summer Dinner Party", date, time, location "Rooftop Terrace", category "Dinner", and submit.
  - Expected: Event is created and appears with the entered title "Summer Dinner Party" in the events list.
  - Note: Event was created, a success toast appeared, and the event was listed on the dashboard as "Summer Dinner Party". However, the category dropdown offers no "Dinner" option (only Birthday/Wedding/Corporate/Social/Holiday/Celebration/Other), so the closest available preset was used.

- [X] FT-02: User can add the optional sections schedule, dress code, and special instructions to an event.
  - Action: While creating/editing an event, fill the optional "Schedule", "Dress Code", and "Special Instructions" fields (e.g., dress code "Cocktail attire") and save.
  - Expected: All three sections are saved and displayed on the event page with the entered text.
  - Note: Event page displayed "Dress Code: Cocktail attire", "Special Instructions: Enter via the side gate; parking in lot B.", and the Schedule section with "6:00 PM Cocktail hour – Drinks on the terrace".

- [X] FT-03: User can define multiple invitation options for one event (e.g., "Dinner only", "Drinks only", "Full evening").
  - Action: In the event editor, add three invitation options named "Dinner only", "Drinks only", and "Full evening", then save.
  - Expected: All three invitation options are listed on the event and selectable when guests RSVP.
  - Note: All three options persisted through edit/save and appeared as selectable radio options in the RSVP form (revealed when the guest selects "Yes").

- [X] FT-04: User can add simple preference questions (e.g., meal choice) that guests answer when RSVPing.
  - Action: In the event editor, add a preference question "Meal choice?" with options (e.g., "Veg", "Meat"), save, then view the event's RSVP form as a guest.
  - Expected: The question "Meal choice?" appears on the RSVP form with its options selectable.
  - Note: "Meal choice?" with radio options "Veg"/"Meat" appeared on the RSVP form (after selecting "Yes") and options were selectable.

- [ ] FT-05: Guest can RSVP as "Yes", "No", or "Maybe" and answer the preference questions in the same flow.
  - Action: On the guest event page, select an invitation option, choose a preference answer, set RSVP to "Maybe", and submit.
  - Expected: RSVP "Maybe" is recorded, shown on the page, and the chosen preference answer is saved with the response.
  - Bug Report:
    - Issue: Incorrect Form Submission / Silent Data Loss
    - Actual: Selecting "Maybe" (or "No") reveals no invitation-option selector and no preference questions — those inputs only render for "Yes", so no preference answer can be saved with a "Maybe". Furthermore, on a newly created event the RSVP submission is never recorded at all: after submitting "Maybe" and separately "Yes" + "Full evening" + "Meat" (each showing toast "RSVP updated successfully!"), the Guest Summary remained Attending (0) / Maybe (0) / Pending (0) and the RSVP form reset to an unselected "Submit RSVP" state after navigating away and back. (On a pre-seeded event the RSVP form does update an existing guest record, but no new guest is ever created from a fresh RSVP.)

- [ ] FT-06: Guests can access a shared event page showing the event's details.
  - Action: Open the event's shared/guest link for a created event.
  - Expected: Page shows the event title, date/time, location, category, and the optional sections exactly as configured.
  - Bug Report:
    - Issue: Broken Navigation / No Data Persistence for Shared Link
    - Actual: Opening the created event's URL directly (fresh page load, as a guest would via a shared link) shows "Event Not Found — This event doesn't exist or has been removed." The app stores everything in memory with no persistence (no localStorage/sessionStorage/IndexedDB/API), so any created event is unreachable via its link after a page load. The page only shows full details (title, date/time, location, dress code, instructions, schedule, poll) when navigated to within the same client-side session.

- [X] FT-07: Guests can vote in the event poll for picking between venue or activity options.
  - Action: On the guest event page, locate the poll and select one of its options (e.g., "Rooftop"), then submit the vote.
  - Expected: The vote is recorded and reflected in the poll results for that option.
  - Note: Clicking "Rooftop lounge" recorded the vote: "Rooftop lounge 1 vote (100%)", "1 total vote".

- [X] FT-08: Guests can post a short message or question in the event's comment thread.
  - Action: On the guest event page, type "What time should we arrive?" in the comment box and post it.
  - Expected: The comment appears in the thread attributed to the guest.
  - Note: Comment appeared as "Alex · What time should we arrive?" and Discussion count incremented to (1), then (2).

- [X] FT-09: Host can change event details after invites are sent, and the change is visible to guests.
  - Action: After at least one RSVP exists, edit the event's location from "Rooftop Terrace" to "Garden Hall" and save, then reload the guest event page.
  - Expected: Guest page now shows location "Garden Hall".
  - Note: Edit form pre-filled "Rooftop Terrace", saved with toast "Event updated successfully!", and the event page (guest-visible) now shows "Garden Hall".

- [X] FT-10: Host can close RSVPs at any time.
  - Action: On the host event management view, click the control to close RSVPs (e.g., "Close RSVPs").
  - Expected: RSVP status becomes closed and guests can no longer submit or change a response.
  - Note: Toast "RSVPs are now closed" appeared, button changed to "Open RSVPs", a notice "RSVPs are currently closed for this event." is shown, and the RSVP form is removed entirely.

- [X] FT-11: Host can close the poll at any time.
  - Action: On the host event management view, click the control to close the poll.
  - Expected: Poll status becomes closed; final vote results remain visible but voting is disabled.
  - Note: Poll status badge changed to "Closed", option buttons became disabled, and results ("Rooftop lounge 1 vote (100%)") remain visible; control changed to "Reopen Poll".

- [X] FT-12: Host can view a summary grouping guests by invitation option, response, and key preferences.
  - Action: With several guests having RSVPed with different invitation options and preference answers, open the event summary view.
  - Expected: Guests are grouped by invitation option (e.g., "Full evening"), by response (Yes/No/Maybe), and their preference answers are visible per group.
  - Note: Verified on the seeded "Sarah & James's Garden Wedding": "By Status" groups guests under Attending (2), Not Attending (1), Maybe (1), Pending (1); "By Option" groups under Full Celebration (2) / Reception Only (1) / Ceremony Only (0); "Preferences" tab shows per-question answer breakdowns (e.g., Meal preference: Filet mignon 1 (50%), Wild mushroom risotto (V) 1 (50%)). Per-guest preference answers are only shown as aggregates in the Preferences tab, not attached to each group.

- [X] FT-13: Canceled or past events remain accessible in a separate area with their final RSVP and poll results.
  - Action: Cancel an event that has RSVPs and poll votes (or use an event whose date has passed), then open the past/canceled events area and open that event.
  - Expected: The event is listed in the separate area and its final RSVP responses and final poll results are displayed.
  - Note: After "Cancel Event" (with confirmation dialog + toast "Event canceled"), the event appeared in Archive → "Canceled (1)" tab, and opening it shows the final state: poll Closed with "Rooftop lounge 1 vote (100%)" and the Guest Summary. The Archive's past event ("Annual Company Holiday Party", Completed) also opens with final RSVPs (Attending (2), Not Attending (1)).

## Constraint

- [X] CS-01: Event cannot be created with required fields empty.
  - Action: Open the event creation form, leave title/date/location empty, and click the create/submit button.
  - Expected: Submission is blocked and a validation message indicates the missing required fields; no event is created.
  - Note: Submission was blocked (stayed on /create), native validation "Please fill out this field." is attached to the required title/date/time/location fields, and no event was created.

- [X] CS-02: When RSVPs are closed, guests cannot submit or change their response.
  - Action: Close RSVPs on an event, then as a guest attempt to change the RSVP to "Yes" and submit.
  - Expected: The RSVP controls are disabled/absent and no change to the recorded response occurs.
  - Note: The entire RSVP card is removed once RSVPs are closed ("Yes/No/Maybe" buttons no longer exist in the DOM); no submission is possible.

- [X] CS-03: When the poll is closed, guests cannot vote or change their vote.
  - Action: Close the poll on an event, then as a guest attempt to select a poll option and vote.
  - Expected: Voting controls are disabled/absent and vote counts remain unchanged.
  - Note: Both poll option buttons have `disabled` set and clicks are rejected; counts remained "Rooftop lounge 1 vote (100%) / Lawn games 0 votes (0%)" after the attempt.

## Interaction

- [X] IX-01: A newly posted comment appears in the thread immediately without a page reload.
  - Action: As a guest, post the comment "Looking forward to it!" and observe the thread without navigating away.
  - Expected: The comment "Looking forward to it!" appears in the thread right away.
  - Note: The comment appeared instantly in the thread with attribution "Alex" and the count went to (2) with no navigation.

- [X] IX-02: Poll results update visibly after a guest votes.
  - Action: As a guest, vote for option "Rooftop" in an open poll and observe the poll display.
  - Expected: The count or percentage for "Rooftop" increases immediately to include the new vote.
  - Note: Immediately after clicking, "Rooftop lounge" changed from "0 votes (0%)" to "1 vote (100%)" and total votes from 0 to 1.

- [X] IX-03: The system shows confirmation feedback when a key action succeeds (event created or RSVP submitted).
  - Action: Create an event, then submit an RSVP as a guest, observing the UI after each action.
  - Expected: A visible success indication (e.g., toast or confirmation message) appears for each successful action.
  - Note: Toasts observed: "Event created successfully!", "RSVP updated successfully!", plus "Event updated successfully!" and "RSVPs are now closed" for other actions.

## Content

- [X] CT-01: The summary view's counts and groupings match the actual RSVP data.
  - Action: With known responses (e.g., 2 "Yes" for "Dinner only", 1 "No"), compare the summary view numbers and group membership against the guest RSVP list.
  - Expected: Each group's guest count and preference breakdown exactly matches the recorded RSVPs.
  - Note: On the seeded wedding event: dashboard card "2 yes · 1 maybe · 1 pending" exactly matches By Status (Attending 2: Michael Chen, Emily Watson; Maybe 1: David Park; Pending 1: Robert Kim; Not Attending 1: Lisa Thompson). By Option counts (1+1) sum to the 2 attendees and name the same people; preference breakdowns (Filet mignon 1 / Risotto 1; dietary None 1 / Gluten-free 1; plus-one No 2) each sum exactly to the 2 attendees after my recorded RSVP change. (Counts could not be validated on a newly created event because RSVPs there are never recorded — see FT-05.)

---

### Additional Global Defect Notes (cross-cutting, observed during testing)

1. **No data persistence at all**: Created events, edits, poll votes, and comments exist only in the in-memory SPA store (no localStorage/sessionStorage/IndexedDB/backend writes). Any hard page load orients the app back to the 3 seeded events, losing every user-created event — this is the root cause of the FT-06 failure and also means "reload the guest event page" (FT-09) can only be satisfied via in-app navigation.
2. **RSVPs on created events are silently dropped**: The RSVP endpoint shows "RSVP updated successfully!" but no guest record is created for a newly created event (Guest Summary stays at 0 in all groups). RSVPs only "work" by mutating pre-seeded guest records.
3. **"Maybe"/"No" RSVPs collect no invitation option or preference answers** — those inputs are only rendered for "Yes", so responses and preferences cannot be captured together for all RSVP types.
4. **Category "Dinner" is not available** in the category dropdown (fixed preset list only).