# Test Result

Run against http://localhost:6001/ with about 87 of the 100 allowed tool calls. Only the 9 seeded products and the homepage featured section were verified after reload. Writes from the admin panel (create, edit, featured toggle) showed success toasts but did not persist; details are in the notes below.

## Functionality

- [X] FT-01: Visitor can browse products by each category
  - Action: Open the homepage and click the "Tech Gadgets", "Home Goods", and "Fitness" category links one at a time.
  - Expected: Each page shows only products from that category, and the page heading matches the category name.
- [ ] FT-02: Homepage shows only products marked as featured
  - Action: Open the homepage and compare the featured section with the default products marked "Featured" in admin. Then mark one non-featured default product as featured, save, and reload the homepage.
  - Expected: Featured section lists exactly the products flagged Featured, and the newly flagged product appears.
  - Bug Report:
    - Issue: Featured flag not persisted after save and reload
    - Actual: Turned on "Featured on homepage" for Theragun Pro and saved; toast read "Product updated successfully". After reloading the homepage, "Editor's Top Picks" still lists only Sony WH-1000XM5, Peloton Bike+, and Dyson V15 Detect. After reloading admin, Theragun Pro shows no Featured badge. The baseline check passed: admin flags Sony, Peloton, and Dyson, matching the homepage.
- [X] FT-03: Product detail page shows review, key specs, and tags
  - Action: Click the title of any default product on a category page.
  - Expected: Page shows the product name, the written review, a key specs list, and the product's tags.
- [X] FT-04: Detail page button opens the external retailer link
  - Action: On a product detail page, click the "Buy at [Retailer]" button.
  - Expected: A new tab opens to the affiliate URL saved for that product in admin, with no error page.
- [X] FT-05: Keyword search returns matching products
  - Action: Type a word from a default product's name into the search box and press Enter.
  - Expected: Results include that product and every other product whose name, review, or tags contain the word.
- [ ] FT-06: Sort options reorder products correctly
  - Action: Choose "Price: Low to High", then "Price: High to Low", then "Rating: High to Low" from the sort control.
  - Expected: The list order matches each option on every change.
  - Bug Report:
    - Issue: Missing sort option "Rating: High to Low"
    - Actual: Sort menu offers Newest, Top Rated, Price: Low to High, and Price: High to Low. There is no "Rating: High to Low". Price Low to High ($199 → $2,495) and Price High to Low ($2,495 → $199) are correct. "Top Rated" orders 4.9 → 4.4, which matches the intent but not the stated label.
