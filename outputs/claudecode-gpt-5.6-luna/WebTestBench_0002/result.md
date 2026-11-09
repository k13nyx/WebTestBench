# Test Result

## Functionality

- [X] FT-01: Organizer can create an event listing with all required event details.
  - Action: Open **Create Event**, enter a title, select **Concert**, **Conference**, or **Workshop**, enter a date and location, add ticket types with prices and quantities, and select **Save Event**.
  - Expected: The event is saved and appears in the organizer’s existing event list.

- [X] FT-02: Organizer can view existing event listings.
  - Action: Open the organizer’s event-management view.
  - Expected: Existing events are displayed with their titles, categories, dates, locations, and ticket information.

- [X] FT-03: Organizer can update an existing event listing.
  - Action: Select an existing event, choose **Edit**, change a supported detail such as location or ticket price, and select **Save Event**.
  - Expected: The changed value is saved and displayed when the event is reopened.

- [X] FT-04: Visitors can browse all upcoming events.
  - Action: Open the visitor event-browsing page.
  - Expected: All available upcoming events are displayed as selectable listings.

- [X] FT-05: Visitors can open an event’s detailed page.
  - Action: Select any event from the browse view.
  - Expected: The event detail page displays the event information and available ticket types.

- [X] FT-06: Visitors can select ticket quantities and complete a reservation.
  - Action: On an event detail page, select a valid quantity for an available ticket type, complete the checkout form, and select **Reserve Tickets**.
  - Expected: The reservation is completed and a reservation confirmation is shown.

- [X] FT-07: Organizer can view ticket reservations for existing events.
  - Action: Open the organizer’s reservation view.
  - Expected: A basic reservation list is displayed, including the related event and reserved ticket information.

## Constraint

- [X] CS-01: Event creation prevents submission when required event details are missing.
  - Action: Open **Create Event**, leave one required field empty, and select **Save Event**.
  - Expected: The event is not saved and the missing field is identified with a validation message.

- [X] CS-02: Ticket types require valid prices and quantities.
  - Action: In the event form, enter a negative, zero, or non-numeric ticket price or quantity, then select **Save Event**.
  - Expected: The event is not saved and the invalid ticket value is identified.

- [ ] CS-03: Visitors cannot reserve more tickets than are available.
  - Action: On an event detail page, attempt to select a quantity greater than the displayed available quantity.
  - Expected: The excessive quantity cannot be submitted, and the interface indicates that availability has been exceeded.
  - Bug Report:
    - Issue: Incorrect ticket quantity limit and missing availability validation feedback
    - Actual: The event displayed 19 tickets available, but the increase control became disabled at 10 tickets. The interface did not allow an attempt above the displayed availability and did not show a message indicating that availability had been exceeded.

- [X] CS-04: Visitors cannot complete checkout with missing required form data.
  - Action: Leave a required checkout field empty and select **Reserve Tickets**.
  - Expected: The reservation is not created and the missing checkout field is identified.

- [X] CS-05: Event browsing filters show only matching events.
  - Action: Apply a category filter, apply a date filter, and enter a keyword in the event search field.
  - Expected: Each applied filter or search term excludes events that do not match its criterion and retains matching events.

## Interaction

- [X] IX-01: Event browse controls update the displayed results after user input.
  - Action: Change the **Category** filter, change the date filter, and submit or activate the keyword search.
  - Expected: The event list refreshes to reflect the selected filters or keyword without displaying stale results.

- [X] IX-02: Ticket quantity changes update the checkout selection and total.
  - Action: Increase and decrease a ticket quantity on an event detail page.
  - Expected: The selected quantity and calculated reservation total update immediately to match the chosen quantity and ticket price.

- [X] IX-03: Organizer save actions provide clear completion feedback.
  - Action: Save a newly created or edited event with valid values.
  - Expected: The interface indicates that the event was saved and shows the saved event data.

- [ ] IX-04: Reservation completion provides clear confirmation and preserves reservation details.
  - Action: Complete a valid checkout and select **Reserve Tickets**.
  - Expected: A confirmation state appears showing the reserved event and ticket information.
  - Bug Report:
    - Issue: Incomplete reservation confirmation details
    - Actual: The confirmation notification stated, “Reservation Confirmed! Your tickets for QA Summer Concert have been reserved,” but did not show the reserved ticket type or quantity. Ticket details were only visible later in the organizer dashboard.

## Content

- [ ] CT-01: Each event listing displays the required event information.
  - Action: Review event cards and an event detail page.
  - Expected: Each event shows a title, category, date, location text, ticket type, ticket price, and available quantity where applicable.
  - Bug Report:
    - Issue: Event cards omit ticket information
    - Actual: The browse event card displayed the title, category, date, location, and starting price, but did not display the ticket type or available quantity. Those details were available only on the event detail page.

- [X] CT-02: Category values use the supported event categories.
  - Action: Review category labels and the category filter options.
  - Expected: Categories are presented as **Concert**, **Conference**, or **Workshop**, with no unrelated category values.

- [X] CT-03: Organizer reservation records contain usable ticket-reservation details.
  - Action: Review the organizer’s reservation list for an event with reservations.
  - Expected: Each record identifies the event, ticket type, and reserved quantity, with no missing or contradictory values.