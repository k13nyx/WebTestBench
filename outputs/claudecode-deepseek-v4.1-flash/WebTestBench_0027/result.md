I have completed all tests. Here is the full checklist with results.

# Test Result

## Functionality

- [ ] FT-01: Catalog displays all available tours in a browsable list/grid
  - Action: Open the site and land on/return to the tour catalog
  - Expected: Tour cards appear, each showing a title and its theme, historical period, culture, and difficulty level
  - Bug Report:
    - Issue: Missing required category metadata on catalog cards
    - Actual: All 6 cards render title + a single theme badge + a difficulty badge only (card inner text e.g. "Ancient Civilizations | Beginner | Mysteries of Ancient Egypt | Journey Through the Land of Pharaohs | 45 min | 3 rooms"). Neither the historical period nor the culture is shown on any card (culture "Egyptian" appears only on the tour detail page; the historical period is never displayed anywhere as a tag).

- [X] FT-02: User can open a tour from the catalog
  - Action: Click a tour card in the catalog
  - Expected: The selected tour opens and its first room/area is displayed

- [X] FT-03: User can move between rooms/areas within a tour
  - Action: Inside a tour, navigate to a next/adjacent room using the provided navigation control
  - Expected: The new room/area loads with its own exhibits visible

- [X] FT-04: Clicking an exhibit opens its overview content layer
  - Action: Click any visible exhibit inside a room
  - Expected: An overview panel (text/media) for that exhibit opens

- [X] FT-05: Exhibit content provides deeper-dive and related-items layers
  - Action: From an open exhibit overview, select the deeper-dive option, then the related-items option
  - Expected: A deeper-dive content layer opens, and a related-items layer lists other linked exhibits

- [X] FT-06: A quiz interaction works inside the tour
  - Action: Locate the quiz within the tour and answer its question(s)
  - Expected: The selected answer is evaluated and correct/incorrect feedback is shown

- [ ] FT-07: A timeline interaction works inside the tour
  - Action: Locate the timeline and interact with it (select/move to a timeline entry)
  - Expected: The timeline responds and displays the content tied to the selected point
  - Bug Report:
    - Issue: Non-interactive timeline (static content only)
    - Actual: The Timeline tab renders a static list of entries (e.g. "1303 BCE – Birth of Ramesses II", "1274 BCE – Battle of Kadesh"). The container holds 0 buttons/links/`[role=button]`/`[tabindex]` elements, entries are plain `<div>`/`<p>` with default cursor, and clicking an entry ("Battle of Kadesh") produces no response and no change to the displayed content.

- [X] FT-08: User can bookmark a tour
  - Action: Click the bookmark control on a tour
  - Expected: The tour is added to the user's bookmarks/saved list

- [X] FT-09: User can mark a tour as "in progress"
  - Action: Enter a tour and click its "in progress" control
  - Expected: The tour is flagged as in progress and appears in the in-progress list

- [X] FT-10: User can resume a tour where they left off
  - Action: Leave an in-progress tour, then reopen it from the in-progress list
  - Expected: The tour opens at the last room/area (and state) the user was on

- [X] FT-11: Search returns matching tours
  - Action: Enter a keyword matching a known tour (e.g., its title or theme) in the search field
  - Expected: Only tours matching the keyword are listed

- [X] FT-12: Filtering by theme, period, culture, and difficulty works
  - Action: Apply one filter per category (theme, historical period, culture, difficulty) individually
  - Expected: The catalog updates to show only tours matching the selected filter value

- [ ] FT-13: Related tour suggestions appear at the end of a tour
  - Action: Reach the end of a tour
  - Expected: A set of suggested related tours is displayed and each is clickable to open that tour
  - Bug Report:
    - Issue: Related-tour suggestion opens a crashed (blank) tour page
    - Actual: The "Continue Your Journey" section lists 2 suggestions, but clicking "Realm of the Greek Gods" navigates to `/tour/greek-mythology` and the page renders completely blank. Console error: `TypeError: Cannot read properties of undefined (reading 'name')` at `TourPage.tsx:590`. Root cause reproduced deterministically: after being on Room 3 of 3 of a 3-room tour, opening the 1-room Greek tour (the persisted room index exceeds the tour's room count) crashes the tour page.

## Constraint

- [X] CS-01: Search with no matches shows an empty state, not a broken catalog
  - Action: Search for a keyword with no matching tours (e.g., "zzzz")
  - Expected: A "No results" message is shown and the rest of the site remains functional

- [X] CS-02: Combined filters narrow results to the intersection and handle no-match combinations
  - Action: Select multiple filters whose combined criteria match no tours
  - Expected: Results show only tours matching all selected filters; if none match, an empty-result state is shown instead of an error

- [X] CS-03: Bookmark and in-progress states persist across reloads
  - Action: Bookmark a tour, mark another in progress, then reload the page
  - Expected: Both states are retained, and a non-bookmarked tour does not appear in the bookmarks list

## Interaction

- [X] IX-01: Catalog cards and exhibits give visual feedback on hover
  - Action: Hover over a tour card and over an exhibit
  - Expected: A visible highlight/cursor change indicates both are interactive

- [X] IX-02: Entering a room shows a clear transition and current-location indicator
  - Action: Move from one room/area to another
  - Expected: The view updates to the new room and a location indicator reflects the current room/area

## Content

- [X] CT-01: All displayed media is relevant to the tour's subject
  - Action: Review thumbnails and exhibit visuals in the catalog and inside a tour
  - Expected: Every image/thumbnail depicts the specific museum, gallery, site, landmark, or imagined place it represents

- [X] CT-02: Educational text matches its exhibit and category labels are consistent
  - Action: Open an exhibit's layers and compare against its category tags (theme, period, culture, difficulty)
  - Expected: Overview, deeper-dive, and related-items text describe that exhibit, and the tag values match the categories shown in search/filters

---

## Summary

- **Passed:** FT-02, FT-03, FT-04, FT-05, FT-06, FT-08, FT-09, FT-10, FT-11, FT-12, CS-01, CS-02, CS-03, IX-01, IX-02, CT-01, CT-02 (17/20)
- **Failed:** FT-01, FT-07, FT-13 (3/20)

**Notable observations:**
- **FT-01** — Cards lack historical-period and culture tags (only theme + difficulty shown).
- **FT-07** — Timeline is display-only; no selectable/movable points.
- **FT-13** — A related suggestion ("Realm of the Greek Gods") opens a blank, crashed tour page. Root cause: the app persists the current room index globally rather than per-tour, so opening any tour with fewer rooms than the stored index index-errors (`rooms[i].name` undefined). This is a broader defect that can affect other tours too (e.g., opening a 1–2 room tour after having advanced deep into a longer tour).
- FT-09 is achieved implicitly: entering a tour auto-flags it "In Progress" (there is no separate explicit "in progress" control to click).