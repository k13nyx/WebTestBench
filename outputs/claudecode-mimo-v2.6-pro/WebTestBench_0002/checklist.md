# Test Checklist

## Functionality
- [ ] FT-01: Organizer can create a new event listing with all required details.
  - Action: As an organizer, open the create-event form, fill in a title, select a category, pick a future date, enter a location text, and add a ticket type with a name, price, and quantity; submit the form.
  - Expected: The event is saved successfully and the form completes without errors.
- [ ] FT-02: A newly created event appears in the upcoming events listing.
  - Action: After creating the event in FT-01, navigate to the upcoming events browse page.
  - Expected: The newly created event appears in the list alongside the default events.
- [ ] FT-03: Visitor can browse all upcoming events.
  - Action: Open the upcoming events page as a visitor (no filters applied).
  - Expected: All upcoming events (default data included) are listed.
- [ ] FT-04: Visitor can filter events by category.
  - Action: Select the category filter "concert" on the events page.
  - Expected: Only events with category "concert" are shown; switching to "conference" or "workshop" shows only events of that category.
- [ ] FT-05: Visitor can filter events by date.
  - Action: Set the date filter to the date of a known default event.
  - Expected: Only events on the selected date are shown in the list.
- [ ] FT-06: Visitor can search events by keywords.
  - Action: Type a word from an existing event's title into the search field and submit.
  - Expected: The events list shows only events whose title contains that keyword.
- [ ] FT-07: Visitor can open an event's detailed page from the listing.
  - Action: Click on an event card/entry in the upcoming events list.
  - Expected: The detailed page for that event opens, showing its full details and ticket selection.
- [ ] F​T-08: Visitor can select ticket quantities on the event detail page.
  - Action: On an event detail page, set a quantity (e.g., 2) for one of the ticket types using the quantity selector.
  - Expected: The selector accepts the value and the chosen quantity is reflected in the checkout summary.
- [ ] FT-09: Visitor can reserve tickets via the checkout form.
  - Action: Select ticket quantities, fill in the checkout form (name, email), and submit it.
  - Expected: The reservation is created successfully and a confirmation of the reservation is shown.
- [ ] FT-10: Organizer can view and update an existing event.
  - Action: Open the organizer's events list, select an existing event, edit its title/location, and save the changes.
  - Expected: The update is saved, and reopening the event shows the changed values.
- [ ] FT-11: Organizer can view a list of ticket reservations.
  - Action: Navigate to the organizer's reservations view after a reservation has been made (FT-09).
  - Expected: A list of ticket reservations is displayed and includes the newly made reservation.

## Constraint
- [ ] CS-01: Event creation is blocked when required fields are missing.
  - Action: Submit the create-event form with an empty title, or empty date/location, or a ticket type missing its name, price, or quantity.
  - Expected: The event is not saved and a validation error identifies the missing required field(s).
- [ ] CS-02: Event category is restricted to the allowed values.
  - Action: Inspect the category field on the create/edit event form and attempt to save with no category or a value other than "concert", "conference", or "workshop".
  - Expected: Only "concert", "conference", and "workshop" are selectable/savable; saving with an empty or other category is rejected with a validation error.
- [ ] CS-03: Ticket reservations cannot exceed the available quantity.
  - Action: On an event detail page, attempt to reserve more tickets of a ticket type than its stated quantity.
  - Expected: The reservation is rejected with a validation error indicating insufficient ticket quantity; no reservation is created.
- [ ] CS-04: Checkout form cannot be submitted with empty required fields.
  - Action: Select ticket quantities, leave the checkout form's name and email empty, and submit.
  - Expected: Submission is blocked with validation errors on the empty fields; no reservation is created.
- [ ] CS-05: Ticket price and quantity must be valid positive numbers.
  - Action: When creating an event, enter a negative or non-numeric value (e.g., "abc") for a ticket type's price or quantity and submit.
  - Expected: The event is not saved and a validation error indicates an invalid price or quantity.

## Interaction
- [ ] IX-01: System provides success feedback after creating or updating an event.
  - Action: Successfully create an event (FT-01), then successfully update an event (FT-10), observing the interface after each save.
  - Expected: A visible success confirmation is displayed after each save (creation and update).
- [ ] IX-02: System provides confirmation feedback after a ticket reservation.
  - Action: Complete a checkout form submission that creates a reservation (FT-09) and observe the interface response.
  - Expected: A visible confirmation is displayed indicating the reservation was completed successfully.

## Content
- [ ] CT-01: Event detail page displays the event's data exactly as entered.
  - Action: Open the detail page of an event created in FT-01 and compare every field against what was entered.
  - Expected: Title, category, date, location, and each ticket type's name, price, and quantity are displayed exactly as entered, with no missing or altered values.
- [ ] CT-02: Reservations list shows accurate reservation data.
  - Action: In the organizer's reservations list (FT-11), compare each reservation row against a completed checkout.
  - Expected: Each reservation shows the correct event, ticket type, quantity reserved, and the name/email supplied at checkout.