# Test Checklist

## Functionality
- [ ] FT-01: Filter listings by product category
  - Action: Select a specific category (e.g., "Cameras") from the category filter sidebar on the listings page.
  - Expected: The listing updates to display only products belonging to the "Cameras" category.
- [ ] FT-02: Filter listings by price range bands
  - Action: Select a predefined price range band (e.g., "$100 - $300") in the filter panel.
  - Expected: The listing refreshes to display only products whose prices fall within the chosen price range band.
- [ ] FT-03: Sort listings by overall score
  - Action: Choose "Overall Score" from the sort options dropdown.
  - Expected: Products are reordered descending from highest to lowest overall rating score.
- [ ] FT-04: Sort listings by publication date
  - Action: Choose "Date" (or "Newest") from the sort options dropdown.
  - Expected: Listings are reordered chronologically by publication or last updated date.
- [ ] FT-05: Search across products and articles
  - Action: Enter a common query keyword into the search bar and press Enter.
  - Expected: Search results return both matching product records and relevant articles (reviews, guides, comparisons).
- [ ] FT-06: View product detail page multi-criteria ratings and verdict
  - Action: Click on a product title or card from the listing to open its detail page.
  - Expected: Product detail page displays individual score breakdowns for criteria (Design, Performance, Value), an overall score, and a verdict summary.
- [ ] FT-07: Navigate to related reviews and comparisons from product detail page
  - Action: On a product detail page, click on a linked article in the "Featured In" or "Related Reviews & Comparisons" section.
  - Expected: The browser navigates directly to the corresponding long-form review or comparison article.
- [ ] FT-08: View long-form review article
  - Action: Open an in-depth review article from the articles section.
  - Expected: The article displays full long-form written analysis, detailed testing sections, author/date metadata, and the reviewed product profile.
- [ ] FT-09: View ranked "best of" list article
  - Action: Open a "Best of" guide article (e.g., "Best Vacuum Cleaners").
  - Expected: The page presents products in an ordered, numbered ranking with ranking badges and individual product summaries.
- [ ] FT-10: View multi-product side-by-side comparison page
  - Action: Open a side-by-side comparison page comparing two or more products.
  - Expected: Products are aligned side-by-side in parallel columns comparing key specs, rating criteria scores, and summary verdicts.

## Constraint
- [ ] CS-01: Filter combination with zero matching items
  - Action: Apply a category and price band combination that matches no available products.
  - Expected: An empty state message (e.g., "No products found matching your criteria") is displayed without broken layouts.
- [ ] CS-02: Empty search query submission
  - Action: Submit the search form with an empty input field or only whitespace characters.
  - Expected: The system prevents submission or displays an inline validation prompt without reloading to an empty/error page.
- [ ] CS-03: Minimum product selection for comparison
  - Action: Attempt to initiate a product comparison with fewer than two products selected.
  - Expected: The compare action button remains disabled or alerts the user that at least two products are required.

## Interaction
- [ ] IX-01: Dynamic listing update on filter toggle
  - Action: Check or uncheck a category or price band filter checkbox.
  - Expected: The product list updates immediately with an active visual indicator/tag showing the applied filter.
- [ ] IX-02: Search dropdown suggestions
  - Action: Type at least three characters into the global search bar without submitting.
  - Expected: An autocomplete/search suggestions dropdown appears showing instant matching product and article titles.
- [ ] IX-03: Comparison table spec row highlighting
  - Action: Hover the mouse cursor over a spec row (e.g., "Battery Life") in the side-by-side comparison table.
  - Expected: The entire horizontal row highlights across all compared product columns.
- [ ] IX-04: Clear all active filters
  - Action: Click the "Clear All" or "Reset Filters" button after applying multiple filters.
  - Expected: All selected filter checkboxes and price bands are reset, and the listing returns to the default unfiltered state.

## Content
- [ ] CT-01: Core category coverage
  - Action: Inspect the primary category navigation and filters.
  - Expected: Navigation options explicitly include designated categories: "Cameras", "Monitors", and "Vacuum Cleaners".
- [ ] CT-02: Criteria rating breakdown labels
  - Action: Verify the rating breakdown component on product detail pages.
  - Expected: Ratings are explicitly labeled with designated criteria including "Design", "Performance", and "Value".
- [ ] CT-03: Side-by-side comparison specification alignment
  - Action: Inspect row headers in the side-by-side comparison table.
  - Expected: Specification labels (e.g., Dimensions, Weight, Key Features) match across all compared products in consistent units and formats.