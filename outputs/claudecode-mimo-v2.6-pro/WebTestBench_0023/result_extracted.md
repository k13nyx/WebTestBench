# Test Result

## Functionality
- [X] FT-01: User can register a new account with valid credentials.
  - Action: Open the registration page, fill in username, email, and password with valid values, click "Register".
  - Expected: Registration succeeds and the new account is usable to sign in.

- [X] FT-02: Seller can create a listing with photo, description, price, and location.
  - Action: Sign in, open "Create Listing", upload a photo, enter title, description, price, location, condition and category, click "Publish".
  - Expected: The new listing is published and appears in the marketplace with all entered data.

- [X] FT-03: User can search items by keyword.
  - Action: Enter a keyword matching a default listing's title (e.g., a word from an existing listing) in the search bar and submit.
  - Expected: Only listings matching the keyword are shown in the results.

- [X] FT-04: User can filter results by category.
  - Action: On the browse page, select one category used by a default listing (e.g., "Furniture") in the Category filter.
  - Expected: Only listings in the selected category are displayed.

- [X] FT-05: User can filter results by price range.
  - Action: Set the price range filter (Min / Max) to a range covering some default listings but excluding others, and apply it.
  - Expected: Only listings whose price falls within the entered range are displayed.

- [X] FT-06: User can filter results by condition.
  - Action: Select one condition value (e.g., "Used") in the Condition filter.
  - Expected: Only listings with the selected condition are displayed.

- [X] FT-07: User can filter results by distance.
  - Action: Set the distance filter (e.g., "Within 10 km") from the current/search location and apply it.
  - Expected: Only listings located within the specified distance are displayed.

- [X] FT-08: User can sort results by price.
  - Action: Select "Price: Low to High" (and then "Price: High to Low") in the Sort control.
  - Expected: Results are re-ordered by price ascending (and then descending) with no items missing.

- [X] FT-09: Buyer can add an item to the cart.
  - Action: Open a default listing and click "Add to Cart".
  - Expected: The item appears in the cart page with its correct title and price.

- [ ] FT-10: Buyer can send a purchase request for an item.
  - Action: Open a default listing and click "Send Purchase Request".
  - Expected: The request is recorded and visible to the buyer with a pending status.
  - Bug Report:
    - Issue: Missing Purchase Request Tracking UI (request never shown to buyer with pending status)
    - Actual: The listing detail page offers only "Add to Cart" and "Message Seller" (no "Send Purchase Request"); the request can only be sent from the cart via "Send Purchase Request", which shows a transient toast "Purchase requests sent to sellers!" and empties the cart. No view shows the request or a pending status afterwards: the item page shows no request status, the cart shows "Your cart is empty", the account menu only has "My Profile / My Listings / Log out" (no requests entry), and "My Profile" opens a 404 "Oops! Page not found" page.

- [ ] FT-11: Seller can update their own listing.
  - Action: Open one of your own listings, click "Edit", change the price and description, and save.
  - Expected: The updated price and description are shown on the listing immediately after saving.
  - Bug Report:
    - Issue: Missing Edit Control (listing update not possible)
    - Actual: There is no "Edit" control anywhere: "My Listings" only offers "View", "Mark Sold" and "Delete", and the owner's detail page only shows a "Manage Your Listings" button. The price ($85) and description cannot be changed and saved; "Mark Sold" only changes the item status to Sold.

- [X] FT-12: Seller can remove their own listing when the item is no longer available.
  - Action: Open one of your own listings and click "Remove"/"Delete", then confirm.
  - Expected: The listing no longer appears in browse, search results, or its detail page.

## Constraint
- [X] CS-01: Cannot register with an email or username that is already taken.
  - Action: On the registration page, submit the form using the email of an existing account.
  - Expected: An error message (e.g., "Email already in use") is shown and no duplicate account is created.

- [X] CS-02: Cannot publish a listing with missing required fields or an invalid price.
  - Action: On "Create Listing", submit the form once with empty photo/description/price/location, then once with price "-5".
  - Expected: Each submission is rejected with a validation error identifying the invalid field; no listing is published.

- [X] CS-03: Cannot edit or remove a listing owned by another user.
  - Action: Open a default listing created by another user and look for "Edit" / "Remove" controls; attempt those actions if accessible.
  - Expected: The controls are absent or the actions are blocked with a permission message; the listing remains unchanged.

- [X] CS-04: Cannot add to cart or purchase-request an unavailable (removed) item.
  - Action: Attempt to add to cart / send a purchase request for a listing that the seller has removed (via its stale link or an item marked unavailable).
  - Expected: The action is blocked with a message such as "Item is no longer available"; the item is not added to the cart.

## Interaction
- [X] IX-01: Cart indicator updates immediately when an item is added.
  - Action: Click "Add to Cart" on a default listing and observe the cart icon/badge without reloading the page.
  - Expected: Confirmation feedback is shown and the cart count updates immediately to include the new item.

- [X] IX-02: Applying filters or sort updates the results in place and reflects the active selection.
  - Action: Select a category and a sort option on the browse page and observe the results list and the filter controls.
  - Expected: The results list updates immediately without a full page reload, and the controls show the currently selected values; when nothing matches, a "No items found" message is shown.

## Content
- [X] CT-01: Listing detail page shows all seller-entered data accurately.
  - Action: Open the detail page of a listing you created (with photo, description, price, location) and compare with what you entered.
  - Expected: The page displays the uploaded photo, description, price, location, condition, and category exactly as entered.

- [ ] CT-02: All displayed listing images and labels are relevant to second-hand/upcycled items.
  - Action: Browse the marketplace with default listings and inspect each listing card's photo, title, price, and condition label.
  - Expected: Every card shows a working, item-relevant photo (no broken/placeholder images) and a condition label (e.g., Used, Refurbished, Upcycled) consistent with the item.
  - Bug Report:
    - Issue: Broken Listing Image
    - Actual: The "Handmade Macrame Wall Hanging" card's photo does not load — `https://images.unsplash.com/photo-1622464689583-a09e88f0d34e?w=600&h=600&fit=crop` reports `complete=true` with `naturalWidth=0` (broken) on initial render and again after scrolling (all other 10 cards load correctly at 600×600). Condition labels are present on every card.
