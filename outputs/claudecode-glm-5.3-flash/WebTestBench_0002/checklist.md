# Test Checklist

## Functionality
- [ ] FT-01: Organizer can create a new event listing
  - Action: Open the organizer event creation form, fill in title "Jazz Night", select category "Concert", set a future date, enter location "Blue Hall, 12 Main St", and submit.
  - Expected: The event "Jazz Night" is created successfully and appears in the list of events.
- [ ] FT-02: Organizer can add ticket types with price and quantity to an event
  - Action: In the event creation/edit form, add a ticket type named "General" with price 25 and quantity 100, and save.
  - Expected: The ticket type "General" (price 25, quantity 100) is saved and shown on the event's detail page.
- [ ] FT-03: Organizer can update an existing event
  - Action: Open an existing event in the organizer area, change its title (e.g., to "Jazz Night Deluxe") or location, and save.
  - Expected: The change is saved and the updated title/location is displayed for that event everywhere it is shown.
- [ ] FT-04: Visitor can browse all upcoming events
  - Action: Open the events browse page as a visitor without applying any filter.
  - Expected: All upcoming events (from default data) are listed, each showing its title, category, date, and location.
- [ ] FT-05: Visitor can filter events by category
  - Action: On the browse page, select a single category filter (e.g., "Workshop").
  - Expected: Only events of category "Workshop" remain listed; events of other categories are not shown.
- [ ] FT-06: Visitor can filter events by date
  - Action: On the browse page, apply a date filter (e.g., a specific date or date range containing at least one default event).
  - Expected: Only events whose date matches the filter are listed.
- [ ] FT-07: Visitor can search events by keyword
  - Action: Enter a keyword that matches an existing event title or location (e.g., "Jazz") into the search box and submit.
  - Expected: Only events whose title/location/description contain the keyword are listed; non-matching events are hidden.
- [ ] FT-08: Visitor can view an event detail page
  - Action: Click on any event card in the browse list.
  - Expected: The detail page opens showing the event's title, category, date, location, and its ticket types with prices and available quantities.
- [ ] FT-09: Visitor can select ticket quantities and complete checkout
  - Action: On an event detail page, set quantity (e.g., 2) for a ticket type, open the checkout form, fill in buyer name and email, and submit.
  - Expected: The reservation is created successfully for the selected event, ticket type, and quantity.
- [ ] FT-10: Organizer can view a list of ticket reservations
  - Action: Open the organizer reservations area after a reservation has been made.
  - Expected: A list of reservations is shown, including at least the event name, ticket type, quantity, and buyer details for each reservation.

## Constraint
- [ ] CS-01: Event creation requires mandatory fields
  - Action: Submit the event creation form with the title (or other required fields) left empty.
  - Expected: Submission is rejected and a validation message is shown; no event is created.
- [ ] CS-02: Category is restricted to the allowed values
  - Action: On the event form, inspect the category options and attempt to use a value outside "Concert", "Conference", "Workshop" (e.g., type a custom value if possible).
  - Expected: Only "Concert", "Conference", and "Workshop" can be selected/saved; any other input is rejected.
- [ ] CS-03: Reserved ticket quantity cannot exceed available quantity
  - Action: On an event detail page, enter a ticket quantity greater than the displayed available quantity (e.g., 999 when only 100 remain) and attempt checkout.
  - Expected: The reservation is rejected with an appropriate message and no reservation is created.
- [ ] CS-04: Ticket quantity must be a positive number
  - Action: Set a ticket quantity to 0 or a negative value and attempt to proceed to checkout/submit.
  - Expected: Submission is blocked with a validation message; a reservation with quantity 0 or negative cannot be created.
- [ ] CS-05: Checkout form requires buyer contact details
  - Action: Submit the checkout form with the buyer name and/or email fields left empty (or with an invalid email format).
  - Expected: Submission is rejected with a validation message and no reservation is created.

## Interaction
- [ ] IX-01: Successful reservation shows a confirmation
  - Action: Complete a valid checkout form and submit it.
  - Expected: A success confirmation (message/screen) appears confirming the tickets were reserved, including the reserved event/quantity.
- [ ] IX-02: Filters and search update the event list in response to input
  - Action: Change the category/date filter or search keyword and observe the event list without reloading manually.
  - Expected: The displayed event list updates to reflect the current filter/search immediately after the action.
- [ ] IX-03: Available ticket quantity decreases after a reservation
  - Action: Note the available quantity of a ticket type, complete a reservation for N tickets, then revisit the event detail page.
  - Expected: The displayed available quantity is reduced by N.

## Content
- [ ] CT-01: Event cards display accurate core details
  - Action: Compare the details shown on each event card in the browse list with the actual event data.
  - Expected: Each card shows the correct title, category, date, and location text for its event, with no placeholder or irrelevant text.
- [ ] CT-02: Ticket types show price and quantity on the detail page
  - Action: Open an event detail page and inspect the ticket type section.
  - Expected: Each ticket type is listed with a clear name, its price (formatted as a price, e.g., "$25.00"), and its available quantity.
- [ ] CT-03: Reservation list entries show relevant reservation data
  - Action: Open the organizer's reservation list and inspect its entries.
  - Expected: Each entry clearly shows which event was reserved, which ticket type, the quantity reserved, and the buyer's name/email — no empty or irrelevant fields.