# Test Checklist

## Functionality

- [ ] FT-01: Organizer can create a new event listing
  - Action: On the organizer's event creation form, fill in title, category, date, location text, and one ticket type (name, price, quantity), then click the "Create Event" button.
  - Expected: The event is created and appears in the organizer's event list with all entered details.

- [ ] FT-02: Visitor can browse all upcoming events
  - Action: Open the public events listing page.
  - Expected: All upcoming default events are displayed, each showing at minimum the event title, category, date, and location.

- [ ] FT-03: Visitor can filter events by category
  - Action: On the events page, select a category filter (e.g., "Concert").
  - Expected: Only default events in the selected category are shown; events in other categories are hidden.

- [ ] FT-04: Visitor can filter events by date
  - Action: Apply the date filter for a specific date (or date range) that matches a default event.
  - Expected: Only events on the selected date (or within the range) are shown; all other events are hidden.

- [ ] FT-05: Visitor can search events by keyword
  - Action: Type a keyword from a default event's title or location into the search field and submit.
  - Expected: Only events containing the keyword are shown; non-matching events are hidden.

- [ ] FT-06: Visitor can open an event detail page
  - Action: Click a default event in the events list.
  - Expected: A detail page opens showing that event's title, category, date, location text, and its ticket types with prices and quantities.

- [ ] FT-07: Visitor can select ticket quantities on the event detail page
  - Action: On a default event's detail page, set the quantity of an available ticket type (e.g., 2 tickets).
  - Expected: The selected quantity is applied and reflected in the ticket selection area before checkout.

- [ ] FT-08: Visitor can reserve tickets through the checkout form
  - Action: With ticket quantities selected, fill in the checkout form (e.g., name and email) and submit it.
  - Expected: Checkout completes successfully and a reservation is recorded for that event.

- [ ] FT-09: Organizer can view their existing events
  - Action: Open the organizer's event management view ("My Events" or equivalent).
  - Expected: The organizer's events are listed with identifying details such as title, category, and date.

- [ ] FT-10: Organizer can update an existing event
  - Action: Open one of the organizer's events, change one or more fields (e.g., title and date), and save.
  - Expected: The changes persist — updated values are shown in the organizer's event list and on the event detail page.

- [ ] FT-11: Organizer can view a list of ticket reservations
  - Action: Open the organizer's reservations view.
  - Expected: A list of reservations is displayed, each showing the event, ticket quantity, and attendee information.

## Constraint

- [ ] CS-01: Event cannot be created with empty required fields
  - Action: On the event creation form, leave required fields (title, date) empty and click "Create Event".
  - Expected: The event is not created; validation messages indicate which required fields are missing.

- [ ] CS-02: Event category is restricted to the defined types
  - Action: Open the category selector on the event creation form and inspect the available options.
  - Expected: Only Concert, Conference, and Workshop can be selected; no free-text or undefined categories are accepted.

- [ ] CS-03: Ticket quantity cannot exceed the available amount
  - Action: On a default event's detail page, attempt to select a quantity greater than a ticket type's available quantity.
  - Expected: The excess quantity is rejected (input capped or error shown); the reservation cannot proceed with the invalid quantity.

- [ ] CS-04: Checkout cannot be submitted with empty required fields
  - Action: On the checkout form, leave required fields (e.g., name, email) empty and submit.
  - Expected: No reservation is created; required-field errors are displayed.

## Interaction

- [ ] IX-01: Success feedback after event creation
  - Action: Complete and submit the event creation form with valid data.
  - Expected: A success message or notification appears confirming the event was created.

- [ ] IX-02: Confirmation shown after checkout
  - Action: Submit the checkout form with valid data and selected ticket quantities.
  - Expected: A confirmation message or screen is displayed summarizing the reserved event and tickets.

- [ ] IX-03: Total price updates when ticket quantities change
  - Action: On the event detail page, increase or decrease the quantity of a ticket type.
  - Expected: The displayed total price recalculates immediately to match quantity × unit price.

## Content

- [ ] CT-01: Event list displays accurate event information
  - Action: Compare each default event entry on the events page with its data on the detail page.
  - Expected: Title, category, date, and location text on every list entry match the event's actual data, with no missing or mislabeled fields.

- [ ] CT-02: Ticket types on the detail page match the event's data
  - Action: Open a default event's detail page and inspect its ticket types.
  - Expected: Each ticket type shows the correct name, price, and quantity/availability consistent with the event's defined tickets.