# Test Checklist

## Functionality
- [ ] FT-01: Organizer can create a new event listing
  - Action: On the organizer event page, fill in Title, Category, Date, Location, and submit.
  - Expected: The new event is saved and appears in the organizer's event list.

- [ ] FT-02: Organizer can attach ticket types to an event
  - Action: While creating/editing an event, add a ticket type with a Name, Price, and Quantity.
  - Expected: The ticket type is saved and displayed on the event.

- [ ] FT-03: Visitor can browse all upcoming events
  - Action: Open the events listing page.
  - Expected: All upcoming events are listed with title, category, date, and location.

- [ ] FT-04: Visitor can filter events by category
  - Action: Select a category (e.g., "Concert") in the category filter.
  - Expected: Only events matching the selected category are shown.

- [ ] FT-05: Visitor can filter events by date
  - Action: Apply a date filter (e.g., a specific day or range).
  - Expected: Only events within the selected date/range are shown.

- [ ] FT-06: Visitor can search events by keyword
  - Action: Enter a keyword (e.g., part of a title) in the search box and search.
  - Expected: Only events matching the keyword are shown.

- [ ] FT-07: Visitor can view an event detail page
  - Action: Click an event from the listing.
  - Expected: A detail page opens showing title, category, date, location, and ticket types with prices.

- [ ] FT-08: Visitor can select ticket quantities
  - Action: On the event detail page, choose a quantity for a ticket type.
  - Expected: The selected quantity is accepted and reflected in the running total.

- [ ] FT-09: Visitor can complete checkout to reserve tickets
  - Action: With a quantity selected, fill in the checkout form and submit it.
  - Expected: The reservation is created and the visitor receives a confirmation.

- [ ] FT-10: Organizer can view and update existing events
  - Action: Open an existing event in the organizer view, change a field (e.g., title or price), and save.
  - Expected: The change is saved and the updated value is shown.

- [ ] FT-11: Organizer can view the list of ticket reservations
  - Action: Open the reservations list for an event.
  - Expected: All reservations for that event are listed.

## Constraint
- [ ] CS-01: Event cannot be created with missing required fields
  - Action: Attempt to submit the event form with Title, Category, Date, or Location left empty.
  - Expected: Submission is blocked and the missing fields are indicated.

- [ ] CS-02: Event category is restricted to the defined values
  - Action: Open the category selector for an event.
  - Expected: Only "concert", "conference", and "workshop" are selectable.

- [ ] CS-03: Ticket quantity cannot exceed available stock
  - Action: On an event detail page, attempt to select a quantity greater than the ticket type's remaining quantity.
  - Expected: The quantity is capped or rejected; more than available cannot be selected.

- [ ] CS-04: Checkout requires mandatory contact fields
  - Action: Attempt to submit the checkout form with required fields (e.g., name, email) empty.
  - Expected: Submission is blocked and the required fields are indicated.

- [ ] CS-05: Sold-out ticket types cannot be reserved
  - Action: Locate a ticket type with zero remaining quantity and attempt to reserve it.
  - Expected: Reservation is prevented and the ticket type is shown as unavailable.

## Interaction
- [ ] IX-01: Successful reservation shows a confirmation
  - Action: Complete a valid checkout submission.
  - Expected: A success confirmation (message/notification) is displayed.

- [ ] IX-02: Search with no matches shows an empty-state message
  - Action: Search for a keyword that matches no event.
  - Expected: A "no results found" message is displayed instead of a blank list.

- [ ] IX-03: Updated event data reflects immediately after saving
  - Action: Edit an event (e.g., change its date) and save, then return to the events listing.
  - Expected: The listing shows the updated value without requiring a full restart.

## Content
- [ ] CT-01: Category options match the specified event types
  - Action: Inspect the category options available when creating or filtering events.
  - Expected: Exactly "concert", "conference", and "workshop" are offered.

- [ ] CT-02: Prices are displayed with a currency indicator
  - Action: View ticket types on an event detail page.
  - Expected: Each price is shown as a monetary value with a currency symbol (e.g., "$25"), not a bare number.

- [ ] CT-03: Event detail page shows all required fields
  - Action: Open any event detail page.
  - Expected: Title, category, date, location text, and ticket types (with prices and quantities) are all present.