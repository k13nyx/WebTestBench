I have completed all checklist items. Let me compile the final results.

# Test Result

## Functionality

- [X] FT-01: User can register a new account
  - Action: Open the registration page, fill username/email/password, click "Register".
  - Expected: Account is created and the user is logged in or redirected to the login/home page.

- [X] FT-02: Seller can create a listing with all required fields
  - Action: Log in, open "Create Listing", enter title, description, price, location, condition, category, upload a photo, and submit.
  - Expected: Listing is saved and appears in the seller's listings and search results.

- [X] FT-03: User can search for items by keyword
  - Action: Type a keyword matching a default listing (e.g., a product in the catalog) into the search bar and submit.
  - Expected: Matching listings are displayed in the results.

- [X] FT-04: User can filter items by category
  - Action: Select a category from the category filter.
  - Expected: Only listings in the selected category are shown.

- [ ] FT-05: User can filter items by price range
  - Action: Set a minimum and maximum price in the price filter.
  - Expected: Only listings whose price falls within the range are shown.
  - Bug Report:
    - Issue: Missing control (no maximum price input)
    - Actual: The "Price Range" filter exposes only ONE slider, labeled "Minimum" (accessibility: `aria-valuemin=0`, `aria-valuemax=500`, single thumb; header shows "$0 - $500" with the upper bound fixed). A maximum price cannot be set, so a price *range* cannot be specified. Verified that the slider acts as a minimum bound only: setting it to $60 returned exactly the 7 listings priced ≥ $60.

- [X] FT-06: User can filter items by condition
  - Action: Select a condition value (e.g., "Used", "Upcycled", "Like New") in the condition filter.
  - Expected: Only listings matching the selected condition are shown.

- [ ] FT-07: User can filter items by distance
  - Action: Provide a location and select a distance radius (e.g., 5 km).
  - Expected: Only listings within the selected distance from the location are shown.
  - Bug Report:
    - Issue: Missing element (no location input) + incorrect filtering
    - Actual: The filter panel provides only a "Max Distance" slider (range 1–50, label "Any" at 50). There is NO field to provide a location, so the prescribed action cannot be performed. Furthermore, the radius results are not based on real locations: with the account location "Seattle, WA", a 5-mile radius returned items located in Brooklyn, NY and Austin, TX, while other same-city items only appeared at 10 miles, and all 10 default items appeared within 20 miles — i.e., distances do not correspond to the listed locations.

- [X] FT-08: User can sort the displayed items
  - Action: Use the sort control to select an option (e.g., price low-to-high, newest).
  - Expected: Result list reorders to match the selected sort option.

- [X] FT-09: Buyer can add an item to the cart
  - Action: Open a listing and click "Add to Cart".
  - Expected: The item is added to the cart and appears in the cart view.

- [X] FT-10: Buyer can send a purchase request
  - Action: Open a listing and submit a purchase request (e.g., click "Request to Buy").
  - Expected: The purchase request is sent/recorded and the buyer sees a confirmation.

- [ ] FT-11: Seller can update an existing listing
  - Action: Open one of the seller's own listings, edit a field (e.g., price), and save.
  - Expected: The listing reflects the updated value across listing view and search.
  - Bug Report:
    - Issue: Missing feature (no edit/update affordance)
    - Actual: No Edit/Update control exists for a seller's own listings. "My Listings" shows only "View", "Mark Sold", and "Delete"; the owned-listing detail page shows only a "Manage Your Listings" button; no edit button, link, modal, or "edit"/"pencil" element is present (verified by inspecting all buttons/links and the rendered HTML). A listing field (e.g., price) therefore cannot be changed after creation.

- [X] FT-12: Seller can remove an existing listing
  - Action: Open one of the seller's own listings and click "Remove"/"Delete".
  - Expected: The listing is removed from the seller's listings and is no longer available to buyers.

## Constraint

- [X] CS-01: Registration rejects invalid or incomplete input
  - Action: Submit the registration form with an empty required field or an invalid email format.
  - Expected: Submission is blocked and a validation error is shown for the offending field.

- [X] CS-02: Listing cannot be published with missing required fields
  - Action: Attempt to submit a listing with any required field (title, description, price, location, condition, photo) left empty.
  - Expected: Submission is blocked and a validation error identifies the missing field(s).

- [ ] CS-03: Invalid price range is prevented
  - Action: Set a minimum price greater than the maximum price in the price filter.
  - Expected: The invalid range is rejected (blocked or corrected); no impossible result set is returned.
  - Bug Report:
    - Issue: Missing element (no maximum price input)
    - Actual: The price filter provides no maximum-price control (only a single "Minimum" slider). A minimum value greater than the maximum therefore cannot be entered, so the specified invalid-range scenario cannot be exercised — the required maximum-price input is absent.

- [X] CS-04: Removed listings do not appear in search or filters
  - Action: After a seller removes a listing, search for it by its exact title and apply its former category/condition filters.
  - Expected: The removed listing does not appear in any search or filtered result.

## Interaction

- [X] IX-01: Success feedback after creating or updating a listing
  - Action: Submit a new listing or save edits to an existing listing.
  - Expected: A success notification/toast is displayed confirming the action.

- [X] IX-02: Confirmation prompt before removing a listing
  - Action: Click "Remove"/"Delete" on an own listing.
  - Expected: A confirmation dialog appears and the listing is deleted only after confirming.

## Content

- [X] CT-01: Listing cards display all required information
  - Action: View any listing card in search results or the listing detail page.
  - Expected: Photo, title, price, condition, and location are all present and populated.

- [ ] CT-02: Listing images are relevant to the item
  - Action: Inspect the photos on default listings.
  - Expected: Each photo corresponds to the listed product (no placeholder, broken, or mismatched images).
  - Bug Report:
    - Issue: Broken image
    - Actual: The default listing "Handmade Macrame Wall Hanging" (product `prod-5`) has a broken photo — its `<img>` reports `naturalWidth = 0` (failed load) and its URL `https://images.unsplash.com/photo-1622464689583-a09e88f0d34e?w=600&h=600&fit=crop` returns an `onerror`/ERROR. The other 9 default listing images load successfully (naturalWidth 600).

---

### Summary of Failures
- **FT-05** — Price filter has only a "Minimum" slider; no maximum price can be set.
- **FT-07** — No location input for distance filtering, and radius results don't match the listed locations.
- **FT-11** — No edit/update UI for a seller's own listings (only View / Mark Sold / Delete).
- **CS-03** — No maximum-price control, so the invalid-range scenario cannot be created.
- **CT-02** — "Handmade Macrame Wall Hanging" (prod-5) default product image is broken.

Passed: FT-01, FT-02, FT-03, FT-04, FT-06, FT-08, FT-09, FT-10, FT-12, CS-01, CS-02, CS-04, IX-01, IX-02, CT-01 (15/20).