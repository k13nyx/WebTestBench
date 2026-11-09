# Test Result

## Functionality
- [X] FT-01: Organizer can create a new event with all required details
  - Action: As organizer, open the event creation form, enter title "Jazz Night", category "concert", a future date, location text "City Hall", and one ticket type (name "General", price 25, quantity 100), then click "Create"/"Save".
  - Expected: The form is accepted and "Jazz Night" appears in the event list and in the organizer's event management view.
  - Verified: toast "Event created / Your new event has been created successfully.", Total Events incremented 3→4, "Jazz Night · Concert · Mar 15, 2027 at 19:00 · City Hall" appears in the management view AND in the visitor "All Upcoming Events" list (via SPA navigation). *(Observation: the app stores state in memory only — a full browser reload resets data to the 3 default events; persistence was not required by the checklist but is a robustness concern.)*

- [X] FT-02: Visitor can browse all upcoming events
  - Action: As visitor, open the home/events listing page.
  - Expected: A list/grid of upcoming events is displayed, each shown as a card or row entry.
  - Verified: "All Upcoming Events" section renders event cards (article elements wrapped in links to /event/{id}) for both future events.

- [X] FT-03: Visitor can filter events by category
  - Action: On the listing page, select the category filter value "workshop" (or equivalent) and apply it.
  - Expected: Only events whose category is "workshop" remain visible; concert and conference events are hidden.
  - Verified: Clicking the "Workshops" button → heading "1 events found", only "Pottery Workshop" card remains; "Jazz Night" (Concert) hidden; a "Clear filters" control appears.

- [X] FT-04: Visitor can filter events by date
  - Action: On the listing page, set the date filter to a specific date on which a default event occurs and apply it.
  - Expected: Only events scheduled on that selected date are shown; events on other dates are hidden.
  - Verified: Setting the date filter input to 2027-03-15 → only "Jazz Night" (Mar 15, 2027) shown, "Pottery Workshop" hidden. Note: all seeded default events are in the past (2025) and, per CS-03, excluded from the upcoming list, so the date filter was exercised against an event present in the browse list; the date-equality filter itself works correctly.

- [X] FT-05: Visitor can search events by keyword
  - Action: Type a keyword taken from an existing event's title (e.g., "Jazz") into the search box and submit.
  - Expected: The results include the matching event and exclude events whose title/description/location do not contain the keyword.
  - Verified: Typing "Jazz" → live results show only "Jazz Night"; non-matching "Pottery Workshop" excluded; past "Summer Jazz Festival" also correctly excluded from search results.

- [X] FT-06: Visitor can open an event's detailed page
  - Action: From the listing, click the title or "View details" link of any event.
  - Expected: A dedicated detail page for that event loads, showing that event's own title, category, date, location, and ticket types.
  - Verified: Card links to /event/event-1794109680163; page shows "Jazz Night" (h1), "Concert", "Monday, March 15, 2027", "19:00", location, and the "Select Tickets" section with its own ticket type.

- [X] FT-07: Visitor can reserve tickets through the checkout form
  - Action: On an event detail page, choose ticket type "General", set quantity to 2, fill the required checkout fields (name and email), and click the reserve/confirm button.
  - Expected: The reservation is completed and the event's reservation appears in the organizer's reservation list with quantity 2.
  - Verified: Organizer dashboard shows "Test Visitor / visitor@example.com / $50 / Nov 8, 2026 — General × 2" under Jazz Night; availability dropped 100→98. Note: the checkout form also requires a Phone Number field (first submit was blocked and focus moved to Phone) — name and email alone were not sufficient.

- [X] FT-08: Organizer can update an existing event
  - Action: As organizer, open the edit form for an existing event, change the location text to "Grand Arena", save, then reopen the event's detail page.
  - Expected: The change is saved — the detail page and management list now display "Grand Arena".
  - Verified: Edit dialog pre-filled; after "Update Event" (toast "Event updated"), management card, listing card, and the reopened detail page all show "Grand Arena".

- [X] FT-09: Organizer can view the list of ticket reservations
  - Action: As organizer, open the reservations/registrations view.
  - Expected: A list of reservations is rendered showing one entry per reservation made against the organizer's events.
  - Verified: Dashboard renders per-event "View Reservations" sections; Jazz Night shows exactly its 2 reservations ("General × 2", "General × 1"), defaults show their 3, empty event shows "No reservations yet for this event." Total Reservations = 5.

## Constraint
- [X] CS-01: Event cannot be created without required fields
  - Action: As organizer, leave the title field empty (and date empty) and click "Create"/"Save".
  - Expected: Submission is blocked and a validation message is shown on the missing field(s); no new event is added to the list.
  - Verified: Submit stayed open, Total Events remained 5, and DOM check showed `title.required = true`, `date.required = true`, both now `:invalid` — the browser's native "Please fill out this field" constraint bubble is the validation message (no custom inline app message).

