# Test Result

## Functionality

- [X] FT-01: Open a product detail page for a default product.
  - Action: Click any product tile/card from a default category listing.
  - Expected: A dedicated product detail page loads showing the product's name, image, description, and a verdict summary.

- [X] FT-02: View multi-criteria ratings on a product detail page.
  - Action: Scroll the product detail page to the ratings section.
  - Expected: Individual ratings (e.g., Design, Performance, Value) and an overall score are displayed for the product.

- [X] FT-03: View related reviews/comparisons from a product detail page.
  - Action: Locate the "Reviews & Comparisons" or equivalent block on the product detail page.
  - Expected: Clickable links to every review article and comparison the product appears in are listed.

- [X] FT-04: Follow a link from a product to one of its review articles.
  - Action: Click a review link from FT-03.
  - Expected: The corresponding long-form review page opens with content directly about that product.

- [X] FT-05: Open a side-by-side comparison page.
  - Action: Click any comparison article from a default "best of" list or product listing.
  - Expected: A comparison page loads displaying multiple products lined up in parallel columns/rows.

- [X] FT-06: Verify comparison page content alignment.
  - Action: Inspect the comparison page from FT-05.
  - Expected: Key specs, per-criterion ratings, and summaries appear aligned side-by-side for each included product.

- [ ] FT-07: View a ranked "best of" list.
  - Action: Navigate to a default "best of" list (e.g., best cameras / monitors / vacuum cleaners).
  - Expected: A ranked list of products is displayed in a defined order (e.g., 1st, 2nd, 3rd).
  - Bug Report:
    - Issue: Missing Visual Ranking
    - Actual: On "Best Of" articles (e.g., /article/best-mirrorless-cameras-2024, /article/best-cordless-vacuums-2024), the "Products Mentioned" section lists products as plain cards without any explicit 1st/2nd/3rd ranking badges or position labels. Although the article text describes a ranking ("Our top pick...", "comes in as a close second..."), the visually-displayed product list is not in the ranked order (e.g., Canon R6 Mark II ranked 1st in text but appears 2nd in the products list).

- [ ] FT-08: Filter listings by category.
  - Action: From a product listing page, select a specific category filter (e.g., "Cameras").
  - Expected: The listing updates to show only products belonging to that category.
  - Bug Report:
    - Issue: Filter Implementation Defect (Price Filter Mis-Match)
    - Actual: The category filter works correctly when isolated. However, when combined with a price band filter, results become incorrect because the price band filter matches against the product's `priceBand` tag (e.g., "premium", "luxury") instead of the actual numeric price range. For example, applying "Cameras" + "Mid-Range ($300-$700)" yields "Showing 0 products" even though products like Samsung Bespoke Jet at $649 fall within that price band (they are tagged "premium" not "mid-range").

- [ ] FT-09: Filter listings by a price range band.
  - Action: Apply a price band filter (e.g., "$200–$500") to a product listing.
  - Expected: The listing shows only products whose price falls within that band.
  - Bug Report:
    - Issue: Incorrect Price Range Filtering
    - Actual: The price band filter does not filter by actual numeric price. It matches the product's `priceBand` categorical tag instead. Example: Mid-Range ($300-$700) alone shows "Showing 0 products" despite Samsung Bespoke Jet ($649) being within range; Premium ($700-$1200) returns Dell ($1099) and LG ($799) monitors tagged "premium" but excludes them when the actual price is checked. Conversely, products at $2499 tagged "premium" show up under the $700-$1200 filter, which is incorrect.

- [X] FT-10: Sort listings by overall score.
  - Action: Select "Sort by Overall Score" (ascending or descending) on a product listing.
  - Expected: Products reorder according to their overall rating in the chosen direction.

- [X] FT-11: Sort listings by date.
  - Action: Select "Sort by Date" (newest/oldest) on a product listing.
  - Expected: Products reorder by their publish/update date in the chosen direction.

- [X] FT-12: Search across products and articles.
  - Action: Enter a keyword (e.g., a product name or a category term) into the site search.
  - Expected: Search results include matching products AND matching review/comparison articles.

## Constraint

- [X] CS-01: Category filter excludes other categories.
  - Action: Apply "Cameras" filter, then inspect the visible results.
  - Expected: No products from "Monitors" or "Vacuum Cleaners" appear in the result set.

- [ ] CS-02: Price range filter excludes out-of-band prices.
  - Action: Apply a $200–$500 band; spot-check several visible product prices.
  - Expected: Every visible product's price is ≥ $200 and ≤ $500.
  - Bug Report:
    - Issue: Filter Does Not Honor Actual Price Bounds
    - Actual: Price filter matches the categorical `priceBand` tag, not the numeric price range. Mid-Range ($300-$700) shows 0 products even though Samsung Bespoke Jet ($649) falls within that band. Conversely, $2499 products (tagged "premium") show under the Premium ($700-$1200) filter. Prices of displayed products under any price filter do not consistently lie within the stated numeric range.

- [X] CS-03: Sort by overall score produces a non-decreasing/non-increasing order.
  - Action: Sort a listing by overall score and read the displayed scores in order.
  - Expected: Scores are in strictly monotonic order (asc or desc as selected); no score is out of place.

- [X] CS-04: Sort by date produces a non-decreasing/non-increasing order.
  - Action: Sort a listing by date and read the displayed dates in order.
  - Expected: Dates are in strictly monotonic order; no item is out of chronological place.

- [X] CS-05: Search returns at least one result type for a generic term.
  - Action: Search for a term that matches both a product and an article (e.g., a category name).
  - Expected: Both a Products section and an Articles (reviews/comparisons) section appear in the results.

## Interaction

- [ ] IX-01: Combining category + price band filters narrows results correctly.
  - Action: Select "Monitors" and a $300–$700 band simultaneously.
  - Expected: Listing shows only monitors priced within $300–$700; counts update to reflect the intersection.
  - Bug Report:
    - Issue: Price Filter Breaks Intersection Logic
    - Actual: With Monitors + Mid-Range ($300-$700), "Showing 0 products" is displayed. While there are genuinely no monitors in that range, the underlying issue is that the price filter operates on the categorical `priceBand` tag rather than numeric price, so intersection results are unreliable across the application. Additionally, when testing Monitors + Premium ($700-$1200), only 1 monitor (LG 27GP950-B, $799, tagged "premium") appears, while Dell Alienware AW3423DWF at $1099 (tagged "luxury") is excluded despite being within the $700-$1200 numeric range.

- [X] IX-02: Switching sort mode updates the listing immediately.
  - Action: Toggle from "Sort by Date" to "Sort by Overall Score" without reloading.
  - Expected: The product list visually reorders to match the newly selected sort, with no page refresh required.

## Content

- [X] CT-01: Each default product displays all required rating criteria.
  - Action: Open detail pages of default products from different categories.
  - Expected: Every product shows ratings for Design, Performance, and Value (or the documented equivalent criteria set).

- [X] CT-02: Default categories match the documented theme.
  - Action: Inspect the category filter/list of options on a product listing.
  - Expected: "Cameras", "Monitors", and "Vacuum Cleaners" are present among the available categories.
