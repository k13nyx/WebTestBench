# Test Result

## Functionality
- [X] FT-01: Create a planning dashboard with wedding date, budget, and guest count.
  - Action: Open the Planning Dashboard, enter a wedding date, budget, and guest count, then click "Save".
  - Expected: Dashboard saves and displays all three entered values.

- [X] FT-02: Update existing dashboard details.
  - Action: Change the budget and guest count values on the dashboard, then click "Save"/"Update".
  - Expected: Dashboard shows the new values (old values replaced), and the updates persist after page reload.

- [X] FT-03: Browse venue and vendor listings.
  - Action: Navigate to the Venues & Vendors listings page.
  - Expected: A browsable list of venue and vendor cards from the default data is displayed.

- [X] FT-04: Filter listings by location type.
  - Action: Select a location type filter (e.g., "Beach") in the filter controls.
  - Expected: Only listings with the selected location type are displayed.

- [X] FT-05: Filter listings by price range.
  - Action: Select a price range filter (e.g., "$$") in the filter controls.
  - Expected: Only listings within the selected price range are displayed.

- [X] FT-06: Filter vendors by service type.
  - Action: Select a service type filter (e.g., "Catering") in the filter controls.
  - Expected: Only vendor listings of the selected service type are displayed.

- [X] FT-07: Search listings by keyword.
  - Action: Enter the name of an existing listing into the search field and submit.
  - Expected: Results narrow to listings matching the entered keyword.

- [X] FT-08: Mark a listing as favorite and find it in Favorites.
  - Action: Click the favorite (heart/star) button on a listing card, then open the Favorites section.
  - Expected: The listing appears in the Favorites section.

- [X] FT-09: View a planning tip or checklist.
  - Action: Open the Planning Tips & Checklists section and click a tip/checklist item.
  - Expected: The full title and content of the tip/checklist are displayed.

- [X] FT-10: Save a tip/checklist to the dashboard.
  - Action: Click "Save to Dashboard" on a tip/checklist item, then open the dashboard.
  - Expected: The tip/checklist appears in the dashboard's saved items list.

- [ ] FT-11: Mark a saved checklist item as completed.
  - Action: On the dashboard, click "Mark as Completed" (or its checkbox) on a saved checklist item, then reload the page.
  - Expected: The item shows a completed state (e.g., checkmark/strikethrough) and remains completed after reload.
  - Bug Report:
    - Issue: Missing Completion Control on Dashboard Saved Items
    - Actual: The dashboard's "Your Saved Checklists" item (e.g., "12+ Months Before — 0 of 6 completed") is a non-interactive summary card: it contains no "Mark as Completed" button and no checkbox, and clicking the card/heading does nothing (0 checkbox/`role="checkbox"` elements and no "complete/mark" buttons exist anywhere on the dashboard). The specified dashboard action cannot be performed. (Completion checkboxes exist only in the checklist's detail view on /checklists; when used there, the checked state does persist — dashboard shows "1 of 6 completed" after reload — but that is outside the specified interaction surface.)

## Constraint
- [ ] CS-01: Dashboard cannot be saved with empty required fields.
  - Action: Clear the wedding date, budget, and guest count fields, then click "Save".
  - Expected: Save is blocked with a required-field validation message; no empty values are saved.
  - Bug Report:
    - Issue: Missing Required-Field Validation on Save
    - Actual: With wedding date, budget, and guest count all cleared, clicking "Save" was not blocked: the form closed and empty values were saved — the dashboard reset to Wedding Date "Not set", Budget "$0", Guest Count "0" (hero reverted to "Plan Your Perfect Day"). No required-field validation message of any kind was displayed.

- [ ] CS-02: Invalid budget or guest count values are rejected.
  - Action: Enter non-numeric text (e.g., "abc") or a negative value (e.g., "-5") in the budget and guest count fields, then click "Save".
  - Expected: A validation error is shown for each invalid field; invalid values are not saved.
  - Bug Report:
    - Issue: Missing Numeric/Range Validation on Budget and Guest Count
    - Actual: No validation error is shown for either field. The negative guest count "-5" was accepted and saved — the dashboard displays "Guest Count: -5" after saving. Non-numeric input "abc" in the budget field is silently discarded to "0" with no error message, and "$0" is saved. Invalid values are not rejected with visible validation errors.

- [X] CS-03: Combined filters only show listings matching all criteria.
  - Action: Apply a location type filter and a price range filter at the same time.
  - Expected: Every displayed listing matches both selected filters; no listing outside the criteria appears.

- [X] CS-04: No duplicate favorites are created.
  - Action: Click the favorite button on a listing that is already in Favorites.
  - Expected: The listing is removed from Favorites (toggled off); no duplicate favorite entries exist.

## Interaction
- [ ] IX-01: Saving dashboard details gives confirmation feedback.
  - Action: Save the dashboard details (on create and on update).
  - Expected: A success confirmation (e.g., a toast reading "Details saved") appears after each save.
  - Bug Report:
    - Issue: Missing Save Confirmation Feedback (Toast)
    - Actual: No success confirmation appears after saving dashboard details — not on create and not on update. After clicking "Save", the toast/notification region (`aria-label="Notifications (F8)"` list) remains empty and no `[role="alert"]`/`[role="status"]`/toast element is rendered, confirmed by polling the DOM every 100ms for 3 seconds after the save. The only visible change is the dashboard values updating silently.

- [X] IX-02: Favorite button shows an immediate visual state change.
  - Action: Click the favorite button on an unfavorited listing card.
  - Expected: The button changes appearance immediately (e.g., outline icon becomes filled/colored) to indicate the favorited state.

## Content
- [X] CT-01: Listing cards show accurate, complete details.
  - Action: Inspect venue and vendor cards on the listings page.
  - Expected: Each card shows its name, location type, price/price range, and service/category, matching that listing's data.

- [ ] CT-02: All listing images and text are wedding-relevant.
  - Action: Browse all venue and vendor listings and review their images and descriptions.
  - Expected: Every listing's image and description are relevant to wedding venues/vendors; no unrelated or broken media appears.
  - Bug Report:
    - Issue: Broken Listing Image
    - Actual: The "DJ Spark Entertainment" vendor card image fails to load — its `<img>` reports `complete: true, naturalWidth: 0, naturalHeight: 0` even after a 2-second re-check, with source `https://images.unsplash.com/photo-1571266028243-d220c6a8b8d1?w=800` (invalid/missing photo). All other 17 listing images load correctly and all descriptions are wedding-relevant, but this broken media violates the "no broken media appears" expectation.

- [X] CT-03: Tips and checklists contain relevant, actionable content.
  - Action: Open each planning tip/checklist item.
  - Expected: Each has a wedding-planning-relevant title and actionable body content (steps/advice); no placeholder or empty text.
