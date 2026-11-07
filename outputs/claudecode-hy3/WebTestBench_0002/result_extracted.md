# Test Result

## Functionality
- [X] FT-01: Organizer can create an event listing
  - Action: Open the "Create Event" form, fill in Title, Category, Date, Location, and add one ticket type with Price and Quantity, then click "Create".
  - Expected: A new event appears in the events list showing the entered title, category, date, and location.
  - Result: PASS — Created "Toast Verify Event" (Concert, 2027-07-15, Toast Hall Orlando) and "QA Future Concert" (Concert, 2027-06-01, QA Hall Seattle); both appeared in the events list (Organizer "Your Events" count went 3→4, and the future-dated event appeared in the public listing).

- [ ] FT-02: Visitor can browse all upcoming events
  - Action: Open the events listing page.
  - Expected: A list of all upcoming events (default data) is displayed.
  - Bug Report:
    - Issue: Empty listing / default data not displayed
    - Actual: The "All Upcoming Events" section renders "No events found" / "Try adjusting your filters or search query." Although 3 default events exist (Summer Jazz Festival, Tech Innovation Summit 2025, Leadership & Management Masterclass), all are dated in 2025 (e.g., "July 15, 2025", "Sep 20, 2025", "Oct 15, 2025") while the current system date is 2026-11-07, so the listing's "upcoming" (future-date) filter excludes every default event. A future-dated event created during testing (2027-06-01 / 2027-07-15) DID appear, confirming the date filter — not a broken list — is the cause. Note: the "Featured Events" section still shows 2 default events, but the main "All Upcoming Events" list is empty.

- [X] FT-03: Visitor can filter events by category
  - Action: Select a category (e.g., "concert") from the category filter control and apply it.
  - Expected: Only events with the selected category are shown.
  - Result: PASS — Clicking "Concerts" showed "1 events found" (the Concert event) and clicking "Workshops" showed "0 events found" (no matching future event); filter correctly narrows by category.

- [X] FT-04: Visitor can filter events by date
  - Action: Apply a date filter (e.g., specific date or date range) using the date filter control.
  - Expected: Only events matching the date filter are shown.
  - Result: PASS — Setting the date input to 2027-06-01 showed "1 events found" (the matching event); changing it to 2027-06-02 showed "0 events found". Date filtering discriminates correctly.

- [X] FT-05: Visitor can search events by keyword
  - Action: Type a keyword into the search field and submit.
  - Expected: Only events whose content matches the keyword are displayed.
  - Result: PASS — Searching "QA" returned "1 events found" (matching event); searching "zzz" returned "0 events found". Search filters correctly.

- [X] FT-06: Visitor can open an event detail page
  - Action: Click on an event from the listing.
  - Expected: The event detail page opens showing the full event information.
  - Result: PASS — Clicking an event opened /event/1 with full info: title, category, date (Tuesday, July 15, 2025), time (19:00), location (Central Park Amphitheater, New York), description, and ticket types.

- [X] FT-07: Visitor can select ticket quantities
  - Action: On the event detail page, set a quantity for a ticket type.
  - Expected: The selected quantity is captured and a running total price is displayed.
  - Result: PASS — Incrementing General Admission to 1 displayed "Total (1 tickets): $45" and a "Continue to Checkout" button.

- [X] FT-08: Visitor can complete checkout to reserve tickets
  - Action: Select ticket quantities and submit the checkout form with valid details.
  - Expected: A ticket reservation is created for the selected event.
  - Result: PASS — Submitting the reservation for Backstage Pass × 10 produced a confirmation toast "Reservation Confirmed! Your tickets for Summer Jazz Festival have been reserved." and the Organizer Dashboard updated (Total Reservations 3→4, Total Revenue $1,169→$3,669, Summer Jazz Festival reservations 2→3).

- [X] FT-09: Organizer can view their existing events
  - Action: Open the organizer's events management view.
  - Expected: A list of the organizer's existing events is displayed.
  - Result: PASS — The Organizer Dashboard "Your Events" section lists the events (4 cards observed: Summer Jazz Festival, Tech Innovation Summit 2025, Leadership & Management Masterclass, Toast Verify Event).

- [X] FT-10: Organizer can update an existing event
  - Action: Open an existing event, edit its details (e.g., title or date), and save.
  - Expected: The event details are updated and reflected in the events list.
  - Result: PASS — Edited the title of Summer Jazz Festival to "Summer Jazz Festival EDITED" via the Edit Event dialog and saved; the events list then showed "Summer Jazz Festival EDITED" and no longer the old title.

