# Test Checklist

## Functionality
- [ ] FT-01: Create a new product entry with all required attributes
  - Action: Open the "Add Product" / "New Product" form; fill Name `QA Test Speaker`, Category `Tech Gadgets`, Price `199`, Rating `4`, brief Review `Compact speaker with solid battery life.`, at least one Spec (`Battery: 12h`), Affiliate URL `https://example-retailer.com/speaker`, Tags `audio, portable`; submit.
  - Expected: Product is saved and appears in the product listing and under the Tech Gadgets category, showing the entered price, rating, and review text.

- [ ] FT-02: Edit an existing default product
  - Action: Open an existing product's edit form, change its Price to `129` and append `Updated by QA.` to its review, then save.
  - Expected: The listing and the product detail page both display the new price `129` and the updated review text; all other fields are unchanged.

- [ ] FT-03: Re-categorize an existing product
  - Action: Open a default Fitness product, change its Category to `Home Goods`, save, then browse the Fitness category.
  - Expected: The product no longer appears under Fitness and now appears under Home Goods.

- [ ] FT-04: Add tags to a product and browse by that tag
  - Action: Add the tag `qaqc` to an existing product and save; then click/select the `qaqc` tag filter.
  - Expected: Only products carrying the `qaqc` tag are displayed; the tagged product is present and untagged products are absent.

- [ ] FT-05: Mark a product as featured and confirm it on the homepage
  - Action: Toggle "Featured" (or equivalent) on an existing default product, save, then open the homepage.
  - Expected: That product appears in the homepage featured section with its name, price, and rating visible.

- [ ] FT-06: Browse products by each category
  - Action: From the homepage/navigation, open each category page: Tech Gadgets, Home Goods, Fitness.
  - Expected: Each page lists a non-empty set of products, and every listed product belongs to that category.

- [ ] FT-07: Sort products by price and by rating
  - Action: On any category listing, select sort `Price: Low to High`, then `Price: High to Low`, then `Highest Rated`.
  - Expected: Listed prices are strictly ascending for the first sort, descending for the second, and ratings are descending for the third.

- [ ] FT-08: Filter products by price range and by minimum rating
  - Action: Apply price range min `50` / max `200`; then separately apply rating filter `4 stars & up`.
  - Expected: Only products priced between 50 and 200 are shown for the first filter; only products rated 4 or higher are shown for the second.

- [ ] FT-09: Search products by keyword
  - Action: Type a word taken from an existing default product's name (e.g. `kettle`) into the search box and submit.
  - Expected: That product appears in the results; products without the keyword in their name, review, or tags do not appear.

- [ ] FT-10: Product detail page shows review, key specs, and retailer button
  - Action: Open the detail page of any default product from the listing.
  - Expected: The page displays the product name, the full brief review, a key specs section with at least one spec row, and a clearly labeled purchase button (e.g. "Buy Now" / "View at Retailer") that carries the external retailer URL.

## Constraint
- [ ] CS-01: Required fields block product creation
  - Action: Open "Add Product", leave Name and Affiliate URL empty, fill the rest, submit.
  - Expected: The product is not saved; an inline error message (e.g. "Name is required") is shown next to each empty required field and the entry does not appear in the listing.

- [ ] CS-02: Invalid price and rating values are rejected
  - Action: Attempt to save a product with Price `-10` and then with Rating `6`; attempt again with Price `abc`.
  - Expected: Each attempt is rejected with a validation error and no product is saved with an invalid price or a rating outside 0–5.

- [ ] CS-03: Non-featured products are excluded from the homepage featured section
  - Action: Note a default product that is not marked featured, then load the homepage.
  - Expected: That product does not appear anywhere in the featured section; the featured section contains only items marked featured.

- [ ] CS-04: No-match search shows an explicit empty state
  - Action: Search for `zzqqxx12345`.
  - Expected: An explicit empty-state message (e.g. "No products found") is displayed; the page does not error out or render a blank results area.

## Interaction
- [ ] IX-01: Clicking a product card opens that product's detail page
  - Action: Click a product card in any listing or featured section.
  - Expected: The detail page for that exact product opens, with the product name matching the card that was clicked.

- [ ] IX-02: Sort and filter selections refresh the list in place and stay applied
  - Action: On a category listing, choose sort `Price: Low to High` and a price range filter, and observe the results grid.
  - Expected: The grid updates to the filtered/sorted set without leaving the page, and the chosen sort option and active filter remain visibly selected/indicated after the refresh.

- [ ] IX-03: Retailer button opens the external retailer link
  - Action: On a product detail page, click the retailer/purchase button.
  - Expected: The external retailer URL opens in a new browser tab, and the URL matches the affiliate link stored for that product.

## Content
- [ ] CT-01: Product cards show the essential summary information
  - Action: Inspect 3 default product cards in any listing.
  - Expected: Each card displays product name, category, price, rating, and a brief review (excerpt or full) — none of these are blank or showing placeholder text like "undefined" / "N/A".

- [ ] CT-02: Detail page content is complete and relevant to the product
  - Action: Open 2 different default product detail pages.
  - Expected: Each shows the product's own brief review text and its own key specs list; no review or spec text is duplicated from a different product or replaced by lorem ipsum/placeholder.

- [ ] CT-03: Only the three intended categories exist and are labeled correctly
  - Action: Open the category navigation/menu and list all available categories.
  - Expected: Exactly the categories Tech Gadgets, Home Goods, and Fitness are offered, labeled with those names, and every default product is assigned to one of them.