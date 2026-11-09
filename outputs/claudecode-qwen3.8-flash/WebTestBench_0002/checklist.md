# Test Checklist

## Functionality
- [ ] FT-01: Organizer can create a new event with all required details
  - Action: As organizer, open the event creation form, enter title "Jazz Night", category "concert", a future date, location text "City Hall", and one ticket type (name "General", price 25, quantity 100), then click "Create"/"Save".
  - Expected: The form is accepted and "Jazz Night" appears in the event list and in the organizer's event management view.

- [ ] FT-02: Visitor can browse all upcoming events
  - Action: As visitor, open the home/events listing page.
  - Expected: A list/grid of upcoming events is displayed, each shown as a card or row entry.

- [ ] FT-03: Visitor can filter events by category
  - Action: On the listing page, select the category filter value "workshop" (or equivalent) and apply it.
  - Expected: Only events whose category is "workshop" remain visible; concert and conference events are hidden.

- [ ] FT-04: Visitor can filter events by date
  - Action: On the listing page, set the date filter to a specific date on which a default event occurs and apply it.
  - Expected: Only events scheduled on that selected date are shown; events on other dates are hidden.

- [ ] FT-05: Visitor can search events by keyword
  - Action: Type a keyword taken from an existing event's title (e.g., "Jazz") into the search box and submit.
  - Expected: The results include the matching event and exclude events whose title/description/location do not contain the keyword.

- [ ] FT-06: Visitor can open an event's detailed page
  - Action: From the listing, click the title or "View details" link of any event.
  - Expected: A dedicated detail page for that event loads, showing that event's own title, category, date, location, and ticket types.

- [ ] FT-07: Visitor can reserve tickets through the checkout form
  - Action: On an event detail page, choose ticket type "General", set quantity to 2, fill the required checkout fields (name and email), and click the reserve/confirm button.
  - Expected: The reservation is completed and the event's reservation appears in the organizer's reservation list with quantity 2.

- [ ] FT-08: Organizer can update an existing event
  - Action: As organizer, open the edit form for an existing event, change the location text to "Grand Arena", save, then reopen the event's detail page.
  - Expected: The change is saved — the detail page and management list now display "Grand Arena".

- [ ] FT-09: Organizer can view the list of ticket reservations
  - Action: As organizer, open the reservations/registrations view.
  - Expected: A list of reservations is rendered showing one entry per reservation made against the organizer's events.

## Constraint
- [ ] CS-01: Event cannot be created without required fields
  - Action: As organizer, leave the title field empty (and date empty) and click "Create"/"Save".
  - Expected: Submission is blocked and a validation message is shown on the missing field(s); no new event is added to the list.

- [ ] CS-02: Cannot reserve more tickets than the available quantity
  - Action: On an event detail page, note the remaining quantity of a ticket type, then attempt to select a quantity greater than that remaining number and submit checkout.
  - Expected: The request is rejected — the quantity input is capped/disabled with an error such as "Only X tickets available", and no over-sell reservation is recorded.

- [ ] CS-03: Past events are excluded from the upcoming-events browse list
  - Action: With a default event whose date is before 2026-11-08 present in the data, load the visitor listing and the category/date filters.
  - Expected: The past event is not displayed anywhere in the upcoming events listing or filter results.

- [ ] CS-04: Category is restricted to the three defined options
  - Action: On the event creation form and on the visitor category filter, inspect the available category choices.
  - Expected: Exactly "concert", "conference", and "workshop" are selectable; no free-text category entry is possible.

## Interaction
- [ ] IX-01: Confirmation is displayed after a reservation is completed
  - Action: Complete a valid checkout reservation as a visitor.
  - Expected: An explicit success message/toast (e.g., "Reservation confirmed") is shown, and/or the user is redirected to a confirmation view for that reservation.

- [ ] IX-02: List results update in response to filter and search actions
  - Action: Change the category filter, then change the keyword search box, on the listing page.
  - Expected: The displayed event results change immediately to match the new criteria (previous results cleared), rather than remaining stale.

- [ ] IX-03: Checkout total recalculates when ticket quantity changes
  - Action: On the checkout form, increase the quantity of a ticket type from 1 to 3.
  - Expected: The displayed order total updates to reflect the new quantity (e.g., 3 × the ticket price), and any per-type subtotal shown also updates.

## Content
- [ ] CT-01: Listing entries display complete event summary information
  - Action: Inspect each event card/row on the visitor listing page.
  - Expected: Every entry shows the event's title, category, date, location text, and a price indicator — no blank, "undefined", "null", or placeholder-lorem text.

- [ ] CT-02: Detail page shows all ticket types with price and remaining quantity
  - Action: Open an event that has multiple ticket types and inspect the ticket selection section.
  - Expected: Each ticket type is listed with its name, its price, and its available/remaining quantity, matching the organizer's data.

- [ ] CT-03: Reservation list content is relevant and correctly attributed
  - Action: Inspect the rows in the organizer's reservation list after reservations exist.
  - Expected: Each row shows the reserved event title, the ticket type/quantity, the reserver's identifying detail, and the reservation date, with no unrelated or empty rows.