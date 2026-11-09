# Test Result

## Functionality

- [ ] FT-01: Create a new product entry with all required details
  - Action: Open the create/add product form, fill in name, brief review, key specs, category, tags, price, rating, and an affiliate purchase link, then click "Save"/"Create".
  - Expected: The new product is created and appears in the product list with all entered values displayed on its entry/detail page.
  - Bug Report:
    - Issue: Data Persistence Failure (created product lost on page reload)
    - Actual: The product is created in-session only. After filling all fields (name "Anker Soundcore Space One", review, 2 key specs, category "Tech Gadgets", tags, $149, 4.3, affiliate link) and clicking "Create Product", a "Product created successfully" toast appears and the product shows in the product list ("10 products found") with all values on its detail page — but only until the page is reloaded. After any page reload the product vanishes from the admin panel and product list ("9 products found" again), and its detail URL (/product/anker-soundcore-space-one) returns "Product Not Found". No data store persists it (localStorage/sessionStorage empty, no API write occurs; data loads from static src/data/products.ts). The product is not durably created.

- [ ] FT-02: Edit an existing product entry
  - Action: Open any existing product, click "Edit", change its review text and price, then save.
  - Expected: The product detail page and product list show the updated review text and price; no other fields are lost.
  - Bug Report:
    - Issue: Data Persistence Failure (edits lost on page reload)
    - Actual: Editing Sony WH-1000XM5 (review text changed to "UPDATED: Industry-leading noise cancellation, verified over 60 days…", price 399 → 349) shows "Product updated successfully" and the changes appear in the product list and detail page in-session with all other fields intact. After a page reload, the admin list, product list, and detail page all revert to the original review text and $399 — the save is never persisted.

- [ ] FT-03: Categorize a product
  - Action: Edit an existing product and set its category to one of "Tech Gadgets", "Home Goods", or "Fitness"; save.
  - Expected: The product is saved with the chosen category and appears when browsing that category.
  - Bug Report:
    - Issue: Data Persistence Failure (category change lost on page reload)
    - Actual: Editing Breville Barista Express from "Home Goods" to "Fitness" works in-session (the product appears under /category/fitness and is removed from /category/home), but after a page reload the product is back in its original category — the chosen category is never saved durably.

- [ ] FT-04: Tag a product
  - Action: Edit an existing product and add one or more tags (e.g., "budget", "wireless"); save.
  - Expected: The product's detail page displays the added tags, and the tags persist after leaving and revisiting the page.
  - Bug Report:
    - Issue: Data Persistence Failure (added tags not persisted)
    - Actual: Tags added in the edit form (e.g., "budget, espresso, kitchen" on Breville Barista Express; "premium, wireless, noise-cancelling" on Sony) display on the detail page immediately after saving, but after leaving and revisiting the page via reload the detail page shows the original seed tags again (e.g., "headphones, wireless, noise-cancelling, premium") — the added tags do not persist.

