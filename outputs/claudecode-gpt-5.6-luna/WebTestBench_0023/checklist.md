# Test Checklist

## Functionality
- [ ] FT-01: User can register for a marketplace account.
  - Action: Open **Register**, enter valid name, email, password, and required details, then select **Register**.
  - Expected: The account is created and the user is signed in or shown a registration-success confirmation.

- [ ] FT-02: User can create a second-hand or upcycled product listing.
  - Action: Open **Create Listing**, upload a product photo, enter a description, price, location, category, and condition, then select **Publish Listing**.
  - Expected: The listing is published and displays the submitted photo, description, price, location, category, and condition.

- [ ] FT-03: User can search marketplace listings by keyword.
  - Action: Enter a keyword matching a default listing in the **Search** field and submit the search.
  - Expected: The results contain listings relevant to the entered keyword.

- [ ] FT-04: User can filter listings by category, price range, condition, and distance.
  - Action: Apply each available filter using values that match at least one default listing.
  - Expected: Results update so every displayed listing matches all selected filters.

- [ ] FT-05: User can sort listing results.
  - Action: Select each available sort option, including price and distance where provided.
  - Expected: Listings reorder according to the selected sort option.

- [ ] FT-06: Buyer can add an available default listing to the cart.
  - Action: Open an available listing and select **Add to Cart**, then open **Cart**.
  - Expected: The selected listing appears in the cart with its correct title, price, and quantity.

- [ ] FT-07: Buyer can send a purchase request for an available listing when that option is provided.
  - Action: Open an available listing, select **Send Purchase Request**, complete any required request fields, and submit.
  - Expected: The purchase request is submitted and associated with the selected listing.

- [ ] FT-08: Seller can update an existing seller-owned listing.
  - Action: Open a seller-owned default listing, select **Edit**, change its description or price, and save the listing.
  - Expected: The listing displays the updated value after saving and reopening it.

- [ ] FT-09: Seller can remove an existing seller-owned listing.
  - Action: Open a seller-owned default listing, select **Remove Listing** or **Delete**, and confirm the removal.
  - Expected: The listing no longer appears in the seller’s listings or marketplace search results.

## Constraint
- [ ] CS-01: Listing publication requires all required product information.
  - Action: Open **Create Listing**, leave the photo, description, price, or location empty one at a time, and select **Publish Listing**.
  - Expected: The listing is not published and the missing field is identified as required.

- [ ] CS-02: Listing price accepts only a valid non-negative monetary value.
  - Action: Enter letters, symbols, a negative value, and an empty value in **Price**, then attempt to publish.
  - Expected: The listing is blocked and a price-validation message is shown for each invalid value.

- [ ] CS-03: Buyers cannot purchase or request an unavailable listing.
  - Action: Open a default listing marked unavailable or removed from sale.
  - Expected: **Add to Cart** and **Send Purchase Request** are hidden or disabled, and no purchase action can be submitted.

- [ ] CS-04: A seller cannot edit or remove a listing owned by another account.
  - Action: While signed in as a different user, open another seller’s default listing.
  - Expected: **Edit** and **Remove Listing** controls are unavailable.

## Interaction
- [ ] IX-01: Search and filter controls update the displayed results.
  - Action: Enter a search term and apply or clear a filter without refreshing the page.
  - Expected: Results update to reflect the change, and clearing the filter restores listings excluded only by that filter.

- [ ] IX-02: Cart state updates after adding an item.
  - Action: Add an available default listing to the cart.
  - Expected: The cart count or cart contents updates immediately and shows the selected item.

- [ ] IX-03: Successful listing changes provide clear user feedback.
  - Action: Successfully publish, update, or remove a listing using the available seller controls.
  - Expected: A visible success confirmation appears, and the listing view reflects the completed action.

## Content
- [ ] CT-01: Marketplace listings are relevant to second-hand or upcycled products.
  - Action: Review the default listing titles, descriptions, categories, and photos.
  - Expected: Each listing clearly represents a second-hand, reused, refurbished, or upcycled product.

- [ ] CT-02: Listing details are complete and consistent wherever displayed.
  - Action: Open a default listing from search results, apply a filter, and view it in the cart or purchase-request flow.
  - Expected: The title, photo, price, condition, location, and description remain consistent across all views.