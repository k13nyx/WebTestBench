All testing is complete. The dashboard now shows correct labels: "Wedding Date → Dec 5, 2026", "Budget → $42,000", "Guest Count → 120" (CT-03 PASS).

# Test Result

## Functionality
- [X] FT-01: Create the planning dashboard with key details
  - Action: Open the dashboard, enter a wedding date, budget amount, and guest count, then save.
  - Expected: All three values are saved and displayed on the dashboard after saving.

- [X] FT-02: Update existing dashboard details
  - Action: Change the wedding date, budget, and guest count on the dashboard to new values and save.
  - Expected: The dashboard displays the new values (not the previous ones) after saving.

- [X] FT-03: Browse venue and vendor listings
  - Action: Open the listings page with no filters applied.
  - Expected: A list of venue and vendor items is displayed, each showing a name, category, location/price details, and an image.

- [X] FT-04: Filter listings by location type
  - Action: Select a location type filter (e.g., "Outdoor") on the listings page.
  - Expected: Only listings matching the selected location type remain visible.

- [X] FT-05: Filter listings by price range
  - Action: Select a price range filter (e.g., budget tier) on the listings page.
  - Expected: Only listings within the selected price range remain visible.

- [X] FT-06: Filter listings by service type
  - Action: Select a service type filter (e.g., "Catering") on the listings page.
  - Expected: Only listings offering the selected service type remain visible.

- [X] FT-07: Search listings by keyword
  - Action: Type a keyword matching a listing name (e.g., a venue name from the default data) into the search box.
  - Expected: The results list shows only listings whose name/details match the keyword.

- [X] FT-08: Mark a listing as favorite
  - Action: Click the favorite (heart/star) control on a listing.
  - Expected: The listing appears in the favorites view and its favorite control shows a selected/filled state.

- [X] FT-09: View planning tips and checklists
  - Action: Open the tips/checklists section.
  - Expected: A collection of planning tips and checklist items is listed, each with a title and readable content.

- [X] FT-10: Save a tip/checklist to the dashboard
  - Action: Click the save control on a tip/checklist item, then open the dashboard.
  - Expected: The saved tip/checklist item appears on the dashboard.

- [ ] FT-11: Mark a checklist item as completed
  - Action: Mark a checklist item as completed from the dashboard.
  - Expected: The item shows a completed/checked state and remains listed as completed after reloading the page.
  - Bug Report:
    - Issue: Missing Control (completion not possible from dashboard)
    - Actual: The dashboard's "Your Saved Checklists" card contains only a title, a "0 of 6 completed" label, and a progress bar — there is no checkbox or completion control, and clicking the card does nothing (URL and content unchanged). Checkboxes exist only on the /checklists page. (When completed there, state does persist and the dashboard later reflects "1 of 6 completed" after reload, but the action cannot be performed from the dashboard as specified.)

## Constraint
- [ ] CS-01: Dashboard cannot be saved with empty required fields
  - Action: Clear the wedding date (and/or budget, guest count) fields and attempt to save.
  - Expected: The save is rejected and an inline validation message identifies the empty required field(s); previous saved values remain intact.
  - Bug Report:
    - Issue: Missing Validation (empty required field accepted)
    - Actual: Clearing the wedding date and clicking Save succeeded — the form closed, no inline validation message appeared anywhere, and the previously saved date was wiped (dashboard reverted to "Wedding Date: Not set" instead of retaining "Sep 20, 2026").

- [ ] CS-02: Dashboard rejects invalid numeric values
  - Action: Enter a negative or non-numeric value in the budget and/or guest count field and attempt to save.
  - Expected: The save is rejected and a validation message indicates the value must be a valid positive number.
  - Bug Report:
    - Issue: Missing Validation (negative values accepted)
    - Actual: Budget "-5000" and guest count "-10" were saved without any error message; the form closed and the dashboard displayed "Budget: $-5,000" and "Guest Count: -10".

- [X] CS-03: Combined filters do not show non-matching listings
  - Action: Apply two filters simultaneously (e.g., location type "Outdoor" + a low price range).
  - Expected: Every visible listing satisfies both filters; no listing appears that matches only one of them.

- [X] CS-04: Search with no matches shows an empty state, not all items
  - Action: Enter a keyword that matches no listing (e.g., "zzzznonexistent") in the search box.
  - Expected: An explicit "no results" message is shown and no unrelated listings are displayed.

