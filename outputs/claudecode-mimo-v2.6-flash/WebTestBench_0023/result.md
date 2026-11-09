# Test Result

## Functionality
- [X] FT-01: User can register a new account
  - Action: Navigate to registration, enter a valid email, username, and password, submit.
  - Expected: Account is created and the user is logged in (header shows username/profile).
- [X] FT-02: Seller can create a listing with photo, description, price, and location
  - Action: Open "Create listing", fill title, description, price, location, category, condition, upload a photo, submit.
  - Expected: Listing is created and appears in the site's item listings with all entered details and the photo.
- [X] FT-03: User can search for items by keyword
  - Action: Type a keyword matching an existing default item title into the search box and submit.
  - Expected: Results show only items matching the keyword.
- [ ] FT-04: User can filter items by category, price range, condition, and distance
  - Action: Apply each filter (category, min/max price, condition, distance) individually using default data.
  - Expected: Each filter narrows results to only items matching the selected criteria.
  - Bug Report:
    - Issue: Missing Filter Control (no maximum-price control)
    - Actual: Category (Furniture → 4 items), condition (Fair → 1 item), distance (4 mi → 4 items) and price minimum ($200 → 2 items ≥ $200) all narrow results correctly, but the "Price Range" section renders only a single thumb labelled "Minimum" (state is `[min, max]`, label always reads "$X - $500"); there is no maximum-price control anywhere in the filter sidebar, so the max-price filter cannot be applied at all.
- [X] FT-05: User can sort search results
  - Action: Select a sort option (e.g., price low→high, price high→low, distance) on the results page.
  - Expected: Results reorder according to the selected sort option.
- [X] FT-06: Buyer can add an item to the cart and view it
  - Action: Click "Add to cart" on a default item, then open the cart.
  - Expected: The item appears in the cart with its title, price, and quantity.
- [X] FT-07: Buyer can send a purchase request for an item
  - Action: Open an item and click "Send purchase request" (or equivalent), then submit.
  - Expected: A purchase request is sent and confirmed (confirmation message or request appears in the buyer's requests).
- [ ] FT-08: Seller can update an existing listing
  - Action: Open own listing, change the price and description, save.
  - Expected: Updated price and description are shown on the listing detail page.
  - Bug Report:
    - Issue: Missing Edit/Update Functionality (Unreachable Feature)
    - Actual: No edit control exists anywhere: "My Listings" offers only View / Mark Sold / Delete, and the owner's detail page offers only "Manage Your Listings"; a full-DOM search for "edit" returns nothing and MyListings.tsx/ProductDetail.tsx/CreateListing.tsx contain no edit route or form, so the price/description cannot be changed.
- [X] FT-09: Seller can remove a listing
  - Action: Open own listing and click "Remove/Delete listing".
  - Expected: The listing disappears from search results and detail page is no longer accessible.

## Constraint
- [ ] CS-01: Registration rejects invalid or duplicate inputs
  - Action: Submit registration with empty required fields, then with an already-used email/username.
  - Expected: Submission is blocked with a clear error message in both cases; no account is created.
  - Bug Report:
    - Issue: No Duplicate-Input Validation (duplicate account created)
    - Actual: Empty fields were correctly blocked ("Please fill out this field." on each required input, still on /register), but re-submitting with the already-used email `alex.rivera@example.com` succeeded: toast "Account created successfully!" was shown, a second account was created and the header switched to the new user "Alex Duplicate" — no error and a duplicate account was created.
- [X] CS-02: Listing form rejects missing required fields or invalid price
  - Action: Submit create-listing form with empty title/description/price/location, then with a negative or non-numeric price.
  - Expected: Submission is blocked with an error identifying the invalid field; no listing is created.
- [X] CS-03: Filters cannot produce contradictory results
  - Action: Set a price range where min > max (e.g., min 100, max 10).
  - Expected: The application prevents or flags the invalid range and does not show mismatched items.
- [X] CS-04: Only the listing owner can edit or delete their listing
  - Action: Log in as a different user and attempt to access edit/delete on another user's listing.
  - Expected: Edit/delete options are hidden or the action is denied with an error; listing remains unchanged.
- [X] CS-05: Cannot add an unavailable/removed item to cart
  - Action: Attempt to add a removed (or sold/unavailable) item to the cart.
  - Expected: The action is blocked and the item is not added to the cart.

## Interaction
- [X] IX-01: Adding an item to the cart gives immediate feedback
  - Action: Click "Add to cart" on an item.
  - Expected: A success toast/confirmation appears and the cart indicator increments without reloading the page.
- [X] IX-02: Search and filter changes update results immediately
  - Action: Change a filter or sort option on the results page.
  - Expected: The results list refreshes promptly to reflect the new criteria, with active filters visibly indicated.
- [X] IX-03: Listing removal is confirmed and reflected immediately
  - Action: Click "Remove listing" and confirm in the dialog.
  - Expected: A confirmation message appears and the listing is removed from the visible list right away.

## Content
- [X] CT-01: Listing detail page shows complete, accurate listing content
  - Action: Open any default listing's detail page.
  - Expected: Photo renders correctly alongside title, description, price, location, category, and condition, all consistent with the list view.
- [X] CT-02: Displayed items are all second-hand or upcycled products
  - Action: Browse the full default catalog.
  - Expected: Every item shown is relevant to the second-hand/upcycled marketplace theme (no unrelated or placeholder items).

---

**Summary: 17 PASS / 3 FAIL** (FT-04, FT-08, CS-01)

Key evidence notes:
- **FT-04**: category/condition/distance/price-min filters all verified working (each narrowed the 11-item list correctly, results updated live, active filters shown via checked boxes + "Clear all filters"); the maximum-price thumb is simply never rendered.
- **FT-08**: the app's `updateProduct` API exists but is only wired to "Mark Sold/Available" — there is no price/description edit UI.
- **CS-01**: empty-field validation works; duplicate email does not.
- **CS-05/FT-09**: a sold item's detail shows "This item is no longer available" with no Add-to-Cart button; after deletion, search returns 0 results and the detail route shows "Product not found".