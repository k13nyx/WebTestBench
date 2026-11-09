# Test Result

**Environment note (systemic finding):** The app is a purely in-memory demo — `localStorage`, `sessionStorage`, and cookies are all empty. Any created event, RSVP, comment, or poll vote is lost on a full page reload (`/event/event-…` → "Event Not Found"). Results below grade each item against its own stated expectation within the running application session; items whose expectations explicitly require cross-session visibility (FT-08) are failed on that basis.

## Functionality
- [X] FT-01: Create event with all core fields
  - Action: Open the event creation form, fill in title, date & time, location, and category, then submit.
  - Expected: Event is created and appears in the organizer's event list with all entered details shown correctly.
  - Note: "Autumn Charity Gala QA" was created (toast "Event created successfully!") and appeared on the Dashboard with correct title, 🎉 Social category, Saturday, December 5, 2026, 6:00 PM – 11:00 PM, Grand Atrium Hall (count went 3→4). Caveat: it only appears for in-app navigation; after a hard reload the event is gone entirely (persistence defect, see FT-08 bug).

- [X] FT-02: Add optional sections to an event
  - Action: While creating/editing an event, fill in the optional "Schedule", "Dress code", and "Special instructions" sections and save.
  - Expected: All three sections are displayed on the shared event page with the entered content.
  - Verified: Schedule ("6:30 PM — Welcome Cocktails — Drinks and canapes in the foyer"), Dress Code ("Black tie optional"), Special Instructions ("Use basement parking; valet available after 6 PM.") all rendered on /event/event-1794108991739.

- [X] FT-03: Define multiple invitation options
  - Action: Add at least two invitation options (e.g., "Dinner only", "Drinks only", "Full evening") to an event and save.
  - Expected: All defined options appear on the event's invitation/RSVP interface for guests to select.
  - Verified: "Full Event" and "Dinner only" appeared as a "Select your attendance option" radiogroup after choosing "Yes"; the seeded wedding showed all 3 of its options (Full Celebration / Reception Only / Ceremony Only with descriptions).

- [X] FT-04: Add preference questions to an event
  - Action: Create a preference question (e.g., "Meal choice" with options Vegetarian/Non-vegetarian) attached to the event and save.
  - Expected: The question and its answer options are rendered on the RSVP form.
  - Verified: "Meal preference" with radios "Vegetarian" / "Non-vegetarian" rendered on the RSVP form after selecting "Yes" and an attendance option.

- [ ] FT-05: Guest submits RSVP with response and preferences
  - Action: On the shared event page, open RSVP as "Yes", select an invitation option (e.g., "Full evening"), answer the preference question, and submit.
  - Expected: RSVP is recorded and the guest's response, chosen invitation option, and preference answers are visible in the organizer's summary.
  - Bug Report:
    - Issue: RSVP submission silently dropped (no guest record created)
    - Actual: Submitted Yes / "Dinner only" / "Vegetarian"; toast "RSVP updated successfully!" appeared, but Guest Summary stayed "Attending (0) No guests", "By Option" showed Full Event (0) / Dinner only (0), and "Preferences" showed "Vegetarian 0 (0%) / Non-vegetarian 0 (0%)"; dashboard card still read "0 yes". The app only supports RSVPs attached to an implicit pre-seeded "current guest" (e.g., Michael Chen on the wedding); a shared event page for a newly created event has no way for a guest to identify themselves (the RSVP form has no name field) and the response is never recorded.

- [ ] FT-06: RSVP "No" and "Maybe" responses
  - Action: Submit two more RSVPs on the same event, one marked "No" and one "Maybe".
  - Expected: Both responses are saved and listed under the correct response group in the summary.
  - Bug Report:
  - - Issue: RSVP responses not persisted to summary (same root cause as FT-05)
    - Actual: "No" then "Maybe" each produced the toast "RSVP updated successfully!", but the By Status tab continued to show Attending (0) / Not Attending (0) / Maybe (0) / Pending (0) — no responses were listed. Also, the form holds only one current response at a time, so three distinct guest responses cannot be recorded from this page.

- [X] FT-07: Guest poll voting
  - Action: On the event page's poll (e.g., venue options "Rooftop Bar" vs "Garden Hall"), select one option and submit the vote.
  - Expected: The vote is recorded and current tallies are displayed for each poll option.
  - Verified: Clicking "Rooftop Bar" instantly showed "Rooftop Bar 1 vote (100%)", "0 votes (0%)" on the other option, and "1 total vote"; after re-voting, "Garden Hall 1 vote (100%)" / "Rooftop Bar 0 votes (0%)".

