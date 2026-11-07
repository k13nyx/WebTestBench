All checklist items have been executed and verified. Here is the full result.

# Test Result

## Functionality

- [X] FT-01: Owner can create a new product entry with name, category, review, price, rating, key specs, tags, and purchase link
  - Action: Open the admin/product management area, click "Add Product" / "New Entry", fill in all fields (name "Test Gadget", category "Tech Gadgets", brief review, price, rating, specs, at least one tag, retailer URL), and save.
  - Expected: Entry is saved and appears in the product listing with all entered values, and a success confirmation is shown.
  - Observed: Toast "Product created successfully" was shown; the admin listing and the visitor listing ("10 products found") both show the new card (Tech, $149, 3.0, "A brief test gadget review for QA purposes."); its detail page shows category Tech, price $149, rating 3.0, tags `budget`/`portable`, "Key Specifications: Battery Life – 20 hours" and the full review, with the purchase button pointing to `https://example.com/test-gadget`. (Note: the app has no backend — data lives in an in-memory React context, so entries are lost on a full page reload; all edits below were therefore verified through in-app navigation.)

- [X] FT-02: Owner can edit an existing product entry and changes are reflected everywhere
  - Action: Open an existing product (from default data) in the editor, change its review text, price, and category, and save.
  - Expected: The updated review, price, and category are shown on the product listing card and on the product detail page; the old values are no longer displayed anywhere.
  - Observed: "Philips Hue Starter Kit" edited (price $199→$179, category Home Goods→Fitness, new short/full review). Listing card: "Fitness | $179 | Philips Hue Starter Kit | UPDATED REVIEW: a smarter, cozier home lighting kit…". Detail page: category Fitness, $179, "My Review: UPDATED FULL REVIEW: The Philips Hue starter kit was edited for QA purposes…". Old price $199, old "Home" category and old review text no longer appear on the listing, detail page, or category pages.

- [X] FT-03: Owner can assign a product to a category (Tech Gadgets, Home Goods, Fitness) and visitors can browse by category
  - Action: Set an existing product's category to "Fitness", then as a visitor open the category browse view and select "Fitness".
  - Expected: Only products assigned to "Fitness" are listed; the edited product appears in that list and no longer appears in its previous category's list.
  - Observed: /category/fitness lists exactly Bowflex SelectTech 552, Theragun Pro, Peloton Bike+ and the edited Philips Hue Starter Kit (4 products, all Fitness). /category/home lists only Breville Barista Express and Dyson V15 Detect — Philips Hue is gone from Home Goods.

- [X] FT-04: Owner can tag products and visitors can view products by tag
  - Action: Add a tag (e.g., "wireless") to a product, then select that tag in the tag filter/browse view.
  - Expected: The tagged product appears under the tag, and only products carrying that tag are shown.
  - Observed: "wireless" was added to Bowflex SelectTech 552 (tags: weights, dumbbells, strength, home-gym, wireless). Selecting the "wireless" chip in the Tags filter yields "2 products found": Bowflex SelectTech 552 and Sony WH-1000XM5 — exactly the two products carrying the tag.

- [ ] FT-05: Owner can mark an item as featured and featured items appear on the homepage
  - Action: Mark an existing product as "Featured", save, then open the homepage.
  - Expected: The marked product is displayed in the homepage featured section with its name, image, price, and rating.
  - Bug Report:
    - Issue: Featured item missing from homepage featured section (hard-coded 3-item cap)
    - Actual: "Bowflex SelectTech 552" was toggled to Featured (admin card showed the "Featured" badge, product listing card showed the badge too). Opening the homepage, the "Editor's Top Picks" section still listed only Sony WH-1000XM5 ($399, 4.8), Peloton Bike+ ($2,495, 4.6) and Dyson V15 Detect ($749, 4.7) — the newly marked Bowflex was absent. The section renders `featuredProducts.slice(0, 3)`, so any 4th featured product is silently dropped. Supporting evidence: after un-featuring Sony WH-1000XM5 (leaving exactly 3 featured: Peloton, Dyson, Bowflex), the homepage section immediately rendered "Bowflex SelectTech 552 | $549 | 4.6 | img:loaded" — confirming the flag is stored correctly and the section is simply capped at 3 entries.

