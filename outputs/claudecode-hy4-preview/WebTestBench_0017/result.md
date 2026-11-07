# Test Result

## Functionality

- [ ] **FT-01**: Homepage exposes all three content types and all three product categories
  - Action: From the homepage, locate and click the navigation forReviews, Comparisons, and Best-of Lists, and each of Cameras, Monitors, and Vacuum Cleaners.
  - Expected: All six destinations load successfully and display a non-empty listing of default content relevant to the clicked type/category.
  - Bug Report:
    - Issue: Missing navigation destinations
    - Actual: The header navigation contains only 4 links — `Cameras -> /products?category=cameras`, `Monitors -> /products?category=monitors`, `Vacuums -> /products?category=vacuums`, `Compare -> /compare` — plus a search toggle. There is no navigation entry for Reviews, Comparisons, or Best-of Lists anywhere in the header or footer (footer only lists the 3 categories plus "Compare Products" and "All Products"). There is no article listing route at all: `/articles` returns the 404 page ("404 / Oops! Page not found"). The three category links do work (clicking Cameras/Monitors/Vacuums from the homepage loads `/products?category=…` with 3 correctly-filtered products each), and `/compare` loads "Compare Products", so 4 of 6 destinations exist; 3 of 6 requested destinations do not exist.

- [X] **FT-02**: A long-form review article renders its complete in-depth content
  - Action: Open any review article from the reviews listing and read to the bottom of the page.
  - Expected: The article page displays its title, publication date, and full body content (multiple paragraphs/sections — not a truncated excerpt only), with no "Read more" dead-end.

- [ ] **FT-03**: "Best of" list is ranked and shows an overall score per product
  - Action: Open a best-of list (e.g., "Best Cameras"), then note the rank and score of each entry from top to bottom.
  - Expected: Products are displayed in explicit ranked order (1, 2, 3…) and every entry shows an overall score value next to/under its name.
  - Bug Report:
    - Issue: Missing rank indicators / ranking not rendered
    - Actual: `/article/best-mirrorless-cameras-2024` renders its entries in a "Products Mentioned" card grid with only an image, name, and score badge (8.7, 8.8, 8.8). No rank number ("1", "2", "3" or "#1") is displayed on any entry. Additionally, the rendered order (Sony A7 IV, Canon EOS R6 Mark II, Fujifilm X-H2S) contradicts the article's own prose, which states "Our top pick for most people is the Canon EOS R6 Mark II… The Sony A7 IV comes in as a close second".

- [X] **FT-04**: Product detail page shows multi-criteria ratings and a verdict summary
  - Action: Open any product's detail page from a listing, search result, or best-of list.
  - Expected: The page shows separate ratings for at least Design, Performance, and Value, plus a distinct "Verdict" summary section containing prose specific to that product.

- [X] **FT-05**: Product detail page links to every review it appears in
  - Action: On a product detail page, note the titles listed in its "Reviews" (appears-in) section, then click one link.
  - Expected: At least one review is listed, and clicking a listed review opens that review article page (title matches the link clicked).

- [ ] **FT-06**: Product detail page links to every comparison it appears in
  - Action: On a product detail page, note the titles listed in its "Comparisons" (appears-in) section, then click one link.
  - Expected: The section is present and distinct from the Reviews section; clicking a listed comparison opens that comparison page (title matches the link clicked).
  - Bug Report:
    - Issue: Comparisons section not distinct from Reviews section
    - Actual: Product detail pages have a single combined "Featured In" section that mixes all article types in one grid. On `/product/sony-a7iv` it contains "The Best Mirrorless Cameras of 2024" (Best Of), "Sony A7 IV Review: The New Hybrid Standard" (Review), and "Canon R6 II vs Sony A7 IV: The Ultimate Showdown" (Comparison) with no sub-headings separating Reviews from Comparisons. Clicking the comparison link does navigate correctly to `/article/canon-vs-sony-2024` with matching H1, but the required separate/distinct "Comparisons" section does not exist.

