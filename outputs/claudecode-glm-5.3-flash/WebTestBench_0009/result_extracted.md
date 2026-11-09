# Test Result

## Functionality

- [X] TEST-ID: FT-01: Owner can create a new listing
  - Action: Open the "Create Listing" form, enter location, description, amenities, at least one image URL, a property type, max guests, and a nightly price (e.g., "120"), then submit.
  - Expected: The listing is saved successfully and appears in the listings/browse view with the entered details.
  - Result: PASS — Created "Sunset Harbor Bungalow" (Key West, Florida, Villa, $120/night, 6 guests, WiFi+Pool, valid image URL). Browse list updated to "7 Properties Found" showing the new card with the entered title, location, guest count, and price; detail page reflected all entered data.

- [X] TEST-ID: FT-02: Owner can edit an existing listing
  - Action: Open one of the owner's existing listings, change the nightly price (e.g., to "150"), and save.
  - Expected: The detail page and list view show the updated price of "150" per night.
  - Result: PASS — Via the "Edit" link on the detail page (/edit-listing/...), changed price to 150 and saved with "Save Changes". Browse card shows "$150 / night" and the detail page shows "$150" ($120 no longer present).

- [X] TEST-ID: FT-03: Traveler can view listing detail page
  - Action: Click any property card in the browse list.
  - Expected: A detail page opens showing the full description, amenities, photos, property type, max guests, nightly price, and location.
  - Result: PASS — Clicking a card opens /property/{id} showing type badge, title, location, guest/bed/bath counts, full "About this place" description, "What this place offers" amenities, photo gallery, and "$X / night" sidebar.

- [X] TEST-ID: FT-04: Reviews are visible on the detail page
  - Action: Open the detail page of a property that has reviews.
  - Expected: Basic reviews are displayed, each showing the reviewer name/comment and a star rating.
  - Result: PASS — Seaside Villa shows "Reviews (3)": Emma S. (5★, comment, October 15, 2024), Marcus T. (5★, comment), Sophie L. (4★, comment) with star icons and numeric ratings.

- [X] TEST-ID: FT-05: Available dates are visible on the detail page
  - Action: Open the detail page of a property.
  - Expected: The page shows the property's available (bookable) date range(s) or calendar.
  - Result: PASS — The booking widget's Check-in/Check-out controls open a calendar (November/December 2026) in which bookable days are enabled and unavailable days are visually disabled (past dates plus booked days Nov 14, Nov 25, Dec 3, 2026). Note: availability is presented via the date-picker calendar rather than a static text range on the page.

- [X] TEST-ID: FT-06: Traveler can submit a booking request
  - Action: On a detail page, select/check-in and check-out dates within the available range and submit the booking request form with a guest count within the property's capacity.
  - Expected: The booking request is submitted successfully and a confirmation (message/toast/status) is shown.
  - Result: PASS — Selected Nov 10–12, 2026, 2 guests, name and email on Seaside Villa ($900 total shown). Submission succeeded with toast "Booking request sent!" and the form reset.

- [ ] TEST-ID: FT-07: Owner can view incoming booking requests
  - Action: Open the owner's booking request management view.
  - Expected: The request submitted in FT-06 is listed, showing the property, dates, and guests.
  - Bug Report:
    - Issue: Incorrect data display — booking dates shown to the owner are off by one day from what the traveler selected
    - Actual: In /manage-bookings the submitted requests appear (property, guests, name correct), but every date range is shifted one day earlier than selected: traveler selected Nov 10–12 → owner sees "Nov 9 - Nov 11, 2026"; traveler selected Nov 24–27 → owner sees "Nov 23 - Nov 26, 2026"; traveler selected Dec 20–22 → owner sees "Dec 19 - Dec 21, 2026". The booking widget itself displayed the correct dates (Nov 10, Nov 12 / Dec 20, Dec 22), so the two views disagree (systematic one-day shift, likely a UTC/local-timezone conversion bug).

