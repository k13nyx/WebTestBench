All tests are complete. Here is the full checklist with updated statuses:

# Test Result

## Functionality

- [X] FT-01: Organizer can create a new event listing
  - Action: On the organizer's event creation form, fill in title, category, date, location text, and one ticket type (name, price, quantity), then click the "Create Event" button.
  - Expected: The event is created and appears in the organizer's event list with all entered details.
  - Verified: Created "Winter Wonderland Concert" (Concert, Dec 25 2026 18:00, Grand Hall, Vienna, ticket "Standard" $50 ×10) via the Create Event dialog; the event appeared immediately in "Your Events" with title/category/date/location correct and "Total Events" went 3 → 4.

- [ ] FT-02: Visitor can browse all upcoming events
  - Action: Open the public events listing page.
  - Expected: All upcoming default events are displayed, each showing at minimum the event title, category, date, and location.
  - Bug Report:
    - Issue: Empty events list — all default events excluded by the "upcoming" date filter
    - Actual: The "All Upcoming Events" section on http://localhost:6002/ displays "No events found" (heading "All Upcoming Events", 0 entries). All 3 seeded default events (Summer Jazz Festival – Jul 15, 2025; Tech Innovation Summit 2025 – Sep 20, 2025; Leadership & Management Masterclass – Oct 15, 2025) are filtered out because the list only renders events with `date >= today` (current date Nov 8, 2026) and every default event is past-dated. Only the 2 "Featured Events" cards render; the list itself shows nothing.

- [ ] FT-03: Visitor can filter events by category
  - Action: On the events page, select a category filter (e.g., "Concert").
  - Expected: Only default events in the selected category are shown; events in other categories are hidden.
  - Bug Report:
    - Issue: Category filter yields no default events (upcoming-date filter excludes all seed data)
    - Actual: Clicking "Concerts" shows "0 events found" — the default Concert event (Summer Jazz Festival) is not displayed, so no category shows its default events. The filter mechanism itself works (verified with a future-dated event: "Conferences" → 1 event shown, "Concerts" → hidden, "All Events" → shown), but every default event is killed by the upcoming-date filter before the category filter can display it.

