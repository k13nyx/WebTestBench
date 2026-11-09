All testing is complete. I've verified every checklist item, including re-doing FT-02 and the new-listing checks via in-app navigation after discovering that full page reloads reset the app's in-memory state. Here is the complete test report:

# Test Result

## Functionality
- [X] FT-01: Owner can create a new short-term rental listing with all required details.
  - Action: Open the "Create Listing" form, fill Location ("Sample City"), Description ("Sample description"), Amenities ("WiFi, Kitchen"), Photo URL (a valid image URL), Property Type, Max Guests, Available Dates, and Nightly Price (e.g. 100), then click "Save"/"Create".
  - Expected: The new listing is created and appears in the property list with the entered location and nightly price.
  - Note: The form offers Title, Location, Property Type, Description, Price per Night, Max Guests, Bedrooms, Bathrooms, Amenities, and Photo URL — there is no "Available Dates" field to fill (availability is managed via per-date calendars). All provided fields were filled (title "Sample Listing", Location "Sample City", type Apartment, price 100, Max Guests 4, WiFi + Kitchen, valid image URL). The listing was created and appeared in the list as "Sample Listing / Sample City / $100 / night" ("7 Properties Found").

- [X] FT-02: Owner can edit an existing listing and save the changes.
  - Action: Open a default listing in the owner's management view, change the Nightly Price to a different valid value, and click "Save"/"Update".
  - Expected: The listing's detail page and list entry show the updated nightly price; other fields remain unchanged.

- [X] FT-03: Traveler can browse all available properties in a list.
  - Action: Open the property browse page without applying any filter.
  - Expected: A list of all default available properties is displayed, each entry showing its title/name and nightly price.

- [X] FT-04: Traveler can filter properties by price range.
  - Action: Set the price range filter (Min Price / Max Price) to a range that matches only some default listings, and apply it.
  - Expected: The list shows only listings whose nightly price falls within the entered range; listings outside the range are hidden.
  - Note: The UI provides a single "Minimum" price slider ($0–$500+) rather than separate Min/Max inputs. With Minimum set to 300 (range 300–500+), only $450, $375, and $320 listings were shown; the $295, $185, $165 listings were hidden — filtering by the entered range works correctly.

- [X] FT-05: Traveler can filter properties by number of guests.
  - Action: Set the Guests filter to a value (e.g. 4) and apply it.
  - Expected: The list shows only listings whose guest capacity is greater than or equal to the entered number of guests.

- [X] FT-06: Traveler can filter properties by property type.
  - Action: Select one property type (e.g. "Apartment") from the Property Type filter and apply it.
  - Expected: The list shows only listings of the selected property type; other types are hidden.

- [X] FT-07: Traveler can sort results by price and by rating.
  - Action: Select "Price" sort option, then select "Rating" sort option.
  - Expected: With price sorting, listings are ordered by nightly price (low-to-high or high-to-low per the selected option); with rating sorting, listings are ordered by average rating descending.
  - Note: Sort options are "Top Rated", "Price: Low to High", "Price: High to Low". Price: Low to High produced $100 → $165 → $185 → $295 → $320 → $375 → $450; Top Rated produced 4.9 → 4.9 → 4.8 → 4.7 → 4.7 → 4.6 (rating descending).

- [X] FT-08: Each listing has a detail page with full description, basic reviews, and available dates.
  - Action: Click a default listing in the browse list to open its detail page.
  - Expected: The page shows the full description, at least one review with rating and comment, and an available-dates display (calendar or date list).

- [ ] FT-09: Traveler can submit a booking request for chosen dates.
  - Action: On a listing detail page, choose an available Start Date and End Date, fill in guest name and email, and click "Request Booking"/"Book".
  - Expected: The booking request is created and listed for that property.
  - Bug Report:
    - Issue: Incorrect booking dates recorded (off-by-one date shift in booking submission)
    - Actual: The booking form's date buttons showed Check-in "Nov 16" and Check-out "Nov 17" (2026) for Seaside Villa; after clicking "Request to Book" the request was created and listed in the owner's Bookings view as "Seaside Villa with Infinity Pool ... Nov 15 - Nov 16, 2026" — one day earlier than the chosen dates. The request is created and listed for the property, but not for the chosen dates (same -1 day shift observed on all submitted requests).

- [X] FT-10: Owner can view booking requests and update their status.
  - Action: Open the owner's booking requests view for a listing that has a pending request, and change its status (e.g. to "Approved").
  - Expected: The request appears in the requests list with its dates and guest info, and after the update shows the new status.

