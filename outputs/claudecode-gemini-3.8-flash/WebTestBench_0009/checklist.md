# Test Checklist

## Functionality
- [ ] FT-01: Create property listing with complete details
  - Action: Fill out the listing creation form with location, description, amenities, photo URL, and nightly price, then click "Create Listing".
  - Expected: The new listing is created and appears in the property listings list.
- [ ] FT-02: Manage and update existing listing
  - Action: Select an existing listing from the owner dashboard, edit the description and nightly price, and click "Save Changes".
  - Expected: The listing updates with the new description and price.
- [ ] FT-03: Filter listings by price range, guests, and property type
  - Action: Set a minimum and maximum price, specify guest count, select a property type from the filter options, and apply filters.
  - Expected: The property list updates to display only listings matching the selected criteria.
- [ ] FT-04: Sort listings by price and rating
  - Action: Select "Price: Low to High" and then "Rating" from the sort dropdown.
  - Expected: The listings rearrange in ascending order by price, then in descending order by average rating.
- [ ] FT-05: Navigate to listing detail page
  - Action: Click on a property card from the browse list.
  - Expected: The listing detail page opens, displaying the property's full description, reviews section, and available dates.
- [ ] FT-06: Submit booking request for chosen dates
  - Action: On the listing detail page, select valid check-in and check-out dates, fill out the traveler request form, and click "Submit Request".
  - Expected: The booking request is submitted and recorded for the listing.
- [ ] FT-07: Owner views and updates booking request status
  - Action: In the owner booking management section, locate a pending booking request and change its status to "Accepted" or "Declined".
  - Expected: The booking request reflects the newly selected status.

## Constraint
- [ ] CS-01: Required field validation on listing creation
  - Action: Submit the listing creation form with empty location and nightly price fields.
  - Expected: Form submission is blocked and inline validation messages indicate the missing required fields.
- [ ] CS-02: Non-negative price validation
  - Action: Enter a negative number or zero in the nightly price field and attempt to submit the listing form.
  - Expected: Submission is rejected with an error message requiring a positive numeric price.
- [ ] CS-03: Restrict booking request on unavailable dates
  - Action: In the booking request form, attempt to select dates marked as unavailable/already booked.
  - Expected: Unavailable dates are disabled for selection or submission is blocked with an "unavailability" error.
- [ ] CS-04: Check-out date precedence constraint
  - Action: Select a check-out date that is identical to or earlier than the check-in date.
  - Expected: The booking form disables submission and displays an error stating check-out must be after check-in.

## Interaction
- [ ] IX-01: Booking request submission feedback
  - Action: Complete and submit a valid booking request form.
  - Expected: A confirmation message or modal appears confirming the booking request was sent successfully.
- [ ] IX-02: Real-time booking status update in owner view
  - Action: Change the status dropdown for a booking request from "Pending" to "Accepted".
  - Expected: The status label/badge immediately updates its visual state and text without requiring a full page refresh.
- [ ] IX-03: Reset applied filters
  - Action: Apply price, guest, and property type filters, then click the "Reset Filters" button.
  - Expected: All filter controls return to default states and the list displays the complete, unfiltered inventory.

## Content
- [ ] CT-01: Property browse card information display
  - Action: View property cards on the main browse page.
  - Expected: Each card displays the property title/location, nightly price, property type, and guest capacity.
- [ ] CT-02: Listing image URL rendering
  - Action: Open a listing detail page that contains photo URLs.
  - Expected: All provided image URLs render valid photos without broken image placeholders.
- [ ] CT-03: Reviews and rating display on detail page
  - Action: Scroll to the reviews section of a listing detail page.
  - Expected: Review author, star rating, and review comments are clearly presented.