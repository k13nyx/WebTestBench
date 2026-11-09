# Test Checklist

## Functionality
- [ ] FT-01: Couple can create a planning dashboard and save key details
  - Action: Open the dashboard, enter a wedding date, budget, and guest count, then click "Save".
  - Expected: Dashboard is created and shows the entered wedding date, budget, and guest count.

- [ ] FT-02: Couple can update existing dashboard details
  - Action: Change the wedding date, budget, and guest count on a saved dashboard and click "Save".
  - Expected: The dashboard updates and displays the new values (not the old ones).

- [ ] FT-03: User can browse venue and vendor listings
  - Action: Open the listings page for venues and vendors.
  - Expected: A list of venue and vendor listings is displayed with multiple entries.

- [ ] FT-04: User can search listings by keyword
  - Action: Type a keyword (e.g., a listing name) into the search field and submit.
  - Expected: Only listings matching the keyword are shown; non-matching listings are hidden.

- [ ] FT-05: User can filter listings by location type, price range, and service type
  - Action: Apply a location type filter, a price range filter, and a service type filter to the listings.
  - Expected: Displayed listings match all selected filter criteria for each category.

- [ ] FT-06: User can mark a listing as a favorite
  - Action: Click the favorite control on a listing card.
  - Expected: The listing is marked as a favorite.

- [ ] FT-07: User can view saved favorites
  - Action: Open the favorites view after marking one or more listings as favorite.
  - Expected: All previously favorited listings are listed in the favorites view.

- [ ] FT-08: User can view the collection of planning tips and checklists
  - Action: Open the planning tips and checklists section.
  - Expected: A collection of tips/checklists is displayed for viewing.

- [ ] FT-09: User can save a tip or checklist to the dashboard
  - Action: On a tip/checklist, click "Save" (or equivalent).
  - Expected: The selected tip/checklist is added to and shown on the dashboard.

- [ ] FT-10: User can mark a checklist item as completed
  - Action: On a saved checklist, mark an item as completed.
  - Expected: The item is recorded as completed and reflected in the checklist state.

## Constraint
- [ ] CS-01: Dashboard cannot be saved with empty required fields
  - Action: Leave wedding date, budget, or guest count empty and click "Save".
  - Expected: Save is blocked and a validation message identifies the missing required field(s).

- [ ] CS-02: Guest count accepts only valid numbers
  - Action: Enter a non-numeric or negative value in the guest count field and click "Save".
  - Expected: Save is blocked with a validation message; no invalid guest count is stored.

- [ ] CS-03: Un-favoriting removes a listing from favorites
  - Action: Click the favorite control on a listing that is already favorited.
  - Expected: The listing is removed from the favorites view; no duplicate or stale favorite remains.

## Interaction
- [ ] IX-01: Confirmation shown after saving the dashboard
  - Action: Enter valid dashboard details and click "Save".
  - Expected: A success confirmation (e.g., "Saved" message/toast) is displayed.

- [ ] IX-02: Favorite control toggles visual state immediately
  - Action: Click the favorite control on a listing.
  - Expected: The control visibly changes state (e.g., filled vs. unfilled) without a page reload.

- [ ] IX-03: Checklist item shows completed state when marked done
  - Action: Mark a checklist item as completed.
  - Expected: The item visually reflects completion (e.g., checkmark or strikethrough).

- [ ] IX-04: No-results message shown when filters/search match nothing
  - Action: Apply filters or a search term that matches no listings.
  - Expected: A clear "no results" message is displayed instead of an empty or stale list.

## Content
- [ ] CT-01: Dashboard displays the required labeled fields
  - Action: View the planning dashboard.
  - Expected: Fields are labeled "Wedding Date", "Budget", and "Guest Count", matching the instruction.

- [ ] CT-02: Listings show wedding-relevant attributes
  - Action: Inspect venue and vendor listing cards.
  - Expected: Listings display relevant details such as location type, price range, and service type.

- [ ] CT-03: Tips, checklists, and media are wedding-planning relevant
  - Action: Review the tips/checklists content and their accompanying images/icons.
  - Expected: All text and media are directly relevant to wedding planning; no unrelated content is present.