- [X] TEST-ID: FT-08: Owner can update a booking request status
  - Action: In the owner's request view, change the status of the submitted request (e.g., to "Approved" or "Declined") using the provided control.
  - Expected: The status is updated and the new status is displayed for that request.
  - Result: PASS — Clicking "Approve" on the submitted request showed toast "Booking approved — The guest will be notified of your approval.", removed it from "Pending (4)"→"(3)", and listed it under History as "Approved".

- [ ] TEST-ID: FT-09: Filter by price range
  - Action: In the browse list, set a price range filter (e.g., min 100, max 200) and apply.
  - Expected: Only properties with nightly prices within 100–200 are shown; all others are excluded.
  - Bug Report:
    - Issue: Missing feature — no maximum-price control; price filter is minimum-only
    - Actual: The "Price Range (per night)" filter contains a single-thumb slider labeled "Minimum" ($0–$500, step 10) with a static "$500+" label; no maximum control exists anywhere in the sidebar. Setting minimum=200 correctly excluded the $150/$165/$185 properties (4 shown: $450, $295, $375, $320), but properties above the range ($295–$450) can never be excluded, so the expected bounded 100–200 result is not achievable.

- [X] TEST-ID: FT-10: Filter by number of guests
  - Action: Set the guest filter to a value (e.g., 4 guests) and apply.
  - Expected: Only properties that can accommodate at least 4 guests are shown.
  - Result: PASS — Guests=4 returned 6 of 7 properties (6, 6, 8, 4, 4, 6 guests); "Sleek City Penthouse" (2 guests) was correctly excluded.

- [X] TEST-ID: FT-11: Filter by property type
  - Action: Select one property type (e.g., "Apartment") from the type filter and apply.
  - Expected: Only properties of that type are shown.
  - Result: PASS — Selecting "Apartment" showed exactly 2 properties ("Modern Loft in Historic District", "Sleek City Penthouse"); the combobox displays "Apartment".

- [X] TEST-ID: FT-12: Sort results by price
  - Action: With results shown, choose "Sort by price" (lowest first).
  - Expected: The list is reordered so the cheapest property appears first.
  - Result: PASS — "Price: Low to High" ordered the 7 listings $150 → $165 → $185 → $295 → $320 → $375 → $450.

- [X] TEST-ID: FT-13: Sort results by rating
  - Action: Choose "Sort by rating" (highest first).
  - Expected: The list is reordered so the highest-rated property appears first.
  - Result: PASS — "Top Rated" ordered listings 4.9 → 4.9 → 4.8 → 4.7 → 4.7 → 4.6, with the unrated newly created listing placed last.

## Constraint

- [X] TEST-ID: CS-01: Cannot create a listing with missing required fields
  - Action: Open the create-listing form, leave required fields (e.g., location or price) empty, and submit.
  - Expected: Submission is blocked and a validation error is shown; no listing is created.
  - Result: PASS — Submitting the empty form was blocked (stay on /create-listing, focus moved to first invalid field); required fields carry validation ("Please fill out this field." on title, location, description, price, guests). No listing was created.

- [X] TEST-ID: CS-02: Nightly price must be a valid positive number
  - Action: Enter an invalid price (e.g., "0", "-50", or "abc") in the create/edit form and submit.
  - Expected: Submission is rejected with a clear validation message.
  - Result: PASS — Price "0" and "-50" both blocked submission with message "Value must be greater than or equal to 1." (input min=1); "abc" cannot be entered at all (input type=number). No listing was created.

- [X] TEST-ID: CS-03: Booking with check-out date not after check-in is blocked
  - Action: In the booking form, select a check-out date equal to or before the check-in date and submit.
  - Expected: Submission is rejected with an error message; no request is created.
  - Result: PASS (enforced by prevention) — With check-in = Nov 26, every day ≤ Nov 26 is disabled in the check-out calendar (only Nov 27+ selectable), so an equal-or-earlier check-out cannot be selected and an invalid request cannot be submitted. Note: protection is at the date-picker level (disabled day buttons) rather than an error message displayed on submit.

