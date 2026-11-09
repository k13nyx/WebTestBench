All verification complete. Let me compile the final test results.

**Test execution summary:** Dashboard CRUD, listings browse/search/filters, favorites, and checklists were all exercised end-to-end with DOM-level verification (values, localStorage persistence, aria-states, image load status, toast-region polling).

---

# Test Result

## Functionality

- [X] FT-01: Planning dashboard displays existing wedding details
  - Action: Open the planning dashboard page.
  - Expected: The dashboard shows the wedding date, budget, and guest count fields, each displaying its current (default) value.
  - Verified: Dashboard (`/`) displays "Wedding Date" (default "Not set"), "Budget" ($25,000), "Guest Count" (100), plus a Planning Progress bar (0%).

- [X] FT-02: User can update the wedding date
  - Action: On the dashboard, edit the wedding date field to a new valid date and click the save/update button.
  - Expected: The dashboard displays the newly saved wedding date.
  - Verified: Opened the "Wedding Details" modal (via Get Started/Update Details), set date to `2026-06-15`, clicked Save — dashboard displays "Jun 15, 2026"; value persisted in localStorage (`weddingDetails.weddingDate`).

- [X] FT-03: User can update the budget
  - Action: On the dashboard, change the budget field to a new valid amount and save.
  - Expected: The dashboard displays the newly saved budget amount.
  - Verified: Changed budget from 25000 → 30000 and saved — dashboard displays "$30,000"; persisted in localStorage.

- [X] FT-04: User can update the guest count
  - Action: On the dashboard, change the guest count field to a new valid number and save.
  - Expected: The dashboard displays the newly saved guest count.
  - Verified: Changed guests from 100 → 150 and saved — dashboard displays "150"; persisted in localStorage.

- [X] FT-05: User can browse venue and vendor listings
  - Action: Open the venue/vendor listings page.
  - Expected: Multiple default listings (venues and vendors) are displayed, each showing at least a name and key details.
  - Verified: `/venues` shows 8 venue listings and `/vendors` shows 10 vendor listings ("Showing 8 of 8 venues" / "Showing 10 of 10 vendors"), each with name, location, rating, category/service type, price tier, and capacity/feature tags.

