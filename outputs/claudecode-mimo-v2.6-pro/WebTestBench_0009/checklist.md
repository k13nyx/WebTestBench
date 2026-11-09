# Test Checklist

## Functionality
- [ ] FT-01: Owner can create a new short-term rental listing with all required details.
  - Action: Open the "Create Listing" form, fill Location ("Sample City"), Description ("Sample description"), Amenities ("WiFi, Kitchen"), Photo URL (a valid image URL), Property Type, Max Guests, Available Dates, and Nightly Price (e.g. 100), then click "Save"/"Create".
  - Expected: The new listing is created and appears in the property list with the entered location and nightly price.

- [ ] FT-02: Owner can edit an existing listing and save the changes.
  - Action: Open a default listing in the owner's management view, change the Nightly Price to a different valid value, and click "Save"/"Update".
  - Expected: The listing's detail page and list entry show the updated nightly price; other fields remain unchanged.

- [ ] FT-03: Traveler can browse all available properties in a list.
  - Action: Open the property browse page without applying any filter.
  - Expected: A list of all default available properties is displayed, each entry showing its title/name and nightly price.

- [ ] FT-04: Traveler can filter properties by price range.
  - Action: Set the price range filter (Min Price / Max Price) to a range that matches only some default listings, and apply it.
  - Expected: The list shows only listings whose nightly price falls within the entered range; listings outside the range are hidden.

- [ ] FT-05: Traveler can filter properties by number of guests.
  - Action: Set the Guests filter to a value (e.g. 4) and apply it.
  - Expected: The list shows only listings whose guest capacity is greater than or equal to the entered number of guests.

- [ ] FT-06: Traveler can filter properties by property type.
  - Action: Select one property type (e.g. "Apartment") from the Property Type filter and apply it.
  - Expected: The list shows only listings of the selected property type; other types are hidden.

- [ ] FT-07: Traveler can sort results by price and by rating.
  - Action: Select "Price" sort option, then select "Rating" sort option.
  - Expected: With price sorting, listings are ordered by nightly price (low-to-high or high-to-low per the selected option); with rating sorting, listings are ordered by average rating descending.

- [ ] FT-08: Each listing has a detail page with full description, basic reviews, and available dates.
  - Action: Click a default listing in the browse list to open its detail page.
  - Expected: The page shows the full description, at least one review with rating and comment, and an available-dates display (calendar or date list).

- [ ] FT-09: Traveler can submit a booking request for chosen dates.
  - Action: On a listing detail page, choose an available Start Date and End Date, fill in guest name and email, and click "Request Booking"/"Book".
  - Expected: The booking request is created and listed for that property.

- [ ] FT-10: Owner can view booking requests and update their status.
  - Action: Open the owner's booking requests view for a listing that has a pending request, and change its status (e.g. to "Approved").
  - Expected: The request appears in the requests list with its dates and guest info, and after the update shows the new status.

## Constraint
- [ ] CS-01: Listing form cannot be submitted with empty required fields.
  - Action: Open the "Create Listing" form, leave Location, Description, and Nightly Price empty, and click "Save"/"Create".
  - Expected: The listing is not created; an error/validation message indicates the required fields must be filled.

- [ ] CS-02: Nightly price must be a positive number.
  - Action: In the listing form, enter Nightly Price as "0", then as "-50", then as "abc", submitting each time.
  - Expected: Each submission is rejected with a price validation message; no listing with a non-positive or non-numeric price is created.

- [ ] CS-03: Photo entry must be a valid image URL.
  - Action: In the listing form, enter "not-a-url" in the Photo URL field and submit with all other fields valid.
  - Expected: The submission is rejected with a URL validation message; no listing is created with an invalid photo URL.

- [ ] CS-04: Booking end date must be after the start date.
  - Action: On the booking request form, set Start Date later than End Date and submit.
  - Expected: The request is rejected with a date-range error message; no booking request is created.

- [ ] CS-05: Booking request cannot be submitted for unavailable dates.
  - Action: On the booking form for a default listing, choose dates that are outside the listing's available dates (or already booked) and submit.
  - Expected: The request is rejected with a message indicating the dates are not available; no booking request is created.

## Interaction
- [ ] IX-01: Creating a listing gives clear success feedback.
  - Action: Submit a valid "Create Listing" form and observe the screen immediately after.
  - Expected: A success confirmation (message or toast) is displayed indicating the listing was created.

- [ ] IX-02: Submitting a booking request gives clear success feedback.
  - Action: Submit a valid booking request form and observe the screen immediately after.
  - Expected: A success confirmation (message or toast) is displayed indicating the request was submitted.

- [ ] IX-03: Filter and sort changes update the results list immediately.
  - Action: Change any filter (price, guests, type) or sort option on the browse page and observe the list.
  - Expected: The results list refreshes in place to reflect the new filter/sort without needing a manual page reload.

## Content
- [ ] CT-01: Listing detail page content matches the listing's entered data.
  - Action: Open a default listing's detail page and compare displayed location, description, amenities, nightly price, and photos against its data.
  - Expected: All displayed text and photo images correspond exactly to that listing's data; photos load and depict the property, not broken/placeholder images.

- [ ] CT-02: Browse list entries show relevant, consistent summary info.
  - Action: Inspect each entry in the property browse list.
  - Expected: Every entry shows the property name/title, location, nightly price, property type, and rating, and these values match the listing's detail page.