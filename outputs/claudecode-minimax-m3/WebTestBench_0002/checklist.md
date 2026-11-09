# Test Checklist

## Functionality
- [ ] FT-01: Organizer creates a new event listing with all required fields
  - Action: As organizer, fill in title, category (concert/conference/workshop), date, location text, and at least one ticket type (price and quantity), then submit.
  - Expected: Event is saved and appears in the organizer's event list.
- [ ] FT-02: Organizer updates an existing event listing
  - Action: As organizer, open an existing event and modify its title, date, location, or ticket details, then save.
  - Expected: Updated values are reflected on the event listing and detail page.
- [ ] FT-03: Organizer views ticket reservations for their event
  - Action: As organizer, open the reservations view for one of their events after a visitor completes a checkout.
  - Expected: Reservation entry shows buyer details, selected ticket type, quantity, and total.
- [ ] FT-04: Visitor browses all upcoming events
  - Action: Open the public events listing page with no filter applied.
  - Expected: Only upcoming events (today or later) are listed with their title, category, date, and location.
- [ ] FT-05: Visitor filters events by category
  - Action: Select category "Concert" in the category filter.
  - Expected: Only events with category = Concert are displayed; other categories are excluded.
- [ ] FT-06: Visitor filters events by date
  - Action: Select or enter a specific date/date range in the date filter.
  - Expected: Only events whose date falls within the selected range are displayed.
- [ ] FT-07: Visitor searches events by keyword
  - Action: Enter a keyword (e.g., a word from an event title or location) into the search box.
  - Expected: Only events whose title or location text contains the keyword are displayed.
- [ ] FT-08: Visitor opens an event detail page
  - Action: Click on an event from the listing.
  - Expected: Detail page opens showing full event information and available ticket types with prices and remaining quantities.
- [ ] FT-09: Visitor selects ticket quantity on the event detail page
  - Action: Choose a ticket type and enter a quantity greater than 0.
  - Expected: Selected ticket type and quantity are captured and the "Checkout" / "Reserve" action becomes available.
- [ ] FT-10: Visitor completes the checkout form to reserve tickets
  - Action: Fill in the checkout form (name, email, and any required buyer fields) and submit.
  - Expected: Reservation is recorded, the ticket quantity is decremented, and the reservation appears in the organizer's reservations list.

## Constraint
- [ ] CS-01: Event cannot be created without required fields
  - Action: Attempt to submit an event form with one or more required fields (title, category, date, location) left empty.
  - Expected: Submission is blocked and an error/inline validation message identifies the missing field(s).
- [ ] CS-02: Cannot reserve more tickets than available quantity
  - Action: On an event detail page, enter a ticket quantity greater than the available quantity for that ticket type and attempt checkout.
  - Expected: Submission is blocked with an error stating the requested quantity exceeds availability.
- [ ] CS-03: Cannot submit checkout with missing or invalid required fields
  - Action: Submit the checkout form with empty required buyer fields (e.g., name or email) or an invalid email format.
  - Expected: Submission is blocked and the invalid/missing fields are flagged.
- [ ] CS-04: Past events are excluded from browse, filter, and search results
  - Action: With at least one past-dated event present in default data, browse the listing, apply each filter, and run a search matching the past event's title.
  - Expected: The past event does not appear in any of the browsed, filtered, or searched result lists.

## Interaction
- [ ] IX-01: Success confirmation is shown after creating an event
  - Action: Create a new event as organizer.
  - Expected: A success message or visible confirmation (e.g., "Event created") appears, and the new event is visible in the organizer's event list.
- [ ] IX-02: Success confirmation is shown after a ticket reservation
  - Action: Complete a ticket checkout as a visitor.
  - Expected: A success/confirmation message or confirmation page is displayed acknowledging the reservation with reservation details.
- [ ] IX-03: Updated event data is reflected immediately on the public listing
  - Action: As organizer, edit an event's title and/or date and save; then as visitor reload the public listing.
  - Expected: The listing reflects the new title/date without requiring a stale cache or error.

## Content
- [ ] CT-01: Event detail page shows all required information
  - Action: Open any event detail page.
  - Expected: Page displays the event title, category, date, location text, ticket type names, prices, and available quantities — all relevant to the event.
- [ ] CT-02: All three event categories are available in the category selector
  - Action: Open the event creation form (or category filter).
  - Expected: The options "Concert", "Conference", and "Workshop" are all present and selectable.