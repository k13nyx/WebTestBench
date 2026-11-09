# Test Result

## Functionality
- [X] FT-01: New user can register an account
  - Action: Open the "Register"/"Sign Up" page, enter a valid name, unused email, and password, then click "Register".
  - Expected: Account is created, the user is logged in, and lands on the marketplace homepage/dashboard.
- [X] FT-02: Seller can create a listing with photo, description, price, and location
  - Action: Click "Create Listing"/"Sell", upload a photo, fill in title, description, price, category, condition, and location, then click "Publish".
  - Expected: The listing is created and appears in the marketplace results and in "My Listings" with all entered details.
- [X] FT-03: Buyer can search listings by keyword
  - Action: Type a product name from the default listings into the search bar and submit.
  - Expected: Only listings whose title/description matches the keyword are displayed.
- [X] FT-04: Buyer can filter listings by category
  - Action: Select one category (e.g., "Furniture") from the Category filter and apply it.
  - Expected: Only listings in the selected category are displayed.
- [ ] FT-05: Buyer can filter listings by price range
  - Action: Enter Min Price and Max Price (e.g., 10 and 50) in the price filter and apply.
  - Expected: Only listings priced between 10 and 50 are displayed.
  - Bug Report:
    - Issue: Missing max-price filter control — price range filtering cannot be performed
    - Actual: The Price Range filter contains only a single-thumb slider labeled "Minimum" (0–500); there are no Min/Max price input fields and no max-price thumb. Setting the slider works only as a minimum-price filter (e.g., min $60 → label "$60 - $500", 7 listings ≥ $60 shown), so it is impossible to display "only listings priced between 10 and 50" — listings above the max price can never be excluded.
- [X] FT-06: Buyer can filter listings by condition
  - Action: Select one condition (e.g., "Used – Good") from the Condition filter and apply it.
  - Expected: Only listings matching that condition are displayed.
- [ ] FT-07: Buyer can filter listings by distance
  - Action: Enter a location/city and a radius (e.g., 25 km) in the Distance filter and apply it.
  - Expected: Only listings located within that radius are displayed.
  - Bug Report:
    - Issue: Incorrect distance filtering — per-listing distances are arbitrary and do not reflect actual geography; no location input exists
    - Actual: The filter has no location/city field, only a "Max Distance" slider (1–50, labeled in miles, not km). The distances used are fake and unrelated to real locations: at a 6-mile radius, listings in Brooklyn, NY ("Handmade Macrame Wall Hanging", "Mid-Century Modern Armchair") and Austin, TX ("Yoga Mat & Blocks Set" — its detail page literally shows "Austin, TX (4 mi)") are displayed as within 6 miles, while other Portland, OR listings are excluded until ~10–16 miles; at 25 the entire catalog (including cross-country listings) is displayed. Only the user's own listing matches at the 1-mile setting.
- [X] FT-08: Buyer can sort listings
  - Action: On the results page, choose "Price: Low to High" from the "Sort by" dropdown.
  - Expected: Listings are re-displayed in ascending price order.
- [X] FT-09: Buyer can add an item to the cart
  - Action: On a listing page, click "Add to Cart", then open the cart page.
  - Expected: The item appears in the cart with its photo, title, and price.
- [X] FT-10: Buyer can send a purchase request
  - Action: On a listing page, click "Send Purchase Request", optionally add a message, and submit.
  - Expected: The purchase request is sent/recorded for that listing.
- [ ] FT-11: Seller can update their own listing
  - Action: Open one of your listings from "My Listings", change the price (or description), and save.
  - Expected: The listing shows the updated value in "My Listings" and in marketplace results.
  - Bug Report:
    - Issue: Missing feature — no edit/update control exists for listings (Unresponsive/absent update capability)
    - Actual: "My Listings" offers only "View", "Mark Sold", and "Delete"; the listing detail page (own listing) offers only "Manage Your Listings"; the user menu has only My Profile/My Listings/Log out; and probing `/product/:id/edit`, `/edit-listing/:id` returns 404. There is no way to change a listing's price or description after creation, so the listing can never show an updated value.
- [X] FT-12: Seller can remove their own listing
  - Action: Open one of your listings, click "Delete"/"Remove Listing", and confirm.
  - Expected: The listing no longer appears in marketplace results or in "My Listings".

## Constraint
- [X] CS-01: Registration cannot be submitted with empty or invalid required fields
  - Action: On the registration form, leave email/password empty (or enter an invalid email format) and click "Register".
  - Expected: Submission is blocked and a validation error indicates the missing/invalid required fields.
- [X] CS-02: Listing cannot be published with missing required fields
  - Action: In the create-listing form, leave the photo, description, price, or location empty and click "Publish".
  - Expected: The listing is not created; an error indicates which required fields are missing.
- [X] CS-03: Listing price must be a positive number
  - Action: Enter a non-numeric (e.g., "abc") or negative price in the create-listing form and submit.
  - Expected: The value is rejected with a validation error and the listing is not created.

## Interaction
- [X] IX-01: Cart badge updates when an item is added
  - Action: Click "Add to Cart" on a listing while watching the cart icon in the header.
  - Expected: The cart count/badge increments immediately, with no page reload errors.
- [X] IX-02: Confirmation dialog before listing removal
  - Action: Click "Delete"/"Remove Listing" on your own listing.
  - Expected: A confirmation dialog appears; the listing is deleted only after confirming and remains if "Cancel" is clicked.
- [X] IX-03: Success feedback after sending a purchase request
  - Action: Submit a purchase request on a listing.
  - Expected: A visible success toast/message (e.g., "Request sent to seller") confirms the request.

## Content
- [X] CT-01: Listing detail page shows complete and correct item information
  - Action: Open any default listing's detail page.
  - Expected: Photo, title, description, price, condition, and location are all displayed and match the listing's data.
- [ ] CT-02: All listings are relevant to the second-hand/upcycled theme
  - Action: Browse the homepage default listings and their images.
  - Expected: Every item is a second-hand or upcycled product (e.g., used furniture, vintage clothing, repurposed goods), and each image loads and matches its listing title.
  - Bug Report:
    - Issue: Broken image resource — one listing's photo fails to load
    - Actual: All 10 default listings are on-theme second-hand/upcycled products (reclaimed wood bookshelf, upcycled pallet table, vintage denim jacket, used yoga mat, etc.), and each image's alt text matches its listing title. However, the "Handmade Macrame Wall Hanging" image (https://images.unsplash.com/photo-1622464689583-a09e88f0d34e?w=600&h=600&fit=crop) fails to load: `naturalWidth = 0` and the console logs "Failed to load resource: the server responded with a status of ...". Verified consistently across two separate checks; the other 9 images load fine.
