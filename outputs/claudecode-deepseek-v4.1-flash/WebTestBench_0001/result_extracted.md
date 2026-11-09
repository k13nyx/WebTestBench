# Test Result

## Functionality

- [X] FT-01: Create a new product entry with all fields populated
  - Action: Go to the admin "Add Product" form, fill in Title, Category, Brief Review, Key Specs, Affiliate Link, and Tags, then click "Save".
  - Expected: Product is saved and appears in the admin product list and its assigned category listing.
  - Note: Verified in a single SPA session — created "QA Session Gadget" (Home Goods, $149, tags "wireless, budget", spec "Battery / 10 hours"); it appeared in the admin list and in the Home Goods listing, and a success toast was shown. (See FT-02: the record does not survive a page reload.)

- [ ] FT-02: Edit an existing product entry
  - Action: Open a default product, change its Title and Review, then click "Save".
  - Expected: Updated title and review persist after reload and display on the product card and detail page.
  - Bug Report:
    - Issue: Changes are not persisted (no datastore / state lost on reload)
    - Actual: Changed Sony WH-1000XM5 → "Sony WH-1000XM5 Edited" with a new review; the card updated and a "Product updated successfully" toast appeared, but after reloading the admin page the title reverted to "Sony WH-1000XM5" and the original review. `localStorage`/`sessionStorage` are empty — data lives only in in-memory React state.

- [X] FT-03: Assign a product to one of the three categories
  - Action: Create or edit a product, select "Tech Gadgets", "Home Goods", or "Fitness" in the Category dropdown, and save.
  - Expected: Product appears in the browse listing for the selected category only.
  - Note: Created product assigned to "Home Goods" appeared under /category/home and not under /category/tech or /category/fitness.

- [X] FT-04: Add tags to a product entry
  - Action: In the product editor, add two tags (e.g., "wireless", "budget") in the Tags field and save.
  - Expected: Both tags are stored and displayed on the product card/detail page.
  - Note: Tags "wireless" and "budget" were saved and rendered as tag chips on the detail page.

- [ ] FT-05: Mark a product as featured
  - Action: Toggle "Featured" on a default product and save.
  - Expected: That product appears in the homepage featured section.
  - Bug Report:
    - Issue: Newly featured product not shown — homepage featured section is capped at 3 items
    - Actual: Toggling "Featured" on "Apple MacBook Pro 14\"" (and later "Samsung Galaxy S24 Ultra") saved successfully (switch aria-checked true, "Product updated successfully" toast), but the homepage "Editor's Top Picks" section still listed only the original 3 featured items (Sony, Peloton, Dyson). The new item appeared on the homepage only after another featured item was unfeatured (set went from 4 → 3).

- [X] FT-06: Browse products by category
  - Action: Click each category ("Tech Gadgets", "Home Goods", "Fitness") in the category navigation.
  - Expected: Only products belonging to the selected category are listed.
  - Note: /category/tech → Tech items only; /category/home → Home items only; /category/fitness → Fitness items only.

- [X] FT-07: Search products by keyword
  - Action: Enter a product keyword (e.g., a default product title word) in the search field and submit.
  - Expected: Products matching the keyword in title/review/tags are listed.
  - Note: Searching "sony" returned only "Sony WH-1000XM5".

- [X] FT-08: View product detail page content
  - Action: Click a product card to open its detail page.
  - Expected: Page shows the curator review and the key specs for that product.
  - Note: Detail pages render category, rating, short description, tags, a "Key Specifications" block, and a "My Review" section.

