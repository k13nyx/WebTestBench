# Test Checklist

## Functionality
- [ ] FT-01: Browse upcoming events
  - Action: Navigate to the events home/listing page.
  - Expected: A list of all upcoming events is displayed showing title, date, location, and category.
- [ ] FT-02: Filter events by category
  - Action: Select a category option (e.g., "Concert", "Conference", or "Workshop") from the category filter.
  - Expected: The list updates to display only events that belong to the chosen category.
- [ ] FT-03: Filter events by date
  - Action: Select a target date or date range in the date filter control.
  - Expected: The list refreshes to display only events scheduled on or within the selected date range.
- [ ] FT-04: Search events by keyword
  - Action: Enter a search term into the keyword search input and submit.
  - Expected: The listing updates to show only events containing the keyword in their title or details.
- [ ] FT-05: View event detailed page
  - Action: Click on an event card or title from the events list.
  - Expected: The event detail page loads, displaying full event information and available ticket types.
- [ ] FT-06: Reserve tickets via checkout form
  - Action: Select ticket quantities on the event detail page, fill in the checkout form details, and click "Reserve".
  - Expected: The reservation is completed and a booking confirmation is displayed.
- [ ] FT-07: Create a new event listing
  - Action: Fill out the event creation form with title, category, date, location text, ticket types (price and quantity), and click "Save Event".
  - Expected: The new event is saved and appears in the organizer's event management list.
- [ ] FT-08: Update an existing event listing
  - Action: Open an existing event in the organizer edit view, modify the location text or title, and click "Update Event".
  - Expected: The changes are saved and reflected accurately on the event detail page and organizer list.
- [ ] FT-09: View ticket reservations list as organizer
  - Action: Navigate to the organizer dashboard and click "View Reservations" for an existing event.
  - Expected: A list of customer reservations for that event is displayed showing attendee details and reserved ticket quantities.

## Constraint
- [ ] CS-01: Block event creation with missing required fields
  - Action: Leave required fields (e.g., title, date, location) empty in the event creation form and click "Save Event".
  - Expected: The form is not submitted, and validation error messages appear under the empty required fields.
- [ ] CS-02: Prevent reserving ticket quantities exceeding available stock
  - Action: Attempt to select or enter a ticket quantity greater than the remaining available tickets for an event.
  - Expected: The input is capped at the maximum remaining tickets or an error message prevents proceeding to checkout.
- [ ] CS-03: Prevent checkout with empty required attendee fields
  - Action: Leave required attendee fields (e.g., name, email) blank in the checkout form and click "Reserve".
  - Expected: The reservation is rejected and visual error indicators highlight the missing required inputs.
- [ ] CS-04: Disallow negative ticket prices or quantities
  - Action: Enter negative numbers in the ticket price or quantity fields during event creation and attempt to save.
  - Expected: Form submission is blocked with validation warnings stating values must be non-negative.

## Interaction
- [ ] IX-01: Dynamic total cost recalculation during ticket selection
  - Action: Increment or decrement the ticket quantity selector on the event detail/checkout screen.
  - Expected: The displayed total price updates immediately to reflect the unit price multiplied by the selected quantity.
- [ ] IX-02: Success feedback on reservation submission
  - Action: Submit a valid reservation through the checkout form.
  - Expected: A success confirmation toast or banner appears confirming the reservation has been recorded.
- [ ] IX-03: Reset event filters and search
  - Action: Apply a category filter and keyword search, then click the "Reset" or "Clear Filters" button.
  - Expected: All filter and search inputs clear, and the event list immediately reloads to show all upcoming events.

## Content
- [ ] CT-01: Event detail page information completeness
  - Action: Open the detail page of an existing event.
  - Expected: Title, category, date, location text, and ticket types with corresponding prices and available quantities are clearly visible.
- [ ] CT-02: Category options match defined event types
  - Action: Inspect the category selection options in the event creation form and filter dropdown.
  - Expected: Options include "Concert", "Conference", and "Workshop".
- [ ] CT-03: Reservation list record details
  - Action: Inspect an entry in the organizer's reservation list.
  - Expected: The entry displays the attendee's contact info, reserved ticket type, ticket quantity, and booking timestamp.