- [ ] **FT-07**: Comparison page lines up specs, ratings, and summaries for several products
  - Action: Open any comparison article and examine the comparison layout across all products it covers.
  - Expected: Two or more products are shown side by side, with the same set of key spec rows and rating rows aligned per product, and each product column includes a summary.
  - Bug Report:
    - Issue: Comparison article has no side-by-side comparison layout
    - Actual: `/article/canon-vs-sony-2024` (tagged "Comparison") contains only prose sections (Autofocus, Image Quality, Video Features, Ergonomics, Lens Ecosystem, The Verdict) followed by a "Products Mentioned" card grid. There are no aligned spec rows, no rating rows per product, and no per-product summary column. The separate `/compare?products=canon-r6ii,sony-a7iv` tool page does align spec rows (Price, Sensor, Video, AF Points, ISO Range, Weight, Battery Life) and rating rows (Overall Score, design, performance, value, features, build) across two columns, but even there each product column shows only brand/name/price/score with no summary prose.

- [X] **FT-08**: Listing can be filtered by category
  - Action: Go to the products/article listing, select the "Monitors" category filter, and apply it.
  - Expected: Only products belonging to Monitors are shown; no Cameras or Vacuum Cleaners products remain visible.

- [ ] **FT-09**: Listing can be filtered by price range band
  - Action: On the products listing, select one predefined price band (e.g., "$500–$999") and apply it.
  - Expected: Every displayed product's price falls within the selected band; products outside it are not shown.
  - Bug Report:
    - Issue: Price band filter returns products outside the selected band
    - Actual: The four bands are labeled `Budget ($0-$300)`, `Mid-Range ($300-$700)`, `Premium ($700-$1200)`, `Luxury ($1200+)`, but they filter on a separate data field that disagrees with the displayed prices. Measured results: `Premium ($700-$1200)` → 5 products: Canon EOS R6 Mark II **$2499**, Fujifilm X-H2S **$2499**, Sony A7 IV **$2499**, LG 27GP950-B $799, Samsung Bespoke Jet **$649** — while Dell Alienware AW3423DWF at **$1099** (inside the band) is excluded. `Luxury ($1200+)` → 4 products including Dell **$1099** and Dyson V15 Detect **$749**, both below $1200. `Mid-Range ($300-$700)` → 0 products although Samsung Bespoke Jet is $649. `Budget ($0-$300)` → 0 products (correct, no product is under $300).

- [X] **FT-10**: Listing can be sorted by overall score
  - Action: On the products listing, select the "Overall Score" sort option.
  - Expected: Products are reordered by overall score (highest first for descending, or lowest first if ascending is selected), and the order differs from the unsorted default unless already coincidental.

- [X] **FT-11**: Listing can be sorted by date
  - Action: On the products (or articles) listing, select the "Date" sort option.
  - Expected: Items are reordered by publication date (newest first for descending), and the displayed dates move monotonically in the chosen direction down the list.

- [X] **FT-12**: Search returns both products and articles
  - Action: In the site search box, enter a term that appears in default content (e.g., "Sony" or "vacuum") and submit.
  - Expected: The results page returns matching items and clearly distinguishes product results from article results (separate sections or labeled result types); both types appear when both match.

## Constraint

- [X] **CS-01**: Category and price band filters combine rather than override each other
  - Action: Apply the "Cameras" category filter, then additionally apply one price band, without clearing the category.
  - Expected: Results include only products that are both Cameras and within the selected price band; the category filter stays selected and results are a subset of each filter alone.

- [X] **CS-02**: A search with no matches shows an explicit no-results state
  - Action: Search for a nonsense string (e.g., "zzzzqqq123") and submit.
  - Expected: A "No results" (or equivalent) message is displayed, no stale results from a previous query remain, and the page does not error out.

- [ ] **CS-03**: Ranked best-of list has no duplicate or skipped ranks
  - Action: Inspect the full rank sequence of a best-of list and cross-check product names.
  - Expected: Ranks run consecutively (1, 2, 3, …) with no repeated rank number and no product listed twice.
  - Bug Report:
    - Issue: No rank sequence exists to validate
    - Actual: On `/article/best-mirrorless-cameras-2024` no rank numbers are rendered on any entry (only score badges 8.7 / 8.8 / 8.8), so there is no 1-2-3 sequence at all — nothing to verify as consecutive. Product names are unique (Sony A7 IV, Canon EOS R6 Mark II, Fujifilm X-H2S, no duplicates), but the display order contradicts the article prose that names Canon as the #1 pick and Sony as #2.

