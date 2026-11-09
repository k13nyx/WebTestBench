# Test Checklist

## Functionality
- [ ] FT-01: Open a product detail page for a default product.
  - Action: Click any product tile/card from a default category listing.
  - Expected: A dedicated product detail page loads showing the product's name, image, description, and a verdict summary.
- [ ] FT-02: View multi-criteria ratings on a product detail page.
  - Action: Scroll the product detail page to the ratings section.
  - Expected: Individual ratings (e.g., Design, Performance, Value) and an overall score are displayed for the product.
- [ ] FT-03: View related reviews/comparisons from a product detail page.
  - Action: Locate the "Reviews & Comparisons" or equivalent block on the product detail page.
  - Expected: Clickable links to every review article and comparison the product appears in are listed.
- [ ] FT-04: Follow a link from a product to one of its review articles.
  - Action: Click a review link from FT-03.
  - Expected: The corresponding long-form review page opens with content directly about that product.
- [ ] FT-05: Open a side-by-side comparison page.
  - Action: Click any comparison article from a default "best of" list or product listing.
  - Expected: A comparison page loads displaying multiple products lined up in parallel columns/rows.
- [ ] FT-06: Verify comparison page content alignment.
  - Action: Inspect the comparison page from FT-05.
  - Expected: Key specs, per-criterion ratings, and summaries appear aligned side-by-side for each included product.
- [ ] FT-07: View a ranked "best of" list.
  - Action: Navigate to a default "best of" list (e.g., best cameras / monitors / vacuum cleaners).
  - Expected: A ranked list of products is displayed in a defined order (e.g., 1st, 2nd, 3rd).
- [ ] FT-08: Filter listings by category.
  - Action: From a product listing page, select a specific category filter (e.g., "Cameras").
  - Expected: The listing updates to show only products belonging to that category.
- [ ] FT-09: Filter listings by a price range band.
  - Action: Apply a price band filter (e.g., "$200–$500") to a product listing.
  - Expected: The listing shows only products whose price falls within that band.
- [ ] FT-10: Sort listings by overall score.
  - Action: Select "Sort by Overall Score" (ascending or descending) on a product listing.
  - Expected: Products reorder according to their overall rating in the chosen direction.
- [ ] FT-11: Sort listings by date.
  - Action: Select "Sort by Date" (newest/oldest) on a product listing.
  - Expected: Products reorder by their publish/update date in the chosen direction.
- [ ] FT-12: Search across products and articles.
  - Action: Enter a keyword (e.g., a product name or a category term) into the site search.
  - Expected: Search results include matching products AND matching review/comparison articles.

## Constraint
- [ ] CS-01: Category filter excludes other categories.
  - Action: Apply "Cameras" filter, then inspect the visible results.
  - Expected: No products from "Monitors" or "Vacuum Cleaners" appear in the result set.
- [ ] CS-02: Price range filter excludes out-of-band prices.
  - Action: Apply a $200–$500 band; spot-check several visible product prices.
  - Expected: Every visible product's price is ≥ $200 and ≤ $500.
- [ ] CS-03: Sort by overall score produces a non-decreasing/non-increasing order.
  - Action: Sort a listing by overall score and read the displayed scores in order.
  - Expected: Scores are in strictly monotonic order (asc or desc as selected); no score is out of place.
- [ ] CS-04: Sort by date produces a non-decreasing/non-increasing order.
  - Action: Sort a listing by date and read the displayed dates in order.
  - Expected: Dates are in strictly monotonic order; no item is out of chronological place.
- [ ] CS-05: Search returns at least one result type for a generic term.
  - Action: Search for a term that matches both a product and an article (e.g., a category name).
  - Expected: Both a Products section and an Articles (reviews/comparisons) section appear in the results.

## Interaction
- [ ] IX-01: Combining category + price band filters narrows results correctly.
  - Action: Select "Monitors" and a $300–$700 band simultaneously.
  - Expected: Listing shows only monitors priced within $300–$700; counts update to reflect the intersection.
- [ ] IX-02: Switching sort mode updates the listing immediately.
  - Action: Toggle from "Sort by Date" to "Sort by Overall Score" without reloading.
  - Expected: The product list visually reorders to match the newly selected sort, with no page refresh required.

## Content
- [ ] CT-01: Each default product displays all required rating criteria.
  - Action: Open detail pages of default products from different categories.
  - Expected: Every product shows ratings for Design, Performance, and Value (or the documented equivalent criteria set).
- [ ] CT-02: Default categories match the documented theme.
  - Action: Inspect the category filter/list of options on a product listing.
  - Expected: "Cameras", "Monitors", and "Vacuum Cleaners" are present among the available categories.