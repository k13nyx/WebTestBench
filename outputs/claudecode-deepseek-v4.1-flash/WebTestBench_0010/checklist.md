# Test Checklist

## Functionality
- [ ] FT-01: Browse the restaurant list
  - Action: Open the application and view the main restaurant listing page.
  - Expected: A list of restaurants is displayed, each showing at least a name and thumbnail.

- [ ] FT-02: View restaurant details
  - Action: Click a restaurant from the list to open its detail page.
  - Expected: Detail page displays the cuisine type and average price for that restaurant.

- [ ] FT-03: Create a reservation
  - Action: On a restaurant page, select a valid date, time, and party size, then submit the reservation.
  - Expected: A new reservation is created and linked to the selected restaurant.

- [ ] FT-04: View upcoming bookings
  - Action: Open the "My Reservations" / bookings section.
  - Expected: All upcoming reservations are listed with restaurant, date, time, and party size.

- [ ] FT-05: Modify an existing reservation
  - Action: Select an upcoming reservation, change the date/time/party size, and save.
  - Expected: The reservation is updated and reflects the new values in the upcoming list.

- [ ] FT-06: Cancel an existing reservation
  - Action: Select an upcoming reservation and choose "Cancel".
  - Expected: The reservation is removed from upcoming bookings and no longer active.

- [ ] FT-07: Submit a review and rating
  - Action: On a visited restaurant page, enter a rating and review text, then submit.
  - Expected: The review and rating are saved and displayed on the restaurant.

- [ ] FT-08: Apply a discount coupon during reservation
  - Action: Enter a valid coupon code in the reservation flow and apply it.
  - Expected: The coupon is accepted and applied to the reservation total.

## Constraint
- [ ] CS-01: Reservation requires all required fields
  - Action: Attempt to submit a reservation with date, time, or party size left empty.
  - Expected: Submission is blocked with a validation message identifying the missing field.

- [ ] CS-02: Past dates are not selectable
  - Action: Attempt to select a date earlier than today in the reservation date picker.
  - Expected: Past dates are disabled or rejected; reservation is not allowed in the past.

- [ ] CS-03: Party size within allowed range
  - Action: Enter a party size below the minimum (e.g., 0) or above the maximum allowed.
  - Expected: Invalid party size is rejected with an error message.

- [ ] CS-04: Review requires rating and visited restaurant
  - Action: Attempt to submit a review with no rating, or on a restaurant not visited.
  - Expected: Submission is blocked and an explanatory message is shown.

- [ ] CS-05: Invalid or expired coupon is rejected
  - Action: Enter an invalid or expired coupon code and apply it.
  - Expected: Coupon is rejected with an error; total remains unchanged.

- [ ] CS-06: Canceled reservation cannot be modified
  - Action: Attempt to modify a reservation that was already canceled.
  - Expected: Modification is blocked; the canceled reservation is not editable.

## Interaction
- [ ] IX-01: Confirmation on successful reservation
  - Action: Complete a valid reservation.
  - Expected: A success confirmation (message/toast) is shown with the reservation details.

- [ ] IX-02: Coupon discount reflected in total
  - Action: Apply a valid coupon during reservation.
  - Expected: The displayed total updates immediately to show the discounted amount.

- [ ] IX-03: Feedback on review submission
  - Action: Submit a valid review and rating.
  - Expected: A success toast/message confirms the review was posted.

- [ ] IX-04: Confirmation prompt before canceling
  - Action: Click "Cancel" on an upcoming reservation.
  - Expected: A confirmation prompt appears before the cancellation is finalized.

## Content
- [ ] CT-01: Restaurant media is relevant
  - Action: Review images/icons shown for restaurants on the list and detail pages.
  - Expected: All displayed media are directly relevant to restaurants/food and load without broken links.

- [ ] CT-02: Detail content matches the reservation theme
  - Action: Inspect text on restaurant detail pages.
  - Expected: Cuisine type, average price, and any review/rating text are present and consistent with that restaurant.