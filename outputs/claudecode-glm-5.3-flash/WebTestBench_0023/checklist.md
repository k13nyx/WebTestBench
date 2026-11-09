# Test Checklist

## Functionality
- [ ] FT-01: User registration creates a working account
  - Action: Open the registration page, fill in username/email, password, and required profile fields with valid data, then submit.
  - Expected: Registration succeeds, user is logged in (or redirected to login/home), and the UI shows the account is authenticated (e.g., username visible).
- [ ] FT-02: Registered user can log in
  - Action: Log out (if logged in), then log in with the credentials from FT-01.
  - Expected: Login succeeds and the user's authenticated view appears with no error message.
- [ ] FT-03: Seller creates a complete listing
  - Action: Log in as the registered user, open the "create listing" form, and submit with a photo, title, description, price, location, and category (using a valid default category).
  - Expected: The listing is created successfully and appears in the user's listings (and/or marketplace browse view) with all entered fields shown correctly.
- [ ] FT-04: Seller updates an existing listing
  - Action: From the seller's own listings view, open the listing from FT-03 and change a field (e.g., price to a new value), then save.
  - Expected: The updated value is saved and displayed on the listing detail/view page.
- [ ] FT-05: Seller removes a listing
  - Action: Delete or remove the updated listing (or any existing default listing owned by the logged-in seller) via its remove/delete control, confirming if prompted.
  - Expected: The listing is removed from the seller's listings and no longer appears in marketplace search/browse results.
- [ ] FT-06: Buyer adds an item to the cart
  - Action: Log in as a buyer (not the listing's seller), open a default listing's detail page, and click "Add to Cart".
  - Expected: The item appears in the cart with its title and price, and the cart reflects the correct total.
- [ ] FT-07: Buyer sends a purchase request
  - Action: On another default listing's detail page, use the purchase request control (e.g., "Send Purchase Request" / "Contact Seller to Buy").
  - Expected: The request is sent successfully with visible confirmation, and it is recorded (visible in the buyer's requests or the seller's incoming requests view if provided).
- [ ] FT-08: Search returns relevant listings
  - Action: Type a search term matching a default listing's title or description (e.g., a known product keyword) into the search bar and submit.
  - Expected: Results include the matching listing(s) and exclude listings not matching the term.
- [ ] FT-09: Filter listings by category
  - Action: Apply a category filter for an existing default category that has listings.
  - Expected: All displayed listings belong to that category; listings from other categories are not shown.
- [ ] FT-10: Filter listings by price range
  - Action: Apply a price range filter set to a range that includes some known default listings but excludes others (e.g., min/max around a known price).
  - Expected: Only listings whose price falls within the range are displayed.
- [ ] FT-11: Filter listings by condition
  - Action: Apply a condition filter (e.g., "Used" or "Like New") for a condition that exists in default data.
  - Expected: Only listings marked with that condition are displayed.
- [ ] FT-12: Sort listings by price
  - Action: Set sort to "Price: Low to High" (then "Price: High to Low") on the default listing list.
  - Expected: Listings are ordered by ascending price first, then by descending price, with no out-of-order items.
- [ ] FT-13: Sort/filter listings by distance
  - Action: Apply a distance-based filter or "Distance" sort (relative to the default location provided by the app/user profile).
  - Expected: Listings are ordered from nearest to farthest (or filtered to within the selected distance), consistent with displayed location/distance values.

## Constraint
- [ ] CS-01: Registration blocked with missing/invalid required fields
  - Action: Submit the registration form leaving required fields empty (or with an invalid email format) then submit with valid data.
  - Expected: Submission is rejected with a visible validation message and no account is created; valid submission then succeeds.
- [ ] CS-02: Listing creation blocked without required fields
  - Action: Open the create-listing form and attempt to submit leaving required fields empty (e.g., no title, no price, or no photo if required) — price must be a positive number.
  - Expected: The form is not submitted and inline validation messages identify the missing/invalid fields; no partial listing is created.
- [ ] CS-03: Invalid price input rejected
  - Action: Enter a negative number or non-numeric text in the price field of the create-listing form and submit.
  - Expected: The value is rejected with a clear validation message and no listing is created.
- [ ] CS-04: Search/filter combination yields no impossible results
  - Action: Apply a search term plus filters (category, price range, condition) whose combination matches no default listing (e.g., a very narrow price range on a rare category).
  - Expected: The app shows an explicit "no results" state rather than displaying non-matching or blank-but-broken content.
- [ ] CS-05: Seller cannot modify or remove another user's listing
  - Action: Log in as a buyer, open a listing created by a different user (default seller), and look for edit/delete controls on that listing's detail page.
  - Expected: No edit/remove controls are available for listings the logged-in user does not own.

## Interaction
- [ ] IX-01: Listing creation gives visible success feedback
  - Action: Successfully submit a complete listing (as in FT-03).
  - Expected: A visible success response (toast/message or redirect to the new listing) confirms creation immediately.
- [ ] IX-02: Cart updates immediately when items are added or removed
  - Action: Add an item to the cart, then remove it from the cart view.
  - Expected: The cart count/total updates immediately after each action without a page reload error, and the removed item disappears.
- [ ] IX-03: Filters and search apply without page errors
  - Action: Rapidly apply and clear multiple filters/search terms in the browse view.
  - Expected: The listing grid updates each time with no stuck stale results or console/UI errors; clearing filters restores the full default listing set.
- [ ] IX-04: Remove action prompts confirmation or provides undo
  - Action: Click "Remove"/"Delete" on one of the seller's own listings.
  - Expected: A confirmation dialog (or undo option) appears before deletion completes; the listing is only removed after confirming.

## Content
- [ ] CT-01: Listing photos are visible and relevant
  - Action: Open several default listings (and the listing created in FT-03) and inspect the photo(s).
  - Expected: Each listing displays a non-broken photo image directly relevant to the item's title/description.
- [ ] CT-02: Listing details are complete and accurate
  - Action: Open a default listing's detail page and compare displayed data with the listing's own title/description.
  - Expected: Title, description, price, condition, location, and category are all present, correctly labeled, and internally consistent (no placeholder or mismatched data).
- [ ] CT-03: Marketplace theme is consistently second-hand/upcycled
  - Action: Browse the homepage and several category pages.
  - Expected: All imagery, headings, and item descriptions relate to second-hand or upcycled products (no off-theme or placeholder content like new-only retail items).
- [ ] CT-04: Prices and currency are consistently formatted
  - Action: Check the price shown on listing cards and detail pages, and cart totals.
  - Expected: All prices use a consistent currency format (e.g., $12.00) matching between listing card, detail page, and cart.