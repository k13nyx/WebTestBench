All tests executed. The final critical finding: with check-in (Nov 25) **after** check-out (Nov 20) and valid name/email, the app displayed **"Booking request sent!"** and created the booking — the invalid date range was accepted. This completes the test execution.

# Test Result

## Functionality
- [X] FT-01: Owner can create a new listing
  - Action: Open the "Create Listing" form and enter a location, description, amenities, an image URL, and a nightly price, then submit.
  - Expected: A new listing is saved and appears in the properties list for travelers.
  - Note: Created "Sunny Beach Condo" (Miami, Villa, $210, WiFi) → redirected to home, "7 Properties Found", new listing visible.

- [X] FT-02: Owner can manage (edit) an existing listing
  - Action: Open one of the owner's existing listings and change a detail (e.g., nightly price), then save.
  - Expected: The updated detail is persisted and reflected on the listing.
  - Note: Edited Seaside Villa price 450→500; "Listing updated!" toast; list now shows "$500 / night".

- [X] FT-03: Traveler can browse all available properties in a list
  - Action: Navigate to the property browsing page with no filters applied.
  - Expected: A list of all default available properties is displayed, each showing key info (location, price, type).
  - Note: Default view shows 6 properties, each with location, price/night, and type.

- [X] FT-04: Traveler can filter properties by price range
  - Action: Set a minimum and/or maximum nightly price filter and apply it.
  - Expected: Only properties within the selected price range are shown.
  - Note: Set minimum to $180 via the price slider → list dropped from 6 to 5; the $165 cottage was excluded (only price ≥ $180 remained).

- [X] FT-05: Traveler can filter properties by number of guests
  - Action: Set a "number of guests" filter (e.g., 4 guests) and apply it.
  - Expected: Only properties that accommodate at least that many guests are shown.
  - Note: Set guests = 4 → 5 properties (the 2-guest Sleek City Penthouse was excluded).

- [X] FT-06: Traveler can filter properties by property type
  - Action: Select a property type filter (e.g., Apartment) and apply it.
  - Expected: Only properties of the selected type are shown.
  - Note: Selected "Apartment" → only "Modern Loft in Historic District" remained (apartment type).

- [X] FT-07: Traveler can sort results by price
  - Action: Choose the "Price" sort option (ascending and descending).
  - Expected: The list reorders so prices are in the selected order.
  - Note: "Price: Low to High" produced order: $165, $185, $295, $320, $375, $450.

- [X] FT-08: Traveler can sort results by rating
  - Action: Choose the "Rating" sort option.
  - Expected: The list reorders so properties are ranked by rating.
  - Note: "Top Rated" produced order by rating: 4.9, 4.9, 4.8, 4.7, 4.7, 4.6.

- [X] FT-09: Traveler can open a listing detail page
  - Action: Click on a property from the list.
  - Expected: The detail page opens showing the full description and available dates.
  - Note: Clicking Seaside Villa opened detail page with full description, amenities, photos, reviews, and a check-in/check-out date picker.

- [X] FT-10: Traveler can submit a booking request for chosen dates
  - Action: On a listing detail page, open the booking request form, enter check-in and check-out dates, and submit.
  - Expected: The booking request is recorded and associated with that listing.
  - Note: Submitted Nov 15–20 for Seaside Villa with name/email → appeared in owner's Booking Requests.

- [X] FT-11: Owner can view booking requests
  - Action: Open the owner's booking requests view.
  - Expected: All booking requests for the owner's listings are listed with their details.
  - Note: /manage-bookings listed requests with property, status, dates, guests, name, email, and message.

- [X] FT-12: Owner can update the status of a booking request
  - Action: Select a booking request and change its status (e.g., to "Approved" or "Rejected").
  - Expected: The new status is saved and displayed for that request.
  - Note: Clicked "Approve" → request moved Pending(3)→History(2) as "Approved" with "Booking approved" toast.

## Constraint
- [X] CS-01: Listing creation enforces required fields
  - Action: Attempt to submit a new listing with mandatory fields (location, description, nightly price) left empty.
  - Expected: Submission is blocked and a validation error identifies the missing required fields.
  - Note: Submission was blocked (stayed on form, focus moved to the first empty required field). No separate textual error banner was rendered, but required-field enforcement prevented creation.

- [ ] CS-02: Booking request enforces a valid date range
  - Action: Attempt to submit a booking request with check-out on or before check-in, or with unavailable dates.
  - Expected: Submission is rejected with a message that the date range is invalid/unavailable.
  - Bug Report:
    - Issue: Missing/inadequate date-range validation (no rejection of illogical ranges)
    - Actual: With check-in = Nov 25 and check-out = Nov 20 (check-out before check-in) plus valid name/email, the app accepted the request and displayed "Booking request sent!"; the booking was created. No error or rejection about the invalid date range appeared (the nights/total summary silently cleared, but submission still succeeded).

- [ ] CS-03: Photo field accepts only a valid image URL
  - Action: Enter a non-URL or non-image value (e.g., "abc" or a text file) in the photo URL field and submit.
  - Expected: Submission is rejected with a message that a valid image URL is required.
  - Bug Report:
    - Issue: Missing image-URL format validation
    - Actual: Submitting a new listing with photo URL "abc" was accepted; "Listing created!" appeared and the listing ("Test Property CS03") appeared in the property list with a broken/invalid image reference. No validation error was shown.

## Interaction
- [X] IX-01: Success notification after listing creation
  - Action: Successfully create a new listing.
  - Expected: A success confirmation (toast/message) appears indicating the listing was created.
  - Note: "Listing created! Your property is now visible to travelers." toast appeared.

- [X] IX-02: Success notification after booking submission
  - Action: Successfully submit a booking request.
  - Expected: A success confirmation (toast/message) appears indicating the request was submitted.
  - Note: "Booking request sent! The property owner will review your request shortly." toast appeared.

- [X] IX-03: Filters and sorts update the list dynamically
  - Action: Apply or change a filter or sort option.
  - Expected: The property list updates immediately to reflect the change without a full page reload.
  - Note: Applying guests/type filters and price/rating sorts updated the list in place (no page reload).

## Content
- [X] CT-01: Listing detail page shows complete, relevant content
  - Action: Open a listing detail page.
  - Expected: It displays the full description, amenities, photo(s), basic reviews, and available dates — all relevant to that property.
  - Note: Detail page showed 3 photos, full "About this place" description, "What this place offers" amenities (Infinity Pool, Sea View, etc.), 3 reviews with ratings/dates, and check-in/check-out date selection.

- [X] CT-02: Browsing list shows relevant short-term rental content
  - Action: Review the default property list and detail pages.
  - Expected: All images, text, and data shown are directly relevant to short-term rental properties (no placeholder or unrelated content).
  - Note: All listings (villas, cabins, lofts, cottages, etc.), descriptions, amenities, prices, ratings, and reviews are relevant short-term-rental content; no placeholder/unrelated data observed.

---

## Summary
- **Passed:** 18/20 (FT-01–FT-12, CS-01, IX-01–IX-03, CT-01–CT-02)
- **Failed:** 2/20 — **CS-02** (invalid date range accepted) and **CS-03** (invalid/non-URL photo accepted).

Both failures are genuine validation gaps: the app accepted a booking whose check-out precedes its check-in (CS-02) and accepted a non-URL string as a photo URL when creating a listing (CS-03), in both cases showing a success confirmation rather than rejecting with an error message.