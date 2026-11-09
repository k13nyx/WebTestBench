# Test Checklist

## Functionality

- [ ] **FT-01: Browse the restaurant list**
  - **Action:** Open the restaurant browsing page and review the pre-existing restaurant entries.
  - **Expected:** A list of restaurants is displayed, and each entry can be selected to view more information.

- [ ] **FT-02: View restaurant details**
  - **Action:** Select a restaurant from the list.
  - **Expected:** The restaurant details page displays the restaurant name, cuisine type, average price, and an option to begin a reservation.

- [ ] **FT-03: Create a restaurant reservation**
  - **Action:** Select a restaurant, enter a valid future date, time, and party size, then select **Reserve** or the equivalent submission control.
  - **Expected:** A reservation is created for the selected restaurant with the entered date, time, and party size.

- [ ] **FT-04: View upcoming reservations**
  - **Action:** Open the reservations or bookings area.
  - **Expected:** The newly created reservation appears in the upcoming bookings list with its restaurant, date, time, and party size.

- [ ] **FT-05: Cancel an upcoming reservation**
  - **Action:** Select an upcoming booking and choose **Cancel reservation**, then confirm the cancellation if prompted.
  - **Expected:** The selected reservation is canceled and no longer appears as an upcoming booking.

- [ ] **FT-06: Modify an upcoming reservation**
  - **Action:** Select an upcoming booking, choose **Modify reservation**, change the date, time, or party size, and save the changes.
  - **Expected:** The selected booking displays the updated reservation details.

- [ ] **FT-07: Submit a restaurant review and rating**
  - **Action:** Open the review form for a restaurant the user has visited, enter review text, select a rating, and submit the review.
  - **Expected:** The review and selected rating are submitted and associated with the correct restaurant.

- [ ] **FT-08: Apply a valid discount coupon during reservation**
  - **Action:** Start a reservation, enter a valid available coupon in the coupon field, and select **Apply coupon** before completing the reservation.
  - **Expected:** The coupon is accepted, the applicable discount is shown, and the reservation can be completed with the discount applied.

## Constraint

- [ ] **CS-01: Require reservation details**
  - **Action:** Attempt to submit a reservation with the date, time, or party size missing.
  - **Expected:** The reservation is not created, and each missing required field is identified for correction.

- [ ] **CS-02: Reject invalid reservation values**
  - **Action:** Attempt to reserve using a past date, an invalid time, or a party size of zero, a negative number, or non-numeric text.
  - **Expected:** The reservation is blocked, and the invalid input is identified.

- [ ] **CS-03: Prevent unavailable or conflicting reservations**
  - **Action:** Attempt to reserve a restaurant and time that is already unavailable or conflicts with an existing booking.
  - **Expected:** The reservation is not created, and the user is told to select another available date or time.

- [ ] **CS-04: Limit reviews to visited restaurants**
  - **Action:** Attempt to submit a review for a restaurant the user has not visited or has not completed a reservation for.
  - **Expected:** The review cannot be submitted unless the restaurant is eligible for review.

- [ ] **CS-05: Validate rating and review requirements**
  - **Action:** Attempt to submit a review without selecting a rating, or with review text exceeding the allowed limit if one is presented.
  - **Expected:** The review is not submitted until all required review inputs are valid.

- [ ] **CS-06: Handle invalid coupons safely**
  - **Action:** Enter an invalid, expired, or unavailable coupon and select **Apply coupon**.
  - **Expected:** The coupon is rejected, no discount is applied, and the user can continue the reservation without the coupon.

- [ ] **CS-07: Keep reservation changes scoped to one booking**
  - **Action:** Create or use at least two upcoming bookings, then cancel or modify only one of them.
  - **Expected:** Only the selected booking changes; all other bookings remain unchanged.

## Interaction

- [ ] **IX-01: Update the reservation summary from selections**
  - **Action:** Change the date, time, and party size in the reservation form.
  - **Expected:** The reservation summary reflects each selected value before submission.

- [ ] **IX-02: Confirm successful reservation creation**
  - **Action:** Submit a reservation with valid details.
  - **Expected:** A visible confirmation indicates that the reservation was created successfully and provides the saved booking details.

- [ ] **IX-03: Confirm cancellation and modification results**
  - **Action:** Cancel one booking and modify another.
  - **Expected:** The interface immediately reflects the canceled status and the updated details without showing stale information.

- [ ] **IX-04: Provide immediate coupon feedback**
  - **Action:** Apply a valid coupon and then apply an invalid coupon in separate reservation attempts.
  - **Expected:** The interface clearly indicates whether the coupon was accepted or rejected and updates the discount display accordingly.

## Content

- [ ] **CT-01: Display relevant restaurant information**
  - **Action:** Review the restaurant list and open several restaurant detail pages.
  - **Expected:** Each restaurant entry contains relevant restaurant information, and no restaurant displays another restaurant’s name, cuisine, price, or review data.

- [ ] **CT-02: Display accurate cuisine and price details**
  - **Action:** Compare the cuisine type and average price shown in the restaurant list with the corresponding restaurant detail page.
  - **Expected:** The cuisine type and average price are present and consistent for the selected restaurant.

- [ ] **CT-03: Display complete booking information**
  - **Action:** Open the upcoming bookings area after creating or using a reservation.
  - **Expected:** Each booking clearly identifies the restaurant, reservation date, reservation time, party size, and current status.

- [ ] **CT-04: Associate reviews and ratings with the correct restaurant**
  - **Action:** Submit or view a review and rating for a restaurant, then inspect that restaurant’s review section.
  - **Expected:** The submitted review text and rating appear under the correct restaurant and are not shown for unrelated restaurants.