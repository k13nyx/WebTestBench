All checklist items executed. Here is the complete test report.

# Test Result

## Functionality
- [X] FT-01: Owner can create a new listing with all required details
  - Action: Open the owner's "Create Listing" form, enter location, description, amenities, a photo image URL, and nightly price; submit.
  - Expected: Listing is created and appears in the traveler browse list with the entered details.
  - Verified: Created "QA Sunset Studio" (Lisbon, Portugal; villa type; full description; amenities WiFi/Kitchen/Pool; photo URL; $120/night; 3 guests). Browse list went 6→7 Properties Found, card shows villa badge, title, "Lisbon, Portugal", 3 guests, $120/night, and the photo loads.

- [X] FT-02: Travelers can browse all available properties in a list
  - Action: Open the main listings page as a traveler.
  - Expected: A list/grid shows default properties, each displaying title/location, price per night, and a way to view details.
  - Verified: Grid of 6 default properties, each with title, location, rating, guests/beds, "$X / night", image, and a link to /property/:id.

- [ ] FT-03: Filter by price range works
  - Action: Set a min and max nightly price in the price filter and apply.
  - Expected: Only listings with nightly price within the entered range are displayed; others are hidden.
  - Bug Report:
    - Issue: Missing control — no maximum price input
    - Actual: The "Price Range (per night)" filter exposes only a single slider thumb labeled "Minimum" (0–500) with a static "$500+" label; a custom maximum price cannot be entered. Min filtering works (min $180 hid the $165 cottage → "5 Properties Found"; min $500 → "0 Properties Found"; the $450 villa remained at min $180), but a two-sided range (e.g., $100–$300) is impossible.

- [X] FT-04: Filter by number of guests works
  - Action: Enter/select a guest count (e.g., 4) in the guests filter and apply.
  - Expected: Only listings that accommodate at least that number of guests are shown.
  - Verified: Guests = 4 → "5 Properties Found"; the 2-guest "Sleek City Penthouse" was hidden; remaining cards show ≥4 guests.

- [X] FT-05: Filter by property type works
  - Action: Select a property type (e.g., "Apartment") in the type filter and apply.
  - Expected: Only listings of the selected type are displayed.
  - Verified: Type options [All types, House, Apartment, Villa, Cabin, Cottage]; selecting Apartment → "2 Properties Found" (Modern Loft, Sleek City Penthouse), both badged "apartment".

- [X] FT-06: Sort by price works
  - Action: Apply the "Price" sort option (ascending, then descending).
  - Expected: Listings reorder by nightly price low-to-high, then high-to-low.
  - Verified: Low-to-High: $165, $185, $295, $320, $375, $450. High-to-Low: $450, $375, $320, $295, $185, $165.

- [X] FT-07: Sort by rating works
  - Action: Apply the "Rating" sort option.
  - Expected: Listings reorder by rating (highest-rated first, or the displayed order matches the selected direction).
  - Verified: "Top Rated" order: 4.9, 4.9, 4.8, 4.7, 4.7, 4.6 (descending).

- [X] FT-08: Each listing has its own detail page
  - Action: Click a listing from the browse list.
  - Expected: A dedicated detail page opens showing the full description, basic reviews, and available dates for that listing.
  - Verified: /property/1 shows "About this place" full description, "What this place offers" amenities, "Reviews (3)", photo gallery, and a date picker in the booking widget where available dates are selectable and past/booked days (e.g., Nov 25) are disabled. Confirmed also for created listing /property/prop-1794112994696.

