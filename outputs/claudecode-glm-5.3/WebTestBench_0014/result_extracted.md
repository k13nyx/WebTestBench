# Test Result

## Functionality
- [X] FT-01: Organizer can create a new event with core fields
  - Action: Open the event creation page and fill in Title, Date & Time, Location, and Category, then click the "Create Event" button.
  - Expected: Event is created and appears in the events list with all four entered values displayed correctly.
  - Verified: Event "QA Test Gala 2026" (✨ Celebration, Thursday, December 31, 2026, 7:00 PM – 1:00 AM, The Grand Test Hall) was created and appeared in the dashboard events list ("4 events") with all four values displayed correctly.

- [X] FT-02: Optional sections (schedule, dress code, special instructions) can be added to an event
  - Action: While creating (or editing) an event, fill in the optional Schedule, Dress Code, and Special Instructions sections and save.
  - Expected: The event saves successfully and each optional section's content is stored and shown on the event page.
  - Verified: Schedule item ("7:00 PM — Welcome cocktails — Meet and greet at the terrace bar."), Dress Code ("Black tie"), and Special Instructions ("Arrive 15 minutes early. Valet parking available at the main entrance.") all saved and displayed on the event page.

- [X] FT-03: Organizer can define multiple invitation options for an event
  - Action: In the event editor, add three invitation options (e.g., "Dinner only", "Drinks only", "Full evening") and save the event.
  - Expected: All three invitation options appear on the event's guest page and are selectable during RSVP.
  - Verified: Options "Full evening", "Dinner only", "Drinks only" were defined in the editor and all three appeared as selectable radios in the RSVP flow on the event page.

- [X] FT-04: Organizer can define preference questions for an event
  - Action: In the event editor, add a preference question (e.g., "Meal choice" with options, or "Activity preference") and save the event.
  - Expected: The preference question and its answer choices appear on the event's guest page as part of the RSVP flow.
  - Verified: Question "Meal choice" with options "Chicken", "Beef", "Vegetarian" was defined and appeared in the RSVP flow on the guest page.

- [X] FT-05: Guest can RSVP with "Yes", "No", or "Maybe" and pick an invitation option
  - Action: Open an existing event's shared page as a guest, select an invitation option, choose the "Yes" (or "No"/"Maybe") response, and submit.
  - Expected: The RSVP is recorded with the selected response and invitation option.
  - Verified: On event "Marcus's 40th Birthday Bash", clicked "Yes", selected invitation option "Drinks & Dancing", submitted ("RSVP updated successfully!"); the Guest Summary "By Option" tab recorded the guest (Amanda Foster) under "Drinks & Dancing" (2).

- [X] FT-06: Guest can answer preference questions during RSVP
  - Action: While completing an RSVP (responding "Yes"), select an answer for the preference question (e.g., a meal choice) and submit.
  - Expected: The selected preference answer is saved together with the RSVP.
  - Verified: Selected "Truffle pasta (V)" for "Dinner selection" and submitted; the Preferences summary tab shows "Truffle pasta (V) — 1 (50%)" saved with the RSVP.

- [X] FT-07: Guest can vote in the event poll
  - Action: On an existing event's shared page, vote for one of the poll options (e.g., a venue or activity option).
  - Expected: The vote is recorded and reflected in the poll's results.
  - Verified: Voted for "90s Hits" in the "What decade's music..." poll; results updated to "90s Hits — 1 vote (50%)".

- [X] FT-08: Guest can post a message in the comment thread
  - Action: On an existing event's shared page, type a short message into the comment input and post it.
  - Expected: The message is posted and visible in the event's comment thread.
  - Verified: Posted "Can't wait! Will the rooftop be heated in November?"; toast "Comment posted!" and the message is visible in the Discussion thread.

- [X] FT-09: Organizer can change event details after invites are sent
  - Action: Open an existing event that already has guest responses, edit its details (e.g., change the time or location), and save.
  - Expected: The change is saved and the updated detail is shown on the event page; existing RSVPs/poll votes are not lost.
  - Verified: Edited "Marcus's 40th Birthday Bash" (venue → "The Skyline Penthouse", start time → 8:00 PM); "Event updated successfully!" and updated details shown; existing RSVPs (Attending: Amanda Foster, Chris Johnson; Pending: Nina Patel), poll votes (2 total votes), and comments all preserved.

- [X] FT-10: Organizer can view a summary grouped by invitation option, response, and preferences
  - Action: Open an existing event's summary/results view.
  - Expected: The summary lists guests grouped by invitation option, by RSVP response (Yes/No/Maybe), and by their preference answers.
  - Verified: Guest Summary provides "By Status" (Attending (2), Not Attending (0), Maybe (0), Pending (1) with guest names), "By Option" (Full Evening (0) / Drinks & Dancing (2)), and "Preferences" (Dinner selection: Truffle pasta (V) 1 (50%)...; Preferred spirit: Whiskey 1, Vodka 1...) groupings.

