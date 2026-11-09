# Test Result

## Functionality

- [X] FT-01: Product listings can be browsed by supported categories.
  - Action: Open the product listing and select each available category, including Cameras, Monitors, and Vacuum Cleaners.
  - Expected: The listing displays products for the selected category.

- [ ] FT-02: Product listings can be filtered by price range bands.
  - Action: Select each available option in the “Price range” filter.
  - Expected: The listing updates to show products within the selected price band.
  - Bug Report:
    - Issue: Incorrect price-range filtering
    - Actual: The Budget and Mid-Range filters return zero products, while the Premium filter includes products priced at $2499 and the Luxury filter includes products priced at $1099 and $749, which are outside their displayed bands.

- [ ] FT-03: Product listings can be sorted by overall score and date.
  - Action: Select “Overall score” and then “Date” from the sort control.
  - Expected: Products reorder according to the selected sort option.
  - Bug Report:
    - Issue: Missing requested sort options
    - Actual: The sort control provides “Highest Score” and “Newest First” instead of “Overall score” and “Date.”

- [X] FT-04: Visitors can search across products and articles.
  - Action: Enter a known product name and a known article title or keyword in the search field and submit each search.
  - Expected: Matching products and articles are returned in the search results.

- [X] FT-05: Each product has an accessible detail page.
  - Action: Select a product from a listing or search result.
  - Expected: The product’s detail page opens and identifies the selected product.

- [X] FT-06: Product detail pages display ratings across multiple criteria.
  - Action: Open product detail pages for products in the default data.
  - Expected: Each page displays ratings for criteria including Design, Performance, and Value.

- [X] FT-07: Product detail pages display a verdict summary.
  - Action: Open a product detail page and locate its verdict section.
  - Expected: A clear verdict summary is displayed for the product.

- [X] FT-08: Product detail pages link to all related reviews and comparisons.
  - Action: On a product with existing editorial coverage, open every link in its reviews and comparisons sections.
  - Expected: Each link opens the corresponding review or comparison article containing that product.

- [X] FT-09: Published long-form review articles are available.
  - Action: Open a review article from a product page, listing, or search result.
  - Expected: The article presents an in-depth review of the selected product.

- [X] FT-10: Published side-by-side comparison articles are available.
  - Action: Open a comparison article from a product page, listing, or search result.
  - Expected: The article compares multiple products side by side.

- [ ] FT-11: Published ranked “best of” lists are available.
  - Action: Open a “best of” article for a supported category.
  - Expected: The article presents multiple products in an explicit ranked order.
  - Bug Report:
    - Issue: Best-of article lacks explicit ranking
    - Actual: The article presents “Products Mentioned” cards and prose such as “top pick” and “close second,” but the products do not have visible numbered ranks or ordered positions.

- [X] FT-12: Comparison pages display key specifications, ratings, and summaries for several products.
  - Action: Open a comparison page and review each product column and comparison row.
  - Expected: At least two products are shown with aligned key specs, ratings, and summary information.

## Constraint

- [X] CS-01: Category filtering excludes products from other categories.
  - Action: Apply the Cameras, Monitors, and Vacuum Cleaners category filters one at a time.
  - Expected: Every displayed product belongs to the selected category; no unrelated-category product appears.

- [ ] CS-02: Price filtering excludes products outside the selected price band.
  - Action: Apply a price range band and inspect the displayed product prices.
  - Expected: Every displayed product price falls within the selected band.
  - Bug Report:
    - Issue: Price-band constraints are not enforced
    - Actual: The Premium ($700-$1200) filter displays $2499 cameras, and the Luxury ($1200+) filter displays products priced at $1099 and $749.

- [X] CS-03: Overall-score sorting produces the correct score order.
  - Action: Sort a product listing by “Overall score” and compare the visible scores from top to bottom.
  - Expected: Products appear in the requested ascending or descending score order.

- [ ] CS-04: Date sorting produces the correct chronological order.
  - Action: Sort an article or product listing by “Date” and compare the visible publication or update dates.
  - Expected: Items appear in the requested newest-first or oldest-first order.
  - Bug Report:
    - Issue: Dates are not visible in the product listing
    - Actual: The listing can be changed to “Newest First,” but product cards do not display publication or update dates, so the chronological order cannot be verified from the visible results.

## Interaction

- [ ] IX-01: Applying a category or price filter visibly updates the listing state.
  - Action: Apply a category or price filter and observe the filter control and results area.
  - Expected: The selected filter is visibly indicated and the results refresh without showing stale unfiltered content.
  - Bug Report:
    - Issue: Price filter produces incorrect result state
    - Actual: Category filters visibly update correctly, but price filters produce inconsistent states: Budget and Mid-Range show zero products, while Premium and Luxury include products outside the selected ranges.

- [ ] IX-02: Changing the sort option visibly refreshes the displayed order.
  - Action: Change the sort control from “Overall score” to “Date” while viewing a populated listing.
  - Expected: The selected sort option is shown and the listing visibly reorders.
  - Bug Report:
    - Issue: Requested sort labels are unavailable
    - Actual: The control does not contain “Overall score” or “Date”; it contains “Highest Score” and “Newest First.” The listing reorders only through those alternate labels.

- [X] IX-03: Search submission clearly presents search results.
  - Action: Submit a search for a known product or article.
  - Expected: A results view appears with the submitted query retained or clearly represented and matching results displayed.

- [X] IX-04: Selecting a product or article result opens the intended content.
  - Action: Click a product result, review result, comparison result, and “best of” result.
  - Expected: Each click opens the corresponding product detail page or article rather than an unrelated page or broken destination.

## Content

- [X] CT-01: Editorial content is limited to the stated product-review themes.
  - Action: Browse category listings, product pages, and articles.
  - Expected: Content is relevant to in-depth guides and product reviews for categories such as cameras, monitors, and vacuum cleaners.

- [ ] CT-02: Ranked “best of” lists contain meaningful ranking information.
  - Action: Inspect a default “best of” list from first place through the final entry.
  - Expected: Every listed product has a visible rank or ordered position and content explaining its inclusion.
  - Bug Report:
    - Issue: Products lack visible rank positions
    - Actual: The best-of article explains why products are included, but each product card has no visible rank or ordered position such as 1st, 2nd, or 3rd.

- [X] CT-03: Comparison rows align the same information across products.
  - Action: Inspect several specification, rating, and summary rows on a comparison page.
  - Expected: Each row represents the same criterion for every product, with no shifted, missing, or mismatched product values.

- [X] CT-04: Product ratings, verdict, and related-article links refer to the same product.
  - Action: Compare the product name and identity across its detail page, ratings, verdict summary, and related links.
  - Expected: All displayed ratings, verdict text, and linked reviews/comparisons correspond to the selected product.