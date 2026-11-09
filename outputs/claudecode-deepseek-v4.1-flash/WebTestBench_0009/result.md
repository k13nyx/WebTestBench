All tests complete. Here is the full verified checklist.

# Test Result

## Functionality

- [X] FT-01: Property owner can create a new listing with all required details
  - Action: As an owner, open the "Create Listing" form and enter a location, description, amenities, at least one photo image URL, and a nightly price, then submit.
  - Expected: The listing is saved and appears in the owner's listings and in the traveler-facing list.

- [X] FT-02: Property owner can edit an existing listing
  - Action: Open an existing default listing in edit mode, change the nightly price, and save.
  - Expected: The updated price is persisted and displayed everywhere the listing appears.
  - Note: Edited "Seaside Villa with Infinity Pool" from $450 → $480; both the list card and the detail page show $480.

- [X] FT-03: Traveler can browse all available properties in a list
  - Action: Open the main listings page.
  - Expected: All available default properties are displayed as list items with name, location, price, and photo.

- [X] FT-04: Traveler can filter listings by price range
  - Action: Set a minimum and maximum nightly price on the listings page.
  - Expected: Only properties whose nightly price falls within the range remain in the list.
  - Note: The price control constrains by both bounds (e.g. min $100 / max $400 left only the 5 properties whose price is ≤ $400). However the "Price Range" slider renders only a single handle labelled *Minimum* — see CS note below if this is treated as a defect.

- [X] FT-05: Traveler can filter listings by number of guests
  - Action: Select a required guest count on the listings page.
  - Expected: Only properties that can accommodate that many guests remain in the list.
  - Note: Entering 6 returned exactly the 3 properties with maxGuests ≥ 6.

- [X] FT-06: Traveler can filter listings by property type
  - Action: Select a property type (e.g., apartment, house, room) on the listings page.
  - Expected: Only properties matching the selected type remain in the list.
  - Note: "Apartment" returned exactly the 2 apartment listings.

- [X] FT-07: Traveler can sort results by price
  - Action: Choose "Sort by price" (ascending and descending).
  - Expected: The list reorders so nightly prices are ordered correctly in each direction.
  - Note: Asc → 165,185,295,320,375,450; Desc → 450,375,320,295,185,165.

- [X] FT-08: Traveler can sort results by rating
  - Action: Choose "Sort by rating" on the listings page.
  - Expected: The list reorders so properties appear from highest to lowest rating.
  - Note: 4.9, 4.9, 4.8, 4.7, 4.7, 4.6.

- [X] FT-09: Listing detail page shows full description, reviews, and available dates
  - Action: Click any property in the list to open its detail page.
  - Expected: The full description, basic reviews, and the available dates are all displayed.
  - Note: "About this place" full description and a "Reviews (3)" section with text + star ratings render; availability is conveyed by the booking calendar (unavailable nights are disabled).

- [X] FT-10: Traveler can submit a booking request for chosen dates
  - Action: On a detail page, select valid check-in and check-out dates and submit the booking request form.
  - Expected: The booking request is created and linked to the property and dates.

- [X] FT-11: Property owner can view submitted booking requests
  - Action: As an owner, open the requests view.
  - Expected: All booking requests for the owner's properties are listed with property, dates, and current status.
  - Note: The submitted request appeared as "Seaside Villa with Infinity Pool · Nov 13 – Nov 16, 2026 · QA Traveler · Pending" alongside the seeded requests.

- [X] FT-12: Property owner can update the status of a booking request
  - Action: Change a request's status (e.g., from pending to approved or declined) and save.
  - Expected: The request's status is updated and reflects the new value on reload.
  - Note: Approving moved the request from Pending → History with an "Approved" badge and a "Booking approved" toast; the new value persists across in-app navigation/re-render. (Data is held only in memory, so a hard browser reload re-seeds the demo data.)

## Constraint

- [ ] CS-01: Listing cannot be created with a missing required field
  - Action: Submit the "Create Listing" form with any required field (location, description, amenities, photo URL, or nightly price) left empty.
  - Expected: Submission is blocked and the missing field is flagged; no listing is created.
  - Bug Report:
    - Issue: Missing required-field validation (photo URL / amenities)
    - Actual: With title, location, description, price and guests filled but the photo image URL left empty (and no amenities selected), clicking "Create Listing" succeeds — a "Listing created!" toast appears and the listing ("No Photo Test") is added to the list. The photo URL field is not marked required and is not flagged, so a listing can be saved with no photo at all.

- [X] CS-02: Nightly price accepts only positive numeric values
  - Action: Enter a zero, negative, or non-numeric value in the nightly price field and submit.
  - Expected: Submission is rejected with a validation message and no listing is saved.
  - Note: Price input is `type=number` with `min=1`; entering 0 blocks submit and flags "Value must be greater than or equal to 1." Negative values are likewise rejected; non-numeric cannot be entered.

- [ ] CS-03: Booking request requires a valid date range
  - Action: Submit a booking request where the check-out date is on or before the check-in date.
  - Expected: Submission is blocked and a date-range error is shown.
  - Bug Report:
    - Issue: Missing check-out > check-in validation
    - Actual: A check-out of Dec 1 was set, then check-in was changed to Dec 5 (check-out before check-in). The "Request to Book" button remained enabled and submitting produced the success toast "Booking request sent!" — the invalid range was accepted with no date-range error.

- [ ] CS-04: Booking request is rejected for unavailable or overlapping dates
  - Action: Submit a booking request for dates that overlap an existing confirmed booking on that property.
  - Expected: The request is rejected with a "dates not available" message.
  - Bug Report:
    - Issue: No availability/overlap enforcement on booking submission
    - Actual: The same property accepts a request for dates identical to an already-submitted request (submitted Nov 16 – Nov 20 twice; both returned "Booking request sent!"). No "dates not available" path exists anywhere, and a request spanning calendar-disabled (unavailable) nights is also accepted. Approving a request does not update the property's availability either.

## Interaction

- [X] IX-01: Success confirmation appears after a listing is created
  - Action: Submit a valid new listing.
  - Expected: A success confirmation (toast or message) is displayed.
  - Note: Toast "Listing created! Your property is now visible to travelers."

- [X] IX-02: List updates immediately when a filter or sort is applied
  - Action: Change any filter or sort control on the listings page.
  - Expected: The visible list updates immediately to reflect the selection without a manual reload.
  - Note: Guests, property-type and sort changes re-rendered the list immediately (e.g. heading changed 6 → 3 / → 2 Properties) with no reload.

## Content

- [X] CT-01: Photos render from provided URLs and match the property
  - Action: View a listing's photos on the list and detail pages.
  - Expected: Images load correctly from their URLs and visually correspond to the property.
  - Note: Gallery `<img>` elements load from their `images.unsplash.com` URLs with `complete=true` and `naturalWidth=800`, and carry the correct property alt text (e.g. "Seaside Villa with Infinity Pool - Photo 1/2/3").

- [X] CT-02: Reviews shown are relevant to the listing
  - Action: Open the reviews section on a property detail page.
  - Expected: Reviews contain text and ratings relevant to that property (not placeholders or unrelated content).
  - Note: Reviews for the Seaside Villa are property-specific ("The sunset views are even better than the photos.", "The pool is incredible.") with matching 5/5/4 ratings and dates.