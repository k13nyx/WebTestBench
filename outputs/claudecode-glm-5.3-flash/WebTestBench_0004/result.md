All 22 checks executed. Here is the full result:

# Test Result

## Functionality

- [X] FT-01: Couple can create a planning dashboard with key details
  - Action: Open the dashboard page, enter a wedding date, budget amount, and guest count, then click "Save" (or equivalent).
  - Expected: All three details (date, budget, guest count) are saved and displayed on the dashboard.
- [X] FT-02: Couple can update existing dashboard details
  - Action: Change the wedding date, budget, and guest count to new values and save.
  - Expected: The dashboard shows the updated values (e.g., budget changes from $25,000 to $30,000 and remains after navigating away and returning).
- [X] FT-03: Venue and vendor listings are browsable
  - Action: Navigate to the listings section and scroll through venue and vendor entries.
  - Expected: Multiple listings are displayed, covering both venues and vendors.
- [X] FT-04: Listings can be filtered by location type
  - Action: Apply a location type filter (e.g., "Beach", "Ballroom", "Garden").
  - Expected: Only listings matching the selected location type remain visible.
- [X] FT-05: Listings can be filtered by price range
  - Action: Select a price range filter (e.g., "$" / low-to-mid range).
  - Expected: Only listings within the selected price range are shown.
- [X] FT-06: Listings can be filtered by service type
  - Action: Apply a service type filter (e.g., "Photography", "Catering", "Florist").
  - Expected: Only vendors offering the selected service type are shown.
- [X] FT-07: Listings can be searched by keyword
  - Action: Type a search term matching an existing listing name (e.g., "Rose") into the search box and submit.
  - Expected: Only listings matching the keyword are displayed.
- [X] FT-08: User can mark a listing as a favorite
  - Action: Click the favorite/heart control on a listing, then open the favorites view.
  - Expected: The listing appears in the favorites list.
- [X] FT-09: Planning tips and checklists collection is viewable
  - Action: Navigate to the tips/checklists section.
  - Expected: A collection of planning tips and checklists is displayed with readable content.
- [X] FT-10: User can save a tip/checklist to their dashboard
  - Action: Click "Save" (or equivalent) on a tip or checklist, then open the dashboard.
  - Expected: The saved tip/checklist appears on the dashboard.
- [X] FT-11: User can mark a checklist item as completed
  - Action: Click the complete/checkbox control on a saved checklist item.
  - Expected: The item is marked as completed and its completed state persists.

## Constraint

- [ ] CS-01: Dashboard cannot be saved with empty required fields
  - Action: Leave the wedding date, budget, or guest count empty and attempt to save the dashboard.
  - Expected: Save is prevented and a validation message indicates the required field(s).
  - Bug Report:
    - Issue: Missing Input Validation / Incorrect Form Submission
    - Actual: With wedding date cleared, budget empty, and guest count empty, clicking "Save" succeeded — the form closed and the dashboard stored Date "Not set", Budget "$0", and Guest Count "0". No validation message appeared, and inputs have no `required` attribute.
- [ ] CS-02: Guest count rejects invalid input
  - Action: Enter a non-numeric or negative value (e.g., "-5" or "abc") in the guest count field and save.
  - Expected: The input is rejected with a validation message; no invalid value is stored.
  - Bug Report:
    - Issue: Missing Input Validation
    - Actual: Guest count "-5" was accepted and saved; the dashboard displays "Guest Count -5". No validation message appears. ("abc" cannot be typed into the native number input, but there is no app-level validation message and no `min` attribute to block negatives.)
- [ ] CS-03: Budget rejects invalid input
  - Action: Enter a non-numeric value (e.g., "free") in the budget field and save.
  - Expected: The input is rejected with a validation message.
  - Bug Report:
    - Issue: Missing Input Validation
    - Actual: No validation message is shown for any budget input. Typing "free" into the number input is silently ignored by the browser (no app feedback), and a negative value "-1000" was accepted and saved, displayed as "Budget $-1,000". No `required`, `min`, or validation message exists.
- [X] CS-04: A tip/checklist cannot be saved to the dashboard twice
  - Action: Save the same tip/checklist to the dashboard, then attempt to save it again.
  - Expected: Duplicate saving is prevented or the item appears only once on the dashboard.
- [X] CS-05: Filters combine correctly
  - Action: Apply two filters together (e.g., location type "Garden" + price range "$$").
  - Expected: Only listings matching BOTH filters are shown; no non-matching listings appear.

## Interaction

- [ ] IX-01: Saving the dashboard shows confirmation feedback
  - Action: Fill in valid details and click "Save" on the dashboard.
  - Expected: A visible success confirmation (e.g., "Dashboard saved" message) appears.
  - Bug Report:
    - Issue: Missing Feedback / No Response Confirmation
    - Actual: Saving valid details (Aug 21, 2027 / $30,000 / 120) produced no visible confirmation. A MutationObserver watching the entire document captured zero added elements after clicking Save — no toast, alert, status region, or inline success message appears; the form simply closes silently.
- [X] IX-02: Favoriting shows immediate visual state change
  - Action: Click the heart/favorite icon on a listing.
  - Expected: The icon immediately switches to a "favorited" visual state (e.g., filled heart) without requiring a page reload.
- [X] IX-03: Completed checklist item shows visual completion state
  - Action: Mark a checklist item as completed.
  - Expected: The item visibly changes state (e.g., checkbox ticked and/or strikethrough text).
- [X] IX-04: Search/filter yielding no matches shows an empty-state message
  - Action: Search for a nonsense keyword (e.g., "zzzqqq") or filter combination with no matches.
  - Expected: A clear "no results found" message is displayed instead of a blank area.

## Content

- [X] CT-01: Each listing displays its key details
  - Action: Inspect venue and vendor listing cards.
  - Expected: Each listing shows its name, category (venue or service type), location type, and price/range information.
- [ ] CT-02: Listing images are wedding-themed and relevant
  - Action: View all displayed images across venue and vendor listings.
  - Expected: Every image depicts wedding-relevant subjects (venues, décor, catering, photography, etc.); no unrelated or broken images appear.
  - Bug Report:
    - Issue: Broken Image
    - Actual: The "DJ Spark Entertainment" vendor card's image (https://images.unsplash.com/photo-1571266028243-d220c6a8b8d1?w=800) fails to load — `complete=true` but `naturalWidth=0` even after the page fully settled, indicating a broken/unavailable image. All other venue and vendor images load correctly (naturalWidth=800) with wedding-relevant alt text.
- [X] CT-03: Tips and checklists content is relevant to wedding planning
  - Action: Open several tips/checklists in the collection.
  - Expected: All content relates to wedding planning topics (e.g., budgeting, timelines, vendor booking); no off-topic content.

---
**Summary: 18 PASS / 4 FAIL.** Failures: CS-01, CS-02, CS-03 (no validation on the dashboard form — empty, zero, and negative values all save without any validation message), IX-01 (no save confirmation feedback), and CT-02 (one broken vendor image on "DJ Spark Entertainment").