All tests executed. Compiling the final results.

# Test Result

## Functionality
- [X] FT-01: Owner can create a new property listing with all required details
  - Action: Open the owner's "Create Listing" page, fill in location, description, at least one amenity, one photo image URL, and a nightly price (e.g., 120), then click the "Create"/"Save" button.
  - Expected: The listing is created and can be found in the app with exactly the entered details (location, description, amenities, photo, price).
  - (Verified twice: "Lakeside Test Retreat" — Lake Geneva, Wisconsin, $120, WiFi, unsplash photo URL; and "Alpine Photo Test Chalet" — Chamonix, France, $140, WiFi + Fireplace, unsplash photo URL. Success toast "Listing created!" shown; detail pages display exactly the entered title, location, description, amenities, photo, and price.)

- [X] FT-02: Newly created listing appears in the traveler's browse list
  - Action: After creating a listing (FT-01), open the property browse list page.
  - Expected: The new listing appears in the list alongside the default listings, showing its photo, location, and nightly price.
  - (List heading changed from "6 Properties Found" to "7 Properties Found"; new card shows its photo, "Lake Geneva, Wisconsin" / "Chamonix, France", and "$120 / $140 / night".)

- [X] FT-03: Traveler can browse all available default properties
  - Action: Open the property list page with no filters or sorting applied.
  - Expected: All default properties are displayed as list items, each showing at least a photo, location, and nightly price.
  - (All 6 default properties displayed — Seaside Villa $450, Tropical Beach House $295, Mountain Retreat Cabin $375, Modern Loft $185, Sleek City Penthouse $320, Charming Coastal Cottage $165 — each with photo, location, and nightly price.)

- [X] FT-04: Listing detail page shows the full description and listing info
  - Action: Click on any default listing from the browse list.
  - Expected: A dedicated detail page opens for that property displaying its full description, location, amenities, and nightly price.
  - (Property/1 detail page shows full "About this place" description, Santorini Greece location, 8 amenities, $450/night, plus reviews and booking widget.)

- [X] FT-05: Traveler can sort listings by price
  - Action: On the list page, choose "Sort by price: low to high", then "high to low".
  - Expected: Listings are re-ordered so nightly prices display in ascending order, then in descending order.
  - ("Price: Low to High" → 165, 185, 295, 320, 375, 450; "Price: High to Low" → 450, 375, 320, 295, 185, 165.)

- [X] FT-06: Traveler can sort listings by rating
  - Action: On the list page, choose "Sort by rating" (high to low).
  - Expected: Listings are re-ordered from the highest-rated to the lowest-rated property.
  - ("Top Rated" selected → order: 4.9, 4.9, 4.8, 4.7, 4.7, 4.6.)

- [ ] FT-07: Traveler can submit a booking request for chosen dates
  - Action: On a listing's detail page, select a check-in and a check-out date and submit the booking request form.
  - Expected: The booking request is successfully submitted and recorded for that listing and those dates.
  - Bug Report:
    - Issue: Incorrect Data Recording (off-by-one-day date recording, timezone handling bug)
    - Actual: The request itself is submitted successfully (success toast "Booking request sent!" appears, and the request is recorded for the correct property with the correct 4-night duration). However, check-in "Nov 14, 2026" and check-out "Nov 18, 2026" were selected on the calendar (buttons displayed "Nov 14"/"Nov 18"; price summary showed "$450 × 4 nights"), yet the recorded request on the owner's page displays "Nov 13 - Nov 17, 2026" — both endpoints shifted one day earlier (browser timezone UTC+7; the app appears to serialize local-midnight dates via UTC, corrupting the recorded dates for non-UTC timezones).

- [X] FT-08: Owner can view booking requests for their listings
  - Action: Open the owner's booking requests page/panel.
  - Expected: The request submitted in FT-07 is listed with the property, the requested dates, and its current status (e.g., "Pending").
  - (Owner → Bookings page shows "Pending (3)"; the submitted request is listed: Seaside Villa with Infinity Pool, "Nov 13 - Nov 17, 2026" [as recorded, see FT-07], 1 guest, Alex Tester, alex.tester@example.com, status "Pending".)

- [X] FT-09: Owner can update the status of a booking request
  - Action: On the requests page, change the pending request's status to "Confirmed" (and optionally another to "Declined") and save.
  - Expected: The request's status is updated and displayed as the newly selected value.
  - (Approve → request moves to History with "Approved" label; Decline on a second request → "Declined" label. Both reflect the newly selected status.)

## Constraint
- [X] CS-01: Listing cannot be created with empty required fields
  - Action: On the "Create Listing" page, leave one or more required fields (location, description, price) empty and click "Create"/"Save".
  - Expected: Submission is blocked, an error indication is shown for the missing fields, and no listing is created.
  - (Native HTML5 validation blocks submission: required fields report "Please fill out this field.", focus moves to the first invalid field, page stays on /create-listing, list count unchanged.)

