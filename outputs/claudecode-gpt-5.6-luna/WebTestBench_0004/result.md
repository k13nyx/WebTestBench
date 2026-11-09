# Test Result

## Functionality

- [X] FT-01: Couples can create a planning dashboard with wedding date, budget, and guest count.
  - Action: Open the planning dashboard, enter valid values in the “Wedding Date,” “Budget,” and “Guest Count” fields, and select “Save.”
  - Expected: A dashboard is created and displays all three entered details.

- [X] FT-02: Couples can update saved dashboard details.
  - Action: Change the wedding date, budget, or guest count on the existing dashboard and select “Save.”
  - Expected: The dashboard displays the updated values after saving and reopening it.

- [ ] FT-03: Users can browse venue listings.
  - Action: Open the venues section and review the available default venue listings.
  - Expected: Venue listing cards are displayed and can be opened to view their details.
  - Bug Report:
    - Issue: Listing detail action is unresponsive.
    - Actual: Venue cards are displayed, but selecting “View Details” produces no modal, navigation, or detail view.

- [ ] FT-04: Users can browse vendor listings.
  - Action: Open the vendors section and review the available default vendor listings.
  - Expected: Vendor listing cards are displayed and can be opened to view their details.
  - Bug Report:
    - Issue: Listing detail action is unresponsive.
    - Actual: Vendor cards are displayed, but selecting “View Profile” produces no modal, navigation, or detail view.

- [X] FT-05: Users can search venue and vendor listings by keyword.
  - Action: Enter a keyword matching a visible default venue or vendor name in the listings search field and submit the search.
  - Expected: Results include the matching listing and exclude listings that do not match the search.

- [X] FT-06: Users can filter venue listings by location type and price range.
  - Action: Select a location type and a price range from the venue filters.
  - Expected: Every displayed venue matches both selected filter values.

- [X] FT-07: Users can filter vendor listings by service type and price range.
  - Action: Select a service type and a price range from the vendor filters.
  - Expected: Every displayed vendor matches both selected filter values.

- [ ] FT-08: Users can save and later access favorite venue or vendor listings.
  - Action: Select the favorite control on a default listing, open the favorites area, and select the saved listing.
  - Expected: The listing appears in favorites and opens its original detail view.
  - Bug Report:
    - Issue: Favorite listing detail action is unresponsive.
    - Actual: The listing appears in the favorites collection, but selecting “View Details” does not open the original detail view.

- [X] FT-09: Users can view planning tips and checklists.
  - Action: Open the planning tips and checklists collection, then open an available item.
  - Expected: The selected item opens and displays its complete title and content or checklist tasks.

- [X] FT-10: Users can save a planning tip or checklist to the dashboard.
  - Action: Open a default planning tip or checklist and select “Save to Dashboard.”
  - Expected: The item appears in the dashboard’s saved planning content area.

- [X] FT-11: Users can mark a saved planning tip or checklist as completed.
  - Action: Open a saved planning tip or checklist from the dashboard and select its completion control.
  - Expected: The item is visibly marked as completed and remains completed after reopening the dashboard.

## Constraint

- [ ] CS-01: The dashboard cannot be saved with missing or invalid key details.
  - Action: Leave “Wedding Date,” “Budget,” or “Guest Count” empty or enter an invalid value, then select “Save.”
  - Expected: The dashboard is not saved, and the invalid or missing field is identified for correction.
  - Bug Report:
    - Issue: Invalid dashboard details are accepted and saved.
    - Actual: Saving with an empty wedding date, budget `-1`, and guest count `0` succeeds. The dashboard displays “Not set,” `$-1`, and `0` without identifying fields for correction.

- [X] CS-02: Combined listing filters return only listings matching every selected criterion.
  - Action: Select multiple venue or vendor filters, then inspect each result and clear the filters afterward.
  - Expected: No result violates any selected filter, and clearing the filters restores the unfiltered default listings.

- [X] CS-03: A listing cannot appear more than once in the favorites collection.
  - Action: Favorite the same venue or vendor multiple times, then open the favorites area.
  - Expected: The listing appears exactly once with one saved favorite state.

## Interaction

- [X] IX-01: Search and filter controls update the listing results after the user applies them.
  - Action: Enter a search term or change a listing filter and apply the change.
  - Expected: The results area visibly refreshes to show the matching state without requiring unrelated navigation.

- [X] IX-02: Favorite controls visibly reflect saved and unsaved states.
  - Action: Select the favorite control on a listing, then select it again.
  - Expected: The control changes to a saved state after the first selection and returns to an unsaved state after the second.

- [X] IX-03: Save and completion actions provide visible status feedback.
  - Action: Save a dashboard detail or planning item, then mark the planning item completed.
  - Expected: The interface visibly confirms the save and displays the planning item as completed.

## Content

- [X] CT-01: Venue and vendor listings display relevant identifying information.
  - Action: Open several default venue and vendor listing cards.
  - Expected: Each venue includes its location type and price information, and each vendor includes its service type and price information.

- [X] CT-02: Planning tips and checklists contain wedding-planning content.
  - Action: Review the titles, descriptions, and checklist tasks in the planning content collection.
  - Expected: Every item is directly relevant to wedding planning and contains readable, actionable content.