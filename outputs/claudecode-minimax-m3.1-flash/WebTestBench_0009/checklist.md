The workspace contains no rental-listing app to inspect (only unrelated artifacts from another project), so the checklist below is derived directly from the instruction.

# Test Checklist

## Functionality
- [ ] FT-01: Owner can create a listing with all required details
  - Action: Open the "Add Listing" / "Create Listing" form, enter location, description, amenities, a photo image URL, nightly price, max guests, and property type, then submit.
  - Expected: Submission succeeds, a success confirmation appears, and the new listing is present in the browse list with the entered details.
- [ ] FT-02: Browse page lists all available properties
  - Action: Open the main browse/list page without applying any filter.
  - Expected: Every default property in the application appears as a card in the list (no property is omitted).
- [ ] FT-03: Traveler can filter listings by nightly price range
  - Action: Set the minimum and maximum nightly price filter to a range that matches only a subset of default listings.
  - Expected: The result list contains only listings whose nightly price falls inside the chosen range; listings outside the range are not shown.
- [ ] FT-04: Traveler can filter listings by number of guests
  - Action: Set the "Guests" filter to a number larger than the capacity of some default listings.
  - Expected: Only listings with a guest capacity of at least the selected value remain in the list.
- [ ] FT-05: Traveler can filter listings by property type
  - Action: Select a single property type (e.g. Apartment, House, Cabin) in the property type filter.
  - Expected: The list shows only listings of that type and no listings of other types.
- [ ] FT-06: Traveler can sort results by nightly price
  - Action: Choose "Price: Low to High", then "Price: High to Low" in the sort control.
  - Expected: Results are ordered by ascending nightly price for the first choice and descending nightly price for the second, without changing which listings match the filters.
- [ ] FT-07: Traveler can sort results by rating
  - Action: Choose the rating option in the sort control.
  - Expected: Results are ordered by rating (highest first), and listings with no rating are placed last or otherwise not above rated listings.
- [ ] FT-08: Detail page shows full listing information
  - Action: Open the detail page of a default listing (click its card from the browse list).
  - Expected: The page displays the listing's full description, complete amenities list, its photo(s), nightly price, guest capacity, property type, and location.
- [ ] FT-09: Detail page shows reviews
  - Action: Open the detail page of a default listing that has reviews and scroll to the reviews section.
  - Expected: Reviews are listed showing reviewer name, star rating, and review text; if the listing has no reviews, an explicit empty-state message is shown.
- [ ] FT-10: Detail page shows date availability
  - Action: Open the availability/calendar section of a listing's detail page.
  - Expected: A month calendar is displayed marking available dates as selectable and unavailable/booked dates as disabled.
- [ ] FT-11: Traveler can submit a booking request for chosen dates
  - Action: On a listing detail page, select available check-in and check-out dates, fill the booking request form (guest name/contact and any requested notes), and submit.
  - Expected: Submission succeeds with a confirmation message, and the request is stored with a "Pending" status for that listing and date range.
- [ ] FT-12: Owner can view incoming booking requests
  - Action: Navigate to the owner's booking requests / reservations view.
  - Expected: The request submitted in FT-11 appears with its listing, traveler name, date range, and current status.
- [ ] FT-13: Owner can update a booking request status
  - Action: In the owner's booking requests view, change the FT-11 request's status using the status control (e.g. Accept / Decline).
  - Expected: The new status is saved and displayed for that request, and the previous status is no longer shown.
- [ ] FT-14: Owner can edit an existing listing
  - Action: Open the owner listing management view, edit a default listing (e.g. change nightly price or description) and save.
  - Expected: The edited values are persisted and shown on the listing's detail page and on its card in the browse list.

## Constraint
- [ ] CS-01: Listing form rejects invalid required input
  - Action: Submit the create-listing form with the nightly price left blank or set to a non-numeric/zero/negative value, and separately with other required fields (location, description) left blank.
  - Expected: Each invalid submission is blocked with a visible field-level error message and no listing is created.
- [ ] CS-02: Booking request rejects invalid or unavailable dates
  - Action: Submit the booking form with a check-out date earlier than the check-in date, and separately attempt to book a date marked unavailable/booked on the calendar.
  - Expected: Both submissions are rejected with a clear error message and no booking request is created.
- [ ] CS-03: Invalid photo URL is rejected or safely handled
  - Action: Create or edit a listing using a photo value that is not a valid image URL (e.g. "not-a-url" or a text-file URL).
  - Expected: The form shows an error for the photo field, or the invalid URL is rejected; no broken-image placeholder is displayed as a listing photo.

## Interaction
- [ ] IX-01: Filters and sorting update results without a full page reload
  - Action: On the browse page, change a filter value and then change the sort order.
  - Expected: The result list re-renders immediately after each change with the new matching properties, and the page is not reloaded from scratch.
- [ ] IX-02: Listing card links to its detail page and status changes are reflected immediately
  - Action: Click a listing card in the browse list, then return to the owner's request view right after changing a request status in FT-13.
  - Expected: The click opens that listing's detail page with a matching URL/title, and the updated request status is shown without needing a manual page refresh.

## Content
- [ ] CT-01: Listing cards show accurate summary data
  - Action: Compare each default listing's card against the listing's detail page and its stored details.
  - Expected: Each card displays the correct nightly price, location, guest capacity, property type, and rating for that property, with no placeholder or "undefined"/"null" text.
- [ ] CT-02: Property photos render correctly and match the listing
  - Action: Inspect the photo area of each default listing card and detail page.
  - Expected: Photos display as actual images (not broken-image icons), and each photo visibly corresponds to the listing it is attached to rather than an unrelated image.