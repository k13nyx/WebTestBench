# Test Result

## Functionality
- [X] FT-01: Organizer can create a new event listing with all required details.
  - Action: As an organizer, open the create-event form, fill in a title, select a category, pick a future date, enter a location text, and add a ticket type with a name, price, and quantity; submit the form.
  - Expected: The event is saved successfully and the form completes without errors.
- [ ] FT-02: A newly created event appears in the upcoming events listing.
  - Action: After creating the event in FT-01, navigate to the upcoming events browse page.
  - Expected: The newly created event appears in the list alongside the default events.
  - Bug Report:
    - Issue: Incomplete Upcoming Events Listing (default events missing from browse list)
    - Actual: After creating "QA Automation Test Event" (FT-01), the "All Upcoming Events" list shows only "QA Automation Test Event" ("Concert | Jun 15, 2027 | QA Test Arena, Testville | From $25 | View Details →"). The three default events ("Summer Jazz Festival", "Tech Innovation Summit 2025", "Leadership & Management Masterclass") are not in the list — they appear only in the separate "Featured Events" section and the Organizer Dashboard. Before any event is created, the list shows "No events found / Try adjusting your filters or search query."
- [ ] FT-03: Visitor can browse all upcoming events.
  - Action: Open the upcoming events page as a visitor (no filters applied).
  - Expected: All upcoming events (default data included) are listed.
  - Bug Report:
    - Issue: Upcoming Events List Excludes Default/Past-Dated Events
    - Actual: With no filters applied, the "All Upcoming Events" section shows "No events found" while the Organizer Dashboard lists the 3 default events ("Total Events: 3"). The list only contains events dated on/after the current date (2026-11-08) — probe-verified: the created event "Past Date Probe Event" dated 2025-03-01 is saved and shown in the organizer's events list ("Your Events") but is absent from "All Upcoming Events". The seeded default events (Jul 15, 2025 / Sep 20, 2025 / Oct 15, 2025) are all in the past and therefore never listed.
- [ ] FT-04: Visitor can filter events by category.
  - Action: Select the category filter "concert" on the events page.
  - Expected: Only events with category "concert" are shown; switching to "conference" or "workshop" shows only events of that category.
  - Bug Report:
    - Issue: Category Filter Results Omit Existing Events of the Selected Category
    - Actual: Clicking "Concerts" shows "1 events found" listing only the session-created "QA Automation Test Event" — the default concert "Summer Jazz Festival" is not shown. Clicking "Conferences" shows "0 events found / No events found" although "Tech Innovation Summit 2025" and "Leadership & Management Masterclass" (category Conference) exist in the system. Clicking "Workshops" shows "0 events found" (no future-dated workshop event existed at test time). No cross-category leakage occurs, but the events of each category are not shown (same root cause as FT-03: past-dated events are excluded from the browseable list).
