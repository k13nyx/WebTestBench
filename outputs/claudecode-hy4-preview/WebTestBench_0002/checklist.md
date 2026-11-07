# Test Checklist

## Functionality

- [ ] FT-01: Organizer can create a new event with title, category, date, and location
  - Action: Open the "Create Event" form; fill Title, select Category (Concert/Conference/Workshop), pick a future Date, enter Location text; submit.
  - Expected: Event is saved and appears in the browse/events list and in the organizer's own events list with the exact values entered.

- [ ] FT-02: Organizer can define multiple ticket types with prices and quantities when creating an event
  - Action: In the Create Event form, add at least two ticket types (e.g., "General $50 qty 100", "VIP $120 qty 20"); submit.
  - Expected: Event is created and both ticket types are stored with their exact names, prices, and quantities.

- [ ] FT-03: Organizer can see a list of their existing events
  - Action: Navigate to the organizer's events management page (e.g., "My Events").
  - Expected: All previously created events are listed, each showing title, category, date, and location.

- [ ] FT-04: Organizer can update an existing event
  - Action: From the organizer's events list, open one event for editing; change its Title and Date; save.
  - Expected: Saved changes are reflected in the organizer's list and on the public browse list / event detail page.

- [ ] FT-05: Visitor can browse all upcoming events
  - Action: Open the public events browse page as a visitor.
  - Expected: A list/grid of upcoming events is displayed; each entry shows title, category, date, and location.

- [ ] FT-06: Visitor can view an event's detail page
  - Action: Click any event from the browse list.
  - Expected: Detail page opens showing that event's title, category, date, location, and every ticket type with its price and available quantity.

- [ ] FT-07: Visitor can filter events by category
  - Action: On the browse page, select the "Conference" category filter (pick a category that has at least one default event).
  - Expected: Only events of that category are shown; no event of another category appears.

- [ ] FT-08: Visitor can filter events by date
  - Action: On the browse page, apply a date filter for a specific date that has at least one default event.
  - Expected: Only events scheduled on that date are shown; events on other dates are hidden.

- [ ] FT-09: Visitor can search events by keyword
  - Action: Type a keyword that exists in a default event's title into the search box; submit.
  - Expected: The matching event(s) appear in results; unrelated events are not shown.

- [ ] FT-10: Visitor can select ticket quantities and complete checkout to reserve tickets
  - Action: On an event detail page, set quantity 2 for one ticket type; fill the checkout form (name, email) and submit the reservation.
  - Expected: Reservation is confirmed (confirmation message/page shown) and the available quantity for that ticket type decreases by 2.

- [ ] FT-11: Organizer can view a list of ticket reservations
  - Action: Navigate to the organizer's reservations page after FT-10's reservation exists.
  - Expected: The reservation appears, showing the event, ticket type, quantity, and the buyer's name/email.

## Constraint

- [ ] CS-01: Event cannot be created with missing required fields
  - Action: In the Create Event form, leave Title empty (then repeat leaving Date empty) and attempt to submit.
  - Expected: Submission is blocked, a validation message identifies the empty required field(s), and no new event is created.

- [ ] CS-02: Ticket quantity cannot exceed available quantity
  - Action: On an event detail page, set a quantity greater than the ticket type's available quantity and attempt to reserve.
  - Expected: Reservation is blocked with an error stating the maximum available quantity; no reservation is created and inventory is unchanged.

- [ ] CS-03: Checkout cannot be submitted with empty or invalid buyer details
  - Action: With a valid ticket quantity selected, submit checkout with an empty name field (then repeat with an invalid email such as "abc").
  - Expected: Submission is blocked with a validation message on the offending field; no reservation is created.

- [ ] CS-04: Only upcoming events appear in the visitor browse list
  - Action: Note any default event dated in the past (or create/observe one), then open the public browse page.
  - Expected: No past-dated event is listed; the browse list contains only events with dates from today onward.

## Interaction

- [ ] IX-01: Category, date filter, and keyword search combine and can be cleared
  - Action: Apply a category filter, then a date filter, then a keyword search; afterwards clear all filters/search.
  - Expected: Results narrow to events matching all applied criteria; clearing restores the full upcoming events list.

- [ ] IX-02: Order total updates live as ticket quantities change
  - Action: On an event detail page, increase a ticket type quantity from 1 to 3.
  - Expected: The displayed order total updates immediately to quantity × price (3 × unit price) without a page reload.

## Content

- [ ] CT-01: Event listings display accurate event data
  - Action: Compare the data shown for one event on the browse list against its detail page.
  - Expected: Title, category label, date, and location text are identical on both, and the date is formatted consistently across all listings.

- [ ] CT-02: Search results are relevant to the entered keyword
  - Action: Search a keyword from a default event's title and inspect every returned result.
  - Expected: Every returned event contains that keyword in its title, category, or location text; no unrelated event is returned.

- [ ] CT-03: Reservation list matches the submitted checkout data
  - Action: Complete a reservation (e.g., 2 × "VIP") and open the organizer's reservations list.
  - Expected: The entry shows the correct event title, the exact ticket type name, quantity 2, and the buyer name/email exactly as entered at checkout.