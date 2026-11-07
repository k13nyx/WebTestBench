# Test Checklist

## Functionality
- [ ] FT-01: Owner can create a new product entry with name, category, review, price, rating, key specs, tags, and purchase link
  - Action: Open the admin/product management area, click "Add Product" / "New Entry", fill in all fields (name "Test Gadget", category "Tech Gadgets", brief review, price, rating, specs, at least one tag, retailer URL), and save.
  - Expected: Entry is saved and appears in the product listing with all entered values, and a success confirmation is shown.

- [ ] FT-02: Owner can edit an existing product entry and changes are reflected everywhere
  - Action: Open an existing product (from default data) in the editor, change its review text, price, and category, and save.
  - Expected: The updated review, price, and category are shown on the product listing card and on the product detail page; the old values are no longer displayed anywhere.

- [ ] FT-03: Owner can assign a product to a category (Tech Gadgets, Home Goods, Fitness) and visitors can browse by category
  - Action: Set an existing product's category to "Fitness", then as a visitor open the category browse view and select "Fitness".
  - Expected: Only products assigned to "Fitness" are listed; the edited product appears in that list and no longer appears in its previous category's list.

- [ ] FT-04: Owner can tag products and visitors can view products by tag
  - Action: Add a tag (e.g., "wireless") to a product, then select that tag in the tag filter/browse view.
  - Expected: The tagged product appears under the tag, and only products carrying that tag are shown.

- [ ] FT-05: Owner can mark an item as featured and featured items appear on the homepage
  - Action: Mark an existing product as "Featured", save, then open the homepage.
  - Expected: The marked product is displayed in the homepage featured section with its name, image, price, and rating.

- [ ] FT-06: Owner can un-feature an item and it is removed from the homepage featured section
  - Action: Unmark the previously featured product, save, then reload the homepage.
  - Expected: The product no longer appears in the homepage featured section while remaining available in the main product listings.

- [ ] FT-07: Visitor can sort products by price (ascending and descending)
  - Action: On the product listing, apply the price sort in both ascending and descending order.
  - Expected: Products are reordered so prices run low→high for ascending and high→low for descending, with the displayed price matching the list order.

- [ ] FT-08: Visitor can sort products by rating (highest and lowest)
  - Action: Apply the rating sort in both directions on the product listing.
  - Expected: Products are reordered by their star rating accordingly, with the displayed rating matching the list order.

- [ ] FT-09: Visitor can filter products by a price range
  - Action: Enter a minimum and maximum price (e.g., 50–200) in the price range filter and apply it.
  - Expected: Only products whose price falls within the range are shown; products below the minimum or above the maximum are excluded.

- [ ] FT-10: Visitor can filter products by minimum rating
  - Action: Set the rating filter to 4 stars and apply it.
  - Expected: Only products with a rating of 4 or higher are shown; products rated 3 or lower are excluded.

- [ ] FT-11: Visitor can search for products by keyword
  - Action: Enter a keyword that appears in a default product's name, review, or tag into the search field and submit.
  - Expected: Matching products are listed and each match contains the searched keyword; non-matching products are not shown.

- [ ] FT-12: Each product has its own detail page showing the review and key specs
  - Action: Click the name or card of any product from a listing or the homepage.
  - Expected: A dedicated detail page loads for that product showing its name, image, price, rating, category, tags, the curator's review, and a list of key specs.

- [ ] FT-13: The detail page has a clear button linking to the external retailer
  - Action: On a product detail page, click the purchase button.
  - Expected: The link opens the product's external retailer URL (e.g., the saved affiliate URL) and the button is clearly labeled as a purchase/buy link.

## Constraint
- [ ] CS-01: A product cannot be saved with required fields missing
  - Action: Open the new/edit product form, leave the name, review, category, price, or purchase link blank, and submit.
  - Expected: Submission is blocked with a clear validation message identifying the missing field(s), and no new/updated entry is saved.

- [ ] CS-02: Price and rating accept only valid values
  - Action: Attempt to save a product with a negative price, a non-numeric price, or a rating outside the 1–5 range.
  - Expected: The entry is rejected with a validation message, and no product with an invalid price or rating is created or updated.

- [ ] CS-03: Only products marked as featured appear in the homepage featured section
  - Action: Compare the homepage featured section against the full product list.
  - Expected: Every product in the featured section has the featured flag, and every product with the featured flag appears in the featured section; non-featured products appear only in the regular listings.

- [ ] CS-04: Filtering and searching with no matches shows an empty result state rather than an error
  - Action: Search for a nonsense keyword (e.g., "zzzqqq") and apply a price range that no product satisfies.
  - Expected: A clear "no products found" message is displayed with no stale product cards, and no error/crash occurs.

## Interaction
- [ ] IX-01: Changing a sort or filter immediately updates the visible result set
  - Action: On the product listing, change the sort option, then change the price filter, without reloading the page.
  - Expected: The displayed product list updates to reflect the new sort/filter selection each time, and the count of shown products changes accordingly.

- [ ] IX-02: Active browse/filter selections are visibly indicated
  - Action: Select a category, a tag, and a sort option on the listing page.
  - Expected: Each chosen control (category link, tag chip, sort dropdown) is shown in an active/selected state distinct from unselected options.

- [ ] IX-03: The system confirms saves, feature toggles, and validation failures
  - Action: Save a new product, toggle the featured flag, and then submit an invalid form.
  - Expected: Successful actions show a clear success message, and the invalid submission shows an error/validation message that is visible on screen.

## Content
- [ ] CT-01: Product cards display the core identifying and pricing information
  - Action: Inspect product cards across the homepage and the product listing.
  - Expected: Each card shows a product image, name, category, price, and rating, with no broken image placeholder or empty label.

- [ ] CT-02: Detail page content matches the curator's entry and the product's category, and the purchase link is identified as external/affiliate
  - Action: Open the detail page for a product and compare the displayed review, specs, price, and tags against the values saved for that product.
  - Expected: The displayed review text and specs match the saved entry exactly, the specs are relevant to the product's category, and the purchase button is clearly labeled as a link to an external retailer (affiliate purchase link).