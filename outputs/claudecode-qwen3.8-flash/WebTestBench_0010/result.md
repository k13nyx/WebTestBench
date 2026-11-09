All checklist items are now executed. Cancelled booking shows a "Cancelled" badge in Past with no action buttons — FT-06 confirmed. Here is the complete result.

# Test Result

## Functionality
- [X] FT-01: Restaurant list is browsable with default data
  - Action: Open the application landing/browse page.
  - Expected: A list of at least 3 default restaurants is displayed, each showing its name, cuisine type, and average price.

- [X] FT-02: Restaurant details can be viewed
  - Action: Click/select one restaurant from the list to open its detail view.
  - Expected: The detail view shows that restaurant's cuisine type and average price (and address/hours if present).

- [X] FT-03: A table reservation can be created
  - Action: On a restaurant, select a future date, an available time slot, and a party size, then press the reserve/confirm button.
  - Expected: A reservation is created and appears in "My Reservations" / upcoming bookings with the chosen restaurant, date, time, and party size.

- [X] FT-04: Upcoming bookings are listed
  - Action: Navigate to the reservations/managing page after FT-03.
  - Expected: The upcoming reservations list shows the newly created booking plus any pre-existing default bookings, each with restaurant name, date, time, and party size.

- [X] FT-05: An existing reservation can be modified
  - Action: Open an upcoming reservation, change its date, time, and/or party size, and save.
  - Expected: The reservation is updated and the new values are reflected in the upcoming bookings list.

- [X] FT-06: An existing reservation can be canceled
  - Action: Use the Cancel action on an upcoming reservation and confirm.
  - Expected: The reservation is removed from the upcoming bookings list and can no longer be modified.

- [X] FT-07: A review and rating can be submitted for a visited restaurant
  - Action: On a restaurant the user has a past/completed reservation for, enter review text, choose a rating, and submit.
  - Expected: The review with its star rating (within 1–5) is saved and displayed on that restaurant's review section.

- [ ] FT-08: A valid discount coupon can be applied during reservation
  - Action: In the reservation flow, enter a valid default coupon code and apply it before confirming.
  - Expected: The discount is applied to the reservation total, and the confirmed booking reflects the discounted price.
  - Bug Report:
    - Issue: Missing reservation total / discounted price
    - Actual: Applying "WELCOME10" shows only a text indicator ("- 10% off", toast "Coupon Applied! 10% off your first reservation") and the booking card shows the label "Coupon applied: WELCOME10". No reservation total or monetary price is ever calculated or displayed anywhere in the form or in the confirmed booking, so the discount is never reflected as a discounted price.

## Constraint
- [X] CS-01: Reservation requires date, time, and party size
  - Action: Attempt to submit a reservation while leaving the date, time, or party size empty/unselected.
  - Expected: The reservation is rejected with a validation error; no booking is created.

- [X] CS-02: Past dates and past times cannot be booked
  - Action: Attempt to select a date earlier than today (or today's already-passed time slot) for a reservation.
  - Expected: The selection is rejected or unavailable, and submission with a past date/time fails validation.

- [X] CS-03: Party size must be a valid positive amount within limits
  - Action: Enter party size 0, a negative value, or a number exceeding the restaurant's stated maximum.
  - Expected: Submission fails with an error indicating an invalid party size.

- [X] CS-04: Invalid or expired coupons are rejected
  - Action: Enter a non-existent or expired coupon code and press Apply.
  - Expected: An error message such as "Invalid or expired coupon" is shown and no discount is applied to the total.

- [ ] CS-05: Reviews are limited to restaurants the user has visited
  - Action: Try to submit a review/rating for a restaurant for which the user has no completed reservation.
  - Expected: The review is rejected (control hidden or error message shown); no review is added for unvisited restaurants.
  - Bug Report:
    - Issue: Missing visit-gating on reviews
    - Actual: The "Write a Review" tab is available on every restaurant page, and a 4-star review was successfully submitted for The Golden Fork while the user's only reservation there was still upcoming (Nov 15, 2026; Past tab showed 0 completed bookings). The review was saved ("Review Submitted!", Reviews count went from 2 to 3) with no hidden control and no rejection error.

## Interaction
- [X] IX-01: Reservation success feedback is shown
  - Action: Complete a valid reservation (FT-03).
  - Expected: A clear confirmation is displayed (e.g., toast or "Reservation confirmed" message) and the user is returned to the reservations view.

- [ ] IX-02: Inline validation feedback appears on invalid input
  - Action: Trigger the errors from CS-01/CS-03 and observe the form.
  - Expected: Error messages appear adjacent to the offending field(s) and clear once the input is corrected; the form does not silently fail.
  - Bug Report:
    - Issue: No field-level inline validation
    - Actual: Submitting with empty Date/Time produced only a generic corner toast "Missing Information / Please fill in all required fields" that does not identify or sit adjacent to the offending field(s); DOM inspection found zero `aria-invalid="true"` attributes, no per-field error text, and no error-styled borders. With the required HTML5 fields (Name/Email/Phone) empty, there was no visible DOM error message at all — only a silent focus shift to the Name input.

- [X] IX-03: Cancellation requires confirmation before it takes effect
  - Action: Press Cancel on an upcoming reservation.
  - Expected: A confirmation dialog/prompt appears; choosing "No/Dismiss" leaves the booking intact, choosing "Yes/Confirm" removes it.

- [ ] IX-04: Modify form opens prefilled with current booking values
  - Action: Open the modify/edit screen for an existing reservation.
  - Expected: The date, time, and party-size controls are pre-filled with the reservation's current values (not blank defaults).
  - Bug Report:
    - Issue: Missing date control in Modify dialog
    - Actual: The "Modify Reservation" dialog pre-filled Time ("19:00") and Party Size ("4 Guests") correctly, but it contains only "New Time" and "Party Size" controls — there is no date control at all, so the reservation's date cannot be viewed or changed in the modify flow.

## Content
- [X] CT-01: Restaurant content is relevant and complete
  - Action: Inspect the restaurant list and detail views.
  - Expected: Every entry shows a real cuisine type and an average price (no empty fields, no "lorem ipsum"/placeholder text); any images are restaurant/food-related.

- [X] CT-02: Booking records display exact values the user selected
  - Action: Compare the upcoming-bookings entry created in FT-03 against the values submitted.
  - Expected: Restaurant name, date, time, party size (and applied coupon discount, if any) all match exactly what was entered — no mismatched or truncated data.

- [X] CT-03: Reviews display text and rating faithfully
  - Action: After FT-07, view the restaurant's review section.
  - Expected: The submitted review text and the correct number of stars are shown as entered; ratings are displayed consistently with the restaurant's average rating.