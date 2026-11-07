# Test Checklist

## Functionality
- [ ] FT-01: Tour catalog lists the application's default tours
  - Action: Open the site's home/catalog view.
  - Expected: A catalog of existing tours is displayed (cards/list entries with tour names); no "no tours" empty state is shown.

- [ ] FT-02: A tour can be opened from the catalog
  - Action: Click any tour entry in the catalog.
  - Expected: The tour opens and shows its first room/area with an interactive tour view (not a dead link or error).

- [ ] FT-03: User can move between rooms/areas within a tour
  - Action: In an open tour, use the next/previous room controls (or room list) to move forward and backward.
  - Expected: The displayed room changes to the selected room and its exhibits/interactive elements update accordingly.

- [ ] FT-04: Clicking an exhibit opens its layered educational content
  - Action: Click an exhibit hotspot/entry inside a room.
  - Expected: An exhibit content panel opens showing an overview plus access to a deeper dive and related items (layered content), for the clicked exhibit only.

- [ ] FT-05: Deeper-dive and related-item layers are reachable within an exhibit
  - Action: In an open exhibit panel, select the deeper-dive and related-item options.
  - Expected: Each selection loads its own distinct content (more detail / related items list) for that exhibit; closing and reopening the exhibit returns to the overview.

- [ ] FT-06: Tour quiz can be answered and scored
  - Action: Open the quiz in a tour, select an answer for a question, and submit.
  - Expected: The quiz accepts the selection and returns a result for that question (correct/incorrect and/or score) without error.

- [ ] FT-07: Tour timeline can be explored
  - Action: Open the timeline in a tour and click/select a timeline entry.
  - Expected: Each entry is displayed with its date/period and associated event description, and entries are navigable.

- [ ] FT-08: A tour can be bookmarked
  - Action: On a catalog tour entry or tour page, click the bookmark control.
  - Expected: The tour is saved to the visitor's bookmarks and is listed in the bookmarks/progress area.

- [ ] FT-09: A tour can be marked as "in progress"
  - Action: Start a tour and use the "mark as in progress" control.
  - Expected: The tour is recorded with "in progress" status and appears in the visitor's in-progress list.

- [ ] FT-10: An in-progress tour resumes at the last visited room
  - Action: Leave a tour after viewing a specific room, then resume it from the in-progress list/bookmarks.
  - Expected: The tour reopens at the same room where the visitor left off, not at the first room.

- [ ] FT-11: Search finds tours by keyword
  - Action: Enter a keyword matching a default tour's name/theme/place in the search field and submit.
  - Expected: Only matching tours are shown in the results; non-matching tours are excluded.

- [ ] FT-12: Tours can be filtered by theme, historical period, culture, and difficulty
  - Action: On the catalog/discovery view, apply each filter control in turn (theme, historical period, culture, difficulty level).
  - Expected: The result list contains only tours matching the selected filter value, and each filter selection narrows/refines the visible tours accordingly.

- [ ] FT-13: Related tour suggestions are offered at the end of a tour
  - Action: Progress through all rooms of a tour to its end.
  - Expected: A related-tours section appears with clickable suggestions of other tours, and clicking one opens that tour.

## Constraint
- [ ] CS-01: Quiz feedback reflects the actual answer key
  - Action: Answer the same quiz question with a correct option and with an incorrect option.
  - Expected: The correct option is reported as correct and the incorrect option as incorrect in both cases (feedback is not inverted or identical for both).

- [ ] CS-02: Search/filter combinations that match nothing show a clear empty state
  - Action: Enter a keyword/filter combination that matches no default tour (e.g., keyword with no matches).
  - Expected: A "no results"/"no tours found" message is displayed instead of an empty area or a leftover list of unrelated tours.

- [ ] CS-03: Progress/bookmark status holds a single consistent state per tour
  - Action: Bookmark a tour, mark it in progress, then remove/unmark it via the same controls.
  - Expected: The tour shows exactly one status at a time (bookmarked, in progress, or not started), the status displayed always matches the saved state, and removing a bookmark/mark removes it from that list.

## Interaction
- [ ] IX-01: Exhibit panel opens and closes on demand
  - Action: Click an exhibit to open its panel, then use the panel's close control (and the tour background).
  - Expected: The panel opens over the tour view and closes when requested, returning focus to the unobstructed room view.

- [ ] IX-02: Active room is visibly indicated while navigating
  - Action: Move from one room to the next using the room controls.
  - Expected: The current room is highlighted/indicated in the room navigation, and the indication updates each time the room changes.

- [ ] IX-03: Bookmark and filter selections give immediate visual feedback
  - Action: Toggle the bookmark control and apply a filter, then observe the control states.
  - Expected: The bookmark control's appearance/state changes to reflect bookmarked vs. not bookmarked, and the active filter is visibly marked as selected.

## Content
- [ ] CT-01: Catalog covers all required tour categories, including imagined places
  - Action: Review the catalog entries and their labels/descriptions.
  - Expected: Tours are present for museums, art galleries, historical sites, and cultural landmarks, and at least one tour is clearly presented as a fully imagined place rather than a real one.

- [ ] CT-02: Exhibit content and tour metadata match each tour's theme
  - Action: Open exhibits in tours of different categories and read the exhibit text, images/media, and tour metadata labels.
  - Expected: Exhibit content is about the exhibit and its museum/gallery/site shown in that tour (no unrelated or placeholder text), displayed images/media are relevant to the exhibit or place, and each tour displays correct theme, historical period, culture, and difficulty labels.