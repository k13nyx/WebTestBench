# Test Result

## Functionality
- [ ] FT-01: Admin creates a new product entry
  - Action: Open the product admin/management area, fill in a new product with name, category (e.g., Tech Gadgets), brief review, price, rating, key specs, and an affiliate purchase link, then save.
  - Expected: The product is saved and appears in the product list with all entered data intact.
  - Bug Report:
    - Issue: Data Loss / Save Not Persisted (created product only held in in-memory SPA state)
    - Actual: The product "Anker PowerCore 10000" was created and briefly appeared in the admin list, but after a page reload /admin shows only the original 9 products (the new entry is gone), localStorage/sessionStorage are empty, /products reports "9 products found" without it, and its detail page returns "Product Not Found". The product is never durably saved to the product list.

- [X] FT-02: Admin edits an existing product entry
  - Action: Open an existing product's edit form, change its review text and price, then save.
  - Expected: The changes are persisted and the updated values are displayed when viewing the product again.
  - Action: Re-opened the created product's edit form, changed Full Review to "UPDATED REVIEW: Outstanding value portable charger..." and price from -10 to 39.99, clicked Save Changes.
  - Expected: Toast "Product updated successfully" appeared and the product was displayed again with $39.99 (admin card and Home Goods category card), Home category, and Featured badge.

- [X] FT-03: Admin assigns a category to a product
  - Action: Create or edit a product and select a category such as "Home Goods" or "Fitness".
  - Expected: The product is saved under the selected category and is retrievable from that category view.
  - Action: In the edit form, changed Category combobox from "Tech Gadgets" to "Home Goods" and saved.
  - Expected: Admin card badge changed to "Home", and navigating to /category/home listed "Anker PowerCore 10000" among only the Home Goods products.

- [ ] FT-04: Admin adds tags to a product
  - Action: Edit a product and add one or more tags (e.g., "budget", "wireless"), then save.
  - Expected: The tags are saved and shown on the product entry.
  - Bug Report:
    - Issue: Tags Never Displayed on Product Entry (and added tag absent from site tag index)
    - Actual: Tags "budget, wireless" were entered and saved with the toast confirmation, but they are never shown anywhere: product cards display no tags, the product's detail page (the only place tags render) returns "Product Not Found", and the listing page's Tags filter cloud does not contain "budget" (alphabetical list jumps appliance/automation → camera), so the added tag is not registered on any product view.

- [ ] FT-05: Admin marks a product as featured
  - Action: Edit a product and enable its "Featured" option, then save.
  - Expected: The product is flagged as featured and is included in the homepage featured section.
  - Bug Report:
    - Issue: Featured Product Missing from Homepage Featured Section
    - Actual: After enabling "Featured on homepage" and saving (admin/category cards show the Featured badge), the homepage "Editor's Top Picks" section still lists only Sony WH-1000XM5, Peloton Bike+, and Dyson V15 Detect. The newly featured "Anker PowerCore 10000" is not included; the homepage Home Goods section also still shows "3 products" and omits it entirely.

- [X] FT-06: Visitor browses products by category
  - Action: Click a category (e.g., Tech Gadgets) from the category navigation.
  - Expected: A list of only the products belonging to that category is displayed.
  - Action: Clicked the "Home" link in the header category navigation.
  - Expected: Page navigated to /category/home with heading "Home Goods" and displayed only Home-category products (Anker, Breville, Philips Hue, Dyson — all tagged "Home"); no Tech or Fitness products present.

- [X] FT-07: Visitor sorts the product list
  - Action: On a product listing page, select a sort option (e.g., price low-to-high or rating).
  - Expected: The product list reorders according to the selected sort criterion.
  - Action: Opened the sort combobox (default "Newest") and selected "Price: Low to High".
  - Expected: List reordered ascending by price: $39.99 (Anker) → $199 (Philips Hue) → $699 (Breville) → $749 (Dyson), replacing the previous order without page reload.

- [X] FT-08: Visitor filters products by price range
  - Action: Apply a price range filter (e.g., $0–$50) on a product listing.
  - Expected: Only products within the specified price range are shown.
  - Action: Opened Filters and dragged/clicked the dual-thumb Price Range slider to set a bounded range ($50–$670), after first validating a $0–$670 range.
  - Expected: With range $0–$670 only $39.99 and $199 products showed (Breville $699 and Dyson $749 excluded); with range $50–$670 only the $199 product showed (Anker $39.99 also excluded). Only in-range products were displayed in both cases.

- [X] FT-09: Visitor filters products by rating
  - Action: Apply a minimum rating filter (e.g., 4 stars and up).
  - Expected: Only products meeting the rating threshold are shown.
  - Action: In Filters, selected "4+ stars" in the Minimum Rating dropdown, then re-selected "4.5+ stars" to verify exclusion.
  - Expected: "4+ stars" kept all 4 Home products (all rated ≥4.4); "4.5+ stars" removed Philips Hue Starter Kit (4.4) and kept only Anker 4.5, Breville 4.5, Dyson 4.7 — only products meeting the threshold were shown.

- [X] FT-10: Visitor searches products by keyword
  - Action: Type a keyword matching an existing product name into the search box and submit.
  - Expected: Search results include products whose name or content matches the keyword.
  - Action: Typed "Dyson" into the listing page search box and pressed Enter.
  - Expected: The product list narrowed to only "Dyson V15 Detect" (all non-matching products removed).

