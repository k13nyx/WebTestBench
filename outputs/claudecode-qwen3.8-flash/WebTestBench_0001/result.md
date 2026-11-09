Testing complete — no JavaScript console errors observed throughout. Below is the full checklist with final statuses.

# Test Result

## Functionality

- [X] FT-01: Curator can create a new product entry with full details
  - Action: Opened /admin "Add Product", filled name ("Anker Nano Power Bank"), category (Tech Gadgets), price (29), rating (4.3), short description, full review, key spec (Battery / 10,000mAh, 20W PD), affiliate URL, tags; submitted.
  - Expected: Save succeeds and the new product appears in the product listing and has its own detail page with all entered values.
  - Verified: "Product created successfully" toast; card appeared in admin and All Products listing; detail page /product/anker-nano-power-bank showed all entered values. (Note: created data does not survive page reload — see CS-04.)

- [X] FT-02: Curator can edit an existing product
  - Action: Edited Sony WH-1000XM5 (Tech Gadgets), changed price $399→$429 and rewrote review text, saved ("Save Changes").
  - Expected: The product detail page and listing card both display the new review text and new price; no duplicate entry is created.
  - Verified: Listing card showed "$429" + "…now tuned even better after our long-term review."; detail page showed $429, new excerpt, new "My Review" text; listing still had exactly one Sony entry.

- [X] FT-03: Each product can be categorized into one of the three curations
  - Action: Edited Apple MacBook Pro 14", changed category Tech Gadgets → Home Goods, saved, then visited both category pages.
  - Expected: The product now appears under Home Goods and no longer appears under its previous category page.
  - Verified: /category/home listed "Apple MacBook Pro 14\"" (+3 defaults); /category/tech listed only Samsung + Sony.

- [ ] FT-04: Each product can be tagged
  - Action: Added tags "budget, best-of-2026" to a product and saved; opened its detail page; clicked the "budget" tag chip.
  - Expected: Tags are displayed on the product, and clicking a tag shows a filtered list containing every product carrying that tag.
  - Bug Report:
    - Issue: Non-functional tag chips / missing tag-filtered list
    - Actual: Tags ARE displayed on the detail page, but the chips are plain `<span>` elements (cursor: auto, no link/button/role, no href); clicking "budget" did nothing (URL stayed /product/macbook-pro-14). No tag-filtered list is reachable. Additionally, the new tags "budget"/"best-of-2026" never appeared in the Filters panel's "Tags" chip list (only the 40 seed tags were listed even after the tagged product existed).

- [ ] FT-05: Curator can mark an item as featured on the homepage
  - Action: Toggled "Featured" ON for Bowflex SelectTech 552 (default product) via admin edit form, saved ("Product updated successfully", admin card showed Featured badge), then loaded the homepage.
  - Expected: The product appears in the homepage featured section.
  - Bug Report:
    - Issue: Featured flag not honored on homepage
    - Actual: Homepage "Editor's Top Picks" still listed only Sony WH-1000XM5, Peloton Bike+, Dyson V15 Detect — the newly featured Bowflex never appeared (section appears capped to 3 items in seed insertion order). It only showed after un-featuring Peloton. Related: the "View all" link /products?featured=true ignores the featured filter entirely and lists ALL 9 products, featured or not.

- [X] FT-06: Visitors can browse products by category
  - Action: Selected Tech, Home Goods, Fitness from the navigation in turn.
  - Expected: Each category page loads and lists only default products belonging to that category.
  - Verified: /category/tech → Sony, MacBook, Samsung (all Tech); /category/home → Dyson, Philips Hue, Breville (all Home); /category/fitness → Bowflex, Theragun, Peloton (all Fitness). No cross-category leakage.

- [ ] FT-07: Visitors can filter products by price range
  - Action: Opened Filters on All Products and attempted a price-range filter (min/max).
  - Expected: Only products priced within the selected range remain visible; all others disappear from the results.
  - Bug Report:
    - Issue: Missing maximum-price control / incomplete price-range filter
    - Actual: The "Price Range" filter is a single Radix slider thumb labeled "Minimum" (aria-valuemax 2495); there is NO maximum input, so "min 0 / max 50" cannot be applied — only a lower bound exists (verified: min=$1000 correctly left only $1,299/$1,999/$2,495 items). The thumb also ignores keyboard adjustment (End/Home produce no change), and one transient state was observed where products were silently hidden from the grid while the slider/labels still read $0–$2,495 (displayed range not reflecting the applied filter).