- [X] CS-02: Listing cannot be created with an invalid nightly price
  - Action: On the "Create Listing" page, fill all fields correctly but enter an invalid price (e.g., -50 or "abc") and submit.
  - Expected: Submission is rejected with an error message about the price, and no listing is created.
  - (Price input has min=1; entering -50 and submitting is blocked with validation message "Value must be greater than or equal to 1." Non-numeric input cannot be entered in the number field. No listing created.)

- [ ] CS-03: Price filter excludes listings outside the selected range
  - Action: On the list page, set a price range filter (e.g., min $50 / max $100) using the default listings' prices.
  - Expected: Only listings with a nightly price within the range are shown; all cheaper or more expensive listings are excluded.
  - Bug Report:
    - Issue: Missing Feature (no maximum price filter — only a minimum-price slider exists)
    - Actual: The "Price Range (per night)" control contains only a single "Minimum" slider (0–$500, step 10). Setting it to $300 correctly excluded cheaper listings ("3 Properties Found": $320, $375, $450; $165/$185/$295 removed, current value visibly shown as "$300"), but there is no way to set a maximum price, so more-expensive listings cannot be excluded and a true min/max range (e.g., $50–$100) cannot be applied.

- [X] CS-04: Guest and property-type filters exclude non-matching listings
  - Action: On the list page, apply a "number of guests" filter (e.g., 4+ guests) and a property-type filter (e.g., "Apartment") separately.
  - Expected: Each filter removes all listings that do not match (fewer guests, or a different property type); only matching listings remain.
  - (Guests = 4 → "5 Properties Found", the 2-guest Sleek City Penthouse excluded, all remaining have ≥4 guests. Property Type = "Apartment" (with guests=4 still active) → "1 Property Found", only the 4-guest Modern Loft apartment remains, all villa/house/cabin/cottage listings excluded.)

- [X] CS-05: Booking request with invalid dates is blocked
  - Action: On a listing's detail page, try to submit the booking form with a check-out date earlier than the check-in date, and once with empty dates.
  - Expected: Submission is blocked with an error indication; no booking request is created.
  - (With a Nov 14 check-in selected, the check-out calendar renders all dates on/before Nov 14 as disabled/unselectable, so a check-out earlier than check-in cannot be chosen. With empty dates, the "Request to Book" button is disabled and cannot be clicked — no request is created.)

## Interaction
- [X] IX-01: Filters and sorting update the results list immediately
  - Action: Apply any filter (price, guests, type) or change the sort option on the list page.
  - Expected: The displayed results update immediately in response to the selection, with the current filter/sort choice visibly indicated.
  - (Every sort change and filter change re-rendered the list instantly; current choices visibly indicated: Sort combobox shows "Price: Low to High"/"Top Rated", price slider shows "$300", type combobox shows "Apartment", guests field holds "4"; result count updates e.g. "6 → 3 → 5 → 1 Properties Found".)

- [X] IX-02: Success feedback is shown after a booking request is submitted
  - Action: Submit a valid booking request form on a listing detail page.
  - Expected: A success message, toast, or on-screen confirmation is displayed telling the user the request was sent.
  - (Toast notification: "Booking request sent! The property owner will review your request shortly." — form resets afterwards.)

- [X] IX-03: Owner gets immediate feedback when a booking status is changed
  - Action: On the requests page, update a request's status (e.g., Pending → Confirmed).
  - Expected: A confirmation is shown and the request's status label updates in place to the new value.
  - (Toast "Booking approved — The guest will be notified of your approval." and "Booking declined — The guest will be notified of your decision."; status labels updated to "Approved"/"Declined" immediately, pending count decremented.)

## Content
- [X] CT-01: Listing photos entered as image URLs are displayed correctly
  - Action: View listing cards on the browse list and the photos on a listing detail page (including a listing created with an image URL).
  - Expected: The images from the provided URLs render as actual photos of the properties, with no broken images.
  - (Created listing with unsplash URL: card image and detail-page photo both load with naturalWidth=800 (actual rendered photo, not broken). Default listings' card and detail photos also all load with naturalWidth=800.)

- [X] CT-02: Reviews shown on a detail page belong to that property
  - Action: Open two different default listings' detail pages and compare their reviews sections.
  - Expected: Each detail page displays basic reviews (rating/comment) that are relevant to that specific property, not identical unrelated text.
  - (Property/1 Seaside Villa: Emma S. "Absolutely magical! The sunset views are even better than the photos.", Marcus T. "Perfect honeymoon destination. The pool is incredible.", Sophie L. Property/2 Modern Loft: James W. "Incredible location and stunning interior design!", Laura M. "Loved the neighborhood. Great restaurants nearby." — distinct, property-specific reviews with ratings and dates.)

- [X] CT-03: Available dates are shown on the listing detail page
  - Action: Open any default listing's detail page and inspect the availability section/calendar.
  - Expected: Available dates for that property are clearly displayed so a visitor can see when it can be booked.
  - (The booking widget's calendar (Nov 2026) clearly distinguishes available dates — selectable/interactive — from unavailable/blocked dates — rendered disabled, e.g., Nov 8, 9, 13, 16, 17, 19, 23, 26, 27 blocked — so a visitor can see exactly when the property can be booked.)