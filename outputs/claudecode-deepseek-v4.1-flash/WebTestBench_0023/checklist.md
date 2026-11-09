# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account
  - Action: Open the registration page, fill username/email/password, click "Register".
  - Expected: Account is created and the user is logged in or redirected to the login/home page.

- [ ] FT-02: Seller can create a listing with all required fields
  - Action: Log in, open "Create Listing", enter title, description, price, location, condition, category, upload a photo, and submit.
  - Expected: Listing is saved and appears in the seller's listings and search results.

- [ ] FT-03: User can search for items by keyword
  - Action: Type a keyword matching a default listing (e.g., a product in the catalog) into the search bar and submit.
  - Expected: Matching listings are displayed in the results.

- [ ] FT-04: User can filter items by category
  - Action: Select a category from the category filter.
  - Expected: Only listings in the selected category are shown.

- [ ] FT-05: User can filter items by price range
  - Action: Set a minimum and maximum price in the price filter.
  - Expected: Only listings whose price falls within the range are shown.

- [ ] FT-06: User can filter items by condition
  - Action: Select a condition value (e.g., "Used", "Upcycled", "Like New") in the condition filter.
  - Expected: Only listings matching the selected condition are shown.

- [ ] FT-07: User can filter items by distance
  - Action: Provide a location and select a distance radius (e.g., 5 km).
  - Expected: Only listings within the selected distance from the location are shown.

- [ ] FT-08: User can sort the displayed items
  - Action: Use the sort control to select an option (e.g., price low-to-high, newest).
  - Expected: Result list reorders to match the selected sort option.

- [ ] FT-09: Buyer can add an item to the cart
  - Action: Open a listing and click "Add to Cart".
  - Expected: The item is added to the cart and appears in the cart view.

- [ ] FT-10: Buyer can send a purchase request
  - Action: Open a listing and submit a purchase request (e.g., click "Request to Buy").
  - Expected: The purchase request is sent/recorded and the buyer sees a confirmation.

- [ ] FT-11: Seller can update an existing listing
  - Action: Open one of the seller's own listings, edit a field (e.g., price), and save.
  - Expected: The listing reflects the updated value across listing view and search.

- [ ] FT-12: Seller can remove an existing listing
  - Action: Open one of the seller's own listings and click "Remove"/"Delete".
  - Expected: The listing is removed from the seller's listings and is no longer available to buyers.

## Constraint
- [ ] CS-01: Registration rejects invalid or incomplete input
  - Action: Submit the registration form with an empty required field or an invalid email format.
  - Expected: Submission is blocked and a validation error is shown for the offending field.

- [ ] CS-02: Listing cannot be published with missing required fields
  - Action: Attempt to submit a listing with any required field (title, description, price, location, condition, photo) left empty.
  - Expected: Submission is blocked and a validation error identifies the missing field(s).

- [ ] CS-03: Invalid price range is prevented
  - Action: Set a minimum price greater than the maximum price in the price filter.
  - Expected: The invalid range is rejected (blocked or corrected); no impossible result set is returned.

- [ ] CS-04: Removed listings do not appear in search or filters
  - Action: After a seller removes a listing, search for it by its exact title and apply its former category/condition filters.
  - Expected: The removed listing does not appear in any search or filtered result.

## Interaction
- [ ] IX-01: Success feedback after creating or updating a listing
  - Action: Submit a new listing or save edits to an existing listing.
  - Expected: A success notification/toast is displayed confirming the action.

- [ ] IX-02: Confirmation prompt before removing a listing
  - Action: Click "Remove"/"Delete" on an own listing.
  - Expected: A confirmation dialog appears and the listing is deleted only after confirming.

## Content
- [ ] CT-01: Listing cards display all required information
  - Action: View any listing card in search results or the listing detail page.
  - Expected: Photo, title, price, condition, and location are all present and populated.

- [ ] CT-02: Listing images are relevant to the item
  - Action: Inspect the photos on default listings.
  - Expected: Each photo corresponds to the listed product (no placeholder, broken, or mismatched images).