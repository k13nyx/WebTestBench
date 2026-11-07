# Test Checklist

## Functionality
- [ ] FT-01: Owner can create a new listing
  - Action: Open the "Create Listing" form and enter a location, description, amenities, an image URL, and a nightly price, then submit.
  - Expected: A new listing is saved and appears in the properties list for travelers.

- [ ] FT-02: Owner can manage (edit) an existing listing
  - Action: Open one of the owner's existing listings and change a detail (e.g., nightly price), then save.
  - Expected: The updated detail is persisted and reflected on the listing.

- [ ] FT-03: Traveler can browse all available properties in a list
  - Action: Navigate to the property browsing page with no filters applied.
  - Expected: A list of all default available properties is displayed, each showing key info (location, price, type).

- [ ] FT-04: Traveler can filter properties by price range
  - Action: Set a minimum and/or maximum nightly price filter and apply it.
  - Expected: Only properties within the selected price range are shown.

- [ ] FT-05: Traveler can filter properties by number of guests
  - Action: Set a "number of guests" filter (e.g., 4 guests) and apply it.
  - Expected: Only properties that accommodate at least that many guests are shown.

- [ ] FT-06: Traveler can filter properties by property type
  - Action: Select a property type filter (e.g., Apartment) and apply it.
  - Expected: Only properties of the selected type are shown.

- [ ] FT-07: Traveler can sort results by price
  - Action: Choose the "Price" sort option (ascending and descending).
  - Expected: The list reorders so prices are in the selected order.

- [ ] FT-08: Traveler can sort results by rating
  - Action: Choose the "Rating" sort option.
  - Expected: The list reorders so properties are ranked by rating.

- [ ] FT-09: Traveler can open a listing detail page
  - Action: Click on a property from the list.
  - Expected: The detail page opens showing the full description and available dates.

- [ ] FT-10: Traveler can submit a booking request for chosen dates
  - Action: On a listing detail page, open the booking request form, enter check-in and check-out dates, and submit.
  - Expected: The booking request is recorded and associated with that listing.

- [ ] FT-11: Owner can view booking requests
  - Action: Open the owner's booking requests view.
  - Expected: All booking requests for the owner's listings are listed with their details.

- [ ] FT-12: Owner can update the status of a booking request
  - Action: Select a booking request and change its status (e.g., to "Approved" or "Rejected").
  - Expected: The new status is saved and displayed for that request.

## Constraint
- [ ] CS-01: Listing creation enforces required fields
  - Action: Attempt to submit a new listing with mandatory fields (location, description, nightly price) left empty.
  - Expected: Submission is blocked and a validation error identifies the missing required fields.

- [ ] CS-02: Booking request enforces a valid date range
  - Action: Attempt to submit a booking request with check-out on or before check-in, or with unavailable dates.
  - Expected: Submission is rejected with a message that the date range is invalid/unavailable.

- [ ] CS-03: Photo field accepts only a valid image URL
  - Action: Enter a non-URL or non-image value (e.g., "abc" or a text file) in the photo URL field and submit.
  - Expected: Submission is rejected with a message that a valid image URL is required.

## Interaction
- [ ] IX-01: Success notification after listing creation
  - Action: Successfully create a new listing.
  - Expected: A success confirmation (toast/message) appears indicating the listing was created.

- [ ] IX-02: Success notification after booking submission
  - Action: Successfully submit a booking request.
  - Expected: A success confirmation (toast/message) appears indicating the request was submitted.

- [ ] IX-03: Filters and sorts update the list dynamically
  - Action: Apply or change a filter or sort option.
  - Expected: The property list updates immediately to reflect the change without a full page reload.

## Content
- [ ] CT-01: Listing detail page shows complete, relevant content
  - Action: Open a listing detail page.
  - Expected: It displays the full description, amenities, photo(s), basic reviews, and available dates — all relevant to that property.

- [ ] CT-02: Browsing list shows relevant short-term rental content
  - Action: Review the default property list and detail pages.
  - Expected: All images, text, and data shown are directly relevant to short-term rental properties (no placeholder or unrelated content).