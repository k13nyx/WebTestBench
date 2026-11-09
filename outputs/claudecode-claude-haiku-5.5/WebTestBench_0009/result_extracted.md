# Test Result

## Functionality
- [ ] FT-01: Owner can create a new listing with all required details
  - Action: Open the owner's "Create Listing" form, enter a location, description, nightly price, property type, max guests, one or more amenities, and one or more photo URLs, then click "Save Listing".
  - Expected: The listing is saved and appears in the owner's listing management view with every entered value shown unchanged.
  - Bug Report:
    - Issue: Missing Owner Listing Management View
    - Actual: The listing saved, and its values (title, location, Villa, $180, 4 guests, WiFi/Kitchen/Pool, photo URL, description) were unchanged on the detail and Edit pages. It appeared in the public browse list. However, owner navigation has only "Create Listing" and "Bookings", with no listing management view. The submit button is labelled "Create Listing", not "Save Listing", and the toast reads "Listing created!", not "Listing saved".

- [ ] FT-02: Owner can edit an existing listing
  - Action: In owner listing management, open a default listing, change its nightly price to a new value and its description to new text, then click "Save Changes".
  - Expected: The new price and description appear in the owner view and on that listing's public detail page.
  - Bug Report:
    - Issue: Edited Listing Disappears From Browse and Public Page
    - Actual: Saving Seaside Villa (id 1) with price $525 showed "Listing updated!", but the browse list dropped to "5 Properties Found" and the villa vanished. The price slider tops out at $500, so the default list hides the listing. Its public detail page could not be reached to confirm $525. Saving the description alone at $450 did update the detail page ("QA FT-02 updated description for Seaside Villa.").

- [X] FT-03: Traveler can browse all available listings in a list
  - Action: Open the browse page without applying any filter or sort.
  - Expected: Every default listing appears as a card showing title, location, nightly price, property type, and rating.

- [ ] FT-04: Traveler can filter listings by price range, number of guests, and property type
  - Action: Set Min price to 100 and Max price to 250, set Guests to 2, set Property type to "Apartment", then click "Apply Filters".
  - Expected: Only listings with nightly price between 100 and 250, max guests of at least 2, and type "Apartment" are shown.
  - Bug Report:
    - Issue: Missing Price Range Controls and Apply Button
    - Actual: The filter panel has only one price slider ("Minimum", range $0–$500+) and no Max price input. There is no "Apply Filters" button; filters apply on change. Guests = 2 with type = Apartment returned 2 listings ($185 Loft, $320 Penthouse), which is correct. The Min 100 / Max 250 range could not be set.

- [X] FT-05: Traveler can sort listings by price and by rating
  - Action: Select "Price: Low to High", then "Price: High to Low", then "Rating: High to Low" from the Sort dropdown.
  - Expected: The list reorders correctly for each option (ascending price, descending price, descending rating).

- [X] FT-06: Listing detail page shows the full listing information
  - Action: Click any listing card and review the detail page.
  - Expected: The page shows the full description, all amenities, all photos, location, nightly price, and property type.

- [X] FT-07: Listing detail page shows available and unavailable dates
  - Action: Open a listing detail page and view the "Availability" calendar.
  - Expected: The calendar displays booked dates as unavailable and remaining future dates as selectable.

- [ ] FT-08: Traveler can submit a booking request for chosen dates
  - Action: On a listing detail page, select an available check-in and check-out date, enter guests = 2, traveler name, and email, then click "Request to Book".
  - Expected: A booking request is created with status "Pending" and the dates and guest count shown as entered.
  - Bug Report:
    - Issue: Incorrect Booking Dates Shown
    - Actual: Selected check-in Nov 17 and check-out Nov 20, 2026. The owner's Bookings page shows "Nov 16 - Nov 19, 2026", which is off by one day. Status "Pending" and 2 guests were correct. The confirmation reads "Booking request sent!", not "Booking request submitted".

- [ ] FT-09: Owner can view booking requests and update their status
  - Action: Log in as the listing owner, open "Booking Requests", select a Pending request, and change its status to "Accepted", then reload the page.
  - Expected: The request appears under the owner's listing, and its status shows "Accepted" after reload.
  - Bug Report:
    - Issue: Status Change Not Persisted After Reload
    - Actual: The request appeared under Seaside Villa as Pending. "Approve" (no "Accepted" option) moved it to History with status "Approved". After reloading /manage-bookings, the request was gone entirely (Pending (2), History (1)). No owner login exists, so there was no "log in" step.

## Constraint
- [ ] CS-01: Listing creation is blocked when required fields are empty
  - Action: Open "Create Listing", leave Location, Nightly price, and Description empty, then click "Save Listing".
  - Expected: The listing is not saved, and each empty required field is marked with an error message.
  - Bug Report:
    - Issue: Missing Per-Field Error Messages
    - Actual: The listing was not saved and the page stayed on /create-listing. Only native browser validation fired (focus moved to Property Title). No per-field error text appeared in the DOM for Location, Description, or Price.

- [ ] CS-02: Listing creation rejects an invalid nightly price or photo URL
  - Action: Enter Nightly price = -50 and Photo URL = "not-a-url", then click "Save Listing".
  - Expected: The listing is not saved, and an error message identifies the invalid price and invalid URL.
  - Bug Report:
    - Issue: Invalid Photo URL Not Validated; No Error Messages
    - Actual: The listing was not saved, but only because the price input failed native min validation (validity.valid = false). No error text appeared. The photo URL input is type="text" and accepted "not-a-url" (validity.valid = true).

