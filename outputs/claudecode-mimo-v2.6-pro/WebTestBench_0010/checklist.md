# Test Checklist

## Functionality
- [ ] FT-01: Browse the list of restaurants.
  - Action: Open the application's home/browse page.
  - Expected: A list of default restaurants is displayed, each entry showing a restaurant name.
- [ ] FT-02: Open a restaurant's detail page.
  - Action: Click a restaurant entry in the restaurant list.
  - Expected: The detail page for that restaurant opens and shows its information.
- [ ] FT-03: Create a table reservation with date, time, and party size.
  - Action: On a restaurant's booking form, select a future date, a time, and party size 2, then click the "Reserve" button.
  - Expected: The reservation is created and appears in the reservations list.
- [ ] FT-04: View upcoming reservations.
  - Action: Navigate to the "My Reservations" page.
  - Expected: All upcoming bookings are listed with restaurant name, date, time, and party size.
- [ ] FT-05: Cancel a reservation.
  - Action: Click "Cancel" on an upcoming reservation and confirm the cancellation.
  - Expected: The reservation is no longer listed as upcoming (removed or shown as cancelled).
- [ ] FT-06: Modify a reservation.
  - Action: Click "Modify" on an upcoming reservation, change the time and party size, then save.
  - Expected: The reservation is updated and shows the new time and party size.
- [ ] FT-07: Submit a review with rating and text.
  - Action: Open a restaurant's review form, select a 4-star rating, enter review text (e.g., "Great food"), click "Submit Review".
  - Expected: The review is submitted and appears in the restaurant's reviews section.
- [ ] FT-08: Apply a discount coupon during reservation.
  - Action: In the coupon field on the booking form, enter a valid coupon code and click "Apply", then complete the reservation.
  - Expected: The coupon is accepted and the reservation is created with the discounted price.

## Constraint
- [ ] CS-01: Reservation cannot be submitted with missing required fields.
  - Action: Open the booking form and click "Reserve" without selecting date, time, or party size.
  - Expected: Submission is blocked with a validation error; no reservation is created.
- [ ] CS-02: Past dates cannot be used for reservations.
  - Action: Select a past date (e.g., yesterday) on the booking form and submit; repeat in the Modify form.
  - Expected: Submission is blocked with a validation error; no reservation is created or updated.
- [ ] CS-03: Invalid coupon codes are rejected.
  - Action: Enter an invalid code (e.g., "FAKE-CODE-999") in the coupon field and click "Apply".
  - Expected: An error message is shown and the displayed price remains unchanged.
- [ ] CS-04: A rating is required to submit a review.
  - Action: Open the review form, leave the rating unselected, enter review text, click "Submit Review".
  - Expected: Submission is blocked with a validation error; no review is created.

## Interaction
- [ ] IX-01: Confirmation feedback after creating a reservation.
  - Action: Complete a reservation as in FT-03.
  - Expected: A success confirmation message (e.g., "Reservation confirmed") is displayed.
- [ ] IX-02: Confirmation feedback after modifying a reservation.
  - Action: Save changes in the Modify form as in FT-06.
  - Expected: A success confirmation message (e.g., "Reservation updated") is displayed.
- [ ] IX-03: Confirmation feedback after cancelling a reservation.
  - Action: Cancel a reservation as in FT-05.
  - Expected: A confirmation message (e.g., "Reservation cancelled") is displayed.
- [ ] IX-04: Confirmation feedback after submitting a review.
  - Action: Submit a review as in FT-07.
  - Expected: A success confirmation message (e.g., "Review submitted") is displayed.
- [ ] IX-05: Coupon application immediately updates the displayed price.
  - Action: Enter a valid coupon code and click "Apply" on the booking form, before submitting.
  - Expected: The displayed total/discount updates immediately to reflect the coupon.

## Content
- [ ] CT-01: Restaurant list entries show complete names.
  - Action: Open the browse page and inspect all restaurant entries in the list.
  - Expected: Every default restaurant entry displays its restaurant name (no blank or placeholder entries).
- [ ] CT-02: Restaurant detail page shows cuisine type and average price.
  - Action: Open the detail page of any restaurant from the list.
  - Expected: The page displays that restaurant's cuisine type and average price with actual values.
- [ ] CT-03: Review display matches submitted content.
  - Action: Open the reviews section of the restaurant reviewed in FT-07.
  - Expected: The review shows the exact rating (4 stars) and review text as entered.