- [X] FT-11: Product detail page displays all required content
  - Action: Open any product's detail page.
  - Expected: The page shows the review, key specs, price, rating, category/tags, and a purchase button.
  - Action: Opened /product/sony-wh-1000xm5 (also verified Dyson and Peloton detail pages).
  - Expected: Page shows "My Review" full text, "Key Specifications" (Driver Size 30mm, Battery Life 30 hours, Weight 250g, Bluetooth 5.2, Noise Cancelling Yes, Adaptive), price $399, rating 4.8 with stars, category "Tech", tags (headphones, wireless, noise-cancelling, premium), and a "Buy Now" purchase button.

- [X] FT-12: Affiliate purchase button opens the external retailer
  - Action: Click the purchase button on a product detail page.
  - Expected: The browser navigates to the external retailer URL configured for that product.
  - Action: Clicked "Buy Now" on the Sony WH-1000XM5 detail page.
  - Expected: A new tab opened at exactly the configured affiliate URL https://example.com/sony-xm5 ("Example Domain" page loaded).

## Constraint
- [X] CS-01: Product cannot be saved with missing required fields
  - Action: Attempt to save a new product without filling in required fields (e.g., name, price, or affiliate link).
  - Expected: The save is rejected and a validation message identifies the missing required field(s).
  - Action: Opened Add Product and clicked "Create Product" with all fields empty.
  - Expected: Save was rejected — toast "Please fill in all required fields" appeared, the form stayed open, and no product was added to the list.

- [ ] CS-02: A product must belong to exactly one valid category
  - Action: Attempt to save a product without selecting a category.
  - Expected: The save is rejected with a validation message requiring a category selection.
  - Bug Report:
    - Issue: Test Cannot Be Executed — No Empty Category State Supported (validation unobservable)
    - Actual: The Category field is always pre-selected ("Tech Gadgets") and the dropdown offers only three options (tech / home / fitness) with no empty or placeholder choice — verified in the DOM (`select` options: Tech Gadgets, Home Goods, Fitness only). It is impossible to submit the form without a category, so the required-category validation message can never be triggered or observed.

- [ ] CS-03: Price and rating inputs reject invalid values
  - Action: Attempt to enter a negative price or a rating outside the allowed range (e.g., 0–5).
  - Expected: The input is rejected with a validation message; the invalid value is not saved.
  - Bug Report:
    - Issue: Invalid Input Accepted — Negative Price Saved Successfully
    - Actual: Rating 6 was correctly blocked by native validation ("Value must be less than or equal to 5.", input min=0 max=5). However, Price accepts -10: the price input has no min/max constraints, the form submitted with toast "Product created successfully", and the product was listed displaying price "-$10". The invalid negative price was saved.

## Interaction
- [ ] IX-01: Featured products appear in the homepage featured section
  - Action: Load the homepage after a product has been marked as featured.
  - Expected: The featured product is visibly listed in the homepage's featured area, and unfeatured products are not.
  - Bug Report:
    - Issue: Newly Featured Product Not Listed in Homepage Featured Area
    - Actual: After marking "Anker PowerCore 10000" as featured and loading the homepage, the "Editor's Top Picks" featured section shows only the three originally-featured products (Sony WH-1000XM5, Peloton Bike+, Dyson V15 Detect); the newly featured product is absent (the homepage also shows "3 products" for Home Goods and omits it from that section). Unfeatured products are correctly excluded from the featured area.

- [X] IX-02: Saving a product provides confirmation feedback
  - Action: Save a new or edited product.
  - Expected: A visible success confirmation (e.g., toast/message) appears indicating the product was saved.
  - Action: Clicked "Create Product", then later "Save Changes" on an edited product.
  - Expected: Visible toasts appeared in the notification region: "Product created successfully" on create and "Product updated successfully" on edit.

- [X] IX-03: Search and filter controls update results without page reload delay issues
  - Action: Change a filter or submit a search query on a listing page.
  - Expected: The product list visibly refreshes to reflect the new criteria, and clearing the filter/search restores the full list.
  - Action: Applied price range, rating filter, sort, and search "Dyson" on /category/home; then clicked "Clear all filters" and cleared the search box.
  - Expected: Each change updated the list instantly in place (URL stayed /category/home, no reload); clearing filters restored price $0–$749, "Any rating", and the full 4-product list; clearing search restored all 4 products.

## Content
- [X] CT-01: Product images are present and relevant to the product
  - Action: Open several product detail pages across categories.
  - Expected: Each product displays an image that clearly corresponds to that product (not missing or showing unrelated media).
  - Action: Opened detail pages for Sony WH-1000XM5 (Tech), Dyson V15 Detect (Home), and Peloton Bike+ (Fitness) and inspected their main image elements.
  - Expected: Each page shows a loaded image (naturalWidth = 600) with alt text exactly matching the product name ("Sony WH-1000XM5", "Dyson V15 Detect", "Peloton Bike+") and a valid Unsplash image URL — no missing or broken images.

- [X] CT-02: Reviews and specs shown to visitors match the admin-entered content
  - Action: Compare a product's detail page against its entry in the admin edit form.
  - Expected: The displayed review text and key specs exactly match the saved admin content.
  - Action: Opened Sony WH-1000XM5's admin edit form and compared its Full Review and Specifications fields against the public detail page.
  - Expected: Exact match — review text ("The Sony WH-1000XM5 represents the pinnacle of wireless noise-cancelling headphones. …seamlessly between devices.") and all five specs (Driver Size/30mm, Battery Life/30 hours, Weight/250g, Bluetooth/5.2, Noise Cancelling/Yes, Adaptive) are identical on both the admin form and the visitor-facing "My Review"/"Key Specifications" sections.
