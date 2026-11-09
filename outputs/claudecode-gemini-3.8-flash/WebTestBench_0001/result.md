# Test Result

## Functionality
- [X] FT-01: Create a new product entry with category, tags, and affiliate link
  - Action: Navigate to the product creation form, fill in "Product Title", "Category", "Tags", "Review", "Key Specs", "Price", and "Affiliate Link", then click "Save Product".
  - Expected: The product is saved successfully and appears in the product inventory list.
- [X] FT-02: Edit an existing product entry
  - Action: Click "Edit" on an existing product in the management list, update the "Review" text and "Price", then click "Update Product".
  - Expected: The updated review and price are saved and reflected on the product listing and detail page.
- [X] FT-03: Mark a product entry as featured
  - Action: Open an existing product in the editor, check the "Featured on Homepage" checkbox, and click "Update Product".
  - Expected: The product appears in the "Featured Products" section on the homepage.
- [X] FT-04: Browse products by category
  - Action: Click on the "Tech Gadgets" category tab in the navigation menu.
  - Expected: The product grid refreshes to show only products assigned to the "Tech Gadgets" category.
- [X] FT-05: Search products by keyword
  - Action: Enter an existing product keyword into the search bar and press Enter or click the "Search" button.
  - Expected: The product list displays only items containing the keyword in their title, tags, or description.
- [ ] FT-06: Filter products by price range
  - Action: Enter values into the "Min Price" and "Max Price" filter fields and click "Apply Filter".
  - Expected: The catalog updates to show only products whose prices fall within the specified range.
  - Bug Report:
    - Issue: Missing Form Controls / Filter Inputs
    - Actual: The filters panel does not provide "Min Price" or "Max Price" input fields or an "Apply Filter" button; price filtering is rendered only as a slider component without discrete input fields or an apply action.
- [X] FT-07: Sort products by rating
  - Action: Select "Highest Rating" from the "Sort By" dropdown menu.
  - Expected: The displayed products reorder descending from highest rating to lowest rating.
- [X] FT-08: Navigate to product detail page
  - Action: Click on a product card or "Read Review" link from the catalog grid.
  - Expected: The browser navigates to the dedicated product detail page showing the product title, review, key specs, and purchase button.
- [X] FT-09: Navigate to external retailer via affiliate link
  - Action: Click the "Buy on Retailer" button on a product detail page.
  - Expected: The browser redirects to the external retailer URL configured in the product's affiliate link.

## Constraint
- [ ] CS-01: Prevent product creation with empty required fields
  - Action: Leave "Product Title" and "Affiliate Link" blank on the product creation form and click "Save Product".
  - Expected: The form submission is blocked, the record is not created, and inline validation messages appear under the empty required fields.
  - Bug Report:
    - Issue: Missing Inline Validation
    - Actual: While submission is blocked with a generic toast notification ("Please fill in all required fields"), no inline validation messages appear under the empty fields, and the Affiliate Link field is not marked as required.
- [ ] CS-02: Restrict affiliate link to valid URL format
  - Action: Enter an invalid string (e.g., "invalid-url-text") into the "Affiliate Link" field and click "Save Product".
  - Expected: The form rejects the submission and displays an error message stating "Please enter a valid URL".
  - Bug Report:
    - Issue: Missing URL Format Validation
    - Actual: The form did not reject the submission and displayed no error message; it accepted "invalid-url-text" and successfully created the product entry.
- [X] CS-03: Display empty state for non-matching search queries
  - Action: Type a non-matching string (e.g., "zzxxqqnonexistent") into the search bar and press Enter.
  - Expected: No products are listed, and an informative "No products found" message is displayed.
- [ ] CS-04: Prevent filtering when minimum price exceeds maximum price
  - Action: Set the "Min Price" higher than "Max Price" (e.g., Min: $100, Max: $20) and click "Apply Filter".
  - Expected: The filter is not applied and an error message indicating that minimum price cannot exceed maximum price is displayed.
  - Bug Report:
    - Issue: Missing Min/Max Price Inputs and Validation
    - Actual: Neither "Min Price" and "Max Price" text/numeric inputs nor an "Apply Filter" button exist; price range is constrained to a slider component, making it impossible to input a minimum price higher than maximum price or view the expected error message.

## Interaction
- [X] IX-01: Display success toast notification upon updating a product
  - Action: Modify an existing product in the editor and click "Update Product".
  - Expected: A confirmation toast stating "Product updated successfully" appears in the top-right corner and auto-dismisses after a few seconds.
- [X] IX-02: Open external affiliate link in a new browser tab
  - Action: Click the "Buy on Retailer" button on any product detail page.
  - Expected: The external retailer website opens in a new browser tab, keeping the original product detail page open.
- [ ] IX-03: Highlight active category filter selection
  - Action: Click on the "Fitness Products" category filter pill.
  - Expected: The "Fitness Products" button dynamically changes to an active highlighted style while other category buttons remain in the default state.
  - Bug Report:
    - Issue: Missing Category Filter Pill Element
    - Actual: There are no category filter pills on the catalog or homepage; category filtering is implemented as a dropdown select combobox and navigation bar links labeled "Tech", "Home", and "Fitness". No pill or button labeled "Fitness Products" exists.

## Content
- [ ] CT-01: Verify default category taxonomy
  - Action: Inspect the category navigation menu on the homepage and catalog page.
  - Expected: The category options strictly contain "Tech Gadgets", "Home Goods", and "Fitness Products".
  - Bug Report:
    - Issue: Incorrect Taxonomy Naming
    - Actual: The category options in the navigation menu strictly display "Tech", "Home", and "Fitness" rather than "Tech Gadgets", "Home Goods", and "Fitness Products".
- [X] CT-02: Verify product detail page content completeness
  - Action: View an existing product's detail page.
  - Expected: The page displays the curator's written review, a structured key specifications list, price, rating, and product category badge.
- [X] CT-03: Verify homepage featured products content
  - Action: Navigate to the "Featured Products" section on the homepage.
  - Expected: Only products marked as featured are displayed with their thumbnail image, title, rating, and brief review snippet.