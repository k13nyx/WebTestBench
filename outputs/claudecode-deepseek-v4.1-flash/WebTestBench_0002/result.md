All checklist items have been executed with evidence. Here is the full result.

# Test Result

## Functionality

- [X] FT-01: Organizer can create a new event listing
  - Action: On the organizer event page, fill in Title, Category, Date, Location, and submit.
  - Expected: The new event is saved and appears in the organizer's event list.
  - Note: Created "QA Test Workshop" (Workshop, Dec 15 2026 18:00, Testville) — it appeared immediately in "Your Events". Also created "QA Listing Two" and another future event — all listed. (Creation form additionally requires a non-empty Description, which is not visually marked.)

- [X] FT-02: Organizer can attach ticket types to an event
  - Action: While creating/editing an event, add a ticket type with a Name, Price, and Quantity.
  - Expected: The ticket type is saved and displayed on the event.
  - Note: Ticket "GA $30 · 100 tickets available" persisted and displayed on the event detail page; "Pass $20 · 3 tickets available" likewise on another event.

- [X] FT-03: Visitor can browse all upcoming events
  - Action: Open the events listing page.
  - Expected: All upcoming events are listed with title, category, date, and location.
  - Note: The listing filters to events whose date is after today; cards show category, title, date (+time), location, "From $X". With two upcoming events present, both were listed. (On a pristine load the seeded events are all dated 2025, so the "All Upcoming Events" list is empty by design; a seeded event edited to a future date appeared correctly — confirming date-based, not broken, filtering.)

- [X] FT-04: Visitor can filter events by category
  - Action: Select a category (e.g., "Concert") in the category filter.
  - Expected: Only events matching the selected category are shown.
  - Note: "Concerts" → 1 concert only; "Conferences" → 0 (when no conference was upcoming); a "Clear filters" control appears when a filter is active.

- [X] FT-05: Visitor can filter events by date
  - Action: Apply a date filter (e.g., a specific day or range).
  - Expected: Only events within the selected date/range are shown.
  - Note: The date input filters to the exact selected day — selecting the event's date (2027-06-20) showed only that event; adjacent days (06-19 / 06-21) showed none.

- [X] FT-06: Visitor can search events by keyword
  - Action: Enter a keyword (e.g., part of a title) in the search box and search.
  - Expected: Only events matching the keyword are shown.
  - Note: "ZZQA" → the matching event; "Jazz" and other terms with no upcoming match → 0.

- [X] FT-07: Visitor can view an event detail page
  - Action: Click an event from the listing.
  - Expected: A detail page opens showing title, category, date, location, and ticket types with prices.
  - Note: Detail page showed "Concert | ZZQA Future Concert | Sunday, June 20, 2027 | 20:00 | Future Hall, Testville | GA $30".

- [X] FT-08: Visitor can select ticket quantities
  - Action: On the event detail page, choose a quantity for a ticket type.
  - Expected: The selected quantity is accepted and reflected in the running total.
  - Note: Quantity incremented 1→2→3→4 with the running total updating ($30→$60→$90→$120) and a "Total (N tickets)" summary.

- [X] FT-09: Visitor can complete checkout to reserve tickets
  - Action: With a quantity selected, fill in the checkout form and submit it.
  - Expected: The reservation is created and the visitor receives a confirmation.
  - Note: Reservation created; organizer view subsequently showed the reservation under the event with the submitted contact details and amount.

- [X] FT-10: Organizer can view and update existing events
  - Action: Open an existing event in the organizer view, change a field (e.g., title or price), and save.
  - Expected: The change is saved and the updated value is shown.
  - Note: Opened the edit dialog (pre-filled with existing values), changed the title to "ZZQA Updated Concert" and date to Jul 25 2027; after "Update Event" the organizer list reflected both changes.

- [X] FT-11: Organizer can view the list of ticket reservations
  - Action: Open the reservations list for an event.
  - Expected: All reservations for that event are listed.
  - Note: Each event card expands to a per-event reservation list (name, email, phone, amount, timestamp, ticket type × qty); the freshly made reservation appeared under its event.

## Constraint

