# Test Checklist

## Functionality

- [ ] FT-01: Organizer can create a new event listing with all required details
  - Action: In the organizer area, open the create-event form, enter a title, select a category (concert/conference/workshop), enter a date, location text, and at least one ticket type with a name, price, and quantity, then save.
  - Expected: The event is saved without error and appears in the organizer's event list.

- [ ] FT-02: Organizer can see their existing events and open one for editing
  - Action: Open the organizer's event list, locate a previously created event, and click it / click its edit control.
  - Expected: The list shows all events belonging to that organizer, and clicking one opens an edit form pre-filled with that event's title, category, date, location, and ticket types.

- [ ] FT-03: Organizer can update an existing event and the changes are saved
  - Action: Edit an existing event, change its title, date, location, and a ticket type's price/quantity, then save.
  - Expected: The updated values are stored and shown in the organizer list and on the public event detail page.

- [ ] FT-04: Organizer can view a list of ticket reservations
  - Action: Open the organizer's reservations section and view the reservations for one of their events.
  - Expected: A list of reservations is displayed showing at least the event, the ticket type, the quantity reserved, and the buyer name/contact for each reservation.

- [ ] FT-05: Visitor can browse all upcoming events
  - Action: Open the public events listing page as a visitor.
  - Expected: All upcoming default events are listed with their title, category, date, and location; events whose date has already passed are not shown.

- [ ] FT-06: Visitor can filter events by category
  - Action: Select a category (e.g., "workshop") in the category filter and apply it.
  - Expected: Only events belonging to the selected category are listed; choosing "All"/clearing the filter restores the full list.

- [ ] FT-07: Visitor can filter events by date
  - Action: Use the date filter to select a specific date (and/or a date range) and apply it.
  - Expected: Only events falling within the selected date/date range are listed; events outside that range are excluded.

- [ ] FT-08: Visitor can search events by keyword
  - Action: Type a keyword taken from a default event's title (e.g., a word appearing in one title) into the search field and submit.
  - Expected: Only events matching the keyword are listed; clearing the search and submitting shows the full list again.

- [ ] FT-09: Visitor can open an event detail page showing the event and its ticket types
  - Action: From the events list, open one event's detail page.
  - Expected: The page shows the event title, category, date, location, and a section listing every ticket type with its price and the quantity available.

- [ ] FT-10: Visitor can select ticket quantities and complete checkout to reserve tickets
  - Action: On an event detail page, set a quantity for a ticket type, fill in the checkout form fields, and submit the reservation.
  - Expected: A reservation is created for the chosen ticket type and quantity, and the reservation appears in the organizer's reservations list.

## Constraint

- [ ] CS-01: Event creation is blocked when required fields are empty
  - Action: Open the create-event form, leave the title, category, date, location, and ticket price/quantity blank, and attempt to save.
  - Expected: The event is not created and each missing required field is flagged with a visible validation error.

- [ ] CS-02: Category is restricted to the three allowed values
  - Action: Open the category selection in the create/edit event form and inspect the available choices.
  - Expected: Exactly "concert", "conference", and "workshop" are selectable; no other or blank category can be saved.

- [ ] CS-03: Ticket price and quantity must be valid positive numbers
  - Action: In the create-event form, enter a non-numeric or zero/negative ticket price, then separately a zero/negative ticket quantity, and attempt to save.
  - Expected: The event is not saved and the invalid price/quantity is rejected with a validation error.

- [ ] CS-04: Visitor cannot reserve more tickets than the available quantity
  - Action: On an event detail page, attempt to reserve a quantity greater than the listed remaining quantity for a ticket type and submit checkout.
  - Expected: The reservation is rejected with a clear error stating the available quantity, and no reservation is created.

- [ ] CS-05: Checkout form requires buyer details
  - Action: On an event detail page, select a ticket quantity, leave the required checkout fields (e.g., name and email) empty, and submit.
  - Expected: The reservation is not created and the missing checkout fields are flagged with validation errors.

- [ ] CS-06: Date filter excludes events outside the selected range
  - Action: Apply a date filter set to a single date, then compare the displayed results with the full event list.
  - Expected: Every displayed event's date falls within the selected date/range, and events dated before the range start or after the range end are excluded.

## Interaction

- [ ] IX-01: Applying a filter or search updates the results list without a full page reload
  - Action: Choose a category, a date, or type a keyword in the listing controls and observe the result area.
  - Expected: The event list updates in place to show only the matching events, with no browser page-reload, and the active filter/search is visibly reflected in the controls.

- [ ] IX-02: A success confirmation is shown after a reservation is completed
  - Action: Complete a valid checkout on an event detail page.
  - Expected: A success/confirmation message appears confirming the reservation (including the event and quantity or total), and the event's remaining ticket quantity is reduced.

- [ ] IX-03: Clicking an event in the list opens that event's detail page
  - Action: Click the title/card of an event in the browsable list.
  - Expected: The detail page for exactly that event opens, showing that event's title, date, location, and ticket types.

## Content

- [ ] CT-01: Event detail page shows the organizer's entered details exactly
  - Action: Compare the title, category, date, and location on an event's detail page with the values entered by the organizer.
  - Expected: Each value matches the organizer-entered data exactly, with the category shown as one of concert/conference/workshop.

- [ ] CT-02: Ticket types display correct names, prices, and quantities
  - Action: Compare the ticket type names, prices, and quantities listed on an event's detail page and checkout area with the organizer's ticket data.
  - Expected: Names and prices match exactly (formatted as currency), and the displayed quantity reflects the current remaining quantity; no placeholder or unrelated text appears.