# Test Result

## Functionality

- [X] FT-01: Create a new product entry with all required attributes
  - Action: Open the "Add Product" / "New Product" form; fill Name `QA Test Speaker`, Category `Tech Gadgets`, Price `199`, Rating `4`, brief Review `Compact speaker with solid battery life.`, at least one Spec (`Battery: 12h`), Affiliate URL `https://example-retailer.com/speaker`, Tags `audio, portable`; submit.
  - Expected: Product is saved and appears in the product listing and under the Tech Gadgets category, showing the entered price, rating, and review text.

- [X] FT-02: Edit an existing default product
  - Action: Open an existing product's edit form, change its Price to `129` and append `Updated by QA.` to its review, then save.
  - Expected: The listing and the product detail page both display the new price `129` and the updated review text; all other fields are unchanged.

- [X] FT-03: Re-categorize an existing product
  - Action: Open a default Fitness product, change its Category to `Home Goods`, save, then browse the Fitness category.
  - Expected: The product no longer appears under Fitness and now appears under Home Goods.

- [ ] FT-04: Add tags to a product and browse by that tag
  - Action: Add the tag `qaqc` to an existing product and save; then click/select the `qaqc` tag filter.
  - Expected: Only products carrying the `qaqc` tag are displayed; the tagged product is present and untagged products are absent.
  - Bug Report:
    - Issue: Stale tag index — newly added tags never appear in the browse tag filter
    - Actual: After adding `qaqc` to Bowflex SelectTech 552 and saving ("Product updated successfully"), the tag IS persisted (the product detail page lists tags `weights / dumbbells / strength / home-gym / qaqc`), but the Filters → Tags list on the browse page still contains only the original 34 tags (`ambiance, android, apple … wireless`) and never includes `qaqc`. `qaqc` therefore cannot be selected, and clicking it leaves all 9 products displayed instead of just the tagged one.

- [ ] FT-05: Mark a product as featured and confirm it on the homepage
  - Action: Toggle "Featured" (or equivalent) on an existing default product, save, then open the homepage.
  - Expected: That product appears in the homepage featured section with its name, price, and rating visible.
  - Bug Report:
    - Issue: Homepage featured section is hard-capped at 3 items, so newly featured products are not surfaced
    - Actual: Toggling Featured on `Breville Barista Express` saved successfully (admin row shows `Home | Featured | Breville Barista Express | $699 | 4.5`, and the Home category listing shows its Featured badge), but the homepage "Editor's Top Picks" section still rendered only the 3 original items (Sony WH-1000XM5, Peloton Bike+, Dyson V15 Detect) — Breville was absent. Only after un-featuring Sony WH-1000XM5 did Breville appear, confirming the section is limited to the first 3 featured products rather than showing all featured items.

- [X] FT-06: Browse products by each category
  - Action: From the homepage/navigation, open each category page: Tech Gadgets, Home Goods, Fitness.
  - Expected: Each page lists a non-empty set of products, and every listed product belongs to that category.

- [X] FT-07: Sort products by price and by rating
  - Action: On any category listing, select sort `Price: Low to High`, then `Price: High to Low`, then `Highest Rated`.
  - Expected: Listed prices are strictly ascending for the first sort, descending for the second, and ratings are descending for the third.

- [ ] FT-08: Filter products by price range and by minimum rating
  - Action: Apply price range min `50` / max `200`; then separately apply rating filter `4 stars & up`.
  - Expected: Only products priced between 50 and 200 are shown for the first filter; only products rated 4 or higher are shown for the second.
  - Bug Report:
    - Issue: Missing maximum-price control — price range filter has only a "Minimum" slider
    - Actual: The Filters → "Price Range" widget exposes a single slider thumb (`role="slider" aria-label="Minimum"`, 0–2495); there is no maximum thumb or max input, so the upper bound cannot be set. With min set to 50 the label reads "Price Range $50 $2495" and all 9 products remain listed — including $399 (Sony), $549 (Bowflex), $599 (Theragun), $699 (Breville), $749 (Dyson), $1,299 (Samsung), $1,999 (MacBook) and $2,495 (Peloton) — instead of only the one product in 50–200 ($199 Philips Hue Starter Kit). The rating half of the test passed: `4+ stars` correctly excluded a 2.0-rated product and kept only products rated 4.4–4.9.