- [X] FT-09: Traveler can submit a booking request for chosen dates
  - Action: On a listing's detail page, open the booking request form, enter check-in/check-out dates within available dates, and submit.
  - Expected: The booking request is submitted successfully and stored against that listing.
  - Verified: On Charming Coastal Cottage, submitted check-in Nov 12 / check-out Nov 14 with name/email; form accepted and the request was stored (appeared in owner's Bookings as pending for that listing).

- [ ] FT-10: Owner can view booking requests
  - Action: Open the owner's booking requests view.
  - Expected: Submitted requests are listed with traveler, listing, chosen dates, and current status.
  - Bug Report:
    - Issue: Incorrect date display in requests list
    - Actual: All fields are present (traveler, email, listing, guests, Pending/History status, Approve/Decline), but the "chosen dates" are displayed one day before what the traveler selected: booked Nov 12–14 → card shows "Nov 11 - Nov 13, 2026"; booked Nov 16–18 → card shows "Nov 15 - Nov 17, 2026" (UTC off-by-one formatting).

- [X] FT-11: Owner can update the status of a booking request
  - Action: From the owner's requests view, change a request's status (e.g., Approve/Accept or Decline) and save.
  - Expected: The new status is saved and displayed for that request.
  - Verified: Approve on "John Smith" → moved to History shown as "Approved" (Pending 2→1, History 1→2). Decline on "Overlap Tester" → moved to History shown as "Seaside Villa with Infinity Pool — Declined" (Pending 3→2, History 2→3), with a "Booking declined" toast.

## Constraint
- [X] CS-01: Listing form rejects missing required fields
  - Action: Open "Create Listing", leave required fields (e.g., location and nightly price) empty, and submit.
  - Expected: Submission is blocked and a validation error identifies the missing required field(s); no partial listing is created.
  - Verified: Submit with empty form stays on /create-listing; form.checkValidity() = false; title/location/description/price/max-guests inputs carry required=true and native validation reports "Please fill out this field." on the offending field; no listing was added (count unchanged until valid submission).

- [X] CS-02: Nightly price must be a valid positive number
  - Action: Enter a negative value, zero, or non-numeric text in the nightly price field and submit.
  - Expected: Submission is blocked with a validation message; the listing is not created.
  - Verified: Price field is type=number with min=1. −50 → blocked, validationMessage "Value must be greater than or equal to 1."; 0 → blocked, same message; non-numeric text cannot be entered. Page remained on /create-listing with no new listing.

- [ ] CS-03: Booking dates must be valid (check-out after check-in)
  - Action: In the booking request form, enter a check-out date equal to or earlier than the check-in date and submit.
  - Expected: Submission is blocked with an error indicating invalid date range.
  - Bug Report:
    - Issue: Missing/absent validation error message for invalid date ranges
    - Actual: With check-in Nov 20, earlier check-out days (Nov 18) are disabled in the picker (selection prevented, but no error message shown). A same-day check-out (Nov 20) appears enabled and clickable in the check-out calendar, yet clicking it is silently ignored — check-out stays "Select" with no validation error or any indication of why. No error message indicating an invalid date range is ever surfaced.

- [ ] CS-04: Unavailable dates cannot be booked
  - Action: In the booking request form, select dates that include an unavailable/already-booked range shown on the detail page, and submit.
  - Expected: Submission is rejected with a message that the selected dates are not available.
  - Bug Report:
    - Issue: Unavailable dates are accepted in booking request
    - Actual: On Seaside Villa, Nov 17 was shown disabled (booked) in the calendar. Submitted check-in Nov 16 → check-out Nov 18, spanning the booked day. No rejection or "not available" message appeared; the request was accepted and listed in the owner's Pending bookings ("Seaside Villa with Infinity Pool — Nov 15 - Nov 17 — Overlap Tester"). The check-out picker only disables the booked day itself, not ranges that span it, and no overlap validation occurs on submit. (Same behavior observed for Nov 24→26 spanning booked Nov 25: silently accepted.)

## Interaction
- [X] IX-01: Success feedback after submitting a booking request
  - Action: Submit a valid booking request.
  - Expected: A visible confirmation (toast/success message) confirms the request was sent and is pending owner review.
  - Verified: Toast displayed: "Booking request sent! The property owner will review your request shortly." Form fields reset after submit.

- [X] IX-02: Empty-state message when filters return no results
  - Action: Apply a filter combination matching no listings (e.g., max price below the cheapest listing).
  - Expected: A clear "no properties found" message appears instead of a blank list or broken layout.
  - Verified: With price minimum set to $500 (above all listings), page shows "0 Properties Found" plus "No properties match your filters. Try adjusting your search criteria." — clean empty state, no broken layout.

- [X] IX-03: Status change reflects immediately in the owner's requests list
  - Action: Approve or decline a booking request as owner, then view/update the requests list.
  - Expected: The request shows the updated status without stale "Pending" data remaining.
  - Verified: Approve and Decline actions updated the list in-place without reload: "Pending (3)" → "Pending (2)", card removed from Pending and re-rendered under History with "Approved"/"Declined" badges; no stale Pending entry remained.

## Content
- [X] CT-01: Listing photos render from image URLs
  - Action: Inspect the browse list and detail pages for listings created with photo image URLs.
  - Expected: Images load and display correctly (no broken-image icons or empty placeholders).
  - Verified: All 6 default browse-card images loaded (naturalWidth > 0, unsplash.com URLs). Detail gallery of /property/1: 3/3 photos loaded (800px). Newly created listing's entered image URL rendered on both the browse card and detail page (naturalWidth > 0). Cottages/loft/cabin/penthouse details: all images loaded. No broken images observed.

- [X] CT-02: Default listing content is relevant and complete
  - Action: Review default listings' titles, locations, descriptions, amenities, ratings, and reviews on list and detail pages.
  - Expected: All content is coherent short-term-rental information (no lorem ipsum, "TODO", or placeholder text); reviews show reviewer name/rating with text.
  - Verified: All 6 listings reviewed (details of props 1–6): coherent location-specific descriptions (Santorini, Barcelona, Aspen, Cornwall, Tulum, Tokyo), amenity lists, ratings + review counts (e.g., "4.9 (127 reviews)"), and reviews with reviewer name, rating, text, and date (e.g., "Emma S. — 5 — Absolutely magical! The sunset views are even better than the photos. — October 15, 2024"). Text scan found no lorem/TODO/FIXME/placeholder strings; the new user-created listing correctly shows "No reviews yet. Be the first to stay here" empty state.