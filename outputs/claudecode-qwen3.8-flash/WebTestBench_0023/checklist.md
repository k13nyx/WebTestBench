# Test Checklist

## Functionality
- [ ] FT-01: New user can register and log in
  - Action: Click "Register"/"Sign Up", submit a valid name, email, and password; then log out and log back in with the same credentials.
  - Expected: Account is created and user is signed in (account name shown in header); subsequent login succeeds.

- [ ] FT-02: Logged-in user can create a complete listing
  - Action: As a signed-in seller, open "Create Listing"/"Sell", upload a photo, enter title, description, category, price, condition, and location, then submit.
  - Expected: Listing is saved; its detail page shows the photo, description, price, condition, and location; the item appears in browse/search results.

- [ ] FT-03: Keyword search returns matching items
  - Action: Enter a keyword present in a default listing's title/description (e.g., "denim jacket") and submit the search.
  - Expected: Matching listings are shown; unrelated listings are excluded.

- [ ] FT-04: Filters narrow results to matching items
  - Action: Apply category (e.g., "Clothing"), price range (e.g., 0–50), condition (e.g., "Good"), and distance (e.g., within 10 km) filters on the results page.
  - Expected: Every displayed result satisfies all active filters simultaneously.

- [ ] FT-05: Results can be sorted by price
  - Action: With multiple results shown, select "Price: Low to High", then "Price: High to Low".
  - Expected: Item cards are ordered by ascending price, then descending price.

- [ ] FT-06: Results can be sorted by distance
  - Action: Select the "Distance: Nearest first" sort option.
  - Expected: Listings are ordered by increasing distance from the reference location.

- [ ] FT-07: Buyer can add an item to the cart
  - Action: As a signed-in buyer, open a default listing and click "Add to Cart", then open the cart page.
  - Expected: The item appears in the cart with the correct title and price.

- [ ] FT-08: Buyer can send a purchase request
  - Action: On a default listing, click "Send Purchase Request"/"Make Offer", provide any requested message, and submit.
  - Expected: Request is submitted successfully with a visible confirmation (e.g., "Request sent").

- [ ] FT-09: Seller can update their own listing
  - Action: As the listing owner, click "Edit", change price and description, and save.
  - Expected: Detail page and search results display the updated values.

- [ ] FT-10: Seller can remove their own listing
  - Action: As the owner, click "Delete"/"Remove Listing" and confirm.
  - Expected: Listing no longer appears in search results; its detail URL shows an "unavailable"/not-found state.

## Constraint
- [ ] CS-01: Listing creation requires all mandatory fields
  - Action: Open "Create Listing" and submit with title, price, and photo left empty.
  - Expected: Submission is blocked with inline errors on each missing field; no listing is created.

- [ ] CS-02: Price must be a positive number
  - Action: Enter "-5", then "abc", in the price field of the create/edit listing form and submit.
  - Expected: A validation error (e.g., "Price must be a positive number") is shown and the listing cannot be saved.

- [ ] CS-03: Listing management is restricted to the owner; listing actions require login
  - Action: Open a default listing owned by another user while signed in as a different user, then as a logged-out visitor; also try opening "Create Listing" while logged out.
  - Expected: "Edit"/"Delete" controls are absent/inaccessible to non-owners and visitors; anonymous create-listing attempts redirect to login.

## Interaction
- [ ] IX-01: Success feedback after publishing a listing
  - Action: Create a valid listing via the FT-02 flow.
  - Expected: A success message/toast (e.g., "Listing published") appears and the user is redirected to the new listing.

- [ ] IX-02: Cart badge updates immediately when an item is added
  - Action: Note the cart icon's item count in the header, then click "Add to Cart" on a listing.
  - Expected: Header cart count increments by 1 without a manual page reload.

- [ ] IX-03: Listing removal requires explicit confirmation
  - Action: Click "Delete" on your own listing and choose "Cancel"; repeat and choose "Confirm".
  - Expected: Cancel leaves the listing intact and live; Confirm removes it.

- [ ] IX-04: No-results state is handled gracefully
  - Action: Search a nonsense term (e.g., "zzzx99") and apply a filter combination that excludes all default items (e.g., 0–1 price range).
  - Expected: A "No items found" message is displayed instead of a blank or broken results area.

## Content
- [ ] CT-01: Listing information is complete and consistent across views
  - Action: Compare a default listing's card in search results with its detail page.
  - Expected: Photo, title, price, condition, category, and location are present and identical in both; no placeholder text or lorem ipsum.

- [ ] CT-02: Listing photos load and depict the listed item
  - Action: Browse search results and open 3–4 default listings.
  - Expected: All images render (no broken-image icons) and each photo plausibly shows the second-hand/upcycled item being sold.

- [ ] CT-03: Site content matches the second-hand/upcycled marketplace theme
  - Action: Open the homepage and inspect the category/condition filter options.
  - Expected: Headings and copy reference second-hand and upcycled goods; filter options are relevant to used items (e.g., condition grades, second-hand-appropriate categories).