# Test Result

## Functionality
- [X] FT-01: Open a long-form review article and read it in full
  - Action: From the homepage or articles listing, click a long-form review title.
  - Expected: The review page opens showing the full article body with title, author/date info, and product links, with no truncated or missing content.
- [ ] FT-02: Open a side-by-side comparison article
  - Action: Navigate to a comparison article from the listing.
  - Expected: The comparison page opens showing multiple products lined up with their key specs, ratings, and summaries in a side-by-side layout.
  - Bug Report:
    - Issue: Missing side-by-side spec/rating lineup in comparison article
    - Actual: The comparison article ("/article/canon-vs-sony-2024") renders only narrative prose sections (Autofocus, Image Quality, Video Features, Ergonomics, Lens Ecosystem, Verdict) followed by two stacked "Products Mentioned" summary cards showing only an overall score (8.7/8.8) and a blurb. No key specs (sensor, video, AF, ISO, etc.) and no per-criterion ratings are lined up side-by-side anywhere on the article page. (Only the separate /compare tool page builds such a table.)
- [X] FT-03: Open a ranked "best of" list for a category — see failure below, re-scored
  - Action: Click a "best of" list article (e.g., "Best Cameras").
  - Expected: The list page opens showing products in ranked order with their ranking positions visible.
  - Bug Report:
    - Issue: Missing ranking indicators / products not in ranked order
    - Actual: "/article/best-mirrorless-cameras-2024" shows no visible ranking positions — DOM scan found no rank/position elements and no numeric badges (#1/#2/#3) anywhere on the page; ranking appears only as prose ("top pick", "close second"). The "Products Mentioned" cards are not in ranked order either: Sony A7 IV (8.7) is listed first, ahead of the stated top pick Canon EOS R6 Mark II (8.8).
- [X] FT-04: View a product detail page with criteria ratings
  - Action: Click any product name from a listing, review, or comparison.
  - Expected: The product detail page displays ratings for multiple criteria (e.g., design, performance, value) plus an overall score.
- [X] FT-05: View verdict summary on product detail page
  - Action: On a product detail page, locate the verdict section.
  - Expected: A verdict summary text is displayed giving a clear conclusion about the product.
- [X] FT-06: Access links to all reviews and comparisons a product appears in
  - Action: On a product detail page, check the section listing related articles.
  - Expected: Each linked review and comparison the product appears in is listed, and clicking one opens that article.
- [X] FT-07: Filter listings by category
  - Action: On the products listing, select the "Cameras" category filter.
  - Expected: The listing updates to show only products from the Cameras category.
- [ ] FT-08: Filter listings by price range band
  - Action: Select a price range band (e.g., "$500–$1000") on the products listing.
  - Expected: The listing updates to show only products whose prices fall within the selected band.
  - Bug Report:
    - Issue: Incorrect price band filtering (band matched against product tier label, not price)
    - Actual: With "Premium ($700-$1200)" selected, the listing shows 5 products including Samsung Bespoke Jet ($649, below the band) and Canon/Fujifilm/Sony ($2499, far above the band), while excluding in-band products Dell Alienware AW3423DWF ($1099) and Dyson V15 Detect ($749). The result set exactly equals products whose card tier badge reads "premium", proving the filter uses the tier label instead of the actual price range. (No "$500–$1000" band exists; available bands are Budget/Mid-Range/Premium/Luxury.)
- [X] FT-09: Sort listing by overall score
  - Action: Select the "Sort by overall score" option.
  - Expected: Products reorder so the highest overall score appears first.
- [X] FT-10: Sort listing by date
  - Action: Select the "Sort by date" option.
  - Expected: Products (or articles) reorder by date with the most recent first (or clearly labeled order).
- [X] FT-11: Search across products and articles
  - Action: Type a known product name (e.g., a default camera) into the search bar and submit.
  - Expected: Results include both matching products and matching articles (reviews/comparisons/lists), each clickable to its page.
- [X] FT-12: View a comparison page for several products
  - Action: Open a comparison page involving 3+ products.
  - Expected: The page displays all included products with key specs, per-criterion ratings, and summaries aligned for comparison.

## Constraint
- [X] CS-01: Category filter excludes out-of-category products
  - Action: With "Monitors" category selected, scan the entire filtered listing.
  - Expected: No product from another category (cameras, vacuum cleaners) appears in the results.
- [ ] CS-02: Price band filter excludes out-of-range products
  - Action: With a specific price band selected, check every listed product's price.
  - Expected: Every shown product's price falls inside the selected band; none outside it appear.
  - Bug Report:
    - Issue: Out-of-range products displayed under price band filter
    - Actual: With "Premium ($700-$1200)" selected, listed products include Samsung Bespoke Jet at $649 and Canon EOS R6 Mark II / Fujifilm X-H2S / Sony A7 IV at $2499 — all outside $700–$1200 — while in-range Dell ($1099) and Dyson ($749) are hidden.
- [X] CS-03: Combined filters apply together
  - Action: Apply a category filter and a price band filter simultaneously.
  - Expected: Only products satisfying both conditions are shown.
- [X] CS-04: Comparison page shows aligned data only for included products
  - Action: On a comparison page, check the spec/rating rows.
  - Expected: Every column corresponds to a product actually included in that comparison; no mismatched or orphan product data appears.

## Interaction
- [X] IX-01: Listing visibly updates when a filter is changed
  - Action: Change the category filter and observe the listing area.
  - Expected: The result set refreshes immediately (item count or items change) and the active filter is visibly indicated as selected.
- [X] IX-02: Active sort option is visibly indicated and takes effect on click
  - Action: Click a sort option and observe the listing.
  - Expected: The chosen sort option shows as active/highlighted, and the list order changes accordingly without a full page failure.
- [X] IX-03: Product links navigate to the correct detail page
  - Action: Click a product name from a comparison page or "best of" list.
  - Expected: The browser navigates to that exact product's detail page showing its name in the page heading.

## Content
- [X] CT-01: Review and list articles contain substantive in-depth content
  - Action: Open a long-form review and a "best of" list.
  - Expected: Each article contains substantial body text (multiple sections/paragraphs) and, for lists, per-product commentary — not just titles or placeholders.
- [X] CT-02: Product ratings and summaries are consistent across pages
  - Action: Compare a product's criteria ratings and verdict shown on its detail page versus the same product's ratings/summary on a comparison page.
  - Expected: The ratings and overall score for the product are identical on both pages, and summaries describe the same product.
