# Test Checklist

## Functionality
- [ ] FT-01: Create/update the planning dashboard with a wedding date
  - Action: Open the planning dashboard and enter a date in the "Wedding Date" field, then click "Save".
  - Expected: The dashboard displays the entered wedding date and the save succeeds.

- [ ] FT-02: Update the budget on the planning dashboard
  - Action: Enter a value in the "Budget" field and click "Save".
  - Expected: The dashboard shows the updated budget amount.

- [ ] FT-03: Update the guest count on the planning dashboard
  - Action: Enter a number in the "Guest Count" field and click "Save".
  - Expected: The dashboard shows the updated guest count.

- [ ] FT-04: Browse venue listings
  - Action: Navigate to the "Venues" section.
  - Expected: A list of venue listings is displayed.

- [ ] FT-05: Browse vendor listings
  - Action: Navigate to the "Vendors" section.
  - Expected: A list of vendor listings is displayed.

- [ ] FT-06: Filter listings by location type
  - Action: Select a "Location Type" filter option (e.g., Indoor, Outdoor, Beach).
  - Expected: Only listings matching the selected location type are shown.

- [ ] FT-07: Filter listings by price range
  - Action: Select/enter a "Price Range" filter.
  - Expected: Only listings within the selected price range are shown.

- [ ] FT-08: Filter listings by service type
  - Action: Select a "Service Type" filter option (e.g., Catering, Photography).
  - Expected: Only listings matching the selected service type are shown.

- [ ] FT-09: Search listings by keyword
  - Action: Type a keyword into the search box and submit.
  - Expected: Only listings matching the keyword are displayed.

- [ ] FT-10: Mark a listing as a favorite
  - Action: Click the "Favorite" (heart/star) button on a listing.
  - Expected: The listing is added to the user's favorites.

- [ ] FT-11: View saved favorites
  - Action: Navigate to the "Favorites" section.
  - Expected: All previously favorited listings are displayed.

- [ ] FT-12: View planning tips and checklists
  - Action: Navigate to the "Tips & Checklists" section.
  - Expected: A collection of planning tips/checklists is displayed.

- [ ] FT-13: Save a tip/checklist to the dashboard
  - Action: Click "Save to Dashboard" on a tip/checklist item.
  - Expected: The item appears in the user's planning dashboard.

- [ ] FT-14: Mark a saved tip/checklist as completed
  - Action: Click "Mark as Completed" on a saved tip/checklist in the dashboard.
  - Expected: The item is shown with a completed status (e.g., checked/strikethrough).

## Constraint
- [ ] CS-01: Dashboard numeric fields reject invalid input
  - Action: Enter a negative or non-numeric value in "Budget" and a value ≤ 0 in "Guest Count", then click "Save".
  - Expected: Save is blocked and a validation error is shown for each invalid field.

- [ ] CS-02: Wedding date cannot be set to a past date
  - Action: Enter a date earlier than today in the "Wedding Date" field and click "Save".
  - Expected: Save is blocked with a validation error indicating the date must be in the future.

## Interaction
- [ ] IX-01: Success confirmation after saving the dashboard
  - Action: Update any dashboard field and click "Save".
  - Expected: A success message/toast (e.g., "Dashboard saved") is displayed.

- [ ] IX-02: Favorite button reflects toggled state
  - Action: Click the "Favorite" button on a listing, then click it again.
  - Expected: The button shows a filled/active state when favorited and reverts to inactive when un-favorited.

## Content
- [ ] CT-01: Listings display relevant detail fields
  - Action: Open any venue or vendor listing.
  - Expected: Each listing shows relevant details: name, location type, price, and service type.

- [ ] CT-02: Tips and checklists are relevant to wedding planning
  - Action: Open the "Tips & Checklists" section and review the items.
  - Expected: All items are clearly related to wedding planning (e.g., budgeting, venues, timelines).