# Test Checklist

## Functionality
- [ ] FT-01: User can register a new account and is logged in.
  - Action: Click "Sign Up", enter a unique name, valid email, and password, then click "Register".
  - Expected: The account is created, the user is logged in, and the header shows the entered name.
- [ ] FT-02: Seller can create a listing with photo, title, description, price, category, condition, and location.
  - Action: Click "Sell", fill in every field, upload one JPG photo, and click "Publish".
  - Expected: The new listing opens in detail view showing all entered values and the photo, and it appears under "My Listings".
- [ ] FT-03: Keyword search returns matching listings.
  - Action: Type a word from the title of a default listing (e.g., "lamp") into the search bar and press Enter.
  - Expected: Results include that listing, and every result's title or description contains the keyword.
- [ ] FT-04: Category and condition filters narrow results correctly.
  - Action: Select one category from the "Category" filter, then select one value from the "Condition" filter.
  - Expected: Every displayed result matches the selected category and condition, and no matching default listing is missing.
- [ ] FT-05: Price range filter returns only items within the range.
  - Action: Enter a minimum of 20 and a maximum of 100 in "Price" and click "Apply".
  - Expected: Every displayed item's price is between 20 and 100 inclusive.
- [ ] FT-06: Distance filter returns only items within the selected radius.
  - Action: Set the location to the default user location and select "10 km" in "Distance", then click "Apply".
  - Expected: Every displayed item shows a distance of 10 km or less from the location.
- [ ] FT-07: Sort options reorder results correctly.
  - Action: Select "Price: Low to High" from the "Sort by" dropdown, then select "Price: High to Low".
  - Expected: Results are ordered ascending by price, then descending by price, with no other changes to the result set.
- [ ] FT-08: User can add an item to the cart.
  - Action: Open a default listing and click "Add to Cart", then click the cart icon.
  - Expected: The item appears in the cart with its correct title, price, and photo.
- [ ] FT-09: User can send a purchase request for an item.
  - Action: Open a default listing, click "Request to Purchase", enter an optional message, and click "Send Request".
  - Expected: The request appears in "My Requests" with status "Pending" and the correct item title.
- [ ] FT-10: Seller can update an existing listing.
  - Action: Open one of your own listings, click "Edit", change the price to a new valid value and the description to new text, then click "Save".
  - Expected: The listing detail shows the new price and description, and the search results reflect the new price.
- [ ] FT-11: Seller can remove a listing that is no longer available.
  - Action: Open one of your own listings, click "Remove Listing", and confirm in the dialog.
  - Expected: The listing no longer appears in "My Listings" or in search results.

## Constraint
- [ ] CS-01: Registration rejects invalid or duplicate account details.
  - Action: Attempt to register with an email already in use, then with an email missing "@", leaving all other fields valid.
  - Expected: Registration is blocked, an inline error appears under the email field, and no account is created.
- [ ] CS-02: Listing cannot be published with required fields missing.
  - Action: Open "Sell", fill in all fields except the title, and click "Publish". Repeat with no photo.
  - Expected: "Publish" is blocked, the missing field is highlighted with an error message, and no listing is created.
- [ ] CS-03: Price input rejects zero, negative, and non-numeric values.
  - Action: In the "Price" field of the listing form, enter "0", then "-5", then "abc".
  - Expected: Each value is rejected with an error message, and the listing cannot be published with any of them.
- [ ] CS-04: Users cannot edit or remove listings they do not own.
  - Action: Open a default listing owned by another seller.
  - Expected: "Edit" and "Remove Listing" controls are not displayed, and the listing cannot be modified.
- [ ] CS-05: Guests are prompted to log in before adding to cart or sending a purchase request.
  - Action: Log out, open a default listing, and click "Add to Cart", then click "Request to Purchase".
  - Expected: Each action redirects to the login page, and the cart and "My Requests" remain unchanged.

## Interaction
- [ ] IX-01: Cart icon count updates immediately after adding an item.
  - Action: Note the cart badge count, click "Add to Cart" on a default listing, and observe the badge without reloading the page.
  - Expected: The badge count increases by exactly 1 immediately, with no page reload.
- [ ] IX-02: Filter and sort changes update results without a page reload, and "Clear Filters" resets everything.
  - Action: Apply a category filter and a price range, then click "Clear Filters".
  - Expected: The results and result count update on each change without a page reload, and after clearing, all filter fields show their defaults and the full result set returns.

## Content
- [ ] CT-01: Search result cards display complete, real content.
  - Action: Run a search with no filters applied and inspect several result cards.
  - Expected: Every card shows a photo (no broken or placeholder images), a title, a price with currency symbol, a condition label, a location, and a distance, with no empty fields.
- [ ] CT-02: Default listing photos match their titles and the marketplace theme.
  - Action: Open at least five default listings and compare each photo to its title and description.
  - Expected: Each photo depicts the item described in its title, and all listing text relates to second-hand or upcycled goods, with no lorem ipsum or unrelated text.