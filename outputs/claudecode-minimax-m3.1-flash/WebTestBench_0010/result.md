All checklist items have been exercised. Here is the final report.

# Test Result

## Functionality

- [X] FT-01: Restaurant list page displays the application's default restaurants
  - Action: Open the app home page / restaurant browse list
  - Expected: A list of the pre-existing default restaurants is shown, each with a name and enough info to identify it (no empty list, no error)

- [X] FT-02: Restaurant detail page shows cuisine type and average price
  - Action: Open the details of any default restaurant from the list
  - Expected: Detail page displays the restaurant's cuisine type and average price (e.g., "$$" / "$25 per person") as non-empty values
  - Note: Detail page renders the cuisine ("French") and a price tier ("$$$$") for all 6 restaurants; the app stores no per-person dollar amount.

- [X] FT-03: A table reservation can be created with date, time, and party size
  - Action: On a restaurant detail page, select a date, a time slot, and a party size, then submit the reservation form
  - Expected: The reservation is accepted and a confirmation with the chosen date, time, and party size is shown
  - Note: Reservation was accepted (toast "Reservation Confirmed! Your table at The Golden Fork is booked for November 15, 2026 at 19:00." + confirmation panel). The party size is not part of the toast/panel text itself; it is confirmed in the resulting booking card in "My Reservations" (4 Guests).

- [X] FT-04: Created reservations appear in the user's upcoming bookings
  - Action: Navigate to the "My Reservations" / upcoming bookings section
  - Expected: The newly created reservation is listed with its restaurant name, date, time, and party size

- [X] FT-05: A reservation can be canceled
  - Action: In the reservations list, click "Cancel" on one of the user's reservations and confirm
  - Expected: The reservation's status changes to canceled and it is no longer counted/shown as an upcoming confirmed booking
  - Note: Confirm dialog shown; after confirming, toast "Reservation Cancelled", Upcoming count went 2 → 1, and the item moved to the "Past" tab with status badge "Cancelled".

- [X] FT-06: A reservation can be modified
  - Action: Click "Modify" on an existing reservation, change the date, time, and/or party size, and save
  - Expected: The reservation is updated and the reservations list (and details) show the new date, time, and party size
  - Note: Time changed 19:00 → 18:00 and party size 4 → 6; list card and stored record updated, toast "Reservation Updated". The modify dialog only exposes Time and Party Size (no date field) — the date field was therefore unchanged.

- [X] FT-07: A review with a rating and text can be submitted for a restaurant
  - Action: Open a restaurant detail page, select a star rating, type review text, and submit
  - Expected: The review is accepted and appears on that restaurant's page

- [ ] FT-08: A valid discount coupon can be applied during the reservation process
  - Action: In the reservation flow, enter a valid coupon code and apply it before confirming
  - Expected: The reservation is created and the coupon discount is reflected in the booking cost shown to the user
  - Bug Report:
    - Issue: Missing Booking Cost / Discount Amount (Incomplete Feature)
    - Actual: Coupon "WELCOME10" was accepted ("Coupon Applied! 10% off your first reservation", chip "WELCOME10 - 10% off") and the reservation was created, but no booking cost is shown anywhere: the reservation form renders no subtotal/total line, and the "My Reservations" card only shows "Coupon applied: WELCOME10" with no amount. The stored reservation record (localStorage `tablespot_reservations`) contains `couponCode` but no price, discount or total field, so the discount is never reflected in a booking cost.

## Constraint

- [X] CS-01: Reservation cannot be submitted with required fields empty
  - Action: On the reservation form, leave the required date/time/party size fields blank and submit
  - Expected: A validation error is shown and no reservation is created
  - Note: Submitting with empty date/time showed the toast "Missing Information — Please fill in all required fields." and created no reservation.

- [X] CS-02: Party size must be a positive valid number
  - Action: Enter an invalid party size (0, negative, or non-numeric text) and submit the reservation form
  - Expected: The form rejects the input with a clear error message and no reservation is created
  - Note: Party size is a restricted dropdown offering only "1 Guest" … "10 Guests", so 0, negative or non-numeric values cannot be entered or submitted at all; no invalid reservation was created. The rejection is enforced at the input control rather than by a validation message.

- [X] CS-03: Reservation date cannot be in the past
  - Action: Select a date earlier than today in the reservation form and submit
  - Expected: Submission is blocked with an error indicating the date is invalid/past, and no reservation is created
  - Note: The calendar disables all days before today (Nov 1–7, 2026 disabled) and every day of the previous month (October 2026 fully disabled), so a past date cannot be selected and no past-dated reservation was created. As with CS-02 the guard is at input level, so no error message is shown (none is reachable).

- [X] CS-04: An invalid coupon code does not apply a discount
  - Action: Enter a non-existent or expired coupon code during the reservation flow and apply it
  - Expected: An error states the coupon is invalid/not applicable, no discount is applied, and the reservation total remains unchanged

