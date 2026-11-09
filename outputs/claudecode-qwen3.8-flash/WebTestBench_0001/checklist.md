# Test Checklist

## Functionality

- [ ] FT-01: Curator can create a new product entry with full details
  - Action: Open the product management area, use "Add Product", fill in name, category, price, rating, short review, key specs, and affiliate URL, then submit.
  - Expected: Save succeeds and the new product appears in the product listing and has its own detail page with all entered values.

- [ ] FT-02: Curator can edit an existing product
  - Action: Open an existing default product (e.g., from Tech Gadgets), change its review text and price, then save.
  - Expected: The product detail page and listing card both display the new review text and new price; no duplicate entry is created.

- [ ] FT-03: Each product can be categorized into one of the three curations
  - Action: Edit a default product and set/change its category to "Home Goods", then view the Home Goods category page.
  - Expected: The product now appears under Home Goods and no longer appears under its previous category page.

- [ ] FT-04: Each product can be tagged
  - Action: Add one or more tags (e.g., "budget", "best-of-2026") to a product and save, then click that tag from the product detail page.
  - Expected: Tags are displayed on the product, and clicking a tag shows a filtered list containing every product carrying that tag.

- [ ] FT-05: Curator can mark an item as featured on the homepage
  - Action: Toggle "Featured" ON for a default product, then load the homepage.
  - Expected: The product appears in the homepage featured section.

- [ ] FT-06: Visitors can browse products by category
  - Action: From the navigation, select each category in turn: Tech Gadgets, Home Goods, Fitness Products.
  - Expected: Each category page loads and lists only default products belonging to that category.

- [ ] FT-07: Visitors can filter products by price range
  - Action: Apply a price range filter (e.g., min 0 / max 50) on a category or listing page and apply it.
  - Expected: Only products priced within the selected range remain visible; all others disappear from the results.

- [ ] FT-08: Visitors can sort products by rating
  - Action: Choose sort option "Rating: High to Low" on a product listing.
  - Expected: Result cards re-order so that displayed rating values are non-increasing down the list.

- [ ] FT-09: Visitors can search by keyword
  - Action: Type a keyword present in a default product's name or review (e.g., "earbuds") into the site search and submit.
  - Expected: The results page lists the matching product(s) and excludes non-matching products.

- [ ] FT-10: Product detail page shows review, specs, and the retailer button
  - Action: Click any product card from a category page to open its detail page.
  - Expected: The detail page displays the full written review, the key specifications list, and one clearly labeled purchase button (e.g., "Buy at Retailer").

- [ ] FT-11: Purchase button links to the external retailer
  - Action: On a product detail page, inspect and click the purchase button.
  - Expected: The button points to that product's stored affiliate URL (correct domain visible in status bar) and navigating leaves this site for that retailer page.

## Constraint

- [ ] CS-01: Product cannot be saved with missing required fields
  - Action: In "Add Product", leave the name and affiliate URL empty (or fill any one required field blank) and click save.
  - Expected: The save is blocked, an inline validation message identifies the empty required field(s), and no incomplete product appears in the listing.

- [ ] CS-02: Affiliate link must be a valid external URL
  - Action: Enter an invalid retailer value such as "buy now" or "notaurl" in the affiliate link field and save.
  - Expected: The value is rejected with a validation error, or the product's purchase button is not rendered; no dead relative link is produced.

- [ ] CS-03: Price-range filter with min greater than max is rejected
  - Action: Set the price filter to min 200 / max 50 and apply.
  - Expected: The app either shows a range error or resets the filter; it never returns a full unfiltered product list as if the filter succeeded.

- [ ] CS-04: Only featured products appear on the homepage featured section
  - Action: Toggle "Featured" OFF for a product currently shown in the homepage featured section, then reload the homepage.
  - Expected: The product is removed from the featured section, and the section contains only products marked featured (no empty placeholder cards).

## Interaction

- [ ] IX-01: Confirmation shown after creating or editing a product
  - Action: Save a new product, then save an edit to an existing product.
  - Expected: A success message/toast (e.g., "Product saved") appears after each save and the view returns to the listing/detail without a manual reload.

- [ ] IX-02: Featured control reflects current state
  - Action: Open the featured toggle/checkbox for a product, then for a non-featured product.
  - Expected: The control shows ON for featured products and OFF for non-featured ones, and toggling it updates instantly (badge/label change) without leaving the page.

- [ ] IX-03: Active filters and sort are visibly indicated and can be cleared
  - Action: Apply a category, a price range, and a rating sort together, then use the "Clear"/"Reset filters" control.
  - Expected: The applied controls show their current values (selected category, range, sort option), and clearing them restores the full unfiltered, default-order product list.

- [ ] IX-04: Empty result state for search and filters
  - Action: Search for a keyword that matches nothing (e.g., "zzzqqq"), and separately filter to a price range containing no products.
  - Expected: A "no products found" message with guidance to adjust/clear filters is displayed; the page shows no broken cards and no JavaScript error.

## Content

- [ ] CT-01: All three categories are populated with relevant default products
  - Action: Open the Tech Gadgets, Home Goods, and Fitness Products category pages.
  - Expected: Each page lists at least one default product whose name and description genuinely belong to that theme (no cross-category mismatches, no lorem ipsum or "sample text").

- [ ] CT-02: Card data matches detail-page data
  - Action: Compare the name, price, rating, and review excerpt on a product card against the same product's detail page.
  - Expected: All shared values are identical; the detail page adds the full review and key specs rather than repeating placeholder content.

- [ ] CT-03: Product images and homepage copy are intact and on-theme
  - Action: Browse the homepage, each category page, and 3 product detail pages, checking every image and text block.
  - Expected: No broken/missing images or empty spec sections; hero and section copy describes curated gadget/home/fitness recommendations with affiliate links, with no unrelated placeholder text.