- [X] FT-06: Owner can un-feature an item and it is removed from the homepage featured section
  - Action: Unmark the previously featured product, save, then reload the homepage.
  - Expected: The product no longer appears in the homepage featured section while remaining available in the main product listings.
  - Observed: Bowflex's "Featured on homepage" switch went checked→unchecked on save; the admin card lost its badge; the homepage "Editor's Top Picks" section then contained only Peloton Bike+ and Dyson V15 Detect (no Bowflex), while the product listing still showed "10 products found" including "Bowflex SelectTech 552 | Fitness | $549 | 4.6". (Navigated via the in-app Home link; a hard browser reload restores the seed data because the app has no persistence.)

- [X] FT-07: Visitor can sort products by price (ascending and descending)
  - Action: On the product listing, apply the price sort in both ascending and descending order.
  - Expected: Products are reordered so prices run low→high for ascending and high→low for descending, with the displayed price matching the list order.
  - Observed: "Price: Low to High" → $149, $179, $399, $549, $599, $699, $749, $1,299, $1,999, $2,495. "Price: High to Low" → $2,495, $1,999, $1,299, $749, $699, $599, $549, $399, $179, $149. Displayed prices matched list order in both directions.

- [ ] FT-08: Visitor can sort products by rating (highest and lowest)
  - Action: Apply the rating sort in both directions on the product listing.
  - Expected: Products are reordered by their star rating accordingly, with the displayed rating matching the list order.
  - Bug Report:
    - Issue: Missing sort option (lowest-rating sort unavailable)
    - Actual: The sort dropdown offers only "Newest", "Top Rated", "Price: Low to High", "Price: High to Low" — there is no lowest-rating / rating-ascending option, so the ascending direction of the rating sort cannot be applied at all. The available "Top Rated" option works (4.9 MacBook → 4.8 Sony → 4.7 Dyson/Samsung → 4.6 Peloton/Bowflex → 4.5 Theragun/Breville → 4.4 Philips Hue → 4.2/3.0 lowest), but "lowest rated" cannot be selected.

- [ ] FT-09: Visitor can filter products by a price range
  - Action: Enter a minimum and maximum price (e.g., 50–200) in the price range filter and apply it.
  - Expected: Only products whose price falls within the range are shown; products below the minimum or above the maximum are excluded.
  - Bug Report:
    - Issue: Price-range control can only set a minimum — no maximum-price input/handle
    - Actual: The "Price Range" control renders a single slider thumb (`role="slider" aria-label="Minimum"`); the underlying UI component renders one `SliderPrimitive.Thumb` for a two-ended range, so the upper bound is permanently pinned at the catalogue maximum ("$0 – $2495" and the max label never changes). Driving the only thumb changes only the minimum: min = $200 → "8 products found" (all ≥ $200, Test Gadget $149 and Philips Hue $179 excluded). No maximum can be entered, so a 50–200 range cannot be applied and products above a chosen maximum can never be excluded.

- [X] FT-10: Visitor can filter products by minimum rating
  - Action: Set the rating filter to 4 stars and apply it.
  - Expected: Only products with a rating of 4 or higher are shown; products rated 3 or lower are excluded.
  - Observed: With a product deliberately rated 3.0 (Test Gadget), "4+ stars" → "9 products found" and Test Gadget (3.0) is excluded while all 4.2–4.9 products remain. "4.5+ stars" → "8 products found" (4.4 and 4.2/3.0 removed), confirming the threshold is applied.

- [X] FT-11: Visitor can search for products by keyword
  - Action: Enter a keyword that appears in a default product's name, review, or tag into the search field and submit.
  - Expected: Matching products are listed and each match contains the searched keyword; non-matching products are not shown.
  - Observed: Searching "sony" → "1 product found": Sony WH-1000XM5 (name, description and the "noise-cancelling"/"wireless" tags contain the keyword). All 9 other products were removed.