- [X] FT-06: User can search listings by keyword
  - Action: Type a keyword matching a default listing (e.g., part of a venue's name) into the search box.
  - Expected: Only listings matching the keyword are shown; all matching default listings appear.
  - Verified: Typed "Garden" into "Search venues..." → "Showing 2 of 8 venues": exactly "Rosewood Garden Estate" and "Meadow Brook Gardens" (both name matches). Vendor search "Bloom" likewise returned exactly "Bloom & Petal Studio" and "Budget Blooms".

- [X] FT-07: User can filter listings by location type
  - Action: Select a location type filter (e.g., Beach, Garden, Ballroom).
  - Expected: Only listings of the selected location type are displayed.
  - Verified: Filter "Ballroom" → 1 of 8 ("The Grand Ballroom"); filter "Beach" → 2 of 8 ("Sunset Beach Resort", "Coastal Haven"). Both correct, filter shows active state.

- [X] FT-08: User can filter listings by price range
  - Action: Select a price range filter (e.g., a defined min–max range).
  - Expected: Only listings whose price falls within the selected range are displayed.
  - Verified: Price Range filter offers defined tiers: Budget ($), Moderate ($$), Luxury ($$$). Selecting "Budget ($)" → "Showing 1 of 8 venues": only "Coastal Haven" (the sole Budget-tier venue).

- [X] FT-09: User can filter listings by service type
  - Action: Select a service type filter (e.g., Catering, Photography).
  - Expected: Only listings offering the selected service type are displayed.
  - Verified: On `/vendors`, Service Type filter options: Photography, Catering, Florist, Music & DJ, Cake & Desserts, Hair & Makeup, Videography, Officiant. Selecting "Catering" → "Showing 1 of 10 vendors": only "Gourmet Celebrations".

- [X] FT-10: User can mark a listing as favorite
  - Action: Click the favorite button (e.g., heart icon) on a venue/vendor listing.
  - Expected: The listing is recorded as favorited.
  - Verified: Clicked the heart on "Rosewood Garden Estate" — recorded to localStorage `favoriteVenues: ["v1"]` and rendered in "Saved Venues (1)"; dashboard "Find Venues" card counter changed from "0 saved" to "1 saved".

- [X] FT-11: User can view saved favorites later
  - Action: Navigate to the favorites section/list after marking a listing as favorite.
  - Expected: The previously favorited listing appears in the favorites list.
  - Verified: `/favorites` shows section "Saved Venues (1)" containing "Rosewood Garden Estate" with its full details (Garden, Luxury ($$$), Napa Valley CA, 4.9, capacity). Dashboard also shows it in "Your Favorites" and the favorites counter.

- [X] FT-12: User can view planning tips and checklists
  - Action: Open the planning tips/checklists page.
  - Expected: A collection of tips and checklists is displayed, and each one can be opened and read.
  - Verified: `/checklists` displays 6 planning checklists ("12+ Months Before", "8-10 Months Before", "Ceremony Planning", "Reception Details", "Wedding Attire", "Honeymoon Planning") with category filters. Each card was clicked and expanded to display its full task list with descriptions (e.g., 6 tasks for "12+ Months Before", 5 for "Wedding Attire").

- [X] FT-13: User can save a tip/checklist to the dashboard
  - Action: Click the save button on a tip/checklist.
  - Expected: The tip/checklist appears in the saved-items section of the user's dashboard.
  - Verified: Clicked "Save to Dashboard" on "12+ Months Before" — card badge changes to "Saved", localStorage `savedChecklists: ["cl1"]`, and the dashboard shows a "Your Saved Checklists" section containing "12+ Months Before" with a "0 of 6 completed" progress tracker.

- [X] FT-14: User can mark a saved checklist item as completed
  - Action: On a checklist saved to the dashboard, check off one item as completed.
  - Expected: The item is shown as completed (e.g., checkbox checked and/or strikethrough) and remains completed when the dashboard is viewed again.
  - Verified: On the saved checklist, clicked the checkbox for "Set a budget" — `aria-checked` false → true, `data-state="unchecked"` → `"checked"`, progress 0% → 17%, localStorage `completedChecklistItems: {"cl1-1": true}`. Dashboard then shows "1 of 6 completed", and re-visiting the checklists page shows the same item still checked (no strikethrough is applied, but the item is visibly checked and persists).

## Constraint

- [ ] CS-01: Dashboard rejects invalid values
  - Action: Enter an invalid value (e.g., "abc" in the budget field, or a negative number in the guest count field) and attempt to save.
  - Expected: The save is rejected and the dashboard keeps the previous valid values; the invalid value is not stored.
  - Bug Report:
    - Issue: Missing input validation on dashboard save (negative values accepted and persisted)
    - Actual: "abc" cannot be typed into the Budget field (browser `type="number"` blocks it), but negative values are freely accepted with no validation or error message: entered guest count **-10** and clicked Save → modal closed and dashboard displayed "-10" (persisted in localStorage); then entered budget **-5000** and clicked Save → dashboard displayed "$-5,000". No rejection, no error/toast, previous valid values were overwritten.

- [X] CS-02: Combined filters return only listings matching all criteria
  - Action: Apply a location type filter and a price range filter at the same time.
  - Expected: Only listings satisfying BOTH the selected location type AND price range are displayed.
  - Verified: On `/venues`, applied "Beach" (2 results) then added "Luxury ($$$)" → "Showing 1 of 8 venues": only "Sunset Beach Resort" (the only Beach venue in the Luxury tier); "Coastal Haven" (Beach, Budget) correctly excluded.

## Interaction

- [ ] IX-01: Saving dashboard details shows confirmation feedback
  - Action: Save a valid dashboard update (e.g., change the budget).
  - Expected: A visible success confirmation (toast/message) appears indicating the dashboard was updated.
  - Bug Report:
    - Issue: No feedback on save — success toast/message never appears
    - Actual: Saved valid dashboard updates four times (date, budget ×2, guest count); after each Save click the modal closes silently. The app's notifications region (`aria-label="Notifications"`, sonner `<ol>`) stayed empty in every snapshot/DOM read after saving, a DOM MutationObserver recorded no toast element being mounted, and a 125 ms × 40 (5 s) poll after Save captured zero toast items. No toast, message, or confirmation indicator of any kind appears.

- [X] IX-02: Favorite button toggles state immediately
  - Action: Click the favorite (heart) icon on a listing.
  - Expected: The icon instantly changes to its favorited state (e.g., unfilled → filled) without requiring a page reload.
  - Verified: On "Rosewood Garden Estate", the heart SVG class changed immediately on click from `lucide-heart ... text-muted-foreground` (unfilled) to `lucide-heart ... fill-primary text-primary scale-110` (filled), with no navigation/reload; state also reflects in localStorage instantly.

## Content

- [ ] CT-01: Listing details and images are wedding-relevant
  - Action: Review the venue and vendor listings, including their images and details.
  - Expected: Every listing's image and details (name, location, price, category) are relevant to weddings and accurately represent the listed venue/vendor; no broken images.
  - Bug Report:
    - Issue: Broken listing image (and duplicate/incorrect image reuse)
    - Actual: (1) The image for vendor listing "DJ Spark Entertainment" fails to load — `https://images.unsplash.com/photo-1571266028243-d220c6a8b8d1?w=800` resolves to 0×0 natural size (`complete: true`, `naturalWidth: 0`), leaving a broken/empty image area on `/vendors` and on its card in search results, while all 9 other vendor images and all 8 venue images load fine (verified across repeated page loads). (2) Additionally, venue "The Grand Ballroom" (Ballroom, Manhattan) reuses the identical image URL as "Rosewood Garden Estate" (Garden, Napa Valley) — the same photo cannot accurately represent both a garden estate and a ballroom. Text details themselves (names, locations, ratings, categories, price tiers, capacities) are present and wedding-relevant; no other broken media found.

- [X] CT-02: Tips and checklists content is wedding-planning relevant
  - Action: Read through the displayed planning tips and checklists.
  - Expected: All content is relevant to wedding planning, readable, and complete (no placeholder text or missing media).
  - Verified: All 6 checklists were opened and read — content is on-topic wedding planning ("Set a budget", "Book your venue", "Write your vows", "Schedule dress fittings", "Choose destination", etc.), fully worded descriptions, readable formatting, category labels (Planning/Ceremony/Reception/Attire/Honeymoon) functional, no placeholder/lorem text, and all images on the page load (0 broken).

---

**Overall:** 16 of 19 checks passed. Three defects found: (1) no validation of negative budget/guest-count values (CS-01), (2) no save-confirmation feedback on the dashboard (IX-01), and (3) a broken image on the DJ Spark Entertainment listing plus a duplicated image across two different venues (CT-01). Note also a minor search quirk observed (not a checklist failure): the vendor search matched "DJ Spark Entertainment" for the keyword "Photo" via its image URL rather than any displayed content; name-based searches all returned correct results.