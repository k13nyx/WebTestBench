# Test Checklist

## Functionality
- [ ] FT-01: Catalog displays all available tours in a browsable list/grid
  - Action: Open the site and land on/return to the tour catalog
  - Expected: Tour cards appear, each showing a title and its theme, historical period, culture, and difficulty level

- [ ] FT-02: User can open a tour from the catalog
  - Action: Click a tour card in the catalog
  - Expected: The selected tour opens and its first room/area is displayed

- [ ] FT-03: User can move between rooms/areas within a tour
  - Action: Inside a tour, navigate to a next/adjacent room using the provided navigation control
  - Expected: The new room/area loads with its own exhibits visible

- [ ] FT-04: Clicking an exhibit opens its overview content layer
  - Action: Click any visible exhibit inside a room
  - Expected: An overview panel (text/media) for that exhibit opens

- [ ] FT-05: Exhibit content provides deeper-dive and related-items layers
  - Action: From an open exhibit overview, select the deeper-dive option, then the related-items option
  - Expected: A deeper-dive content layer opens, and a related-items layer lists other linked exhibits

- [ ] FT-06: A quiz interaction works inside the tour
  - Action: Locate the quiz within the tour and answer its question(s)
  - Expected: The selected answer is evaluated and correct/incorrect feedback is shown

- [ ] FT-07: A timeline interaction works inside the tour
  - Action: Locate the timeline and interact with it (select/move to a timeline entry)
  - Expected: The timeline responds and displays the content tied to the selected point

- [ ] FT-08: User can bookmark a tour
  - Action: Click the bookmark control on a tour
  - Expected: The tour is added to the user's bookmarks/saved list

- [ ] FT-09: User can mark a tour as "in progress"
  - Action: Enter a tour and click its "in progress" control
  - Expected: The tour is flagged as in progress and appears in the in-progress list

- [ ] FT-10: User can resume a tour where they left off
  - Action: Leave an in-progress tour, then reopen it from the in-progress list
  - Expected: The tour opens at the last room/area (and state) the user was on

- [ ] FT-11: Search returns matching tours
  - Action: Enter a keyword matching a known tour (e.g., its title or theme) in the search field
  - Expected: Only tours matching the keyword are listed

- [ ] FT-12: Filtering by theme, period, culture, and difficulty works
  - Action: Apply one filter per category (theme, historical period, culture, difficulty) individually
  - Expected: The catalog updates to show only tours matching the selected filter value

- [ ] FT-13: Related tour suggestions appear at the end of a tour
  - Action: Reach the end of a tour
  - Expected: A set of suggested related tours is displayed and each is clickable to open that tour

## Constraint
- [ ] CS-01: Search with no matches shows an empty state, not a broken catalog
  - Action: Search for a keyword with no matching tours (e.g., "zzzz")
  - Expected: A "No results" message is shown and the rest of the site remains functional

- [ ] CS-02: Combined filters narrow results to the intersection and handle no-match combinations
  - Action: Select multiple filters whose combined criteria match no tours
  - Expected: Results show only tours matching all selected filters; if none match, an empty-result state is shown instead of an error

- [ ] CS-03: Bookmark and in-progress states persist across reloads
  - Action: Bookmark a tour, mark another in progress, then reload the page
  - Expected: Both states are retained, and a non-bookmarked tour does not appear in the bookmarks list

## Interaction
- [ ] IX-01: Catalog cards and exhibits give visual feedback on hover
  - Action: Hover over a tour card and over an exhibit
  - Expected: A visible highlight/cursor change indicates both are interactive

- [ ] IX-02: Entering a room shows a clear transition and current-location indicator
  - Action: Move from one room/area to another
  - Expected: The view updates to the new room and a location indicator reflects the current room/area

## Content
- [ ] CT-01: All displayed media is relevant to the tour's subject
  - Action: Review thumbnails and exhibit visuals in the catalog and inside a tour
  - Expected: Every image/thumbnail depicts the specific museum, gallery, site, landmark, or imagined place it represents

- [ ] CT-02: Educational text matches its exhibit and category labels are consistent
  - Action: Open an exhibit's layers and compare against its category tags (theme, period, culture, difficulty)
  - Expected: Overview, deeper-dive, and related-items text describe that exhibit, and the tag values match the categories shown in search/filters