All tests executed. Here is the complete checklist with results:

# Test Result

## Functionality
- [X] FT-01: Product detail page shows multi-criteria ratings
  - Action: Open any product detail page (e.g., a camera).
  - Expected: Page displays ratings for at least three criteria (e.g., Design, Performance, Value) with numeric scores, plus an overall score.
  - Verified: Canon R6 II page shows "Detailed Ratings" with Design 8.8, Performance 9.0, Value 8.2, Features 8.8, Build 9.0 plus Overall Score 8.8.
- [X] FT-02: Product detail page shows a verdict summary
  - Action: Open any product detail page.
  - Expected: A "Verdict" or "Summary" section is present containing a written conclusion paragraph for the product.
  - Verified: "Our Verdict" section with conclusion paragraph present on all 9 product pages.
- [X] FT-03: Product detail page lists all reviews and comparisons it appears in
  - Action: Open a product that appears in at least one review and one comparison article.
  - Expected: Page shows a links section listing every review article and every comparison article referencing this product; each link navigates to the correct article.
  - Verified: "Featured In" section lists all referencing articles (Canon R6 II → Best Mirrorless 2024 + Canon vs Sony; Sony A7 IV → 3 articles incl. its review; Dyson V15 → 2). All target slugs load correct article content.
- [X] FT-04: Long-form review article is viewable in full
  - Action: Open a review article from the reviews listing.
  - Expected: The full long-form review is displayed (title, product link, multiple body sections/paragraphs), not truncated to a teaser.
  - Verified: /article/sony-a7iv-review shows title "Sony A7 IV Review: The New Hybrid Standard", date Jan 20 2024, 6 H2 sections (Design and Build, Image Quality, Autofocus, Video, Verdict…), 8 paragraphs, link to /product/sony-a7iv.
- [ ] FT-05: Comparison article is viewable
  - Action: Open a comparison article.
  - Expected: Article displays its title and side-by-side comparison of two or more products with their specs and scores.
  - Bug Report:
    - Issue: Missing side-by-side comparison layout
    - Actual: /article/canon-vs-sony-2024 renders title + sequential prose sections (Autofocus, Image Quality, Video Features, Ergonomics, Lens Ecosystem, The Verdict) — 0 comparison tables on the page. Specs are never lined up; scores (8.7/8.8) only appear on generic "Products Mentioned" cards at the bottom, not in an aligned side-by-side spec/score comparison.
