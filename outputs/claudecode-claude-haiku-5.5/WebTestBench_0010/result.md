# Test Result

## Functionality
- [X] FT-01: User can browse the restaurant list and open a restaurant's detail page.
  - Action: Open the restaurant list page, then click any restaurant name.
  - Expected: The list shows all default restaurants. The detail page for the clicked restaurant opens and shows its name, cuisine type, and average price.
- [ ] FT-02: User can reserve a table with a valid date, time, and party size.
  - Action: On a restaurant detail page, select a future date, an available time, and a party size of 2. Click "Reserve".
  - Expected: A confirmation shows the restaurant name, date, time, and party size. The reservation appears under "My Reservations".
  - Bug Report:
    - Issue: Incomplete Confirmation
    - Actual: The "Reservation Confirmed!" notice reads "Your table at The Golden Fork is booked for November 11, 2026 at 19:00." It does not show the party size. The reservation does appear in "My Reservations" with 2 Guests. The button is labeled "Confirm Reservation", not "Reserve".
- [X] FT-03: User can view upcoming reservations.
  - Action: Open "My Reservations" from the main navigation.
  - Expected: All upcoming reservations are listed, each showing restaurant, date, time, and party size. Past reservations are not listed as upcoming.
- [X] FT-04: User can cancel an upcoming reservation.
  - Action: On an upcoming reservation, click "Cancel" and then confirm.
  - Expected: The reservation's status changes to "Cancelled". It no longer appears in the upcoming list.
- [X] FT-05: User can modify an upcoming reservation.
  - Action: On an upcoming reservation, click "Modify". Change the time to another available slot and change the party size to 4. Click "Save".
  - Expected: The reservation shows the new time and party size in "My Reservations". The change is confirmed.
- [ ] FT-06: User can submit a rating and review for a restaurant they have visited.
  - Action: On a restaurant with a past reservation in the default data, select 4 stars, enter "Great service" in the review field, and click "Submit Review".
  - Expected: The review appears on the restaurant's page with 4 stars and the text "Great service".
  - Bug Report:
    - Issue: Precondition Unmet / Review Accepted Without Visit
    - Actual: The default data has no past reservation for the user (Past tab showed 0 before testing). I submitted a 4-star "Great service" review on The Golden Fork anyway. It was accepted ("Review Submitted!") and shows 4 stars with the text "Great service". The action could not be run as written, and the acceptance is a rule violation (see CS-05).
- [ ] FT-07: User can apply a valid coupon during reservation.
  - Action: In the reservation form, enter a valid coupon code from the default data in the coupon field and click "Apply". Then complete the reservation.
  - Expected: The coupon is accepted and a discount line appears in the reservation summary. The confirmation shows the discount.
  - Bug Report:
    - Issue: Missing Discount Display
    - Actual: Applying "WELCOME10" shows "Coupon Applied! 10% off your first reservation" and a chip "WELCOME10 - 10% off". No reservation summary or discount line appears. The confirmation reads only "Your table at The Golden Fork is booked for November 12, 2026 at 19:00." The coupon is later shown in My Reservations as "Coupon applied: WELCOME10".

## Constraint
- [X] CS-01: Cannot reserve a past date or time.
  - Action: On a restaurant detail page, select yesterday's date or a time that has already passed today. Click "Reserve".
  - Expected: The past date or time cannot be selected, or an error such as "Please select a future date and time" appears. No reservation is created.
- [ ] CS-02: Cannot reserve with an invalid party size.
  - Action: Set the party size to 0. Then try to set it above the maximum shown in the form, and click "Reserve".
  - Expected: The party size is rejected with a validation message. No reservation is created.
  - Bug Report:
    - Issue: Missing Validation Message
    - Actual: The party size control only offers "1 Guest" through "10 Guests". 0 and values above 10 cannot be chosen, so no reservation is created. However, no validation message is shown for an invalid value, as the Expected states.
- [ ] CS-03: Cannot select a time slot that is unavailable.
  - Action: On a restaurant detail page, view the time slots for a date where some slots are already booked.
  - Expected: Booked or unavailable slots are disabled and cannot be selected.
  - Bug Report:
    - Issue: Booked Slot Selectable
    - Actual: I confirmed a reservation for The Golden Fork on November 12, 2026 at 19:00. When I reopened the time list for that date, "19:00" was still enabled (no aria-disabled or disabled attribute). Every slot on November 11 was also enabled. No booked slot was disabled anywhere.
- [X] CS-04: Cannot submit a review without a star rating.
  - Action: On a visited restaurant, enter review text but leave the stars unselected. Click "Submit Review".
  - Expected: An error such as "Please select a rating" appears. The review is not saved.
