# Test Result

**Application:** CuratedPicks — http://localhost:6001/ (Vite + React SPA, client‑side only)
**Method:** Playwright DOM‑only interaction (no screenshots). Filters/sorts/search driven via real clicks + keyboard; admin form driven via `fill`.
**Catalogue under test (in‑memory, 10 products):** 9 seeded products + `Anker Prime 20K Power Bank` (created during FT‑01). Test edits left on `Philips Hue Starter Kit` (price $219, category Fitness, featured, extra tags, revised review) and `Dyson V15 Detect` (featured cleared). Three throw‑away products created during CS‑01 were deleted (admin trash + `confirm()`), restoring the catalogue to 10.

---

## Functionality

- [X] **FT‑01 — Create product.** Filled every field of *Add Product* (name, category, price, rating, short description, full review, spec rows, tags, image URL, retailer link, featured) and submitted. Toast **“Product created successfully”** appeared; `Anker Prime 20K Power Bank` was added to the admin list, to the `/products` listing, to the homepage *Tech Gadgets* section, and it has a working detail page `/product/anker-prime-20k-power-bank` with specs, review and a *Buy Now* link to `https://example.com/anker-20k`. Catalogue count went 9 → 10.

- [X] **FT‑02 — Edit product.** Edited `Philips Hue Starter Kit` (price 199→219, category, review text, tags, featured switch). Toast **“Product updated successfully”**; the admin list, `/products` listing, homepage and detail page all reflected the new values, and re‑opening the edit form showed the saved values, not the old ones.

- [X] **FT‑03 — Categorise a product.** Reassigned `Philips Hue Starter Kit` from *Home* to *Fitness*. It immediately moved out of *Home Goods* and into *Fitness* in the listing, into the homepage *Fitness* section, and its detail page’s related list switched to *More in Fitness* (Peloton Bike+, Theragun Pro, Bowflex SelectTech 552). Category filter *Home Goods* returns exactly the two remaining Home products.

- [ ] **FT‑04 — Tag a product.**
  **Bug Report**
  - **Issue:** Tags are never surfaced on a product card. A tag saved through the admin form (`bluetooth, portable`) is stored and rendered only on the detail page — the listing cards, homepage cards and related‑product cards contain no tags at all, so the feature is invisible where the checklist expects it. Secondary defect: the tag filter chip list is a static export, so a tag that exists on a product (`bluetooth`, assigned to `Anker Prime 20K Power Bank` and `Philips Hue Starter Kit`) has no chip and cannot be selected as a filter.
  - **Actual:** Tag entry + persistence works (detail page of `Philips Hue Starter Kit` lists `lighting, smart-home, ambiance, automation, bluetooth, kitchen`; `Anker` lists `bluetooth, portable`), but the DOM of all 10 listing cards is only `Category | $Price | Name | short description | rating | Buy Now` — no tag element exists. The chip list contains 36 static tags (`ambiance … wireless`) with **no** `bluetooth` chip. Filtering by a tag that does have a chip still matches the saved data correctly (`kitchen` → exactly `Breville Barista Express` + `Philips Hue Starter Kit`).

- [X] **FT‑05 — Mark a product as featured.** The *Featured on homepage* switch (`role="switch"`) persisted: `Philips Hue Starter Kit` → `aria-checked="true"` and appeared in the homepage *Editor’s Top Picks*; `Dyson V15 Detect` was switched off and simultaneously disappeared from *Editor’s Top Picks* and lost its *Featured* badge in the listing. Only the 3 flagged products carry the badge.

- [X] **FT‑06 — Browse by category.** Homepage exposes *Tech Gadgets*, *Home Goods*, *Fitness* sections. The *All Categories* filter set to *Home Goods* returned **“2 products found”** — `Dyson V15 Detect` ($749) and `Breville Barista Express` ($699) — with every other product excluded.

