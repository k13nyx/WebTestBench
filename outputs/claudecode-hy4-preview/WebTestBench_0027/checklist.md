# Test Checklist

## Functionality
- [ ] FT-01: Tour catalog lists available tours
  - Action: Open the home page and go to the tour catalog/browse section.
  - Expected: At least 3 tour cards are displayed, each with a title, thumbnail image, and a clickable "Start Tour" / "View Tour" action.

- [ ] FT-02: Opening a tour loads the tour at its first room/area
  - Action: Click "Start Tour" on any default tour card.
  - Expected: The tour view opens, showing the first room/area of that tour with a room/area name label visible.

- [ ] FT-03: User can move between rooms/areas within a tour
  - Action: In the tour view, click the "Next" room control, then the "Previous" room control.
  - Expected: The view advances to the next room (room name changes), and returns to the previous room on "Previous".

- [ ] FT-04: Clicking an exhibit opens its overview content
  - Action: Inside a room, click on an exhibit marker/hotspot (e.g., a painting, artifact, or placard).
  - Expected: An exhibit panel opens showing an overview: title, image, and a short descriptive text about that exhibit.

- [ ] FT-05: Exhibit panel provides a deeper-dive content layer
  - Action: In the open exhibit panel, click the deeper-dive control (e.g., "Deeper Dive", "Learn More", "Read More").
  - Expected: An expanded/detailed layer replaces or appends additional educational content beyond the overview text.

- [ ] FT-06: Exhibit panel provides related items that can be opened
  - Action: In the same exhibit panel, open the "Related Items" section and click one listed item.
  - Expected: A list of related items is shown, and clicking one opens that item's own content panel.

- [ ] FT-07: User can answer a quiz inside the tour
  - Action: Inside a room containing a quiz element, select an answer option and click "Submit" (or equivalent).
  - Expected: Feedback is displayed indicating whether the selected answer is correct or incorrect, along with the correct answer/explanation.

- [ ] FT-08: User can interact with a timeline inside the tour
  - Action: Inside a room containing a timeline, click a timeline entry/era marker.
  - Expected: Details for that entry (date/period and description text) are displayed.

- [ ] FT-09: User can bookmark a tour
  - Action: From a tour card or tour view, click the "Bookmark" / "Save" control, then open the "Bookmarks"/"Saved" list.
  - Expected: The bookmarked tour appears in the Bookmarks/Saved list.

- [ ] FT-10: User can mark a tour "In Progress" and resume where they left off
  - Action: Open a tour, advance to a room other than the first, mark/exit so it is saved as "In Progress", then click "Resume" on that tour.
  - Expected: The tour reopens directly at the last visited room/area, not the first room.

- [ ] FT-11: Search finds tours by keyword
  - Action: Type the name (or a word from the title) of a default tour into the catalog search box and submit.
  - Expected: The results list contains that tour and excludes tours whose title does not contain the keyword.

- [ ] FT-12: Filters narrow tours by theme, historical period, culture, and difficulty level
  - Action: In the catalog, apply a filter value for each of: theme, historical period, culture, and difficulty level (one at a time).
  - Expected: Each applied filter returns only tours matching that value, and the active filter is indicated in the UI.

- [ ] FT-13: Related tour suggestions are shown at the end of a tour
  - Action: Navigate to the final room/area of a tour and reach the end-of-tour view.
  - Expected: A "Related Tours" / "You may also like" section lists at least 1 suggested tour, and clicking one opens that tour.

## Constraint
- [ ] CS-01: Search or filter with no matches shows an empty state, not broken results
  - Action: Enter a nonsense search term (e.g., "zzzqqq") and/or select a filter combination with no matching default tours.
  - Expected: A clear "No tours found" (or equivalent) message is shown and no tour cards are rendered.

- [ ] CS-02: Room navigation is bounded by the first and last room
  - Action: On the first room of a tour, click "Previous"; then navigate to the last room and click "Next".
  - Expected: "Previous" is disabled/unavailable on the first room and "Next" is disabled/unavailable (or an end-of-tour view is shown) on the last room; the user cannot navigate outside the tour.

- [ ] CS-03: Bookmarking an already-bookmarked tour does not create duplicates
  - Action: Bookmark a tour, then bookmark the same tour again (or toggle the control twice), and open the Bookmarks list.
  - Expected: The tour appears only once in the Bookmarks list; re-clicking an active bookmark removes it.

## Interaction
- [ ] IX-01: Exhibit hotspots give a visible hover affordance
  - Action: Hover the mouse over an exhibit marker/hotspot in a room, then move the cursor away.
  - Expected: The hotspot visibly highlights/changes (e.g., outline, glow, label, cursor change) on hover and returns to its normal state when un-hovered.

- [ ] IX-02: Tour status updates to "In Progress" immediately
  - Action: Start a tour, advance one room, return to the catalog, and locate that tour's card.
  - Expected: The card displays an "In Progress" status/badge (or progress indicator) reflecting the current position without a page reload.

## Content
- [ ] CT-01: Catalog contains both real and imagined places
  - Action: Review the tour catalog titles and descriptions.
  - Expected: The catalog includes at least one real museum/gallery/historical site/landmark and at least one clearly fictional/imagined place, each labeled as such.

- [ ] CT-02: Tour cards display the metadata required for discovery
  - Action: Inspect any default tour card in the catalog.
  - Expected: The card shows its theme, historical period, culture, and difficulty level (as text, tags, or badges).

- [ ] CT-03: Tour content is relevant and free of placeholders
  - Action: Open a tour, visit two rooms, and open two exhibits.
  - Expected: All exhibit text is topic-relevant educational content, all images load (no broken-image icons), and no placeholder text (e.g., "lorem ipsum", "TODO", "Sample text") appears.