# Test Result

## Functionality
- [X] FT-01: Restaurant list is browsable from the landing page
  - Action: Open the app's home page (restaurant listing).
  - Expected: At least 3 default restaurant cards render, each with a restaurant name visible; no error state.

- [X] FT-02: Restaurant detail page shows cuisine type and average price
  - Action: Open R1's detail page.
  - Expected: Page shows R1's name, a non-empty cuisine type (e.g., "Italian"), and a non-empty average price value (e.g., "$$" or "25").

- [X] FT-03: User can reserve a table with date, time, and party size
  - Action: On R1's detail page, select a future date, a time slot, party size = 2, then click "Reserve"/"Book".
  - Expected: A reservation is created and appears under My Reservations / Upcoming with R1, that date, that time, party size 2.

- [X] FT-04: Upcoming bookings are viewable
  - Action: Go to the "My Reservations"/"Upcoming" page.
  - Expected: All current bookings are listed, each showing restaurant name, date, time, and party size; the FT-03 booking is present.

- [X] FT-05: User can modify an existing reservation
  - Action: On the FT-03 upcoming booking, click "Modify", change party size to 4, save.
  - Expected: Booking list shows party size 4 with date/time unchanged; value is still 4 after page reload.

- [X] FT-06: User can cancel a reservation
  - Action: Click "Cancel" on an upcoming booking and confirm.
  - Expected: Booking is removed from the Upcoming list or shown with status "Canceled".

- [ ] FT-07: User can submit a rating and review for a visited restaurant
  - Action: In My Reservations open the default past/completed booking, click "Write Review", select 4 stars, enter "Great food and service.", submit.
  - Expected: Review is saved and appears in that restaurant's Reviews section with 4/5 stars, the review text, and the reviewer name.
  - Bug Report:
    - Issue: Missing Default Data / Missing Entry Point (test not executable as specified)
    - Actual: My Reservations loads with "Upcoming (0)" and "Past (0)" — the app ships no default past/completed booking. The Past tab's only entry is the booking cancelled during FT-06, shown with status "Cancelled" and offering no "Write Review" action (only "Modify"/"Cancel" exist on upcoming cards). The specified action (open default past booking → "Write Review") is therefore impossible. Note: the review feature itself works via the "Write a Review" tab on a detail page (submitted review rendered as 4 filled + 1 muted star, name "Jane Doe", text "Great food and service."), but it is not reachable from, or gated on, a completed visit.

- [ ] FT-08: Valid coupon applies a discount to the reservation
  - Action: Start a new reservation on R1 and enter the valid coupon code listed by the app (e.g., in its coupon/deals display), then complete the booking.
  - Expected: Reservation is created and its total/price reflects the coupon discount (discount amount or reduced total shown).
  - Bug Report:
    - Issue: Missing Price/Discount Display
    - Actual: Reservation was created with WELCOME10 and the booking card shows only "Coupon applied: WELCOME10". No discount amount, subtotal, or total/price is displayed anywhere in the app (reservation form, confirmation panel, or My Reservations card), so the reduced total cannot be verified. The only "$" text on the reservations page is the restaurant's "$$$$" price-range label.

## Constraint
- [ ] CS-01: Reservation cannot be created with missing or invalid required fields
  - Action: Open R1's reservation form, leave date/time/party size unset (or set party size to 0) and submit.
  - Expected: Submit is blocked with a validation message; no booking is added to Upcoming.
  - Bug Report:
    - Issue: Missing Validation Feedback
    - Actual: Clicking "Confirm Reservation" with date unset and Name/Email/Phone empty produced no validation message — no inline errors, no toast (notification region empty), and the form remained unchanged. Upcoming stayed at (0), so submission was blocked, but no message was shown to the user.

- [X] CS-02: Reservation cannot be made for a past date
  - Action: Attempt to reserve R1 for 2026-11-07 (yesterday).
  - Expected: No booking is created — the past date is unselectable, or an error message appears on submit.

- [X] CS-03: Invalid coupon code is rejected
  - Action: In the reservation form enter "INVALIDCODE123" and apply it.
  - Expected: Error message shown (e.g., "Invalid coupon"); no discount applied; booking can still be made at full price.

- [ ] CS-04: Review cannot be submitted without a rating
  - Action: Open a review form, leave the star rating unselected (and/or the comment empty), submit.
  - Expected: Submission blocked with a validation message; no new review appears in the Reviews section.
  - Bug Report:
    - Issue: Missing Validation Feedback
    - Actual: Clicking "Submit Review" with no rating, empty name, empty date of visit and empty comment produced no validation message (notification region empty, no inline errors). The review was not saved (review count stayed at "Reviews (1)"), so submission was blocked, but the user receives no feedback about why.

- [ ] CS-05: Review is only allowed for restaurants the user has visited
  - Action: Open the detail page of a restaurant with no past/completed reservation in the account and try to submit a review.
  - Expected: No review is saved — the review form is unavailable/disabled, or submission is blocked with a message about visiting first.
  - Bug Report:
    - Issue: Missing Business-Rule Enforcement
    - Actual: On Trattoria Bella (no reservation history at all — My Reservations showed Past (0) initially), the "Write a Review" tab was fully enabled. Submitting 4 stars, name "Jane Doe", date of visit 2026-11-01 and text "Great food and service." succeeded with the toast "Review Submitted! Thank you for sharing your experience."; the review count went from "Reviews (1)" to "Reviews (2)" and the review persisted. No visit requirement or warning was enforced.

## Interaction
- [X] IX-01: Clicking a restaurant opens its own detail page
  - Action: Click the second restaurant card in the list.
  - Expected: Detail page for that exact restaurant opens (its name matches the card clicked).

- [X] IX-02: Success confirmation appears after a reservation is created
  - Action: Complete a new valid reservation on R1.
  - Expected: A confirmation message/banner (e.g., "Reservation confirmed") is displayed immediately without leaving the page in an error state.

- [ ] IX-03: Applying a coupon updates the displayed price immediately
  - Action: In the reservation form, note the total, then apply the valid coupon code before submitting.
  - Expected: Total/price display updates right away to show the discount (no submission needed).
  - Bug Report:
    - Issue: No Price/Total Displayed
    - Actual: The reservation form has no total/price element at all (before or after applying a coupon). Applying WELCOME10 only added a "WELCOME10 - 10% off" chip next to the coupon field plus a "Coupon Applied! 10% off your first reservation" toast; no total/price value exists to update.

- [X] IX-04: Cancelling requires confirmation before the booking is removed
  - Action: Click "Cancel" on an upcoming booking, then dismiss/decline the prompt.
  - Expected: A confirmation prompt appears first, and declining it leaves the booking intact in Upcoming.

## Content
- [X] CT-01: Listing cards contain real, relevant restaurant data
  - Action: Inspect every restaurant card on the listing page.
  - Expected: Each card shows a real name, cuisine type, and average price — no empty values, "N/A", "undefined", or placeholder/lorem text.

- [X] CT-02: Restaurant imagery renders and is topic-relevant
  - Action: Load the listing page and two restaurant detail pages.
  - Expected: All images/icons load (no broken-image icon) and depict restaurants/food/dining content.

- [X] CT-03: Detail page data matches the listing card for the same restaurant
  - Action: Compare R1's listing card with R1's detail page.
  - Expected: Name, cuisine type, and average price are identical on both views.
