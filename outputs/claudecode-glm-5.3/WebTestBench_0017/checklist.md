# Test Checklist

## Functionality

- [ ] FT-01: Product listing displays default products with key info
  - Action: Open the product listing page.
  - Expected: Default products are shown, each with product name, category (camera/monitor/vacuum cleaner), price, and overall score.

- [ ] FT-02: Filter listings by category
  - Action: Select the "Cameras" category filter on the product listing page.
  - Expected: Only camera products are displayed; all results belong to the Cameras category.

- [ ] FT-03: Filter listings by price range band
  - Action: Select a price range band (e.g., "$500–$1000") on the product listing page.
  - Expected: Only products whose price falls inside the selected band are shown; products outside the band are excluded.

- [ ] FT-04: Sort products by overall score
  - Action: Apply the "Sort by overall score" option on the product listing page.
  - Expected: Products are listed in descending order of overall score (highest first).

- [ ] FT-05: Sort products by date
  - Action: Apply the "Sort by date" option on the product listing page.
  - Expected: Products are listed newest-first (or selected order), and the order changes correctly versus the score sort.

- [ ] FT-06: Search across products and articles
  - Action: Type an existing product name into the search box and submit.
  - Expected: Results include both the matching product and any articles (reviews/comparisons/best-of lists) that mention it, each linking to its page.

- [ ] FT-07: Product detail page shows multi-criteria ratings and verdict
  - Action: Open any product detail page.
  - Expected: The page displays a rating for each criterion (e.g., Design, Performance, Value), an overall score, and a verdict summary text block.

- [ ] FT-08: Product detail page links to all reviews and comparisons it appears in
  - Action: Open a product detail page and click each listed "appears in" link.
  - Expected: Every link opens the correct review, comparison, or best-of list article that actually contains this product.

- [ ] FT-09: Comparison page aligns multiple products side by side
  - Action: Open any comparison article page.
  - Expected: Key specs, criterion ratings, and summary text for each product are aligned in parallel columns/rows so values for the same attribute line up across products.

- [ ] FT-10: Ranked "best of" list displays products in order
  - Action: Open any "best of" list article.
  - Expected: Products are displayed as a ranked list (e.g., #1, #2, #3) with rank numbers, and each entry links to its product detail page.

## Constraint

- [ ] CS-01: Combined category + price filters return only the intersection
  - Action: Select "Monitors" category AND a price band that only some monitors fall into.
  - Expected: Results contain only monitors within the selected price band; no product outside either condition appears.

- [ ] CS-02: Filter combination with no matches shows an empty state
  - Action: Select a category and price band combination where no product qualifies (e.g., "Vacuum Cleaners" + highest price band if none apply).
  - Expected: A clear "no results found" message is shown; no unrelated products are listed.

- [ ] CS-03: Search with no matches shows a clear empty state
  - Action: Search for a nonsense string (e.g., "zzxxqq123").
  - Expected: A "no results" message is displayed; no broken page, error, or unrelated results appear.

- [ ] CS-04: Overall score is consistent between listing and detail page
  - Action: Note a product's overall score on the listing page, then open its detail page and compare.
  - Expected: The overall score shown on the detail page exactly matches the score shown on the listing page for the same product.

## Interaction

- [ ] IX-01: Applying a filter updates the listing immediately
  - Action: Click a category filter on the product listing page.
  - Expected: The product list updates to reflect the filter without errors, and the updated list is visible without requiring a manual page refresh.

- [ ] IX-02: Active filter/sort selections are visually indicated
  - Action: Select one category filter and one sort option.
  - Expected: The selected filter and sort option are visibly highlighted/marked as active (e.g., filled button, checked state, bolded label).

- [ ] IX-03: Clearing search restores the full listing
  - Action: Perform a search, then clear the search box.
  - Expected: The listing returns to the complete, unfiltered default product list.

- [ ] IX-04: Clicking a product card navigates to its detail page
  - Action: Click any product card/entry in the listing.
  - Expected: The browser navigates to that product's detail page showing the same product name.

## Content

- [ ] CT-01: Site content covers the stated product categories
  - Action: Browse the listing, category filters, and articles.
  - Expected: Content includes products and articles for cameras, monitors, and vacuum cleaners, consistent with the in-depth product-review theme.

- [ ] CT-02: Product images are relevant to their product and category
  - Action: Inspect product images on the listing, detail, and comparison pages.
  - Expected: Each image depicts the correct product type (e.g., a camera product shows a camera image); no broken, placeholder, or mismatched images.

- [ ] CT-03: Reviews are long-form and substantive
  - Action: Open several review articles.
  - Expected: Each review contains substantial long-form content (multiple sections/paragraphs of analysis), not a short stub or placeholder text.

- [ ] CT-04: Comparison table values match product detail pages
  - Action: Pick two products in a comparison article and compare their spec values and ratings with their detail pages.
  - Expected: Specs and criterion ratings shown in the comparison exactly match those on the corresponding product detail pages.