- [ ] FT-08: Comment thread posting
  - Action: Type a short message in the event page's comment input and submit.
  - Expected: The comment appears in the thread with the guest's name/identifier and is visible to other visitors of the page.
  - Bug Report:
    - Issue: Comments not shared with other visitors (no persistence/backend)
    - Actual: Posting "QA Tester / Is there a vegetarian menu option?" did work in-session — thread count became (1) and the comment rendered with name, "less than a minute ago" timestamp, and toast "Comment posted!". However, on a fresh page load (any other visitor) the shared URL /event/event-1794108991739 returns "Event Not Found"; all app state is in-memory (localStorage/sessionStorage/cookies are empty), so no posted comment is ever visible to another visitor.

- [X] FT-09: Edit event details after invites are sent
  - Action: Open an existing event with RSVPs already recorded, change the date/time and location, and save.
  - Expected: The shared event page immediately shows the updated details; existing RSVPs, poll votes, and comments are preserved.
  - Note: Edited date 2026-12-05→2026-12-19, time 18:00→19:30, venue "Grand Atrium Hall"→"Riverside Pavilion"; the shared page immediately showed "Saturday, December 19, 2026 / 7:30 PM - 11:00 PM / Riverside Pavilion" with toast "Event updated successfully!". Poll vote (Garden Hall 1 vote) and the posted comment were preserved. "Existing RSVPs" could not be tested because none can ever exist on a created event (FT-05 bug); on the seeded wedding, guest data likewise remains intact when editing.

- [X] FT-10: View grouped RSVP summary
  - Action: Open the organizer summary view for an event with multiple guests.
  - Expected: Guests are grouped by invitation option, by response ("Yes"/"No"/"Maybe"), and key preferences (e.g., meal counts) are displayed per group.
  - Verified on the wedding (5 guests): By Status — Attending (2: Emily Watson, [Michael Chen after update]), Not Attending (2), Maybe (1: David Park), Pending (1: Robert Kim); By Option — Full Celebration (1), Reception Only (0), Ceremony Only (0); Preferences — "Meal preference: Wild mushroom risotto (V) 1 (100%)", "Dietary restrictions: Gluten-free 1 (100%)", "Plus one: No 1 (100%)". Tabs also exist on created events (structure present; empty due to FT-05 bug).

- [X] FT-11: Archive area for canceled/past events
  - Action: Cancel an event (or open one whose date has passed) and navigate to the separate "past/canceled events" area.
  - Expected: The event appears there with its final RSVP counts and final poll results still readable.
  - Verified: /archive has "Past Events (1)" (Annual Company Holiday Party, "Completed", 2 yes) and "Canceled (1)" tabs; after canceling (confirm dialog + toast "Event canceled"), "Autumn Charity Gala QA" appeared under Canceled with Canceled badge and "0 yes" count; opening it shows the final closed poll ("After-party venue?" Closed, Garden Hall 1 vote 100%) and the Guest Summary groups. Caveat: canceled/edited state only survives within the session (same persistence defect).

## Constraint
- [ ] CS-01: Required fields enforced on event creation
  - Action: Attempt to submit the event form with the title or date/time left empty.
  - Expected: Submission is blocked and a validation message names the missing required field.
  - Bug Report:
    - Issue: Missing field-specific validation message
    - Actual: Submission was correctly blocked (URL stayed /create; empty title, start date, start time, and venue inputs all have HTML5 `required`, and the DOM showed exactly 4 invalid inputs). But no application-generated validation message exists anywhere in the DOM (query for error/alert/required text returned zero visible elements) — only the generic browser-native bubble "Please fill out this field." on the focused input. The message never names the missing field (e.g., "Title is required" / "Start Date is required"); the app has no inline error rendering at all.

- [X] CS-02: Close RSVPs
  - Action: As organizer, close RSVPs for an open event, then try to submit a new RSVP or change an existing one as a guest.
  - Expected: RSVP form is no longer submittable; the page shows RSVPs are closed, and no new/changed responses are recorded.
  - Verified: "Close RSVPs" (toast "RSVPs are now closed") removed the entire Yes/No/Maybe form and Submit button, replaced by the paragraph "RSVPs are currently closed for this event.", and the organizer button flipped to "Open RSVPs". No submission is possible → no responses recorded.

