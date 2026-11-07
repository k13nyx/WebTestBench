I have completed the full test session. Here are the results:

# Test Result

## Functionality

- [X] FT-01: Owner can create a listing with all required details
  - Action: Open the "Add Listing" / "Create Listing" form, enter location, description, amenities, a photo image URL, nightly price, max guests, and property type, then submit.
  - Expected: Submission succeeds, a success confirmation appears, and the new listing is present in the browse list with the entered details.
- [X] FT-02: Browse page lists all available properties
  - Action: Open the main browse/list page without applying any filter.
  - Expected: Every default property in the application appears as a card in the list (no property is omitted).
- [ ] FT-03: Traveler can filter listings by nightly price range
  - Action: Set the minimum and maximum nightly price filter to a range that matches only a subset of default listings.
  - Expected: The result list contains only listings whose nightly price falls inside the chosen range; listings outside the range are not shown.
  - Bug Report:
    - Issue: Missing Filter Control (no maximum nightly price input)
    - Actual: The "Price Range (per night)" control renders a single Radix thumb with `aria-label="Minimum"` (range 0–500) and static labels "$0" / "$500+" — there is no maximum-price thumb or input anywhere in the filter panel (DOM dump of the sidebar shows only 1 `[role=slider]`, 1 number input = "Number of Guests", 0 price inputs). A bounded price range therefore cannot be expressed; only "price ≥ X" is filterable (verified working: min $210 → 4 properties shown, $185 and $165 correctly excluded).
- [X] FT-04: Traveler can filter listings by number of guests
  - Action: Set the "Guests" filter to a number larger than the capacity of some default listings.
  - Expected: Only listings with a guest capacity of at least the selected value remain in the list.
- [X] FT-05: Traveler can filter listings by property type
  - Action: Select a single property type (e.g. Apartment, House, Cabin) in the property type filter.
  - Expected: The list shows only listings of that type and no listings of other types.
- [X] FT-06: Traveler can sort results by nightly price
  - Action: Choose "Price: Low to High", then "Price: High to Low" in the sort control.
  - Expected: Results are ordered by ascending nightly price for the first choice and descending nightly price for the second, without changing which listings match the filters.
- [X] FT-07: Traveler can sort results by rating
  - Action: Choose the rating option in the sort control.
  - Expected: Results are ordered by rating (highest first), and listings with no rating are placed last or otherwise not above rated listings.
- [X] FT-08: Detail page shows full listing information
  - Action: Open the detail page of a default listing (click its card from the browse list).
  - Expected: The page displays the listing's full description, complete amenities list, its photo(s), nightly price, guest capacity, property type, and location.
- [X] FT-09: Detail page shows reviews
  - Action: Open the detail page of a default listing that has reviews and scroll to the reviews section.
  - Expected: Reviews are listed showing reviewer name, star rating, and review text; if the listing has no reviews, an explicit empty-state message is shown.
- [X] FT-10: Detail page shows date availability
  - Action: Open the availability/calendar section of a listing's detail page.
  - Expected: A month calendar is displayed marking available dates as selectable and unavailable/booked dates as disabled.
- [ ] FT-11: Traveler can submit a booking request for chosen dates
  - Action: On a listing detail page, select available check-in and check-out dates, fill the booking request form (guest name/contact and any requested notes), and submit.
  - Expected: Submission succeeds with a confirmation message, and the request is stored with a "Pending" status for that listing and date range.
  - Bug Report:
    - Issue: Incorrect Date Persistence (off-by-one day on stored booking dates)
    - Actual: Submission works and the toast "Booking request sent! The property owner will review your request shortly." appears, and the request is created with status "Pending" — but the stored date range is one day earlier than the dates selected on the calendar. Reproduced twice on /property/1: selected check-in "Nov 18" / check-out "Nov 19" (panel showed "$450 × 1 nights") → owner Bookings view shows "Nov 17 - Nov 18, 2026"; selected "Nov 16" / "Nov 17" → stored as "Nov 15 - Nov 16, 2026". The booking therefore blocks the wrong nights on the property calendar.
- [X] FT-12: Owner can view incoming booking requests
  - Action: Navigate to the owner's booking requests / reservations view.
  - Expected: The request submitted in FT-11 appears with its listing, traveler name, date range, and current status.
