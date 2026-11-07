# Test Checklist

## Functionality
- [ ] FT-01: Restaurant list page displays the application's default restaurants
  - Action: Open the app home page / restaurant browse list
  - Expected: A list of the pre-existing default restaurants is shown, each with a name and enough info to identify it (no empty list, no error)

- [ ] FT-02: Restaurant detail page shows cuisine type and average price
  - Action: Open the details of any default restaurant from the list
  - Expected: Detail page displays the restaurant's cuisine type and average price (e.g., "$$" / "$25 per person") as non-empty values

- [ ] FT-03: A table reservation can be created with date, time, and party size
  - Action: On a restaurant detail page, select a date, a time slot, and a party size, then submit the reservation form
  - Expected: The reservation is accepted and a confirmation with the chosen date, time, and party size is shown

- [ ] FT-04: Created reservations appear in the user's upcoming bookings
  - Action: Navigate to the "My Reservations" / upcoming bookings section
  - Expected: The newly created reservation is listed with its restaurant name, date, time, and party size

- [ ] FT-05: A reservation can be canceled
  - Action: In the reservations list, click "Cancel" on one of the user's reservations and confirm
  - Expected: The reservation's status changes to canceled and it is no longer counted/shown as an upcoming confirmed booking

- [ ] FT-06: A reservation can be modified
  - Action: Click "Modify" on an existing reservation, change the date, time, and/or party size, and save
  - Expected: The reservation is updated and the reservations list (and details) show the new date, time, and party size

- [ ] FT-07: A review with a rating and text can be submitted for a restaurant
  - Action: Open a restaurant detail page, select a star rating, type review text, and submit
  - Expected: The review is accepted and appears on that restaurant's page

- [ ] FT-08: A valid discount coupon can be applied during the reservation process
  - Action: In the reservation flow, enter a valid coupon code and apply it before confirming
  - Expected: The reservation is created and the coupon discount is reflected in the booking cost shown to the user

## Constraint
- [ ] CS-01: Reservation cannot be submitted with required fields empty
  - Action: On the reservation form, leave the required date/time/party size fields blank and submit
  - Expected: A validation error is shown and no reservation is created

- [ ] CS-02: Party size must be a positive valid number
  - Action: Enter an invalid party size (0, negative, or non-numeric text) and submit the reservation form
  - Expected: The form rejects the input with a clear error message and no reservation is created

- [ ] CS-03: Reservation date cannot be in the past
  - Action: Select a date earlier than today in the reservation form and submit
  - Expected: Submission is blocked with an error indicating the date is invalid/past, and no reservation is created

- [ ] CS-04: An invalid coupon code does not apply a discount
  - Action: Enter a non-existent or expired coupon code during the reservation flow and apply it
  - Expected: An error states the coupon is invalid/not applicable, no discount is applied, and the reservation total remains unchanged

- [ ] CS-05: The same restaurant, date, and time slot cannot be double-booked
  - Action: Create a reservation for a restaurant/date/time, then attempt to create another reservation for the same restaurant, date, and time slot
  - Expected: The second attempt is blocked with a message about the unavailable slot, and only one reservation exists for that slot

## Interaction
- [ ] IX-01: Clicking a restaurant in the list opens its detail page
  - Action: Click a restaurant name/card in the restaurant list
  - Expected: The app navigates to that restaurant's detail page showing its cuisine, average price, and reservation option

- [ ] IX-02: A success message is shown after creating a reservation
  - Action: Complete a valid reservation submission and observe the page
  - Expected: A success/confirmation message appears (e.g., toast or banner) indicating the reservation was created

- [ ] IX-03: Applying a coupon updates the total before the reservation is confirmed
  - Action: Type a valid coupon code and click "Apply" in the reservation form
  - Expected: The discount and new total update immediately on the page, without requiring the reservation to be submitted first

## Content
- [ ] CT-01: Restaurant list and detail page show consistent cuisine and price
  - Action: Compare the cuisine type and average price shown in the restaurant list with those on the clicked restaurant's detail page
  - Expected: Values match exactly for the same restaurant, with no blank or placeholder ("N/A", "TBD") entries for default restaurants

- [ ] CT-02: Reservation confirmation and summary show the correct booking details
  - Action: Create a reservation for a specific restaurant, date, time, and party size, then open the reservation summary in the reservations list
  - Expected: The restaurant name, date, time, party size, and total match what was entered in the form

- [ ] CT-03: Submitted reviews display reviewer, rating, and review text
  - Action: Submit a review with a rating and text, then view the reviews section of that restaurant
  - Expected: The review appears with its star rating, review text, and author, and the restaurant's average rating reflects it

- [ ] CT-04: Discount and total amounts are displayed accurately and no placeholder text is shown
  - Action: Apply a known coupon on a reservation and read the displayed discount and total
  - Expected: The displayed discount matches the coupon's stated value and the total equals the pre-discount amount minus the discount; no "lorem ipsum", "TBD", or empty content appears anywhere in the restaurant, reservation, or review views