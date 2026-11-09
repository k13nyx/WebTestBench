# Test Checklist

## Functionality
- [ ] FT-01: Couple can create a planning dashboard with key details
  - Action: Open the dashboard page, enter a wedding date, budget amount, and guest count, then click "Save" (or equivalent).
  - Expected: All three details (date, budget, guest count) are saved and displayed on the dashboard.
- [ ] FT-02: Couple can update existing dashboard details
  - Action: Change the wedding date, budget, and guest count to new values and save.
  - Expected: The dashboard shows the updated values (e.g., budget changes from $25,000 to $30,000 and remains after navigating away and returning).
- [ ] FT-03: Venue and vendor listings are browsable
  - Action: Navigate to the listings section and scroll through venue and vendor entries.
  - Expected: Multiple listings are displayed, covering both venues and vendors.
- [ ] FT-04: Listings can be filtered by location type
  - Action: Apply a location type filter (e.g., "Beach", "Ballroom", "Garden").
  - Expected: Only listings matching the selected location type remain visible.
- [ ] FT-05: Listings can be filtered by price range
  - Action: Select a price range filter (e.g., "$" / low-to-mid range).
  - Expected: Only listings within the selected price range are shown.
- [ ] FT-06: Listings can be filtered by service type
  - Action: Apply a service type filter (e.g., "Photography", "Catering", "Florist").
  - Expected: Only vendors offering the selected service type are shown.
- [ ] FT-07: Listings can be searched by keyword
  - Action: Type a search term matching an existing listing name (e.g., "Rose") into the search box and submit.
  - Expected: Only listings matching the keyword are displayed.
- [ ] FT-08: User can mark a listing as a favorite
  - Action: Click the favorite/heart control on a listing, then open the favorites view.
  - Expected: The listing appears in the favorites list.
- [ ] FT-09: Planning tips and checklists collection is viewable
  - Action: Navigate to the tips/checklists section.
  - Expected: A collection of planning tips and checklists is displayed with readable content.
- [ ] FT-10: User can save a tip/checklist to their dashboard
  - Action: Click "Save" (or equivalent) on a tip or checklist, then open the dashboard.
  - Expected: The saved tip/checklist appears on the dashboard.
- [ ] FT-11: User can mark a checklist item as completed
  - Action: Click the complete/checkbox control on a saved checklist item.
  - Expected: The item is marked as completed and its completed state persists.

## Constraint
- [ ] CS-01: Dashboard cannot be saved with empty required fields
  - Action: Leave the wedding date, budget, or guest count empty and attempt to save the dashboard.
  - Expected: Save is prevented and a validation message indicates the required field(s).
- [ ] CS-02: Guest count rejects invalid input
  - Action: Enter a non-numeric or negative value (e.g., "-5" or "abc") in the guest count field and save.
  - Expected: The input is rejected with a validation message; no invalid value is stored.
- [ ] CS-03: Budget rejects invalid input
  - Action: Enter a non-numeric value (e.g., "free") in the budget field and save.
  - Expected: The input is rejected with a validation message.
- [ ] CS-04: A tip/checklist cannot be saved to the dashboard twice
  - Action: Save the same tip/checklist to the dashboard, then attempt to save it again.
  - Expected: Duplicate saving is prevented or the item appears only once on the dashboard.
- [ ] CS-05: Filters combine correctly
  - Action: Apply two filters together (e.g., location type "Garden" + price range "$$").
  - Expected: Only listings matching BOTH filters are shown; no non-matching listings appear.

## Interaction
- [ ] IX-01: Saving the dashboard shows confirmation feedback
  - Action: Fill in valid details and click "Save" on the dashboard.
  - Expected: A visible success confirmation (e.g., "Dashboard saved" message) appears.
- [ ] IX-02: Favoriting shows immediate visual state change
  - Action: Click the heart/favorite icon on a listing.
  - Expected: The icon immediately switches to a "favorited" visual state (e.g., filled heart) without requiring a page reload.
- [ ] IX-03: Completed checklist item shows visual completion state
  - Action: Mark a checklist item as completed.
  - Expected: The item visibly changes state (e.g., checkbox ticked and/or strikethrough text).
- [ ] IX-04: Search/filter yielding no matches shows an empty-state message
  - Action: Search for a nonsense keyword (e.g., "zzzqqq") or filter combination with no matches.
  - Expected: A clear "no results found" message is displayed instead of a blank area.

## Content
- [ ] CT-01: Each listing displays its key details
  - Action: Inspect venue and vendor listing cards.
  - Expected: Each listing shows its name, category (venue or service type), location type, and price/range information.
- [ ] CT-02: Listing images are wedding-themed and relevant
  - Action: View all displayed images across venue and vendor listings.
  - Expected: Every image depicts wedding-relevant subjects (venues, décor, catering, photography, etc.); no unrelated or broken images appear.
- [ ] CT-03: Tips and checklists content is relevant to wedding planning
  - Action: Open several tips/checklists in the collection.
  - Expected: All content relates to wedding planning topics (e.g., budgeting, timelines, vendor booking); no off-topic content.