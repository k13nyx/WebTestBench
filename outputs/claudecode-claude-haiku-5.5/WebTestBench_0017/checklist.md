# Test Checklist

## Functionality
- [ ] FT-01: Category browsing shows only products from the chosen category.
  - Action: Click "Cameras", then "Monitors", then "Vacuum Cleaners" in the category navigation.
  - Expected: Each page lists only products of that category, and the active category is highlighted.
- [ ] FT-02: Price band filter narrows the listing to the selected band.
  - Action: Open a category page and select one price band in the price filter.
  - Expected: Every listed product's price falls within the selected band, and the product count updates.
- [ ] FT-03: Sort by overall score orders products from highest to lowest score.
  - Action: Open a category page and select "Sort by: Overall Score".
  - Expected: Products are ordered by overall score, highest first.
- [ ] FT-04: Sort by date orders products newest first.
  - Action: Select "Sort by: Date".
  - Expected: Products are ordered by publication date, newest first.
- [ ] FT-05: Search returns matching products and articles.
  - Action: Type a known product name, then a keyword from a known article title, into the search box and press Enter.
  - Expected: Results include the matching product and article, each labeled with its type.
- [ ] FT-06: Product detail page shows the complete product profile.
  - Action: Click any product name in a listing.
  - Expected: The page shows the product name, overall score, ratings for Design, Performance, and Value, a verdict summary, and sections titled "Reviews" and "Comparisons."
- [ ] FT-07: Links on a product page open the related articles.
  - Action: On a product detail page, click the first article under "Reviews," then go back and click the first item under "Comparisons."
  - Expected: Each link opens the correct article page, and that article's title matches the link text.
- [ ] FT-08: Comparison page shows several products side by side.
  - Action: Open any comparison article from the Comparisons section or the search results.
  - Expected: The page shows a table with one column per product, rows for key specs, ratings, and summaries, and all of them are aligned by row.
- [ ] FT-09: Best-of list shows products in ranked order.
  - Action: Open any "best of" list article.
  - Expected: Products are numbered sequentially from 1, each with its rank, score, and a short summary.
- [ ] FT-10: Publish form opens for creating a new article.
  - Action: Click "Publish" or "New Article" in the site navigation. Do not submit.
  - Expected: A form opens with fields for title, article type (Review, Comparison, or Best-of), category, linked products, and body content.

## Constraint
- [ ] CS-01: Search with no matches shows a "No results" message and no unrelated items.
  - Action: Type "zzzqqx" in the search box and press Enter.
  - Expected: The message "No results found" appears, and no product or article cards are displayed.
- [ ] CS-02: All ratings and overall scores stay within the stated scale.
  - Action: Check the ratings and overall scores on five product detail pages and the scores shown on a best-of list.
  - Expected: Every value is between 0 and the scale maximum shown on the page (for example, 10), with no negative or out-of-range values.
- [ ] CS-03: Each product appears in exactly one price band.
  - Action: Apply each price band filter in turn in one category and count the products in each result.
  - Expected: The counts add up to the total number of products in that category, and no product appears in two bands.
- [ ] CS-04: Visitors cannot see publishing or editing controls.
  - Action: Browse the site as an unauthenticated visitor and check the navigation and product and article pages.
  - Expected: No "Publish," "New Article," "Edit," or "Delete" controls are visible.

## Interaction
- [ ] IX-01: Changing the sort option updates the listing in place.
  - Action: On a category page, open the sort menu and select a different option.
  - Expected: The product order changes without a full page reload, and the sort control displays the newly selected option.
- [ ] IX-02: Active filters appear as removable chips.
  - Action: Select a price band, then click the "x" on the resulting filter chip.
  - Expected: The chip appears when the filter is applied, and clicking "x" removes it and restores the full listing.
- [ ] IX-03: Returning from a product page keeps the listing's filters and sort.
  - Action: On a category page, apply a price band and a sort option, click a product, then press the browser Back button.
  - Expected: The listing reappears with the same price band and sort option still applied.

## Content
- [ ] CT-01: Product images on each category page match that category.
  - Action: Open the Cameras, Monitors, and Vacuum Cleaners pages and look at the product images.
  - Expected: Each image shows a product from the page's category (for example, a camera on the Cameras page), with no unrelated or broken images.
- [ ] CT-02: Product detail pages contain complete rating and verdict content.
  - Action: Open five product detail pages.
  - Expected: Each page shows numeric ratings for Design, Performance, and Value, and a verdict summary with real text (not blank or placeholder).
- [ ] CT-03: Pages contain no placeholder text, and spec values use consistent units.
  - Action: Review the home page, a product page, a comparison page, and a best-of list.
  - Expected: No text such as "Lorem ipsum," "TBD," or "placeholder" appears, and every spec row on a comparison page uses one consistent unit (for example, all weights in "g" or all in "kg").