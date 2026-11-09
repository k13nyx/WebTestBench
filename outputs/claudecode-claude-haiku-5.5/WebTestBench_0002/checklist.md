# Test Checklist

## Functionality
- [ ] FT-01: Visitor can browse all upcoming events
  - Action: Open the events home page without logging in.
  - Expected: Every default event dated today or later appears in the list, showing title, category, date, and location text.

- [ ] FT-02: Visitor can open an event's detail page
  - Action: Click the title of any default event in the list.
  - Expected: Detail page shows title, category, date, location text, and each ticket type with its name, price, and remaining quantity.

- [ ] FT-03: Visitor can select ticket quantities and proceed to checkout
  - Action: On a detail page, set the quantity of one ticket type to 2 (using the + control or typing 2), then click "Checkout" (or "Reserve").
  - Expected: Checkout form opens and summarizes the chosen ticket type, quantity 2, and total equal to price × 2.

- [ ] FT-04: Completing checkout reserves the tickets
  - Action: On the checkout form, enter a valid name and email, then click "Place Order" (or "Submit").
  - Expected: A reservation is created; the event's remaining quantity for the chosen ticket type drops by the reserved amount.

- [ ] FT-05: Category filter returns only matching events
  - Action: On the events list, select "Conference" in the category filter.
  - Expected: Only upcoming events categorized as Conference are listed. Selecting "All" restores the full list.

- [ ] FT-06: Date filter returns only events in the chosen date range
  - Action: Set the "From" and "To" date filters to a range that contains exactly one default event, then apply.
  - Expected: Only events whose dates fall within the range are listed, and the boundary dates are included.

- [ ] FT-07: Keyword search matches event title and location
  - Action: Type a word from a default event's title (for example, "Summit") in the search box and submit.
  - Expected: Only events whose title or location text contains the keyword (case-insensitive) are listed.

- [ ] FT-08: Organizer can view and update their existing events
  - Action: Log in with the default organizer account, open "My Events", click a default event, change its location text, and click "Save".
  - Expected: "My Events" lists only this organizer's events with title, category, and date. After saving, a success confirmation appears and the new location shows on the event's public detail page.

- [ ] FT-09: Organizer can view the reservation list for an event
  - Action: Logged in as the organizer, open a default event that has reservations (or the one from FT-04) and select "Reservations".
  - Expected: A list appears with one row per reservation, showing buyer name, email, ticket type, quantity, and total.

- [ ] FT-10: Organizer create form contains all required event fields
  - Action: Logged in as the organizer, click "Create Event" and inspect the form without submitting.
  - Expected: Form contains Title (text), Category (dropdown with only Concert, Conference, Workshop), Date (date picker), Location (text), and a ticket-type section with Name, Price, and Quantity fields plus an "Add Ticket Type" control.

## Constraint
- [ ] CS-01: Checkout is blocked when a required field is empty or the email is malformed
  - Action: On the checkout form, leave the Name field empty and click "Place Order". Then enter "user@" in Email and click "Place Order" again.
  - Expected: Both attempts are blocked, a validation message appears beside the faulty field, and no reservation is created.

- [ ] CS-02: Ticket quantity cannot exceed the remaining quantity
  - Action: On a detail page, click the + control for a ticket type until it passes its displayed remaining quantity (or type a number larger than it).
  - Expected: The quantity stops at the remaining amount (or an error states the maximum), and the checkout cannot be started with a higher number.

- [ ] CS-03: Checkout cannot proceed with zero tickets selected
  - Action: On a detail page, leave all ticket quantities at 0 and click "Checkout".
  - Expected: Checkout does not open; a message such as "Select at least one ticket" appears.

- [ ] CS-04: Organizer create and edit forms reject missing required fields or negative prices
  - Action: On the Create Event form, leave Title empty and click "Save". Then on an existing event's edit form, enter -5 as a ticket price and click "Save".
  - Expected: Both saves are blocked with an error on the Title field and the price field respectively; no change is stored.

- [ ] CS-05: Organizer cannot set a ticket quantity below the number already reserved
  - Action: Logged in as the organizer, edit an event that has reservations for a ticket type, and set that type's quantity to a number lower than the reserved count, then click "Save".
  - Expected: Save is rejected with a message stating the minimum allowed quantity; the stored quantity is unchanged.

- [ ] CS-06: Visitors cannot access organizer pages
  - Action: Logged out (or logged in as a visitor), navigate directly to the organizer "My Events" page.
  - Expected: Access is denied or redirected to the login page; no event management controls or reservation data are shown.

## Interaction
- [ ] IX-01: Total price updates immediately when ticket quantity changes
  - Action: On a detail page with a ticket type priced at a known amount, click + once, then click + again, then click − once.
  - Expected: The displayed total updates on each click (price × quantity) without a page reload.

- [ ] IX-02: Filter and search update results instantly and show an empty-state message
  - Action: Apply the category "Workshop" filter, then type the keyword "zzzz" in the search box and press Enter.
  - Expected: The list refreshes without a full page reload after each change; with no matches, the message "No events found" appears in place of the list.

## Content
- [ ] CT-01: Event category, date, and price display consistently across list, detail, and organizer views
  - Action: For one default event, note its category, date, and ticket price on the events list, the detail page, and the organizer edit form.
  - Expected: Category is one of Concert, Conference, or Workshop; the date and price values are identical in all three views, and prices show a currency symbol with two decimal places.

- [ ] CT-02: Reservation details in the organizer view match the checkout entries
  - Action: Compare the reservation created in FT-04 with the organizer's reservation list for that event.
  - Expected: Buyer name, email, ticket type, quantity, and total in the organizer list exactly match the values entered at checkout and shown in the checkout summary.