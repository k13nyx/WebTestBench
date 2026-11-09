# Test Result

## Functionality
- [X] FT-01: User can browse the restaurant list
  - Action: Open the application home page / restaurant listing page.
  - Expected: A list of restaurants is displayed, each showing its name (default seed data present, at least 3 restaurants).
- [X] FT-02: User can view restaurant details
  - Action: Click on any restaurant card/name in the list.
  - Expected: A detail view opens showing the restaurant's cuisine type and average price.
- [X] FT-03: User can create a reservation
  - Action: On a restaurant's page, select a date, a time, and a party size, then submit the reservation.
  - Expected: The reservation is created successfully and a confirmation is shown (message/toast/entry in bookings).
- [X] FT-04: User can view upcoming reservations
  - Action: Open the "My Reservations" (or equivalent) section after creating a booking.
  - Expected: The upcoming reservation appears with restaurant name, date, time, and party size.
- [X] FT-05: User can cancel a reservation
  - Action: Open an upcoming reservation and click "Cancel".
  - Expected: The reservation's status changes to cancelled (or it is removed) and it no longer counts as an upcoming booking.
- [X] FT-06: User can modify a reservation
  - Action: Open an upcoming reservation, change the date/time/party size, and save.
  - Expected: The reservation shows the updated date/time/party size in "My Reservations".
- [X] FT-07: User can submit a review with a rating
  - Action: On a restaurant's detail page, enter a review text, select a rating, and submit.
  - Expected: The review and rating appear on the restaurant's page.
- [X] FT-08: User can apply a discount coupon to a reservation
  - Action: During the reservation process, enter a valid coupon code (from the app's default data) and apply it.
  - Expected: The discount is applied and the adjusted price/amount is shown before confirming.

## Constraint
- [X] CS-01: Reservation cannot be submitted with missing required fields
  - Action: Attempt to submit the reservation form without selecting date, time, or party size.
  - Expected: Submission is blocked and a validation message is displayed; no reservation is created.
- [X] CS-02: Party size must be a valid positive value
  - Action: Enter an invalid party size (e.g., 0 or a negative number) and attempt to submit.
  - Expected: Submission is rejected with an error message; the reservation is not created.
- [X] CS-03: Past dates cannot be reserved
  - Action: Select a date earlier than today for a new reservation and attempt to submit.
  - Expected: Submission is blocked with a validation message.
- [ ] CS-04: Duplicate/conflicting reservation is prevented
  - Action: Create a reservation for a restaurant at a given date/time, then attempt to create another reservation for the same restaurant at the same date/time.
  - Expected: The second booking is rejected or the user is warned about the conflict; two identical bookings are not both created.
  - Bug Report:
    - Issue: Missing duplicate/conflict validation on reservation submission
    - Actual: After creating a reservation for The Golden Fork on Nov 15, 2026 at 19:00 (2 Guests), submitting the exact same reservation again succeeded with the normal "Reservation Confirmed" confirmation (View My Reservations / Make Another Reservation panel). No conflict warning or rejection appeared. "My Reservations" then showed "Upcoming (2)" with two identical entries: The Golden Fork · November 15, 2026 · 19:00 · 2 Guests.
- [X] CS-05: Invalid coupon code is rejected
  - Action: Enter a non-existent coupon code (e.g., "INVALID123") during reservation and apply it.
  - Expected: An error message is shown, no discount is applied, and the price remains unchanged.
- [X] CS-06: Review cannot be submitted without a rating
  - Action: Enter review text but leave the rating unselected, then submit.
  - Expected: Submission is blocked with a validation message; no review is created.
- [X] CS-07: Cancelled reservations are not listed as upcoming
  - Action: Cancel a reservation and re-open "My Reservations".
  - Expected: The cancelled booking no longer appears in the upcoming bookings view (or is clearly marked cancelled, not upcoming).

## Interaction
- [X] IX-01: Selecting a restaurant opens its detail view
  - Action: Click a restaurant card/name in the list.
  - Expected: The interface navigates (or switches) to that restaurant's detail page without errors.
- [X] IX-02: Confirmation feedback after booking
  - Action: Complete a valid reservation submission.
  - Expected: A visible success confirmation (message, toast, or status) appears after submission.
- [X] IX-03: Coupon applied gives visible feedback
  - Action: Apply a valid coupon code in the reservation form.
  - Expected: The interface visibly reflects the discount (e.g., updated price, "Discount applied" message).

## Content
- [X] CT-01: Restaurant details show correct cuisine and price info
  - Action: Open each restaurant's detail page from the default list.
  - Expected: Cuisine type and average price are displayed and match the restaurant's listed data (not empty/placeholder text).
- [X] CT-02: Reviews display rating and text together
  - Action: View the reviews section of a restaurant that has at least one submitted review.
  - Expected: Each review shows both the reviewer's text and its rating value.
