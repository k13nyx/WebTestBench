# Test Checklist

## Functionality
- [ ] FT-01: Owner can create a new listing with all required details
  - Action: Open the owner's "Create Listing" form, enter location, description, amenities, a photo image URL, and nightly price; submit.
  - Expected: Listing is created and appears in the traveler browse list with the entered details.

- [ ] FT-02: Travelers can browse all available properties in a list
  - Action: Open the main listings page as a traveler.
  - Expected: A list/grid shows default properties, each displaying title/location, price per night, and a way to view details.

- [ ] FT-03: Filter by price range works
  - Action: Set a min and max nightly price in the price filter and apply.
  - Expected: Only listings with nightly price within the entered range are displayed; others are hidden.

- [ ] FT-04: Filter by number of guests works
  - Action: Enter/select a guest count (e.g., 4) in the guests filter and apply.
  - Expected: Only listings that accommodate at least that number of guests are shown.

- [ ] FT-05: Filter by property type works
  - Action: Select a property type (e.g., "Apartment") in the type filter and apply.
  - Expected: Only listings of the selected type are displayed.

- [ ] FT-06: Sort by price works
  - Action: Apply the "Price" sort option (ascending, then descending).
  - Expected: Listings reorder by nightly price low-to-high, then high-to-low.

- [ ] FT-07: Sort by rating works
  - Action: Apply the "Rating" sort option.
  - Expected: Listings reorder by rating (highest-rated first, or the displayed order matches the selected direction).

- [ ] FT-08: Each listing has its own detail page
  - Action: Click a listing from the browse list.
  - Expected: A dedicated detail page opens showing the full description, basic reviews, and available dates for that listing.

- [ ] FT-09: Traveler can submit a booking request for chosen dates
  - Action: On a listing's detail page, open the booking request form, enter check-in/check-out dates within available dates, and submit.
  - Expected: The booking request is submitted successfully and stored against that listing.

- [ ] FT-10: Owner can view booking requests
  - Action: Open the owner's booking requests view.
  - Expected: Submitted requests are listed with traveler, listing, chosen dates, and current status.

- [ ] FT-11: Owner can update the status of a booking request
  - Action: From the owner's requests view, change a request's status (e.g., Approve/Accept or Decline) and save.
  - Expected: The new status is saved and displayed for that request.

## Constraint
- [ ] CS-01: Listing form rejects missing required fields
  - Action: Open "Create Listing", leave required fields (e.g., location and nightly price) empty, and submit.
  - Expected: Submission is blocked and a validation error identifies the missing required field(s); no partial listing is created.

- [ ] CS-02: Nightly price must be a valid positive number
  - Action: Enter a negative value, zero, or non-numeric text in the nightly price field and submit.
  - Expected: Submission is blocked with a validation message; the listing is not created.

- [ ] CS-03: Booking dates must be valid (check-out after check-in)
  - Action: In the booking request form, enter a check-out date equal to or earlier than the check-in date and submit.
  - Expected: Submission is blocked with an error indicating invalid date range.

- [ ] CS-04: Unavailable dates cannot be booked
  - Action: In the booking request form, select dates that include an unavailable/already-booked range shown on the detail page, and submit.
  - Expected: Submission is rejected with a message that the selected dates are not available.

## Interaction
- [ ] IX-01: Success feedback after submitting a booking request
  - Action: Submit a valid booking request.
  - Expected: A visible confirmation (toast/success message) confirms the request was sent and is pending owner review.

- [ ] IX-02: Empty-state message when filters return no results
  - Action: Apply a filter combination matching no listings (e.g., max price below the cheapest listing).
  - Expected: A clear "no properties found" message appears instead of a blank list or broken layout.

- [ ] IX-03: Status change reflects immediately in the owner's requests list
  - Action: Approve or decline a booking request as owner, then view/update the requests list.
  - Expected: The request shows the updated status without stale "Pending" data remaining.

## Content
- [ ] CT-01: Listing photos render from image URLs
  - Action: Inspect the browse list and detail pages for listings created with photo image URLs.
  - Expected: Images load and display correctly (no broken-image icons or empty placeholders).

- [ ] CT-02: Default listing content is relevant and complete
  - Action: Review default listings' titles, locations, descriptions, amenities, ratings, and reviews on list and detail pages.
  - Expected: All content is coherent short-term-rental information (no lorem ipsum, "TODO", or placeholder text); reviews show reviewer name/rating with text.