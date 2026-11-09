All checklist items have been executed. CT-01 confirmed across all six detail pages (French·$$$$, Japanese·$$$, Italian·$$, American BBQ·$$, Indian·$$, Seafood·$$$ — all matching the list), and CT-02 content reviewed on list, detail, reservation form, and reviews.

# Test Result

## Functionality
- [X] FT-01: User can browse the list of restaurants
  - Action: Open the application's main restaurant listing page.
  - Expected: A list of available restaurants is displayed, each entry selectable to view its details.
- [X] FT-02: User can view restaurant details
  - Action: Click on any restaurant in the list.
  - Expected: The restaurant's detail page opens, showing its cuisine type and average price.
- [X] FT-03: User can reserve a table
  - Action: On a restaurant detail page, select a date, a time, and a party size, then submit the reservation.
  - Expected: The reservation is created and the selected date, time, and party size are saved for that restaurant.
- [X] FT-04: User can view upcoming reservations
  - Action: Navigate to the user's reservations ("My reservations" / "Upcoming bookings") section.
  - Expected: The newly created booking appears in the list of upcoming reservations.
- [X] FT-05: User can cancel a reservation
  - Action: Open an upcoming reservation and click the cancel option.
  - Expected: The reservation is canceled and no longer appears in the upcoming reservations list.
- [X] FT-06: User can modify a reservation
  - Action: Open an upcoming reservation, change its date, time, or party size, and save the changes.
  - Expected: The reservation is updated and displays the newly selected values.
- [X] FT-07: User can submit a review and rating for a restaurant
  - Action: Open a restaurant page, select a star rating, enter review text, and submit.
  - Expected: The review with its rating is saved and appears in the restaurant's reviews section.
- [X] FT-08: User can apply a discount coupon during reservation
  - Action: During the reservation process, enter a valid discount coupon code and apply it, then complete the reservation.
  - Expected: The coupon is accepted and the reservation is completed with the discount applied.

## Constraint
- [X] CS-01: Reservation cannot be submitted with missing date, time, or party size
  - Action: Attempt to submit a reservation while any of the date, time, or party size fields is unselected/empty.
  - Expected: Submission is blocked with an error message and no reservation is created.
- [X] CS-02: Invalid coupon codes are rejected
  - Action: Enter a nonexistent/invalid coupon code during reservation and click apply.
  - Expected: The coupon is rejected with an error message and no discount is applied.
- [X] CS-03: Review cannot be submitted without a rating
  - Action: Attempt to submit a review while leaving the rating unselected (with or without review text).
  - Expected: Submission is blocked with an error message and the review is not posted.

## Interaction
- [X] IX-01: Success confirmation is shown after creating a reservation
  - Action: Complete a valid reservation submission.
  - Expected: A visible success message/notification appears confirming the reservation was created.
- [X] IX-02: Applying a valid coupon immediately updates the displayed price summary
  - Action: Enter a valid coupon code and apply it during the reservation process.
  - Expected: The displayed total/discount summary updates immediately to reflect the applied coupon.

## Content
- [X] CT-01: Restaurant list entries show accurate cuisine type and average price
  - Action: Browse the restaurant list and open each restaurant's detail page.
  - Expected: Each restaurant displays a cuisine type and average price, and the values match between the list and detail views.
- [X] CT-02: All displayed content is relevant to restaurant dining
  - Action: Browse the restaurant list, a restaurant detail page, and the reviews section.
  - Expected: All visible names, descriptions, ratings, and media relate to restaurants/reservations, with no placeholder or unrelated content.

**Summary: 16/16 passed.**

Key evidence observed during execution:
- **FT-03/FT-04**: Reservation created for The Golden Fork (Nov 15, 2026, 19:00, 4 Guests) and appeared under "Upcoming (1)" with "Coupon applied: WELCOME10".
- **FT-06**: Modified time 19:00 → 20:00 with toast "Reservation Updated".
- **FT-05**: Confirmation dialog → toast "Reservation Cancelled", Upcoming became (0).
- **FT-07**: New review by "Test Reviewer" (5 stars, Visited Nov 1, 2026) listed; rating count (2)→(3).
- **CS-01**: Toast "Missing Information — Please fill in all required fields."
- **CS-02**: Toast "Invalid Coupon — The coupon code you entered is not valid." for `INVALID99`.
- **CS-03**: Toast "Missing Information — Please fill in all fields and select a rating."
- **IX-01**: Toast + panel "Reservation Confirmed! Your table at The Golden Fork is booked for November 15, 2026 at 19:00."
- **IX-02**: Toast "Coupon Applied! 10% off your first reservation" with inline "WELCOME10 − 10% off" displayed immediately.