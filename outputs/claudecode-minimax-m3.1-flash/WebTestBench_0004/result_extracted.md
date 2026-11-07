# Test Result

## Functionality
- [X] FT-01: Create a new planning dashboard with wedding date, budget, and guest count
  - Action: Open the dashboard/planning page, enter a wedding date, a total budget, and a guest count, then submit/save the form.
  - Expected: The dashboard is created without error and shows the entered wedding date, budget, and guest count as the couple's current plan details.
- [X] FT-02: Update the wedding date on an existing dashboard
  - Action: Locate the wedding date field on the dashboard, change it to a different valid date, and save.
  - Expected: The dashboard now displays the new wedding date, and the previous date is no longer shown.
- [X] FT-03: Update the budget and guest count on an existing dashboard
  - Action: Locate the budget and guest count fields, change each to a different valid value, and save.
  - Expected: Both the budget and the guest count on the dashboard reflect the newly entered values.
- [X] FT-04: Browse venue listings
  - Action: Navigate to the venues/listings section and view the listing page.
  - Expected: Multiple venue listings are shown using the site's default venue data, each identifiable as a venue.
- [X] FT-05: Browse vendor listings
  - Action: Navigate to the vendors/listings section and view the listing page.
  - Expected: Multiple vendor listings are shown using the site's default vendor data, each identifiable as a vendor.
- [X] FT-06: Search listings by keyword
  - Action: Type a keyword matching a default listing's name or category (e.g. a venue's name) into the search box and submit or press Enter.
  - Expected: The results are narrowed to listings matching that keyword, and non-matching listings are removed from the result set.
- [X] FT-07: Filter listings by location type
  - Action: Apply the location type filter using a value present in the default listing data.
  - Expected: Only listings with the selected location type are displayed.
- [X] FT-08: Filter listings by price range
  - Action: Apply the price range filter using a range that includes at least one default listing and excludes another.
  - Expected: Only listings whose price falls inside the selected range are displayed.
- [X] FT-09: Filter listings by service type
  - Action: Apply the service type filter using a service present in the default listing data.
  - Expected: Only listings offering the selected service type are displayed.
- [X] FT-10: Mark a listing as a favorite and view it later
  - Action: On a venue or vendor listing, click the favorite (heart/star) control, then open the Favorites section.
  - Expected: The listing is saved to the favorites collection and appears in the Favorites list.
- [X] FT-11: View planning tips and checklists
  - Action: Navigate to the planning tips/checklists section and open one of the available tips or checklists.
  - Expected: A list of tips/checklists is shown and the selected item's full content is displayed.
- [X] FT-12: Save a tip/checklist to the dashboard
  - Action: On a tip or checklist item, click its "Save to Dashboard" (or equivalent) control, then open the dashboard.
  - Expected: The saved tip/checklist appears on the dashboard as a saved planning item.
- [X] FT-13: Mark a saved tip/checklist as completed
  - Action: On the dashboard (or the checklist item), mark a saved tip/checklist item as completed.
  - Expected: The item is shown in a completed state and remains identifiable as completed on the dashboard.

## Constraint
- [ ] CS-01: Dashboard form rejects missing required details
  - Action: Submit the dashboard/create form with the wedding date, budget, or guest count left blank.
  - Expected: The form is not submitted/saved and each missing field shows a clear required-field validation message.
  - Bug Report:
    - Issue: Missing form validation — required details are silently accepted and saved
    - Actual: Clicking "Save" in the Wedding Details modal with the Wedding Date empty closed the modal and wrote to storage: `weddingDetails = {"weddingDate":"","budget":25000,...}`. Repeating with all three fields blank saved again (`{"weddingDate":"","budget":0,"guestCount":0,...}`), and the dashboard displayed "Not set" / "$0" / "0". No validation message appeared anywhere (`[role="alert"], [role="status"], .text-destructive` returned an empty list), the modal closed instead of blocking submission, and the inputs carry no `required`, `min`, or `step` attributes.
- [ ] CS-02: Budget and guest count only accept valid numeric values
  - Action: Enter a non-numeric or negative budget, and a non-integer or negative guest count, then attempt to save.
  - Expected: Invalid entries are rejected with a validation message and are not written to the dashboard; only valid positive budget and non-negative whole-number guest count values are accepted.
  - Bug Report:
    - Issue: No numeric validation — negative and fractional values are accepted and persisted
    - Actual: Entering budget `-5000` and guest count `5.5` and clicking "Save" produced no validation message; the dashboard immediately showed "$-5,000" and "5.5" and persisted `budget:-5000, guestCount:5.5`. The number inputs have no `min`/`step` attributes and no client-side validation.
- [X] CS-03: Filters and search that match nothing show an empty result state
  - Action: Combine a filter or search term that matches no listing (e.g. a price range below every listing's price) and apply it.
  - Expected: A clear "no results" message is shown and the page does not display a blank or broken listing area.
- [X] CS-04: Un-marking a favorite removes it from the favorites list
  - Action: In the Favorites section, click the favorited control on an item to unfavorite it, then reload/open the Favorites section again.
  - Expected: The item is no longer listed as a favorite and does not reappear after the page is reloaded.

## Interaction
- [X] IX-01: Favorite control reflects the current favorited state
  - Action: Observe the favorite control on a listing, click it, then click it again.
  - Expected: The control's appearance and/or label visibly change between not-favorited and favorited (e.g. filled vs. outline heart, "Favorited" label), matching the state stored for that listing.
- [X] IX-02: Saved/completed checklist items show immediate state feedback
  - Action: Save a tip/checklist to the dashboard and then toggle its completed checkbox.
  - Expected: The dashboard item list updates immediately to show the item as saved and then as completed (e.g. checked box and/or struck-through text) without a page reload.

## Content
- [X] CT-01: Listing content accurately describes each venue and vendor
  - Action: Review the visible details (name, price, location type, service type, image) on several venue and vendor listings.
  - Expected: Each listing displays accurate, coherent details for that specific venue or vendor, and every image shown is a relevant venue or vendor image (not an unrelated or generic placeholder).
- [X] CT-02: Tips and checklists contain relevant, usable wedding planning content
  - Action: Read the text of several tips and checklists in the planning tips/checklists section.
  - Expected: All content is about wedding planning and is fully written out — no lorem ipsum, "Coming soon", or empty headings/placeholder text.