- [X] FT-09: Search products by keyword
  - Action: Type a word taken from an existing default product's name (e.g. `kettle`) into the search box and submit.
  - Expected: That product appears in the results; products without the keyword in their name, review, or tags do not appear.

- [X] FT-10: Product detail page shows review, key specs, and retailer button
  - Action: Open the detail page of any default product from the listing.
  - Expected: The page displays the product name, the full brief review, a key specs section with at least one spec row, and a clearly labeled purchase button (e.g. "Buy Now" / "View at Retailer") that carries the external retailer URL.

## Constraint

- [ ] CS-01: Required fields block product creation
  - Action: Open "Add Product", leave Name and Affiliate URL empty, fill the rest, submit.
  - Expected: The product is not saved; an inline error message (e.g. "Name is required") is shown next to each empty required field and the entry does not appear in the listing.
  - Bug Report:
    - Issue: No per-field inline validation; and Affiliate URL is not enforced as required
    - Actual: With Name and Affiliate URL both empty, submission was blocked and the form stayed open, but the only feedback was one generic message "Please fill in all required fields" rendered in a `<div>` outside the form fields (a transient toast that disappears after a few seconds) — no inline error appears next to the Name or Affiliate URL inputs. Additionally, when Name was filled but Affiliate URL left empty, the product was created anyway ("Product created successfully", entry `QA No Affiliate` added to the listing), so the empty Affiliate URL was not rejected at all.

- [ ] CS-02: Invalid price and rating values are rejected
  - Action: Attempt to save a product with Price `-10` and then with Rating `6`; attempt again with Price `abc`.
  - Expected: Each attempt is rejected with a validation error and no product is saved with an invalid price or a rating outside 0–5.
  - Bug Report:
    - Issue: No price validation — negative and non-numeric prices are accepted and saved
    - Actual: Price `-10` was accepted: "Product created successfully" and the admin listing shows the product with price `-$10`. Typing `abc` into the Price field (a `type="number"` input with no `min`/`max`/`step`) silently resolved to `0`, and that product was also created successfully as `QA Price Abc` at $0. Only Rating `6` was rejected (submission blocked, no product created) — and that case relied on the browser's native number-input `max=5` check with no error message rendered in the app.

- [X] CS-03: Non-featured products are excluded from the homepage featured section
  - Action: Note a default product that is not marked featured, then load the homepage.
  - Expected: That product does not appear anywhere in the featured section; the featured section contains only items marked featured.

- [X] CS-04: No-match search shows an explicit empty state
  - Action: Search for `zzqqxx12345`.
  - Expected: An explicit empty-state message (e.g. "No products found") is displayed; the page does not error out or render a blank results area.

## Interaction

- [X] IX-01: Clicking a product card opens that product's detail page
  - Action: Click a product card in any listing or featured section.
  - Expected: The detail page for that exact product opens, with the product name matching the card that was clicked.

- [X] IX-02: Sort and filter selections refresh the list in place and stay applied
  - Action: On a category listing, choose sort `Price: Low to High` and a price range filter, and observe the results grid.
  - Expected: The grid updates to the filtered/sorted set without leaving the page, and the chosen sort option and active filter remain visibly selected/indicated after the refresh.

- [X] IX-03: Retailer button opens the external retailer link
  - Action: On a product detail page, click the retailer/purchase button.
  - Expected: The external retailer URL opens in a new browser tab, and the URL matches the affiliate link stored for that product.

## Content

- [X] CT-01: Product cards show the essential summary information
  - Action: Inspect 3 default product cards in any listing.
  - Expected: Each card displays product name, category, price, rating, and a brief review (excerpt or full) — none of these are blank or showing placeholder text like "undefined" / "N/A".

- [X] CT-02: Detail page content is complete and relevant to the product
  - Action: Open 2 different default product detail pages.
  - Expected: Each shows the product's own brief review text and its own key specs list; no review or spec text is duplicated from a different product or replaced by lorem ipsum/placeholder.

- [X] CT-03: Only the three intended categories exist and are labeled correctly
  - Action: Open the category navigation/menu and list all available categories.
  - Expected: Exactly the categories Tech Gadgets, Home Goods, and Fitness are offered, labeled with those names, and every default product is assigned to one of them.
