# Test Checklist

## Functionality
- [ ] FT-01: Product entries can be created with review, category, tags, key specifications, price, rating, and retailer URL.
  - Action: Open **Add Product**, complete all product fields with valid values, and select **Save Product**.
  - Expected: The product is saved and appears in the product catalog with the entered information.

- [ ] FT-02: Existing product entries can be edited.
  - Action: Open an existing product, select **Edit Product**, change its review text, and save.
  - Expected: The updated review appears on the product listing and detail page.

- [ ] FT-03: Products can be assigned to the Tech Gadgets, Home Goods, or Fitness Products category.
  - Action: Edit an existing product and select each available category one at a time, saving after each change.
  - Expected: The product appears under the selected category and is absent from the other category views.

- [ ] FT-04: Products can be assigned one or more descriptive tags.
  - Action: Edit an existing product, add a valid tag, and save.
  - Expected: The tag is displayed with the product and can be used to identify or filter the product.

- [ ] FT-05: Products can be marked as featured on the homepage.
  - Action: Mark an existing product as **Featured** and save.
  - Expected: The product appears in the homepage featured-product section.

- [ ] FT-06: Visitors can browse products by category.
  - Action: Select **Tech Gadgets**, **Home Goods**, and **Fitness Products** from the category navigation.
  - Expected: Each category page displays only products assigned to that category.

- [ ] FT-07: Visitors can sort products by available sort options.
  - Action: Open the product catalog and select each available sort option, such as price or rating.
  - Expected: Product cards reorder according to the selected sort rule.

- [ ] FT-08: Visitors can filter products by price range and rating.
  - Action: Apply a price-range filter and a rating filter using values represented by the default products.
  - Expected: The catalog displays only products meeting all selected filter criteria.

- [ ] FT-09: Visitors can search for products by keyword.
  - Action: Enter a keyword appearing in an existing product name or review into the **Search** field and submit the search.
  - Expected: Results include the matching product and exclude products with no matching searchable content.

- [ ] FT-10: Each product has a dedicated detail page.
  - Action: Select an existing product card or product title.
  - Expected: A detail page opens for that product and displays its product name, review, key specifications, and retailer purchase link.

## Constraint
- [ ] CS-01: Product entries cannot be saved without required product information.
  - Action: Open **Add Product** or **Edit Product**, clear a required field, and select **Save Product**.
  - Expected: The product is not saved and the missing field is identified with a validation message.

- [ ] CS-02: A product cannot be assigned an unsupported category.
  - Action: Open the product category control and inspect the available category choices.
  - Expected: Only **Tech Gadgets**, **Home Goods**, and **Fitness Products** can be selected.

- [ ] CS-03: Applying filters does not display products outside the selected criteria.
  - Action: Apply a price or rating filter whose range excludes at least one default product.
  - Expected: Every displayed product satisfies the selected filter, and excluded products are not shown.

- [ ] CS-04: A search with no matching keyword returns no unrelated products.
  - Action: Search for a unique keyword that does not appear in any default product.
  - Expected: The results area shows a clear **No products found** state and no product cards.

## Interaction
- [ ] IX-01: Saving a product provides clear confirmation and refreshes displayed data.
  - Action: Save a valid edit to an existing product.
  - Expected: A **Product saved** confirmation appears, and the updated product data is visible without showing stale values.

- [ ] IX-02: Category, sort, and filter controls update results without requiring unrelated navigation.
  - Action: Change a category, sort option, and filter while viewing the catalog.
  - Expected: Results update after each selection and the active control state clearly reflects the current selection.

- [ ] IX-03: Clearing search and filters restores the complete applicable product list.
  - Action: Enter a search term, apply a filter, then select **Clear Search** or **Clear Filters**.
  - Expected: The corresponding restriction is removed and all applicable products are displayed again.

- [ ] IX-04: The retailer purchase button opens the external retailer destination.
  - Action: On a product detail page, select the **Buy at Retailer** button.
  - Expected: The retailer URL opens in a new browser tab or window, and the destination is different from the product website.

## Content
- [ ] CT-01: Product cards display accurate, relevant catalog information.
  - Action: Compare several default product cards with their detail pages.
  - Expected: Each card shows the correct product name, category, rating, price, and brief review summary.

- [ ] CT-02: Product detail pages contain the required editorial and specification content.
  - Action: Open several default product detail pages.
  - Expected: Each page contains the curator’s review, readable key specifications, and a clearly identifiable affiliate purchase link.