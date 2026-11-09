# Test Checklist

## Functionality
- [ ] FT-01: Organizer can create a new event with all required details
  - Action: As an organizer, create an event providing title, category (concert/conference/workshop), date, location text, and at least one ticket type with price and quantity.
  - Expected: The event is saved and appears in the event listings.
- [ ] FT-02: Organizer can view and update an existing event
  - Action: Open an existing event from the organizer's event list, change its title and ticket price, then save.
  - Expected: The event detail page shows the updated title and ticket price after saving.
- [ ] FT-03: Organizer can see the list of ticket reservations
  - Action: Open the reservations list for an event that has reservations.
  - Expected: A list displays reservation entries including the event name, ticket type, quantity, and customer details.
- [ ] FT-04: Visitor can browse all upcoming events
  - Action: Open the events browsing page as a visitor.
  - Expected: All upcoming events are listed, each showing title, category, date, and location.
- [ ] FT-05: Visitor can filter events by category
  - Action: Select the "concert" category filter on the events list.
  - Expected: Only events with category "concert" remain in the list.
- [ ] FT-06: Visitor can filter events by date
  - Action: Apply a date filter (e.g., a specific date or date range) on the events list.
  - Expected: Only events occurring within the selected date criteria are shown.
- [ ] FT-07: Visitor can search events by keyword
  - Action: Enter a keyword matching an event title (e.g., part of a known event title) in the search box and submit.
  - Expected: The results list shows only events whose text matches the keyword.
- [ ] FT-08: Visitor can open an event detail page
  - Action: Click on an event from the browse list.
  - Expected: A detail page opens showing the event's title, category, date, location, description, and available ticket types with prices and remaining quantities.
- [ ] FT-09: Visitor can select ticket quantities for multiple ticket types
  - Action: On an event detail page, set quantities for two different ticket types.
  - Expected: The selected quantities are reflected and the total price updates accordingly.
- [ ] FT-10: Visitor can complete checkout to reserve tickets
  - Action: Proceed to checkout with selected tickets, fill in the checkout form (name, email, etc.), and submit.
  - Expected: The reservation is created, an order summary/confirmation is displayed, and the reservation appears in the organizer's reservations list.
- [ ] FT-11: Ticket quantity stock is consumed after reservation
  - Action: Note an event's ticket quantity, reserve some tickets, then view the event detail page again.
  - Expected: The remaining ticket quantity is reduced by the reserved amount.

## Constraint
- [ ] CS-01: Event creation requires all mandatory fields
  - Action: Attempt to create an event leaving the title (or category, date, location) empty.
  - Expected: The event is not created and an error message identifies the missing required field.
- [ ] CS-02: Ticket types require valid price and quantity values
  - Action: Attempt to save a ticket type with an empty, negative, or non-numeric price or quantity.
  - Expected: The ticket type is rejected with a validation error; no invalid price/quantity is saved.
- [ ] CS-03: Cannot reserve more tickets than available quantity
  - Action: On an event detail page, enter a quantity greater than the remaining stock for a ticket type and attempt to checkout.
  - Expected: Checkout is blocked with an error message stating insufficient availability.
- [ ] CS-04: Cannot submit checkout with an incomplete form
  - Action: Attempt to submit the checkout form with required fields (e.g., name, email) left empty or with an invalid email format.
  - Expected: The reservation is not created and validation errors are shown on the offending fields.
- [ ] CS-05: Zero ticket quantity cannot be reserved
  - Action: Proceed to checkout with all ticket quantities set to 0 (or none selected).
  - Expected: Checkout is not allowed and a message indicates at least one ticket must be selected.

## Interaction
- [ ] IX-01: Applying a filter or search updates the event list immediately
  - Action: Change the category filter or enter a search keyword and submit.
  - Expected: The event list refreshes to show matching events without a full page reload failure, and the active filter/search state is visibly indicated.
- [ ] IX-02: Checkout total updates when ticket quantities change
  - Action: Change a ticket quantity on the event detail or checkout page.
  - Expected: The displayed order total recalculates immediately to reflect the new quantities.
- [ ] IX-03: Successful reservation shows a confirmation
  - Action: Complete a valid checkout submission.
  - Expected: A clear confirmation message or page is displayed showing the reserved event, ticket types, quantities, and total.
- [ ] IX-04: Navigating from browse list to detail and back preserves browsing context
  - Action: Apply a category filter, open an event detail page, then return to the list.
  - Expected: The user returns to the event list with the previously applied filter still active.

## Content
- [ ] CT-01: Event detail page content matches the event's entered data
  - Action: Open the detail page of a known event.
  - Expected: Title, category, date, location text, and every ticket type's name, price, and quantity exactly match what the organizer entered.
- [ ] CT-02: Category values are limited to the three defined types
  - Action: Review the category options when creating an event and the category labels shown on event listings.
  - Expected: Only "concert", "conference", and "workshop" appear as categories, with each event displaying exactly one of them.
- [ ] CT-03: Reservation list shows accurate reservation details
  - Action: Open the organizer's reservation list after a checkout was completed.
  - Expected: The entry shows the correct event title, ticket type, quantity, and customer information matching the submitted checkout data.