# Test Result

## Functionality
- [X] FT-01: A long-form review article opens and shows complete review content.
  - Action: From the home/listing page, open a full product review article.
  - Expected: Article page shows title, long-form body text, and the product being reviewed.
- [ ] FT-02: A ranked "best of" list opens for a category.
  - Action: Open a "best of" list (e.g., "Best Cameras").
  - Expected: Page shows multiple products of that category, each with a visible rank (1, 2, 3…) in ranked order.
  - Bug Report:
    - Issue: Missing Rank Indicators on Ranked "Best Of" List
    - Actual: On /article/best-mirrorless-cameras-2024 the "Products Mentioned" section lists Sony A7 IV (8.7), Canon EOS R6 Mark II (8.8), Fujifilm X-H2S (8.8) with no visible rank numbers (1, 2, 3…) anywhere on the page (DOM scan for rank/badge/position elements returned none), and the products are not in ranked order (Sony 8.7 is listed first although the body names Canon the "top pick" and Sony "a close second").
- [X] FT-03: Product detail page shows multi-criteria ratings.
  - Action: Open any product's detail page.
  - Expected: Page shows the product name, an overall score, and per-criterion ratings including "Design", "Performance", and "Value".
- [X] FT-04: Product detail page shows a verdict summary.
  - Action: On the product detail page, scroll to the verdict section.
  - Expected: A "Verdict" (summary) block with a short concluding text is displayed.
- [X] FT-05: Product page links to every review and comparison it appears in.
  - Action: On a product detail page that appears in articles, click each listed review/comparison link.
  - Expected: Section lists all such articles by name; each link opens the correct article containing that product.
- [X] FT-06: Listing can be filtered by category.
  - Action: On the product listing, select category "Cameras".
  - Expected: Listing shows only camera products; at least one product is shown.
- [ ] FT-07: Listing can be filtered by price range band.
  - Action: Select a price range band (e.g., the band containing a known default product).
  - Expected: Listing shows only products whose price falls inside the selected band.
  - Bug Report:
    - Issue: Price Range Band Filter Matches Tier Tag Instead of Price (Incorrect Filter Results)
    - Actual: On /products, selecting the band "Premium ($700-$1200)" shows "Showing 5 products": Canon EOS R6 Mark II $2499, Fujifilm X-H2S $2499, Sony A7 IV $2499, Samsung Bespoke Jet $649 (all priced outside the $700–$1200 band) plus LG 27GP950-B $799, while Dell Alienware AW3423DWF $1099 and Dyson V15 Detect $749 — both priced inside the band — are excluded. The filter matches the cosmetic "premium"/"luxury" badge shown on product cards, not the stated dollar range.
- [X] FT-08: Listing can be sorted by overall score.
  - Action: Choose sort "Overall Score" (highest first).
  - Expected: Products are ordered by overall score descending (first product's score ≥ second's ≥ …).
- [X] FT-09: Listing can be sorted by date.
  - Action: Choose sort "Date" (newest first).
  - Expected: Content is ordered newest-first by publish date.
- [X] FT-10: Search returns both products and articles.
  - Action: Type a term that appears in a product name and in an article title into the search field and submit.
  - Expected: Results page lists matching product(s) and matching article(s), each labeled by type.
- [ ] FT-11: Comparison page lines up several products side by side.
  - Action: Open a comparison article covering 2+ products.
  - Expected: Page shows a side-by-side layout with, for every compared product: key specs, criterion ratings, and a short summary.
  - Bug Report:
    - Issue: Comparison Article Lacks Side-by-Side Spec/Rating Lineup (Incomplete Comparison Layout)
    - Actual: Opening the comparison article /article/canon-vs-sony-2024 (2 products) shows only single-column narrative prose ("Autofocus", "Image Quality", "Video Features"…) and stacked "Products Mentioned" cards carrying just an overall score (8.8 / 8.7) and a one-line description — no side-by-side layout with key specs and per-criterion ratings for each compared product. The other comparison article (/article/dyson-v15-vs-samsung-jet) uses the same template. (The separate /compare tool page shows side-by-side spec and criterion-rating tables, but also omits a short summary per product.)

## Constraint
- [ ] CS-01: Category and price filters combine without letting non-matching products through.
  - Action: Apply category "Monitors" and a price band simultaneously.
  - Expected: Every remaining product is a monitor AND priced inside the band; nothing else is listed.
  - Bug Report:
    - Issue: Combined Filters Let Non-Matching Product Through (price band not enforced by actual price)
    - Actual: With category "Monitors" and price band "Luxury ($1200+)" applied simultaneously, the listing shows 2 products: "ASUS ROG Swift PG32UCDM $1299" (compliant) and "Dell Alienware AW3423DWF $1099" — the Dell is priced $1099, below the $1200+ band, so a product whose price falls outside the selected band is listed.
- [X] CS-02: A search query matching nothing yields an empty result state, never unrelated results or an error.
  - Action: Search for a nonsensical string (e.g., "zzzqqqxyz").
  - Expected: Page shows a "no results" empty state (or zero result count) and does not crash or list unrelated items.
- [X] CS-03: An empty search query cannot be submitted.
  - Action: Clear the search field and press Enter / click the search button.
  - Expected: No empty results page is shown; submission is blocked or a message prompts for a query.
- [X] CS-04: Sort options are mutually exclusive.
  - Action: Apply sort "Date", then apply sort "Overall Score".
  - Expected: Listing is ordered only by overall score; the previous date ordering is fully replaced and only one sort is shown as active.
- [X] CS-05: Rating values respect a single valid scale across the site.
  - Action: Inspect criterion and overall ratings on several product detail pages.
  - Expected: Every rating is a numeric value within the site's rating scale (e.g., 0–5), and each product uses the same criteria set (Design, Performance, Value).

## Interaction
- [X] IX-01: Applying filters updates the listing in place with a visible selected state.
  - Action: Click a category filter, then a price band.
  - Expected: Listing updates without an error page; the chosen filter(s) display a selected/active state.
- [X] IX-02: Changing the sort control immediately re-orders the listing and marks the chosen sort as active.
  - Action: Switch between "Overall Score" and "Date" sort options.
  - Expected: The visible order changes right away each time, and the currently applied sort option is highlighted/selected.

## Content
- [X] CT-01: The named categories all have default content.
  - Action: Browse listings/lists for "Cameras", "Monitors", and "Vacuum Cleaners".
  - Expected: Each of the three categories shows at least one product and at least one review or "best of" list relevant to it.
- [X] CT-02: Product media and text are relevant to the product shown.
  - Action: Open a product detail page and inspect its image(s) and description.
  - Expected: The image depicts the named product (or its category) and the description text refers to that product, with no placeholder or mismatched content.