- [X] FT-11: Organizer can view ticket reservations
  - Action: Open the reservations view.
  - Expected: A list of ticket reservations (event, ticket type, quantity) is shown.
  - Result: PASS — The reservations view for Summer Jazz Festival listed reservations with attendee, ticket type and quantity (e.g., "Test User / test@example.com / Backstage Pass × 10 / $2500", plus Alice Johnson, Carol Davis).

## Constraint
- [ ] CS-01: Cannot create event with empty required fields
  - Action: Submit the Create Event form leaving Title or Date empty.
  - Expected: Submission is rejected with a validation error and no event is created.
  - Bug Report:
    - Issue: Silent rejection — no validation error message
    - Actual: With Title/Date empty, clicking "Create Event" did not create an event (Total Events stayed at 3 and the dialog stayed open), but NO validation error message appeared anywhere in the form or as a toast/notification. Rejection occurs but the user receives no feedback explaining why.

- [X] CS-02: Category must be from the allowed set
  - Action: Attempt to assign a category outside the allowed options (concert, conference, workshop).
  - Expected: The invalid category is not accepted (no such option available or submission rejected).
  - Result: PASS — Category is a fixed dropdown offering only Concert, Conference, and Workshop (verified in the dialog's DOM). No free-text entry or invalid option is possible, so an out-of-set category cannot be assigned.

- [X] CS-03: Cannot reserve more tickets than available
  - Action: Enter a ticket quantity greater than the available quantity and submit checkout.
  - Expected: Reservation is rejected with an error indicating insufficient tickets.
  - Result: PASS (constraint satisfied) — The ticket quantity stepper enforces a hard cap (observed max 10 per ticket type, which is ≤ the available amount, e.g., Backstage Pass shows "20 tickets available" but the stepper disabled its "+" at 10). A user therefore cannot select more tickets than available; over-reservation is prevented. (Note: the prevention is done by input capping rather than a checkout "insufficient tickets" error message.)

- [ ] CS-04: Checkout form requires valid input
  - Action: Submit the checkout form with empty required fields.
  - Expected: Submission is blocked and validation errors are shown.
  - Bug Report:
    - Issue: Silent rejection — no validation error message
    - Actual: Clicking "Confirm Reservation" with empty Full Name / Email / Phone Number did not create a reservation (the dialog remained open), but NO validation errors (inline or toast) were displayed. Submission is blocked but the user gets no error feedback.

## Interaction
- [ ] IX-01: Success feedback after key actions
  - Action: Create an event, then complete a ticket reservation.
  - Expected: A success toast/confirmation message appears after each completed action.
  - Bug Report:
    - Issue: Missing success toast on event creation
    - Actual: After completing a ticket reservation, a success toast appeared ("Reservation Confirmed! Your tickets for Summer Jazz Festival have been reserved."). However, after creating an event, no success toast or confirmation message appeared — the Create dialog simply closed (event was created, confirmed by the events count increasing 3→4). The "after each completed action" expectation is not met for the create action.

- [X] IX-02: List updates dynamically on filter/search
  - Action: Apply a category/date filter or enter a keyword in the search field.
  - Expected: The events list updates to reflect the applied filter/search results.
  - Result: PASS — Applying category (Concerts→1, Workshops→0), date (2027-06-01→1, 2027-06-02→0), and search ("QA"→1, "zzz"→0) all caused the list heading ("X events found") and card set to update live.

## Content
- [X] CT-01: Event list shows relevant event details
  - Action: Open the events listing page.
  - Expected: Each event shows its title, category, date, and location text.
  - Result: PASS — Event cards in the listing display title, category badge, date, location, and price (e.g., "Toast Verify Event / Concert / Jul 15, 2027 / Toast Hall, Orlando / From $30"). (The default 2025 events are absent from the upcoming list — tracked under FT-02 — but every event that is displayed carries all required fields.)

- [X] CT-02: Event detail shows all ticket types with prices
  - Action: Open an event detail page.
  - Expected: Each ticket type displays its name, price, and available quantity.
  - Result: PASS — Summer Jazz Festival detail listed General Admission ($45, "500 tickets available"), VIP Seating ($120, "100 tickets available"), and Backstage Pass ($250, "20 tickets available"), each with name, price, and available quantity.

- [X] CT-03: Displayed content is relevant and complete
  - Action: Review the events list and detail pages.
  - Expected: All text and data are event-related, consistent, and free of placeholder/lorem content.
  - Result: PASS — No placeholder/lorem/TODO text was found anywhere in the inspected pages; all descriptions, locations, and ticket info are real, event-related, and consistent.