- [X] CS-02: Cannot reserve more tickets than the available quantity
  - Action: On an event detail page, note the remaining quantity of a ticket type, then attempt to select a quantity greater than that remaining number and submit checkout.
  - Expected: The request is rejected — the quantity input is capped/disabled with an error such as "Only X tickets available", and no over-sell reservation is recorded.
  - Verified: Remaining quantity shown as "100 tickets available". Quantity selection is a stepper (no free-text input); repeatedly pressing "+" was capped — the increment button becomes disabled (per-order cap of 10, well below the 100 available), so selecting >100 is impossible and no over-sell reservation was recorded (stock decremented correctly: 100→98→97). Note: the cap is enforced silently (button disabled) without an explicit "Only X tickets available" error string.

- [X] CS-03: Past events are excluded from the upcoming-events browse list
  - Action: With a default event whose date is before 2026-11-08 present in the data, load the visitor listing and the category/date filters.
  - Expected: The past event is not displayed anywhere in the upcoming events listing or filter results.
  - Verified: Default past events (Jul 15, 2025; Sep 20, 2025; Oct 15, 2025) never appear in "All Upcoming Events", category filter results, date filter results, or search results (e.g., "Jazz" did not return "Summer Jazz Festival"). Observation: a separate static "Featured Events" module on the home page does show two past-dated events; this is outside the upcoming listing/filter scope specified.

- [X] CS-04: Category is restricted to the three defined options
  - Action: On the event creation form and on the visitor category filter, inspect the available category choices.
  - Expected: Exactly "concert", "conference", and "workshop" are selectable; no free-text category entry is possible.
  - Verified: Creation/edit form uses a closed select with exactly the options "Concert", "Conference", "Workshop" (no free-text input; value is a `select` element). Visitor filter offers only the fixed buttons "All Events / Concerts / Conferences / Workshops".

## Interaction
- [X] IX-01: Confirmation is displayed after a reservation is completed
  - Action: Complete a valid checkout reservation as a visitor.
  - Expected: An explicit success message/toast (e.g., "Reservation confirmed") is shown, and/or the user is redirected to a confirmation view for that reservation.
  - Verified: Notification region displays toast "Reservation Confirmed! Your tickets for Jazz Night have been reserved." and the app redirects to the home page after a "Processing…" state.

- [X] IX-02: List results update in response to filter and search actions
  - Action: Change the category filter, then change the keyword search box, on the listing page.
  - Expected: The displayed event results change immediately to match the new criteria (previous results cleared), rather than remaining stale.
  - Verified: Clicking "Workshops" instantly reduced 2→1 cards and updated the results heading to "1 events found"; typing "Jazz" in search instantly swapped the list (Pottery Workshop removed, no stale entries); clearing filters restored both events.

- [X] IX-03: Checkout total recalculates when ticket quantity changes
  - Action: On the checkout form, increase the quantity of a ticket type from 1 to 3.
  - Expected: The displayed order total updates to reflect the new quantity (e.g., 3 × the ticket price), and any per-type subtotal shown also updates.
  - Verified: Total updated live: "Total (1 tickets) $25" → "Total (2 tickets) $50" → "Total (3 tickets) $75" (3 × $25); checkout Order Summary per-type subtotal also tracked quantity ("General × 2 — $50", Total $50).

## Content
- [X] CT-01: Listing entries display complete event summary information
  - Action: Inspect each event card/row on the visitor listing page.
  - Expected: Every entry shows the event's title, category, date, location text, and a price indicator — no blank, "undefined", "null", or placeholder-lorem text.
  - Verified: Every upcoming card shows title (h3), category badge, date + time, location, "From $25"/"From $15" price indicator, and "View Details →"; no undefined/null/placeholder text anywhere.

- [X] CT-02: Detail page shows all ticket types with price and remaining quantity
  - Action: Open an event that has multiple ticket types and inspect the ticket selection section.
  - Expected: Each ticket type is listed with its name, its price, and its available/remaining quantity, matching the organizer's data.
  - Verified: Pottery Workshop detail lists "Standard — $15 — 50 tickets available" and "Premium Kit — $30 — 20 tickets available", matching organizer entry data; Jazz Night showed remaining stock correctly reflecting reservations ("97 tickets available" after 3 booked).

- [X] CT-03: Reservation list content is relevant and correctly attributed
  - Action: Inspect the rows in the organizer's reservation list after reservations exist.
  - Expected: Each row shows the reserved event title, the ticket type/quantity, the reserver's identifying detail, and the reservation date, with no unrelated or empty rows.
  - Verified: Rows grouped under their event's heading (e.g., under "Jazz Night": Test Visitor · visitor@example.com · 555-0199 · $50 · Nov 8, 2026 10:50 AM · "General × 2"), defaults correctly attributed to their own events; empty event shows an explicit "No reservations yet for this event." message — no unrelated or blank rows. *(Minor note: the event title appears as the section grouping rather than repeated inside each row.)*