## Constraint
- [X] CS-01: Listing form cannot be submitted with empty required fields.
  - Action: Open the "Create Listing" form, leave Location, Description, and Nightly Price empty, and click "Save"/"Create".
  - Expected: The listing is not created; an error/validation message indicates the required fields must be filled.
  - Note: Submission is blocked by native HTML5 validation (required attributes on Title/Location/Description/Price/Max Guests); the browser shows its validation message ("Please fill out this field") on the first empty required field, and no listing is created.

- [X] CS-02: Nightly price must be a positive number.
  - Action: In the listing form, enter Nightly Price as "0", then as "-50", then as "abc", submitting each time.
  - Expected: Each submission is rejected with a price validation message; no listing with a non-positive or non-numeric price is created.
  - Note: The price input is type=number with min="1". "0" and "-50" are rejected with the validation message "Value must be greater than or equal to 1" on the price field; "abc" cannot be entered in a number input (field stays empty) and is rejected with a validation message on the price field. Verified no listing was created in any of the three cases.

- [ ] CS-03: Photo entry must be a valid image URL.
  - Action: In the listing form, enter "not-a-url" in the Photo URL field and submit with all other fields valid.
  - Expected: The submission is rejected with a URL validation message; no listing is created with an invalid photo URL.
  - Bug Report:
    - Issue: Missing photo URL validation (invalid image URL accepted)
    - Actual: With Photo URL "not-a-url" and all other fields valid, clicking "Create Listing" succeeded with the toast "Listing created! Your property is now visible to travelers."; the listing "CS3 Test Listing" was created and appears in the browse list ("8 Properties Found"). No URL validation message is displayed.

- [ ] CS-04: Booking end date must be after the start date.
  - Action: On the booking request form, set Start Date later than End Date and submit.
  - Expected: The request is rejected with a date-range error message; no booking request is created.
  - Bug Report:
    - Issue: Missing date-range validation on booking form (end date before start date accepted)
    - Actual: With Check-in "Nov 29" and Check-out "Nov 26" (end before start) shown in the form's date buttons, clicking "Request to Book" succeeded with the toast "Booking request sent! The property owner will review your request shortly." and created the request (listed as "Nov 28 - Nov 25, 2026" — end before start). No date-range error message is displayed.

- [ ] CS-05: Booking request cannot be submitted for unavailable dates.
  - Action: On the booking form for a default listing, choose dates that are outside the listing's available dates (or already booked) and submit.
  - Expected: The request is rejected with a message indicating the dates are not available; no booking request is created.
  - Bug Report:
    - Issue: Missing availability validation on booking form (request accepted for unavailable dates)
    - Actual: For Seaside Villa (whose calendar disables Nov 25 as unavailable), a request with Check-in "Nov 24" and Check-out "Nov 27" — a range spanning the unavailable Nov 25 — was accepted with "Booking request sent!" and created (listed as "Nov 23 - Nov 26, 2026"). No "dates are not available" message is displayed.

## Interaction
- [X] IX-01: Creating a listing gives clear success feedback.
  - Action: Submit a valid "Create Listing" form and observe the screen immediately after.
  - Expected: A success confirmation (message or toast) is displayed indicating the listing was created.

- [X] IX-02: Submitting a booking request gives clear success feedback.
  - Action: Submit a valid booking request form and observe the screen immediately after.
  - Expected: A success confirmation (message or toast) is displayed indicating the request was submitted.

- [X] IX-03: Filter and sort changes update the results list immediately.
  - Action: Change any filter (price, guests, type) or sort option on the browse page and observe the list.
  - Expected: The results list refreshes in place to reflect the new filter/sort without needing a manual page reload.

## Content
- [X] CT-01: Listing detail page content matches the listing's entered data.
  - Action: Open a default listing's detail page and compare displayed location, description, amenities, nightly price, and photos against its data.
  - Expected: All displayed text and photo images correspond exactly to that listing's data; photos load and depict the property, not broken/placeholder images.

- [ ] CT-02: Browse list entries show relevant, consistent summary info.
  - Action: Inspect each entry in the property browse list.
  - Expected: Every entry shows the property name/title, location, nightly price, property type, and rating, and these values match the listing's detail page.
  - Bug Report:
    - Issue: Missing rating element in browse list entries for listings without reviews (inconsistent summary info)
    - Actual: Default listing entries show all five values (e.g. "Villa | Seaside Villa with Infinity Pool | 4.9 | Santorini, Greece | $450 / night", matching its detail page), but entries for newly created listings ("Sample Listing | Sample City | $100 / night", "CS3 Test Listing | Testville | $100 / night") display no rating value at all, so not every entry shows the five required summary values. (The other displayed values do match those listings' detail pages.)