- [X] **CS-04**: Overall score is consistent between listing and product detail page
  - Action: Note a product's overall score in a listing/best-of page, then open that product's detail page and compare.
  - Expected: The two overall score values are identical; no product displays a blank/missing overall score in either view.

## Interaction

- [X] **IX-01**: Choosing a sort option visibly reorders the listing and marks it active
  - Action: Change the sort control from its default to "Overall Score", then to "Date".
  - Expected: The listing updates in place each time with the new order, and the currently selected sort option is shown as active/selected in the control.

- [X] **IX-02**: Applied filters are visibly indicated on the page
  - Action: Apply a category filter, then apply a price band filter.
  - Expected: The selected category and price band are each visibly reflected in the interface (checked/selected state, filter chip, or results heading naming them), and each can be removed/cleared to restore the full listing.

## Content

- [ ] **CT-01**: Product listings and detail pages contain real, relevant product data
  - Action: Review several product cards and two product detail pages from default data.
  - Expected: Each shows a real product name, a price, and a category matching Cameras/Monitors/Vacuum Cleaners; no placeholder text ("Lorem ipsum", "Product 1", "TODO"), and no broken or missing product images.
  - Bug Report:
    - Issue: Broken product image
    - Actual: All 9 products show real names, prices ($649–$2499) and a valid category (Cameras/Monitors/Vacuums); no placeholder text found, and detail pages for Canon EOS R6 Mark II and Sony A7 IV show full real specs, pros/cons and verdicts. However, on `/products` the image for **Roborock S8 Pro Ultra** failed to load: `<img alt="Roborock S8 Pro Ultra" src="https://images.unsplash.com/photo-1603618090554-0df40bb5e4c7?w=600&q=80">` reports `naturalWidth = 0`, `naturalHeight = 0`, `complete = true`. The other 8 product images all report naturalWidth 600.

- [X] **CT-02**: All articles contain substantive, on-theme review content
  - Action: Open one review, one comparison, and one best-of list and inspect their text and media.
  - Expected: Each displays a non-empty title, date, and body text about cameras, monitors, or vacuum cleaners; no generic stock filler, unrelated topics, or empty sections/spec rows.

---

### Notes on observations that did not change a verdict

- **FT-05**: The appears-in section is labeled "Featured In" rather than "Reviews"; it does list the review ("Sony A7 IV Review: The New Hybrid Standard") and the click opens the matching article, so the functional expectation is met.
- **FT-10 / IX-01**: The listing's default sort is already "Highest Score", so selecting it is a no-op; correctness was confirmed by first switching to "Price: High to Low" (order changed) and then back to "Highest Score" (order restored to 9.0, 8.9, 8.8, 8.8, 8.8, 8.7, 8.7, 8.6, 8.6 — monotonically descending).
- **FT-11**: Product cards in the listing render no publication date, so "dates move monotonically" is not directly observable. Correct ordering was confirmed indirectly: the "Newest First" order produced on `/products` is identical to the homepage "Latest Products" section (which links to `/products?sort=date`) — ASUS PG32UCDM, Roborock S8 Pro Ultra, LG 27GP950, Samsung Bespoke Jet, Canon R6 II, Dell AW3423DWF, …
- **CS-01**: The intersection behaviour was verified with Monitors (3) + Premium (5) → 1 result (LG 27GP950-B), a proper subset of each filter alone, with the Monitors checkbox still `data-state="checked"`. Note that Cameras + Luxury returned 0 products even though all three cameras are $2499 — a downstream symptom of the FT-09 band/label mismatch, not of the combination logic itself.
- **IX-02**: Indication is via checkbox state (`aria-checked="true"` / `data-state="checked"`) and the "Showing N products" count; there are no filter chips and the H1 stays "All Products" regardless of filters. Clearing both filters restored "Showing 9 products".
- **Secondary issue (not in checklist)**: clicking a category nav link while already on `/products` updates the URL to `/products?category=…` but does not apply the filter (still "Showing 9 products" with mixed categories); the filter only applies on a fresh mount (homepage → category link, or a direct URL load).