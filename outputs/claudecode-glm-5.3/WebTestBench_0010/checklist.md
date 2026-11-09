# Test Checklist

## Functionality
- [ ] FT-01: User can browse the list of restaurants
  - Action: Open the restaurant listing page.
  - Expected: A list of restaurants (from default data) is displayed with each restaurant's name visible.

- [ ] FT-02: User can view restaurant details including cuisine type and average price
  - Action: Click on any restaurant in the list.
  - Expected: A details page opens showing the restaurant's name, cuisine type (e.g., "Italian", "Japanese"), and average price (e.g., "$$"/"$30 per person").

- [ ] FT-03: User can create a reservation by selecting date, time, and party size
  - Action: On a restaurant's page, select a valid future date, a time slot, and a party size, then click the "Reserve" button.
  - Expected: The reservation is created and appears in the user's reservations list with the selected restaurant, date, time, and party size.

- [ ] FT-04: User can view their upcoming reservations
  - Action: Navigate to the "My Reservations" (or equivalent) page.
  - Expected: All active future reservations are listed, each showing restaurant name, date, time, party size, and status.

- [ ] FT-05: User can cancel a reservation
  - Action: On an upcoming reservation, click the "Cancel" button and confirm.
  - Expected: The reservation status changes to "Cancelled" (or is removed from upcoming bookings) and no longer appears as an active upcoming booking.

- [ ] FT-06: User can modify a reservation
  - Action: On an upcoming reservation, click "Modify", change the date, time, or party size, and save.
  - Expected: The reservation is updated and the reservations list shows the new date/time/party size, replacing the old values.

- [ ] FT-07: User can apply a valid discount coupon during reservation
  - Action: During the reservation flow, enter a valid coupon code (from default data) in the coupon field and apply it before confirming.
  - Expected: The coupon is accepted and the reservation total/price reflects the discounted amount.

- [ ] FT-08: User can submit a review with a rating for a restaurant
  - Action: On a restaurant's page, select a star rating (e.g., 4 of 5) and enter short review text, then submit.
  - Expected: The review is saved and appears in the restaurant's reviews section with the entered text and rating.

- [ ] FT-09: User can complete a reservation without applying a coupon
  - Action: Create a reservation leaving the coupon field empty.
  - Expected: The reservation is created successfully at the normal (undiscounted) amount.

## Constraint
- [ ] CS-01: Reservation cannot be submitted with missing required fields
  - Action: On the reservation form, leave date, time, or party size empty and click "Reserve".
  - Expected: The reservation is not created; a validation message indicates the required missing fields.

- [ ] CS-02: Reservation cannot use a past date
  - Action: Attempt to create a reservation with a date earlier than today.
  - Expected: The reservation is not created; an error message indicates the date must be in the future (or a past date cannot be selected).

- [ ] CS-03: Party size must be a positive valid number
  - Action: Attempt to submit a reservation with party size 0 or empty.
  - Expected: The reservation is not created; a validation message indicates a valid party size is required.

- [ ] CS-04: Invalid coupon code is rejected
  - Action: During the reservation flow, enter a fake/expired coupon code (e.g., "INVALID123") and apply it.
  - Expected: The coupon is not applied; an error message indicates the code is invalid or expired, and the price remains undiscounted.

- [ ] CS-05: Review cannot be submitted without a rating
  - Action: On a restaurant's page, leave the rating unselected (and/or review text empty) and click submit.
  - Expected: The review is not saved; a validation message indicates a rating (and/or text) is required.

- [ ] CS-06: Cancelled reservation cannot be modified
  - Action: Attempt to modify a reservation that has already been cancelled.
  - Expected: No modification is possible; the "Modify" action is unavailable or returns an error stating the reservation is cancelled.

## Interaction
- [ ] IX-01: Success confirmation shown after reservation is created
  - Action: Complete a valid reservation.
  - Expected: A confirmation message (toast/banner) appears stating the reservation was created successfully, with the booking summary.

- [ ] IX-02: Confirmation feedback shown after cancellation
  - Action: Cancel an upcoming reservation and confirm the action.
  - Expected: A message appears confirming the reservation was cancelled; the reservations list updates immediately without a full page reload error.

- [ ] IX-03: Coupon field provides immediate feedback when applied
  - Action: Type a coupon code and click "Apply" in the reservation flow.
  - Expected: Inline feedback appears next to the coupon field (success with discount amount for a valid code, error for an invalid one) without losing already-entered reservation details.

- [ ] IX-04: Submitted review and rating update the restaurant's display immediately
  - Action: Submit a review with a rating for a restaurant.
  - Expected: The new review appears in the reviews list without requiring a page reload, and the restaurant's average rating updates to include the new rating.

## Content
- [ ] CT-01: Restaurant list entries contain relevant, consistent information
  - Action: Browse the restaurant list and open at least three restaurant detail pages.
  - Expected: Each restaurant displays a real-sounding name, a cuisine type, and an average price; values match between the list view and the detail view for the same restaurant.

- [ ] CT-02: Restaurant images are relevant to the restaurant theme
  - Action: View restaurant cards and detail pages.
  - Expected: All displayed images are food/restaurant/interior photos relevant to each restaurant; no broken images or unrelated placeholders.

- [ ] CT-03: Reviews and ratings displayed are relevant to their restaurant
  - Action: Open a restaurant's reviews section and read existing reviews (from default data).
  - Expected: Each review contains plausible text about the dining experience and a rating (1–5 scale); no empty reviews, spam, or reviews belonging to another restaurant.