# Test Result

## Functionality

- [X] FT-01: Curator can create a new product entry
  - Action: Open the product creation form, fill in name, category (e.g., "Tech Gadgets"), price, rating, brief review, key specs, and affiliate purchase link, then save.
  - Expected: Product is saved and appears in the product list with exactly the entered data.

- [X] FT-02: Curator can edit an existing product entry
  - Action: Open a default product's edit form, change its review text and price, then save.
  - Expected: Changes persist — the listing card and detail page show the updated review and price.

- [X] FT-03: Curator can categorize and tag a product entry
  - Action: In a product's edit form, set its category to one of the three (e.g., "Fitness Products") and add tags (e.g., "cardio"), then save.
  - Expected: Product appears when browsing that category, and its tags are displayed on the product card or detail page.

- [X] FT-04: Curator can mark an item as featured on the homepage
  - Action: Toggle the "Featured" flag on a default product, save, then open the homepage.
  - Expected: The product appears in the homepage featured section.

- [X] FT-05: Visitors can browse products by category
  - Action: Click each category (Tech Gadgets, Home Goods, Fitness Products) from the navigation.
  - Expected: The listing shows only products belonging to the selected category, and all three categories contain default products.

- [X] FT-06: Visitors can sort products by price and rating
  - Action: On the product listing, apply "Sort by Price: Low to High", then "Sort by Rating: High to Low".
  - Expected: Products re-order correctly by ascending price, then by descending rating, on each sort change.

- [X] FT-07: Visitors can filter products by price range
  - Action: Apply a price range filter (e.g., min $20 / max $100) on the listing.
  - Expected: Only products priced within the range are displayed; out-of-range products are hidden.

- [X] FT-08: Visitors can filter products by rating
  - Action: Apply a rating filter (e.g., 4 stars and up).
  - Expected: Only products with rating ≥ 4 are displayed.

- [X] FT-09: Visitors can search products by keyword
  - Action: Type a keyword from a default product's name (e.g., a word in "Wireless Earbuds") into the search input and submit.
  - Expected: Products matching the keyword are shown; non-matching products are excluded.

- [X] FT-10: Each product has a detail page with review, specs, and purchase button
  - Action: Click a default product card to open its detail page.
  - Expected: The page shows the curator's review, key specs, and a clearly labeled purchase button for the external retailer.

- [X] FT-11: Purchase button opens the correct external retailer link
  - Action: Click the purchase/"Buy at retailer" button on a product detail page.
  - Expected: The external retailer page opens (new tab) at the URL saved as that product's affiliate link.

## Constraint

- [ ] CS-01: Product form enforces required fields
  - Action: In the creation form, leave name, category, or affiliate link empty and attempt to save.
  - Expected: Product is not saved and a validation message identifies each missing required field.
  - Bug Report:
    - Issue: Missing per-field required-field validation (generic validation feedback only).
    - Actual: The product is indeed not saved, but the only feedback is a generic toast "Please fill in all required fields" — no message identifies the individual missing fields; the empty Name/Category/Affiliate Link inputs show no inline error text, no error styling, and no `aria-invalid` attributes, so the user cannot tell which required field is missing.

- [X] CS-02: Homepage featured section shows only flagged items
  - Action: View the featured section, then un-feature one featured product and return to the homepage.
  - Expected: Only products with the Featured flag appear; the un-flagged product is removed from the section.

- [X] CS-03: Combined filters constrain results consistently
  - Action: On the listing, select a category and apply a price range filter plus a rating filter at the same time.
  - Expected: Only products satisfying ALL active filters are shown; no product violating any one filter appears.

## Interaction

- [X] IX-01: Save actions give success feedback
  - Action: Save a newly created product and save an edited product.
  - Expected: A success confirmation (toast/message) appears after each save, and the form closes or resets.

- [X] IX-02: Clearing search restores the full listing
  - Action: Run a keyword search, then clear the search input.
  - Expected: The listing returns to showing all default products without requiring a page reload.

- [X] IX-03: No-results searches show a friendly empty state
  - Action: Search for a keyword that matches no products (e.g., "zzzqqq").
  - Expected: A clear "no products found" message is shown instead of an empty page or error.

## Content

- [X] CT-01: Featured homepage items display complete, correct product data
  - Action: Compare each homepage featured item's name, price, rating, and category against its detail page.
  - Expected: All displayed values match the product's stored data with no missing fields (no blank prices/ratings).

- [X] CT-02: Detail page review and specs are relevant, real content
  - Action: Open detail pages for one product in each category (tech, home, fitness).
  - Expected: Each shows a genuine brief review and key specs specific to that product — no placeholder text (e.g., "Lorem ipsum") or specs belonging to another product.

- [X] CT-03: Product images match their product and category theme
  - Action: Check the image shown for several default products across Tech Gadgets, Home Goods, and Fitness Products.
  - Expected: Each image directly depicts its own product type (e.g., a gadget image for the tech product), loads without broken-image icons, and no image is repeated across unrelated products.