- [X] FT-12: Each product has its own detail page showing the review and key specs
  - Action: Click the name or card of any product from a listing or the homepage.
  - Expected: A dedicated detail page loads for that product showing its name, image, price, rating, category, tags, the curator's review, and a list of key specs.
  - Observed: /product/philips-hue-starter-kit renders: category badge "Fitness", rating 4.4, name "Philips Hue Starter Kit", short review, "$179", image (loaded, naturalWidth > 0), tag chips lighting / smart-home / ambiance / automation, "Key Specifications" list (Bulbs Included – 3 Color Bulbs; Lumens – 800 per bulb; Color Range – 16 million colors; Hub – Bridge included; Compatibility – Alexa, Google, HomeKit) and the "My Review" section. /product/test-gadget shows the same structure with its own values.

- [X] FT-13: The detail page has a clear button linking to the external retailer
  - Action: On a product detail page, click the purchase button.
  - Expected: The link opens the product's external retailer URL (e.g., the saved affiliate URL) and the button is clearly labeled as a purchase/buy link.
  - Observed: The primary button renders "Buy Now" plus a lucide `external-link` icon, `href="https://example.com/philips-hue"` (the saved affiliate URL), `target="_blank"`, `rel="noopener noreferrer"` — Test Gadget's button correctly points at `https://example.com/test-gadget`.

## Constraint

- [ ] CS-01: A product cannot be saved with required fields missing
  - Action: Open the new/edit product form, leave the name, review, category, price, or purchase link blank, and submit.
  - Expected: Submission is blocked with a clear validation message identifying the missing field(s), and no new/updated entry is saved.
  - Bug Report:
    - Issue: Incomplete form validation — entries with missing required fields are saved
    - Actual: Only the name and the short description are validated. Blank name → blocked with toast "Please fill in all required fields" and no entry created; blank review → blocked, no entry created. But a product with a **blank purchase link (and blank price)** was created and appears in the listings as "QA Missing Link | Tech | $12", with its "Buy Now" link having an empty `href=""`. The category is a select that always submits a value (it cannot be cleared), and the price is not validated either. The message is also generic ("Please fill in all required fields") and does not identify which field is missing.