- [ ] FT-06: "Best of" ranked list is viewable
  - Action: Open a "Best of" list article for a category (e.g., cameras).
  - Expected: Article displays a ranked list of products (e.g., positions 1, 2, 3…) with each entry linking to its product detail page.
  - Bug Report:
    - Issue: Missing ranked-list presentation
    - Actual: /article/best-mirrorless-cameras-2024 and /article/best-cordless-vacuums-2024 contain prose award labels ("Our top pick…", "Best Value") and an unranked "Products Mentioned" card grid. No numeric positions (1, 2, 3, #1…) anywhere in either article; in the cameras article the mention-card order (Sony, Canon, Fujifilm) even contradicts the narrative ranking (Canon = top pick).
- [X] FT-07: Filter listings by category
  - Action: On the products or articles listing, select the category filter "Cameras" (or similar).
  - Expected: Only items belonging to the Cameras category are shown; items from other categories are hidden.
  - Verified: Checking "Cameras" shows exactly the 3 cameras; Monitors/Vacuums cards removed ("Showing 3 products").
- [ ] FT-08: Filter listings by price range band
  - Action: Apply a price band filter (e.g., "Under $500" or "$500–$1000").
  - Expected: Only products whose price falls within the selected band are listed.
  - Bug Report:
    - Issue: Incorrect price-band filtering (filter keys off misassigned tier tag, not actual price)
    - Actual: "Mid-Range ($300-$700)" returns "Showing 0 products" although Samsung Bespoke Jet costs $649 (in-band). "Premium ($700-$1200)" returns $2499 cameras (out of band). "Luxury ($1200+)" returns all 9 products including $649, $749 and $799 items (out of band).
- [X] FT-09: Sort listings by overall score
  - Action: Set sort control to "Overall Score" (or similar).
  - Expected: Products are ordered by overall score, highest first (or lowest first if the control says ascending).
  - Verified: Default "Highest Score" ordering: 9.0 → 8.9 → 8.8 → 8.8 → 8.8 → 8.7 → 8.7 → 8.6 → 8.6 (descending).
- [X] FT-10: Sort listings by date
  - Action: Set sort control to "Date" (or "Newest").
  - Expected: Products/articles are ordered by publish date, newest first (or as labeled).
  - Verified: "Newest First" option exists in the sort dropdown; its order (ASUS, Roborock, LG, Samsung, Canon, Dell, Dyson, Sony, Fujifilm) matches the "Latest Products / Recently added" ordering on the homepage.
- [X] FT-11: Search across products and articles
  - Action: Enter a search term matching a known product name in the search box and submit.
  - Expected: Results include the matching product detail page(s); enter a term matching an article title, results include that article.
  - Verified: "Dyson" + Enter → /search?q=Dyson, "Found 4 results": 2 products (Dyson V15, Samsung Bespoke Jet) + 2 articles. "Mirrorless" → returns "The Best Mirrorless Cameras of 2024" article.
- [X] FT-12: Comparison page lines up multiple products at once
  - Action: Open a comparison page containing at least 3 products.
  - Expected: All selected products appear as parallel columns/rows showing key specs, ratings per criterion, and a summary for each product, aligned so values are comparable across products.
  - Verified: Selected 3 products on /compare; "Ratings" table aligns Overall + 5 criteria across 3 columns (8.8/8.7/8.8 matching product pages), "Specifications" table aligns Price/Sensor/Video/AF/ISO/Weight/Battery, plus per-product Pros & Cons blocks.

## Constraint
- [X] CS-01: Category and price filters combine correctly
  - Action: Apply category "Cameras" together with a price band that excludes most cameras (e.g., "Under $200").
  - Expected: Only products matching BOTH filters are shown; empty result set is handled gracefully (e.g., "No products found" message, not an error).
  - Verified: Cameras + Budget ($0-$300) → "Showing 0 products" with friendly "No products match your filters." message and a "Clear all filters" action; no crash.
- [X] CS-02: Search with no matches shows empty state
  - Action: Search for a nonsense term (e.g., "zzzzqqq").
  - Expected: No results are shown and a clear "no results" message is displayed; app does not crash or show unrelated items.
  - Verified: /search?q=zzzzqqq shows "No results found for "zzzzqqq"" / "No Results Found – Try adjusting your search terms or browse our categories" with 0 product links.
- [X] CS-03: Filters and sort persist across the listing session
  - Action: Apply a category filter, then change the sort order.
  - Expected: The category filter remains applied after changing sort; results reflect both filter and new sort.
  - Verified: With "Newest First" selected, checking "Cameras" still yields exactly the 3 cameras and the sort control still reads "Newest First".
- [X] CS-04: Score display matches rating scale
  - Action: Inspect criteria and overall scores on multiple product detail pages.
  - Expected: All scores fall within a consistent scale (e.g., 0–10 or 0–100) and no score is blank, negative, or out of range.
  - Verified: All 9 products: overall 8.6–9.0, sub-scores 8.0–9.4 — consistent 0–10 scale, none blank/negative/out of range.

## Interaction
- [X] IX-01: Product links from listings navigate to detail pages
  - Action: Click a product card/row in a listing or ranked list.
  - Expected: Browser navigates to that product's detail page showing its name, ratings, and verdict.
  - Verified: Clicking the first product card navigated to /product/dell-aw3423dwf with H1 "Dell Alienware AW3423DWF", Detailed Ratings and Our Verdict present.
- [X] IX-02: Article links from product page navigate correctly
  - Action: On a product detail page, click one of the linked review/comparison articles.
  - Expected: Browser navigates to that article page without error, and the article references this product.
  - Verified: Clicking a "Featured In" link navigated to /article/best-mirrorless-cameras-2024, which mentions "Canon EOS R6 Mark II".
- [X] IX-03: Filters/sort apply immediately without page errors
  - Action: Change a filter or sort control on a listing.
  - Expected: The visible list updates to reflect the new filter/sort without a console error or blank page.
  - Verified: All filter/sort changes updated the list instantly; console contains only React Router future-flag warnings (the single 404 console error came from my direct navigation to the non-existent /articles route, not from any filter/sort interaction).
- [X] IX-04: Comparison page is reachable via a comparison control
  - Action: From an article or listing, open the comparison view (e.g., "Compare" link/button).
  - Expected: Comparison page opens showing the products lined up side-by-side.
  - Verified: Header "Compare" link → /compare; product page "Add to Comparison" → /compare?products=canon-r6ii with the Canon pre-selected in the comparison grid.

## Content
- [X] CT-01: All listed products match their category
  - Action: Open the Cameras category listing (and one other category, e.g., Monitors).
  - Expected: Every displayed product is actually a camera (or monitor); no off-category items appear.
  - Verified: Cameras filter → Canon R6 II, Fujifilm X-H2S, Sony A7 IV only; /products?category=monitors → Dell AW3423DWF, ASUS PG32UCDM, LG 27GP950-B only.
- [ ] CT-02: Product pages contain product imagery
  - Action: Open several product detail pages.
  - Expected: Each page shows a product image relevant to that product (no broken images, no placeholder icons for unrelated products).
  - Bug Report:
    - Issue: Broken image
    - Actual: On /product/roborock-s8pro the main product image (photo-1603618090554-0df40bb5e4c7) fails to load — naturalWidth=0 with complete=true even after networkidle + 1.5s wait. All other 8 product pages load their images correctly (naturalWidth 600/1200).
- [X] CT-03: Comparison articles state the products being compared
  - Action: Open comparison articles.
  - Expected: Each comparison's title/content explicitly names all products compared, matching the products shown in its comparison table.
  - Verified: "Canon R6 II vs Sony A7 IV: The Ultimate Showdown" title and body explicitly name Canon EOS R6 Mark II and Sony A7 IV, matching the two products in its "Products Mentioned" section.
- [X] CT-04: Reviews and "best of" lists show publish dates and scores
  - Action: Inspect review articles and ranked lists.
  - Expected: Each shows a publish date and score/ranking values consistent with the product pages they reference (e.g., a product ranked #1 has the list's top score).
  - Verified: Review (Jan 20 2024, score 8.7 = product page 8.7), comparison (Feb 28 2024, cards show 8.7/8.8 matching product pages), best-of lists (Mar 15/Mar 8 2024; mention cards show 8.9/8.6/8.7 matching product pages, and the top pick Dyson carries the highest score 8.9). Note: lists lack explicit numeric rank positions — that deficiency is reported under FT-06.

**Summary: 20 PASS / 4 FAIL** — the failures are: price-band filter misaligned with actual prices (FT-08), no side-by-side layout in comparison articles (FT-05), no numeric ranked positions in "best of" articles (FT-06), and one broken product image on the Roborock S8 Pro Ultra page (CT-02).