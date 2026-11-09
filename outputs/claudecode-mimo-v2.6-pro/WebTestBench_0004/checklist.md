# Test Checklist

## Functionality
- [ ] FT-01: Create a planning dashboard with wedding date, budget, and guest count.
  - Action: Open the Planning Dashboard, enter a wedding date, budget, and guest count, then click "Save".
  - Expected: Dashboard saves and displays all three entered values.

- [ ] FT-02: Update existing dashboard details.
  - Action: Change the budget and guest count values on the dashboard, then click "Save"/"Update".
  - Expected: Dashboard shows the new values (old values replaced), and the updates persist after page reload.

- [ ] FT-03: Browse venue and vendor listings.
  - Action: Navigate to the Venues & Vendors listings page.
  - Expected: A browsable list of venue and vendor cards from the default data is displayed.

- [ ] FT-04: Filter listings by location type.
  - Action: Select a location type filter (e.g., "Beach") in the filter controls.
  - Expected: Only listings with the selected location type are displayed.

- [ ] FT-05: Filter listings by price range.
  - Action: Select a price range filter (e.g., "$$") in the filter controls.
  - Expected: Only listings within the selected price range are displayed.

- [ ] FT-06: Filter vendors by service type.
  - Action: Select a service type filter (e.g., "Catering") in the filter controls.
  - Expected: Only vendor listings of the selected service type are displayed.

- [ ] FT-07: Search listings by keyword.
  - Action: Enter the name of an existing listing into the search field and submit.
  - Expected: Results narrow to listings matching the entered keyword.

- [ ] FT-08: Mark a listing as favorite and find it in Favorites.
  - Action: Click the favorite (heart/star) button on a listing card, then open the Favorites section.
  - Expected: The listing appears in the Favorites section.

- [ ] FT-09: View a planning tip or checklist.
  - Action: Open the Planning Tips & Checklists section and click a tip/checklist item.
  - Expected: The full title and content of the tip/checklist are displayed.

- [ ] FT-10: Save a tip/checklist to the dashboard.
  - Action: Click "Save to Dashboard" on a tip/checklist item, then open the dashboard.
  - Expected: The tip/checklist appears in the dashboard's saved items list.

- [ ] FT-11: Mark a saved checklist item as completed.
  - Action: On the dashboard, click "Mark as Completed" (or its checkbox) on a saved checklist item, then reload the page.
  - Expected: The item shows a completed state (e.g., checkmark/strikethrough) and remains completed after reload.

## Constraint
- [ ] CS-01: Dashboard cannot be saved with empty required fields.
  - Action: Clear the wedding date, budget, and guest count fields, then click "Save".
  - Expected: Save is blocked with a required-field validation message; no empty values are saved.

- [ ] CS-02: Invalid budget or guest count values are rejected.
  - Action: Enter non-numeric text (e.g., "abc") or a negative value (e.g., "-5") in the budget and guest count fields, then click "Save".
  - Expected: A validation error is shown for each invalid field; invalid values are not saved.

- [ ] CS-03: Combined filters only show listings matching all criteria.
  - Action: Apply a location type filter and a price range filter at the same time.
  - Expected: Every displayed listing matches both selected filters; no listing outside the criteria appears.

- [ ] CS-04: No duplicate favorites are created.
  - Action: Click the favorite button on a listing that is already in Favorites.
  - Expected: The listing is removed from Favorites (toggled off); no duplicate favorite entries exist.

## Interaction
- [ ] IX-01: Saving dashboard details gives confirmation feedback.
  - Action: Save the dashboard details (on create and on update).
  - Expected: A success confirmation (e.g., a toast reading "Details saved") appears after each save.

- [ ] IX-02: Favorite button shows an immediate visual state change.
  - Action: Click the favorite button on an unfavorited listing card.
  - Expected: The button changes appearance immediately (e.g., outline icon becomes filled/colored) to indicate the favorited state.

## Content
- [ ] CT-01: Listing cards show accurate, complete details.
  - Action: Inspect venue and vendor cards on the listings page.
  - Expected: Each card shows its name, location type, price/price range, and service/category, matching that listing's data.

- [ ] CT-02: All listing images and text are wedding-relevant.
  - Action: Browse all venue and vendor listings and review their images and descriptions.
  - Expected: Every listing's image and description are relevant to wedding venues/vendors; no unrelated or broken media appears.

- [ ] CT-03: Tips and checklists contain relevant, actionable content.
  - Action: Open each planning tip/checklist item.
  - Expected: Each has a wedding-planning-relevant title and actionable body content (steps/advice); no placeholder or empty text.