- [X] CS-01: Event cannot be created with missing required fields
  - Action: Attempt to submit the event form with Title, Category, Date, or Location left empty.
  - Expected: Submission is blocked and the missing fields are indicated.
  - Note: The dialog did not close and the empty required fields (Title, Location, Date, Time, ticket Name) were flagged invalid by the browser. Category defaults to "Concert" so it cannot be left empty.

- [X] CS-02: Event category is restricted to the defined values
  - Action: Open the category selector for an event.
  - Expected: Only "concert", "conference", and "workshop" are selectable.
  - Note: The selector offered exactly Concert, Conference, Workshop (values stored lowercase).

- [X] CS-03: Ticket quantity cannot exceed available stock
  - Action: On an event detail page, attempt to select a quantity greater than the ticket type's remaining quantity.
  - Expected: The quantity is capped or rejected; more than available cannot be selected.
  - Note: With stock 100 the "+" capped at 10 then disabled; with stock reduced to 3 the "+" capped at exactly 3 and disabled. Quantity never exceeded remaining stock.

- [X] CS-04: Checkout requires mandatory contact fields
  - Action: Attempt to submit the checkout form with required fields (e.g., name, email) empty.
  - Expected: Submission is blocked and the required fields are indicated.
  - Note: Submitting the empty checkout kept the dialog open and flagged all three required inputs (Full Name, Email, Phone) invalid.

- [X] CS-05: Sold-out ticket types cannot be reserved
  - Action: Locate a ticket type with zero remaining quantity and attempt to reserve it.
  - Expected: Reservation is prevented and the ticket type is shown as unavailable.
  - Note: After reserving the last 10 of "VIP Table", the same session showed the type as "Sold out" with the quantity controls removed — reservation not possible.

## Interaction

- [X] IX-01: Successful reservation shows a confirmation
  - Action: Complete a valid checkout submission.
  - Expected: A success confirmation (message/notification) is displayed.
  - Note: Toast displayed "Reservation Confirmed! Your tickets for … have been reserved."

- [X] IX-02: Search with no matches shows an empty-state message
  - Action: Search for a keyword that matches no event.
  - Expected: A "no results found" message is displayed instead of a blank list.
  - Note: Showed "0 events found", "No events found" and "Try adjusting your filters or search query."

- [X] IX-03: Updated event data reflects immediately after saving
  - Action: Edit an event (e.g., change its date) and save, then return to the events listing.
  - Expected: The listing shows the updated value without requiring a full restart.
  - Note: After editing, the listing immediately showed the new title/date ("ZZQA Updated Concert · Jul 25, 2027") via client-side navigation.

## Content

- [X] CT-01: Category options match the specified event types
  - Action: Inspect the category options available when creating or filtering events.
  - Expected: Exactly "concert", "conference", and "workshop" are offered.
  - Note: Create/Edit category selector offers Concert, Conference, Workshop only; the filter bar offers All Events, Concerts, Conferences, Workshops.

- [X] CT-02: Prices are displayed with a currency indicator
  - Action: View ticket types on an event detail page.
  - Expected: Each price is shown as a monetary value with a currency symbol (e.g., "$25"), not a bare number.
  - Note: Prices rendered as "$30", "$45", "$20", "$400", etc.

- [X] CT-03: Event detail page shows all required fields
  - Action: Open any event detail page.
  - Expected: Title, category, date, location text, and ticket types (with prices and quantities) are all present.
  - Note: Detail page contained category ("Concert"), title, date ("Sunday, June 20, 2027"), time, location text, and ticket types with prices and "N tickets available" quantities.

---

**Summary:** 21/21 items PASS. No FAIL items.

**Additional non-blocking observations (not covered by any checklist item):**
- The Create/Edit event form marks **Description as a required field** (`required` attribute) but gives no visual required indicator (no asterisk) and no custom error text; the form is silently blocked by native validation when Description is empty. This can surprise an organizer who fills every labelled field the spec lists.
- Event data is held **in memory only** and resets on a full page reload; persistence across sessions/reloads is not provided.
- The event listing filters to future-dated events by default; the seeded events (all dated 2025) therefore never appear on the "All Upcoming Events" list under the current clock, though the Featured section still shows them.