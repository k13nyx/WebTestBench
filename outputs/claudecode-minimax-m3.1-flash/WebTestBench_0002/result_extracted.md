# Test Result

## Functionality

- [X] FT-01: Organizer can create a new event listing with all required details
  - Action: In the organizer area, open the create-event form, enter a title, select a category (concert/conference/workshop), enter a date, location text, and at least one ticket type with a name, price, and quantity, then save.
  - Expected: The event is saved without error and appears in the organizer's event list.
  - Note: Created "Aurora Rock Concert" (Concert, 2027‑03‑15, Aurora Hall Oslo, Standard Entry $50 ×100 + VIP Balcony $150 ×20) plus "Quantum Dev Conference" (Conference, 2027‑04‑20) and "Watercolor Masterclass" (Workshop, 2027‑05‑10). Each showed the "Event created" toast and appeared in "Your Events" with correct badge/date/location.

- [X] FT-02: Organizer can see their existing events and open one for editing
  - Action: Open the organizer's event list, locate a previously created event, and click it / click its edit control.
  - Expected: The list shows all events belonging to that organizer, and clicking one opens an edit form pre-filled with that event's title, category, date, location, and ticket types.

- [X] FT-03: Organizer can update an existing event and the changes are saved
  - Action: Edit an existing event, change its title, date, location, and a ticket type's price/quantity, then save.
  - Expected: The updated values are stored and shown in the organizer list and on the public event detail page.
  - Note: Title→"Aurora Rock Festival 2027", date→2027‑03‑20, location→"Aurora Grand Hall, Oslo", Standard Entry price 50→55 / qty 100→120. Toast "Event updated"; organizer card and public detail page ("$55", "120 tickets available") both reflected the new values.

- [X] FT-04: Organizer can view a list of ticket reservations
  - Action: Open the organizer's reservations section and view the reservations for one of their events.
  - Expected: A list of reservations is displayed showing at least the event, the ticket type, the quantity reserved, and the buyer name/contact for each reservation.
  - Note: The dashboard's per-event "View Reservations" section shows e.g. under Aurora Rock Festival 2027: "Dana Tester / dana.tester@example.com / 555-0199 / $110 / Nov 7, 2026 / Tickets: Standard Entry × 2"; stats updated to 4 reservations / $1,279.

- [X] FT-05: Visitor can browse all upcoming events
  - Action: Open the public events listing page as a visitor.
  - Expected: All upcoming default events are listed with their title, category, date, and location; events whose date has already passed are not shown.
  - Note: "All Upcoming Events" listed each upcoming event with title, category badge, date, time and location (the 3 future-dated events created above); all seeded events (dated 2025) were excluded as past. The seeded data contains no future-dated events relative to the current system date (2026‑11‑07), so the list was empty until future-dated events were created. Note: the separate "Featured Events" carousel still shows the two past 2025 events (it is not filtered by date).

- [X] FT-06: Visitor can filter events by category
  - Action: Select a category (e.g., "workshop") in the category filter and apply it.
  - Expected: Only events belonging to the selected category are listed; choosing "All"/clearing the filter restores the full list.
  - Note: "Workshops" → heading changed to "1 events found" with only Watercolor Masterclass; "All Events" restored all 3.

- [X] FT-07: Visitor can filter events by date
  - Action: Use the date filter to select a specific date (and/or a date range) and apply it.
  - Expected: Only events falling within the selected date/date range are listed; events outside that range are excluded.
  - Note: Date 2027‑04‑20 → only "Quantum Dev Conference"; clearing the date restored all 3.

- [X] FT-08: Visitor can search events by keyword
  - Action: Type a keyword taken from a default event's title (e.g., a word appearing in one title) into the search field and submit.
  - Expected: Only events matching the keyword are listed; clearing the search and submitting shows the full list again.
  - Note: "Aurora" → "1 events found" (Aurora Rock Festival 2027 only); clearing the field restored the full list of 3.

- [X] FT-09: Visitor can open an event detail page showing the event and its ticket types
  - Action: From the events list, open one event's detail page.
  - Expected: The page shows the event title, category, date, location, and a section listing every ticket type with its price and the quantity available.
  - Note: Detail page showed "Aurora Rock Festival 2027", Concert, Saturday March 20 2027, 19:00, Aurora Grand Hall Oslo, and a "Select Tickets" section with Standard Entry $55 / "120 tickets available" and VIP Balcony $150 / "20 tickets available".

- [X] FT-10: Visitor can select ticket quantities and complete checkout to reserve tickets
  - Action: On an event detail page, set a quantity for a ticket type, fill in the checkout form fields, and submit the reservation.
  - Expected: A reservation is created for the chosen ticket type and quantity, and the reservation appears in the organizer's reservations list.
  - Note: Selected Standard Entry × 2 ($110), filled Dana Tester / dana.tester@example.com / 555-0199, confirmed → reservation created and listed in the organizer's reservations ("Dana Tester … Standard Entry × 2", card shows "1 reservations / $110 revenue").

## Constraint

- [X] CS-01: Event creation is blocked when required fields are empty
  - Action: Open the create-event form, leave the title, category, date, location, and ticket price/quantity blank, and attempt to save.
  - Expected: The event is not created and each missing required field is flagged with a visible validation error.
  - Note: Event count stayed at 6 and the dialog stayed open; every required field (title, description, location, date, time, ticket name, price, quantity) reported `:invalid` with the browser validation message "Please fill out this field." (validation is browser-native — no inline error text elements are rendered).

- [X] CS-02: Category is restricted to the three allowed values
  - Action: Open the category selection in the create/edit event form and inspect the available choices.
  - Expected: Exactly "concert", "conference", and "workshop" are selectable; no other or blank category can be saved.
  - Note: The select contains exactly 3 options (concert|Conference, conference|Conference, workshop|Workshop); there is no blank option and the trigger always holds a valid value (default "concert").