- [X] FT-08: Visitors can sort products by rating
  - Action: Chose the rating sort ("Top Rated", the app's Rating-High-to-Low option) on the All Products listing.
  - Expected: Result cards re-order so that displayed rating values are non-increasing down the list.
  - Verified: Ratings in order: 4.9, 4.8, 4.7, 4.7, 4.6, 4.6, 4.5, 4.5, 4.4, 4.3 — strictly non-increasing; the selection also displayed as the sort control's value.

- [X] FT-09: Visitors can search by keyword
  - Action: Typed "espresso" (keyword in Breville Barista Express's name/description; "earbuds" matches no default product) into site search and submitted.
  - Expected: The results page lists the matching product(s) and excludes non-matching products.
  - Verified: Navigated to /products?search=espresso → "1 product found", only "Breville Barista Express"; all others excluded.

- [X] FT-10: Product detail page shows review, specs, and the retailer button
  - Action: Clicked a product card from the Home Goods category page (Apple MacBook Pro 14") to open its detail page.
  - Expected: The detail page displays the full written review, the key specifications list, and one clearly labeled purchase button (e.g., "Buy at Retailer").
  - Verified: Detail page shows "My Review" full paragraph, "Key Specifications" (Chip Apple M3 Pro, 18GB Unified, 512GB SSD, 14.2\" Liquid Retina XDR, Up to 17 hours), and a single clearly labeled "Buy Now" button. Same structure confirmed on Sony and Anker detail pages.

- [X] FT-11: Purchase button links to the external retailer
  - Action: On Sony's detail page, inspected and clicked the "Buy Now" button.
  - Expected: The button points to that product's stored affiliate URL (correct domain visible in status bar) and navigating leaves this site for that retailer page.
  - Verified: href = https://example.com/sony-xm5 (matches stored affiliate URL), target="_blank"; clicking opened a new tab at https://example.com/sony-xm5 ("Example Domain"), leaving this site; original tab preserved.

## Constraint

- [ ] CS-01: Product cannot be saved with missing required fields
  - Action: In "Add Product", left name and affiliate URL empty and clicked Create Product.
  - Expected: The save is blocked, an inline validation message identifies the empty required field(s), and no incomplete product appears in the listing.
  - Bug Report:
    - Issue: Missing inline field-level validation
    - Actual: Save was correctly blocked (no incomplete product created; form stayed open) and a toast appeared, but the only message was the generic "Please fill in all required fields" — no inline message identifying WHICH fields are empty, and no input is marked (no aria-invalid, no per-field error text next to Name/Short Description).

- [ ] CS-02: Affiliate link must be a valid external URL
  - Action: Created a product with affiliate link value "notaurl".
  - Expected: The value is rejected with a validation error, or the product's purchase button is not rendered; no dead relative link is produced.
  - Bug Report:
    - Issue: Unvalidated affiliate URL / dead relative link
    - Actual: "notaurl" was accepted ("Product created successfully", no validation error). The product's "Buy Now" button rendered with href="notaurl", which resolves to the on-site dead link http://localhost:6001/product/notaurl instead of an external retailer.

- [ ] CS-03: Price-range filter with min greater than max is rejected
  - Action: Attempted to set the price filter to min 200 / max 50 on the listing page.
  - Expected: The app either shows a range error or resets the filter; it never returns a full unfiltered product list as if the filter succeeded.
  - Bug Report:
    - Issue: Filter control missing / test not executable
    - Actual: The Filters panel provides only a single "Minimum" price slider (no maximum-price input anywhere in the UI), so min 200 / max 50 cannot be entered and the defined validation behavior cannot be exercised. During testing the single slider also exhibited state inconsistencies (list filtered while displayed range labels still showed $0), so reliable rejection behavior could not be observed.

- [ ] CS-04: Only featured products appear on the homepage featured section
  - Action: Toggled "Featured" OFF for Peloton Bike+ (currently in the homepage featured section), saved, confirmed client-side removal (grid showed Sony/Dyson/Bowflex), then RELOADED the homepage.
  - Expected: The product is removed from the featured section, and the section contains only products marked featured (no empty placeholder cards).
  - Bug Report:
    - Issue: State lost on reload (featured change not persisted)
    - Actual: Immediately after reload, "Editor's Top Picks" again showed Sony, Peloton Bike+ (re-marked "Featured") and Dyson — the un-featuring was reverted. The app stores all data in memory with no persistence (no localStorage/backend): every reload restores seed data, and edits even silently reverted mid-session after filter-clearing (the newly created Anker product vanished from the 10→9 listing without any delete action).

## Interaction

- [X] IX-01: Confirmation shown after creating or editing a product
  - Action: Saved a new product, then saved edits to Sony, MacBook, and Bowflex.
  - Expected: A success message/toast (e.g., "Product saved") appears after each save and the view returns to the listing/detail without a manual reload.
  - Verified: Toast "Product created successfully" after create; "Product updated successfully" after each edit; the form auto-closed and returned to the admin listing immediately with no manual reload.

- [X] IX-02: Featured control reflects current state
  - Action: Opened the featured switch for featured products (Sony, Peloton) and a non-featured product (Bowflex) in the edit form; toggled and saved.
  - Expected: The control shows ON for featured products and OFF for non-featured ones, and toggling it updates instantly (badge/label change) without leaving the page.
  - Verified: switch aria-checked="true" for Sony/Peloton, "false" for Bowflex; toggling changed state instantly; after save the "Featured" label appeared on the Bowflex admin card and disappeared from Peloton's without leaving/reloading the page.

- [X] IX-03: Active filters and sort are visibly indicated and can be cleared
  - Action: Applied category Tech Gadgets + price min $500 + "Top Rated" sort together, then clicked the clear control.
  - Expected: The applied controls show their current values (selected category, range, sort option), and clearing them restores the full unfiltered, default-order product list.
  - Verified: With all three active, controls read "Tech Gadgets", "Top Rated", "$500"/"$2495" (2 products shown, ratings non-increasing); a "Clear all filters" button appeared while filters were active and restored "10 products found", "All Categories", "Newest", slider at $0.

- [X] IX-04: Empty result state for search and filters
  - Action: Searched for "zzzqqq" (no match); separately applied Home Goods + min $1,000 price filter (no products qualify).
  - Expected: A "no products found" message with guidance to adjust/clear filters is displayed; the page shows no broken cards and no JavaScript error.
  - Verified: Both scenarios showed "0 products found" + message "No products match your filters. Try adjusting your search."; zero article cards rendered and no console errors were logged.

## Content

- [X] CT-01: All three categories are populated with relevant default products
  - Action: Opened the Tech Gadgets, Home Goods, and Fitness Products category pages.
  - Expected: Each page lists at least one default product whose name and description genuinely belong to that theme (no cross-category mismatches, no lorem ipsum or "sample text").
  - Verified: Tech → Sony WH-1000XM5, MacBook Pro, Galaxy S24 Ultra; Home → Dyson V15, Philips Hue, Breville espresso machine; Fitness → Peloton, Theragun, Bowflex — all on-theme with real descriptions; no lorem/placeholder text found on any page.

- [X] CT-02: Card data matches detail-page data
  - Action: Compared Sony's listing card (name, $429, 4.8, excerpt "Best-in-class ANC headphones, now tuned even better…") against its detail page.
  - Expected: All shared values are identical; the detail page adds the full review and key specs rather than repeating placeholder content.
  - Verified: Name, price $429, rating 4.8, and excerpt identical on both; detail page additionally shows the unique "My Review" long text and 6 populated "Key Specifications" rows. Same correspondence confirmed for MacBook.

- [X] CT-03: Product images and homepage copy are intact and on-theme
  - Action: Browsed the homepage, each category page, and 3 product detail pages (Sony, MacBook, Anker), checking images (naturalWidth) and text blocks.
  - Expected: No broken/missing images or empty spec sections; hero and section copy describes curated gadget/home/fitness recommendations with affiliate links, with no unrelated placeholder text.
  - Verified: 0 broken images (all loaded, every img had a product-name alt), spec sections populated on all 3 detail pages, hero copy "Discover Products Worth Your Money — Curated tech gadgets, home essentials, and fitness gear — personally tested and honestly reviewed", "Hand-picked recommendations" badge, and footer "Affiliate links may earn us a commission" — all on-theme, no placeholder text.

**Summary: 15 PASS / 7 FAIL** (FT-04, FT-05, FT-07, CS-01, CS-02, CS-03, CS-04). The dominant systemic defect is lack of data persistence (all curator changes revert on reload; new products/tags unstable in-session), plus an incomplete price-range filter (minimum-only) and non-clickable tags.