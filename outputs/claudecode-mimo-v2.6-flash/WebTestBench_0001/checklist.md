# Test Checklist

## Functionality
- [ ] FT-01: Admin creates a new product entry
  - Action: Open the product admin/management area, fill in a new product with name, category (e.g., Tech Gadgets), brief review, price, rating, key specs, and an affiliate purchase link, then save.
  - Expected: The product is saved and appears in the product list with all entered data intact.

- [ ] FT-02: Admin edits an existing product entry
  - Action: Open an existing product's edit form, change its review text and price, then save.
  - Expected: The changes are persisted and the updated values are displayed when viewing the product again.

- [ ] FT-03: Admin assigns a category to a product
  - Action: Create or edit a product and select a category such as "Home Goods" or "Fitness".
  - Expected: The product is saved under the selected category and is retrievable from that category view.

- [ ] FT-04: Admin adds tags to a product
  - Action: Edit a product and add one or more tags (e.g., "budget", "wireless"), then save.
  - Expected: The tags are saved and shown on the product entry.

- [ ] FT-05: Admin marks a product as featured
  - Action: Edit a product and enable its "Featured" option, then save.
  - Expected: The product is flagged as featured and is included in the homepage featured section.

- [ ] FT-06: Visitor browses products by category
  - Action: Click a category (e.g., Tech Gadgets) from the category navigation.
  - Expected: A list of only the products belonging to that category is displayed.

- [ ] FT-07: Visitor sorts the product list
  - Action: On a product listing page, select a sort option (e.g., price low-to-high or rating).
  - Expected: The product list reorders according to the selected sort criterion.

- [ ] FT-08: Visitor filters products by price range
  - Action: Apply a price range filter (e.g., $0–$50) on a product listing.
  - Expected: Only products within the specified price range are shown.

- [ ] FT-09: Visitor filters products by rating
  - Action: Apply a minimum rating filter (e.g., 4 stars and up).
  - Expected: Only products meeting the rating threshold are shown.

- [ ] FT-10: Visitor searches products by keyword
  - Action: Type a keyword matching an existing product name into the search box and submit.
  - Expected: Search results include products whose name or content matches the keyword.

- [ ] FT-11: Product detail page displays all required content
  - Action: Open any product's detail page.
  - Expected: The page shows the review, key specs, price, rating, category/tags, and a purchase button.

- [ ] FT-12: Affiliate purchase button opens the external retailer
  - Action: Click the purchase button on a product detail page.
  - Expected: The browser navigates to the external retailer URL configured for that product.

## Constraint
- [ ] CS-01: Product cannot be saved with missing required fields
  - Action: Attempt to save a new product without filling in required fields (e.g., name, price, or affiliate link).
  - Expected: The save is rejected and a validation message identifies the missing required field(s).

- [ ] CS-02: A product must belong to exactly one valid category
  - Action: Attempt to save a product without selecting a category.
  - Expected: The save is rejected with a validation message requiring a category selection.

- [ ] CS-03: Price and rating inputs reject invalid values
  - Action: Attempt to enter a negative price or a rating outside the allowed range (e.g., 0–5).
  - Expected: The input is rejected with a validation message; the invalid value is not saved.

## Interaction
- [ ] IX-01: Featured products appear in the homepage featured section
  - Action: Load the homepage after a product has been marked as featured.
  - Expected: The featured product is visibly listed in the homepage's featured area, and unfeatured products are not.

- [ ] IX-02: Saving a product provides confirmation feedback
  - Action: Save a new or edited product.
  - Expected: A visible success confirmation (e.g., toast/message) appears indicating the product was saved.

- [ ] IX-03: Search and filter controls update results without page reload delay issues
  - Action: Change a filter or submit a search query on a listing page.
  - Expected: The product list visibly refreshes to reflect the new criteria, and clearing the filter/search restores the full list.

## Content
- [ ] CT-01: Product images are present and relevant to the product
  - Action: Open several product detail pages across categories.
  - Expected: Each product displays an image that clearly corresponds to that product (not missing or showing unrelated media).

- [ ] CT-02: Reviews and specs shown to visitors match the admin-entered content
  - Action: Compare a product's detail page against its entry in the admin edit form.
  - Expected: The displayed review text and key specs exactly match the saved admin content.