- [X] **FT‑07 — Sort by price and rating.** *Price: High to Low* → 2495, 1999, 1299, 749, 699, 599, 549, 399, 219, 49.99. *Price: Low to High* → 49.99 … 2495. *Top Rated* → MacBook Pro 4.9, Sony 4.8, Dyson 4.7, Samsung 4.7, Peloton4.6, Bowflex 4.6, Anker 4.6, Theragun 4.5, Breville 4.5, Philips Hue 4.4. Ordering is correct in all three modes.

- [ ] **FT‑08 — Filter by price range and rating.**
  **Bug Report**
  - **Issue:** The price filter exposes only one handle. The slider is labelled *Price Range* with two displayed bounds (`$0 … $2495`), but the DOM contains exactly **one** `[role="slider"]` thumb (`aria-label="Minimum"`); there is no *Maximum* thumb, and the upper bound is pinned to the catalogue maximum ($2,495). A bounded range (e.g. $100–$500) therefore cannot be expressed.
  - **Actual:** Minimum works and filters correctly — thumb driven to `aria-valuenow="500"` (label `$500`) → **“7 products found”**: Samsung $1,299, MacBook $1,999, Bowflex $549, Theragun $599, Peloton $2,495, Breville $699, Dyson $749 (Anker $49.99, Sony $399, Philips Hue $219 correctly excluded). The displayed upper label stays `$2495` and no Maximum control exists to lower it. The rating half of the item passes: *4.5+ stars* → **“9 products found”**, excluding only `Philips Hue Starter Kit` (4.4).

- [X] **FT‑09 — Search by keyword.** Typing `Sony` in the search box → **“1 products found”** (`Sony WH-1000XM5` only); every other product was excluded. Matching covers name, short description and tags. *(Observation, not a failure: the full review body is not indexed — the query `Matter`, which occurs only inside the Philips Hue review, returns 0 results.)*

- [X] **FT‑10 — Detail page.** `/product/…` renders the product name, category, rating, price, **My Review** body, a **Key Specifications** table (e.g. Sony: Driver Size 30mm / Battery Life 30 hours / Weight 250g / Bluetooth 5.2 / Noise Cancelling Yes, Adaptive) and the **Buy Now** retailer button pointing at the stored affiliate URL.

---

## Constraint

- [ ] **CS‑01 — Required‑field and URL validation.**
  **Bug Report**
  - **Issue:** (a) The retailer/affiliate URL is not validated at all — neither blank nor malformed values are rejected. (b) The validation message is generic and does not identify the offending field, and no inline/field‑level error is rendered.
  - **Actual:**
    - Blank **name** → blocked, toast **“Please fill in all required fields”**, product count unchanged, form stays open. Same for a blank **short description**. But the toast names no field, there is no `[role="alert"]`/`aria-invalid`/inline error anywhere in the form (`inlineErr: []`), so the user cannot tell which field is invalid.
    - Blank **retailer URL** → **accepted**: product count 12 → 13, toast **“Product created successfully”**. The saved product had `affiliateLink = ""`, and its detail page rendered a *Buy Now* anchor with `href=""` (a dead link).
    - Invalid URL `not a link` → **accepted**: toast “Product created successfully”, the product was created with `affiliateLink = "not a link"`.
    - Source confirmation (`/src/pages/AdminPage.tsx`): `if (!formData.name || !formData.shortDescription) { toast.error('Please fill in all required fields'); return; }` — `affiliateLink`, `imageUrl`, `fullReview` and `price` are never validated. Category cannot be blank (the `<select>` always holds `tech|home|fitness`).

- [X] **CS‑02 — Filters never return non‑matching products.** Every filter was cross‑checked against the values saved in the admin form. Category *Home Goods* → 2 products, both category `home`; *4.5+ stars* → 9 products, all rating ≥ 4.5, `Philips Hue` (4.4) excluded; minimum price $500 → 7 products, all ≥ $500; tag `kitchen` → exactly `Breville Barista Express` + `Philips Hue Starter Kit`, the only two products carrying that tag. No filter ever leaked a product that did not match the saved field.

