# Test Checklist

## Functionality
- [ ] FT-01: User can register for a new marketplace account
  - Action: Open the registration page, fill in a valid username/email and password, and submit the form.
  - Expected: A new account is created and the user is logged in or shown a confirmation.

- [ ] FT-02: Seller can create a listing with photo, description, price, and location
  - Action: From the "Create Listing" page, upload a photo, enter a description, set a price, and set a location, then submit.
  - Expected: The listing is saved and appears in the marketplace with all entered details.

- [ ] FT-03: Buyer can search items by keyword
  - Action: Enter a keyword into the search bar and submit the search.
  - Expected: Results show only items matching the keyword in title or description.

- [ ] FT-04: Buyer can filter items by category
  - Action: Select a category from the filter options and apply it.
  - Expected: Results show only items belonging to the selected category.

- [ ] FT-05: Buyer can filter items by price range
  - Action: Set a minimum and maximum price and apply the filter.
  - Expected: Results show only items priced within the specified range.

- [ ] FT-06: Buyer can filter items by condition
  - Action: Select a condition (e.g., New, Used, Refurbished) and apply the filter.
  - Expected: Results show only items matching the selected condition.

- [ ] FT-07: Buyer can filter items by distance
  - Action: Set a distance radius from a location and apply the filter.
  - Expected: Results show only items within the specified distance of the location.

- [ ] FT-08: Buyer can sort items
  - Action: Choose a sort option (e.g., price low-to-high, newest) and apply it.
  - Expected: Results are reordered according to the selected sort criteria.

- [ ] FT-09: Buyer can add an item to the cart
  - Action: Open an item and click the "Add to Cart" button.
  - Expected: The item is added to the cart and is visible in the cart view.

- [ ] FT-10: Buyer can send a purchase request
  - Action: Open an item and click "Send Purchase Request" (or equivalent).
  - Expected: A purchase request is sent to the seller and confirmed to the buyer.

- [ ] FT-11: Seller can update their own listing
  - Action: Open one of the seller's own listings and edit the details, then save.
  - Expected: The listing is updated and reflects the new details.

- [ ] FT-12: Seller can remove their own listing
  - Action: Open one of the seller's own listings and choose "Remove" or "Delete".
  - Expected: The listing is removed and no longer appears in the marketplace.

## Constraint
- [ ] CS-01: Listing cannot be created with empty required fields
  - Action: Attempt to submit a listing with one or more required fields (photo, description, price, location) left blank.
  - Expected: Submission is blocked and a validation message indicates the missing fields.

- [ ] CS-02: Seller cannot modify another user's listing
  - Action: As one user, attempt to open another user's listing and access edit/remove controls.
  - Expected: Edit and remove options are not available for listings owned by other users.

- [ ] CS-03: Purchase request cannot be sent for an unavailable item
  - Action: Attempt to send a purchase request for an item that has been removed or marked unavailable.
  - Expected: The request is blocked with a message stating the item is no longer available.

## Interaction
- [ ] IX-01: Success confirmation appears after creating a listing
  - Action: Submit a valid new listing.
  - Expected: A success message or toast confirms the listing was created.

- [ ] IX-02: Cart updates visibly when an item is added
  - Action: Click "Add to Cart" on an item.
  - Expected: The cart indicator (count/badge) increments and reflects the added item.

- [ ] IX-03: Results refresh immediately when filters or sort are applied
  - Action: Apply or change a filter/sort option.
  - Expected: The item list updates dynamically without requiring a full page reload.

## Content
- [ ] CT-01: Each listing displays its photo, description, price, and location
  - Action: Open any listing from the marketplace.
  - Expected: The listing page shows the uploaded photo, description text, price, and location.

- [ ] CT-02: Displayed content aligns with the second-hand/upcycled theme
  - Action: Browse the homepage and listing samples.
  - Expected: All titles, images, categories, and descriptions relate to second-hand or upcycled products.