- [X] CS-05: A listing cannot be duplicated in favorites
  - Action: Click the favorite control on an already-favorited listing.
  - Expected: The listing remains a single entry in the favorites view (it is unfavorited or stays favorited once — never duplicated).

- [ ] CS-06: A checklist item cannot be saved to the dashboard twice
  - Action: Save the same tip/checklist item to the dashboard, then attempt to save it again.
  - Expected: The dashboard shows the item exactly once.
  - Bug Report:
    - Issue: Save Toggle Removes Item on Second Attempt (0 copies instead of exactly 1)
    - Actual: After saving "12+ Months Before", its button changes to "Saved"; clicking that control again un-saves the item — the card reverts to "Available / Save to Dashboard" and the dashboard shows the item 0 times (it was removed rather than remaining saved exactly once). No duplicate was ever created, but the final state is not "exactly once".

## Interaction
- [ ] IX-01: Favorite control gives immediate visual feedback
  - Action: Click the favorite control on a listing.
  - Expected: The control instantly changes to its selected/filled state, and a toast/notification confirms the item was added to favorites.
  - Bug Report:
    - Issue: Missing Toast/Notification
    - Actual: The heart instantly changes to the filled state (svg class gains "fill-primary text-primary scale-110", pink color), but no toast/notification appears — polling for 1.5s after the click found zero toast/status elements in the DOM (the notification region's list stays empty).

- [X] IX-02: Filter and search results update immediately
  - Action: Change a filter selection or type in the search box.
  - Expected: The listing results update without a page reload, and a visible indication (result count or loading state) reflects the change.

- [ ] IX-03: Completing a checklist item gives immediate feedback
  - Action: Mark a checklist item as completed.
  - Expected: The item's checkbox/state updates instantly and a success toast/notification confirms completion.
  - Bug Report:
    - Issue: Missing Success Toast/Notification
    - Actual: The checkbox flips "unchecked" → "checked" instantly and progress updates to 17% (persisting after reload), but no success toast/notification appears — DOM polling over 1.2s after the click found no toast/status/alert elements.

- [ ] IX-04: Saving the dashboard confirms success
  - Action: Save valid dashboard details.
  - Expected: A success message/toast appears and the form shows the just-saved values without requiring a manual refresh.
  - Bug Report:
    - Issue: Missing Success Message/Toast on Save
    - Actual: After clicking Save, the form closes and the dashboard shows the just-saved values without refresh (e.g., "$50,000"), but no success message/toast ever appears — repeated polling (up to 1.5s per save, multiple saves) found zero toast elements in the DOM.

## Content
- [ ] CT-01: Listings display complete, relevant details
  - Action: Open the listings page and inspect each visible listing card.
  - Expected: Every card shows a wedding-relevant name, an image relevant to the venue/service, a location, a price, and its category labels — no placeholder text (e.g., "Lorem ipsum", "TODO", broken images).
  - Bug Report:
    - Issue: Broken Image on Listing Card
    - Actual: On the Vendors page, the "DJ Spark Entertainment" card's image fails to load (img complete=true, naturalWidth=0 after 2.5s, src https://images.unsplash.com/photo-1571266028243-d220c6a8b8d1?w=800 — verified broken on two separate checks). All other cards (8 venues + 9 vendors) have loaded images, correct names, locations, price tiers, and category labels, and no placeholder text ("Lorem ipsum"/"TODO") was found anywhere.

- [X] CT-02: Tips and checklists contain wedding-planning content
  - Action: Open the tips/checklists section and open at least three items.
  - Expected: Each item shows complete, readable wedding-planning advice or actionable checklist steps — no empty, truncated, or off-topic content.

- [X] CT-03: Dashboard displays values in correct labeled fields
  - Action: After saving, inspect the dashboard.
  - Expected: The wedding date appears formatted as a date under a "Wedding Date" label, the budget appears with a currency format under a "Budget" label, and the guest count appears as a number under a "Guest Count" label — values are not swapped or mislabeled.

---

**Summary:** 14 PASS / 9 FAIL. The app's filtering, search, favorites, checklist saving, and dashboard CRUD work correctly, but it has systemic gaps: **no toast/notification system fires at all** (IX-01/03/04), **no dashboard form validation** (CS-01/02), **no completion control on the dashboard** (FT-11), a **save-toggle quirk** that removes items on second click (CS-06), and **one broken vendor image** (CT-01).