- [ ] FT-05: Mark a product as featured
  - Action: Edit an existing product and enable the "Featured" setting; save, then open the homepage.
  - Expected: The product appears in the homepage's featured section; previously featured items remain until unmarked.
  - Bug Report:
    - Issue: Featured Section Display Limit + Non-persistent Featured State
    - Actual: Marking a 4th product featured (Apple MacBook Pro 14", toggle confirmed aria-checked=true, "Product updated successfully") does not show it in the homepage "Editor's Top Picks" section, which is hard-capped at 3 items and keeps showing only the seeded Sony/Peloton/Dyson. MacBook only appeared after an existing featured item (Sony) was unmarked in the same session (swap to Peloton/Dyson/MacBook). Additionally, the featured flag is lost entirely on page reload (see IX-02). The expected "the product appears in the homepage's featured section" is not met in the app's default state.

- [X] FT-06: Browse products by category
  - Action: From the homepage or navigation, select a category (e.g., "Tech Gadgets").
  - Expected: The product list shows only products assigned to that category, including at least one default product.

- [X] FT-07: Sort products by price and rating
  - Action: Open the product list and apply sorting "Price: Low to High", then "Price: High to Low", then "Rating: High to Low".
  - Expected: Each sort reorders the list correctly (prices ascending/descending, ratings descending) without hiding any products.

- [ ] FT-08: Filter products by price range and rating
  - Action: Set a price range (e.g., 0–50) and a minimum rating (e.g., 4 stars) using the filter controls, then apply.
  - Expected: Only products whose price falls within the range AND whose rating meets the minimum are shown; clearing filters restores the full list.
  - Bug Report:
    - Issue: Missing Filter Control / Mis-calibrated Slider (price range cannot be set)
    - Actual: The price filter exposes only a single "Minimum" slider thumb (aria-valuemin=0, aria-valuemax=2495) — there is no maximum price control at all, so a price *range* such as 0–50 cannot be configured (products above any desired maximum stay listed). Additionally the minimum slider's drag mapping is broken: dragging the thumb to 25%/50%/80% of the track sets $20/$40/$70 instead of roughly $620/$1250/$2000 of the 0–2495 scale, and "End" does nothing, so meaningful minimum prices cannot be selected by dragging. The minimum-rating dropdown ("Any rating / 4+ stars / 4.5+ stars") works correctly (4.5+ hides the 4.4-rated Philips Hue), and resetting controls restores the full list — but the price-range expectation cannot be met.

- [X] FT-09: Search products by keyword
  - Action: Type a keyword matching an existing product (e.g., part of a product name or tag) into the search field and submit.
  - Expected: The search results page lists the matching product(s) with name, review excerpt, and price visible.

- [X] FT-10: View a product's detail page
  - Action: Click any product card/title from the product list.
  - Expected: The detail page displays the product name, the full brief review, key specs, price, rating, and an external purchase button.

- [X] FT-11: Use the affiliate purchase link
  - Action: Click the external purchase button (labeled with the retailer, e.g., "Buy at [Retailer]") on a product detail page.
  - Expected: The external retailer URL stored for that product opens (in a new tab), and the URL matches the affiliate link shown for the product.

## Constraint

- [ ] CS-01: Prevent saving a product with missing required fields
  - Action: Open the create product form and submit it with an empty name, empty review, or empty purchase link.
  - Expected: The form does not create the product; it shows a validation error identifying the missing required field(s).
  - Bug Report:
    - Issue: Incomplete Form Validation (empty purchase link accepted; generic error message)
    - Actual: Submitting the fully empty form is blocked with a toast "Please fill in all required fields", but this generic message does not identify which required field(s) are missing, and there is no per-field error. Worse, submitting with name and review filled but an EMPTY purchase link succeeds — toast "Product created successfully" and the product ("Link Missing Test") is created with no affiliate link at all. Only Product Name and Short Description are enforced (labels marked *); the purchase link is not required despite the checklist.

- [ ] CS-02: Reject an invalid external purchase link
  - Action: In the create/edit product form, enter a non-URL value (e.g., "not a link") in the affiliate link field and save.
  - Expected: The save is rejected with a message that the purchase link must be a valid URL; no product is saved with the invalid link.
  - Bug Report:
    - Issue: Missing URL Validation (invalid link accepted and saved)
    - Actual: Entering "not a link" in the Affiliate Link field and clicking "Create Product" succeeds — toast "Product created successfully" and the product ("Invalid Link Test Product") is saved and listed in the admin panel with the invalid link. The Affiliate Link input is type="text" with no required/pattern constraints; no validation message is shown and the save is not rejected.

- [ ] CS-03: Prevent an invalid price range filter
  - Action: In the price range filter, enter a minimum price greater than the maximum price (e.g., min 100, max 10) and apply.
  - Expected: The filter does not produce a broken/empty-result state; an error or correction prompt is shown and the product list remains usable.
  - Bug Report:
    - Issue: Non-executable Test Scenario / Missing Filter Control (no maximum price input or validation prompt exists)
    - Actual: This scenario cannot be entered in the UI: the price filter provides only a "Minimum" slider (no maximum price field and no numeric min/max inputs to type into), so "min 100, max 10" cannot be expressed. Over-dragging the thumb past the track end silently clamps within bounds with no error or correction prompt of any kind (the list stays usable, but the required validation feedback never appears because there is no max value to compare against).

## Interaction

- [X] IX-01: Confirm create/edit actions with success feedback
  - Action: Save a new product, then save an edit to an existing product.
  - Expected: Each save displays a visible success confirmation (e.g., toast "Product saved") that disappears automatically after a few seconds.

- [ ] IX-02: Homepage responds to featured changes
  - Action: Mark a product as featured and reload the homepage; then unmark it and reload again.
  - Expected: The homepage featured section updates accordingly — the product appears when featured and is removed when unfeatured, without requiring a server restart.
  - Bug Report:
    - Issue: Non-persistent Featured State (featured changes lost on reload)
    - Actual: After marking Apple MacBook Pro 14" as featured ("Product updated successfully") and reloading the homepage, the "Editor's Top Picks" section still shows only the seeded Sony/Peloton/Dyson — the marked product does not appear. After unmarking and reloading, the change is likewise gone (seed state returns). All featured flags live only in client-side memory (data is re-imported from static src/data/products.ts on every load), so the homepage featured section reverts to seed content on every page reload. (It also caps at 3 items even within a session — see FT-05.)

- [X] IX-03: Sorting/filtering updates the list without full reload errors
  - Action: Change sort order, then adjust filters, in sequence on the product list page.
  - Expected: The product list refreshes each time to reflect the new order/filter; no blank page or error state occurs between changes.

## Content

- [X] CT-01: Featured homepage content matches the site's niche themes
  - Action: View the homepage featured section and each featured product's category.
  - Expected: All featured products belong to tech gadgets, home goods, or fitness, with relevant names, review text, and product images — no placeholder or unrelated content.

- [X] CT-02: Product detail pages show meaningful review and specs content
  - Action: Open 2–3 existing product detail pages and read the review and key specs sections.
  - Expected: Each page shows a brief, product-specific review and concrete key specs (e.g., dimensions, battery life) — not empty, generic, or duplicated text across products.

- [ ] CT-03: Purchase button label is clear and retailer-specific
  - Action: Inspect the external purchase button on several product detail pages.
  - Expected: Each button has a clear action label indicating an external purchase (e.g., "Buy at Amazon" / "Check Price at [Retailer]"), not vague text like "Click here" or "More".
  - Bug Report:
    - Issue: Vague / Non-retailer-specific Button Label
    - Actual: Every purchase button on every product detail page and card reads exactly "Buy Now" (verified on Sony WH-1000XM5, Dyson V15 Detect, Theragun Pro, and all list cards). The label names no retailer (e.g., "Buy at Amazon") and gives no indication the purchase happens externally, regardless of which affiliate link (example.com/sony-xm5, example.com/dyson-v15, etc.) it points to.
