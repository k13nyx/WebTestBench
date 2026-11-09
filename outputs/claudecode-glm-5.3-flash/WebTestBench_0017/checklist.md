# Test Checklist

## Functionality
- [ ] FT-01: Product detail page shows multi-criteria ratings
  - Action: Open any product detail page (e.g., a camera).
  - Expected: Page displays ratings for at least three criteria (e.g., Design, Performance, Value) with numeric scores, plus an overall score.
- [ ] FT-02: Product detail page shows a verdict summary
  - Action: Open any product detail page.
  - Expected: A "Verdict" or "Summary" section is present containing a written conclusion paragraph for the product.
- [ ] FT-03: Product detail page lists all reviews and comparisons it appears in
  - Action: Open a product that appears in at least one review and one comparison article.
  - Expected: Page shows a links section listing every review article and every comparison article referencing this product; each link navigates to the correct article.
- [ ] FT-04: Long-form review article is viewable in full
  - Action: Open a review article from the reviews listing.
  - Expected: The full long-form review is displayed (title, product link, multiple body sections/paragraphs), not truncated to a teaser.
- [ ] FT-05: Comparison article is viewable
  - Action: Open a comparison article.
  - Expected: Article displays its title and side-by-side comparison of two or more products with their specs and scores.
- [ ] FT-06: "Best of" ranked list is viewable
  - Action: Open a "Best of" list article for a category (e.g., cameras).
  - Expected: Article displays a ranked list of products (e.g., positions 1, 2, 3…) with each entry linking to its product detail page.
- [ ] FT-07: Filter listings by category
  - Action: On the products or articles listing, select the category filter "Cameras" (or similar).
  - Expected: Only items belonging to the Cameras category are shown; items from other categories are hidden.
- [ ] FT-08: Filter listings by price range band
  - Action: Apply a price band filter (e.g., "Under $500" or "$500–$1000").
  - Expected: Only products whose price falls within the selected band are listed.
- [ ] FT-09: Sort listings by overall score
  - Action: Set sort control to "Overall Score" (or similar) on a product listing.
  - Expected: Products are ordered by overall score, highest first (or lowest first if the control says ascending).
- [ ] FT-10: Sort listings by date
  - Action: Set sort control to "Date" (or "Newest").
  - Expected: Products/articles are ordered by publish date, newest first (or as labeled).
- [ ] FT-11: Search across products and articles
  - Action: Enter a search term matching a known product name in the search box and submit.
  - Expected: Results include the matching product detail page(s); enter a term matching an article title, results include that article.
- [ ] FT-12: Comparison page lines up multiple products at once
  - Action: Open a comparison page containing at least 3 products.
  - Expected: All selected products appear as parallel columns/rows showing key specs, ratings per criterion, and a summary for each product, aligned so values are comparable across products.

## Constraint
- [ ] CS-01: Category and price filters combine correctly
  - Action: Apply category "Cameras" together with a price band that excludes most cameras (e.g., "Under $200").
  - Expected: Only products matching BOTH filters are shown; empty result set is handled gracefully (e.g., "No products found" message, not an error).
- [ ] CS-02: Search with no matches shows empty state
  - Action: Search for a nonsense term (e.g., "zzzzqqq").
  - Expected: No results are shown and a clear "no results" message is displayed; app does not crash or show unrelated items.
- [ ] CS-03: Filters and sort persist across the listing session
  - Action: Apply a category filter, then change the sort order.
  - Expected: The category filter remains applied after changing sort; results reflect both filter and new sort.
- [ ] CS-04: Score display matches rating scale
  - Action: Inspect criteria and overall scores on multiple product detail pages.
  - Expected: All scores fall within a consistent scale (e.g., 0–10 or 0–100) and no score is blank, negative, or out of range.

## Interaction
- [ ] IX-01: Product links from listings navigate to detail pages
  - Action: Click a product card/row in a listing or ranked list.
  - Expected: Browser navigates to that product's detail page showing its name, ratings, and verdict.
- [ ] IX-02: Article links from product page navigate correctly
  - Action: On a product detail page, click one of the linked review/comparison articles.
  - Expected: Browser navigates to that article page without error, and the article references this product.
- [ ] IX-03: Filters/sort apply immediately without page errors
  - Action: Change a filter or sort control on a listing.
  - Expected: The visible list updates to reflect the new filter/sort without a console error or blank page.
- [ ] IX-04: Comparison page is reachable via a comparison control
  - Action: From an article or listing, open the comparison view (e.g., "Compare" link/button).
  - Expected: Comparison page opens showing the products lined up side-by-side.

## Content
- [ ] CT-01: All listed products match their category
  - Action: Open the Cameras category listing (and one other category, e.g., Monitors).
  - Expected: Every displayed product is actually a camera (or monitor); no off-category items appear.
- [ ] CT-02: Product pages contain product imagery
  - Action: Open several product detail pages.
  - Expected: Each page shows a product image relevant to that product (no broken images, no placeholder icons for unrelated products).
- [ ] CT-03: Comparison articles state the products being compared
  - Action: Open comparison articles.
  - Expected: Each comparison's title/content explicitly names all products compared, matching the products shown in its comparison table.
- [ ] CT-04: Reviews and "best of" lists show publish dates and scores
  - Action: Inspect review articles and ranked lists.
  - Expected: Each shows a publish date and score/ranking values consistent with the product pages they reference (e.g., a product ranked #1 has the list's top score).