- [ ] CS-05: The same restaurant, date, and time slot cannot be double-booked
  - Action: Create a reservation for a restaurant/date/time, then attempt to create another reservation for the same restaurant, date, and time slot
  - Expected: The second attempt is blocked with a message about the unavailable slot, and only one reservation exists for that slot
  - Bug Report:
    - Issue: Double-Booking Not Prevented (Missing Validation)
    - Actual: A second reservation for The Golden Fork, 2026-11-15, 19:00 was submitted and was accepted with the toast "Reservation Confirmed! Your table at The Golden Fork is booked for November 15, 2026 at 19:00." — no "slot unavailable" message appeared. Two confirmed reservations for the identical restaurant/date/time slot now exist (localStorage `tablespot_reservations`: `res_1794062992012` and `res_1794063020508`, both restaurantId 1, 2026-11-15, 19:00, status "confirmed").

## Interaction

- [X] IX-01: Clicking a restaurant in the list opens its detail page
  - Action: Click a restaurant name/card in the restaurant list
  - Expected: The app navigates to that restaurant's detail page showing its cuisine, average price, and reservation option

- [X] IX-02: A success message is shown after creating a reservation
  - Action: Complete a valid reservation submission and observe the page
  - Expected: A success/confirmation message appears (e.g., toast or banner) indicating the reservation was created

- [ ] IX-03: Applying a coupon updates the total before the reservation is confirmed
  - Action: Type a valid coupon code and click "Apply" in the reservation form
  - Expected: The discount and new total update immediately on the page, without requiring the reservation to be submitted first
  - Bug Report:
    - Issue: Total Not Displayed (Incomplete Feature)
    - Actual: The discount does update immediately (toast "Coupon Applied! 10% off your first reservation" and chip "WELCOME10 - 10% off" appear right after clicking Apply, before submission), but no total or new total is rendered on the page — the reservation form shows no price/summary line at all, so the user cannot see a discounted total.

## Content

- [X] CT-01: Restaurant list and detail page show consistent cuisine and price
  - Action: Compare the cuisine type and average price shown in the restaurant list with those on the clicked restaurant's detail page
  - Expected: Values match exactly for the same restaurant, with no blank or placeholder ("N/A", "TBD") entries for default restaurants
  - Note: Verified for all 6 restaurants — list vs. detail: The Golden Fork French/$$$$, Sakura Garden Japanese/$$$, Trattoria Bella Italian/$$, Ember & Smoke American BBQ/$$, Spice Route Indian/$$, Ocean Blue Seafood/$$$. No "N/A"/"TBD"/"lorem" placeholders. (Separate observation, outside this item's scope: list ratings are static and do not match the computed detail ratings — e.g. list 4.8 vs. detail 4.5 for The Golden Fork, list 4.6 vs. detail 5.0 for Sakura Garden.)

- [ ] CT-02: Reservation confirmation and summary show the correct booking details
  - Action: Create a reservation for a specific restaurant, date, time, and party size, then open the reservation summary in the reservations list
  - Expected: The restaurant name, date, time, party size, and total match what was entered in the form
  - Bug Report:
    - Issue: Missing Total in Reservation Summary (Incomplete Feature)
    - Actual: The "My Reservations" card correctly shows the entered values (The Golden Fork · French · $$$$, November 15, 2026, 19:00, 2 Guests, Downtown, status Upcoming), but no total/cost is displayed on the card or anywhere in the reservation detail, and the stored reservation record contains no total field — so the total required by the expectation cannot be displayed or matched.

- [X] CT-03: Submitted reviews display reviewer, rating, and review text
  - Action: Submit a review with a rating and text, then view the reviews section of that restaurant
  - Expected: The review appears with its star rating, review text, and author, and the restaurant's average rating reflects it
  - Note: Review appeared as "QA Reviewer — Visited Nov 5, 2026" with 4 stars and the submitted text; the tab count changed Reviews (2) → Reviews (3) and the restaurant average rating updated from 4.5 to 4.3 with count (3).

- [ ] CT-04: Discount and total amounts are displayed accurately and no placeholder text is shown
  - Action: Apply a known coupon on a reservation and read the displayed discount and total
  - Expected: The displayed discount matches the coupon's stated value and the total equals the pre-discount amount minus the discount; no "lorem ipsum", "TBD", or empty content appears anywhere in the restaurant, reservation, or review views
  - Bug Report:
    - Issue: Discount Amount / Total Not Displayed (Incomplete Feature)
    - Actual: The coupon percentage itself is displayed accurately (WELCOME10 → toast "10% off your first reservation" and chip "- 10% off"), and no "lorem ipsum"/"TBD"/"N/A" placeholder text was found on the restaurant list, any of the 6 detail pages, the reservation pages or the review views. However, no discount amount and no pre-discount/total amounts are rendered anywhere (form, confirmation, reservations card, stored record), so the "total equals pre-discount minus discount" condition cannot be satisfied or verified — the app implements no monetary price model, showing only a "$$"–"$$$$" price tier.

---

**Summary:** 13 passed, 5 failed (FT-08, CS-05, IX-03, CT-02, CT-04). The four total/cost failures share one root cause: the application has no monetary price model, so no subtotal, discount amount or total is ever rendered. CS-05 is an independent defect — double-booking of the same restaurant/date/time slot is not validated. Additional observations not covered by the checklist: the Modify dialog offers no date field, the reservation confirmation text omits the party size, and list-page ratings are static and disagree with the computed detail-page ratings.