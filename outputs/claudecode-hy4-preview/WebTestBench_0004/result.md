# Test Result

## Functionality

- [X] FT-01: Planning dashboard can be created and updated with wedding date, budget, and guest count
  - Action: Open the Dashboard page, enter a wedding date (e.g., 2027-06-12), a budget (e.g., 25000), and a guest count (e.g., 150) into the corresponding fields, click "Save". Then change only the Budget value (e.g., 30000) and click "Save"/"Update".
  - Expected: All three values are displayed on the dashboard after saving; after the update, the Budget shows the new value (30000) and the wedding date and guest count remain unchanged.

- [X] FT-02: User can browse venue and vendor listings
  - Action: Open the Venues / Vendors listings page using the default data.
  - Expected: At least 3 default listings are displayed, and each listing shows its name, service type, location, and price.

- [X] FT-03: User can search listings by keyword
  - Action: Type the exact name of one default listing (visible in the unfiltered list) into the search box and submit.
  - Expected: Only the matching listing(s) are displayed; all non-matching listings are hidden.

- [X] FT-04: User can filter listings by service type
  - Action: Open the "Service Type" filter and select one category (e.g., Venue, Photographer, or Caterer).
  - Expected: Only listings belonging to that service type are displayed; listings of other service types are hidden.

- [X] FT-05: User can filter listings by price range
  - Action: Open the "Price Range" filter and select one range (e.g., the lowest available range).
  - Expected: Only listings whose displayed price falls within the selected range are shown; out-of-range listings are hidden.

- [X] FT-06: User can filter listings by location type
  - Action: Open the "Location Type" filter and select one type (e.g., Outdoor, Beach, or Indoor).
  - Expected: Only listings matching the selected location type are displayed; others are hidden.

- [X] FT-07: User can add and remove favorites
  - Action: On any default listing, click its Favorite (heart) button, then open the "Favorites" page/section. Click the Favorite button again on that same listing.
  - Expected: After the first click, the listing appears in Favorites. After the second click, the listing is removed from Favorites.

- [X] FT-08: User can view the planning tips and checklists collection
  - Action: Open the Tips / Checklists page using the default data.
  - Expected: A collection of planning tips and/or checklists is displayed, and at least one checklist can be opened to reveal its individual tasks.

- [ ] FT-09: User can save a checklist to their dashboard
  - Action: Open one default checklist and click "Save to Dashboard" (or equivalent), then open the Dashboard page.
  - Expected: The saved checklist (title and its tasks) is listed on the Dashboard.
  - Bug Report:
    - Issue: Incomplete Data Rendering / Missing Content
    - Actual: After saving "12+ Months Before", the Dashboard's "Your Saved Checklists" section renders only the title and "0 of 6 completed" plus a progress bar. The individual tasks ("Set a budget", "Choose a wedding date", "Book your venue", "Start your guest list", "Hire a wedding planner", "Book photographer & videographer") are never listed on the Dashboard, and clicking the saved checklist card does not expand it (no checkbox or task element exists anywhere in `main`).

- [ ] FT-10: User can mark a checklist task as completed
  - Action: On a saved checklist on the Dashboard, click the checkbox/complete control on one task.
  - Expected: That task is recorded as completed; the remaining tasks stay incomplete.
  - Bug Report:
    - Issue: Missing Interactive Control
    - Actual: The saved checklist on the Dashboard has no checkbox or complete control — a DOM query for `[role="checkbox"]` on the Dashboard returns 0 elements. Task completion is only possible on the separate /checklists page, so the action described cannot be performed on the Dashboard.

## Constraint

- [X] CS-01: Search with no matches shows an empty-state message instead of an error or blank page
  - Action: Type a nonsense string with no relation to any listing (e.g., "zzzqqq123") into the search box and submit.
  - Expected: A "No results found" (or equivalent) message is displayed, the listings area is empty, and the page remains usable (filters still present).

- [ ] CS-02: Dashboard rejects invalid detail values
  - Action: On the Dashboard, enter a non-numeric value (e.g., "abc") into the Budget field and click "Save".
  - Expected: The invalid value is not saved; an inline validation message is shown and the previously saved valid value remains displayed.
  - Bug Report:
    - Issue: Missing Form Validation
    - Actual: The app performs no validation of its own. Typing "abc" is rejected only by the browser's native `input type="number"` handling (the field silently keeps its old value, Playwright reports "Cannot type text into input[type=number]"), and clicking "Save" then saves the form with no inline error message of any kind. Confirming the absence of app-level validation: entering `-5` in Budget and clicking "Save" was accepted and the Dashboard displayed "$-5" with no validation message.

