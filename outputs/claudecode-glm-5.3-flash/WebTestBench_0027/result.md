All tests executed. Compiling the final report:

# Test Result

## Functionality
- [X] FT-01: Catalog displays multiple tours covering both real and imagined places
  - Action: Open the website's tour catalog/home page
  - Expected: Multiple tour cards are displayed, and the catalog includes at least one real place (e.g., a museum, historical site) and at least one fully imagined/fictional place, each with a title and thumbnail
  - Notes: 6 tour cards with thumbnails are displayed. Real places: Mysteries of Ancient Egypt, Glory of Rome, Renaissance Masters, etc. Fully imagined place: "Realm of the Greek Gods – Legends of Mount Olympus" (Throne Room of Olympus, Throne of Zeus — a purely mythological realm)
- [X] FT-02: User can open a tour from the catalog and enter its first room/area
  - Action: Click on a tour card in the catalog (e.g., any tour title or "Start Tour" button)
  - Expected: The tour opens, showing the first room/area of that tour with its name shown
  - Notes: Clicking "Mysteries of Ancient Egypt" opened the tour showing "The Great Hall of Pharaohs" as Room 1 of 3
- [X] FT-03: User can move through different rooms/areas within a tour
  - Action: Start a tour, then navigate to the next room (e.g., click "Next Room", a room link, or a map area)
  - Expected: A different room/area loads, and the user can move both forward and back between rooms of the tour
  - Notes: "Next Room" loaded "The Tomb Chamber" (Room 2 of 3); "Previous Room" returned to "The Great Hall of Pharaohs" (Room 1 of 3); room tabs also work ("Treasury of the Pharaohs", Room 3 of 3)
- [X] FT-04: Clicking an exhibit opens layered educational content
  - Action: In any room, click on a visible exhibit (e.g., an artifact, artwork, or hotspot)
  - Expected: A panel/modal opens showing an overview of that exhibit
  - Notes: Clicking "Colossal Statue of Ramesses II" opened a panel with its overview text and tabs (Overview / Deep Dive / Timeline / Quiz)
- [X] FT-05: Exhibit content has multiple layers (overview, deeper dive, related items)
  - Action: Open an exhibit panel, then click to go deeper (e.g., "Learn More", a tab, or an expandable section)
  - Expected: At least two additional content layers are reachable: a deeper dive section and a related items/links section, each with actual content
  - Notes: "Deep Dive" tab showed a detailed biography of Ramesses II (Nineteenth Dynasty, Hittite peace treaty), and a "Related Items" section listing "Nefertari Bust" and "Abu Simbel Model"
- [X] FT-06: Tour includes an interactive quiz that responds to answers
  - Action: Find a quiz within a tour, select an answer, and submit it
  - Expected: The quiz accepts the answer and shows feedback (e.g., correct/incorrect indication or score)
  - Notes: Quiz tab "How long did Ramesses II reign as pharaoh?" — selected "66 years", clicked "Submit Answer", got "🎉 Correct! Well done!" and options were locked
- [X] FT-07: Tour includes an interactive timeline
  - Action: Find a timeline element within a tour and interact with it (click an event or drag/scrub along it)
  - Expected: Timeline event details are shown for the selected point (e.g., a date and its description)
  - Notes: Timeline tab shows 4 events, each with a date and description: 1303 BCE Birth of Ramesses II, 1279 BCE Becomes Pharaoh, 1274 BCE Battle of Kadesh, 1213 BCE Death of Ramesses II (all details visible; events are static cards without a selection state)
- [X] FT-08: User can bookmark a tour
  - Action: Open a tour and click its bookmark button (e.g., a bookmark icon or "Bookmark" button)
  - Expected: The tour is marked as bookmarked (visual state changes and/or it appears in a bookmarks/saved list)
  - Notes: "Save Tour" button toggled to "Saved"; tour appears under "Saved Tours (1)" in My Collection
- [X] FT-09: Starting a tour marks it as "In Progress"
  - Action: Enter a tour and visit at least one room, then return to the catalog
  - Expected: The tour shows an "In Progress" indicator and/or appears in an "In Progress"/"Continue" section
  - Notes: Catalog shows a "Continue Exploring" section and the card carries an "In Progress" badge (also shown in My Collection: In Progress = 3)
- [X] FT-10: User can resume a tour where they left off
  - Action: Note the room reached in FT-09, leave the tour, then click "Resume"/"Continue" on that tour
  - Expected: The tour reopens at (or offers to continue from) the room/area last visited, not necessarily the first room
  - Notes: After visiting "Treasury of the Pharaohs" (Room 3 of 3) and leaving, clicking the Continue Exploring card reopened the tour directly at Room 3 of 3
- [X] FT-11: Search returns matching tours
  - Action: Type a term matching an existing tour's name or theme (e.g., "Egypt" or "Renaissance") into the search box and submit
  - Expected: Only tours relevant to the term are shown, including the matching tour
  - Notes: Searching "Egypt" narrowed the catalog to "1 Tour Available" — Mysteries of Ancient Egypt only