- [X] **CS‑03 — Empty search state and clear.** Searching `zzzznotfound` → **“0 products found”** with an empty grid and a **“Clear all filters”** button. Clicking it restored all 10 products, emptied the search input (`""`) and reset the price/rating/category/tag filters simultaneously.

---

## Interaction

- [X] **IX‑01 — Clicking a card opens the detail page.** Clicking the title link of the `Anker Prime 20K Power Bank` card (`a[href="/product/anker-prime-20k-power-bank"]`) routed to `/product/anker-prime-20k-power-bank` with `<h1>Anker Prime 20K Power Bank</h1>`. Same for the Philips Hue and Sony cards.

- [X] **IX‑02 — Retailer button opens the external link in a new tab.** *Buy Now* on the detail page has `href="https://example.com/anker-20k"`, `target="_blank"`, `rel="noopener noreferrer"`. Clicking it raised a real `popup` (new tab) while the SPA stayed on `/product/anker-prime-20k-power-bank`.

- [X] **IX‑03 — Edit form is pre‑filled and saving confirms.** All 10 edit forms opened with the saved values already populated — name, category (`select` value `tech`/`home`/`fitness`), price, rating, image URL, affiliate link, comma‑separated tags, short description, full review and every spec label/value row (e.g. `Philips Hue`: Bulbs Included / 3 Color Bulbs … Compatibility / Alexa, Google, HomeKit) — and the *Featured on homepage* switch pre‑set to `aria-checked="true|false"`. Saving shows the toast **“Product updated successfully”** and the updated values are reflected on the listing, homepage and detail page.

- [X] **IX‑04 — Featured indicator on the card.** Exactly the 3 featured products render a *Featured* badge in the card DOM (`Featured|Fitness|$2,495|Peloton Bike+…`, `Featured|Tech|$399|Sony WH-1000XM5…`, `Featured|Fitness|$219|Philips Hue Starter Kit…`); the other 7 cards contain no such badge.

---

## Content

- [X] **CT‑01 — Homepage featured section is exact.** The *Editor’s Top Picks* section contains exactly 3 cards — `Sony WH-1000XM5`, `Peloton Bike+`, `Philips Hue Starter Kit` — matching one‑for‑one the products whose admin switch is `aria-checked="true"` (no extras, none missing). When `Dyson V15 Detect` was un‑flagged it dropped out of the section, confirming the section is driven by the flag and not hard‑coded.

- [X] **CT‑02 — Detail page shows the correct, complete saved content.** `Philips Hue Starter Kit` detail page renders: category `Fitness`, rating `4.4`, price `$219`, the full saved review beginning **“UPDATED REVIEW: The Philips Hue Starter Kit is the most mature smart lighting system I have tested…”** (verbatim, untruncated), all 5 saved spec rows, all 6 saved tags, retailer link `https://example.com/philips-hue`, and the *Featured* badge. `Sony WH-1000XM5` renders `Tech`, `4.8`, `$399`, its 4 spec rows and its original review. `Anker Prime 20K Power Bank` renders `Tech`, `4.6`, `$49.99`, `Capacity / 20000mAh`, its review and its link. No placeholder, “TBD” or “Lorem ipsum” text and no cross‑contamination between products.

- [X] **CT‑03 — Category and tag labels match the assignments.** Every card’s category badge equals the category saved in the admin `select` (Sony/MacBook/Samsung/Anker → Tech, Peloton/Theragun/Bowflex/Philips Hue → Fitness, Dyson/Breville → Home), and the detail page header plus the *More in …* related list agree with the same value. Each detail page lists exactly the tags saved in the admin form (e.g. Philips Hue → `lighting, smart-home, ambiance, automation, bluetooth, kitchen`; Breville → `coffee, espresso, kitchen, appliance`; Anker → `bluetooth, portable`).
