# Test Result

## Functionality
- [X] FT-01: User can browse the list of restaurants
  - Action: Open the restaurant listing page.
  - Expected: A list of restaurants (from default data) is displayed with each restaurant's name visible.
  - Verified: 6 restaurants displayed (The Golden Fork, Sakura Garden, Trattoria Bella, Ember & Smoke, Spice Route, Ocean Blue), each with name, cuisine · price, rating, and neighborhood ("6 restaurants available" counter shown).

- [X] FT-02: User can view restaurant details including cuisine type and average price
  - Action: Click on any restaurant in the list.
  - Expected: A details page opens showing the restaurant's name, cuisine type (e.g., "Italian", "Japanese"), and average price (e.g., "$$"/"$30 per person").
  - Verified: Trattoria Bella detail page shows heading "Trattoria Bella", cuisine "Italian", price "$$", plus address, rating (4.0), and features.

- [X] FT-03: User can create a reservation by selecting date, time, and party size
  - Action: On a restaurant's page, select a valid future date, a time slot, and a party size, then click the "Reserve" button.
  - Expected: The reservation is created and appears in the user's reservations list with the selected restaurant, date, time, and party size.
  - Verified: Reservation created at Trattoria Bella for Nov 15, 2026, 19:00, 4 Guests; appeared in My Reservations with exactly those values.

- [X] FT-04: User can view their upcoming reservations
  - Action: Navigate to the "My Reservations" (or equivalent) page.
  - Expected: All active future reservations are listed, each showing restaurant name, date, time, party size, and status.
  - Verified: "My Reservations" page lists reservations with restaurant name, cuisine · price, status "Upcoming", date, time, party size, and neighborhood, with Upcoming/Past tabs and counts.

- [X] FT-05: User can cancel a reservation
  - Action: On an upcoming reservation, click the "Cancel" button and confirm.
  - Expected: The reservation status changes to "Cancelled" (or is removed from upcoming bookings) and no longer appears as an active upcoming booking.
  - Verified: Cancelling The Golden Fork reservation via confirm dialog removed it from Upcoming (2→1) and it appears in the Past tab with status "Cancelled".

- [X] FT-06: User can modify a reservation
  - Action: On an upcoming reservation, click "Modify", change the date, time, or party size, and save.
  - Expected: The reservation is updated and the reservations list shows the new date/time/party size, replacing the old values.
  - Verified: Modify dialog changed time 19:00→18:30 and party size 4→6; after "Save Changes" the card shows November 15, 2026, 18:30, 6 Guests, with toast "Reservation Updated — Your reservation has been modified successfully."

- [X] FT-07: User can apply a valid discount coupon during reservation
  - Action: During the reservation flow, enter a valid coupon code (from default data) in the coupon field and apply it before confirming.
  - Expected: The coupon is accepted and the reservation total/price reflects the discounted amount.
  - Verified: WELCOME10 accepted with feedback "Coupon Applied! 10% off your first reservation" and inline "WELCOME10 - 10% off" badge; the reservation was created and the reservations list shows "Coupon applied: WELCOME10" on the booking, reflecting the discount. (Note: the app expresses the discount as a percentage/badge on the reservation rather than a monetary total; no dollar total is displayed anywhere in the reservation flow.)

- [X] FT-08: User can submit a review with a rating for a restaurant
  - Action: On a restaurant's page, select a star rating (e.g., 4 of 5) and enter short review text, then submit.
  - Expected: The review is saved and appears in the restaurant's reviews section with the entered text and rating.
  - Verified: 4-star review with text "Great sushi and lovely ambiance." submitted at Sakura Garden; toast "Review Submitted!"; the review appears in the Reviews section (author "Test Reviewer", "Visited Nov 1, 2026", entered text, 4 of 5 stars displayed).

- [X] FT-09: User can complete a reservation without applying a coupon
  - Action: Create a reservation leaving the coupon field empty.
  - Expected: The reservation is created successfully at the normal (undiscounted) amount.
  - Verified: Reservation created at Trattoria Bella with empty coupon field — confirmed successfully at the normal undiscounted state (no coupon/discount badge on the booking, unlike the coupon reservation which shows "Coupon applied: WELCOME10").

## Constraint
- [X] CS-01: Reservation cannot be submitted with missing required fields
  - Action: On the reservation form, leave date, time, or party size empty and click "Reserve".
  - Expected: The reservation is not created; a validation message indicates the required missing fields.
  - Verified: With date/time empty, clicking "Confirm Reservation" shows toast "Missing Information — Please fill in all required fields." and no reservation is created (focus moves to first invalid field).

- [X] CS-02: Reservation cannot use a past date
  - Action: Attempt to create a reservation with a date earlier than today.
  - Expected: The reservation is not created; an error message indicates the date must be in the future (or a past date cannot be selected).
  - Verified: The date picker disables all past dates — in November 2026, days 1–8 (before today, Nov 9, 2026) are disabled, and every date in October 2026 is disabled, so a past date cannot be selected.

- [X] CS-03: Party size must be a positive valid number
  - Action: Attempt to submit a reservation with party size 0 or empty.
  - Expected: The reservation is not created; a validation message indicates a valid party size is required.
  - Verified: The party size dropdown only offers 1–10 Guests; 0 or empty cannot be selected, so a reservation with an invalid party size cannot be created. The constraint is enforced at input level (in addition, the form shows "Please fill in all required fields" validation for missing required fields).

- [X] CS-04: Invalid coupon code is rejected
  - Action: During the reservation flow, enter a fake/expired coupon code (e.g., "INVALID123") and apply it.
  - Expected: The coupon is not applied; an error message indicates the code is invalid or expired, and the price remains undiscounted.
  - Verified: "INVALID123" → toast "Invalid Coupon — The coupon code you entered is not valid."; no discount applied; the coupon could then be corrected and applied.

