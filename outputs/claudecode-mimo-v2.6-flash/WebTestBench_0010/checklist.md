# Test Checklist

## Functionality
- [ ] FT-01: User can browse the list of restaurants
  - Action: Open the application's main restaurant listing page.
  - Expected: A list of available restaurants is displayed, each entry selectable to view its details.
- [ ] FT-02: User can view restaurant details
  - Action: Click on any restaurant in the list.
  - Expected: The restaurant's detail page opens, showing its cuisine type and average price.
- [ ] FT-03: User can reserve a table
  - Action: On a restaurant detail page, select a date, a time, and a party size, then submit the reservation.
  - Expected: The reservation is created and the selected date, time, and party size are saved for that restaurant.
- [ ] FT-04: User can view upcoming reservations
  - Action: Navigate to the user's reservations ("My reservations" / "Upcoming bookings") section.
  - Expected: The newly created booking appears in the list of upcoming reservations.
- [ ] FT-05: User can cancel a reservation
  - Action: Open an upcoming reservation and click the cancel option.
  - Expected: The reservation is canceled and no longer appears in the upcoming reservations list.
- [ ] FT-06: User can modify a reservation
  - Action: Open an upcoming reservation, change its date, time, or party size, and save the changes.
  - Expected: The reservation is updated and displays the newly selected values.
- [ ] FT-07: User can submit a review and rating for a restaurant
  - Action: Open a restaurant page, select a star rating, enter review text, and submit.
  - Expected: The review with its rating is saved and appears in the restaurant's reviews section.
- [ ] FT-08: User can apply a discount coupon during reservation
  - Action: During the reservation process, enter a valid discount coupon code and apply it, then complete the reservation.
  - Expected: The coupon is accepted and the reservation is completed with the discount applied.

## Constraint
- [ ] CS-01: Reservation cannot be submitted with missing date, time, or party size
  - Action: Attempt to submit a reservation while any of the date, time, or party size fields is unselected/empty.
  - Expected: Submission is blocked with an error message and no reservation is created.
- [ ] CS-02: Invalid coupon codes are rejected
  - Action: Enter a nonexistent/invalid coupon code during reservation and click apply.
  - Expected: The coupon is rejected with an error message and no discount is applied.
- [ ] CS-03: Review cannot be submitted without a rating
  - Action: Attempt to submit a review while leaving the rating unselected (with or without review text).
  - Expected: Submission is blocked with an error message and the review is not posted.

## Interaction
- [ ] IX-01: Success confirmation is shown after creating a reservation
  - Action: Complete a valid reservation submission.
  - Expected: A visible success message/notification appears confirming the reservation was created.
- [ ] IX-02: Applying a valid coupon immediately updates the displayed price summary
  - Action: Enter a valid coupon code and apply it during the reservation process.
  - Expected: The displayed total/discount summary updates immediately to reflect the applied coupon.

## Content
- [ ] CT-01: Restaurant list entries show accurate cuisine type and average price
  - Action: Browse the restaurant list and open each restaurant's detail page.
  - Expected: Each restaurant displays a cuisine type and average price, and the values match between the list and detail views.
- [ ] CT-02: All displayed content is relevant to restaurant dining
  - Action: Browse the restaurant list, a restaurant detail page, and the reviews section.
  - Expected: All visible names, descriptions, ratings, and media relate to restaurants/reservations, with no placeholder or unrelated content.