# Test Result

## Functionality

- [X] FT-01: Tour catalog lists the application's default tours
  - Action: Open the site's home/catalog view.
  - Expected: A catalog of existing tours is displayed (cards/list entries with tour names); no "no tours" empty state is shown.

- [X] FT-02: A tour can be opened from the catalog
  - Action: Click any tour entry in the catalog.
  - Expected: The tour opens and shows its first room/area with an interactive tour view (not a dead link or error).

- [X] FT-03: User can move between rooms/areas within a tour
  - Action: In an open tour, use the next/previous room controls (or room list) to move forward and backward.
  - Expected: The displayed room changes to the selected room and its exhibits/interactive elements update accordingly.

- [X] FT-04: Clicking an exhibit opens its layered educational content
  - Action: Click an exhibit hotspot/entry inside a room.
  - Expected: An exhibit content panel opens showing an overview plus access to a deeper dive and related items (layered content), for the clicked exhibit only.

- [ ] FT-05: Deeper-dive and related-item layers are reachable within an exhibit
  - Action: In an open exhibit panel, select the deeper-dive and related-item options.
  - Expected: Each selection loads its own distinct content (more detail / related items list) for that exhibit; closing and reopening the exhibit returns to the overview.
  - Bug Report:
    - Issue: Stale panel layer on reopen (no reset to Overview) / missing selectable related-item layer
    - Actual: Deeper Dive and Related Items do load distinct content (e.g. "Colossal Statue of Ramesses II" → Deep Dive text about the Nineteenth Dynasty + "Related Items: Nefertari Bust, Abu Simbel Model"; "Golden Death Mask of Tutankhamun" → Deep Dive text + "Related Items: Scarab Necklace, Royal Throne"). However, after closing the panel (via the X control and via the backdrop) and reopening the same exhibit, the panel does NOT return to the overview — it restores the previously active tab (Quiz for "Colossal Statue of Ramesses II" showing the disabled options and the stored "🎉 Correct! Well done!"; Deep Dive for "Golden Death Mask of Tutankhamun", whose active tab still carries `text-primary border-b-2 border-primary`). Additionally there is no separate "Related Items" tab/option to select — related items are static, non-clickable chips rendered inside the Deep Dive layer.

- [X] FT-06: Tour quiz can be answered and scored
  - Action: Open the quiz in a tour, select an answer for a question, and submit.
  - Expected: The quiz accepts the selection and returns a result for that question (correct/incorrect and/or score) without error.

- [X] FT-07: Tour timeline can be explored
  - Action: Open the timeline in a tour and click/select a timeline entry.
  - Expected: Each entry is displayed with its date/period and associated event description, and entries are navigable.
  - Note: All four entries render with date + event ("1303 BCE – Birth of Ramesses II", "1279 BCE – Becomes Pharaoh", "1274 BCE – Battle of Kadesh", "1213 BCE – Death of Ramesses II"); the entries are static divs (clicking one produces no state change), but the full timeline is browsable in the panel.

- [X] FT-08: A tour can be bookmarked
  - Action: On a catalog tour entry or tour page, click the bookmark control.
  - Expected: The tour is saved to the visitor's bookmarks and is listed in the bookmarks/progress area.

- [X] FT-09: A tour can be marked as "in progress"
  - Action: Start a tour and use the "mark as in progress" control.
  - Expected: The tour is recorded with "in progress" status and appears in the visitor's in-progress list.
  - Note: There is no explicit "mark as in progress" button (only "Save Tour"); the status is set automatically when a tour is opened, and the tour then appears under "In Progress" in My Collection with an "In Progress" badge.

- [X] FT-10: An in-progress tour resumes at the last visited room
  - Action: Leave a tour after viewing a specific room, then resume it from the in-progress list/bookmarks.
  - Expected: The tour reopens at the same room where the visitor left off, not at the first room.

- [X] FT-11: Search finds tours by keyword
  - Action: Enter a keyword matching a default tour's name/theme/place in the search field and submit.
  - Expected: Only matching tours are shown in the results; non-matching tours are excluded.

- [X] FT-12: Tours can be filtered by theme, historical period, culture, and difficulty
  - Action: On the catalog/discovery view, apply each filter control in turn (theme, historical period, culture, difficulty level).
  - Expected: The result list contains only tours matching the selected filter value, and each filter selection narrows/refines the visible tours accordingly.

