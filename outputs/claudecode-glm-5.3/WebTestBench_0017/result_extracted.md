# Test Result

## Functionality

- [X] FT-01: Product listing displays default products with key info
  - Action: Open the product listing page.
  - Expected: Default products are shown, each with product name, category (camera/monitor/vacuum cleaner), price, and overall score.

- [X] FT-02: Filter listings by category
  - Action: Select the "Cameras" category filter on the product listing page.
  - Expected: Only camera products are displayed; all results belong to the Cameras category.

- [ ] FT-03: Filter listings by price range band
  - Action: Select a price range band (e.g., "$500–$1000") on the product listing page.
  - Expected: Only products whose price falls inside the selected band are shown; products outside the band are excluded.
  - Bug Report:
    - Issue: Incorrect Filter Logic (price band filter matches an internal price-tier tag, not the product's actual price)
    - Actual: Selecting "Premium ($700-$1200)" shows 5 products: Canon EOS R6 Mark II ($2499), Fujifilm X-H2S ($2499), Sony A7 IV ($2499), LG 27GP950-B ($799), Samsung Bespoke Jet ($649). Three shown products are priced outside the band ($2499 ×3, $649), while products inside the band — Dell Alienware AW3423DWF ($1099) and Dyson V15 Detect ($749) — are excluded. The filter evidently selects products tagged "premium" regardless of their displayed price, and the tier tags are inconsistent with the band definitions (e.g., $2499 cameras tagged "premium", a $1099 monitor tagged "luxury").

- [X] FT-04: Sort products by overall score
  - Action: Apply the "Sort by overall score" option on the product listing page.
  - Expected: Products are listed in descending order of overall score (highest first).

- [X] FT-05: Sort products by date
  - Action: Apply the "Sort by date" option on the product listing page.
  - Expected: Products are listed newest-first (or selected order), and the order changes correctly versus the score sort.

- [X] FT-06: Search across products and articles
  - Action: Type an existing product name into the search box and submit.
  - Expected: Results include both the matching product and any articles (reviews/comparisons/best-of lists) that mention it, each linking to its page.

- [X] FT-07: Product detail page shows multi-criteria ratings and verdict
  - Action: Open any product detail page.
  - Expected: The page displays a rating for each criterion (e.g., Design, Performance, Value), an overall score, and a verdict summary text block.

- [X] FT-08: Product detail page links to all reviews and comparisons it appears in
  - Action: Open a product detail page and click each listed "appears in" link.
  - Expected: Every link opens the correct review, comparison, or best-of list article that actually contains this product.

- [X] FT-09: Comparison page aligns multiple products side by side
  - Action: Open any comparison article page.
  - Expected: Key specs, criterion ratings, and summary text for each product are aligned in parallel columns/rows so values for the same attribute line up across products.

- [ ] FT-10: Ranked "best of" list displays products in order
  - Action: Open any "best of" list article.
  - Expected: Products are displayed as a ranked list (e.g., #1, #2, #3) with rank numbers, and each entry links to its product detail page.
  - Bug Report:
    - Issue: Missing Rank Numbers in "Best Of" article
    - Actual: "The Best Mirrorless Cameras of 2024" expresses ranking only in prose ("Our top pick for most people is the Canon EOS R6 Mark II... The Sony A7 IV comes in as a close second") and shows an unranked "Products Mentioned" card grid with no #1/#2/#3 rank numbers, listed out of rank order (Sony A7 IV appears before top pick Canon EOS R6 Mark II). Same pattern in "The Best Cordless Vacuums of 2024" (sections "The Premium Choice"/"Best Value"/"For Hands-Free Cleaning", no rank numbers). Entries do link to product detail pages, but no rank numbers are displayed anywhere.

## Constraint

- [ ] CS-01: Combined category + price filters return only the intersection
  - Action: Select "Monitors" category AND a price band that only some monitors fall into.
  - Expected: Results contain only monitors within the selected price band; no product outside either condition appears.
  - Bug Report:
    - Issue: Filter Intersection Violation (price band condition not enforced against actual price)
    - Actual: Selecting "Monitors" + "Luxury ($1200+)" returns 2 products: Dell Alienware AW3423DWF ($1099) and ASUS ROG Swift PG32UCDM ($1299). The Dell monitor's price ($1099) falls outside the "$1200+" band, yet it appears in the results. Only the ASUS ($1299) actually satisfies both conditions; the category condition works but the price condition is violated (filter matches the internal "luxury" tag, not the price).

- [X] CS-02: Filter combination with no matches shows an empty state
  - Action: Select a category and price band combination where no product qualifies (e.g., "Vacuum Cleaners" + highest price band if none apply).
  - Expected: A clear "no results found" message is shown; no unrelated products are listed.

- [X] CS-03: Search with no matches shows a clear empty state
  - Action: Search for a nonsense string (e.g., "zzxxqq123").
  - Expected: A "no results" message is displayed; no broken page, error, or unrelated results appear.

- [X] CS-04: Overall score is consistent between listing and detail page
  - Action: Note a product's overall score on the listing page, then open its detail page and compare.
  - Expected: The overall score shown on the detail page exactly matches the score shown on the listing page for the same product.

## Interaction

- [X] IX-01: Applying a filter updates the listing immediately
  - Action: Click a category filter on the product listing page.
  - Expected: The product list updates to reflect the filter without errors, and the updated list is visible without requiring a manual page refresh.

- [X] IX-02: Active filter/sort selections are visually indicated
  - Action: Select one category filter and one sort option.
  - Expected: The selected filter and sort option are visibly highlighted/marked as active (e.g., filled button, checked state, bolded label).

- [ ] IX-03: Clearing search restores the full listing
  - Action: Perform a search, then clear the search box.
  - Expected: The listing returns to the complete, unfiltered default product list.
  - Bug Report:
    - Issue: Unresponsive Search Clear (stale filtered results remain)
    - Actual: After searching "Dyson" (page navigates to /search?q=Dyson showing 4 filtered results), clearing the search box and submitting has no effect — the page remains at /search?q=Dyson displaying the previous filtered results. No automatic return to the complete default product list occurs; the full 9-product listing is only reachable by explicitly navigating to /products via nav links. (Typing in the search box also does not filter the /products listing inline, so no restoration behavior exists at all.)

- [X] IX-04: Clicking a product card navigates to its detail page
  - Action: Click any product card/entry in the listing.
  - Expected: The browser navigates to that product's detail page showing the same product name.

## Content

- [X] CT-01: Site content covers the stated product categories
  - Action: Browse the listing, category filters, and articles.
  - Expected: Content includes products and articles for cameras, monitors, and vacuum cleaners, consistent with the in-depth product-review theme.

- [ ] CT-02: Product images are relevant to their product and category
  - Action: Inspect product images on the listing, detail, and comparison pages.
  - Expected: Each image depicts the correct product type (e.g., a camera product shows a camera image); no broken, placeholder, or mismatched images.
  - Bug Report:
    - Issue: Broken Product Image (HTTP 404)
    - Actual: The Roborock S8 Pro Ultra image (https://images.unsplash.com/photo-1603618090554-0df40bb5e4c7?w=600&q=80) fails to load on the product listing page and on its product detail page (naturalWidth = 0; direct HTTP request returns status 404). All other 8 product images load successfully (naturalWidth 600) with alt text matching their product names and distinct photo URLs per product.

- [X] CT-03: Reviews are long-form and substantive
  - Action: Open several review articles.
  - Expected: Each review contains substantial long-form content (multiple sections/paragraphs of analysis), not a short stub or placeholder text.

- [X] CT-04: Comparison table values match product detail pages
  - Action: Pick two products in a comparison article and compare their spec values and ratings with their detail pages.
  - Expected: Specs and criterion ratings shown in the comparison exactly match those on the corresponding product detail pages.
