# Test Checklist

## Functionality
- [ ] FT-01: User can browse the restaurant list and open a restaurant's detail page.
  - Action: Open the restaurant list page, then click any restaurant name.
  - Expected: The list shows all default restaurants. The detail page for the clicked restaurant opens and shows its name, cuisine type, and average price.
- [ ] FT-02: User can reserve a table with a valid date, time, and party size.
  - Action: On a restaurant detail page, select a future date, an available time, and a party size of 2. Click "Reserve".
  - Expected: A confirmation shows the restaurant name, date, time, and party size. The reservation appears under "My Reservations".
- [ ] FT-03: User can view upcoming reservations.
  - Action: Open "My Reservations" from the main navigation.
  - Expected: All upcoming reservations are listed, each showing restaurant, date, time, and party size. Past reservations are not listed as upcoming.
- [ ] FT-04: User can cancel an upcoming reservation.
  - Action: On an upcoming reservation, click "Cancel" and then confirm.
  - Expected: The reservation's status changes to "Cancelled". It no longer appears in the upcoming list.
- [ ] FT-05: User can modify an upcoming reservation.
  - Action: On an upcoming reservation, click "Modify". Change the time to another available slot and change the party size to 4. Click "Save".
  - Expected: The reservation shows the new time and party size in "My Reservations". The change is confirmed.
- [ ] FT-06: User can submit a rating and review for a restaurant they have visited.
  - Action: On a restaurant with a past reservation in the default data, select 4 stars, enter "Great service" in the review field, and click "Submit Review".
  - Expected: The review appears on the restaurant's page with 4 stars and the text "Great service".
- [ ] FT-07: User can apply a valid coupon during reservation.
  - Action: In the reservation form, enter a valid coupon code from the default data in the coupon field and click "Apply". Then complete the reservation.
  - Expected: The coupon is accepted and a discount line appears in the reservation summary. The confirmation shows the discount.

## Constraint
- [ ] CS-01: Cannot reserve a past date or time.
  - Action: On a restaurant detail page, select yesterday's date or a time that has already passed today. Click "Reserve".
  - Expected: The past date or time cannot be selected, or an error such as "Please select a future date and time" appears. No reservation is created.
- [ ] CS-02: Cannot reserve with an invalid party size.
  - Action: Set the party size to 0. Then try to set it above the maximum shown in the form, and click "Reserve".
  - Expected: The party size is rejected with a validation message. No reservation is created.
- [ ] CS-03: Cannot select a time slot that is unavailable.
  - Action: On a restaurant detail page, view the time slots for a date where some slots are already booked.
  - Expected: Booked or unavailable slots are disabled and cannot be selected.
- [ ] CS-04: Cannot submit a review without a star rating.
  - Action: On a visited restaurant, enter review text but leave the stars unselected. Click "Submit Review".
  - Expected: An error such as "Please select a rating" appears. The review is not saved.
- [ ] CS-05: Cannot review a restaurant the user has not visited.
  - Action: Open a restaurant that has no past reservation for the user. Attempt to submit a rating and review.
  - Expected: The review form is hidden or disabled. If submitted, an error such as "You can only review restaurants you have visited" appears.
- [ ] CS-06: Invalid or expired coupon is rejected.
  - Action: In the reservation form, enter "INVALID123" in the coupon field and click "Apply".
  - Expected: An error such as "Invalid or expired coupon" appears. The reservation total does not change.
- [ ] CS-07: Cannot modify a reservation into a conflicting or unavailable slot.
  - Action: On an upcoming reservation, click "Modify" and choose a time slot that is already booked. Click "Save".
  - Expected: An error appears and the slot is not accepted. The original reservation remains unchanged in "My Reservations".

## Interaction
- [ ] IX-01: Cancel requires confirmation before the reservation is cancelled.
  - Action: On an upcoming reservation, click "Cancel". Then click "Keep Reservation" in the dialog.
  - Expected: A dialog asking to confirm the cancellation appears. After "Keep Reservation", the dialog closes and the reservation stays active.
- [ ] IX-02: Star rating responds to hover and click.
  - Action: On a visited restaurant's review form, hover over the 3rd star, then click it.
  - Expected: On hover, stars 1 to 3 are highlighted. After the click, the rating stays at 3 stars when the mouse moves away.

## Content
- [ ] CT-01: Restaurant cards and detail pages show complete, non-placeholder cuisine type and average price.
  - Action: Review every restaurant on the list page, then open its detail page.
  - Expected: Each restaurant shows a non-empty name, a cuisine type, and an average price formatted as currency. No "N/A", "undefined", or blank values appear.
- [ ] CT-02: Reservation details match the values entered.
  - Action: Reserve a table with a specific date, time, and party size, such as 2 PM and 3 guests. Then check the confirmation and "My Reservations".
  - Expected: The date, time, and party size displayed exactly match the values entered.
- [ ] CT-03: Restaurant rating and reviews are displayed accurately.
  - Action: On a restaurant detail page with existing reviews, compare the displayed average rating with the individual review ratings. Check that each review shows its rating, text, and date.
  - Expected: The average rating equals the mean of the individual ratings, rounded to one decimal place. Each review's rating and text are shown correctly.
- [ ] CT-04: Discounted total is calculated correctly.
  - Action: Complete a reservation with a valid coupon. Compare the subtotal, the discount, and the final total shown in the summary.
  - Expected: The discount equals the coupon's stated percentage or amount applied to the subtotal. The final total equals the subtotal minus the discount.