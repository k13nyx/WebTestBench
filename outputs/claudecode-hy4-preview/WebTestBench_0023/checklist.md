# Test Checklist

Note: Button/label names below use common marketplace wording (e.g. "Sign Up", "Create Listing", "Add to Cart", "Send Purchase Request", "Edit", "Remove"). Map each to the app's equivalent label when executing.

## Functionality
- [ ] FT-01: New user can register an account
  - Action: Open the site, click "Sign Up"/"Register", fill name, email, and password, submit.
  - Expected: Account is created; the user is signed in (their name/account menu appears in the header) and no error message is shown.

- [ ] FT-02: Signed-in user can create a listing with photo, description, price, and location
  - Action: Click "Create Listing"; enter a title, description, price, location, category, and condition; upload one photo; submit.
  - Expected: Listing is created successfully and appears in the browse/listing results and in the user's own listings area.

- [ ] FT-03: Listing detail page shows all supplied information
  - Action: Open any default listing from the browse results.
  - Expected: The detail page displays the item photo, title, description, price, location, condition, and seller information.

- [ ] FT-04: Keyword search returns only matching listings
  - Action: In the search box, enter a word found in a default listing's title (e.g. "chair"), submit.
  - Expected: Only listings whose title/description contains that word are shown; unrelated listings are absent.

- [ ] FT-05: Filtering by category and by condition narrows results correctly
  - Action: In the browse view, select one category from the category filter, then select one condition value.
  - Expected: Every displayed listing belongs to the chosen category and matches the chosen condition.

- [ ] FT-06: Filtering by price range and by distance narrows results correctly
  - Action: Set a min and max price, then set a distance value/radius (with a location if prompted).
  - Expected: Every displayed listing has a price within the set range and a distance no greater than the set radius.

- [ ] FT-07: Results can be sorted by price
  - Action: In the browse view, choose the price low-to-high sort option, then the high-to-low option.
  - Expected: Prices appear in ascending order for the first option and descending order for the second.

- [ ] FT-08: Buyer can add an item to the cart
  - Action: Open a default listing that is not your own and click "Add to Cart".
  - Expected: The item is added to the cart; the cart view lists that item with its price.

- [ ] FT-09: Buyer can send a purchase request to the seller
  - Action: Open a default listing that is not your own and click "Send Purchase Request" (submit any required message/confirmation).
  - Expected: The request is submitted and confirmed to the buyer; it appears in the seller's incoming requests/notifications.

- [ ] FT-10: Seller can update and remove their own listing
  - Action: Open a listing you created, click "Edit", change the price and description, save; then reopen it and click "Remove"/"Delete".
  - Expected: The saved changes are visible on the listing, and after removal the listing no longer appears in the browse/search results.

## Constraint
- [ ] CS-01: Listing cannot be created with required fields left empty
  - Action: Open "Create Listing", leave title, description, price, and location empty, and submit.
  - Expected: Submission is blocked with a visible validation message for each empty required field; no listing is created.

- [ ] CS-02: Invalid price values are rejected
  - Action: Try to create a listing with a negative price, then with a non-numeric price (e.g. "abc").
  - Expected: Both submissions are rejected with a price validation error; no listing is created.

- [ ] CS-03: Seller-only controls appear only on the seller's own listings
  - Action: View a listing you created, then view a listing created by another user.
  - Expected: "Edit" and "Remove" controls appear only on your own listing; on another user's listing only buyer actions (cart / purchase request) are shown.

- [ ] CS-04: A removed listing is no longer reachable
  - Action: Remove one of your own listings, then search for it by its exact title and try to open its detail page.
  - Expected: The listing does not appear in search or browse results, and its detail page is not accessible (not-found message or redirect).

## Interaction
- [ ] IX-01: Creating a listing gives immediate feedback
  - Action: Submit a valid new listing through "Create Listing".
  - Expected: A success confirmation (message/toast) appears and the user is taken to the new listing or to their listings view.

- [ ] IX-02: Cart indicator updates when an item is added
  - Action: Note the cart indicator/count in the header, add a default item to the cart, then open the cart.
  - Expected: The cart count increases by one, and the cart shows the added item with a correct total price for the items in the cart.

- [ ] IX-03: Filters and sort apply immediately and stay visible
  - Action: Apply a category filter and a price sort in the browse view.
  - Expected: The result list updates in place without a full page reload, and the active filter/sort selections remain displayed (checked, highlighted, or as removable filter chips).

## Content
- [ ] CT-01: Listing photos load and match the listed item
  - Action: Browse the default listings and open three of them.
  - Expected: Every listing image loads (no broken-image icon or blank frame) and shows the actual listed product, not an unrelated or generic placeholder image.

- [ ] CT-02: Site content matches the second-hand/upcycled marketplace theme
  - Action: Review the home page heading, navigation, category names, and listing titles/descriptions.
  - Expected: All visible text is about second-hand or upcycled goods; category names fit that theme; no lorem ipsum, template filler, or unrelated placeholder text is present.

- [ ] CT-03: Price and distance are displayed in a readable, complete format
  - Action: Inspect listing cards in the browse results and one detail page.
  - Expected: Each price is shown as a currency amount (symbol or currency code with the number), and each distance is shown with a unit such as km or mi.