- [ ] FT-13: Related tour suggestions are offered at the end of a tour
  - Action: Progress through all rooms of a tour to its end.
  - Expected: A related-tours section appears with clickable suggestions of other tours, and clicking one opens that tour.
  - Bug Report:
    - Issue: Application crash (blank page / React error boundary) when a related-tour suggestion is clicked
    - Actual: The "Continue Your Journey" related-tours section is present with clickable suggestions, but clicking one from a tour that is not on room 1 crashes the app: `TypeError: Cannot read properties of undefined` in TourPage and the document renders an empty body (~87 chars of HTML, no header/footer). Reproduced 4/4 times from "Mysteries of Ancient Egypt" at "Room 2 of 3" and at "Room 3 of 3" (targets "Realm of the Greek Gods" and "Glory of Rome"); the same link clicked from "Room 1 of 3" opens the tour normally.

## Constraint

- [X] CS-01: Quiz feedback reflects the actual answer key
  - Action: Answer the same quiz question with a correct option and with an incorrect option.
  - Expected: The correct option is reported as correct and the incorrect option as incorrect in both cases (feedback is not inverted or identical for both).

- [X] CS-02: Search/filter combinations that match nothing show a clear empty state
  - Action: Enter a keyword/filter combination that matches no default tour (e.g., keyword with no matches).
  - Expected: A "no results"/"no tours found" message is displayed instead of an empty area or a leftover list of unrelated tours.

- [ ] CS-03: Progress/bookmark status holds a single consistent state per tour
  - Action: Bookmark a tour, mark it in progress, then remove/unmark it via the same controls.
  - Expected: The tour shows exactly one status at a time (bookmarked, in progress, or not started), the status displayed always matches the saved state, and removing a bookmark/mark removes it from that list.
  - Bug Report:
    - Issue: Stale bookmark UI — removing a bookmark does not remove the tour from the Saved Tours list (list/count/button state do not refresh)
    - Actual: With "Mysteries of Ancient Egypt" bookmarked and in progress, "My Collection" showed "In Progress: 3" and "Saved Tours: 1" (the same card appearing in both lists, both badged "In Progress"). Clicking the card's bookmark control removed it from the persisted state (localStorage `bookmarkedTours` became `[]`), but the page still showed "Saved Tours: 1" with the Ancient Egypt card still listed, and the bookmark button on the In Progress card still rendered in the bookmarked (filled `bg-primary`) style. Only after re-loading /bookmarks did the list update to "Saved Tours: 0 / No saved tours yet".

## Interaction

- [X] IX-01: Exhibit panel opens and closes on demand
  - Action: Click an exhibit to open its panel, then use the panel's close control (and the tour background).
  - Expected: The panel opens over the tour view and closes when requested, returning focus to the unobstructed room view.

- [X] IX-02: Active room is visibly indicated while navigating
  - Action: Move from one room to the next using the room controls.
  - Expected: The current room is highlighted/indicated in the room navigation, and the indication updates each time the room changes.

- [X] IX-03: Bookmark and filter selections give immediate visual feedback
  - Action: Toggle the bookmark control and apply a filter, then observe the control states.
  - Expected: The bookmark control's appearance/state changes to reflect bookmarked vs. not bookmarked, and the active filter is visibly marked as selected.

## Content

- [X] CT-01: Catalog covers all required tour categories, including imagined places
  - Action: Review the catalog entries and their labels/descriptions.
  - Expected: Tours are present for museums, art galleries, historical sites, and cultural landmarks, and at least one tour is clearly presented as a fully imagined place rather than a real one.

- [ ] CT-02: Exhibit content and tour metadata match each tour's theme
  - Action: Open exhibits in tours of different categories and read the exhibit text, images/media, and tour metadata labels.
  - Expected: Exhibit content is about the exhibit and its museum/gallery/site shown in that tour (no unrelated or placeholder text), displayed images/media are relevant to the exhibit or place, and each tour displays correct theme, historical period, culture, and difficulty labels.
  - Bug Report:
    - Issue: Missing metadata label — the historical period is never displayed for a tour
    - Actual: Exhibit content and media are correct and topical (e.g. "The Birth of Venus" → "Painted by Sandro Botticelli around 1485… in the Uffizi Gallery in Florence, Italy" with related items "Primavera, Medici Portraits" and an unsplash image with matching alt text; "Water Lilies (Nymphéas)" → Monet/Giverny deep dive; Tutankhamun mask → "housed in the Egyptian Museum in Cairo"). Theme, culture and difficulty are shown correctly per tour (e.g. Ancient Civilizations / Egyptian / Beginner; Art History / European / Intermediate; Art History / French / Beginner; Architecture / International / Advanced; Mythology / Greek / Beginner). However, no historical-period label is rendered anywhere on a tour page or catalog card — a full-text scan of /tour/renaissance-masters, /tour/modern-architecture and /tour/greek-mythology found zero elements containing "Period", "BCE" or any year range; the period exists only as a value in the Period filter dropdown (e.g. "Renaissance (1400-1600)"), never as a displayed tour label.
