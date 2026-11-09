# Test Checklist

## Functionality
- [ ] FT-01: Catalog displays multiple tours covering both real and imagined places
  - Action: Open the website's tour catalog/home page
  - Expected: Multiple tour cards are displayed, and the catalog includes at least one real place (e.g., a museum, historical site) and at least one fully imagined/fictional place, each with a title and thumbnail
- [ ] FT-02: User can open a tour from the catalog and enter its first room/area
  - Action: Click on a tour card in the catalog (e.g., any tour title or "Start Tour" button)
  - Expected: The tour opens, showing the first room/area of that tour with its name shown
- [ ] FT-03: User can move through different rooms/areas within a tour
  - Action: Start a tour, then navigate to the next room (e.g., click "Next Room", a room link, or a map area)
  - Expected: A different room/area loads, and the user can move both forward and back between rooms of the tour
- [ ] FT-04: Clicking an exhibit opens layered educational content
  - Action: In any room, click on a visible exhibit (e.g., an artifact, artwork, or hotspot)
  - Expected: A panel/modal opens showing an overview of that exhibit
- [ ] FT-05: Exhibit content has multiple layers (overview, deeper dive, related items)
  - Action: Open an exhibit panel, then click to go deeper (e.g., "Learn More", a tab, or an expandable section)
  - Expected: At least two additional content layers are reachable: a deeper dive section and a related items/links section, each with actual content
- [ ] FT-06: Tour includes an interactive quiz that responds to answers
  - Action: Find a quiz within a tour, select an answer, and submit it
  - Expected: The quiz accepts the answer and shows feedback (e.g., correct/incorrect indication or score)
- [ ] FT-07: Tour includes an interactive timeline
  - Action: Find a timeline element within a tour and interact with it (click an event or drag/scrub along it)
  - Expected: Timeline event details are shown for the selected point (e.g., a date and its description)
- [ ] FT-08: User can bookmark a tour
  - Action: Open a tour and click its bookmark button (e.g., a bookmark icon or "Bookmark" button)
  - Expected: The tour is marked as bookmarked (visual state changes and/or it appears in a bookmarks/saved list)
- [ ] FT-09: Starting a tour marks it as "In Progress"
  - Action: Enter a tour and visit at least one room, then return to the catalog
  - Expected: The tour shows an "In Progress" indicator and/or appears in an "In Progress"/"Continue" section
- [ ] FT-10: User can resume a tour where they left off
  - Action: Note the room reached in FT-09, leave the tour, then click "Resume"/"Continue" on that tour
  - Expected: The tour reopens at (or offers to continue from) the room/area last visited, not necessarily the first room
- [ ] FT-11: Search returns matching tours
  - Action: Type a term matching an existing tour's name or theme (e.g., "Egypt" or "Renaissance") into the search box and submit
  - Expected: Only tours relevant to the term are shown, including the matching tour
- [ ] FT-12: Filters narrow the catalog by theme, historical period, culture, and difficulty
  - Action: Open the filters, apply one filter per dimension (theme, historical period, culture, difficulty) one at a time
  - Expected: Each applied filter updates the catalog to show only tours matching that dimension, and all four filter dimensions are available
- [ ] FT-13: Related tour suggestions appear at the end of a tour
  - Action: Navigate to the last room/complete a tour
  - Expected: A "Related Tours"/"You may also like" section shows suggestions linking to other tours
- [ ] FT-14: Related tour suggestion is clickable and leads to that tour
  - Action: From a finished tour's related suggestions, click one suggested tour
  - Expected: The suggested tour's page/view opens (catalog entry or tour start)

## Constraint
- [ ] CS-01: Search with no matching results shows a clear empty state
  - Action: Search for a gibberish term (e.g., "zzzqqq")
  - Expected: A "no results" style message is shown instead of an error or unrelated tours
- [ ] CS-02: Combining multiple filters yields only tours matching all of them
  - Action: Apply two filters simultaneously that no single tour satisfies together (e.g., a theme + a difficulty with no overlap in default data)
  - Expected: Zero tours are shown with an empty-state message; no tour violating either filter appears
- [ ] CS-03: Quiz must not be submittable with no answer selected
  - Action: Open a quiz question and attempt to submit without selecting any option
  - Expected: Submission is prevented (button disabled or validation message shown); no result is displayed

## Interaction
- [ ] IX-01: Bookmarked/in-progress state persists after page reload
  - Action: Bookmark a tour or start one, reload the page, and check the catalog/bookmarks
  - Expected: The bookmark and/or "In Progress" status is still shown after reload
- [ ] IX-02: Exhibit panel can be closed and the room returns to its prior state
  - Action: Open an exhibit panel, then close it (e.g., "X" or "Close" button)
  - Expected: The panel closes and the room view is fully visible again with no leftover overlay

## Content
- [ ] CT-01: Exhibit content is accurate and relevant to the tour's theme
  - Action: Open 2–3 exhibits in a real-place tour (e.g., a museum or historical site tour) and read titles/descriptions
  - Expected: Each exhibit's title and description are factually plausible and clearly related to that tour's stated theme/period
- [ ] CT-02: Each tour card shows its difficulty and metadata
  - Action: Inspect tour cards in the catalog
  - Expected: Each card displays its difficulty level (e.g., Beginner/Intermediate/Advanced) and theme/period/culture tags matching the tour's actual content