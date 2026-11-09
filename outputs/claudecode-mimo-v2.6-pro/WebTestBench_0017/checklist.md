The working directory contains no app source, so the checklist is derived directly from the user instruction (with names taken from its terminology: category, price range band, overall score, verdict, comparison page, etc.).

# Test Checklist

## Functionality
- [ ] FT-01: A long-form review article opens and shows complete review content.
  - Action: From the home/listing page, open a full product review article.
  - Expected: Article page shows title, long-form body text, and the product being reviewed.
- [ ] FT-02: A ranked "best of" list opens for a category.
  - Action: Open a "best of" list (e.g., "Best Cameras").
  - Expected: Page shows multiple products of that category, each with a visible rank (1, 2, 3…) in ranked order.
- [ ] FT-03: Product detail page shows multi-criteria ratings.
  - Action: Open any product's detail page.
  - Expected: Page shows the product name, an overall score, and per-criterion ratings including "Design", "Performance", and "Value".
- [ ] FT-04: Product detail page shows a verdict summary.
  - Action: On the product detail page, scroll to the verdict section.
  - Expected: A "Verdict" (summary) block with a short concluding text is displayed.
- [ ] FT-05: Product page links to every review and comparison it appears in.
  - Action: On a product detail page that appears in articles, click each listed review/comparison link.
  - Expected: Section lists all such articles by name; each link opens the correct article containing that product.
- [ ] FT-06: Listing can be filtered by category.
  - Action: On the product listing, select category "Cameras".
  - Expected: Listing shows only camera products; at least one product is shown.
- [ ] FT-07: Listing can be filtered by price range band.
  - Action: Select a price range band (e.g., the band containing a known default product).
  - Expected: Listing shows only products whose price falls inside the selected band.
- [ ] FT-08: Listing can be sorted by overall score.
  - Action: Choose sort "Overall Score" (highest first).
  - Expected: Products are ordered by overall score descending (first product's score ≥ second's ≥ …).
- [ ] FT-09: Listing can be sorted by date.
  - Action: Choose sort "Date" (newest first).
  - Expected: Content is ordered newest-first by publish date.
- [ ] FT-10: Search returns both products and articles.
  - Action: Type a term that appears in a product name and in an article title into the search field and submit.
  - Expected: Results page lists matching product(s) and matching article(s), each labeled by type.
- [ ] FT-11: Comparison page lines up several products side by side.
  - Action: Open a comparison article covering 2+ products.
  - Expected: Page shows a side-by-side layout with, for every compared product: key specs, criterion ratings, and a short summary.

## Constraint
- [ ] CS-01: Category and price filters combine without letting non-matching products through.
  - Action: Apply category "Monitors" and a price band simultaneously.
  - Expected: Every remaining product is a monitor AND priced inside the band; nothing else is listed.
- [ ] CS-02: A search query matching nothing yields an empty result state, never unrelated results or an error.
  - Action: Search for a nonsensical string (e.g., "zzzqqqxyz").
  - Expected: Page shows a "no results" empty state (or zero result count) and does not crash or list unrelated items.
- [ ] CS-03: An empty search query cannot be submitted.
  - Action: Clear the search field and press Enter / click the search button.
  - Expected: No empty results page is shown; submission is blocked or a message prompts for a query.
- [ ] CS-04: Sort options are mutually exclusive.
  - Action: Apply sort "Date", then apply sort "Overall Score".
  - Expected: Listing is ordered only by overall score; the previous date ordering is fully replaced and only one sort is shown as active.
- [ ] CS-05: Rating values respect a single valid scale across the site.
  - Action: Inspect criterion and overall ratings on several product detail pages.
  - Expected: Every rating is a numeric value within the site's rating scale (e.g., 0–5), and each product uses the same criteria set (Design, Performance, Value).

## Interaction
- [ ] IX-01: Applying filters updates the listing in place with a visible selected state.
  - Action: Click a category filter, then a price band.
  - Expected: Listing updates without an error page; the chosen filter(s) display a selected/active state.
- [ ] IX-02: Changing the sort control immediately re-orders the listing and marks the chosen sort as active.
  - Action: Switch between "Overall Score" and "Date" sort options.
  - Expected: The visible order changes right away each time, and the currently applied sort option is highlighted/selected.

## Content
- [ ] CT-01: The named categories all have default content.
  - Action: Browse listings/lists for "Cameras", "Monitors", and "Vacuum Cleaners".
  - Expected: Each of the three categories shows at least one product and at least one review or "best of" list relevant to it.
- [ ] CT-02: Product media and text are relevant to the product shown.
  - Action: Open a product detail page and inspect its image(s) and description.
  - Expected: The image depicts the named product (or its category) and the description text refers to that product, with no placeholder or mismatched content.