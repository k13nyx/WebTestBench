# Test Checklist

## Functionality
- [ ] FT-01: Owner can create a new listing with all required details
  - Action: Open the create-listing form, enter location, description, amenities, at least one photo URL, and nightly price; submit.
  - Expected: The new listing is saved and appears in the browse list with the entered data.
- [ ] FT-02: Owner can edit an existing listing
  - Action: Open an existing listing's edit form, change the nightly price and description, save.
  - Expected: The updated values are persisted and shown on the listing and its detail page.
- [ ] FT-03: Traveler can browse all available properties in a list
  - Action: Navigate to the property browse/main page.
  - Expected: A list of all default properties is displayed, each as a separate card/item.
- [ ] FT-04: Filter properties by price range
  - Action: Set a minimum and maximum nightly price in the price filter.
  - Expected: Only properties with nightly price within the selected range are shown.
- [ ] FT-05: Filter properties by number of guests
  - Action: Select a guest count in the guests filter.
  - Expected: Only properties that accommodate at least the selected number of guests are shown.
- [ ] FT-06: Filter properties by type of property
  - Action: Select a property type (e.g., apartment, house) in the type filter.
  - Expected: Only listings of the selected property type are shown.
- [ ] FT-07: Sort results by price
  - Action: Choose the price sort option.
  - Expected: Listings are reordered by nightly price in the direction indicated by the sort control (e.g., low→high, high→low).
- [ ] FT-08: Sort results by rating
  - Action: Choose the rating sort option.
  - Expected: Listings are reordered by rating (highest first).
- [ ] FT-09: Listing detail page shows description, reviews, and available dates
  - Action: Click a property in the browse list to open its detail page.
  - Expected: The page displays the full description, a list of basic reviews, and an available-dates section.
- [ ] FT-10: Traveler can submit a booking request for chosen dates
  - Action: On a detail page, fill the booking request form with valid check-in/check-out dates and required traveler info, then submit.
  - Expected: The request is recorded and visible to the owner with the chosen dates.
- [ ] FT-11: Owner can view incoming booking requests
  - Action: Open the owner's booking-requests view.
  - Expected: Each request is listed with the property, dates, requester info, and current status.
- [ ] FT-12: Owner can update the status of a booking request
  - Action: Select a request and change its status (e.g., approve/reject).
  - Expected: The new status is saved and displayed for that request.

## Constraint
- [ ] CS-01: Listing cannot be created with required fields empty
  - Action: Submit the create-listing form with location, price, or other required fields left blank.
  - Expected: Submission is blocked, no listing is created, and an error identifies the missing fields.
- [ ] CS-02: Booking request cannot be submitted with invalid dates or missing required fields
  - Action: Submit the booking form with check-out on/before check-in, dates outside availability, or required fields empty.
  - Expected: Submission is blocked with a clear error message, and no request is created.
- [ ] CS-03: Combined filters never show non-matching properties
  - Action: Apply price range, guest count, and property type filters simultaneously.
  - Expected: Every displayed property satisfies all active filters at once; no property violating any filter appears.

## Interaction
- [ ] IX-01: Browse list responds immediately to filter and sort changes
  - Action: Change a filter or sort option on the browse page.
  -Expected: The list and its result count update without a page reload, reflecting only matching properties.
- [ ] IX-02: Booking submission and status updates give immediate feedback
  - Action: Submit a booking request, then as owner change a request's status.
  - Expected: A visible confirmation/feedback message appears, and the new request/status is shown right away.

## Content
- [ ] CT-01: Property cards show relevant listing information
  - Action: Inspect cards on the browse list.
  - Expected: Each card shows a photo, location, nightly price, and rating that match that property's data.
- [ ] CT-02: Listing photos load from the entered image URLs
  - Action: Open detail pages for default listings.
  - Expected: All photo images render successfully (no broken images) and depict property/interior imagery relevant to the listing.
- [ ] CT-03: Reviews and dates shown are relevant to the property
  - Action: Open the detail page of a property.
  - Expected: Reviews reference that property's stay experience, and the available-dates section shows dates belonging to that property.