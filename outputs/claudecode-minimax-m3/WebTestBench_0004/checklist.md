# Test Checklist

## Functionality
- [ ] FT-01: Create a new planning dashboard with wedding date, budget, and guest count
  - Action: Click "Create Dashboard" or equivalent, enter a valid wedding date, budget amount, and guest count, then save.
  - Expected: Dashboard is created and the entered date, budget, and guest count are displayed on the dashboard.

- [ ] FT-02: Update existing dashboard details (wedding date, budget, guest count)
  - Action: Edit one or more dashboard fields (date/budget/guest count) and save.
  - Expected: The dashboard reflects the new values after saving.

- [ ] FT-03: Browse venue and vendor listings
  - Action: Navigate to the listings page using default data already present.
  - Expected: A list of venue and vendor items is displayed.

- [ ] FT-04: Filter listings by location type, price range, and service type
  - Action: Apply filters for location type, price range, and/or service type on the listings page.
  - Expected: Only listings matching the selected filter criteria are shown.

- [ ] FT-05: Search listings using a keyword
  - Action: Enter a keyword (e.g., a venue or vendor name) in the search box and submit.
  - Expected: Listings matching the keyword are displayed.

- [ ] FT-06: Mark a venue or vendor listing as a favorite
  - Action: Click the "favorite" / heart icon on a listing.
  - Expected: The listing is saved to the user's favorites.

- [ ] FT-07: View the planning tips and checklists collection
  - Action: Navigate to the tips/checklists section using default data.
  - Expected: A collection of planning tips and checklists is displayed.

- [ ] FT-08: Save a planning tip or checklist to the dashboard
  - Action: Click "Save" on a planning tip or checklist.
  - Expected: The item appears in the user's dashboard saved list.

- [ ] FT-09: Mark a saved planning tip or checklist as completed
  - Action: Click "Mark as Completed" on a saved planning item.
  - Expected: The item's status changes to "Completed" on the dashboard.

## Constraint
- [ ] CS-01: Dashboard cannot be saved with any required field empty
  - Action: Leave wedding date, budget, or guest count blank and click Save.
  - Expected: Save is blocked and a validation message indicates the missing required field.

- [ ] CS-02: Dashboard cannot be saved with an invalid budget
  - Action: Enter a negative number or non-numeric value for budget and click Save.
  - Expected: Save is blocked and a validation message indicates the budget is invalid.

- [ ] CS-03: Dashboard cannot be saved with an invalid guest count
  - Action: Enter a negative number or non-numeric value for guest count and click Save.
  - Expected: Save is blocked and a validation message indicates the guest count is invalid.

- [ ] CS-04: A planning tip or checklist cannot be saved twice to the dashboard
  - Action: Save a planning item that is already saved.
  - Expected: The duplicate save is prevented, or the existing saved entry is not duplicated.

## Interaction
- [ ] IX-01: Success confirmation appears after creating or updating the dashboard
  - Action: Save a new or updated dashboard.
  - Expected: A success message/toast (e.g., "Dashboard saved") is displayed.

- [ ] IX-02: Favorites indicator updates when a listing is marked or unmarked as favorite
  - Action: Click the favorite icon on a listing to toggle it.
  - Expected: The favorite state visually updates (e.g., filled vs. outlined heart) and/or the favorites count changes.

- [ ] IX-03: Completed planning items display a visual "completed" state
  - Action: Mark a saved planning tip or checklist as completed.
  - Expected: The item shows a clear "completed" visual indicator (e.g., checkmark, strikethrough, or status label).

## Content
- [ ] CT-01: Each venue/vendor listing displays relevant details
  - Action: Open the listings page and inspect entries.
  - Expected: Each listing shows a name, image, category (location/service type), and price information relevant to wedding venues/vendors.

- [ ] CT-02: Each planning tip/checklist displays relevant title and description content
  - Action: Open the tips/checklists collection and inspect entries.
  - Expected: Each item shows a title and description related to wedding planning (e.g., "12-Month Wedding Timeline," "Budget Checklist").