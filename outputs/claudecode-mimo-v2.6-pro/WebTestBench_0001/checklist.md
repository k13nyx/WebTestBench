# Test Checklist

## Functionality
- [ ] FT-01: Create a new product entry with all required details
  - Action: Open the create/add product form, fill in name, brief review, key specs, category, tags, price, rating, and an affiliate purchase link, then click "Save"/"Create".
  - Expected: The new product is created and appears in the product list with all entered values displayed on its entry/detail page.

- [ ] FT-02: Edit an existing product entry
  - Action: Open any existing product, click "Edit", change its review text and price, then save.
  - Expected: The product detail page and product list show the updated review text and price; no other fields are lost.

- [ ] FT-03: Categorize a product
  - Action: Edit an existing product and set its category to one of "Tech Gadgets", "Home Goods", or "Fitness"; save.
  - Expected: The product is saved with the chosen category and appears when browsing that category.

- [ ] FT-04: Tag a product
  - Action: Edit an existing product and add one or more tags (e.g., "budget", "wireless"); save.
  - Expected: The product's detail page displays the added tags, and the tags persist after leaving and revisiting the page.

- [ ] FT-05: Mark a product as featured
  - Action: Edit an existing product and enable the "Featured" setting; save, then open the homepage.
  - Expected: The product appears in the homepage's featured section; previously featured items remain until unmarked.

- [ ] FT-06: Browse products by category
  - Action: From the homepage or navigation, select a category (e.g., "Tech Gadgets").
  - Expected: The product list shows only products assigned to that category, including at least one default product.

- [ ] FT-07: Sort products by price and rating
  - Action: Open the product list and apply sorting "Price: Low to High", then "Price: High to Low", then "Rating: High to Low".
  - Expected: Each sort reorders the list correctly (prices ascending/descending, ratings descending) without hiding any products.

- [ ] FT-08: Filter products by price range and rating
  - Action: Set a price range (e.g., 0–50) and a minimum rating (e.g., 4 stars) using the filter controls, then apply.
  - Expected: Only products whose price falls within the range AND whose rating meets the minimum are shown; clearing filters restores the full list.

- [ ] FT-09: Search products by keyword
  - Action: Type a keyword matching an existing product (e.g., part of a product name or tag) into the search field and submit.
  - Expected: The search results page lists the matching product(s) with name, review excerpt, and price visible.

- [ ] FT-10: View a product's detail page
  - Action: Click any product card/title from the product list.
  - Expected: The detail page displays the product name, the full brief review, key specs, price, rating, and an external purchase button.

- [ ] FT-11: Use the affiliate purchase link
  - Action: Click the external purchase button (labeled with the retailer, e.g., "Buy at [Retailer]") on a product detail page.
  - Expected: The external retailer URL stored for that product opens (in a new tab), and the URL matches the affiliate link shown for the product.

## Constraint
- [ ] CS-01: Prevent saving a product with missing required fields
  - Action: Open the create product form and submit it with an empty name, empty review, or empty purchase link.
  - Expected: The form does not create the product; it shows a validation error identifying the missing required field(s).

- [ ] CS-02: Reject an invalid external purchase link
  - Action: In the create/edit product form, enter a non-URL value (e.g., "not a link") in the affiliate link field and save.
  - Expected: The save is rejected with a message that the purchase link must be a valid URL; no product is saved with the invalid link.

- [ ] CS-03: Prevent an invalid price range filter
  - Action: In the price range filter, enter a minimum price greater than the maximum price (e.g., min 100, max 10) and apply.
  - Expected: The filter does not produce a broken/empty-result state; an error or correction prompt is shown and the product list remains usable.

## Interaction
- [ ] IX-01: Confirm create/edit actions with success feedback
  - Action: Save a new product, then save an edit to an existing product.
  - Expected: Each save displays a visible success confirmation (e.g., toast "Product saved") that disappears automatically after a few seconds.

- [ ] IX-02: Homepage responds to featured changes
  - Action: Mark a product as featured and reload the homepage; then unmark it and reload again.
  - Expected: The homepage featured section updates accordingly — the product appears when featured and is removed when unfeatured, without requiring a server restart.

- [ ] IX-03: Sorting/filtering updates the list without full reload errors
  - Action: Change sort order, then adjust filters, in sequence on the product list page.
  - Expected: The product list refreshes each time to reflect the new order/filter; no blank page or error state occurs between changes.

## Content
- [ ] CT-01: Featured homepage content matches the site's niche themes
  - Action: View the homepage featured section and each featured product's category.
  - Expected: All featured products belong to tech gadgets, home goods, or fitness, with relevant names, review text, and product images — no placeholder or unrelated content.

- [ ] CT-02: Product detail pages show meaningful review and specs content
  - Action: Open 2–3 existing product detail pages and read the review and key specs sections.
  - Expected: Each page shows a brief, product-specific review and concrete key specs (e.g., dimensions, battery life) — not empty, generic, or duplicated text across products.

- [ ] CT-03: Purchase button label is clear and retailer-specific
  - Action: Inspect the external purchase button on several product detail pages.
  - Expected: Each button has a clear action label indicating an external purchase (e.g., "Buy at Amazon" / "Check Price at [Retailer]"), not vague text like "Click here" or "More".