- [ ] CS-05: Cannot review a restaurant the user has not visited.
  - Action: Open a restaurant that has no past reservation for the user. Attempt to submit a rating and review.
  - Expected: The review form is hidden or disabled. If submitted, an error such as "You can only review restaurants you have visited" appears.
  - Bug Report:
    - Issue: Unvisited Review Accepted
    - Actual: The "Write a Review" form on The Golden Fork is visible and enabled. With no visit on record, a 4-star review submitted and the app showed "Review Submitted!". The review count went from 2 to 3. No "You can only review restaurants you have visited" error appeared.
- [X] CS-06: Invalid or expired coupon is rejected.
  - Action: In the reservation form, enter "INVALID123" in the coupon field and click "Apply".
  - Expected: An error such as "Invalid or expired coupon" appears. The reservation total does not change.
- [ ] CS-07: Cannot modify a reservation into a conflicting or unavailable slot.
  - Action: On an upcoming reservation, click "Modify" and choose a time slot that is already booked. Click "Save".
  - Expected: An error appears and the slot is not accepted. The original reservation remains unchanged in "My Reservations".
  - Bug Report:
    - Issue: Conflicting Slot Accepted
    - Actual: I had two upcoming reservations at The Golden Fork on November 12 (19:00 and 20:00). I changed the 20:00 one to 19:00, the slot held by the other booking. The app showed "Reservation Updated" and "My Reservations" lists two 19:00 bookings for that date.

## Interaction
- [X] IX-01: Cancel requires confirmation before the reservation is cancelled.
  - Action: On an upcoming reservation, click "Cancel". Then click "Keep Reservation" in the dialog.
  - Expected: A dialog asking to confirm the cancellation appears. After "Keep Reservation", the dialog closes and the reservation stays active.
- [X] IX-02: Star rating responds to hover and click.
  - Action: On a visited restaurant's review form, hover over the 3rd star, then click it.
  - Expected: On hover, stars 1 to 3 are highlighted. After the click, the rating stays at 3 stars when the mouse moves away.

## Content
- [ ] CT-01: Restaurant cards and detail pages show complete, non-placeholder cuisine type and average price.
  - Action: Review every restaurant on the list page, then open its detail page.
  - Expected: Each restaurant shows a non-empty name, a cuisine type, and an average price formatted as currency. No "N/A", "undefined", or blank values appear.
  - Bug Report:
    - Issue: Price Not Shown as Currency
    - Actual: All six cards show a name and cuisine, with no N/A, undefined, or blank values. Price appears only as tier symbols: French "$$$$", Japanese "$$$", Italian "$$", American BBQ "$$", Indian "$$", Seafood "$$$". No average price amount in currency format appears. I opened only The Golden Fork's detail page, which shows "$$$$".
- [ ] CT-02: Reservation details match the values entered.
  - Action: Reserve a table with a specific date, time, and party size, such as 2 PM and 3 guests. Then check the confirmation and "My Reservations".
  - Expected: The date, time, and party size displayed exactly match the values entered.
  - Bug Report:
    - Issue: Party Size Missing from Confirmation
    - Actual: I entered November 12, 2026, 19:00, and 2 guests. "My Reservations" shows November 12, 2026, 19:00, and 2 Guests, which matches. The confirmation shows only the date and time, with no party size.
- [X] CT-03: Restaurant rating and reviews are displayed accurately.
  - Action: On a restaurant detail page with existing reviews, compare the displayed average rating with the individual review ratings. Check that each review shows its rating, text, and date.
  - Expected: The average rating equals the mean of the individual ratings, rounded to one decimal place. Each review's rating and text are shown correctly.
- [ ] CT-04: Discounted total is calculated correctly.
  - Action: Complete a reservation with a valid coupon. Compare the subtotal, the discount, and the final total shown in the summary.
  - Expected: The discount equals the coupon's stated percentage or amount applied to the subtotal. The final total equals the subtotal minus the discount.
  - Bug Report:
    - Issue: No Pricing Summary
    - Actual: After applying WELCOME10 and completing a reservation, no subtotal, discount amount, or final total appears in the form, the confirmation, or "My Reservations". The only trace is the text "Coupon applied: WELCOME10". The 10% calculation cannot be verified.

---

Notes:
- Test data was changed during the run. Reservations were created and cancelled, and a 4-star review by "QA Tester" was posted to The Golden Fork. A confirmed reservation for Nov 12, 2026 at 19:00 (with WELCOME10) remains active, along with a second one at 19:00 from the CS-07 test.
- I used about 100 tool calls, so I stopped at the budget limit.