- [ ] CS-05: Review cannot be submitted without a rating
  - Action: On a restaurant's page, leave the rating unselected (and/or review text empty) and click submit.
  - Expected: The review is not saved; a validation message indicates a rating (and/or text) is required.
  - Bug Report:
    - Issue: Missing Validation Message (silent form failure)
    - Actual: On Sakura Garden's "Write a Review" form, with name ("Test Reviewer") and review text ("Great sushi and lovely ambiance.") filled but the star rating unselected, clicking "Submit Review" produced no feedback whatsoever — no toast, no inline error, no new DOM content (verified via repeated polling over 1s and a full before/after page-text diff). The review is correctly not saved (review count stays unchanged), but the user receives no validation message indicating a rating is required; the button appears simply non-functional. (By contrast, the reservation form does show a "Please fill in all required fields" validation toast for the equivalent scenario.)

- [X] CS-06: Cancelled reservation cannot be modified
  - Action: Attempt to modify a reservation that has already been cancelled.
  - Expected: No modification is possible; the "Modify" action is unavailable or returns an error stating the reservation is cancelled.
  - Verified: The cancelled reservation (The Golden Fork, status "Cancelled") appears in the Past tab with no "Modify" or "Cancel" buttons rendered; the Modify action is unavailable.

## Interaction
- [X] IX-01: Success confirmation shown after reservation is created
  - Action: Complete a valid reservation.
  - Expected: A confirmation message (toast/banner) appears stating the reservation was created successfully, with the booking summary.
  - Verified: Toast "Reservation Confirmed! Your table at Trattoria Bella is booked for November 15, 2026 at 19:00." plus an in-page confirmation panel ("Reservation Confirmed! Check your email for confirmation details.") with "View My Reservations" / "Make Another Reservation" actions.

- [X] IX-02: Confirmation feedback shown after cancellation
  - Action: Cancel an upcoming reservation and confirm the action.
  - Expected: A message appears confirming the reservation was cancelled; the reservations list updates immediately without a full page reload error.
  - Verified: Toast "Reservation Cancelled — Your reservation has been cancelled."; the reservations list updated immediately in-place (Upcoming count 2→1, Past 0→1) with no page reload or error.

- [X] IX-03: Coupon field provides immediate feedback when applied
  - Action: Type a coupon code and click "Apply" in the reservation flow.
  - Expected: Inline feedback appears next to the coupon field (success with discount amount for a valid code, error for an invalid one) without losing already-entered reservation details.
  - Verified: Invalid code → immediate error ("Invalid Coupon — The coupon code you entered is not valid."); valid code WELCOME10 → immediate success ("Coupon Applied! 10% off your first reservation" with inline "WELCOME10 - 10% off" badge). In both cases the already-entered date (Nov 20, 2026), time (19:30), party size (2 Guests), name, email, and phone were preserved.

- [X] IX-04: Submitted review and rating update the restaurant's display immediately
  - Action: Submit a review with a rating for a restaurant.
  - Expected: The new review appears in the reviews list without requiring a page reload, and the restaurant's average rating updates to include the new rating.
  - Verified: After submitting a 4-star review at Sakura Garden (SPA state update, no reload), the Reviews tab count changed from (1) to (2) immediately, the new review appeared in the list, and the restaurant's average rating updated from 5.0 (1) to 4.5 (2), correctly including the new rating.

## Content
- [X] CT-01: Restaurant list entries contain relevant, consistent information
  - Action: Browse the restaurant list and open at least three restaurant detail pages.
  - Expected: Each restaurant displays a real-sounding name, a cuisine type, and an average price; values match between the list view and the detail view for the same restaurant.
  - Verified: Opened three detail pages — Trattoria Bella (list "Italian · $$" / detail "Italian" + "$$"), The Golden Fork (list "French · $$$$" / detail "French" + "$$$$"), Sakura Garden (list "Japanese · $$$" / detail "Japanese" + "$$$"). All names are realistic, and cuisine/price values match between list and detail views.

- [X] CT-02: Restaurant images are relevant to the restaurant theme
  - Action: View restaurant cards and detail pages.
  - Expected: All displayed images are food/restaurant/interior photos relevant to each restaurant; no broken images or unrelated placeholders.
  - Verified: All 6 restaurant card images and detail hero images load successfully (naturalWidth 800, no broken images), have alt text matching restaurant names, and use cuisine-appropriate Unsplash food/restaurant photography (e.g., sushi for the Japanese Sakura Garden, grilled meat for the BBQ Ember & Smoke, pasta/Italian kitchen for Trattoria Bella, restaurant interior for The Golden Fork).

- [X] CT-03: Reviews and ratings displayed are relevant to their restaurant
  - Action: Open a restaurant's reviews section and read existing reviews (from default data).
  - Expected: Each review contains plausible text about the dining experience and a rating (1–5 scale); no empty reviews, spam, or reviews belonging to another restaurant.
  - Verified: Reviews are restaurant-appropriate and plausible — Sakura Garden (Japanese/omakase): Emily K. "The omakase was incredible. Each piece of sushi was a work of art…"; The Golden Fork (French, tasting menu): Sarah M. "…The tasting menu was a journey through flavors…", James L. "Beautiful ambiance and excellent food…"; Trattoria Bella (Italian): Michael R. "Authentic Italian flavors… The pasta is made fresh daily…". All display 1–5 scale star ratings; no empty or spam reviews, and no cross-restaurant content.
