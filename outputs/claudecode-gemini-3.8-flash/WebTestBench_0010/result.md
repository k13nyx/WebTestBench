# Test Result

## Functionality
- [X] FT-01: Browse restaurant listing
  - Action: Navigate to the restaurant directory page.
  - Expected: A list of available default restaurants is displayed with their names and cover images.
- [X] FT-02: View restaurant details
  - Action: Click on any restaurant card from the restaurant list.
  - Expected: The restaurant details page opens, displaying its cuisine type and average price.
- [X] FT-03: Create a table reservation
  - Action: On the restaurant page, select a valid date, time, and party size, then click "Reserve Table".
  - Expected: The reservation is successfully created, and a booking confirmation is displayed.
- [X] FT-04: Apply a valid discount coupon
  - Action: During table reservation, enter a valid coupon code in the coupon field and click "Apply".
  - Expected: The discount is applied and the updated total or discount amount is reflected in the booking summary.
- [X] FT-05: View upcoming reservations
  - Action: Navigate to the "My Reservations" page.
  - Expected: A list of upcoming bookings is displayed, showing restaurant name, date, time, and party size for each.
- [X] FT-06: Modify an existing reservation
  - Action: Click "Modify" on an upcoming booking, change the party size and time slot, then click "Save Changes".
  - Expected: The reservation details update and reflect the new time and party size in the upcoming reservations list.
- [X] FT-07: Cancel an existing reservation
  - Action: Click "Cancel" on an upcoming booking and confirm the action.
  - Expected: The reservation is removed from the upcoming bookings list or marked with status "Cancelled".
- [X] FT-08: Submit a restaurant review and rating
  - Action: On a visited restaurant's page, select a star rating, type a comment in the review box, and click "Submit Review".
  - Expected: The review and rating are submitted successfully and appear in the restaurant's reviews section.

## Constraint
- [X] CS-01: Block reservation submission with missing fields
  - Action: Leave the date, time, or party size field blank and click "Reserve Table".
  - Expected: Form submission is blocked, and validation error messages appear for the missing required fields.
- [X] CS-02: Prevent booking on past dates
  - Action: Attempt to select or enter a date prior to today in the reservation date selector.
  - Expected: Past dates are disabled from selection or an error message prevents form submission.
- [ ] CS-03: Validate minimum party size
  - Action: Enter "0" or a negative number in the party size field and attempt to reserve.
  - Expected: Form submission is blocked with an error indicating that party size must be at least 1.
  - Bug Report:
    - Issue: Missing Input Field / Pre-restricted Dropdown
    - Actual: Party size is implemented as a fixed dropdown select menu with predefined options from "1 Guest" to "10 Guests" rather than an editable text/numeric input. Users cannot enter "0" or negative numbers, and no validation error message indicating that party size must be at least 1 exists.
- [X] CS-04: Reject invalid coupon codes
  - Action: Enter an invalid coupon code "INVALIDCODE" in the coupon field and click "Apply".
  - Expected: An error message "Invalid or expired coupon" appears, and no discount is applied.
- [X] CS-05: Prevent review submission without rating
  - Action: Enter text into the review comment box without selecting any rating stars and click "Submit Review".
  - Expected: Submission is prevented, and an error message prompts the user to select a rating.

## Interaction
- [X] IX-01: Cancellation confirmation dialog
  - Action: Click the "Cancel Reservation" button on an active booking.
  - Expected: A confirmation modal appears asking the user to confirm or dismiss the cancellation before proceeding.
- [ ] IX-02: Instant price update on coupon application
  - Action: Enter a valid coupon code and click "Apply".
  - Expected: The price summary dynamically recalculates to display the discount without reloading the page.
  - Bug Report:
    - Issue: Missing Price Summary Component
    - Actual: The reservation form does not contain a price summary or calculate any monetary totals. Applying a valid coupon displays a static discount percentage tag ("- 10% off"), but no price summary dynamically recalculates.

## Content
- [X] CT-01: Restaurant metadata accuracy
  - Action: Inspect the information section on a restaurant's detail page.
  - Expected: The cuisine type (e.g., "Italian", "Japanese") and average price indicator (e.g., "$$" or "$30-$50 per person") are clearly visible and formatted correctly.
- [X] CT-02: Upcoming booking card information
  - Action: View an active booking card in "My Reservations".
  - Expected: The card displays complete details including restaurant name, reservation date, time, party size, and booking status.
- [X] CT-03: Review entry details
  - Action: View the restaurant review list after submission.
  - Expected: Each review item displays the selected star rating, review text, and timestamp or reviewer name.