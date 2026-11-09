# Test Checklist

## Functionality
- [ ] FT-01: Owner can create a new listing
  - Action: Open the "Create Listing" form, enter location, description, amenities, at least one image URL, a property type, max guests, and a nightly price (e.g., "120"), then submit.
  - Expected: The listing is saved successfully and appears in the listings/browse view with the entered details.
- [ ] FT-02: Owner can edit an existing listing
  - Action: Open one of the owner's existing listings, change the nightly price (e.g., to "150"), and save.
  - Expected: The detail page and list view show the updated price of "150" per night.
- [ ] FT-03: Traveler can view listing detail page
  - Action: Click any property card in the browse list.
  - Expected: A detail page opens showing the full description, amenities, photos, property type, max guests, nightly price, and location.
- [ ] FT-04: Reviews are visible on the detail page
  - Action: Open the detail page of a property that has reviews.
  - Expected: Basic reviews are displayed, each showing the reviewer name/comment and a star rating.
- [ ] FT-05: Available dates are visible on the detail page
  - Action: Open the detail page of a property.
  - Expected: The page shows the property's available (bookable) date range(s) or calendar.
- [ ] FT-06: Traveler can submit a booking request
  - Action: On a detail page, select/check-in and check-out dates within the available range and submit the booking request form with a guest count within the property's capacity.
  - Expected: The booking request is submitted successfully and a confirmation (message/toast/status) is shown.
- [ ] FT-07: Owner can view incoming booking requests
  - Action: Open the owner's booking request management view.
  - Expected: The request submitted in FT-06 is listed, showing the property, dates, and guests.
- [ ] FT-08: Owner can update a booking request status
  - Action: In the owner's request view, change the status of the submitted request (e.g., to "Approved" or "Declined") using the provided control.
  - Expected: The status is updated and the new status is displayed for that request.
- [ ] FT-09: Filter by price range
  - Action: In the browse list, set a price range filter (e.g., min 100, max 200) and apply.
  - Expected: Only properties with nightly prices within 100–200 are shown; all others are excluded.
- [ ] FT-10: Filter by number of guests
  - Action: Set the guest filter to a value (e.g., 4 guests) and apply.
  - Expected: Only properties that can accommodate at least 4 guests are shown.
- [ ] FT-11: Filter by property type
  - Action: Select one property type (e.g., "Apartment") from the type filter and apply.
  - Expected: Only properties of that type are shown.
- [ ] FT-12: Sort results by price
  - Action: With results shown, choose "Sort by price" (lowest first).
  - Expected: The list is reordered so the cheapest property appears first.
- [ ] FT-13: Sort results by rating
  - Action: Choose "Sort by rating" (highest first).
  - Expected: The list is reordered so the highest-rated property appears first.

## Constraint
- [ ] CS-01: Cannot create a listing with missing required fields
  - Action: Open the create-listing form, leave required fields (e.g., location or price) empty, and submit.
  - Expected: Submission is blocked and a validation error is shown; no listing is created.
- [ ] CS-02: Nightly price must be a valid positive number
  - Action: Enter an invalid price (e.g., "0", "-50", or "abc") in the create/edit form and submit.
  - Expected: Submission is rejected with a clear validation message.
- [ ] CS-03: Booking with check-out date not after check-in is blocked
  - Action: In the booking form, select a check-out date equal to or before the check-in date and submit.
  - Expected: Submission is rejected with an error message; no request is created.
- [ ] CS-04: Booking for more guests than property capacity is blocked
  - Action: Submit a booking request with a guest count exceeding the property's maximum guests (e.g., 10 guests for a 4-guest property).
  - Expected: Submission is rejected with an error message.
- [ ] CS-05: Booking dates outside available dates are blocked
  - Action: Submit a booking request with dates outside the property's shown available date range.
  - Expected: Submission is rejected with an error message.
- [ ] CS-06: Image URLs must be valid
  - Action: Enter an empty or malformed image URL in the listing form and submit.
  - Expected: Submission is rejected with a validation error, or the invalid entry is not accepted as a photo.

## Interaction
- [ ] IX-01: Filters update the visible list immediately
  - Action: Apply or clear a filter (e.g., property type) and observe the list.
  - Expected: The list updates dynamically (or after clicking "Apply") without requiring a full page reload, and a "no results" state appears when nothing matches.
- [ ] IX-02: Feedback after submitting a booking request
  - Action: Submit a valid booking request.
  - Expected: A visible success confirmation (message/toast) appears after submission.

## Content
- [ ] CT-01: Listing images render as property photos
  - Action: Open the browse list and a detail page.
  - Expected: Every displayed image loads successfully (no broken-image icons) and depicts the property/accommodation theme.
- [ ] CT-02: Listing details are complete and relevant
  - Action: Open each default listing's detail page.
  - Expected: Each shows non-empty location, description, amenities, property type, nightly price, and guest capacity that match the listing's theme.

*(20 items total: 13 FT, 6 CS, 2 IX, 2 CT — with IX-02 duplicating the confirmation aspect of FT-06 kept distinct as UX feedback; if a strict 20-item cap is required, merge IX-02 into FT-06.)*