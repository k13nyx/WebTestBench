Submission blocked with "Missing Information — Please fill in all required fields." — **CS-01 ✓** confirmed robustly (no reservation created in either variant).

All checklist items have been executed. Here is the full checklist with updated statuses:

# Test Result

## Functionality
- [X] FT-01: Browse the list of restaurants.
  - Action: Open the application's home/browse page.
  - Expected: A list of default restaurants is displayed, each entry showing a restaurant name.
- [X] FT-02: Open a restaurant's detail page.
  - Action: Click a restaurant entry in the restaurant list.
  - Expected: The detail page for that restaurant opens and shows its information.
- [X] FT-03: Create a table reservation with date, time, and party size.
  - Action: On a restaurant's booking form, select a future date, a time, and party size 2, then click the "Reserve" button.
  - Expected: The reservation is created and appears in the reservations list.
- [X] FT-04: View upcoming reservations.
  - Action: Navigate to the "My Reservations" page.
  - Expected: All upcoming bookings are listed with restaurant name, date, time, and party size.
- [X] FT-05: Cancel a reservation.
  - Action: Click "Cancel" on an upcoming reservation and confirm the cancellation.
  - Expected: The reservation is no longer listed as upcoming (removed or shown as cancelled).
- [X] FT-06: Modify a reservation.
  - Action: Click "Modify" on an upcoming reservation, change the time and party size, then save.
  - Expected: The reservation is updated and shows the new time and party size.
- [X] FT-07: Submit a review with rating and text.
  - Action: Open a restaurant's review form, select a 4-star rating, enter review text (e.g., "Great food"), click "Submit Review".
  - Expected: The review is submitted and appears in the restaurant's reviews section.
- [X] FT-08: Apply a discount coupon during reservation.
  - Action: In the coupon field on the booking form, enter a valid coupon code and click "Apply", then complete the reservation.
  - Expected: The coupon is accepted and the reservation is created with the discounted price.

## Constraint
- [X] CS-01: Reservation cannot be submitted with missing required fields.
  - Action: Open the booking form and click "Reserve" without selecting date, time, or party size.
  - Expected: Submission is blocked with a validation error; no reservation is created.
- [ ] CS-02: Past dates cannot be used for reservations.
  - Action: Select a past date (e.g., yesterday) on the booking form and submit; repeat in the Modify form.
  - Expected: Submission is blocked with a validation error; no reservation is created or updated.
  - Bug Report:
    - Issue: Missing Validation Flow / Missing Form Field — past-date submission path cannot be exercised as specified
    - Actual: On the booking form's date picker, all past dates are rendered as disabled grid cells (e.g., gridcell "7" for yesterday is `[disabled]` with no pointer cursor; a forced click has no effect — the Date button remains "Select date" and no cell becomes selected). Consequently no past date can ever be submitted and the expected submission-level validation error is never produced. The "Modify Reservation" dialog contains only "New Time" and "Party Size" comboboxes and "Save Changes" — there is no date field at all, so the required "repeat in the Modify form" check cannot be performed (a reservation's date cannot be inspected or changed to a past date there).
- [X] CS-03: Invalid coupon codes are rejected.
  - Action: Enter an invalid code (e.g., "FAKE-CODE-999") in the coupon field and click "Apply".
  - Expected: An error message is shown and the displayed price remains unchanged.
- [X] CS-04: A rating is required to submit a review.
  - Action: Open the review form, leave the rating unselected, enter review text, click "Submit Review".
  - Expected: Submission is blocked with a validation error; no review is created.

## Interaction
- [X] IX-01: Confirmation feedback after creating a reservation.
  - Action: Complete a reservation as in FT-03.
  - Expected: A success confirmation message (e.g., "Reservation confirmed") is displayed.
- [X] IX-02: Confirmation feedback after modifying a reservation.
  - Action: Save changes in the Modify form as in FT-06.
  - Expected: A success confirmation message (e.g., "Reservation updated") is displayed.
- [X] IX-03: Confirmation feedback after cancelling a reservation.
  - Action: Cancel a reservation as in FT-05.
  - Expected: A confirmation message (e.g., "Reservation cancelled") is displayed.
- [X] IX-04: Confirmation feedback after submitting a review.
  - Action: Submit a review as in FT-07.
  - Expected: A success confirmation message (e.g., "Review submitted") is displayed.
- [X] IX-05: Coupon application immediately updates the displayed price.
  - Action: Enter a valid coupon code and click "Apply" on the booking form, before submitting.
  - Expected: The displayed total/discount updates immediately to reflect the coupon.

## Content
- [X] CT-01: Restaurant list entries show complete names.
  - Action: Open the browse page and inspect all restaurant entries in the list.
  - Expected: Every default restaurant entry displays its restaurant name (no blank or placeholder entries).
- [X] CT-02: Restaurant detail page shows cuisine type and average price.
  - Action: Open the detail page of any restaurant from the list.
  - Expected: The page displays that restaurant's cuisine type and average price with actual values.
- [X] CT-03: Review display matches submitted content.
  - Action: Open the reviews section of the restaurant reviewed in FT-07.
  - Expected: The review shows the exact rating (4 stars) and review text as entered.

**Summary: 17 PASS / 1 FAIL (CS-02).** Key evidence for the failed item is quoted verbatim in its Bug Report: past dates are hard-disabled at the calendar-picker level (so the prescribed past-date submission flow cannot be executed and no submission-time validation error ever appears), and the Modify dialog lacks any date field (so the check cannot be repeated there). All other observed confirmations matched expectations exactly: reservation lifecycle ("Reservation Confirmed!", "Reservation Updated", "Reservation Cancelled"), review lifecycle ("Review Submitted!", "Missing Information — Please fill in all fields and select a rating."), coupon handling ("Coupon Applied! 10% off" / "Invalid Coupon"), and the review display verified in the DOM as 4 filled + 1 muted star with the exact text "Great food".