# Test Checklist

## Functionality
- [ ] FT-01: Owner can create a new listing with all required details
  - Action: Open the owner listing form, enter a Location, Title, Description, select at least one Amenity, paste one Photo image URL, enter a Nightly price (e.g. 150), click "Create Listing".
  - Expected: Listing is saved and appears in the browse list showing the entered title, location, and "$150 / night".

- [ ] FT-02: Owner can edit an existing listing
  - Action: Open the owner's "My Listings" view, click "Edit" on a default listing, change the Nightly price to a different value, save.
  - Expected: The browse list and the listing detail page show the new price; the old price is no longer displayed.

- [ ] FT-03: Traveler can browse all available properties as a list
  - Action: Open the browse/listings page without applying any filter.
  - Expected: All default properties are displayed in a list, each showing title, location, and nightly price.

- [ ] FT-04: Results can be filtered by price range
  - Action: Set the price range filter to a narrow band (e.g. Min 100, Max 200) and apply it.
  - Expected: Only properties whose nightly price falls within 100–200 are shown; every listed price is inside the range.

- [ ] FT-05: Results can be filtered by number of guests
  - Action: Set the guests filter to a specific number (e.g. 4) and apply it.
  - Expected: Only properties that accommodate at least 4 guests are shown; no property with a smaller capacity appears.

- [ ] FT-06: Results can be filtered by property type
  - Action: Select a single property type (e.g. "Apartment") in the type filter and apply it.
  - Expected: Only listings of that type are shown; no listing of another type (e.g. "House") appears in the results.

- [ ] FT-07: Results can be sorted by price or by rating
  - Action: Choose "Price: Low to High", verify order; then choose "Rating: High to Low", verify order.
  - Expected: Prices appear in strictly ascending order for the price sort, and ratings appear in descending order for the rating sort.

- [ ] FT-08: Each listing has a detail page with description, reviews, and available dates
  - Action: Open the detail page of any default listing from the browse list.
  - Expected: The page shows the full description, at least one review with rating and text, and a list/calendar of available dates.

- [ ] FT-09: Traveler can submit a booking request for chosen dates
  - Action: On a listing detail page, fill the booking form (name, email, check-in date, check-out date within the available dates) and submit.
  - Expected: A confirmation is shown to the traveler, and the request appears in the owner's booking requests view with the chosen dates and status "Pending".

- [ ] FT-10: Owner can update the status of a booking request
  - Action: In the owner's booking requests view, change the status of a pending request to "Accepted" and save; reload the page.
  - Expected: The request displays status "Accepted" and remains "Accepted" after reload.

## Constraint
- [ ] CS-01: Listing cannot be created with required fields left empty
  - Action: Open the listing form, leave Location and Nightly price empty, fill the rest, click "Create Listing".
  - Expected: Submission is blocked, an error is shown on the empty required fields, and no new listing is added to the browse list.

- [ ] CS-02: Nightly price must be a positive number
  - Action: Attempt to create a listing with Nightly price "0", then "-50", then "abc".
  - Expected: Each attempt is rejected with a validation message; no listing with an invalid price is created.

- [ ] CS-03: Booking request must have check-out after check-in
  - Action: On a listing detail page, submit the booking form with a check-out date earlier than the check-in date.
  - Expected: Submission is blocked with a date-range error; no booking request is created.

- [ ] CS-04: Booking cannot be requested for unavailable dates
  - Action: Submit the booking form using a date range that includes a date marked as unavailable on that listing.
  - Expected: Submission is rejected with an availability message; no booking request is created.

- [ ] CS-05: Photo field accepts only a valid image URL
  - Action: Attempt to create a listing with the photo field set to plain text (e.g. "not-a-url").
  - Expected: Submission is rejected or the field is flagged as invalid; no listing is created with an invalid photo value.

## Interaction
- [ ] IX-01: Selecting a listing opens its own detail page
  - Action: Click a listing card/row in the browse list.
  - Expected: The page navigates to that listing's detail page (URL/content changes to the selected property only).

- [ ] IX-02: Filter and sort controls update the results list in place
  - Action: On the browse page, apply a filter and then change the sort option.
  - Expected: The results list re-renders immediately on the same page, and the applied filter/sort selection stays visible as active.

- [ ] IX-03: Owner status change is reflected immediately in the requests list
  - Action: In the owner's booking requests view, change a request status to "Declined" without reloading the page.
  - Expected: That row's status label updates to "Declined" right away.

## Content
- [ ] CT-01: Listing images render correctly and are relevant to the property
  - Action: View the browse list and open two listing detail pages; inspect all displayed images.
  - Expected: Every image loads (no broken/placeholder icons), and each image depicts a rental property/interior/travel scene relevant to its listing.

- [ ] CT-02: Detail page content matches the selected listing
  - Action: Note the title, location, amenities, and price of a listing in the browse list, then open its detail page.
  - Expected: The detail page shows the same title, location, amenity list, and price as the listing that was selected — no mismatched or placeholder data.