- [ ] FT-05: Visitor can filter events by date.
  - Action: Set the date filter to the date of a known default event.
  - Expected: Only events on the selected date are shown in the list.
  - Bug Report:
    - Issue: Date Filter Returns No Results for a Default Event's Date
    - Actual: Setting the date filter to 2025-07-15 (date of default event "Summer Jazz Festival") shows "0 events found" — the event occurring on the selected date is not displayed. (The date filter mechanism itself narrows correctly over listed events: setting 2027-06-15 shows exactly "1 events found: QA Automation Test Event", and 2027-06-15 is that event's date. The default events are excluded from the list entirely — see FT-03.)
- [ ] FT-06: Visitor can search events by keywords.
  - Action: Type a word from an existing event's title into the search field and submit.
  - Expected: The events list shows only events whose title contains that keyword.
  - Bug Report:
    - Issue: Keyword Search Does Not Find Default Events by Title
    - Actual: Typing "Summer" (a word from the existing default event title "Summer Jazz Festival") returns "0 events found" — the matching event is not shown. (Search works over listed events: typing "Automation" shows exactly "1 events found: QA Automation Test Event".) The default events are absent from the searchable list (same root cause as FT-03).
- [X] FT-07: Visitor can open an event's detailed page from the listing.
  - Action: Click on an event card/entry in the upcoming events list.
  - Expected: The detailed page for that event opens, showing its full details and ticket selection.
- [X] FT-08: Visitor can select ticket quantities on the event detail page.
  - Action: On an event detail page, set a quantity (e.g., 2) for one of the ticket types using the quantity selector.
  - Expected: The selector accepts the value and the chosen quantity is reflected in the checkout summary.
- [X] FT-09: Visitor can reserve tickets via the checkout form.
  - Action: Select ticket quantities, fill in the checkout form (name, email), and submit it.
  - Expected: The reservation is created successfully and a confirmation of the reservation is shown.
- [X] FT-10: Organizer can view and update an existing event.
  - Action: Open the organizer's events list, select an existing event, edit its title/location, and save the changes.
  - Expected: The update is saved, and reopening the event shows the changed values.
- [X] FT-11: Organizer can view a list of ticket reservations.
  - Action: Navigate to the organizer's reservations view after a reservation has been made (FT-09).
  - Expected: A list of ticket reservations is displayed and includes the newly made reservation.

## Constraint
- [X] CS-01: Event creation is blocked when required fields are missing.
  - Action: Submit the create-event form with an empty title, or empty date/location, or a ticket type missing its name, price, or quantity.
  - Expected: The event is not saved and a validation error identifies the missing required field(s).
- [ ] CS-02: Event category is restricted to the allowed values.
  - Action: Inspect the category field on the create/edit event form and attempt to save with no category or a value other than "concert", "conference", or "workshop".
  - Expected: Only "concert", "conference", and "workshop" are selectable/savable; saving with an empty or other category is rejected with a validation error.
  - Bug Report:
    - Issue: Missing Category Validation (event saved with empty category)
    - Actual: The dropdown offers exactly the three allowed values (options: "Concert"=concert, "Conference"=conference, "Workshop"=workshop — no other or empty option is selectable via the UI). However, when the create form was submitted with the category empty (combobox displaying "Select category", select value ""), the event was created without any validation error — "CS-05 Negative Test Event" was saved with no category and "Total Events" changed from 4 to 5. The expected rejection ("saving with an empty or other category is rejected with a validation error") did not occur.
- [ ] CS-03: Ticket reservations cannot exceed the available quantity.
  - Action: On an event detail page, attempt to reserve more tickets of a ticket type than its stated quantity.
  - Expected: The reservation is rejected with a validation error indicating insufficient ticket quantity; no reservation is created.
  - Bug Report:
    - Issue: Missing Validation Error for Insufficient Ticket Quantity (silent input capping)
    - Actual: Attempting to select more than the stated quantity — 4 clicks of "+" on a ticket type showing "2 tickets available" — leaves the counter at 2 with the "+" button disabled and no error message. On an event showing "98 tickets available" the selector similarly stops at 10 with "+" disabled. After all stock was reserved, the detail page shows "Sold out" with no quantity selector or checkout offered. No over-limit reservation is ever created, but no "insufficient ticket quantity" validation error is displayed — the attempt is silently prevented instead of rejected with the expected error.
- [X] CS-04: Checkout form cannot be submitted with empty required fields.
  - Action: Select ticket quantities, leave the checkout form's name and email empty, and submit.
  - Expected: Submission is blocked with validation errors on the empty fields; no reservation is created.
- [X] CS-05: Ticket price and quantity must be valid positive numbers.
  - Action: When creating an event, enter a negative or non-numeric value (e.g., "abc") for a ticket type's price or quantity and submit.
  - Expected: The event is not saved and a validation error indicates an invalid price or quantity.

## Interaction
- [X] IX-01: System provides success feedback after creating or updating an event.
  - Action: Successfully create an event (FT-01), then successfully update an event (FT-10), observing the interface after each save.
  - Expected: A visible success confirmation is displayed after each save (creation and update).
- [X] IX-02: System provides confirmation feedback after a ticket reservation.
  - Action: Complete a checkout form submission that creates a reservation (FT-09) and observe the interface response.
  - Expected: A visible confirmation is displayed indicating the reservation was completed successfully.

## Content
- [X] CT-01: Event detail page displays the event's data exactly as entered.
  - Action: Open the detail page of an event created in FT-01 and compare every field against what was entered.
  - Expected: Title, category, date, location, and each ticket type's name, price, and quantity are displayed exactly as entered, with no missing or altered values.
- [X] CT-02: Reservations list shows accurate reservation data.
  - Action: In the organizer's reservations list (FT-11), compare each reservation row against a completed checkout.
  - Expected: Each reservation shows the correct event, ticket type, quantity reserved, and the name/email supplied at checkout.
