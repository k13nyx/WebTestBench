I'll decompose the instruction into a prioritized, binary-pass UI/UX checklist.

# Test Checklist

## Functionality
- [ ] FT-01: Product detail page shows per-criterion ratings
  - Action: Open any product from the product listing (e.g., a camera).
  - Expected: Dedicated detail page loads showing individual numeric ratings for **Design**, **Performance**, and **Value**.

- [ ] FT-02: Product detail page shows a verdict summary
  - Action: On the same product detail page, locate the verdict block.
  - Expected: A section labeled "Verdict" (or equivalent) contains a written summary paragraph, not just a score.

- [ ] FT-03: Product detail page links to every article featuring that product
  - Action: On the product detail page, find the "Reviews" / "Comparisons" links section.
  - Expected: At least one link to a long-form review and one link to a comparison article for that product are listed.

- [ ] FT-04: Listings can be filtered by category
  - Action: On a listing page, select category **Cameras**, then **Monitors**, then **Vacuum Cleaners**.
  - Expected: Each selection produces a filtered listing page of items in that category.

- [ ] FT-05: Listings can be filtered by price range band
  - Action: Apply a price range band filter (e.g., "$0–$200" / "$200–$500") on a listing page.
  - Expected: The filter control accepts the selection and the listing re-renders.

- [ ] FT-06: Listings can be sorted by overall score
  - Action: Choose sort option **Overall Score** on a product listing.
  - Expected: Result order changes to be driven by the product's overall score.

- [ ] FT-07: Listings can be sorted by date
  - Action: Choose sort option **Date** on a product/article listing.
  - Expected: Result order changes to be driven by publication date.

- [ ] FT-08: Search covers both products and articles
  - Action: Enter a term matching a known product (e.g., a camera model) and submit the site search.
  - Expected: Results include the matching product **and** any review/comparison/"best of" articles referencing it.

- [ ] FT-09: Multi-product comparison page is reachable
  - Action: Open a side-by-side comparison article that covers 3+ products in one category.
  - Expected: A single page renders all compared products together, not on separate pages.

- [ ] FT-10: Long-form guide articles render full body content
  - Action: Open a long-form review and a ranked "best of" list from the listings/homepage.
  - Expected: Each renders a full multi-paragraph article body (not a stub, teaser-only, or 404).

## Constraint
- [ ] CS-01: Category filter excludes out-of-category items
  - Action: Filter listings by **Monitors**; inspect every card shown.
  - Expected: Zero cameras or vacuum cleaners appear in the filtered results.

- [ ] CS-02: Price band filter excludes out-of-band products
  - Action: Apply the lowest price band; check each displayed product's listed price.
  - Expected: No product with a price above the band's upper limit is shown.

- [ ] CS-03: Sorting produces a strictly consistent order
  - Action: Sort a listing by **Overall Score**, then by **Date**; read the scores/dates top-to-bottom.
  - Expected: Scores descend monotonically; dates are consistently newest-first (or oldest-first, matching the label). No misordered rows.

- [ ] CS-04: Rating values stay in a valid scale and agree with the overall score
  - Action: On two product detail pages, record the Design/Performance/Value ratings and the overall score.
  - Expected: All ratings fall within the stated scale (e.g., 0–10 or 0–5) and the overall score is consistent with (not higher than) the individual criteria.

## Interaction
- [ ] IX-01: Listing card click navigates to the product detail page
  - Action: Click a product card/title in a filtered listing.
  - Expected: Browser navigates to that specific product's detail page (URL and content match the clicked item).

- [ ] IX-02: Changing filter/sort updates the listing without error
  - Action: While on a listing, change category, then price band, then sort option in sequence.
  - Expected: Results update each time; no blank page, JS error, or stale results left on screen.

- [ ] IX-03: Related-article links on a product page navigate correctly
  - Action: From a product detail page, click a linked review and a linked comparison.
  - Expected: Each opens the corresponding article page, and the clicked product is present/discussed there.

## Content
- [ ] CT-01: Rating criteria are explicitly labeled
  - Action: Inspect the ratings block on a product detail page.
  - Expected: Each score carries a visible criterion name (Design, Performance, Value) — no unlabeled/orphan numbers.

- [ ] CT-02: Comparison page lines up specs, ratings, and summaries per product
  - Action: Inspect the columns of a multi-product comparison page.
  - Expected: Every compared product column contains key specs, criterion ratings, and a short summary — no empty or missing column.

- [ ] CT-03: "Best of" lists display an explicit rank
  - Action: Open a "best of" list article (e.g., Best Cameras).
  - Expected: Each entry shows its rank number (1, 2, 3…) and the order on screen matches those rank numbers.