- [ ] CS-02: Price and rating accept only valid values
  - Action: Attempt to save a product with a negative price, a non-numeric price, or a rating outside the 1–5 range.
  - Expected: The entry is rejected with a validation message, and no product with an invalid price or rating is created or updated.
  - Bug Report:
    - Issue: No price/rating validation in the submit handler — invalid prices are stored and displayed
    - Actual: The submit handler validates only `name` and `shortDescription` (no price/rating checks). A product with price −50 was accepted and created, displaying as "QA Negative Price | Tech | -$50" on the listing. A non-numeric price ("abc") was accepted too: the browser refused to parse the value and it was silently stored as $0 ("QA NonNumeric Price | Tech | $0"). Only the rating range was incidentally enforced by the native `max="5"` input (rating 9 was blocked and not created, though via the browser's own bubble rather than an app message).

- [ ] CS-03: Only products marked as featured appear in the homepage featured section
  - Action: Compare the homepage featured section against the full product list.
  - Expected: Every product in the featured section has the featured flag, and every product with the featured flag appears in the featured section; non-featured products appear only in the regular listings.
  - Bug Report:
    - Issue: Flagged product absent from the featured section (section limited to 3 entries)
    - Actual: The section's three entries (Sony WH-1000XM5, Peloton Bike+, Dyson V15 Detect) all carry the featured flag, but Bowflex SelectTech 552 also had `featured = true` (badge shown in the admin panel and on the listing card) and never appeared in the section, which renders `featuredProducts.slice(0, 3)`. The section's "View all" link (`/products?featured=true`) is also broken — that URL shows all 10 products because the products page ignores the `featured` query parameter (non-featured items such as Test Gadget and Breville appear there too).

- [X] CS-04: Filtering and searching with no matches shows an empty result state rather than an error
  - Action: Search for a nonsense keyword (e.g., "zzzqqq") and apply a price range that no product satisfies.
  - Expected: A clear "no products found" message is displayed with no stale product cards, and no error/crash occurs.
  - Observed: Searching "zzzqqq" → "0 products found", 0 product cards and the message "No products match your filters. Try adjusting your search."; combining it with a minimum price of $2,000 gave the same clean empty state. No console error or crash occurred. (Caveat: a price range that no product satisfies cannot be produced on its own, because the range filter's maximum is fixed at $2,495 — see FT-09.)

## Interaction

- [X] IX-01: Changing a sort or filter immediately updates the visible result set
  - Action: On the product listing, change the sort option, then change the price filter, without reloading the page.
  - Expected: The displayed product list updates to reflect the new sort/filter selection each time, and the count of shown products changes accordingly.
  - Observed: Without any reload: sort "Price: Low to High" reordered the 10 cards; "Top Rated" reordered them by rating; the price slider minimum moved 0 → 200 and the header count changed "10 products found" → "8 products found"; the rating filter changed it to "9 products found"; the tag chip changed it to "2 products found"; search changed it to "1 product found" and then "0 products found".

- [X] IX-02: Active browse/filter selections are visibly indicated
  - Action: Select a category, a tag, and a sort option on the listing page.
  - Expected: Each chosen control (category link, tag chip, sort dropdown) is shown in an active/selected state distinct from unselected options.
  - Observed: The selected tag chip switches to `border-transparent bg-primary text-primary-foreground` while unselected chips stay `text-foreground`; the active nav category link uses `text-primary bg-primary/5` versus `text-muted-foreground` for the others; the sort dropdown marks the chosen option with `data-state="checked"` plus a visible check glyph in the indicator span (unselected options have an empty indicator) and the trigger displays the current value ("Newest", "Fitness", "4+ stars").

- [X] IX-03: The system confirms saves, feature toggles, and validation failures
  - Action: Save a new product, toggle the featured flag, and then submit an invalid form.
  - Expected: Successful actions show a clear success message, and the invalid submission shows an error/validation message that is visible on screen.
  - Observed: Creating a product showed the toast "Product created successfully"; saving an edit and toggling the featured flag showed "Product updated successfully"; submitting the form with a blank name/review showed the error toast "Please fill in all required fields". All appear in the on-screen notification region.

## Content

- [X] CT-01: Product cards display the core identifying and pricing information
  - Action: Inspect product cards across the homepage and the product listing.
  - Expected: Each card shows a product image, name, category, price, and rating, with no broken image placeholder or empty label.
  - Observed: All 10 listing cards (and the homepage cards) render a loaded `<img>` with the product name as `alt` (naturalWidth > 0 for every one — no broken-image placeholders), the name as a heading, a category badge (Tech / Fitness / Home), the formatted price ($149 … $2,495), the star rating (3.0 … 4.9) and a "Buy Now" link — no empty labels.

- [X] CT-02: Detail page content matches the curator's entry and the product's category, and the purchase link is identified as external/affiliate
  - Action: Open the detail page for a product and compare the displayed review, specs, price, and tags against the values saved for that product.
  - Expected: The displayed review text and specs match the saved entry exactly, the specs are relevant to the product's category, and the purchase button is clearly labeled as a link to an external retailer (affiliate purchase link).
  - Observed: /product/philips-hue-starter-kit displays exactly the saved values — "$179", rating 4.4, tags lighting / smart-home / ambiance / automation, "My Review: UPDATED FULL REVIEW: The Philips Hue starter kit was edited for QA purposes and now reads exactly like this text." and the five saved specs (Bulbs Included, Lumens, Color Range, Hub, Compatibility), which match the entry byte-for-byte. Specs are category-appropriate for products whose category matches (Philips Hue: lighting specs; Bowflex SelectTech 552: Weight Range, Increments, Dimensions, Sets Replaced, Warranty for Fitness; Test Gadget: Battery Life for Tech). The purchase button reads "Buy Now" with an external-link icon, targets the retailer URL in a new tab (`target="_blank"`, `rel="noopener noreferrer"`), and the site discloses "Affiliate links may earn us a commission."