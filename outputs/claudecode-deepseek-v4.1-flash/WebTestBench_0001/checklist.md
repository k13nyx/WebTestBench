# Test Checklist

## Functionality

- [ ] FT-01: Create a new product entry with all fields populated
  - Action: Go to the admin "Add Product" form, fill in Title, Category, Brief Review, Key Specs, Affiliate Link, and Tags, then click "Save".
  - Expected: Product is saved and appears in the admin product list and its assigned category listing.

- [ ] FT-02: Edit an existing product entry
  - Action: Open a default product, change its Title and Review, then click "Save".
  - Expected: Updated title and review persist after reload and display on the product card and detail page.

- [ ] FT-03: Assign a product to one of the three categories
  - Action: Create or edit a product, select "Tech Gadgets", "Home Goods", or "Fitness" in the Category dropdown, and save.
  - Expected: Product appears in the browse listing for the selected category only.

- [ ] FT-04: Add tags to a product entry
  - Action: In the product editor, add two tags (e.g., "wireless", "budget") in the Tags field and save.
  - Expected: Both tags are stored and displayed on the product card/detail page.

- [ ] FT-05: Mark a product as featured
  - Action: Toggle "Featured" on a default product and save.
  - Expected: That product appears in the homepage featured section.

- [ ] FT-06: Browse products by category
  - Action: Click each category ("Tech Gadgets", "Home Goods", "Fitness") in the category navigation.
  - Expected: Only products belonging to the selected category are listed.

- [ ] FT-07: Search products by keyword
  - Action: Enter a product keyword (e.g., a default product title word) in the search field and submit.
  - Expected: Products matching the keyword in title/review/tags are listed.

- [ ] FT-08: View product detail page content
  - Action: Click a product card to open its detail page.
  - Expected: Page shows the curator review and the key specs for that product.

- [ ] FT-09: Open the external retailer link from detail page
  - Action: Click the affiliate purchase button on a product detail page.
  - Expected: Browser navigates to the correct external retailer URL for that product.

- [ ] FT-10: Sort products by price and rating
  - Action: Apply "Price: Low to High", "Price: High to Low", and "Rating" sort options in sequence.
  - Expected: Product list reorders to match each selected sort attribute correctly.

## Constraint

- [ ] CS-01: Prevent saving a product with missing required fields
  - Action: Submit the "Add Product" form with Title, Category, and Affiliate Link left empty.
  - Expected: Save is blocked and field-level validation messages identify each missing required field; no product is created.

- [ ] CS-02: Unfeaturing a product removes it from the homepage
  - Action: Turn off "Featured" for a currently featured product and save, then load the homepage.
  - Expected: The product no longer appears in the homepage featured section.

- [ ] CS-03: Reject an invalid price range filter
  - Action: Set the price filter "Min" greater than "Max" and apply.
  - Expected: Filter is rejected or corrected with a visible error/hint; no nonsensical result set is shown.

- [ ] CS-04: Handle search/filter with no matching products
  - Action: Search for a random non-existent keyword and apply an impossible filter combination.
  - Expected: A clear "No products found" empty state is shown; no unrelated products are displayed.

## Interaction

- [ ] IX-01: Filtering updates results dynamically with visible active state
  - Action: Apply a price range and a minimum rating filter on the category listing.
  - Expected: List updates immediately to matching products and the applied filters are visibly indicated.

- [ ] IX-02: Show confirmation after creating or editing a product
  - Action: Save a newly created product and save an edited product.
  - Expected: A success message/toast confirms the save on both actions.

- [ ] IX-03: Show a featured indicator on featured products
  - Action: View the homepage and category listing containing a featured product.
  - Expected: Featured products display a distinct "Featured" badge/label.

## Content

- [ ] CT-01: Product reviews are brief and product-relevant
  - Action: Open several default product cards and detail pages.
  - Expected: Each review is a brief text block that clearly relates to the specific product and its category.

- [ ] CT-02: Key specs on detail pages are relevant to the product
  - Action: Review the key specs section on multiple product detail pages across categories.
  - Expected: Key specs list attributes appropriate to that product (e.g., battery/specs for gadgets, dimensions for home goods).

- [ ] CT-03: Homepage and imagery align with the curated niche theme
  - Action: Inspect the homepage featured section and product thumbnails across the site.
  - Expected: All featured items and images belong to tech gadgets, home goods, or fitness and are relevant to their product.