# Test Checklist

## Functionality
- [ ] FT-01: Owner can create a new listing with all required details
  - Action: Open the owner's "Create Listing" form, enter a location, description, nightly price, property type, max guests, one or more amenities, and one or more photo URLs, then click "Save Listing".
  - Expected: The listing is saved and appears in the owner's listing management view with every entered value shown unchanged.
- [ ] FT-02: Owner can edit an existing listing
  - Action: In owner listing management, open a default listing, change its nightly price to a new value and its description to new text, then click "Save Changes".
  - Expected: The new price and description appear in the owner view and on that listing's public detail page.
- [ ] FT-03: Traveler can browse all available listings in a list
  - Action: Open the browse page without applying any filter or sort.
  - Expected: Every default listing appears as a card showing title, location, nightly price, property type, and rating.
- [ ] FT-04: Traveler can filter listings by price range, number of guests, and property type
  - Action: Set Min price to 100 and Max price to 250, set Guests to 2, set Property type to "Apartment", then click "Apply Filters".
  - Expected: Only listings with nightly price between 100 and 250, max guests of at least 2, and type "Apartment" are shown.
- [ ] FT-05: Traveler can sort listings by price and by rating
  - Action: Select "Price: Low to High", then "Price: High to Low", then "Rating: High to Low" from the Sort dropdown.
  - Expected: The list reorders correctly for each option (ascending price, descending price, descending rating).
- [ ] FT-06: Listing detail page shows the full listing information
  - Action: Click any listing card and review the detail page.
  - Expected: The page shows the full description, all amenities, all photos, location, nightly price, and property type.
- [ ] FT-07: Listing detail page shows available and unavailable dates
  - Action: Open a listing detail page and view the "Availability" calendar.
  - Expected: The calendar displays booked dates as unavailable and remaining future dates as selectable.
- [ ] FT-08: Traveler can submit a booking request for chosen dates
  - Action: On a listing detail page, select an available check-in and check-out date, enter guests = 2, traveler name, and email, then click "Request to Book".
  - Expected: A booking request is created with status "Pending" and the dates and guest count shown as entered.
- [ ] FT-09: Owner can view booking requests and update their status
  - Action: Log in as the listing owner, open "Booking Requests", select a Pending request, and change its status to "Accepted", then reload the page.
  - Expected: The request appears under the owner's listing, and its status shows "Accepted" after reload.

## Constraint
- [ ] CS-01: Listing creation is blocked when required fields are empty
  - Action: Open "Create Listing", leave Location, Nightly price, and Description empty, then click "Save Listing".
  - Expected: The listing is not saved, and each empty required field is marked with an error message.
- [ ] CS-02: Listing creation rejects an invalid nightly price or photo URL
  - Action: Enter Nightly price = -50 and Photo URL = "not-a-url", then click "Save Listing".
  - Expected: The listing is not saved, and an error message identifies the invalid price and invalid URL.
- [ ] CS-03: Booking is blocked when check-out is not after check-in
  - Action: On a listing detail page, select the same date for check-in and check-out, then click "Request to Book".
  - Expected: The request is not submitted, and the message "Check-out must be after check-in" appears.
- [ ] CS-04: Booking is blocked for dates already marked unavailable
  - Action: Attempt to select a date shown as unavailable on the calendar as check-in, then try to submit a booking spanning it.
  - Expected: The unavailable date cannot be selected, and any booking spanning it is rejected with a message stating the dates are unavailable.
- [ ] CS-05: Booking is blocked when guest count exceeds the listing's maximum
  - Action: On a listing with a stated max guests value, enter one more guest than that value and submit the booking request.
  - Expected: The request is not submitted, and a message states the maximum guest count for the listing.
- [ ] CS-06: Owner can view only booking requests for their own listings
  - Action: Log in as an owner, open "Booking Requests", and check every request shown.
  - Expected: Only requests for listings owned by the logged-in owner appear; requests for other owners' listings are not visible.

## Interaction
- [ ] IX-01: System shows confirmation after saving a listing or submitting a booking request
  - Action: Save a listing via "Save Listing", then submit a booking request via "Request to Book".
  - Expected: A success message "Listing saved" appears after saving, and "Booking request submitted" appears after submitting, without a page reload.
- [ ] IX-02: Filter and sort results update immediately, with a no-results message when applicable
  - Action: Apply a price range that matches no listing (Min 5000, Max 6000), then clear it, then select a sort option.
  - Expected: The list updates without a page reload, shows "0 listings found" with a "No results" message for the impossible range, and restores all listings when cleared.

## Content
- [ ] CT-01: Listing photos load and match the property
  - Action: Open each default listing's detail page and view all photos.
  - Expected: Every photo loads without a broken image icon and depicts a property consistent with that listing's type and description.
- [ ] CT-02: Reviews and rating are specific to each listing and consistent with its card
  - Action: On a listing detail page, read the displayed reviews and compare the average rating with the rating on that listing's browse card.
  - Expected: Each review references this property only, and the average of the displayed reviews matches the rating on the browse card.
- [ ] CT-03: Listing details are consistent between browse cards and detail pages
  - Action: For three default listings, compare the title, location, nightly price, property type, and amenities on the browse card with those on the detail page.
  - Expected: All compared values are identical on both pages for each listing.