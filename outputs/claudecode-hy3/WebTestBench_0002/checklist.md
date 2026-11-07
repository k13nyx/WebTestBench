# Test Checklist

## Functionality
- [ ] FT-01: Organizer can create an event listing
  - Action: Open the "Create Event" form, fill in Title, Category, Date, Location, and add one ticket type with Price and Quantity, then click "Create".
  - Expected: A new event appears in the events list showing the entered title, category, date, and location.

- [ ] FT-02: Visitor can browse all upcoming events
  - Action: Open the events listing page.
  - Expected: A list of all upcoming events (default data) is displayed.

- [ ] FT-03: Visitor can filter events by category
  - Action: Select a category (e.g., "concert") from the category filter control and apply it.
  - Expected: Only events with the selected category are shown.

- [ ] FT-04: Visitor can filter events by date
  - Action: Apply a date filter (e.g., specific date or date range) using the date filter control.
  - Expected: Only events matching the date filter are shown.

- [ ] FT-05: Visitor can search events by keyword
  - Action: Type a keyword into the search field and submit.
  - Expected: Only events whose content matches the keyword are displayed.

- [ ] FT-06: Visitor can open an event detail page
  - Action: Click on an event from the listing.
  - Expected: The event detail page opens showing the full event information.

- [ ] FT-07: Visitor can select ticket quantities
  - Action: On the event detail page, set a quantity for a ticket type.
  - Expected: The selected quantity is captured and a running total price is displayed.

- [ ] FT-08: Visitor can complete checkout to reserve tickets
  - Action: Select ticket quantities and submit the checkout form with valid details.
  - Expected: A ticket reservation is created for the selected event.

- [ ] FT-09: Organizer can view their existing events
  - Action: Open the organizer's events management view.
  - Expected: A list of the organizer's existing events is displayed.

- [ ] FT-10: Organizer can update an existing event
  - Action: Open an existing event, edit its details (e.g., title or date), and save.
  - Expected: The event details are updated and reflected in the events list.

- [ ] FT-11: Organizer can view ticket reservations
  - Action: Open the reservations view.
  - Expected: A list of ticket reservations (event, ticket type, quantity) is shown.

## Constraint
- [ ] CS-01: Cannot create event with empty required fields
  - Action: Submit the Create Event form leaving Title or Date empty.
  - Expected: Submission is rejected with a validation error and no event is created.

- [ ] CS-02: Category must be from the allowed set
  - Action: Attempt to assign a category outside the allowed options (concert, conference, workshop).
  - Expected: The invalid category is not accepted (no such option available or submission rejected).

- [ ] CS-03: Cannot reserve more tickets than available
  - Action: Enter a ticket quantity greater than the available quantity and submit checkout.
  - Expected: Reservation is rejected with an error indicating insufficient tickets.

- [ ] CS-04: Checkout form requires valid input
  - Action: Submit the checkout form with empty required fields.
  - Expected: Submission is blocked and validation errors are shown.

## Interaction
- [ ] IX-01: Success feedback after key actions
  - Action: Create an event, then complete a ticket reservation.
  - Expected: A success toast/confirmation message appears after each completed action.

- [ ] IX-02: List updates dynamically on filter/search
  - Action: Apply a category/date filter or enter a keyword in the search field.
  - Expected: The events list updates to reflect the applied filter/search results.

## Content
- [ ] CT-01: Event list shows relevant event details
  - Action: Open the events listing page.
  - Expected: Each event shows its title, category, date, and location text.

- [ ] CT-02: Event detail shows all ticket types with prices
  - Action: Open an event detail page.
  - Expected: Each ticket type displays its name, price, and available quantity.

- [ ] CT-03: Displayed content is relevant and complete
  - Action: Review the events list and detail pages.
  - Expected: All text and data are event-related, consistent, and free of placeholder/lorem content.