# Test Checklist

## Functionality

- [ ] **FT-01**: Homepage exposes all three content types and all three product categories
  - Action: From the homepage, locate and click the navigation forReviews, Comparisons, and Best-of Lists, and each of Cameras, Monitors, and Vacuum Cleaners.
  - Expected: All six destinations load successfully and display a non-empty listing of default content relevant to the clicked type/category.

- [ ] **FT-02**: A long-form review article renders its complete in-depth content
  - Action: Open any review article from the reviews listing and read to the bottom of the page.
  - Expected: The article page displays its title, publication date, and full body content (multiple paragraphs/sections — not a truncated excerpt only), with no "Read more" dead-end.

- [ ] **FT-03**: "Best of" list is ranked and shows an overall score per product
  - Action: Open a best-of list (e.g., "Best Cameras"), then note the rank and score of each entry from top to bottom.
  - Expected: Products are displayed in explicit ranked order (1, 2, 3…) and every entry shows an overall score value next to/under its name.

- [ ] **FT-04**: Product detail page shows multi-criteria ratings and a verdict summary
  - Action: Open any product's detail page from a listing, search result, or best-of list.
  - Expected: The page shows separate ratings for at least Design, Performance, and Value, plus a distinct "Verdict" summary section containing prose specific to that product.

- [ ] **FT-05**: Product detail page links to every review it appears in
  - Action: On a product detail page, note the titles listed in its "Reviews" (appears-in) section, then click one link.
  - Expected: At least one review is listed, and clicking a listed review opens that review article page (title matches the link clicked).

- [ ] **FT-06**: Product detail page links to every comparison it appears in
  - Action: On a product detail page, note the titles listed in its "Comparisons" (appears-in) section, then click one link.
  - Expected: The section is present and distinct from the Reviews section; clicking a listed comparison opens that comparison page (title matches the link clicked).

- [ ] **FT-07**: Comparison page lines up specs, ratings, and summaries for several products
  - Action: Open any comparison article and examine the comparison layout across all products it covers.
  - Expected: Two or more products are shown side by side, with the same set of key spec rows and rating rows aligned per product, and each product column includes a summary.

- [ ] **FT-08**: Listing can be filtered by category
  - Action: Go to the products/article listing, select the "Monitors" category filter, and apply it.
  - Expected: Only products belonging to Monitors are shown; no Cameras or Vacuum Cleaners products remain visible.

- [ ] **FT-09**: Listing can be filtered by price range band
  - Action: On the products listing, select one predefined price band (e.g., "$500–$999") and apply it.
  - Expected: Every displayed product's price falls within the selected band; products outside it are not shown.

- [ ] **FT-10**: Listing can be sorted by overall score
  - Action: On the products listing, select the "Overall Score" sort option.
  - Expected: Products are reordered by overall score (highest first for descending, or lowest first if ascending is selected), and the order differs from the unsorted default unless already coincidental.

- [ ] **FT-11**: Listing can be sorted by date
  - Action: On the products (or articles) listing, select the "Date" sort option.
  - Expected: Items are reordered by publication date (newest first for descending), and the displayed dates move monotonically in the chosen direction down the list.

- [ ] **FT-12**: Search returns both products and articles
  - Action: In the site search box, enter a term that appears in default content (e.g., "Sony" or "vacuum") and submit.
  - Expected: The results page returns matching items and clearly distinguishes product results from article results (separate sections or labeled result types); both types appear when both match.

## Constraint

- [ ] **CS-01**: Category and price band filters combine rather than override each other
  - Action: Apply the "Cameras" category filter, then additionally apply one price band, without clearing the category.
  - Expected: Results include only products that are both Cameras and within the selected price band; the category filter stays selected and results are a subset of each filter alone.

- [ ] **CS-02**: A search with no matches shows an explicit no-results state
  - Action: Search for a nonsense string (e.g., "zzzzqqq123") and submit.
  - Expected: A "No results" (or equivalent) message is displayed, no stale results from a previous query remain, and the page does not error out.

- [ ] **CS-03**: Ranked best-of list has no duplicate or skipped ranks
  - Action: Inspect the full rank sequence of a best-of list and cross-check product names.
  - Expected: Ranks run consecutively (1, 2, 3, …) with no repeated rank number and no product listed twice.

- [ ] **CS-04**: Overall score is consistent between listing and product detail page
  - Action: Note a product's overall score in a listing/best-of page, then open that product's detail page and compare.
  - Expected: The two overall score values are identical; no product displays a blank/missing overall score in either view.

## Interaction

- [ ] **IX-01**: Choosing a sort option visibly reorders the listing and marks it active
  - Action: Change the sort control from its default to "Overall Score", then to "Date".
  - Expected: The listing updates in place each time with the new order, and the currently selected sort option is shown as active/selected in the control.

- [ ] **IX-02**: Applied filters are visibly indicated on the page
  - Action: Apply a category filter, then apply a price band filter.
  - Expected: The selected category and price band are each visibly reflected in the interface (checked/selected state, filter chip, or results heading naming them), and each can be removed/cleared to restore the full listing.

## Content

- [ ] **CT-01**: Product listings and detail pages contain real, relevant product data
  - Action: Review several product cards and two product detail pages from default data.
  - Expected: Each shows a real product name, a price, and a category matching Cameras/Monitors/Vacuum Cleaners; no placeholder text ("Lorem ipsum", "Product 1", "TODO"), and no broken or missing product images.

- [ ] **CT-02**: All articles contain substantive, on-theme review content
  - Action: Open one review, one comparison, and one best-of list and inspect their text and media.
  - Expected: Each displays a non-empty title, date, and body text about cameras, monitors, or vacuum cleaners; no generic stock filler, unrelated topics, or empty sections/spec rows.