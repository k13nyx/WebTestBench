# Test Checklist

## Functionality
- [ ] FT-01: Create the planning dashboard with key details
  - Action: Open the dashboard, enter a wedding date, budget amount, and guest count, then save.
  - Expected: All three values are saved and displayed on the dashboard after saving.

- [ ] FT-02: Update existing dashboard details
  - Action: Change the wedding date, budget, and guest count on the dashboard to new values and save.
  - Expected: The dashboard displays the new values (not the previous ones) after saving.

- [ ] FT-03: Browse venue and vendor listings
  - Action: Open the listings page with no filters applied.
  - Expected: A list of venue and vendor items is displayed, each showing a name, category, location/price details, and an image.

- [ ] FT-04: Filter listings by location type
  - Action: Select a location type filter (e.g., "Outdoor") on the listings page.
  - Expected: Only listings matching the selected location type remain visible.

- [ ] FT-05: Filter listings by price range
  - Action: Select a price range filter (e.g., budget tier) on the listings page.
  - Expected: Only listings within the selected price range remain visible.

- [ ] FT-06: Filter listings by service type
  - Action: Select a service type filter (e.g., "Catering") on the listings page.
  - Expected: Only listings offering the selected service type remain visible.

- [ ] FT-07: Search listings by keyword
  - Action: Type a keyword matching a listing name (e.g., a venue name from the default data) into the search box.
  - Expected: The results list shows only listings whose name/details match the keyword.

- [ ] FT-08: Mark a listing as favorite
  - Action: Click the favorite (heart/star) control on a listing.
  - Expected: The listing appears in the favorites view and its favorite control shows a selected/filled state.

- [ ] FT-09: View planning tips and checklists
  - Action: Open the tips/checklists section.
  - Expected: A collection of planning tips and checklist items is listed, each with a title and readable content.

- [ ] FT-10: Save a tip/checklist to the dashboard
  - Action: Click the save control on a tip/checklist item, then open the dashboard.
  - Expected: The saved tip/checklist item appears on the dashboard.

- [ ] FT-11: Mark a saved checklist item as completed
  - Action: Mark a checklist item as completed from the dashboard.
  - Expected: The item shows a completed/checked state and remains listed as completed after reloading the page.

## Constraint
- [ ] CS-01: Dashboard cannot be saved with empty required fields
  - Action: Clear the wedding date (and/or budget, guest count) fields and attempt to save.
  - Expected: The save is rejected and an inline validation message identifies the empty required field(s); previous saved values remain intact.

- [ ] CS-02: Dashboard rejects invalid numeric values
  - Action: Enter a negative or non-numeric value in the budget and/or guest count field and attempt to save.
  - Expected: The save is rejected and a validation message indicates the value must be a valid positive number.

- [ ] CS-03: Combined filters do not show non-matching listings
  - Action: Apply two filters simultaneously (e.g., location type "Outdoor" + a low price range).
  - Expected: Every visible listing satisfies both filters; no listing appears that matches only one of them.

- [ ] CS-04: Search with no matches shows an empty state, not all items
  - Action: Enter a keyword that matches no listing (e.g., "zzzznonexistent") in the search box.
  - Expected: An explicit "no results" message is shown and no unrelated listings are displayed.

- [ ] CS-05: A listing cannot be duplicated in favorites
  - Action: Click the favorite control on an already-favorited listing.
  - Expected: The listing remains a single entry in the favorites view (it is unfavorited or stays favorited once — never duplicated).

- [ ] CS-06: A checklist item cannot be saved to the dashboard twice
  - Action: Save the same tip/checklist item to the dashboard, then attempt to save it again.
  - Expected: The dashboard shows the item exactly once.

## Interaction
- [ ] IX-01: Favorite control gives immediate visual feedback
  - Action: Click the favorite control on a listing.
  - Expected: The control instantly changes to its selected/filled state, and a toast/notification confirms the item was added to favorites.

- [ ] IX-02: Filter and search results update immediately
  - Action: Change a filter selection or type in the search box.
  - Expected: The listing results update without a page reload, and a visible indication (result count or loading state) reflects the change.

- [ ] IX-03: Completing a checklist item gives immediate feedback
  - Action: Mark a checklist item as completed.
  - Expected: The item's checkbox/state updates instantly and a success toast/notification confirms completion.

- [ ] IX-04: Saving the dashboard confirms success
  - Action: Save valid dashboard details.
  - Expected: A success message/toast appears and the form shows the just-saved values without requiring a manual refresh.

## Content
- [ ] CT-01: Listings display complete, relevant details
  - Action: Open the listings page and inspect each visible listing card.
  - Expected: Every card shows a wedding-relevant name, an image relevant to the venue/service, a location, a price, and its category labels — no placeholder text (e.g., "Lorem ipsum", "TODO", broken images).

- [ ] CT-02: Tips and checklists contain wedding-planning content
  - Action: Open the tips/checklists section and open at least three items.
  - Expected: Each item shows complete, readable wedding-planning advice or actionable checklist steps — no empty, truncated, or off-topic content.

- [ ] CT-03: Dashboard displays values in correct labeled fields
  - Action: After saving, inspect the dashboard.
  - Expected: The wedding date appears formatted as a date under a "Wedding Date" label, the budget appears with a currency format under a "Budget" label, and the guest count appears as a number under a "Guest Count" label — values are not swapped or mislabeled.