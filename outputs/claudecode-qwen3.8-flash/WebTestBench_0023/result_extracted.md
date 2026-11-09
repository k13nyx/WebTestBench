# Test Result

## Functionality

- [X] FT-01: New user can register and log in
  - Action: Click "Register"/"Sign Up", submit a valid name, email, and password; then log out and log back in with the same credentials.
  - Expected: Account is created and user is signed in (account name shown in header); subsequent login succeeds.
  - Note: Registered "QA Tester" (qa.tester@example.com) → toast "Account created successfully!", name shown in header; logged out via account menu → "Log in"/"Sign up" returned; logged back in → "Welcome back!" + name in header. (Side observation: the app persists no session data in localStorage — a full page reload logs the user out, though this is outside the item's stated steps.)

- [X] FT-02: Logged-in user can create a complete listing
  - Action: As a signed-in seller, open "Create Listing"/"Sell", upload a photo, enter title, description, category, price, condition, and location, then submit.
  - Expected: Listing is saved; its detail page shows the photo, description, price, condition, and location; the item appears in browse/search results.
  - Note: "Upcycled Sailcloth Tote Bag" ($42, Other, Good, Portland OR + photo) saved; detail page /product/prod-1794112522428 showed photo (naturalWidth 600), full description, "$42", "Good", "Portland, OR"; card appeared first in Browse (11 items) and via search.

- [X] FT-03: Keyword search returns matching items
  - Action: Enter a keyword present in a default listing's title/description (e.g., "denim jacket") and submit the search.
  - Expected: Matching listings are shown; unrelated listings are excluded.
  - Note: "denim jacket" → exactly 1 card ("Vintage Denim Jacket - Size M", "1 items available"); clearing restored all 11.

- [ ] FT-04: Filters narrow results to matching items
  - Action: Apply category (e.g., "Clothing"), price range (e.g., 0–50), condition (e.g., "Good"), and distance (e.g., within 10 km) filters on the results page.
  - Expected: Every displayed result satisfies all active filters simultaneously.
  - Bug Report:
    - Issue: Incomplete filter control — the "Price Range" filter has no maximum. The slider exposes only one handle (role=slider aria-label "Minimum", range 0–500); the "$0 – $500" caption is static. A 0–50 price cap cannot be applied.
    - Actual: Category (Home Decor), Condition (New) and Max Distance (e.g. "11 miles" → 0 items at "1 miles") filters work and the remaining result "Handmade Macrame Wall Hanging $45 Brooklyn NY New" (3 mi, Home Decor, New) satisfied all applied filters, but the price-range portion of the test is not executable as specified because no upper-bound price control exists.

- [X] FT-05: Results can be sorted by price
  - Action: With multiple results shown, select "Price: Low to High", then "Price: High to Low".
  - Expected: Item cards are ordered by ascending price, then descending price.
  - Note: Ascending $35→$42→$45→$55→$65→$95→$125→$175→$180→$285→$320; descending $320→$285→$180→$175→$125→$95… exact.

- [X] FT-06: Results can be sorted by distance
  - Action: Select the "Distance: Nearest first" sort option.
  - Expected: Listings are ordered by increasing distance from the reference location.
  - Note: Option is labeled "Distance" (nearest-first); sampled detail pages confirm ascending order: Armchair 2.5 mi (pos 2) < Macrame 3 mi (pos 3) < Headphones 5 mi (pos 5) < Floor Lamp 7 mi (pos 7) < Harry Potter 12 mi (pos 10) < Denim Jacket 15 mi (pos 11).

- [X] FT-07: Buyer can add an item to the cart
  - Action: As a signed-in buyer, open a default listing and click "Add to Cart", then open the cart page.
  - Expected: The item appears in the cart with the correct title and price.
  - Note: "Add to Cart" on prod-2 → toast "Added to cart!"; /cart shows "Vintage Denim Jacket - Size M … $65", "1 item", "Total $65.00".

- [X] FT-08: Buyer can send a purchase request
  - Action: On a default listing, click "Send Purchase Request"/"Make Offer", provide any requested message, and submit.
  - Expected: Request is submitted successfully with a visible confirmation (e.g., "Request sent").
  - Note: On prod-2 the purchase-request entry point is "Message Seller"; dialog "Send a message to Marcus Chen" + textarea → "Send Message" → dialog closes and toast "Message sent to seller!" is shown. (The cart page also exposes a "Send Purchase Request" button.)

- [ ] FT-09: Seller can update their own listing
  - Action: As the listing owner, click "Edit", change price and description, and save.
  - Expected: Detail page and search results display the updated values.
  - Bug Report:
    - Issue: Missing feature — no listing-edit capability exists anywhere in the UI.
    - Actual: As the owner (Emma Green), the listing detail page shows only a "Manage Your Listings" button, and My Listings cards offer only "View", "Mark Sold", and "Delete" buttons. There is no "Edit" control; price and description cannot be changed. The app's own summary "Manage your items for sale" provides no update flow.

- [X] FT-10: Seller can remove their own listing
  - Action: As the owner, click "Delete"/"Remove Listing" and confirm.
  - Expected: Listing no longer appears in search results; its detail URL shows an "unavailable"/not-found state.
  - Note: After confirming the delete dialog on "Upcycled Sailcloth Tote Bag": card vanished from My Listings, search "Sailcloth" → "No items found", and /product/prod-1794112522428 renders "Product not found" + "Back to Browse".

## Constraint

- [ ] CS-01: Listing creation requires all mandatory fields
  - Action: Open "Create Listing" and submit with title, price, and photo left empty.
  - Expected: Submission is blocked with inline errors on each missing field; no listing is created.
  - Bug Report:
    - Issue: Missing inline validation errors (silent blocking).
    - Actual: Submitting the empty form does block creation (URL stays /create-listing, nothing saved), but no error messages are rendered on any field — a DOM query for role=alert/error text found none; the app only moves focus to the Title input. Missing-price and missing-photo states likewise show no inline error.

- [ ] CS-02: Price must be a positive number
  - Action: Enter "-5", then "abc", in the price field of the create/edit listing form and submit.
  - Expected: A validation error (e.g., "Price must be a positive number") is shown and the listing cannot be saved.
  - Bug Report:
    - Issue: No visible validation error, and non-positive price accepted.
    - Actual: With "-5", submission is blocked silently (no error text/toast; only field focus — the browser's native constraint "Value must be greater than or equal to 0." fires invisibly); "abc" cannot even be entered (number input silently drops letters, value became empty); and a price of 0 was accepted — a listing "Upcycled Saddle Leather Messenger Bag" was successfully created and saved with "$0", contradicting "price must be a positive number".

- [ ] CS-03: Listing management is restricted to the owner; listing actions require login
  - Action: Open a default listing owned by another user while signed in as a different user, then as a logged-out visitor; also try opening "Create Listing" while logged out.
  - Expected: "Edit"/"Delete" controls are absent/inaccessible to non-owners and visitors; anonymous create-listing attempts redirect to login.
  - Bug Report:
    - Issue: Anonymous protected routes do not redirect to login; they render a blank page.
    - Actual: Owner-only restriction itself holds — Marcus Chen's listing (prod-2) showed no Edit/Delete when viewed as Emma ("Add to Cart"/"Message Seller" only) nor as a logged-out visitor (same buttons only). However, visiting /create-listing while logged out stays at URL /create-listing with a completely empty page (document.body.innerText length 0 — no header, no form, no redirect); /my-listings behaves the same. Expected redirect to /login does not occur.

## Interaction

- [ ] IX-01: Success feedback after publishing a listing
  - Action: Create a valid listing via the FT-02 flow.
  - Expected: A success message/toast (e.g., "Listing published") appears and the user is redirected to the new listing.
  - Bug Report:
    - Issue: Incorrect post-submit redirect.
    - Actual: The success toast "Listing created successfully!" does appear, but the user is redirected to /my-listings (the listings-management page), not to the new listing's detail page.

- [X] IX-02: Cart badge updates immediately when an item is added
  - Action: Note the cart icon's item count in the header, then click "Add to Cart" on a listing.
  - Expected: Header cart count increments by 1 without a manual page reload.
  - Note: Header cart button initially rendered no count; after clicking "Add to Cart" (no reload), the same button rendered "1" and /cart confirms "1 item".

- [X] IX-03: Listing removal requires explicit confirmation
  - Action: Click "Delete" on your own listing and choose "Cancel"; repeat and choose "Confirm".
  - Expected: Cancel leaves the listing intact and live; Confirm removes it.
  - Note: "Delete" opens role=alertdialog "Delete listing? This action cannot be undone…". Cancel → listing remained in My Listings and still purchasable; second attempt + "Delete" → removed.

- [X] IX-04: No-results state is handled gracefully
  - Action: Search a nonsense term (e.g., "zzzx99") and apply a filter combination that excludes all default items (e.g., 0–1 price range).
  - Expected: A "No items found" message is displayed instead of a blank or broken results area.
  - Note: Search "zzzx99" → "0 items available" + explicit "No items found" message (results area intact); likewise Max Distance "1 miles" yielded 0 cards with the same graceful state. (The literal "0–1 price" combination is not constructible — see FT-04.)

## Content

- [ ] CT-01: Listing information is complete and consistent across views
  - Action: Compare a default listing's card in search results with its detail page.
  - Expected: Photo, title, price, condition, category, and location are present and identical in both; no placeholder text or lorem ipsum.
  - Bug Report:
    - Issue: Category missing from the results card.
    - Actual: For "Vintage Denim Jacket - Size M", the card shows title, "$65", "San Francisco, CA", "Good" and the photo (matching the detail page exactly, no placeholder/lorem text), but the card does not display the category ("Clothing") that the detail page shows. The six required fields are not all present in both views.

- [ ] CT-02: Listing photos load and depict the listed item
  - Action: Browse search results and open 3–4 default listings.
  - Expected: All images render (no broken-image icons) and each photo plausibly shows the second-hand/upcycled item being sold.
  - Bug Report:
    - Issue: Broken listing photo (HTTP 404).
    - Actual: The "Handmade Macrame Wall Hanging" image fails to load both on its browse card and on its detail page: src https://images.unsplash.com/photo-1622464689583-a09e88f0d34e?w=600&h=600&fit=crop returns status 404 (naturalWidth = 0, console "Failed to load resource"). The other 4 sampled listings (denim jacket, armchair, Harry Potter set, train set) render with photos whose alt text matches the item (content plausibility assessed via DOM metadata only, per DOM-only policy).

- [X] CT-03: Site content matches the second-hand/upcycled marketplace theme
  - Action: Open the homepage and inspect the category/condition filter options.
  - Expected: Headings and copy reference second-hand and upcycled goods; filter options are relevant to used items (e.g., condition grades, second-hand-appropriate categories).
  - Note: H1 "Give Items a Second Life"; copy "Discover unique second-hand treasures and upcycled creations…", stats "Items Saved from Landfill", footer "Giving items a second chance". Filters: "Upcycled items only" special filter; condition grades New/Like New/Good/Fair/Worn; categories Furniture, Clothing, Electronics, Home Decor, Books, Sports, Toys, Other — all appropriate for a second-hand/upcycled marketplace. Cards also carry "Upcycled" badges.
