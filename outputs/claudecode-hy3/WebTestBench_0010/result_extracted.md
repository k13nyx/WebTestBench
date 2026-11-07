# Test Result

## Functionality
- [X] FT-01: Browse list of restaurants
  - Action: Open the application homepage.
  - Expected: A list of restaurants is displayed, each showing at least its name.
- [X] FT-02: View restaurant details (cuisine type and average price)
  - Action: Click on a restaurant from the list.
  - Expected: A detail view shows the restaurant's cuisine type and average price.
- [X] FT-03: Reserve a table with date, time, and party size
  - Action: On a restaurant, select a valid date, time, and party size, then submit the reservation.
  - Expected: The reservation is created and a confirmation is shown.
- [X] FT-04: View upcoming bookings
  - Action: Open the reservations/manage section.
  - Expected: All upcoming reservations are listed with their date, time, party size, and restaurant.
- [X] FT-05: Cancel a reservation
  - Action: Select an upcoming reservation and choose cancel.
  - Expected: The reservation is removed from the upcoming list.
- [X] FT-06: Modify a reservation
  - Action: Select an upcoming reservation and edit the date, time, or party size, then save.
  - Expected: The reservation reflects the updated details.
- [X] FT-07: Submit a review and rating for a visited restaurant
  - Action: Open a restaurant you have visited and submit a rating with review text.
  - Expected: The review is saved and displayed for that restaurant.
- [X] FT-08: Apply a discount coupon during reservation
  - Action: During the reservation process, enter a valid coupon code and proceed.
  - Expected: The discount is applied to the reservation total.

## Constraint
- [X] CS-01: Reservation requires valid date, time, and party size
  - Action: Attempt to submit a reservation with an empty or invalid date, time, or party size.
  - Expected: Submission is blocked and a validation error identifies the missing/invalid field.
- [X] CS-02: Only valid coupons are accepted
  - Action: Enter an invalid or expired coupon code during reservation.
  - Expected: The coupon is rejected with an error message and no discount is applied.
- [X] CS-03: Review submission requires a rating
  - Action: Attempt to submit a review without selecting a rating.
  - Expected: Submission is blocked and a "rating required" error is shown.
- [X] CS-04: Party size must be within allowed bounds
  - Action: Enter a party size of 0 or above the maximum allowed value.
  - Expected: The value is rejected with a validation message.

## Interaction
- [X] IX-01: Show success confirmation after reservation creation
  - Action: Complete a valid reservation.
  - Expected: A success toast or confirmation message appears confirming the booking.
- [X] IX-02: Reservation list updates immediately after changes
  - Action: Cancel or modify a reservation.
  - Expected: The upcoming reservations list refreshes to reflect the change without a manual page reload.

## Content
- [X] CT-01: Restaurant details are accurate and relevant
  - Action: Open several restaurants and inspect their details.
  - Expected: Each shows a cuisine type and average price that are relevant and consistent with the restaurant.
- [X] CT-02: Reviews display relevant rating and text
  - Action: View the reviews section of a restaurant.
  - Expected: Each review shows a rating (e.g., stars/number) and text directly relevant to that restaurant.