- [ ] FT-04: Visitor can filter events by date
  - Action: Apply the date filter for a specific date (or date range) that matches a default event.
  - Expected: Only events on the selected date (or within the range) are shown; all other events are hidden.
  - Bug Report:
    - Issue: Date filter returns zero events for dates that match default events
    - Actual: Setting the date filter to 2025-07-15 (Summer Jazz Festival's date) yields "0 events found" — the matching event is hidden. The date filter only surfaces events that are also upcoming (`date >= today`); verified the mechanism works with a future date (2026-12-20 → "1 events found"), but all default events' dates are in the past, so any default-event date returns an empty list.

- [ ] FT-05: Visitor can search events by keyword
  - Action: Type a keyword from a default event's title or location into the search field and submit.
  - Expected: Only events containing the keyword are shown; non-matching events are hidden.
  - Bug Report:
    - Issue: Keyword search returns no results for default events
    - Actual: Searching "Jazz" (contained in default event title "Summer Jazz Festival") returns "0 events found" / "No events found — Try adjusting your filters or search query." The search matches title/location/description, but the upcoming-date filter excludes every past-dated default event before matching, so keywords from any default event yield nothing. (Search itself functions: "Leadership" returns the future-dated event.)

- [X] FT-06: Visitor can open an event detail page
  - Action: Click a default event in the events list.
  - Expected: A detail page opens showing that event's title, category, date, location text, and its ticket types with prices and quantities.
  - Verified: Clicking the seeded event entry (Executive Leadership Masterclass, /event/5) and the featured default event (Summer Jazz Festival, /event/1) both open detail pages showing title, category badge, date, time, location, description, and all ticket types with name, price, and availability (e.g., General Admission $45 – 500 available; VIP Seating $120 – 100; Backstage Pass $250 – 20).

- [X] FT-07: Visitor can select ticket quantities on the event detail page
  - Action: On a default event's detail page, set the quantity of an available ticket type (e.g., 2 tickets).
  - Expected: The selected quantity is applied and reflected in the ticket selection area before checkout.
  - Verified: Using the + stepper set "Two-Day Pass" to quantity 2 — the stepper displays "2" and the summary bar shows "Total (2 tickets) — $900" before checkout.

- [X] FT-08: Visitor can reserve tickets through the checkout form
  - Action: With ticket quantities selected, fill in the checkout form (e.g., name and email) and submit it.
  - Expected: Checkout completes successfully and a reservation is recorded for that event.
  - Verified: With 2× Two-Day Pass + 1× Team Package selected, filled Full Name/Email/Phone and confirmed; the "Reservation Confirmed!" toast appeared and the reservation was recorded — the organizer dashboard shows the new reservation (Dana White, $2700, Two-Day Pass × 2, Team Package (5) × 1) with totals updated to 4 reservations / $3,869 revenue.

- [X] FT-09: Organizer can view their existing events
  - Action: Open the organizer's event management view ("My Events" or equivalent).
  - Expected: The organizer's events are listed with identifying details such as title, category, and date.
  - Verified: The Organizer Dashboard's "Your Events" section lists all events with title, category badge, date/time, location, reservation count, and revenue (e.g., "Summer Jazz Festival — Concert — Jul 15, 2025 at 19:00").

- [X] FT-10: Organizer can update an existing event
  - Action: Open one of the organizer's events, change one or more fields (e.g., title and date), and save.
  - Expected: The changes persist — updated values are shown in the organizer's event list and on the event detail page.
  - Verified: Opened the Edit Event dialog for "Leadership & Management Masterclass", changed title to "Executive Leadership Masterclass" and date to 2026-12-20, saved; a "Your event has been updated successfully." toast appeared, the organizer list shows the new title/date, and the detail page (/event/5) shows "Executive Leadership Masterclass — Sunday, December 20, 2026".

- [X] FT-11: Organizer can view a list of ticket reservations
  - Action: Open the organizer's reservations view.
  - Expected: A list of reservations is displayed, each showing the event, ticket quantity, and attendee information.
  - Verified: The "View/Hide Reservations" toggle opens a reservations list under each event showing attendee name, email, phone, amount, date, and tickets with quantities (e.g., Alice Johnson — alice@email.com — 555-0101 — $90 — "Tickets: General Admission × 2"; and the newly created Dana White reservation).

## Constraint

- [X] CS-01: Event cannot be created with empty required fields
  - Action: On the event creation form, leave required fields (title, date) empty and click "Create Event".
  - Expected: The event is not created; validation messages indicate which required fields are missing.
  - Verified: Clicking "Create Event" with empty Title/Location/Date/Time/Ticket Name is blocked by native form validation (inputs carry `required`, `validity.valueMissing=true`; focus jumps to the first invalid field "Event Title" and the browser displays the required-field message). "Total Events" stayed at 3 — no event was created.

- [X] CS-02: Event category is restricted to the defined types
  - Action: Open the category selector on the event creation form and inspect the available options.
  - Expected: Only Concert, Conference, and Workshop can be selected; no free-text or undefined categories are accepted.
  - Verified: The Category control is a non-typeable select combobox offering exactly three options — Concert, Conference, Workshop (native select options: concert, conference, workshop). There is no free-text entry for category.

- [X] CS-03: Ticket quantity cannot exceed the available amount
  - Action: On a default event's detail page, attempt to select a quantity greater than a ticket type's available quantity.
  - Expected: The excess quantity is rejected (input capped or error shown); the reservation cannot proceed with the invalid quantity.
  - Verified: On "Team Package (5)" (10 tickets available), pressing + repeatedly caps the quantity at exactly 10 and the + button becomes disabled (`disabled=true`), preventing any excess; the total correctly shows "(12 tickets)" = 2×$450 + 10×$1800 at the cap. Checkout can only proceed with quantities ≤ availability.

- [X] CS-04: Checkout cannot be submitted with empty required fields
  - Action: On the checkout form, leave required fields (e.g., name, email) empty and submit.
  - Expected: No reservation is created; required-field errors are displayed.
  - Verified: Clicking "Confirm Reservation" with empty Full Name/Email/Phone is blocked by native validation (all three inputs `required` with `valueMissing=true`; focus moves to "Full Name" and the browser displays the required-field message). The dialog stays open and no reservation is recorded (reservations count unchanged until a valid submission).

## Interaction

- [X] IX-01: Success feedback after event creation
  - Action: Complete and submit the event creation form with valid data.
  - Expected: A success message or notification appears confirming the event was created.
  - Verified: After submitting the Create Event form, a toast notification appeared: "Event created — Your new event has been created successfully."

- [X] IX-02: Confirmation shown after checkout
  - Action: Submit the checkout form with valid data and selected ticket quantities.
  - Expected: A confirmation message or screen is displayed summarizing the reserved event and tickets.
  - Verified: The checkout dialog shows the order summary (Two-Day Pass × 2 — $900, Team Package (5) × 1 — $1800, Total $2700) and, on confirmation, displays the toast "Reservation Confirmed! — Your tickets for Executive Leadership Masterclass have been reserved."

- [X] IX-03: Total price updates when ticket quantities change
  - Action: On the event detail page, increase or decrease the quantity of a ticket type.
  - Expected: The displayed total price recalculates immediately to match quantity × unit price.
  - Verified: Increasing "Two-Day Pass" 0 → 1 → 2 updated the total immediately $450 → $900 ("Total (1 tickets)" → "Total (2 tickets)"); decreasing "Team Package (5)" 10 → 1 adjusted the total from $18,900 to $2700 in real time. Each total matched quantity × unit price exactly.

## Content

- [ ] CT-01: Event list displays accurate event information
  - Action: Compare each default event entry on the events page with its data on the detail page.
  - Expected: Title, category, date, and location text on every list entry match the event's actual data, with no missing or mislabeled fields.
  - Bug Report:
    - Issue: Event list renders zero entries — default events' information not displayed
    - Actual: The "All Upcoming Events" list displays no entries at all ("No events found"), so the default events' title/category/date/location are not shown in the list (third default event, Leadership & Management Masterclass, has no entry anywhere on the events page). The two "Featured Events" cards that do render are accurate — Summer Jazz Festival (Concert, July 15, 2025, Central Park Amphitheater, New York) and Tech Innovation Summit 2025 (Conference, Sep 20, 2025, Convention Center, San Francisco) each match their detail pages exactly — but the event list itself displays no event information because of the upcoming-date filter excluding all past-dated seed events.

- [X] CT-02: Ticket types on the detail page match the event's data
  - Action: Open a default event's detail page and inspect its ticket types.
  - Expected: Each ticket type shows the correct name, price, and quantity/availability consistent with the event's defined tickets.
  - Verified: Event 1: General Admission $45 (500 available), VIP Seating $120 (100), Backstage Pass $250 (20) — consistent with reservation data (GA ×2 = $90; VIP ×4 = $480). Event 2: Standard Pass $299 (1000), Premium Pass $599 (200), Executive Pass $999 (50) — consistent (Premium ×1 = $599). Event 3/5: Two-Day Pass $450 (80), Team Package (5) $1800 (10) — matches the organizer's stored ticket data.

**Root-cause note:** FT-02, FT-03, FT-04, FT-05, and CT-01 share one defect: the public events list applies `new Date(event.date) >= new Date()` ("only show upcoming events") while all seeded default events carry 2025 dates, which are in the past relative to the current date (Nov 8, 2026). The list, search, category filter, and date filter mechanics were all verified to work correctly with future-dated events, but with the shipped default data the visitor sees an empty list and can neither browse, filter, nor search any default event.