- [ ] FT-07: Price range and minimum rating filters narrow results
  - Action: Set a price range (e.g., min and max around a default product's price) and a minimum rating of 4 stars.
  - Expected: Only products within the price range and rated 4 or higher remain listed.
  - Bug Report:
    - Issue: Price range filter cannot be set
    - Actual: The rating filter works: "4+ stars" keeps all 9, and "4.5+ stars" narrows to 8 (Philips Hue removed). The price range is a single slider labeled "Minimum" with no maximum handle. Its value stayed at $0 after clicking the track and after End and ArrowRight key presses, and the list did not change.
- [ ] FT-08: Admin can create a product entry
  - Action: Use the admin create form to enter name, category, tags, price, rating, review, specs, and retailer link, then save.
  - Expected: Product saves, appears in its chosen category listing, and its detail page shows all entered values.
  - Bug Report:
    - Issue: Created product does not appear in its category
    - Actual: Created "QA FT08 Lamp" (Home Goods, $250, 4.2, tags, one spec, valid link). Toast read "Product created successfully" and the card appeared in admin. /category/home still lists only Breville, Philips, and Dyson. After reload, /products shows the original 9 products and the new product is absent. The detail page could not be reached.
- [ ] FT-09: Admin can edit an existing product, including category and tags
  - Action: Open a default product in admin, change its review text, category, and one tag, then save and view its detail page.
  - Expected: Changes appear on the detail page and in the category listing, and the new tag is searchable.
  - Bug Report:
    - Issue: Edits not persisted
    - Actual: Bowflex SelectTech 552 was edited (review text, category Fitness → Home Goods, tag "dumbbells" → "qaedit"). Toast read "Product updated successfully". After reload, the detail page still shows the original review, the Fitness category, and the original tags. "qaedit" is not present and is not searchable.

## Constraint

- [ ] CS-01: Product cannot be saved with required fields empty
  - Action: Open the create form, leave Name, Category, Review, and Retailer Link blank, and click Save.
  - Expected: Save is blocked, each empty required field shows an error message, and no product is created.
  - Bug Report:
    - Issue: No per-field error messages
    - Actual: Save was blocked and nothing was created, but the only feedback was one toast, "Please fill in all required fields". No field shows an error message or invalid state. Category cannot be left blank because it defaults to "Tech Gadgets". "Full Review" and "Affiliate Link" are not marked required, unlike "Product Name" and "Short Description".
- [ ] CS-02: Retailer link must be a valid web address
  - Action: Enter "not-a-link" in the Retailer Link field and click Save.
  - Expected: Save is blocked with a message stating the link must be a valid http or https URL.
  - Bug Report:
    - Issue: Invalid retailer link accepted
    - Actual: "not-a-link" was saved. Toast read "Product created successfully" and card "QA Test Product" appeared in admin. No http/https message was shown. The product did not persist across reload.
- [ ] CS-03: Rating and price accept only valid values
  - Action: Enter rating "6" and price "-10" on the product form and click Save.
  - Expected: Save is blocked; rating must be 1 to 5 and price must be a positive number, with error messages shown for each.
  - Bug Report:
    - Issue: Price not validated; no app error messages
    - Actual: Rating 6 was blocked only by the browser's native check ("Value must be less than or equal to 5."), with no app message. Price -10 passed validation (`checkValidity()` returned true, no min attribute), so no price error appears.
- [ ] CS-04: Price range filter rejects minimum greater than maximum
  - Action: Enter 200 in the minimum price field and 50 in the maximum price field.
  - Expected: Filter is not applied to the list, and a message states the minimum cannot exceed the maximum.
  - Bug Report:
    - Issue: No minimum or maximum price inputs exist
    - Actual: The Filters panel has only a slider with no text fields, so the values 200 and 50 cannot be entered. No message appears. The slider is also non-functional (see FT-07).
- [ ] CS-05: Visitors cannot see or access admin controls
  - Action: Browse the homepage, a category page, and a product detail page as a visitor without logging in.
  - Expected: No create, edit, or featured-toggle controls are visible, and navigating directly to the admin area redirects to a login prompt.
  - Bug Report:
    - Issue: Admin area accessible without login
    - Actual: Navigating to /admin loaded the Admin Panel directly, with no login prompt, showing "Add Product" and Edit and delete controls on every product. Homepage, category, and detail pages showed no edit or featured controls (this part passed).

## Interaction

- [ ] IX-01: Success message appears after saving a product
  - Action: Save a valid product in the admin create or edit form.
  - Expected: A success toast reading "Product saved" appears and the form closes or confirms the save.
  - Bug Report:
    - Issue: Success toast text mismatch
    - Actual: Edit save shows "Product updated successfully" and create save shows "Product created successfully". Neither reads "Product saved". The form closes on success.
- [ ] IX-02: Result count updates when search, sort, or filter changes
  - Action: Note the "Showing N products" count, then apply a keyword search and a price filter.
  - Expected: The count updates immediately to match the number of visible products after each change.
  - Bug Report:
    - Issue: Count label mismatch and price filter not applicable
    - Actual: No "Showing N products" text exists. The count reads "N products found" and updates correctly for search (1 result for "Peloton") and the rating filter (9 → 8). The price filter cannot be applied, so that half of the check cannot be completed.
- [ ] IX-03: No-results message appears when nothing matches
  - Action: Search for "zzzzqqq" and press Enter.
  - Expected: The page shows "No products match your search" and a "Clear filters" button that restores the full list when clicked.
  - Bug Report:
    - Issue: Wrong no-results message and missing "Clear filters" button
    - Actual: The page shows "0 products found" and "No products match your filters. Try adjusting your search." No "Clear filters" button is present in the DOM.

## Content

- [X] CT-01: All product images load and are not broken
  - Action: Browse every category page and the homepage featured section.
  - Expected: Every product card and detail page shows a loaded image, with no broken image icons or blank placeholders.
- [X] CT-02: Products and reviews match their category theme
  - Action: Review the product names, images, and review text under "Tech Gadgets", "Home Goods", and "Fitness".
  - Expected: Each product is relevant to its category, and each review text refers to the product it is shown with.
- [ ] CT-03: Price and rating formatting is consistent across pages
  - Action: Compare one product's price and star rating on the category listing and on its detail page.
  - Expected: Price shows a currency symbol with two decimals and the star rating matches the numeric value on both pages, with no placeholder text such as "Lorem" or "TBD".
  - Bug Report:
    - Issue: Price lacks two decimal places
    - Actual: Prices render as "$399", "$1,999", and "$2,495" with no decimals. Ratings match between listing and detail pages (for example, 4.8 on both), and no placeholder text was found on any detail page.

## Notes

- **Writes do not persist.** Create, edit, and featured changes all showed success toasts, but after reload the public catalog and admin list showed only the original 9 products with original values. Test artifacts ("QA Test Product", "QA FT08 Lamp", the Theragun featured flag, and the Bowflex edit) were session-only and do not appear on reload.
- **FT-04 label:** the button reads "Buy Now", not "Buy at [Retailer]". The Expected behavior (new tab to the saved affiliate URL, no error page) was met, so I marked it passed.
- **Not tested:** tag-based search (FT-09's "searchable" check could not run because the tag edit did not persist).