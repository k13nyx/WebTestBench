# Test Checklist

## Functionality
- [ ] FT-01: Planning dashboard displays key wedding details
  - Action: Navigate to the dashboard page.
  - Expected: Dashboard shows fields/sections for Wedding Date, Budget, and Guest Count with default values populated.

- [ ] FT-02: User can update and persist wedding date, budget, and guest count
  - Action: Edit Wedding Date to a future date, Budget to a numeric amount, Guest Count to a number, then click "Save"/"Update". Reload the page.
  - Expected: All three values display the new entries and persist after reload.

- [ ] FT-03: Venue and vendor listings are browsable
  - Action: Navigate to the Venues/Vendors listings page.
  - Expected: A grid/list of default venue and vendor entries is displayed.

- [ ] FT-04: Listings can be filtered by location type
  - Action: Apply a location type filter (e.g., "Outdoor" or "Beach").
  - Expected: Only listings matching that location type remain visible.

- [ ] FT-05: Listings can be filtered by price range and service type
  - Action: Apply a price range filter (e.g., "$$$") and a service type filter (e.g., "Catering"), individually and combined.
  - Expected: Only listings matching the active filter(s) are shown; combined filters return listings satisfying both.

- [ ] FT-06: User can search listings by keyword
  - Action: Type a known venue/vendor name (from default data) into the search field.
  - Expected: Results narrow to listings whose name/details match the keyword.

- [ ] FT-07: User can mark listings as favorites and view them later
  - Action: Click "Favorite" on 2 listings, then open the Favorites page/section.
  - Expected: Both favorited listings appear in the favorites view.

- [ ] FT-08: User can view planning tips/checklists and save one to the dashboard
  - Action: Open the Tips/Checklists section, select a checklist (e.g., "12-Month Wedding Timeline"), and click "Save to Dashboard".
  - Expected: The checklist appears in the dashboard's saved items.

- [ ] FT-09: User can mark checklist items as completed
  - Action: On a saved checklist, toggle a task item to "Completed".
  - Expected: The item shows a completed state (e.g., strikethrough/checked) and completion persists on the dashboard.

## Constraint
- [ ] CS-01: Dashboard rejects invalid budget and guest count values
  - Action: Enter a negative number or non-numeric text (e.g., "abc") into Budget and Guest Count, then save.
  - Expected: Save is blocked with a visible validation error; previous valid values are retained.

- [ ] CS-02: Wedding date cannot be set in the past
  - Action: Set Wedding Date to a date before today (before 2026-11-08) and attempt to save.
  - Expected: Validation error is shown and the past date is not saved.

- [ ] CS-03: Search/filter with no matching results shows an empty state
  - Action: Search for a nonsensical keyword (e.g., "zzzqqq") or combine filters with no matches.
  - Expected: A "no results" message is displayed; the page does not error or show unrelated listings.

- [ ] CS-04: A listing cannot be favorited more than once
  - Action: Click "Favorite" on the same listing twice, then open Favorites.
  - Expected: The listing appears exactly once in Favorites (no duplicates); second click unfavorits it.

## Interaction
- [ ] IX-01: Favorite button reflects toggled state immediately
  - Action: Click the favorite icon on a listing, then click it again.
  - Expected: Icon visibly changes (e.g., filled/outline or "Save"→"Saved") on each click without a full page reload.

- [ ] IX-02: Listing results update reactively when filters or search change
  - Action: Change a filter dropdown and modify the search text.
  - Expected: The listings area refreshes instantly to match the new criteria.

- [ ] IX-03: Success feedback shown after saving
  - Action: Save dashboard edits and save a checklist to the dashboard.
  - Expected: A confirmation message/toast (e.g., "Saved successfully") appears after each save action.

## Content
- [ ] CT-01: Listing cards display complete, wedding-relevant details
  - Action: Inspect 3+ venue/vendor cards on the listings page.
  - Expected: Each card shows name, location type, price range, and service type; all content relates to wedding venues/vendors (no placeholder/lorem text).

- [ ] CT-02: Default data covers all required sections
  - Action: Check the listings, favorites, and tips/checklists areas on first load.
  - Expected: At least several pre-existing venues and vendors (with varied categories) and at least one tips/checklist collection with multiple task items are present.