- [X] FT-13: Owner can update a booking request status
  - Action: In the owner's booking requests view, change the FT-11 request's status using the status control (e.g. Accept / Decline).
  - Expected: The new status is saved and displayed for that request, and the previous status is no longer shown.
- [X] FT-14: Owner can edit an existing listing
  - Action: Open the owner listing management view, edit a default listing (e.g. change nightly price or description) and save.
  - Expected: The edited values are persisted and shown on the listing's detail page and on its card in the browse list.

## Constraint

- [X] CS-01: Listing form rejects invalid required input
  - Action: Submit the create-listing form with the nightly price left blank or set to a non-numeric/zero/negative value, and separately with other required fields (location, description) left blank.
  - Expected: Each invalid submission is blocked with a visible field-level error message and no listing is created.
- [ ] CS-02: Booking request rejects invalid or unavailable dates
  - Action: Submit the booking form with a check-out date earlier than the check-in date, and separately attempt to book a date marked unavailable/booked on the calendar.
  - Expected: Both submissions are rejected with a clear error message and no booking request is created.
  - Bug Report:
    - Issue: Missing Form Validation (invalid date range accepted, no error message)
    - Actual: On /property/1 the check-in was set to "Nov 30" and check-out to "Nov 28" (check-out earlier than check-in); the "Request to Book" button remained enabled, the submission produced no error message/toast, and a request was created — the owner's Bookings view then lists "Seaside Villa with Infinity Pool / Pending / Nov 29 - Nov 27, 2026 / QA Inverted". Booked/unavailable dates are only greyed out in the calendar widget (no validation on submit), so no error is ever shown for them either.
- [ ] CS-03: Invalid photo URL is rejected or safely handled
  - Action: Create or edit a listing using a photo value that is not a valid image URL (e.g. "not-a-url" or a text-file URL).
  - Expected: The form shows an error for the photo field, or the invalid URL is rejected; no broken-image placeholder is displayed as a listing photo.
  - Bug Report:
    - Issue: Missing URL Validation / Broken Image Displayed
    - Actual: Creating a listing with photo "not-a-url" and otherwise valid data was accepted — toast "Listing created! Your property is now visible to travelers." and the new card rendered with `src="not-a-url"` (resolved to http://localhost:6009/not-a-url) and `naturalWidth = 0`, i.e. a broken-image icon displayed as the listing photo. No field-level error was shown for the photo input.

## Interaction

- [X] IX-01: Filters and sorting update results without a full page reload
  - Action: On the browse page, change a filter value and then change the sort order.
  - Expected: The result list re-renders immediately after each change with the new matching properties, and the page is not reloaded from scratch.
- [X] IX-02: Listing card links to its detail page and status changes are reflected immediately
  - Action: Click a listing card in the browse list, then return to the owner's request view right after changing a request status in FT-13.
  - Expected: The click opens that listing's detail page with a matching URL/title, and the updated request status is shown without needing a manual page refresh.

## Content

- [X] CT-01: Listing cards show accurate summary data
  - Action: Compare each default listing's card against the listing's detail page and its stored details.
  - Expected: Each card displays the correct nightly price, location, guest capacity, property type, and rating for that property, with no placeholder or "undefined"/"null" text.
- [X] CT-02: Property photos render correctly and match the listing
  - Action: Inspect the photo area of each default listing card and detail page.
  - Expected: Photos display as actual images (not broken-image icons), and each photo visibly corresponds to the listing it is attached to rather than an unrelated image.

**Summary of evidence highlights:** default listings (Seaside Villa $450/4.9, Tropical Beach House $295/4.9, Mountain Retreat Cabin $375/4.8, Modern Loft $185/4.7, Sleek City Penthouse $320/4.7, Charming Coastal Cottage $165/4.6) all appear on the browse page and their card data matches their detail pages exactly; guests filter 5 → 3 listings; type filter Apartment → 2 listings; price sort low→high / high→low verified on the full set; "Top Rated" sorts 4.9→4.6 with a newly created unrated listing placed last; owner Approve immediately moves the request to History with status "Approved"; edit of price 450→499 plus description is reflected on both the detail page and the browse card; all 18 default photos load (`naturalWidth = 800`) with listing-specific alt text.