- [X] FT-12: Filters narrow the catalog by theme, historical period, culture, and difficulty
  - Action: Open the filters, apply one filter per dimension (theme, historical period, culture, difficulty) one at a time
  - Expected: Each applied filter updates the catalog to show only tours matching that dimension, and all four filter dimensions are available
  - Notes: Filters panel exposes Theme, Period, Culture, Difficulty. Theme=Mythology → 1 tour (Realm of the Greek Gods); Period=Renaissance (1400-1600) → 1 tour (Renaissance Masters); Culture=Egyptian → 1 tour (Ancient Egypt); Difficulty=Advanced → 1 tour (Modern Architecture Marvels)
- [ ] FT-14: Related tour suggestion is clickable and leads to that tour
  - Action: From a finished tour's related suggestions, click one suggested tour
  - Expected: The suggested tour's page/view opens (catalog entry or tour start)
  - Bug Report:
    - Issue: Application crash (blank screen) on related-tour navigation
    - Actual: Clicking the "Realm of the Greek Gods" suggestion in the "Continue Your Journey" section while on a later room of "Mysteries of Ancient Egypt" (Room 3 of 3) throws `TypeError: Cannot read properties of undefined` in `<TourPage>` and renders a completely blank page (empty DOM) at /tour/greek-mythology. Reproduced twice. Control test: the same suggestion links work when navigating from a tour whose last-visited room index is within the target tour's room count (greek-mythology → roman-empire loaded fine), and direct URL loads of /tour/greek-mythology also work — the crash is specific to navigating via the suggestion when the source tour's saved room index (2) exceeds the target tour's room count (1)

## Constraint
- [X] CS-01: Search with no matching results shows a clear empty state
  - Action: Search for a gibberish term (e.g., "zzzqqq")
  - Expected: A "no results" style message is shown instead of an error or unrelated tours
  - Notes: Shows "0 Tours Available", "No tours found — Try adjusting your search or filters" with a "Clear all filters" button
- [X] CS-02: Combining multiple filters yields only tours matching all of them
  - Action: Apply two filters simultaneously that no single tour satisfies together (e.g., a theme + a difficulty with no overlap in default data)
  - Expected: Zero tours are shown with an empty-state message; no tour violating either filter appears
  - Notes: Theme=Architecture + Difficulty=Beginner → "0 Tours Available" with "No tours found" empty state; no violating tour rendered
- [X] CS-03: Quiz must not be submittable with no answer selected
  - Action: Open a quiz question and attempt to submit without selecting any option
  - Expected: Submission is prevented (button disabled or validation message shown); no result is displayed
  - Notes: No "Submit Answer" button exists in the DOM until an option is selected; it appears only after clicking an answer

## Interaction
- [X] IX-01: Bookmarked/in-progress state persists after page reload
  - Action: Bookmark a tour or start one, reload the page, and check the catalog/bookmarks
  - Expected: The bookmark and/or "In Progress" status is still shown after reload
  - Notes: After a full page reload, "Continue Exploring" shows all 3 in-progress tours with "In Progress" badges, and My Collection still lists Saved Tours (1) and In Progress (3)
- [X] IX-02: Exhibit panel can be closed and the room returns to its prior state
  - Action: Open an exhibit panel, then close it (e.g., "X" or "Close" button)
  - Expected: The panel closes and the room view is fully visible again with no leftover overlay
  - Notes: Closing via the X removed the panel entirely from the DOM; the room view (Room 1 of 3, exhibits grid) was fully visible with no overlay remnants

## Content
- [X] CT-01: Exhibit content is accurate and relevant to the tour's theme
  - Action: Open 2–3 exhibits in a real-place tour (e.g., a museum or historical site tour) and read titles/descriptions
  - Expected: Each exhibit's title and description are factually plausible and clearly related to that tour's stated theme/period
  - Notes: Reviewed 4 exhibits in the Ancient Egypt tour: Colossal Statue of Ramesses II (10m granite, 66-year reign — accurate), Bust of Queen Nefertari (limestone, Great Royal Wife of Ramesses II — accurate), The Book of the Dead (papyrus with afterlife spells — accurate), Canopic Jars (four alabaster jars for organs — accurate); the Tutankhamun golden mask description (~11 kg solid gold) is also factually plausible
- [X] CT-02: Each tour card shows its difficulty and metadata
  - Action: Inspect tour cards in the catalog
  - Expected: Each card displays its difficulty level (e.g., Beginner/Intermediate/Advanced) and theme/period/culture tags matching the tour's actual content
  - Notes: All 6 cards show a theme tag (Ancient Civilizations / Art History / Mythology / Architecture) and difficulty (Beginner / Intermediate / Advanced) matching their content, plus duration and room count