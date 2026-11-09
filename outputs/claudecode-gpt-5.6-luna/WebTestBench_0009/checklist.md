# Test Checklist

## Functionality
- [ ] **FT-01: Owner can create a short-term rental listing with all supported details.**
  - **Action:** As a property owner, open the listing creation form, enter a location, description, amenities, one or more image URLs, and a nightly price, then select **Save/Create Listing**.
  - **Expected:** The listing is saved successfully and appears in the owner’s listing management view.

- [ ] **FT-02: Owner can edit an existing property listing.**
  - **Action:** Open an existing listing, change its description, amenities, photo URL, or nightly price, and select **Save/Update**.
  - **Expected:** The updated values persist after leaving and reopening the listing.

- [ ] **FT-03: Traveler can browse available properties in a list.**
  - **Action:** Open the traveler property-browsing page.
  - **Expected:** All currently available default properties are displayed as individual list entries.

- [ ] **FT-04: Traveler can filter properties by price range, guest capacity, and property type.**
  - **Action:** Set a minimum and maximum nightly price, a number of guests, and a property type, then apply the filters.
  - **Expected:** Every displayed result satisfies all selected filter conditions.

- [ ] **FT-05: Traveler can sort property results by price and rating.**
  - **Action:** Select the price sort option and verify the order, then select the rating sort option.
  - **Expected:** Results reorder according to the selected price or rating sort criterion.

- [ ] **FT-06: Traveler can open an individual property detail page.**
  - **Action:** Select a property from the browse list.
  - **Expected:** A detail page opens for the selected property and identifies the same property.

- [ ] **FT-07: Traveler can submit a booking request for selected available dates.**
  - **Action:** On a property detail page, choose available check-in and check-out dates, complete the booking request form, and select **Submit Booking Request**.
  - **Expected:** The request is submitted successfully and is associated with the selected property and dates.

- [ ] **FT-08: Owner can view booking requests and update their status.**
  - **Action:** Open the owner booking-request management view, select an existing request, change its status using the available status control, and save the change.
  - **Expected:** The request appears in the owner’s request list with the newly selected status after refresh.

## Constraint
- [ ] **CS-01: Listing creation is blocked when required listing details are missing.**
  - **Action:** Leave Location, Description, Amenities, Photos, or Nightly Price empty and select **Save/Create Listing**.
  - **Expected:** The listing is not saved, and each missing required field is clearly identified.

- [ ] **CS-02: Listing photo entries accept only valid image URLs.**
  - **Action:** Enter an invalid or non-URL value in the Photos field and attempt to save the listing.
  - **Expected:** The listing is not saved, and the Photos field displays a validation error.

- [ ] **CS-03: Nightly price accepts only valid non-negative numeric values.**
  - **Action:** Enter letters, symbols, or a negative number in Nightly Price and attempt to save the listing.
  - **Expected:** The listing is not saved, and the price field indicates that a valid non-negative amount is required.

- [ ] **CS-04: Booking requests cannot use invalid or unavailable dates.**
  - **Action:** Attempt to submit a request with missing dates, a check-out date before check-in, dates in the past, or dates marked unavailable.
  - **Expected:** Submission is blocked and no booking request is created.

- [ ] **CS-05: Applied filters do not display properties outside the selected criteria.**
  - **Action:** Apply a narrow price, guest-capacity, or property-type filter and inspect every returned result.
  - **Expected:** No returned property violates any active filter.

## Interaction
- [ ] **IX-01: Property results update when filters are applied or cleared.**
  - **Action:** Apply one or more browse filters, then clear the filters.
  - **Expected:** The result list reflects the applied criteria, and clearing the filters restores the unfiltered available-property list.

- [ ] **IX-02: The interface provides success feedback for completed owner and traveler actions.**
  - **Action:** Successfully save a listing update, submit a booking request, and update a request status.
  - **Expected:** Each completed action produces visible confirmation feedback and leaves the user on the relevant updated view.

- [ ] **IX-03: Empty search results are communicated clearly.**
  - **Action:** Apply filter values that match no available property.
  - **Expected:** The results area displays a clear no-results message instead of appearing broken or showing unrelated properties.

## Content
- [ ] **CT-01: Property list entries display relevant identifying information.**
  - **Action:** Inspect the available-property list.
  - **Expected:** Each property entry shows its location, property type, guest capacity, nightly price, rating, and a relevant property image when those details exist.

- [ ] **CT-02: Property detail pages display complete and matching listing information.**
  - **Action:** Compare a property’s browse-list entry with its detail page.
  - **Expected:** The detail page shows the full description, amenities, photos, nightly price, location, and property details for the selected property without unrelated or placeholder content.

- [ ] **CT-03: Reviews and availability information are present and understandable on detail pages.**
  - **Action:** Inspect the reviews and availability sections for an existing property.
  - **Expected:** Basic reviews include readable review information, and available and unavailable dates are clearly distinguishable for booking selection.