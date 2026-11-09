# Test Checklist

## Functionality
- [ ] FT-01: Visitor can browse products by each category
  - Action: Open the homepage and click the "Tech Gadgets", "Home Goods", and "Fitness" category links one at a time.
  - Expected: Each page shows only products from that category, and the page heading matches the category name.
- [ ] FT-02: Homepage shows only products marked as featured
  - Action: Open the homepage and compare the featured section with the default products marked "Featured" in admin. Then mark one non-featured default product as featured, save, and reload the homepage.
  - Expected: Featured section lists exactly the products flagged Featured, and the newly flagged product appears.
- [ ] FT-03: Product detail page shows review, key specs, and tags
  - Action: Click the title of any default product on a category page.
  - Expected: Page shows the product name, the written review, a key specs list, and the product's tags.
- [ ] FT-04: Detail page button opens the external retailer link
  - Action: On a product detail page, click the "Buy at [Retailer]" button.
  - Expected: A new tab opens to the affiliate URL saved for that product in admin, with no error page.
- [ ] FT-05: Keyword search returns matching products
  - Action: Type a word from a default product's name into the search box and press Enter.
  - Expected: Results include that product and every other product whose name, review, or tags contain the word.
- [ ] FT-06: Sort options reorder products correctly
  - Action: Choose "Price: Low to High", then "Price: High to Low", then "Rating: High to Low" from the sort control.
  - Expected: The list order matches each option on every change.
- [ ] FT-07: Price range and minimum rating filters narrow results
  - Action: Set a price range (e.g., min and max around a default product's price) and a minimum rating of 4 stars.
  - Expected: Only products within the price range and rated 4 or higher remain listed.
- [ ] FT-08: Admin can create a product entry
  - Action: Use the admin create form to enter name, category, tags, price, rating, review, specs, and retailer link, then save.
  - Expected: Product saves, appears in its chosen category listing, and its detail page shows all entered values.
- [ ] FT-09: Admin can edit an existing product, including category and tags
  - Action: Open a default product in admin, change its review text, category, and one tag, then save and view its detail page.
  - Expected: Changes appear on the detail page and in the category listing, and the new tag is searchable.

## Constraint
- [ ] CS-01: Product cannot be saved with required fields empty
  - Action: Open the create form, leave Name, Category, Review, and Retailer Link blank, and click Save.
  - Expected: Save is blocked, each empty required field shows an error message, and no product is created.
- [ ] CS-02: Retailer link must be a valid web address
  - Action: Enter "not-a-link" in the Retailer Link field and click Save.
  - Expected: Save is blocked with a message stating the link must be a valid http or https URL.
- [ ] CS-03: Rating and price accept only valid values
  - Action: Enter rating "6" and price "-10" on the product form and click Save.
  - Expected: Save is blocked; rating must be 1 to 5 and price must be a positive number, with error messages shown for each.
- [ ] CS-04: Price range filter rejects minimum greater than maximum
  - Action: Enter 200 in the minimum price field and 50 in the maximum price field.
  - Expected: Filter is not applied to the list, and a message states the minimum cannot exceed the maximum.
- [ ] CS-05: Visitors cannot see or access admin controls
  - Action: Browse the homepage, a category page, and a product detail page as a visitor without logging in.
  - Expected: No create, edit, or featured-toggle controls are visible, and navigating directly to the admin area redirects to a login prompt.

## Interaction
- [ ] IX-01: Success message appears after saving a product
  - Action: Save a valid product in the admin create or edit form.
  - Expected: A success toast reading "Product saved" appears and the form closes or confirms the save.
- [ ] IX-02: Result count updates when search, sort, or filter changes
  - Action: Note the "Showing N products" count, then apply a keyword search and a price filter.
  - Expected: The count updates immediately to match the number of visible products after each change.
- [ ] IX-03: No-results message appears when nothing matches
  - Action: Search for "zzzzqqq" and press Enter.
  - Expected: The page shows "No products match your search" and a "Clear filters" button that restores the full list when clicked.

## Content
- [ ] CT-01: All product images load and are not broken
  - Action: Browse every category page and the homepage featured section.
  - Expected: Every product card and detail page shows a loaded image, with no broken image icons or blank placeholders.
- [ ] CT-02: Products and reviews match their category theme
  - Action: Review the product names, images, and review text under "Tech Gadgets", "Home Goods", and "Fitness".
  - Expected: Each product is relevant to its category, and each review text refers to the product it is shown with.
- [ ] CT-03: Price and rating formatting is consistent across pages
  - Action: Compare one product's price and star rating on the category listing and on its detail page.
  - Expected: Price shows a currency symbol with two decimals and the star rating matches the numeric value on both pages, with no placeholder text such as "Lorem" or "TBD".