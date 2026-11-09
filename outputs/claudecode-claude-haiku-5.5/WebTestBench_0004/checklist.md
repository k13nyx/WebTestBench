# Test Checklist

## Functionality
- [ ] FT-01: Dashboard wedding date, budget, and guest count can be updated and persist after reload.
  - Action: Open the Dashboard. Change Wedding Date to a new future date, Budget to 25000, and Guest Count to 120. Click "Save". Reload the page.
  - Expected: After reload, Wedding Date shows the new date, Budget shows 25000, and Guest Count shows 120.
- [ ] FT-02: Venue and vendor listings can be browsed from their own sections.
  - Action: Click "Venues" in the main navigation, then click "Vendors".
  - Expected: Each section loads a list of default listings. Venues show venue listings only, and Vendors show vendor listings only.
- [ ] FT-03: Keyword search returns matching listings.
  - Action: On the Venues page, type a venue name from the default data (e.g., a full or partial name) into the search box and press Enter.
  - Expected: Only listings whose name matches the search term appear. The matching listing is visible in the results.
- [ ] FT-04: Venues can be filtered by location type.
  - Action: On the Venues page, select "Location Type: Outdoor" in the filter panel.
  - Expected: Only venues tagged "Outdoor" are listed. Selecting "Indoor" instead shows only "Indoor" venues.
- [ ] FT-05: Listings can be filtered by price range.
  - Action: On the Venues page, set Price Range to a min and max that match a subset of default venues (e.g., min 0, max 5000). Click "Apply".
  - Expected: Only venues whose price falls within the range are listed. No venue outside the range appears.
- [ ] FT-06: Vendors can be filtered by service type.
  - Action: On the Vendors page, select "Service Type: Photography" in the filter panel.
  - Expected: Only vendors in the "Photography" service type are listed.
- [ ] FT-07: A listing can be marked as a favorite and appears in the Favorites view.
  - Action: On the Venues page, click the heart icon on any venue. Click "Favorites" in the navigation.
  - Expected: The favorited venue appears in the Favorites list. The venue's heart icon was filled after clicking.
- [ ] FT-08: A planning tip or checklist can be saved to the dashboard.
  - Action: Click "Tips & Checklists" in the navigation. Click any tip or checklist title to open it. Click "Save to Dashboard". Go to "Dashboard".
  - Expected: The saved tip or checklist appears in the Dashboard's "Saved Items" section with the correct title.
- [ ] FT-09: A checklist item can be marked as completed and the status persists.
  - Action: Open a saved checklist from the Dashboard. Check the first unchecked item. Reload the page.
  - Expected: The item remains checked after reload.

## Constraint
- [ ] CS-01: Guest count and budget accept only non-negative numbers.
  - Action: In the Dashboard, enter -5 in Guest Count and "abc" in Budget. Click "Save".
  - Expected: Save is blocked. Each invalid field shows an error message, and the previous values remain unchanged.
- [ ] CS-02: Price range minimum cannot exceed the maximum.
  - Action: On the Venues page, set Price Range min to 8000 and max to 2000. Click "Apply".
  - Expected: The filter is not applied. An error such as "Minimum must be less than or equal to maximum" is shown, and listings are not filtered by this range.
- [ ] CS-03: Wedding date must be a future date.
  - Action: In the Dashboard, enter a past date (e.g., 2020-01-01) in Wedding Date. Click "Save".
  - Expected: Save is blocked. An error such as "Wedding date must be in the future" is shown, and the saved date is unchanged.

## Interaction
- [ ] IX-01: Saving dashboard changes shows a confirmation message.
  - Action: Change Guest Count to 100 in the Dashboard. Click "Save".
  - Expected: A confirmation message "Dashboard updated" appears and disappears after a few seconds.
- [ ] IX-02: The favorite icon toggles visually on each click.
  - Action: On the Venues page, click the heart icon on a venue once, then click it again.
  - Expected: First click fills the heart and updates the Favorites count. Second click empties the heart and decreases the count.
- [ ] IX-03: A search with no matches shows an empty-state message.
  - Action: On the Vendors page, type "zzzzqqq" in the search box and press Enter.
  - Expected: No listings appear. The message "No results found" is displayed.
- [ ] IX-04: The Save to Dashboard button changes state after saving.
  - Action: Open a tip or checklist and click "Save to Dashboard". Click the button again.
  - Expected: The button changes to "Saved" and is disabled after the first click. The item is not added to the Dashboard twice.
- [ ] IX-05: Marking a checklist item complete updates its visual state and progress.
  - Action: Open a saved checklist. Check one item.
  - Expected: The item text shows a strikethrough. The checklist progress indicator (e.g., "1 of N completed") increases by one.

## Content
- [ ] CT-01: Venue listings show relevant wedding venue content.
  - Action: On the Venues page, review each default venue card and its image.
  - Expected: Every card shows a venue name, location type, and price range. Every image loads and shows a venue or wedding-related scene. No placeholder text or broken images appear.
- [ ] CT-02: Vendor listings show the service type that matches their category.
  - Action: On the Vendors page, filter by "Service Type: Catering". Check each listed vendor.
  - Expected: Every listed vendor is a catering service, and its description refers to catering or food services. No vendor from another service type appears.
- [ ] CT-03: Planning tips and checklists are relevant to wedding planning.
  - Action: Open "Tips & Checklists" and click three different tips or checklists.
  - Expected: Each title and body text relates to wedding planning. No lorem ipsum, placeholder text, or off-topic content appears.