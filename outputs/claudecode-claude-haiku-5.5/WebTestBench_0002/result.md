# Test Result

**Run summary:** 93 of 100 tool calls used. Testing ran against http://localhost:6002/ in an in-session flow, with a hard reload checked once. The seeded data is dated 2025 and today is 2026-11-09, so almost every "upcoming" check was blocked by the data. Several failures are real defects regardless of that.

**Side effects on the app (not restored):**
- Summer Jazz Festival location was changed to "Riverside Hall, New York" (FT-08).
- Summer Jazz General Admission quantity was saved as **3** (CS-05).
- One reservation was created: Test Buyer, buyer@example.com, General Admission × 2, $90 (FT-04).

## Functionality

- [ ] FT-01: Visitor can browse all upcoming events
  - Action: Open the events home page without logging in.
  - Expected: Every default event dated today or later appears in the list, showing title, category, date, and location text.
  - Bug Report:
    - Issue: Upcoming list empty / wrong date data
    - Actual: "All Upcoming Events" shows "No events found". The only default events are "Summer Jazz Festival" (July 15, 2025) and "Tech Innovation Summit 2025" (Sep 20, 2025). Both are before today (2026-11-09), so the list is empty. The featured grid still shows both past events.

- [X] FT-02: Visitor can open an event's detail page
  - Action: Click the title of any default event in the list.
  - Expected: Detail page shows title, category, date, location text, and each ticket type with its name, price, and remaining quantity.
  - Note: The upcoming list is empty, so I opened the event from the featured card title. The detail page showed all required fields.

- [X] FT-03: Visitor can select ticket quantities and proceed to checkout
  - Action: On a detail page, set the quantity of one ticket type to 2 (using the + control or typing 2), then click "Checkout" (or "Reserve").
  - Expected: Checkout form opens and summarizes the chosen ticket type, quantity 2, and total equal to price × 2.
  - Note: The button is labeled "Continue to Checkout". The summary showed "General Admission × 2" and total $90 (= $45 × 2).

- [X] FT-04: Completing checkout reserves the tickets
  - Action: On the checkout form, enter a valid name and email, then click "Place Order" (or "Submit").
  - Expected: A reservation is created; the event's remaining quantity for the chosen ticket type drops by the reserved amount.
  - Note: Remaining General Admission dropped from 500 to 498 in-session, and the reservation appears on the organizer dashboard. The form also requires a Phone field, which the checklist does not mention. After a full page reload, the public page showed 500 again, so the change does not persist.

- [ ] FT-05: Category filter returns only matching events
  - Action: On the events list, select "Conference" in the category filter.
  - Expected: Only upcoming events categorized as Conference are listed. Selecting "All" restores the full list.
  - Bug Report:
    - Issue: Filter cannot be verified / empty results
    - Actual: The upcoming list shows "No events found" for "Conferences", "All Events", and every other filter state. "All" does not restore any upcoming events, because none are dated today or later.

- [ ] FT-06: Date filter returns only events in the chosen date range
  - Action: Set the "From" and "To" date filters to a range that contains exactly one default event, then apply.
  - Expected: Only events whose dates fall within the range are listed, and the boundary dates are included.
  - Bug Report:
    - Issue: Missing date range filter
    - Actual: The filter bar has only one unlabeled date input and no "From" or "To" controls. The upcoming list is empty for every state, so no range can show an event.

- [ ] FT-07: Keyword search matches event title and location
  - Action: Type a word from a default event's title (for example, "Summit") in the search box and submit.
  - Expected: Only events whose title or location text contains the keyword (case-insensitive) are listed.
  - Bug Report:
    - Issue: Search returns no matches for a default event title
    - Actual: Searching "Summit" + Enter shows "No events found". The default event "Tech Innovation Summit 2025" contains the keyword, but it is hidden because it is dated before today.

- [ ] FT-08: Organizer can view and update their existing events
  - Action: Log in with the default organizer account, open "My Events", click a default event, change its location text, and click "Save".
  - Expected: "My Events" lists only this organizer's events with title, category, and date. After saving, a success confirmation appears and the new location shows on the event's public detail page.
  - Bug Report:
    - Issue: No login or "My Events" page; update not visible publicly
    - Actual: There is no login step and no "My Events" label. The page is "Organizer Dashboard" with "Your Events", and it opens without authentication. Saving the location showed the "Event updated" toast and the dashboard shows "Riverside Hall, New York". After a full reload, the public detail page still shows "Central Park Amphitheater, New York". Also, the edit form loads General Admission quantity as 498 (the remaining count, not the 500 total), so saving unchanged rewrites capacity.

- [X] FT-09: Organizer can view the reservation list for an event
  - Action: Logged in as the organizer, open a default event that has reservations (or the one from FT-04) and select "Reservations".
  - Expected: A list appears with one row per reservation, showing buyer name, email, ticket type, quantity, and total.
  - Note: "View Reservations" on Summer Jazz showed one row per reservation with name, email, ticket type, quantity, and total.