- [X] FT-09: Open the external retailer link from detail page
  - Action: Click the affiliate purchase button on a product detail page.
  - Expected: Browser navigates to the correct external retailer URL for that product.
  - Note: "Buy Now" on Sony WH-1000XM5 opened a new tab to `https://example.com/sony-xm5` (matches the product's affiliate link; `target="_blank"`).

- [X] FT-10: Sort products by price and rating
  - Action: Apply "Price: Low to High", "Price: High to Low", and "Rating" sort options in sequence.
  - Expected: Product list reorders to match each selected sort attribute correctly.
  - Note: Price Low→High produced ascending prices ($199…$2,495); High→Low descending; the rating option is labeled "Top Rated" (not "Rating") and sorted descending (4.9→4.4). Options present: Newest, Top Rated, Price: Low to High, Price: High to Low.

## Constraint

- [ ] CS-01: Prevent saving a product with missing required fields
  - Action: Submit the "Add Product" form with Title, Category, and Affiliate Link left empty.
  - Expected: Save is blocked and field-level validation messages identify each missing required field; no product is created.
  - Bug Report:
    - Issue: Missing field-level validation messages
    - Actual: Submitting with required fields empty did block the save and no product was created, but the only feedback was a generic toast "Please fill in all required fields". No per-field error text, no `aria-invalid`, and no `required` attributes exist — the form does not identify which specific field(s) are missing.

- [X] CS-02: Unfeaturing a product removes it from the homepage
  - Action: Turn off "Featured" for a currently featured product and save, then load the homepage.
  - Expected: The product no longer appears in the homepage featured section.
  - Note: Unfeaturing Sony WH-1000XM5 removed it from "Editor's Top Picks" on the homepage.

- [ ] CS-03: Reject an invalid price range filter
  - Action: Set the price filter "Min" greater than "Max" and apply.
  - Expected: Filter is rejected or corrected with a visible error/hint; no nonsensical result set is shown.
  - Bug Report:
    - Issue: Missing "Max" price control / no invalid-range validation (action cannot be performed)
    - Actual: The "Price Range" filter renders only a single slider labeled "Minimum" (range 0–2495) — there is no "Maximum"/Max control and no numeric Min/Max inputs. It is therefore impossible to set Min > Max, and no error or hint for an invalid range is ever presented.

- [X] CS-04: Handle search/filter with no matching products
  - Action: Search for a random non-existent keyword and apply an impossible filter combination.
  - Expected: A clear "No products found" empty state is shown; no unrelated products are displayed.
  - Note: Searching "zzzznonexistentkeywordzzz" showed "0 products found" plus a dedicated empty state: "No products match your filters. Try adjusting your search." with a "Clear all filters" action; no unrelated products rendered.

## Interaction

- [X] IX-01: Filtering updates results dynamically with visible active state
  - Action: Apply a price range and a minimum rating filter on the category listing.
  - Expected: List updates immediately to matching products and the applied filters are visibly indicated.
  - Note: Setting Minimum price to $1000 immediately reduced the list to the 3 products ≥ $1000; the Minimum Rating dropdown offers "Any rating / 4+ stars / 4.5+ stars" and combining it re-filtered instantly. A "Clear all filters" control appears as the active-filter indicator.

- [X] IX-02: Show confirmation after creating or editing a product
  - Action: Save a newly created product and save an edited product.
  - Expected: A success message/toast confirms the save on both actions.
  - Note: Create → toast "Product created successfully"; Edit → toast "Product updated successfully".

- [X] IX-03: Show a featured indicator on featured products
  - Action: View the homepage and category listing containing a featured product.
  - Expected: Featured products display a distinct "Featured" badge/label.
  - Note: Featured products show a distinct badge with a star icon and the text "Featured" on both the homepage and category listings.

## Content

- [X] CT-01: Product reviews are brief and product-relevant
  - Action: Open several default product cards and detail pages.
  - Expected: Each review is a brief text block that clearly relates to the specific product and its category.
  - Note: e.g., Sony "Industry-leading noise cancellation…"; Dyson "Intelligent cordless vacuum with laser dust detection…"; Peloton "Premium connected fitness bike…". All brief and on-topic.

- [X] CT-02: Key specs on detail pages are relevant to the product
  - Action: Review the key specs section on multiple product detail pages across categories.
  - Expected: Key specs list attributes appropriate to that product (e.g., battery/specs for gadgets, dimensions for home goods).
  - Note: Tech (Sony: Driver Size, Battery Life, Weight, Bluetooth, Noise Cancelling; MacBook: Chip, Memory, Storage, Display, Battery); Home (Dyson: Runtime, Bin Volume, Weight, Suction Power, Filtration; Philips Hue: Bulbs, Lumens, Color Range, Hub, Compatibility); Fitness (Peloton: Screen, Resistance Levels, Dimensions, Weight Capacity, Subscription; Theragun: Stall Force, Amplitude, Speed Range, Battery Life, Attachments).

- [X] CT-03: Homepage and imagery align with the curated niche theme
  - Action: Inspect the homepage featured section and product thumbnails across the site.
  - Expected: All featured items and images belong to tech gadgets, home goods, or fitness and are relevant to their product.
  - Note: Featured picks are Sony WH-1000XM5 (Tech), Peloton Bike+ (Fitness), Dyson V15 Detect (Home). All product images carry alt text matching the product name (e.g., "Sony WH-1000XM5") and use product-appropriate photo URLs.
