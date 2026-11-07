# Test Checklist

## Functionality
- [ ] FT-01: Create a new product entry with review, affiliate link, category, and tags
  - Action: Open the product creation form and submit a product with a review, affiliate link, category, and at least one tag.
  - Expected: The product is saved and appears in the product listing.

- [ ] FT-02: Edit an existing product entry
  - Action: Open an existing product and change its review, category, or tags, then save.
  - Expected: The updated product reflects the edits in the listing/detail page.

- [ ] FT-03: Assign a product to one of the three categories (Tech Gadgets, Home Goods, Fitness Products)
  - Action: Create or edit a product and set its category to each of the three values.
  - Expected: The product is saved under the selected category and is browsable under it.

- [ ] FT-04: Add tags to a product entry
  - Action: Add one or more tags to a product and save.
  - Expected: The product displays the assigned tags and is retrievable by those tags.

- [ ] FT-05: Mark a product as featured
  - Action: Toggle the "featured" option on a product and save.
  - Expected: The product is flagged as featured and eligible for the homepage.

- [ ] FT-06: Browse products filtered to a single category
  - Action: Select the "Tech Gadgets" (or Home Goods / Fitness Products) category view.
  - Expected: Only products in that category are displayed.

- [ ] FT-07: Sort products by price
  - Action: Apply sort by price (ascending and descending).
  - Expected: Products reorder correctly by price in both directions.

- [ ] FT-08: Sort products by rating
  - Action: Apply sort by rating.
  - Expected: Products reorder correctly from highest to lowest rating.

- [ ] FT-09: Filter products by price range
  - Action: Set a minimum and/or maximum price range filter.
  - Expected: Only products within the price range are shown.

- [ ] FT-10: Filter products by minimum rating
  - Action: Set a minimum rating filter (e.g., 4 stars and up).
  - Expected: Only products meeting or exceeding the rating are shown.

- [ ] FT-11: Search products by keyword
  - Action: Enter a keyword into the search field and submit.
  - Expected: Only products matching the keyword (name, review, or tags) are returned.

- [ ] FT-12: Product detail page shows review, key specs, and external retailer button
  - Action: Open any product's detail page.
  - Expected: The page displays the written review, key specs, and a clearly labeled button linking to the external retailer.

## Constraint
- [ ] CS-01: Block product creation when required fields are empty
  - Action: Attempt to submit a product with the review, affiliate link, or category left empty.
  - Expected: Submission is blocked with a validation message identifying the missing required field.

- [ ] CS-02: Reject an invalid (non-URL) affiliate link
  - Action: Enter a non-URL value (e.g., "buyhere") in the affiliate link field and submit.
  - Expected: Submission is rejected and the link field is flagged as invalid.

- [ ] CS-03: Restrict category to the three allowed values
  - Action: Attempt to assign a category outside Tech Gadgets, Home Goods, or Fitness Products.
  - Expected: The category control offers only those three options and no other value can be saved.

## Interaction
- [ ] IX-01: Show a success confirmation after creating or editing a product
  - Action: Successfully create or edit a product.
  - Expected: A clear success message/toast is displayed confirming the action.

- [ ] IX-02: Display featured products on the homepage
  - Action: Open the homepage with one or more products marked featured.
  - Expected: Featured products are visibly shown in a dedicated homepage section.

## Content
- [ ] CT-01: Product images/icons are relevant to the product
  - Action: Inspect the image/icon shown for several products.
  - Expected: Each visual asset directly represents the corresponding product (tech gadget, home good, or fitness item).

- [ ] CT-02: Each product displays a non-empty, on-theme review
  - Action: Open several product detail/listing entries.
  - Expected: Every product shows a review that is populated and relevant to that product.