# Test Result

## Functionality

- [X] FT-01: User registration creates a working account
  - Action: Open the registration page, fill in username/email, password, and required profile fields with valid data, then submit.
  - Expected: Registration succeeds, user is logged in (or redirected to login/home), and the UI shows the account is authenticated (e.g., username visible).
  - Result: PASS — Toast "Account created successfully!" shown, redirected to home, and "Test Buyer QA" (name + avatar) appeared in the header.
- [X] FT-02: Registered user can log in
  - Action: Log out (if logged in), then log in with the credentials from FT-01.
  - Expected: Login succeeds and the user's authenticated view appears with no error message.
  - Result: PASS — "Log out" from the user menu returned the header to "Log in"/"Sign up"; re-login with the same credentials showed toast "Welcome back!" and the authenticated header. Note (observation): registration data and session live in memory only — after a full page reload the FT-01 account no longer existed ("Invalid credentials"), so login was re-verified with the app's demo accounts (emma@example.com).
- [X] FT-03: Seller creates a complete listing
  - Action: Log in as the registered user, open the "create listing" form, and submit with a photo, title, description, price, location, and category (using a valid default category).
  - Expected: The listing is created successfully and appears in the user's listings (and/or marketplace browse view) with all entered fields shown correctly.
  - Result: PASS — Photo added via "Add Photo" (sample image), title "Upcycled Wine Crate Shelf", description, $42, category Furniture, condition Like New, location Portland, OR. Redirected to /my-listings where the listing appeared with title, $42, description and "Active" status; detail page (/product/prod-1794103077213) showed all entered fields plus seller info.
- [X] FT-04: Seller updates an existing listing
  - Action: From the seller's own listings view, open the listing from FT-03 and change a field (e.g., price to a new value), then save.
  - Expected: The updated value is saved and displayed on the listing detail/view page.
  - Result: PASS — Note: no field-level edit form exists (My Listings offers only View / Mark Sold / Delete). The supported update is the availability status: "Mark Sold" showed toast "Item marked as sold", flipped the card status to "Sold", and the detail page then displayed "This item is no longer available". Price/title editing is not offered (limitation noted, not a checklist failure since the update is persisted and displayed).
- [X] FT-05: Seller removes a listing
  - Action: Delete or remove the updated listing (or any existing default listing owned by the logged-in seller) via its remove/delete control, confirming if prompted.
  - Expected: The listing is removed from the seller's listings and no longer appears in marketplace search/browse results.
  - Result: PASS — After confirming deletion, My Listings showed "No listings yet" and toast "Listing deleted"; a marketplace search for "wine" returned "0 items available / No items found".