- [ ] CS-03: Booking is blocked when check-out is not after check-in
  - Action: On a listing detail page, select the same date for check-in and check-out, then click "Request to Book".
  - Expected: The request is not submitted, and the message "Check-out must be after check-in" appears.
  - Bug Report:
    - Issue: Expected Validation Message Missing
    - Actual: After check-in = Nov 17, the check-out calendar disabled Nov 17 and all earlier dates, so the same date could not be chosen. "Request to Book" stayed disabled, and "Check-out must be after check-in" never appeared.

- [ ] CS-04: Booking is blocked for dates already marked unavailable
  - Action: Attempt to select a date shown as unavailable on the calendar as check-in, then try to submit a booking spanning it.
  - Expected: The unavailable date cannot be selected, and any booking spanning it is rejected with a message stating the dates are unavailable.
  - Bug Report:
    - Issue: Incomplete Verification (Spanning Case Not Executed)
    - Actual: Future dates shown as unavailable (e.g., Nov 13, 18, 19, 21, 24, 30) are disabled and cannot be selected as check-in. The spanning-booking case (e.g., Nov 11 → Nov 14 across Nov 13) and its rejection message were not tested within the tool budget.

- [ ] CS-05: Booking is blocked when guest count exceeds the listing's maximum
  - Action: On a listing with a stated max guests value, enter one more guest than that value and submit the booking request.
  - Expected: The request is not submitted, and a message states the maximum guest count for the listing.
  - Bug Report:
    - Issue: No Guest-Limit Message
    - Actual: On the 6-guest Seaside Villa, entering 7 guests (with name and email) and clicking "Request to Book" showed no message and no toast. The request did not appear in the owner's Bookings page, so it was silently dropped. The "Max 6 guests" hint is the only text.

- [ ] CS-06: Owner can view only booking requests for their own listings
  - Action: Log in as an owner, open "Booking Requests", and check every request shown.
  - Expected: Only requests for listings owned by the logged-in owner appear; requests for other owners' listings are not visible.
  - Bug Report:
    - Issue: Owner Scoping Not Verifiable
    - Actual: The app has no owner login or identity, only a traveler/owner role toggle. The Booking Requests page lists requests for Seaside Villa and Mountain Retreat Cabin with no owner indication, so filtering to the logged-in owner's listings cannot be confirmed.

## Interaction
- [ ] IX-01: System shows confirmation after saving a listing or submitting a booking request
  - Action: Save a listing via "Save Listing", then submit a booking request via "Request to Book".
  - Expected: A success message "Listing saved" appears after saving, and "Booking request submitted" appears after submitting, without a page reload.
  - Bug Report:
    - Issue: Confirmation Text Mismatch
    - Actual: Saving a listing showed "Listing created!" (not "Listing saved"). Submitting a booking showed "Booking request sent!" (not "Booking request submitted"). Both appeared in-page without a reload.

- [ ] IX-02: Filter and sort results update immediately, with a no-results message when applicable
  - Action: Apply a price range that matches no listing (Min 5000, Max 6000), then clear it, then select a sort option.
  - Expected: The list updates without a page reload, shows "0 listings found" with a "No results" message for the impossible range, and restores all listings when cleared.
  - Bug Report:
    - Issue: Price Range Cannot Express Requested Range
    - Actual: The price control is a single minimum slider capped at $500 with no Max input, so Min 5000 / Max 6000 cannot be applied. Sort and Clear Filters did update in-page without reload (Clear restored 6 listings). A zero-result state displays "0 Properties Found" with "No properties match your filters." (seen via search), but the wording differs from "0 listings found" / "No results".

## Content
- [ ] CT-01: Listing photos load and match the property
  - Action: Open each default listing's detail page and view all photos.
  - Expected: Every photo loads without a broken image icon and depicts a property consistent with that listing's type and description.
  - Bug Report:
    - Issue: Incomplete Verification (5 of 6 Listings Not Checked)
    - Actual: For Seaside Villa, all 3 photos loaded (naturalWidth > 0) and are consistent with a villa. The detail pages for the other five default listings were not opened within the tool budget.

- [ ] CT-02: Reviews and rating are specific to each listing and consistent with its card
  - Action: On a listing detail page, read the displayed reviews and compare the average rating with the rating on that listing's browse card.
  - Expected: Each review references this property only, and the average of the displayed reviews matches the rating on the browse card.
  - Bug Report:
    - Issue: Rating Mismatch With Displayed Reviews
    - Actual: Seaside Villa's card and header show 4.9 (127 reviews), but the three displayed reviews score 5, 5, and 4, averaging 4.67. The reviews are specific to this property. The other listings were not checked.

- [ ] CT-03: Listing details are consistent between browse cards and detail pages
  - Action: For three default listings, compare the title, location, nightly price, property type, and amenities on the browse card with those on the detail page.
  - Expected: All compared values are identical on both pages for each listing.
  - Bug Report:
    - Issue: Amenities Absent From Browse Cards
    - Actual: For Seaside Villa, title, location, price, and type match between card and detail. Browse cards show no amenities, so the amenities comparison cannot match. Cards also show "3 beds" where the detail page shows "3 bedrooms". Only one listing was compared (the other two were not checked).
