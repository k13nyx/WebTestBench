# Test Checklist

## Functionality
- [ ] FT-01: Owner can create a new property listing with all required details
  - Action: Open the owner's "Create Listing" page, fill in location, description, at least one amenity, one photo image URL, and a nightly price (e.g., 120), then click the "Create"/"Save" button.
  - Expected: The listing is created and can be found in the app with exactly the entered details (location, description, amenities, photo, price).
- [ ] FT-02: Newly created listing appears in the traveler's browse list
  - Action: After creating a listing (FT-01), open the property browse list page.
  - Expected: The new listing appears in the list alongside the default listings, showing its photo, location, and nightly price.
- [ ] FT-03: Traveler can browse all available default properties
  - Action: Open the property list page with no filters or sorting applied.
  - Expected: All default properties are displayed as list items, each showing at least a photo, location, and nightly price.
- [ ] FT-04: Listing detail page shows the full description and listing info
  - Action: Click on any default listing from the browse list.
  - Expected: A dedicated detail page opens for that property displaying its full description, location, amenities, and nightly price.
- [ ] FT-05: Traveler can sort listings by price
  - Action: On the list page, choose "Sort by price: low to high", then "high to low".
  - Expected: Listings are re-ordered so nightly prices display in ascending order, then in descending order.
- [ ] FT-06: Traveler can sort listings by rating
  - Action: On the list page, choose "Sort by rating" (high to low).
  - Expected: Listings are re-ordered from the highest-rated to the lowest-rated property.
- [ ] FT-07: Traveler can submit a booking request for chosen dates
  - Action: On a listing's detail page, select a check-in and a check-out date and submit the booking request form.
  - Expected: The booking request is successfully submitted and recorded for that listing and those dates.
- [ ] FT-08: Owner can view booking requests for their listings
  - Action: Open the owner's booking requests page/panel.
  - Expected: The request submitted in FT-07 is listed with the property, the requested dates, and its current status (e.g., "Pending").
- [ ] FT-09: Owner can update the status of a booking request
  - Action: On the requests page, change the pending request's status to "Confirmed" (and optionally another to "Declined") and save.
  - Expected: The request's status is updated and displayed as the newly selected value.

## Constraint
- [ ] CS-01: Listing cannot be created with empty required fields
  - Action: On the "Create Listing" page, leave one or more required fields (location, description, price) empty and click "Create"/"Save".
  - Expected: Submission is blocked, an error indication is shown for the missing fields, and no listing is created.
- [ ] CS-02: Listing cannot be created with an invalid nightly price
  - Action: On the "Create Listing" page, fill all fields correctly but enter an invalid price (e.g., -50 or "abc") and submit.
  - Expected: Submission is rejected with an error message about the price, and no listing is created.
- [ ] CS-03: Price filter excludes listings outside the selected range
  - Action: On the list page, set a price range filter (e.g., min $50 / max $100) using the default listings' prices.
  - Expected: Only listings with a nightly price within the range are shown; all cheaper or more expensive listings are excluded.
- [ ] CS-04: Guest and property-type filters exclude non-matching listings
  - Action: On the list page, apply a "number of guests" filter (e.g., 4+ guests) and a property-type filter (e.g., "Apartment") separately.
  - Expected: Each filter removes all listings that do not match (fewer guests, or a different property type); only matching listings remain.
- [ ] CS-05: Booking request with invalid dates is blocked
  - Action: On a listing's detail page, try to submit the booking form with a check-out date earlier than the check-in date, and once with empty dates.
  - Expected: Submission is blocked with an error indication; no booking request is created.

## Interaction
- [ ] IX-01: Filters and sorting update the results list immediately
  - Action: Apply any filter (price, guests, type) or change the sort option on the list page.
  - Expected: The displayed results update immediately in response to the selection, with the current filter/sort choice visibly indicated.
- [ ] IX-02: Success feedback is shown after a booking request is submitted
  - Action: Submit a valid booking request form on a listing detail page.
  - Expected: A success message, toast, or on-screen confirmation is displayed telling the user the request was sent.
- [ ] IX-03: Owner gets immediate feedback when a booking status is changed
  - Action: On the requests page, update a request's status (e.g., Pending → Confirmed).
  - Expected: A confirmation is shown and the request's status label updates in place to the new value.

## Content
- [ ] CT-01: Listing photos entered as image URLs are displayed correctly
  - Action: View listing cards on the browse list and the photos on a listing detail page (including a listing created with an image URL).
  - Expected: The images from the provided URLs render as actual photos of the properties, with no broken images.
- [ ] CT-02: Reviews shown on a detail page belong to that property
  - Action: Open two different default listings' detail pages and compare their reviews sections.
  - Expected: Each detail page displays basic reviews (rating/comment) that are relevant to that specific property, not identical unrelated text.
- [ ] CT-03: Available dates are shown on the listing detail page
  - Action: Open any default listing's detail page and inspect the availability section/calendar.
  - Expected: Available dates for that property are clearly displayed so a visitor can see when it can be booked.