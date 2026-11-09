# Test Checklist

## Functionality
- [ ] FT-01: New user can register an account
  - Action: Open the "Register"/"Sign Up" page, enter a valid name, unused email, and password, then click "Register".
  - Expected: Account is created, the user is logged in, and lands on the marketplace homepage/dashboard.
- [ ] FT-02: Seller can create a listing with photo, description, price, and location
  - Action: Click "Create Listing"/"Sell", upload a photo, fill in title, description, price, category, condition, and location, then click "Publish".
  - Expected: The listing is created and appears in the marketplace results and in "My Listings" with all entered details.
- [ ] FT-03: Buyer can search listings by keyword
  - Action: Type a product name from the default listings into the search bar and submit.
  - Expected: Only listings whose title/description matches the keyword are displayed.
- [ ] FT-04: Buyer can filter listings by category
  - Action: Select one category (e.g., "Furniture") from the Category filter and apply it.
  - Expected: Only listings in the selected category are displayed.
- [ ] FT-05: Buyer can filter listings by price range
  - Action: Enter Min Price and Max Price (e.g., 10 and 50) in the price filter and apply.
  - Expected: Only listings priced between 10 and 50 are displayed.
- [ ] FT-06: Buyer can filter listings by condition
  - Action: Select one condition (e.g., "Used – Good") from the Condition filter and apply it.
  - Expected: Only listings matching that condition are displayed.
- [ ] FT-07: Buyer can filter listings by distance
  - Action: Enter a location/city and a radius (e.g., 25 km) in the Distance filter and apply it.
  - Expected: Only listings located within that radius are displayed.
- [ ] FT-08: Buyer can sort listings
  - Action: On the results page, choose "Price: Low to High" from the "Sort by" dropdown.
  - Expected: Listings are re-displayed in ascending price order.
- [ ] FT-09: Buyer can add an item to the cart
  - Action: On a listing page, click "Add to Cart", then open the cart page.
  - Expected: The item appears in the cart with its photo, title, and price.
- [ ] FT-10: Buyer can send a purchase request
  - Action: On a listing page, click "Send Purchase Request", optionally add a message, and submit.
  - Expected: The purchase request is sent/recorded for that listing.
- [ ] FT-11: Seller can update their own listing
  - Action: Open one of your listings from "My Listings", change the price (or description), and save.
  - Expected: The listing shows the updated value in "My Listings" and in marketplace results.
- [ ] FT-12: Seller can remove their own listing
  - Action: Open one of your listings, click "Delete"/"Remove Listing", and confirm.
  - Expected: The listing no longer appears in marketplace results or in "My Listings".

## Constraint
- [ ] CS-01: Registration cannot be submitted with empty or invalid required fields
  - Action: On the registration form, leave email/password empty (or enter an invalid email format) and click "Register".
  - Expected: Submission is blocked and a validation error indicates the missing/invalid required fields.
- [ ] CS-02: Listing cannot be published with missing required fields
  - Action: In the create-listing form, leave the photo, description, price, or location empty and click "Publish".
  - Expected: The listing is not created; an error indicates which required fields are missing.
- [ ] CS-03: Listing price must be a positive number
  - Action: Enter a non-numeric (e.g., "abc") or negative price in the create-listing form and submit.
  - Expected: The value is rejected with a validation error and the listing is not created.

## Interaction
- [ ] IX-01: Cart badge updates when an item is added
  - Action: Click "Add to Cart" on a listing while watching the cart icon in the header.
  - Expected: The cart count/badge increments immediately, with no page reload errors.
- [ ] IX-02: Confirmation dialog before listing removal
  - Action: Click "Delete"/"Remove Listing" on your own listing.
  - Expected: A confirmation dialog appears; the listing is deleted only after confirming and remains if "Cancel" is clicked.
- [ ] IX-03: Success feedback after sending a purchase request
  - Action: Submit a purchase request on a listing.
  - Expected: A visible success toast/message (e.g., "Request sent to seller") confirms the request.

## Content
- [ ] CT-01: Listing detail page shows complete and correct item information
  - Action: Open any default listing's detail page.
  - Expected: Photo, title, description, price, condition, and location are all displayed and match the listing's data.
- [ ] CT-02: All listings are relevant to the second-hand/upcycled theme
  - Action: Browse the homepage default listings and their images.
  - Expected: Every item is a second-hand or upcycled product (e.g., used furniture, vintage clothing, repurposed goods), and each image loads and matches its listing title.