- [X] CS-03: Close poll
  - Action: As organizer, close the event poll, then try to cast or change a vote as a guest.
  - Expected: Voting controls are disabled/hidden, results remain visible, and no new votes are accepted.
  - Verified: After "Close Poll", status badge changed "Open"→"Closed", both option buttons became `[disabled]`, and final tallies remained visible ("Garden Hall 1 vote (100%)", "1 total vote"). Organizer action became "Reopen Poll".

- [X] CS-04: One RSVP per guest, one vote per poll option set
  - Action: Attempt to submit a second RSVP for the same guest, and separately try to select two options in the single-choice poll.
  - Expected: Duplicate RSVP is rejected or replaces the prior one (never creates two entries); poll allows only one selection at a time.
  - Verified: Second/third RSVP submissions replace rather than duplicate — after submitting Yes→No→Maybe on the gala, summary stayed at a single (implicit) response state, never two entries; on the wedding, the current guest's existing "Yes" was replaced by "No" (Michael Chen appears exactly once, moving from Attending to Not Attending). Poll is a single-choice control: clicking "Garden Hall" after "Rooftop Bar" moved the vote (total stayed 1) rather than selecting both. Note: the replace-behavior is partly a consequence of the FT-05 drop bug on guest-less events.

## Interaction
- [X] IX-01: Confirmation feedback after RSVP submission
  - Action: Submit an RSVP on the shared event page.
  - Expected: A success confirmation (toast/message) appears and the guest's recorded response is shown; error feedback appears if submission fails.
  - Verified: Every submission produced a toast ("RSVP updated successfully!") in the notifications region, and where RSVPs record (seeded wedding) the recorded response was shown (form kept "No" selected; Michael Chen listed under Not Attending). Note: on guest-less created events the confirmation appears but the response itself is never shown — recorded as FT-05.

- [X] IX-02: Live poll result update after voting
  - Action: Cast a vote, then reload/revisit the event page as another guest.
  - Expected: Poll tallies reflect the new vote (bar/counts updated), not the stale pre-vote state.
  - Verified: After voting, results updated instantly (0 votes→1 vote/100% with bar), and on revisit via Dashboard → event page the tallies showed the new state ("Garden Hall 1 vote (100%), 1 total vote") — not stale. Caveat: a full page reload (true second visitor) shows nothing because all data is lost — covered under FT-08/global persistence defect.

- [X] IX-03: Hidden optional sections when empty
  - Action: View a shared event page for an event where schedule, dress code, and special instructions were left blank.
  - Expected: Those sections are not displayed (no empty headings/placeholders) on the guest-facing page.
  - Verified: "Minimal Test Event" (title/date/time/venue only) — the guest page contains only date/time, venue, Discussion, and RSVP/Guest Summary. No "Schedule", "Dress Code", "Special Instructions", or "Polls" headings/placeholders rendered at all.

## Content
- [X] CT-01: Event details render consistently across views
  - Action: Compare the event's title, date/time, location, and category shown on the shared event page, the RSVP form, and the organizer summary/archive view.
  - Expected: All views show identical, correctly formatted values matching what the organizer entered (no placeholder text like "Lorem ipsum" or broken/undefined values).
  - Verified: "Autumn Charity Gala QA" showed identically across event page, dashboard card, archive card, and edit form — 🎉 Social, "Saturday, December 19, 2026", "7:30 PM - 11:00 PM", "Riverside Pavilion" (after edit). Inputs 2026-12-19/19:30 were correctly reformatted (no raw "undefined"/"Invalid Date"). The RSVP panel and Guest Summary simply don't repeat event details (no contradictions or broken values). Seed wedding values also matched across all views.

- [X] CT-02: Category options present and relevant
  - Action: Open the category selector on the event form.
  - Expected: A list of event-planning-relevant categories (e.g., Party, Dinner, Wedding, Meeting) is offered, and the chosen category is shown with the event.
  - Verified: The selector offers 🎂 Birthday, 💒 Wedding, 💼 Corporate, 🎉 Social, 🎄 Holiday, ✨ Celebration, 📅 Other — event-planning-relevant. Choosing "✨ Celebration" rendered "✨ Celebration" on that event's page; default "🎉 Social" correctly displayed on the gala across dashboard/event/archive; dashboard/seed events show their categories (Birthday/Wedding/Social/Corporate).