- [X] TEST-ID: CS-04: Booking for more guests than property capacity is blocked
  - Action: Submit a booking request with a guest count exceeding the property's maximum guests (e.g., 10 guests for a 4-guest property).
  - Expected: Submission is rejected with an error message.
  - Result: PASS — With 10 guests (max 6) on Seaside Villa, clicking "Request to Book" did not create a request (no "Booking request sent!" appeared); the guests input was flagged invalid with message "Value must be less than or equal to 6." and received focus.

- [ ] TEST-ID: CS-05: Booking dates outside available dates are blocked
  - Action: Submit a booking request with dates outside the property's shown available date range.
  - Expected: Submission is rejected with an error message.
  - Bug Report:
    - Issue: Missing validation — booking range spanning an unavailable/booked date is accepted
    - Actual: On Seaside Villa the calendar marks Nov 25, 2026 as unavailable (disabled in both pickers). However, selecting check-in Nov 24 → check-out Nov 27 (a range spanning the unavailable Nov 25, total $1,350) and submitting was ACCEPTED with the success toast "Booking request sent!" — no error or rejection. Only individual disabled days are blocked; ranges that overlap booked days are not validated on submit, allowing double-booked requests.

- [ ] TEST-ID: CS-06: Image URLs must be valid
  - Action: Enter an empty or malformed image URL in the listing form and submit.
  - Expected: Submission is rejected with a validation error, or the invalid entry is not accepted as a photo.
  - Bug Report:
    - Issue: Missing validation — malformed image URL accepted
    - Actual: With all other fields valid, entering "not-a-valid-url" in the photo field and submitting created the listing successfully (no validation error, redirected to browse). The card rendered the entry as a relative URL "http://localhost:6009/not-a-valid-url" producing a broken image (naturalWidth=0) in both the browse list and detail page.

## Interaction

- [X] TEST-ID: IX-01: Filters update the visible list immediately
  - Action: Apply or clear a filter (e.g., property type) and observe the list.
  - Expected: The list updates dynamically (or after clicking "Apply") without requiring a full page reload, and a "no results" state appears when nothing matches.
  - Result: PASS — Guest, type, price, and sort changes updated the list instantly via client-side re-render (URL unchanged, no reload; count header e.g. "7 Properties Found" → "2 Properties Found" → "0 Properties Found"). With Apartment + 5 guests (impossible combination), the empty state "No properties match your filters. Try adjusting your search criteria." was displayed.

- [X] TEST-ID: IX-02: Feedback after submitting a booking request
  - Action: Submit a valid booking request.
  - Expected: A visible success confirmation (message/toast) appears after submission.
  - Result: PASS — After submitting, a visible toast appeared: "Booking request sent! The property owner will review your request shortly." (button cycled through "Sending..." state and the form reset).

## Content

- [X] TEST-ID: CT-01: Listing images render as property photos
  - Action: Open the browse list and a detail page.
  - Expected: Every displayed image loads successfully (no broken-image icons) and depicts the property/accommodation theme.
  - Result: PASS — All 7 browse card images loaded (naturalWidth > 0), and all 18 detail-page photos across the 6 default listings (3 each) loaded successfully; all are accommodation-themed Unsplash photos (exteriors, pools, interiors). (The only broken image observed was the deliberately malformed URL submitted in the CS-06 test, not default content.)

- [X] TEST-ID: CT-02: Listing details are complete and relevant
  - Action: Open each default listing's detail page.
  - Expected: Each shows non-empty location, description, amenities, property type, nightly price, and guest capacity that match the listing's theme.
  - Result: PASS — All 6 default listings verified: Seaside Villa (Santorini, Greece / Villa / $450 / 6 guests / 440-char description / 8 amenities incl. Infinity Pool, Sea View), Modern Loft (Barcelona / Apartment / $185 / 4 guests / 7 amenities), Mountain Retreat Cabin (Aspen / Cabin / $375 / 8 guests / Hot Tub, Ski Storage), Charming Coastal Cottage (Cornwall / Cottage / $165 / 4 guests / Beach Access, Pet Friendly), Tropical Beach House (Tulum / House / $295 / 6 guests / Beachfront, Hammocks), Sleek City Penthouse (Tokyo / Apartment / $320 / 2 guests / Concierge, Smart Home) — all fields non-empty and theme-consistent.