- [ ] CS-03: Favorites and saved checklists cannot contain duplicate entries
  - Action: Favorite a default listing from the listings page, then open that same listing's detail view and click its Favorite button again. Also click "Save to Dashboard" twice on the same checklist.
  - Expected: The listing appears exactly once in Favorites, and the checklist appears exactly once on the Dashboard.
  - Bug Report:
    - Issue: Incorrect Toggle Behavior / Missing Detail View
    - Actual: "Save to Dashboard" is not idempotent — after the first click the button reads "Saved" and the checklist appears under "Your Saved Checklists"; clicking it a second time toggles it back to "Save to Dashboard" and the checklist is removed from the Dashboard entirely (the "Your Saved Checklists" section disappears). For the favorites half, the action cannot be completed: there is no listing detail view at all — the "View Details" button produces no navigation (URL stays `http://localhost:6004/venues`), no modal/dialog opens, and the cards/images are not clickable (a gradient overlay intercepts pointer events).

- [X] CS-04: Dashboard details, favorites, and completed tasks persist after a page reload
  - Action: After FT-01, FT-07, and FT-10, reload the browser page.
  - Expected: The saved wedding date, budget, and guest count, the favorited listing, and the completed-task state all remain exactly as they were before the reload.

## Interaction

- [X] IX-01: Favorite button reflects its toggled state immediately
  - Action: Click the Favorite (heart) button on a default listing without reloading the page.
  - Expected: The button visually changes to an active/filled favorite state on click, and reverts to its inactive state when clicked again.

- [ ] IX-02: Success confirmation is shown after the dashboard is saved
  - Action: Change any dashboard field (e.g., guest count) and click "Save".
  - Expected: A success toast or confirmation message (e.g., "Dashboard saved") is displayed without requiring a page reload.
  - Bug Report:
    - Issue: Missing User Feedback / No Confirmation
    - Actual: After changing the guest count and clicking "Save", no toast or confirmation message appeared. The notification infrastructure exists but stays empty: `document.querySelector('section[aria-label="Notifications (F8)"] ol')` is empty and the `aria-live="polite"` region has no text, sampled at 100 ms, 400 ms, 700 ms, 1 s, and 2.5 s after the click.

- [ ] IX-03: Completed checklist task shows a completed visual state immediately
  - Action: Click the complete control on a dashboard checklist task without reloading the page.
  - Expected: The task immediately renders in a completed state (checked checkbox and/or strikethrough styling).
  - Bug Report:
    - Issue: Missing Interactive Control / Missing Visual State
    - Actual: No complete control exists on the Dashboard's saved checklist (0 elements with `role="checkbox"` in the Dashboard DOM), so no task can be rendered in a completed state there. The correct visual state does render on the /checklists page (`data-state="checked"`, check icon, `line-through text-muted-foreground` label), but that state is never surfaced on the Dashboard, which only updates the counter text to "1 of 6 completed".

## Content

- [X] CT-01: Listings display relevant, complete wedding vendor information
  - Action: Inspect every default listing on the listings page.
  - Expected: Each listing shows a real name, service type, location, and price with no placeholder or unrelated text (e.g., no "Lorem ipsum", "Sample", "Test item").

- [ ] CT-02: Listing images/icons are wedding-related and load correctly
  - Action: View the listings page and one listing detail view.
  - Expected: Every image/icon loads (no broken-image icon or empty frame) and each depicts a wedding venue, vendor service, or wedding-related scene.
  - Bug Report:
    - Issue: Broken Image
    - Actual: On the /vendors listings page, the image for "DJ Spark Entertainment" fails to load — `<img src="https://images.unsplash.com/photo-1571266028243-d220c6a8b8d1?w=800" alt="DJ Spark Entertainment">` reports `naturalWidth: 0, naturalHeight: 0` (complete=true indicates an error state), leaving an empty/broken frame. All other venue and vendor images loaded (naturalWidth 800). Additionally, the "one listing detail view" part of the action cannot be performed because no listing detail view exists (see CS-03).

- [X] CT-03: Tips and checklists content is specific to wedding planning
  - Action: Read the titles and tasks of all default tips/checklists.
  - Expected: Every tip and task relates to planning a wedding (e.g., booking a venue, sending invitations, arranging catering); no content from an unrelated domain appears.