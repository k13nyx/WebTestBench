# Test Checklist

## Functionality
- [ ] FT-01: User can create a new product entry
  - Action: Open the "Add Product"/"New Product" form, enter a product name, review text, price, key specs, category, tags, external retailer URL, and save.
  - Expected: The product is saved and its card appears in the default product listing with the entered name, price, and category; a confirmation message is shown.

- [ ] FT-02: User can edit an existing product entry
  - Action: Open a default product, click "Edit", change its review text and price, and save.
  - Expected: The changes are saved and the new values are shown on the product's card and detail page; the original values are no longer displayed.

- [ ] FT-03: User can categorize a product
  - Action: On a default product, assign one of the categories (tech gadgets, home goods, fitness) and save.
  - Expected: The product appears under that category in the category listing and shows the assigned category label on its card and detail page.

- [ ] FT-04: User can tag a product
  - Action: On a default product, add one or more tags (e.g., "bluetooth", "kitchen") and save.
  - Expected: The tags are saved, are displayed on the product's card and detail page, and are returned when browsing/filtering by those tags.

- [ ] FT-05: User can mark a product as featured and it appears on the homepage
  - Action: On a default product, enable the "Featured" toggle/mark-as-featured control and save; then open the homepage.
  - Expected: The product is listed in the homepage's featured section, and the featured marker is shown on its card elsewhere in the site.

- [ ] FT-06: Visitor can browse products by category
  - Action: Open the product listing and select each category (tech gadgets, home goods, fitness).
  - Expected: The listing shows only products belonging to the selected category, with the current category visibly indicated.

- [ ] FT-07: Visitor can sort the product list by price and by rating
  - Action: On the product listing, select "Price" sorting and then "Rating" sorting (both ascending and descending options if offered).
  - Expected: The displayed order changes accordingly — lowest price first when sorted by price ascending, highest-rated products first when sorted by rating descending — and every visible card's price/rating matches that order.

- [ ] FT-08: Visitor can filter products by price range and by rating
  - Action: On the product listing, set a minimum/maximum price range and apply; then set a minimum rating and apply.
  - Expected: After the price filter, every displayed product's price falls within the chosen range; after the rating filter, every displayed product's rating is at or above the chosen value.

- [ ] FT-09: Visitor can search products by keyword
  - Action: Enter a keyword from a default product's name, review, or tag into the search box and submit.
  - Expected: The results include the matching product(s), and non-matching products are excluded from the result list.

- [ ] FT-10: Each product has a detail page with review, key specs, and retailer link
  - Action: Click a product card/title in any listing to open its detail page.
  - Expected: The detail page shows that product's review text, its key specs, and a clearly labelled purchase/retailer button linking to the external retailer.

## Constraint
- [ ] CS-01: A product cannot be saved with missing required data or an invalid retailer link
  - Action: Open the Add Product form, leave the product name, review, category, and retailer URL blank (one at a time) and attempt to save; then enter a non-URL string (e.g., "not a link") as the retailer URL and save.
  - Expected: Saving is blocked for each case, an error message identifies the invalid field, and no incomplete/empty product entry is created in the listing.

- [ ] CS-02: Filtering never returns products that fail the filter criteria
  - Action: Apply a narrow price range and a high minimum rating (e.g., price 100–150 and rating 4+) and inspect every result card's price and rating; also apply a price range and rating that no default product satisfies.
  - Expected: Every result satisfies both active criteria, and when no product satisfies them, zero product cards are shown (not the full list, not an error page).

- [ ] CS-03: A search with no matching results shows an empty state and can be cleared
  - Action: Search for a nonsense keyword (e.g., "xyzqwerty123"), then clear the search box.
  - Expected: A "no results"/no products found message is shown with zero product cards, and after clearing the search the full default product list is displayed again.

## Interaction
- [ ] IX-01: Clicking a product card opens that product's detail page
  - Action: Click the card image/title of a default product in the listing.
  - Expected: The browser navigates to the matching product's detail page showing that product's name, review, specs, and retailer button.

- [ ] IX-02: The retailer button opens the external store link
  - Action: Click the "Buy"/"View on retailer" button on a product detail page.
  - Expected: The external retailer URL opens in a new tab/window (the site itself stays on the product detail page), and the URL matches the retailer link stored for that product.

- [ ] IX-03: The edit form opens pre-filled and saving confirms the update
  - Action: Click "Edit" on a default product and observe the form fields; save without changes, then change the price and save again.
  - Expected: The form is pre-populated with the product's current name, review, price, category, and tags; after saving, a confirmation message appears and the updated price is shown on the product's card and detail page.

- [ ] IX-04: Featured products are visibly marked in listings
  - Action: Browse the main product listing and view a card for a product that has been marked as featured.
  - Expected: That card displays a clearly visible featured indicator (e.g., "Featured" badge/label), while non-featured cards do not.

## Content
- [ ] CT-01: The homepage featured section contains exactly the featured products
  - Action: Mark one default product as featured and unmark another that was featured; then open the homepage.
  - Expected: The featured section lists the marked product and omits the unmarked one, and each entry links to the correct product's detail page.

- [ ] CT-02: Product detail page shows the correct, complete saved content
  - Action: Open the detail pages of two different default products and compare the displayed review, key specs, price, and category with what was entered/saved for each.
  - Expected: Each detail page shows that product's own review text, key specs, price, and category — no placeholder text, no "TBD", and no content copied from the other product.

- [ ] CT-03: Category and tag labels match each product's assignments
  - Action: View product cards and detail pages for products in each category and for products with multiple tags.
  - Expected: Every product displays its assigned category label (tech gadgets / home goods / fitness) and all of its saved tags, with no missing or extra labels shown.