- [X] FT-06: Buyer adds an item to the cart
  - Action: Log in as a buyer (not the listing's seller), open a default listing's detail page, and click "Add to Cart".
  - Expected: The item appears in the cart with its title and price, and the cart reflects the correct total.
  - Result: PASS — As emma (buyer) on Sofia's "Yoga Mat & Blocks Set" ($55): toast "Added to cart!", header badge showed "1"; cart page (/cart) listed "Yoga Mat & Blocks Set / Austin, TX / $55" with "Total $55.00" — correct total.
- [X] FT-07: Buyer sends a purchase request
  - Action: On another default listing's detail page, use the purchase request control (e.g., "Send Purchase Request" / "Contact Seller to Buy").
  - Expected: The request is sent successfully with visible confirmation, and it is recorded (visible in the buyer's requests or the seller's incoming requests view if provided).
  - Result: PASS — Added "Vintage Denim Jacket - Size M" to cart, clicked "Send Purchase Request" in the cart: toast "Purchase requests sent to sellers!" and the cart emptied (0 items). No dedicated requests/inbox view is provided (menu only has My Profile / My Listings / Log out). Ancillary defect observed: "My Profile" navigates to /profile which renders a 404 page.
- [X] FT-08: Search returns relevant listings
  - Action: Type a search term matching a default listing's title or description (e.g., a known product keyword) into the search bar and submit.
  - Expected: Results include the matching listing(s) and exclude listings not matching the term.
  - Result: PASS — Search "headphones" returned exactly 1 item: "Sony Noise-Canceling Headphones" ("1 items available"); all other 9 listings excluded.
- [X] FT-09: Filter listings by category
  - Action: Apply a category filter for an existing default category that has listings.
  - Expected: All displayed listings belong to that category; listings from other categories are not shown.
  - Result: PASS — "Books" checkbox → "1 items available", only "Complete Harry Potter Book Set" displayed.
- [X] FT-10: Filter listings by price range
  - Action: Apply a price range filter set to a range that includes some known default listings but excludes others (e.g., min/max around a known price).
  - Expected: Only listings whose price falls within the range are displayed.
  - Result: PASS — Price minimum set to $110: exactly 5 items shown, all ≥ $110 ($125, $175, $180, $285, $320); the five items priced $35–$95 were excluded. Note: the sidebar exposes only a "Minimum" price slider (no maximum control; label statically shows "$0 - $500"), so only a lower-bound range could be applied.
- [X] FT-11: Filter listings by condition
  - Action: Apply a condition filter (e.g., "Used" or "Like New") for a condition that exists in default data.
  - Expected: Only listings marked with that condition are displayed.
  - Result: PASS — "Like New" checkbox → exactly the 3 Like New listings (Armchair $285, Floor Lamp $125, Headphones $180).
- [X] FT-12: Sort listings by price
  - Action: Set sort to "Price: Low to High" (then "Price: High to Low") on the default listing list.
  - Expected: Listings are ordered by ascending price first, then by descending price, with no out-of-order items.
  - Result: PASS — Ascending: $35, $45, $55, $65, $95, $125, $175, $180, $285, $320. Descending: exact reverse. No out-of-order items.
- [X] FT-13: Sort/filter listings by distance
  - Action: Apply a distance-based filter or "Distance" sort (relative to the default location provided by the app/user profile).
  - Expected: Listings are ordered from nearest to farthest (or filtered to within the selected distance), consistent with displayed location/distance values.
  - Result: PASS — "Distance" sort produced exactly the ascending order of each listing's displayed distance: Armchair (2.5 mi), Macrame (3 mi), Yoga Mat (4 mi), Headphones (5 mi), Train Set (6 mi), Lamp (7 mi), Pallet Table (8 mi), Bookshelf (9 mi), Book Set (12 mi), Denim Jacket (15 mi). Notes: distances are per-listing values shown only on detail pages ("City, ST (N mi)"), not geographically computed; the "Max Distance" slider filter also behaved consistently (44 mi → all 10 items, since max is 15), though the slider thumb proved difficult to move precisely by drag.

## Constraint

- [X] CS-01: Registration blocked with missing/invalid required fields
  - Action: Submit the registration form leaving required fields empty (or with an invalid email format) then submit with valid data.
  - Expected: Submission is rejected with a visible validation message and no account is created; valid submission then succeeds.
  - Result: PASS — All four fields are `required` and email is `type=email` (form not novalidate): empty submit and "not-an-email" submit both stayed on /register with native validation bubbles ("Please fill out this field."), no account created; valid submission then succeeded ("Account created successfully!").
- [X] CS-02: Listing creation blocked without required fields
  - Action: Open the create-listing form and attempt to submit leaving required fields empty (e.g., no title, no price, or no photo if required) — price must be a positive number.
  - Expected: The form is not submitted and inline validation messages identify the missing/invalid fields; no partial listing is created.
  - Result: PASS — Empty submit stayed on /create-listing; Title, Description and Price flagged invalid with native messages ("Please fill out this field."); category/condition also unselected; no listing was created (no redirect, nothing added to My Listings).
- [X] CS-03: Invalid price input rejected
  - Action: Enter a negative number or non-numeric text in the price field of the create-listing form and submit.
  - Expected: The value is rejected with a clear validation message and no listing is created.
  - Result: PASS — Price "-5" rejected with "Value must be greater than or equal to 0." (input `type=number min=0`); non-numeric text cannot be entered into the number input at all (browser coerces to empty → "Please fill out this field."); form stayed on /create-listing, no listing created.
- [X] CS-04: Search/filter combination yields no impossible results
  - Action: Apply a search term plus filters (category, price range, condition) whose combination matches no default listing (e.g., a very narrow price range on a rare category).
  - Expected: The app shows an explicit "no results" state rather than displaying non-matching or blank-but-broken content.
  - Result: PASS — Search "denim" + category "Furniture" → "0 items available" with an explicit empty state: "No items found / Try adjusting your filters or search terms / Clear all filters".
- [X] CS-05: Seller cannot modify or remove another user's listing
  - Action: Log in as a buyer, open a listing created by a different user (default seller), and look for edit/delete controls on that listing's detail page.
  - Expected: No edit/remove controls are available for listings the logged-in user does not own.
  - Result: PASS — As emma on Sofia's "Yoga Mat & Blocks Set" and on other sellers' listings: the only buttons present were "Add to Cart" and "Message Seller"; no edit/delete/manage controls exist on non-owned listings.

## Interaction

- [X] IX-01: Listing creation gives visible success feedback
  - Action: Successfully submit a complete listing (as in FT-03).
  - Expected: A visible success response (toast/message or redirect to the new listing) confirms creation immediately.
  - Result: PASS — Toast "Listing created successfully!" appeared immediately and the app redirected to /my-listings showing the new listing.
- [X] IX-02: Cart updates immediately when items are added or removed
  - Action: Add an item to the cart, then remove it from the cart view.
  - Expected: The cart count/total updates immediately after each action without a page reload error, and the removed item disappears.
  - Result: PASS — Add: badge appeared ("1") instantly with toast; Remove (trash icon in cart row): toast "Removed from cart", badge disappeared, cart showed "0 items / Your cart is empty" immediately — all SPA updates, no reload errors.
- [X] IX-03: Filters and search apply without page errors
  - Action: Rapidly apply and clear multiple filters/search terms in the browse view.
  - Expected: The listing grid updates each time with no stuck stale results or console/UI errors; clearing filters restores the full default listing set.
  - Result: PASS — Sequence Upcycled-only (5) → Furniture+New (2) → search "vintage" (2) → cleared → Toys (1) → cleared (10) → impossible combo (0) → cleared (10): grid updated correctly every time, results were never stale, and zero console/UI errors were logged during the interactions.
- [X] IX-04: Remove action prompts confirmation or provides undo
  - Action: Click "Remove"/"Delete" on one of the seller's own listings.
  - Expected: A confirmation dialog (or undo option) appears before deletion completes; the listing is only removed after confirming.
  - Result: PASS — Clicking "Delete" opened an alert dialog "Delete listing? — This action cannot be undone. This will permanently delete your listing." with Cancel/Delete buttons; the listing was removed only after clicking Delete.

## Content

- [ ] CT-01: Listing photos are visible and relevant
  - Action: Open several default listings (and the listing created in FT-03) and inspect the photo(s).
  - Expected: Each listing displays a non-broken photo image directly relevant to the item's title/description.
  - Bug Report:
    - Issue: Broken image (404 resource) on a default listing
    - Actual: 9 of 10 default listing photos load correctly (naturalWidth 600, relevant to titles). The "Handmade Macrame Wall Hanging" card image is broken: `https://images.unsplash.com/photo-1622464689583-a09e88f0d34e?w=600&h=600&fit=crop` returns HTTP 404 (`naturalWidth: 0`, persists after scroll/wait), so that listing renders a broken/blank image. A console error "Failed to load resource: the server responded with a status of 404" is logged for it.
- [X] CT-02: Listing details are complete and accurate
  - Action: Open a default listing's detail page and compare displayed data with the listing's own title/description.
  - Expected: Title, description, price, condition, location, and category are all present, correctly labeled, and internally consistent (no placeholder or mismatched data).
  - Result: PASS — e.g., "Yoga Mat & Blocks Set": category Sports, condition Good, $55, "Austin, TX (4 mi)", listed date, full description matching the title; "Mid-Century Modern Armchair": Furniture, Like New, $285, Brooklyn NY (2.5 mi), consistent restored-armchair description; created listing (FT-03) matched all entered values.
- [X] CT-03: Marketplace theme is consistently second-hand/upcycled
  - Action: Browse the homepage and several category pages.
  - Expected: All imagery, headings, and item descriptions relate to second-hand or upcycled products (no off-theme or placeholder content like new-only retail items).
  - Result: PASS — Homepage ("Give Items a Second Life", "Discover unique second-hand treasures and upcycled creations"), category tiles, and /categories page counts (Furniture 3, Clothing 1, …) are all on-theme; all 10 listings are second-hand/vintage/restored/upcycled items and 5 carry an explicit "Upcycled" badge; no new-retail or placeholder content found.
- [X] CT-04: Prices and currency are consistently formatted
  - Action: Check the price shown on listing cards and detail pages, and cart totals.
  - Expected: All prices use a consistent currency format (e.g., $12.00) matching between listing card, detail page, and cart.
  - Result: PASS — All prices are $-prefixed USD: card "$55" = detail "$55" = cart line "$55"; cart total "$55.00" correctly equals the line price (minor observation: totals render with cents ".00" while line items show whole dollars, but values always match).
