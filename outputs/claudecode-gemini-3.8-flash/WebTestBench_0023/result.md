# Test Result

## Functionality
- [X] FT-01: User account registration
  - Action: Fill out the registration form with valid credentials (username, email, password) and click the "Register" button.
  - Expected: User account is successfully created and user is logged in to the marketplace.
- [X] FT-02: Create a new product listing
  - Action: In the listing creation form, upload an item photo, fill in title, description, price, condition, category, and location, then click "Publish Listing".
  - Expected: The new listing is published and appears in the marketplace and the seller's active listings.
- [X] FT-03: Keyword search for items
  - Action: Enter an item name into the search bar and press Enter or click the "Search" button.
  - Expected: Catalog updates to display only items with titles or descriptions matching the search term.
- [X] FT-04: Filter items by category, price range, condition, and distance
  - Action: Select a specific category, adjust minimum and maximum price inputs, select an item condition (e.g., "Upcycled"), set distance radius, and click "Apply Filters".
  - Expected: Product list updates to display only items that satisfy all applied filter criteria.
- [X] FT-05: Sort product listings
  - Action: Select "Price: Low to High" from the sort dropdown menu.
  - Expected: The displayed items immediately reorder from lowest price to highest price.
- [X] FT-06: Add item to cart
  - Action: Open a product details page and click the "Add to Cart" button.
  - Expected: The product is added to the cart and the header cart badge count increments by 1.
- [X] FT-07: Send purchase request to seller
  - Action: Click "Send Purchase Request" on a product detail page, enter a message to the seller, and click "Submit Request".
  - Expected: The purchase request is submitted and delivered to the seller.
- [ ] FT-08: Edit and update existing listing
  - Action: Navigate to "My Listings", click "Edit" on an existing listing, modify the price and description, and click "Save Changes".
  - Expected: The listing updates with the new price and description across the marketplace.
  - Bug Report:
    - Issue: Missing Edit Listing Feature
    - Actual: Listing cards in "My Listings" only contain "View", "Mark Sold", and "Delete" buttons; there is no "Edit" button or form to update existing listings.
- [X] FT-09: Remove listing
  - Action: Navigate to "My Listings", locate an unavailable item, and click the "Delete Listing" button.
  - Expected: The listing is permanently removed from the user's listings and is no longer searchable or visible in the marketplace.

## Constraint
- [ ] CS-01: Prevent listing creation with missing required fields
  - Action: Leave the price and location fields blank on the listing creation form and click "Publish Listing".
  - Expected: Form submission is blocked, and validation error messages appear under the empty required fields.
  - Bug Report:
    - Issue: Missing Field-Level Validation Messages
    - Actual: Form submission is blocked by a generic toast notification ("Please fill in all required fields"), but no validation error messages appear under the empty required fields.
- [X] CS-02: Reject negative or non-numeric listing prices
  - Action: Enter "-15" into the price input field during listing creation and attempt to submit.
  - Expected: System prevents form submission and displays an error stating that price must be a positive number.
- [ ] CS-03: Inverted price filter range prevention
  - Action: Enter a minimum price of "$100" and a maximum price of "$50" in the price filter and click "Apply Filters".
  - Expected: System displays an error message indicating minimum price cannot exceed maximum price, preventing filter execution.
  - Bug Report:
    - Issue: Missing Inverted Price Range Validation
    - Actual: The price filter is implemented as a slider without text inputs for minimum/maximum prices and lacks an "Apply Filters" button, with no error message preventing inverted price range input.
- [ ] CS-04: Unauthorized listing modification restriction
  - Action: Attempt to access the edit URL or edit controls of an item belonging to another seller.
  - Expected: System denies access, displays an unauthorized error message, and does not allow editing.
  - Bug Report:
    - Issue: Missing Unauthorized Access Handling
    - Actual: Attempting to navigate to an edit URL returns a 404 "Page not found" error because edit routes do not exist, rather than denying access with an unauthorized error message.

## Interaction
- [X] IX-01: Listing deletion confirmation dialog
  - Action: Click the "Delete Listing" button on an item in "My Listings".
  - Expected: A confirmation modal appears asking the user to confirm or cancel the deletion before removing the listing.
- [ ] IX-02: Purchase request submission feedback
  - Action: Submit the purchase request modal on a product page.
  - Expected: The modal closes and a success toast notification appears stating "Purchase request sent successfully".
  - Bug Report:
    - Issue: Incorrect Toast Feedback Message
    - Actual: Upon submitting the message dialog, the toast notification displays "Message sent to seller!" instead of "Purchase request sent successfully".
- [ ] IX-03: Cart preview notification on item addition
  - Action: Click the "Add to Cart" button on any product card.
  - Expected: A cart slide-out drawer or popover appears confirming the item was added and showing the current cart subtotal.
  - Bug Report:
    - Issue: Missing Cart Preview Notification
    - Actual: Product cards in the catalog do not have an "Add to Cart" button, and clicking "Add to Cart" on the product detail page triggers a toast message without displaying a cart slide-out drawer or popover with the cart subtotal.

## Content
- [X] CT-01: Second-hand and upcycled condition badge display
  - Action: Browse product cards in the main marketplace catalog.
  - Expected: Each product card visibly displays a clear condition badge corresponding to second-hand or upcycled status (e.g., "Upcycled", "Used - Like New", "Refurbished").
- [X] CT-02: Complete listing metadata on product page
  - Action: Open any default product detail page from the catalog.
  - Expected: Page displays the product title, photo gallery, item description, price, condition, and location details accurately without placeholder text.