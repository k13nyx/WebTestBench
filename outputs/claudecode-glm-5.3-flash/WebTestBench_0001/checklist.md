# Test Checklist

## Functionality
- [ ] FT-01: Create a new product entry
  - Action: Open the product creation form, fill in name, review text, specs, price, rating, category (e.g., "Tech Gadgets"), tag(s), and an external retailer URL, then submit.
  - Expected: The product is saved and appears in the product list with the entered details.
- [ ] FT-02: Edit an existing product entry
  - Action: Open an existing product's edit form, change its review text and price, then save.
  - Expected: The detail page and list views reflect the updated review text and price.
- [ ] FT-03: Assign/change a product's category
  - Action: Edit a product and change its category from its current one (e.g., "Home Goods" to "Fitness").
  - Expected: The product now appears under the new category when browsing and no longer under the old one.
- [ ] FT-04: Add tags to a product
  - Action: Edit a product and add one or more tags (e.g., "budget", "wireless"), then save.
  - Expected: The tags are displayed on the product's card/detail page.
- [ ] FT-05: Mark a product as featured
  - Action: Toggle "featured" on a product via the edit form or product list control.
  - Expected: The product appears in the featured section on the homepage.
- [ ] FT-06: Browse products by category
  - Action: From the homepage or navigation, select a category (e.g., "Fitness").
  - Expected: Only products belonging to that category are listed.
- [ ] FT-07: Sort products
  - Action: On the product listing page, choose a sort option (e.g., sort by price ascending, then by rating).
  - Expected: Products reorder correctly according to the selected sort attribute.
- [ ] FT-08: Filter products by price range
  - Action: Apply a price range filter (e.g., min $0 / max $50) on the listing page.
  - Expected: Only products with prices within the specified range are shown.
- [ ] FT-09: Filter products by rating
  - Action: Apply a rating filter (e.g., minimum rating 4 stars).
  - Expected: Only products with rating ≥ the selected value are shown.
- [ ] FT-10: Search products by keyword
  - Action: Enter a keyword matching an existing product name or review (e.g., a known product name fragment) into the search box and submit.
  - Expected: Matching products are shown; non-matching products are excluded.
- [ ] FT-11: View product detail page
  - Action: Click a product card/title from any listing.
  - Expected: The detail page shows the review text, key specs (price, rating, etc.), and an external retailer link button.
- [ ] FT-12: External retailer link works
  - Action: On a product detail page, click the purchase/affiliate link button.
  - Expected: The browser navigates to the product's external retailer URL (correct target as entered in the entry).
- [ ] FT-13: Unfeature a product removes it from homepage
  - Action: Toggle "featured" off on a currently featured product.
  - Expected: The product no longer appears in the homepage featured section.

## Constraint
- [ ] CS-01: Product cannot be created without required fields
  - Action: Submit the product creation form with the name (and/or other required fields) left empty.
  - Expected: Submission is blocked and a validation message is shown; no empty product is created.
- [ ] CS-02: Every product must belong to a category
  - Action: Attempt to create or save a product without selecting a category.
  - Expected: Submission is blocked with a validation message, or a default category is enforced — the product is never left category-less in listings.
- [ ] CS-03: Retailer link must be a valid URL
  - Action: Enter an invalid retailer URL (e.g., "not-a-url") in the product form and save.
  - Expected: Validation error is shown and the product is not saved with the invalid link.
- [ ] CS-04: Filters and search combine correctly
  - Action: Apply a category browse plus a price filter plus a keyword search simultaneously.
  - Expected: Only products satisfying ALL active conditions are displayed; no contradictory/empty-state error.

## Interaction
- [ ] IX-01: Success feedback after saving a product
  - Action: Create or edit a product and submit the form.
  - Expected: A visible success confirmation (e.g., toast or message like "Product saved") appears.
- [ ] IX-02: Clicking a category/filter visibly updates the list without errors
  - Action: Click a category link or change a filter/sort control on the listing page.
  - Expected: The product list updates immediately to reflect the selection with no console/page errors.

## Content
- [ ] CT-01: Product detail shows a complete review and specs
  - Action: Open any pre-existing product's detail page.
  - Expected: The page displays a non-empty review text and key specs (at least price and rating) relevant to that product.
- [ ] CT-02: Product images/content are relevant to the product
  - Action: Inspect product cards and detail pages of default products.
  - Expected: Any displayed image/icon matches the product's type (tech gadget, home good, fitness product) — no placeholder or unrelated media.