- [X] FT-11: Canceled or past events are accessible in a separate area with final results
  - Action: Open the separate area for canceled/past events and select one of them.
  - Expected: The event is viewable there, showing its final RSVP results and final poll results.
  - Verified: Archive page ("View past and canceled events with their final RSVP and poll results") has "Past Events (1)" and "Canceled (1)" tabs; opened the canceled "Summer Backyard BBQ" — it shows final RSVP results (Attending (2): Jake Williams, Sarah Miller) and final poll results (Cornhole 2 votes (50%), Volleyball 1 (25%), Giant Jenga 1 (25%), Croquet 0, 4 total votes).

## Constraint
- [X] CS-01: Event cannot be created without required fields
  - Action: On the creation page, leave Title (or Date/Location/Category) empty and attempt to save.
  - Expected: The event is not created and a validation message identifies the missing required field(s).
  - Verified: Clicking "Create Event" with empty fields did not create the event; the required Title field is flagged (native validation: "Please fill out this field.", input `required` + `checkValidity() === false`, focus moved to the missing field).

- [X] CS-02: Closed RSVPs reject new responses
  - Action: As organizer, close RSVPs for an event, then as a guest attempt to submit an RSVP.
  - Expected: The RSVP cannot be submitted; the RSVP section shows it is closed.
  - Verified: Clicked "Close RSVPs" ("RSVPs are now closed"); the RSVP form (Yes/No/Maybe, invitation options, preference questions, submit button) was removed and replaced with "RSVPs are currently closed for this event." — no RSVP can be submitted.

- [X] CS-03: Closed poll rejects new votes
  - Action: As organizer, close the poll for an event, then as a guest attempt to vote.
  - Expected: The vote is not recorded; the poll shows results but voting is disabled.
  - Verified: Clicked "Close Poll"; poll status changed to "Closed", all poll option buttons became disabled (voting not possible) while results (90s Hits 1 vote (50%), 2000s Bangers 1 vote (50%), 2 total votes) remain displayed.

- [X] CS-04: Empty comment cannot be posted
  - Action: On an event page, click the comment post button with an empty comment input.
  - Expected: No comment is added to the thread (a validation message may appear).
  - Verified: With an empty comment input the "Post" button is disabled; clicking it does nothing — comment count remains unchanged and no empty comment is added to the thread.

## Interaction
- [X] IX-01: Creating an event shows a success confirmation
  - Action: Fill all required fields on the creation page and click "Create Event".
  - Expected: A success message (or clear confirmation) appears and the user is directed to the new event page.
  - Verified: Notification "Event created successfully!" appeared and the app navigated directly to the new event's page (/event/event-1794091815630).

- [X] IX-02: Poll results update immediately after a guest votes
  - Action: On an event page, vote for a poll option.
  - Expected: The poll's displayed vote counts/results update instantly to include the new vote without a page reload error.
  - Verified: After clicking "90s Hits", the displayed counts instantly changed from "90s Hits 0 votes (0%)" to "1 vote (50%)" (and "80s Classics" from 1 to 0) with no reload or error.

- [X] IX-03: Posted comment appears in the thread immediately
  - Action: Post a comment on an event page.
  - Expected: The new comment appears at the top/bottom of the thread right away, without needing to leave and return to the page.
  - Verified: The posted comment appeared instantly at the top of the thread (timestamp "less than a minute ago") and the discussion count updated from (1) to (2) without leaving the page.

## Content
- [X] CT-01: Event page displays all details exactly as entered
  - Action: Open an existing event page and compare Title, Date & Time, Location, Category, Schedule, Dress Code, and Special Instructions against what was entered/saved.
  - Expected: Every field's content matches the saved values with no truncation, placeholder text, or missing sections.
  - Verified: Event page for "QA Test Gala 2026" showed every field exactly as entered: Title, ✨ Celebration, "Thursday, December 31, 2026", "7:00 PM – 1:00 AM", "The Grand Test Hall", "42 Test Avenue, Testville, TS 12345", "Black tie", "Arrive 15 minutes early. Valet parking available at the main entrance.", and the Schedule item — no truncation, placeholders, or missing sections.

- [X] CT-02: Guest page content matches the organizer's definitions
  - Action: On an existing event's guest page, verify the invitation options, preference questions, and poll choices shown to guests.
  - Expected: The labels and choices shown to guests exactly match those the organizer defined for that event, with no extra or missing options.
  - Verified: On the created event's guest page the invitation options ("Full evening", "Dinner only", "Drinks only"), preference question ("Meal choice" → Chicken/Beef/Vegetarian), and poll options (Live band/DJ night/Board games) exactly matched the organizer's definitions; likewise on "Marcus's 40th Birthday Bash" (Full Evening $75 / Drinks & Dancing $35; Dinner selection: Prime ribeye/Pan-seared halibut/Truffle pasta (V); Preferred spirit: Whiskey/Vodka/Tequila/Non-alcoholic; poll: 80s Classics/90s Hits/2000s Bangers/Mix it up!) — no extra or missing options.
