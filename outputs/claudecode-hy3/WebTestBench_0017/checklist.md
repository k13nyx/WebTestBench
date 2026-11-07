# Test Checklist

## Functionality
- [ ] FT-01: User can view a long-form review article
  - Action: Open a review article from the listing or homepage.
  - Expected: The full long-form review content displays (title, body, ratings).
- [ ] FT-02: User can view a side-by-side comparison article
  - Action: Open a comparison article from the listing.
  - Expected: Comparison article displays multiple products compared together.
- [ ] FT-03: User can view a ranked "best of" list for a category
  - Action: Open a "best of" list (e.g., for cameras).
  - Expected: A ranked list of products in that category displays in ranked order.
- [ ] FT-04: User can open a product detail page
  - Action: Click a product name or card.
  - Expected: The product's detail page opens.
- [ ] FT-05: Product detail shows ratings across multiple criteria
  - Action: Open a product detail page.
  - Expected: Ratings are shown for multiple criteria (e.g., design, performance, value).
- [ ] FT-06: Product detail shows a verdict summary
  - Action: Open a product detail page.
  - Expected: A verdict summary text block is displayed.
- [ ] FT-07: Product detail links to all reviews and comparisons it appears in
  - Action: Open a product detail page.
  - Expected: A section lists links to every review and comparison featuring that product.
- [ ] FT-08: User can filter listings by category
  - Action: Select a category filter (e.g., "monitors").
  - Expected: Listings update to show only that category's items.
- [ ] FT-09: User can filter listings by price range band
  - Action: Select a price range band (e.g., "$100–$300").
  - Expected: Listings update to show only items within that price band.
- [ ] FT-10: User can sort listings by overall score
  - Action: Select "Sort by overall score".
  - Expected: Listings reorder by overall score (highest first).
- [ ] FT-11: User can sort listings by date
  - Action: Select "Sort by date".
  - Expected: Listings reorder by publication date (newest first).
- [ ] FT-12: User can search across products and articles
  - Action: Enter a query in the search box and submit.
  - Expected: Results include matching products and matching articles.
- [ ] FT-13: User can view a comparison page lining up specs, ratings, summaries
  - Action: Open a comparison page for several products.
  - Expected: Multiple products display together with key specs, ratings, and summaries.

## Constraint
- [ ] CS-01: Category filter excludes items from other categories
  - Action: Apply a single category filter.
  - Expected: No items from unselected categories appear in the results.
- [ ] CS-02: Price band filter includes only in-band items
  - Action: Apply a single price band filter.
  - Expected: No item priced outside the selected band appears in the results.
- [ ] CS-03: Product detail shows a complete set of criteria ratings (none missing)
  - Action: Open a product detail page.
  - Expected: Every defined criterion (design, performance, value, etc.) has a rating value; none are blank or absent.

## Interaction
- [ ] IX-01: Changing a filter or sort updates the listing dynamically
  - Action: Change category filter or sort option.
  - Expected: The listing re-renders with new results without a full page reload.
- [ ] IX-02: Comparison page aligns specs/ratings/summaries row-by-row
  - Action: Open a comparison page with multiple products.
  - Expected: Specs, ratings, and summaries are aligned in corresponding rows for side-by-side reading.

## Content
- [ ] CT-01: Category list includes cameras, monitors, and vacuum cleaners
  - Action: Open the category navigation/listing.
  - Expected: At minimum, "cameras", "monitors", and "vacuum cleaners" categories are present.
- [ ] CT-02: Product images are relevant to the actual product
  - Action: Open several product detail pages.
  - Expected: Displayed images depict the actual product, not unrelated or placeholder media.