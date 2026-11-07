# Test Checklist

**Preconditions:** Desktop browser. Today = 2026-11-08. Use only the app's default restaurants, bookings, and coupons — do not create new restaurants. "R1" = the first restaurant card in the default list.

## Functionality
- [ ] FT-01: Restaurant list is browsable from the landing page
  - Action: Open the app's home page (restaurant listing).
  - Expected: At least 3 default restaurant cards render, each with a restaurant name visible; no error state.

- [ ] FT-02: Restaurant detail page shows cuisine type and average price
  - Action: Open R1's detail page.
  - Expected: Page shows R1's name, a non-empty cuisine type (e.g., "Italian"), and a non-empty average price value (e.g., "$$" or "25").

- [ ] FT-03: User can reserve a table with date, time, and party size
  - Action: On R1's detail page, select a future date, a time slot, party size = 2, then click "Reserve"/"Book".
  - Expected: A reservation is created and appears under My Reservations / Upcoming with R1, that date, that time, party size 2.

- [ ] FT-04: Upcoming bookings are viewable
  - Action: Go to the "My Reservations"/"Upcoming" page.
  - Expected: All current bookings are listed, each showing restaurant name, date, time, and party size; the FT-03 booking is present.

- [ ] FT-05: User can modify an existing reservation
  - Action: On the FT-03 upcoming booking, click "Modify", change party size to 4, save.
  - Expected: Booking list shows party size 4 with date/time unchanged; value is still 4 after page reload.

- [ ] FT-06: User can cancel a reservation
  - Action: Click "Cancel" on an upcoming booking and confirm.
  - Expected: Booking is removed from the Upcoming list or shown with status "Canceled".

- [ ] FT-07: User can submit a rating and review for a visited restaurant
  - Action: In My Reservations open the default past/completed booking, click "Write Review", select 4 stars, enter "Great food and service.", submit.
  - Expected: Review is saved and appears in that restaurant's Reviews section with 4/5 stars, the review text, and the reviewer name.

- [ ] FT-08: Valid coupon applies a discount to the reservation
  - Action: Start a new reservation on R1 and enter the valid coupon code listed by the app (e.g., in its coupon/deals display), then complete the booking.
  - Expected: Reservation is created and its total/price reflects the coupon discount (discount amount or reduced total shown).

## Constraint
- [ ] CS-01: Reservation cannot be created with missing or invalid required fields
  - Action: Open R1's reservation form, leave date/time/party size unset (or set party size to 0) and submit.
  - Expected: Submit is blocked with a validation message; no booking is added to Upcoming.

- [ ] CS-02: Reservation cannot be made for a past date
  - Action: Attempt to reserve R1 for 2026-11-07 (yesterday).
  - Expected: No booking is created — the past date is unselectable, or an error message appears on submit.

- [ ] CS-03: Invalid coupon code is rejected
  - Action: In the reservation form enter "INVALIDCODE123" and apply it.
  - Expected: Error message shown (e.g., "Invalid coupon"); no discount applied; booking can still be made at full price.

- [ ] CS-04: Review cannot be submitted without a rating
  - Action: Open a review form, leave the star rating unselected (and/or the comment empty), submit.
  - Expected: Submission blocked with a validation message; no new review appears in the Reviews section.

- [ ] CS-05: Review is only allowed for restaurants the user has visited
  - Action: Open the detail page of a restaurant with no past/completed reservation in the account and try to submit a review.
  - Expected: No review is saved — the review form is unavailable/disabled, or submission is blocked with a message about visiting first.

## Interaction
- [ ] IX-01: Clicking a restaurant opens its own detail page
  - Action: Click the second restaurant card in the list.
  - Expected: Detail page for that exact restaurant opens (its name matches the card clicked).

- [ ] IX-02: Success confirmation appears after a reservation is created
  - Action: Complete a new valid reservation on R1.
  - Expected: A confirmation message/banner (e.g., "Reservation confirmed") is displayed immediately without leaving the page in an error state.

- [ ] IX-03: Applying a coupon updates the displayed price immediately
  - Action: In the reservation form, note the total, then apply the valid coupon code before submitting.
  - Expected: Total/price display updates right away to show the discount (no submission needed).

- [ ] IX-04: Cancelling requires confirmation before the booking is removed
  - Action: Click "Cancel" on an upcoming booking, then dismiss/decline the prompt.
  - Expected: A confirmation prompt appears first, and declining it leaves the booking intact in Upcoming.

## Content
- [ ] CT-01: Listing cards contain real, relevant restaurant data
  - Action: Inspect every restaurant card on the listing page.
  - Expected: Each card shows a real name, cuisine type, and average price — no empty values, "N/A", "undefined", or placeholder/lorem text.

- [ ] CT-02: Restaurant imagery renders and is topic-relevant
  - Action: Load the listing page and two restaurant detail pages.
  - Expected: All images/icons load (no broken-image icon) and depict restaurants/food/dining content.

- [ ] CT-03: Detail page data matches the listing card for the same restaurant
  - Action: Compare R1's listing card with R1's detail page.
  - Expected: Name, cuisine type, and average price are identical on both views.