- [X] FT-10: Organizer create form contains all required event fields
  - Action: Logged in as the organizer, click "Create Event" and inspect the form without submitting.
  - Expected: Form contains Title (text), Category (dropdown with only Concert, Conference, Workshop), Date (date picker), Location (text), and a ticket-type section with Name, Price, and Quantity fields plus an "Add Ticket Type" control.
  - Note: The control is labeled "Add Ticket" (not "Add Ticket Type"); the category options were Concert, Conference, Workshop.

## Constraint

- [X] CS-01: Checkout is blocked when a required field is empty or the email is malformed
  - Action: On the checkout form, leave the Name field empty and click "Place Order". Then enter "user@" in Email and click "Place Order" again.
  - Expected: Both attempts are blocked, a validation message appears beside the faulty field, and no reservation is created.
  - Note: Both attempts were blocked by native browser validation ("Please fill out this field." and "Please enter a part following '@'"). The dialog stayed open and no reservation was created. The messages are browser-native bubbles, not DOM text.

- [ ] CS-02: Ticket quantity cannot exceed the remaining quantity
  - Action: On a detail page, click the + control for a ticket type until it passes its displayed remaining quantity (or type a number larger than it).
  - Expected: The quantity stops at the remaining amount (or an error states the maximum), and the checkout cannot be started with a higher number.
  - Bug Report:
    - Issue: Quantity capped at the wrong limit
    - Actual: Backstage Pass shows "20 tickets available". The "+" control disabled itself at 10 with no maximum message, so the quantity stopped short of the remaining 20.

- [ ] CS-03: Checkout cannot proceed with zero tickets selected
  - Action: On a detail page, leave all ticket quantities at 0 and click "Checkout".
  - Expected: Checkout does not open; a message such as "Select at least one ticket" appears.
  - Bug Report:
    - Issue: Missing zero-ticket message
    - Actual: At zero tickets the checkout bar is removed entirely, so no checkout control is available. No "Select at least one ticket" message appears anywhere on the page.

- [X] CS-04: Organizer create and edit forms reject missing required fields or negative prices
  - Action: On the Create Event form, leave Title empty and click "Save". Then on an existing event's edit form, enter -5 as a ticket price and click "Save".
  - Expected: Both saves are blocked with an error on the Title field and the price field respectively; no change is stored.
  - Note: The create form was blocked by native validation on Title ("Please fill out this field."). The edit form was blocked by native validation on price ("Value must be greater than or equal to 0."). Cancel was used afterwards, so nothing was stored.

- [ ] CS-05: Organizer cannot set a ticket quantity below the number already reserved
  - Action: Logged in as the organizer, edit an event that has reservations for a ticket type, and set that type's quantity to a number lower than the reserved count, then click "Save".
  - Expected: Save is rejected with a message stating the minimum allowed quantity; the stored quantity is unchanged.
  - Bug Report:
    - Issue: Incorrect quantity validation
    - Actual: Summer Jazz General Admission has 4 reserved (Alice 2 + Test Buyer 2). Setting quantity to 3 and clicking "Update Event" showed "Event updated" with no rejection, and the quantity was stored as 3.

- [ ] CS-06: Visitors cannot access organizer pages
  - Action: Logged out (or logged in as a visitor), navigate directly to the organizer "My Events" page.
  - Expected: Access is denied or redirected to the login page; no event management controls or reservation data are shown.
  - Bug Report:
    - Issue: Unauthenticated access to organizer pages
    - Actual: The "Organizer Dashboard" at /organizer loads with no login. It shows total revenue, reservation lists with buyer names, emails, and phone numbers, and edit and delete controls.

## Interaction

- [X] IX-01: Total price updates immediately when ticket quantity changes
  - Action: On a detail page with a ticket type priced at a known amount, click + once, then click + again, then click − once.
  - Expected: The displayed total updates on each click (price × quantity) without a page reload.
  - Note: The total went $45 → $90 → $45 in-session, with no reload.

- [X] IX-02: Filter and search update results instantly and show an empty-state message
  - Action: Apply the category "Workshop" filter, then type the keyword "zzzz" in the search box and press Enter.
  - Expected: The list refreshes without a full page reload after each change; with no matches, the message "No events found" appears in place of the list.
  - Note: "No events found" appeared, and a window marker survived the interactions, so there was no reload. The upcoming list is empty in every state, so the refresh itself was not really exercised.

## Content

- [ ] CT-01: Event category, date, and price display consistently across list, detail, and organizer views
  - Action: For one default event, note its category, date, and ticket price on the events list, the detail page, and the organizer edit form.
  - Expected: Category is one of Concert, Conference, or Workshop; the date and price values are identical in all three views, and prices show a currency symbol with two decimal places.
  - Bug Report:
    - Issue: Price format missing two decimal places
    - Actual: Category (Concert) and date (July 15, 2025 / 2025-07-15) match across views, and General Admission is $45 on detail and edit. Prices render as "$45", "$120", "$250" with no decimal places, not two.

- [X] CT-02: Reservation details in the organizer view match the checkout entries
  - Action: Compare the reservation created in FT-04 with the organizer's reservation list for that event.
  - Expected: Buyer name, email, ticket type, quantity, and total in the organizer list exactly match the values entered at checkout and shown in the checkout summary.
  - Note: The organizer list shows Test Buyer, buyer@example.com, General Admission × 2, $90. That matches the checkout entries and summary (the phone number 555-0123 is extra).