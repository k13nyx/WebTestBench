# Test Checklist

## Functionality
- [ ] FT-01: Property owner can create a new listing with all required details
  - Action: As an owner, open the "Create Listing" form and enter a location, description, amenities, at least one photo image URL, and a nightly price, then submit.
  - Expected: The listing is saved and appears in the owner's listings and in the traveler-facing list.

- [ ] FT-02: Property owner can edit an existing listing
  - Action: Open an existing default listing in edit mode, change the nightly price, and save.
  - Expected: The updated price is persisted and displayed everywhere the listing appears.

- [ ] FT-03: Traveler can browse all available properties in a list
  - Action: Open the main listings page.
  - Expected: All available default properties are displayed as list items with name, location, price, and photo.

- [ ] FT-04: Traveler can filter listings by price range
  - Action: Set a minimum and maximum nightly price on the listings page.
  - Expected: Only properties whose nightly price falls within the range remain in the list.

- [ ] FT-05: Traveler can filter listings by number of guests
  - Action: Select a required guest count on the listings page.
  - Expected: Only properties that can accommodate that many guests remain in the list.

- [ ] FT-06: Traveler can filter listings by property type
  - Action: Select a property type (e.g., apartment, house, room) on the listings page.
  - Expected: Only properties matching the selected type remain in the list.

- [ ] FT-07: Traveler can sort results by price
  - Action: Choose "Sort by price" (ascending and descending).
  - Expected: The list reorders so nightly prices are ordered correctly in each direction.

- [ ] FT-08: Traveler can sort results by rating
  - Action: Choose "Sort by rating" on the listings page.
  - Expected: The list reorders so properties appear from highest to lowest rating.

- [ ] FT-09: Listing detail page shows full description, reviews, and available dates
  - Action: Click any property in the list to open its detail page.
  - Expected: The full description, basic reviews, and the available dates are all displayed.

- [ ] FT-10: Traveler can submit a booking request for chosen dates
  - Action: On a detail page, select valid check-in and check-out dates and submit the booking request form.
  - Expected: The booking request is created and linked to the property and dates.

- [ ] FT-11: Property owner can view submitted booking requests
  - Action: As an owner, open the requests view.
  - Expected: All booking requests for the owner's properties are listed with property, dates, and current status.

- [ ] FT-12: Property owner can update the status of a booking request
  - Action: Change a request's status (e.g., from pending to approved or declined) and save.
  - Expected: The request's status is updated and reflects the new value on reload.

## Constraint
- [ ] CS-01: Listing cannot be created with a missing required field
  - Action: Submit the "Create Listing" form with any required field (location, description, amenities, photo URL, or nightly price) left empty.
  - Expected: Submission is blocked and the missing field is flagged; no listing is created.

- [ ] CS-02: Nightly price accepts only positive numeric values
  - Action: Enter a zero, negative, or non-numeric value in the nightly price field and submit.
  - Expected: Submission is rejected with a validation message and no listing is saved.

- [ ] CS-03: Booking request requires a valid date range
  - Action: Submit a booking request where the check-out date is on or before the check-in date.
  - Expected: Submission is blocked and a date-range error is shown.

- [ ] CS-04: Booking request is rejected for unavailable or overlapping dates
  - Action: Submit a booking request for dates that overlap an existing confirmed booking on that property.
  - Expected: The request is rejected with a "dates not available" message.

## Interaction
- [ ] IX-01: Success confirmation appears after a listing is created
  - Action: Submit a valid new listing.
  - Expected: A success confirmation (toast or message) is displayed.

- [ ] IX-02: List updates immediately when a filter or sort is applied
  - Action: Change any filter or sort control on the listings page.
  - Expected: The visible list updates immediately to reflect the selection without a manual reload.

## Content
- [ ] CT-01: Photos render from provided URLs and match the property
  - Action: View a listing's photos on the list and detail pages.
  - Expected: Images load correctly from their URLs and visually correspond to the property.

- [ ] CT-02: Reviews shown are relevant to the listing
  - Action: Open the reviews section on a property detail page.
  - Expected: Reviews contain text and ratings relevant to that property (not placeholders or unrelated content).