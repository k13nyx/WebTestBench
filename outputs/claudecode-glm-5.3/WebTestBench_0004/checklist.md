# Test Checklist

## Functionality

- [ ] FT-01: Planning dashboard displays existing wedding details
  - Action: Open the planning dashboard page.
  - Expected: The dashboard shows the wedding date, budget, and guest count fields, each displaying its current (default) value.

- [ ] FT-02: User can update the wedding date
  - Action: On the dashboard, edit the wedding date field to a new valid date and click the save/update button.
  - Expected: The dashboard displays the newly saved wedding date.

- [ ] FT-03: User can update the budget
  - Action: On the dashboard, change the budget field to a new valid amount and save.
  - Expected: The dashboard displays the newly saved budget amount.

- [ ] FT-04: User can update the guest count
  - Action: On the dashboard, change the guest count field to a new valid number and save.
  - Expected: The dashboard displays the newly saved guest count.

- [ ] FT-05: User can browse venue and vendor listings
  - Action: Open the venue/vendor listings page.
  - Expected: Multiple default listings (venues and vendors) are displayed, each showing at least a name and key details.

- [ ] FT-06: User can search listings by keyword
  - Action: Type a keyword matching a default listing (e.g., part of a venue's name) into the search box.
  - Expected: Only listings matching the keyword are shown; all matching default listings appear.

- [ ] FT-07: User can filter listings by location type
  - Action: Select a location type filter (e.g., Beach, Garden, Ballroom).
  - Expected: Only listings of the selected location type are displayed.

- [ ] FT-08: User can filter listings by price range
  - Action: Select a price range filter (e.g., a defined min–max range).
  - Expected: Only listings whose price falls within the selected range are displayed.

- [ ] FT-09: User can filter listings by service type
  - Action: Select a service type filter (e.g., Catering, Photography).
  - Expected: Only listings offering the selected service type are displayed.

- [ ] FT-10: User can mark a listing as favorite
  - Action: Click the favorite button (e.g., heart icon) on a venue/vendor listing.
  - Expected: The listing is recorded as favorited.

- [ ] FT-11: User can view saved favorites later
  - Action: Navigate to the favorites section/list after marking a listing as favorite.
  - Expected: The previously favorited listing appears in the favorites list.

- [ ] FT-12: User can view planning tips and checklists
  - Action: Open the planning tips/checklists page.
  - Expected: A collection of tips and checklists is displayed, and each one can be opened and read.

- [ ] FT-13: User can save a tip/checklist to the dashboard
  - Action: Click the save button on a tip/checklist.
  - Expected: The tip/checklist appears in the saved-items section of the user's dashboard.

- [ ] FT-14: User can mark a saved checklist item as completed
  - Action: On a checklist saved to the dashboard, check off one item as completed.
  - Expected: The item is shown as completed (e.g., checkbox checked and/or strikethrough) and remains completed when the dashboard is viewed again.

## Constraint

- [ ] CS-01: Dashboard rejects invalid values
  - Action: Enter an invalid value (e.g., "abc" in the budget field, or a negative number in the guest count field) and attempt to save.
  - Expected: The save is rejected and the dashboard keeps the previous valid values; the invalid value is not stored.

- [ ] CS-02: Combined filters return only listings matching all criteria
  - Action: Apply a location type filter and a price range filter at the same time.
  - Expected: Only listings satisfying BOTH the selected location type AND price range are displayed.

## Interaction

- [ ] IX-01: Saving dashboard details shows confirmation feedback
  - Action: Save a valid dashboard update (e.g., change the budget).
  - Expected: A visible success confirmation (toast/message) appears indicating the dashboard was updated.

- [ ] IX-02: Favorite button toggles state immediately
  - Action: Click the favorite (heart) icon on a listing.
  - Expected: The icon instantly changes to its favorited state (e.g., unfilled → filled) without requiring a page reload.

## Content

- [ ] CT-01: Listing details and images are wedding-relevant
  - Action: Review the venue and vendor listings, including their images and details.
  - Expected: Every listing's image and details (name, location, price, category) are relevant to weddings and accurately represent the listed venue/vendor; no broken images.

- [ ] CT-02: Tips and checklists content is wedding-planning relevant
  - Action: Read through the displayed planning tips and checklists.
  - Expected: All content is relevant to wedding planning, readable, and complete (no placeholder text or missing media).