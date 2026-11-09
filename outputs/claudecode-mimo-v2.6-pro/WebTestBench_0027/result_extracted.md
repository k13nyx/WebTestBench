# Test Result

## Functionality
- [X] FT-01: Tour catalog displays a browsable list of available tours.
  - Action: Open the tour catalog page.
  - Expected: A list/grid of tour cards is displayed, each showing at least a tour title and a cover image or thumbnail.

- [X] FT-02: User can start a tour from the catalog.
  - Action: Click the first tour card in the catalog.
  - Expected: The tour view opens, displaying the first room/area of the selected tour.

- [X] FT-03: User can move through different rooms/areas of a tour.
  - Action: Click the "Next" control (or a room/area selector) in the tour view.
  - Expected: The view changes to a different room/area of the same tour, and the room/area name updates accordingly.

- [X] FT-04: Clicking an exhibit opens layered educational content.
  - Action: Click an exhibit in the current room.
  - Expected: A content panel/overlay opens showing an overview, a "deeper dive" section, and a list of related items, all reachable within the panel.

- [X] FT-05: User can complete a quiz inside a tour.
  - Action: Open the quiz element in a tour, select an answer for a question, and click "Submit".
  - Expected: The quiz accepts the answer and displays a result indicating whether the answer was correct (e.g., correct/incorrect feedback or a score).

- [ ] FT-06: User can interact with a timeline inside a tour.
  - Action: Open the timeline element in a tour and click an event/point on the timeline.
  - Expected: Information for the selected timeline event (title and description) is displayed.
  - Bug Report:
    - Issue: Non-interactive Timeline Events / Missing Event Description
    - Actual: In the "Golden Death Mask of Tutankhamun" exhibit's Timeline tab, clicking an event (e.g., "Birth of Tutankhamun") triggers no response — no selection state appears and no event detail is displayed. DOM inspection shows the timeline entries are static divs (no click handler, cursor: auto) containing only a date and a title ("1341 BCE / Birth of Tutankhamun") with no description text anywhere; the expected title + description information is never shown.

- [X] FT-07: User can bookmark a tour.
  - Action: Click the "Bookmark" (or save) button on a tour (catalog card or tour page).
  - Expected: The tour appears in the user's bookmarked/saved tours list.

- [X] FT-08: User can mark a tour as "in progress".
  - Action: Mark a tour as "in progress" (via the tour's status control or by starting it).
  - Expected: The tour appears in the "In Progress" list with an "in progress" status label.

- [X] FT-09: User can resume a tour where they left off.
  - Action: Leave a tour after visiting at least two rooms, then open it again from the "In Progress" list and click "Resume".
  - Expected: The tour opens at the last visited room/area, not at the first room.

- [X] FT-10: User can search for tours by keyword.
  - Action: Enter a keyword matching a tour title/subject into the search bar on the catalog page.
  - Expected: The catalog updates to show only tours matching the keyword.

- [X] FT-11: User can filter tours by theme, historical period, culture, and difficulty level.
  - Action: On the catalog page, select values in each of the "Theme", "Historical Period", "Culture", and "Difficulty" filters.
  - Expected: The catalog updates to show only tours matching the selected filter values; each of the four filter controls exists and is functional.

- [X] FT-12: Related tours are suggested at the end of a tour.
  - Action: Navigate to the end/finish screen of a tour.
  - Expected: A list of suggested related tours is displayed and each suggestion links to its tour.

## Constraint
- [X] CS-01: Combined filters must apply strict AND matching.
  - Action: Select two different filter values at once (e.g., Theme = "Art" and Difficulty = "Beginner") on the catalog page.
  - Expected: Every displayed tour matches both selected values; no tour matching only one of them is shown.

- [X] CS-02: "Resume" must not be offered for tours that have never been started.
  - Action: Locate a tour that is not in the "In Progress" list and inspect its available actions.
  - Expected: No "Resume" control is shown (or it is disabled); only "Start"/"Begin" is available.

- [X] CS-03: Room/area navigation must be bounded by the tour's room list.
  - Action: In a tour, click "Previous" on the first room and "Next" on the last room.
  - Expected: The "Previous" control is disabled on the first room, the "Next" control is disabled on the last room, and the view never leaves the tour's defined rooms.

## Interaction
- [X] IX-01: Exhibit elements give visual click feedback and the content panel opens/closes smoothly.
  - Action: Hover over an exhibit, click it, then close the content panel (via its close button).
  - Expected: The exhibit shows a hover/active highlight, the content panel opens on click, and closes on the close action, returning to the room view.

- [X] IX-02: Tour progress indicator updates as the user moves through rooms.
  - Action: Move from one room/area to the next and observe the progress indicator (e.g., "Room 2 of 5" or a progress bar).
  - Expected: The progress indicator updates immediately to reflect the current room/area position in the tour.

## Content
- [X] CT-01: Catalog content covers diverse venue types including both real and fully imagined places.
  - Action: Browse the tour catalog and read the tour titles/descriptions.
  - Expected: Tours include museums, art galleries, historical sites, and cultural landmarks, and include at least one real place and at least one fully imagined place, as identified in the tour descriptions.

- [X] CT-02: Exhibit educational content is relevant to the exhibit it belongs to.
  - Action: Open the layered content (overview and deeper dive) for two different exhibits.
  - Expected: All text in each panel directly discusses that exhibit's subject/artwork/place; no content about an unrelated topic appears.

- [ ] CT-03: Related tour suggestions are thematically relevant to the completed tour.
  - Action: Finish a tour and review the suggested related tours.
  - Expected: Each suggested tour shares at least one attribute with the completed tour (same theme, period, culture, or venue type); no unrelated tours are suggested.
  - Bug Report:
    - Issue: Unrelated Tour Suggested (Related-Tour Matching Violation)
    - Actual: After completing "Mysteries of Ancient Egypt" (theme "Ancient Civilizations", period "Ancient (3000 BCE - 30 BCE)", culture "Egyptian", real historical sites), the "Continue Your Journey" suggestions include "Realm of the Greek Gods" (theme "Mythology", period "Ancient (800 BCE - 31 BCE)" — verified distinct via the Period filter, culture "Greek", fully imagined Mount Olympus). It shares no theme, period, culture, or venue type with the completed tour — only the "Beginner" difficulty, which is not an accepted relevance attribute. ("Glory of Rome" is relevant via shared theme.)