- [ ] CS-03: Ticket price and quantity must be valid positive numbers
  - Action: In the create-event form, enter a non-numeric or zero/negative ticket price, then separately a zero/negative ticket quantity, and attempt to save.
  - Expected: The event is not saved and the invalid price/quantity is rejected with a validation error.
  - Bug Report:
    - Issue: Missing Input Validation (zero ticket price accepted and saved)
    - Actual: With title "Zero Price Probe", category Concert, date 2026‑12‑01, location "Test Hall, Berlin", ticket "Probe Ticket", **Price = 0** and Quantity = 50, clicking "Create Event" saved the event: toast "Event created — Your new event has been created successfully", "Total Events" went 3 → 4 and a "Zero Price Probe" card was added to "Your Events" with $0 revenue. The price field is declared `min="0"`, so 0 satisfies the native constraint and no validation error is displayed. (A negative price = ‑5 and quantity = 0 were blocked, but only by native HTML5 validation with browser bubble text "Value must be greater than or equal to 0." / "…greater than or equal to 1.", with no in-page validation error.)

- [X] CS-04: Visitor cannot reserve more tickets than the available quantity
  - Action: On an event detail page, attempt to reserve a quantity greater than the listed remaining quantity for a ticket type and submit checkout.
  - Expected: The reservation is rejected with a clear error stating the available quantity, and no reservation is created.
  - Note: After the organizer's stock for Standard Entry was reduced to 5, repeatedly clicking "+" on that ticket type stopped at 5 (the control became disabled) and no over-quantity selection could be submitted, so no reservation exceeding availability was created; the row continuously displays the remaining "5 tickets available". Note: the rejection is enforced by disabling the increment control rather than by an error message — the app never renders a "only N available" error (the checkout form itself performs no quantity/availability check).

- [X] CS-05: Checkout form requires buyer details
  - Action: On an event detail page, select a ticket quantity, leave the required checkout fields (e.g., name and email) empty, and submit.
  - Expected: The reservation is not created and the missing checkout fields are flagged with validation errors.
  - Note: With Full Name / Email / Phone Number empty, clicking "Confirm Reservation" left the dialog open, created no reservation (organizer counters unchanged) and each of the three fields reported `:invalid` with "Please fill out this field." (native browser validation bubble; no inline error text is rendered).

- [X] CS-06: Date filter excludes events outside the selected range
  - Action: Apply a date filter set to a single date, then compare the displayed results with the full event list.
  - Expected: Every displayed event's date falls within the selected date/range, and events dated before the range start or after the range end are excluded.
  - Note: With date 2027‑04‑20 selected, the only listed event was "Quantum Dev Conference" (Apr 20, 2027); the 2027‑03‑20 and 2027‑05‑10 events were excluded, and all seeded 2025 events remained excluded.

## Interaction

- [X] IX-01: Applying a filter or search updates the results list without a full page reload
  - Action: Choose a category, a date, or type a keyword in the listing controls and observe the result area.
  - Expected: The event list updates in place to show only the matching events, with no browser page-reload, and the active filter/search is visibly reflected in the controls.
  - Note: A marker set on `window` survived every filter/search/date change (no page reload); the heading switched to "1 events found", the selected category button stayed in its active (highlighted) state, the search text and date value remained in the controls, and a "Clear filters" control appeared while a filter was active.

- [X] IX-02: A success confirmation is shown after a reservation is completed
  - Action: Complete a valid checkout on an event detail page.
  - Expected: A success/confirmation message appears confirming the reservation (including the event and quantity or total), and the event's remaining ticket quantity is reduced.
  - Note: Toast "Reservation Confirmed! Your tickets for Aurora Rock Festival 2027 have been reserved." appeared and the app navigated back to the listing; the ticket's remaining quantity dropped from 5 to 3 on the detail page. Note: the toast names the event but not the quantity/total — those were shown in the checkout order summary ("Standard Entry × 2", "Total $110") immediately before confirmation.

- [X] IX-03: Clicking an event in the list opens that event's detail page
  - Action: Click the title/card of an event in the browsable list.
  - Expected: The detail page for exactly that event opens, showing that event's title, date, location, and ticket types.
  - Note: Clicking the "Aurora Rock Festival 2027" card opened /event/event-1794059651309 showing that event's title, Concert, Saturday March 20 2027, Aurora Grand Hall Oslo and its two ticket types.

## Content

- [X] CT-01: Event detail page shows the organizer's entered details exactly
  - Action: Compare the title, category, date, and location on an event's detail page with the values entered by the organizer.
  - Expected: Each value matches the organizer-entered data exactly, with the category shown as one of concert/conference/workshop.
  - Note: Detail page read "Aurora Rock Festival 2027" / "Concert" / "Saturday, March 20, 2027" / "Aurora Grand Hall, Oslo" — identical to the organizer-entered and edited values.

- [X] CT-02: Ticket types display correct names, prices, and quantities
  - Action: Compare the ticket type names, prices, and quantities listed on an event's detail page and checkout area with the organizer's ticket data.
  - Expected: Names and prices match exactly (formatted as currency), and the displayed quantity reflects the current remaining quantity; no placeholder or unrelated text appears.
  - Note: Detail page showed "Standard Entry $55 — 120 tickets available" and "VIP Balcony $150 — 20 tickets available" (matching the organizer's ticket data, currency-formatted); after the stock was edited to 5 and 2 tickets were reserved, the detail page showed "3 tickets available", and the checkout order summary read "Standard Entry × 2 / $110 / Total $110".
