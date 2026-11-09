# Test Result

## Functionality

- [ ] FT-01: Publish a long-form review.
  - Action: Create a new review for a default product, enter title, body, and per-criteria ratings, then save.
  - Expected: Review is saved and appears on the product's detail page and in article listings.
  - Bug Report:
    - Issue: Missing Feature (no authoring/publishing UI)
    - Actual: The application exposes only read-only routes (`/`, `/products`, `/product/:id`, `/article/:id`, `/compare`, `/search`). No "create review", form, or save control exists anywhere; article data is served from a static `/src/data/articles.ts` file. A review cannot be created.

- [ ] FT-02: Publish a side-by-side comparison article.
  - Action: Create a comparison article for two default products, add comparison body and summary, then save.
  - Expected: Comparison article is saved and appears on the comparison page and in article listings.
  - Bug Report:
    - Issue: Missing Feature (no authoring/publishing UI)
    - Actual: No interface exists to author a comparison article. `/compare` only supports interactively selecting pre-existing products (max 4) for on-screen comparison; it does not create/save an article and provides no body/summary fields.

- [ ] FT-03: Publish a ranked "best of" list.
  - Action: Create a "best of" list for a category (e.g., cameras), assign ranked default products, then save.
  - Expected: List is saved and displays products in the assigned rank order.
  - Bug Report:
    - Issue: Missing Feature (no authoring/publishing UI)
    - Actual: No "best of" creation UI or rank-assignment control exists. Existing best-of articles are static seed data that cannot be authored or re-ranked by the user.

- [X] FT-04: Product detail page shows ratings across multiple criteria.
  - Action: Open the detail page of a default product.
  - Expected: Ratings for design, performance, and value appear as numeric values on a consistent scale, alongside an overall score.

- [X] FT-05: Product detail page shows a verdict summary.
  - Action: Open the detail page of a default product.
  - Expected: A verdict summary is displayed and describes the product's overall assessment.

- [X] FT-06: Product detail page links to all reviews and comparisons.
  - Action: Open a default product's detail page that has reviews and comparisons.
  - Expected: Every review and comparison containing that product is listed, and each link opens the correct page.

- [X] FT-07: Filter listings by category.
  - Action: On the listing page, select category "Cameras" (repeat with "Monitors").
  - Expected: Only products belonging to the selected category are shown.

- [ ] FT-08: Filter listings by price range band.
  - Action: On the listing page, select a price band (e.g., "Under $100").
  - Expected: Only products whose price falls within the selected band are shown.
  - Bug Report:
    - Issue: Incorrect Filtering (band ≠ price)
    - Actual: Bands filter by an internal tier label, not by price. "Premium ($700-$1200)" returned Canon R6 II ($2499), Fujifilm X-H2S ($2499), Sony A7 IV ($2499) and Samsung Bespoke Jet ($649); "Mid-Range ($300-$700)" returned nothing despite Samsung at $649; "Luxury ($1200+)" returned Dell AW3423DWF ($1099) and Dyson V15 ($749). Displayed prices contradict the selected bands.

- [X] FT-09: Sort listings by overall score or date.
  - Action: Apply "Sort by overall score," then apply "Sort by date."
  - Expected: Listing reorders to highest overall score first and newest date first, respectively.

- [X] FT-10: Search across products and articles.
  - Action: Enter a default product name in the search field and submit.
  - Expected: Matching products and matching articles are both returned in the results.

- [X] FT-11: Comparison page lines up several products at once.
  - Action: Open a comparison page containing multiple default products (e.g., three cameras).
  - Expected: Key specs, ratings, and summaries are displayed side by side for each product.

## Constraint

- [ ] CS-01: Review cannot be published with empty required fields.
  - Action: Submit a review with an empty title, empty body, or missing rating.
  - Expected: Save is blocked and an inline validation error identifies the missing field.
  - Bug Report:
    - Issue: Missing Feature / Untestable (no review form)
    - Actual: There is no review submission form anywhere in the app, so no validation logic or inline error can be triggered. The behavior required by this constraint does not exist.

- [X] CS-02: Comparison requires at least two products.
  - Action: Attempt to create a comparison page containing only one product.
  - Expected: Creation is blocked and a message states at least two products are required.

- [ ] CS-03: "Best of" list cannot have duplicate or skipped ranks.
  - Action: Assign the same rank to two products (or skip a rank position), then save.
  - Expected: Save is blocked and the duplicate or skipped rank is flagged.
  - Bug Report:
    - Issue: Missing Feature / Untestable (no rank authoring UI)
    - Actual: No interface exists to assign ranks to products or to save a "best of" list, so duplicate/skipped-rank validation cannot be exercised.

## Interaction

- [X] IX-01: Filters and sorting update the listing without reloading.
  - Action: Apply a category filter and change the sort order on the listing page.
  - Expected: Results update in place with no full page reload.

- [ ] IX-02: Confirmation shown after publishing.
  - Action: Publish a review successfully.
  - Expected: A success confirmation message appears and the new item is immediately visible.
  - Bug Report:
    - Issue: Missing Feature (no publish action)
    - Actual: No publish/create action exists, so no success confirmation can be shown. A Toaster component is mounted but is never triggered by any user-reachable authoring flow.

- [ ] IX-03: Clearing filters restores the full listing.
  - Action: Apply category and price filters, then click "Clear filters."
  - Expected: All default listings return and all filter controls reset.
  - Bug Report:
    - Issue: Missing Control ("Clear filters" button absent)
    - Actual: No "Clear filters" button or link exists on `/products` (grep for /clear filters?/ returned 0 matches). Filters can only be reset by manually un-checking each box; the required one-click clear control is missing.

## Content

- [X] CT-01: Displayed product images are relevant.
  - Action: Inspect product cards and detail pages for default products.
  - Expected: Each product's image matches that product; no placeholder or unrelated images appear.

- [X] CT-02: Comparison key specs are aligned per product.
  - Action: Inspect the spec table on a comparison page.
  - Expected: Each spec occupies its own row and each product's value appears in its own column.

- [X] CT-03: Article and product content is relevant to its category.
  - Action: Review published reviews, comparison articles, and "best of" lists.
  - Expected: Each article carries its category label and links to the products it discusses; no unrelated or placeholder content is present.
