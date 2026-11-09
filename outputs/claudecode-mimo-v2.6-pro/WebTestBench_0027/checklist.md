# Test Checklist

## Functionality
- [ ] FT-01: Tour catalog displays a browsable list of available tours.
  - Action: Open the tour catalog page.
  - Expected: A list/grid of tour cards is displayed, each showing at least a tour title and a cover image or thumbnail.

- [ ] FT-02: User can start a tour from the catalog.
  - Action: Click the first tour card in the catalog.
  - Expected: The tour view opens, displaying the first room/area of the selected tour.

- [ ] FT-03: User can move through different rooms/areas of a tour.
  - Action: Click the "Next" control (or a room/area selector) in the tour view.
  - Expected: The view changes to a different room/area of the same tour, and the room/area name updates accordingly.

- [ ] FT-04: Clicking an exhibit opens layered educational content.
  - Action: Click an exhibit in the current room.
  - Expected: A content panel/overlay opens showing an overview, a "deeper dive" section, and a list of related items, all reachable within the panel.

- [ ] FT-05: User can complete a quiz inside a tour.
  - Action: Open the quiz element in a tour, select an answer for a question, and click "Submit".
  - Expected: The quiz accepts the answer and displays a result indicating whether the answer was correct (e.g., correct/incorrect feedback or a score).

- [ ] FT-06: User can interact with a timeline inside a tour.
  - Action: Open the timeline element in a tour and click an event/point on the timeline.
  - Expected: Information for the selected timeline event (title and description) is displayed.

- [ ] FT-07: User can bookmark a tour.
  - Action: Click the "Bookmark" (or save) button on a tour (catalog card or tour page).
  - Expected: The tour appears in the user's bookmarked/saved tours list.

- [ ] FT-08: User can mark a tour as "in progress".
  - Action: Mark a tour as "in progress" (via the tour's status control or by starting it).
  - Expected: The tour appears in the "In Progress" list with an "in progress" status label.

- [ ] FT-09: User can resume a tour where they left off.
  - Action: Leave a tour after visiting at least two rooms, then open it again from the "In Progress" list and click "Resume".
  - Expected: The tour opens at the last visited room/area, not at the first room.

- [ ] FT-10: User can search for tours by keyword.
  - Action: Enter a keyword matching a tour title/subject into the search bar on the catalog page.
  - Expected: The catalog updates to show only tours matching the keyword.

- [ ] FT-11: User can filter tours by theme, historical period, culture, and difficulty level.
  - Action: On the catalog page, select values in each of the "Theme", "Historical Period", "Culture", and "Difficulty" filters.
  - Expected: The catalog updates to show only tours matching the selected filter values; each of the four filter controls exists and is functional.

- [ ] FT-12: Related tours are suggested at the end of a tour.
  - Action: Navigate to the end/finish screen of a tour.
  - Expected: A list of suggested related tours is displayed and each suggestion links to its tour.

## Constraint
- [ ] CS-01: Combined filters must apply strict AND matching.
  - Action: Select two different filter values at once (e.g., Theme = "Art" and Difficulty = "Beginner") on the catalog page.
  - Expected: Every displayed tour matches both selected values; no tour matching only one of them is shown.

- [ ] CS-02: "Resume" must not be offered for tours that have never been started.
  - Action: Locate a tour that is not in the "In Progress" list and inspect its available actions.
  - Expected: No "Resume" control is shown (or it is disabled); only "Start"/"Begin" is available.

- [ ] CS-03: Room/area navigation must be bounded by the tour's room list.
  - Action: In a tour, click "Previous" on the first room and "Next" on the last room.
  - Expected: The "Previous" control is disabled on the first room, the "Next" control is disabled on the last room, and the view never leaves the tour's defined rooms.

## Interaction
- [ ] IX-01: Exhibit elements give visual click feedback and the content panel opens/closes smoothly.
  - Action: Hover over an exhibit, click it, then close the content panel (via its close button).
  - Expected: The exhibit shows a hover/active highlight, the content panel opens on click, and closes on the close action, returning to the room view.

- [ ] IX-02: Tour progress indicator updates as the user moves through rooms.
  - Action: Move from one room/area to the next and observe the progress indicator (e.g., "Room 2 of 5" or a progress bar).
  - Expected: The progress indicator updates immediately to reflect the current room/area position in the tour.

## Content
- [ ] CT-01: Catalog content covers diverse venue types including both real and fully imagined places.
  - Action: Browse the tour catalog and read the tour titles/descriptions.
  - Expected: Tours include museums, art galleries, historical sites, and cultural landmarks, and include at least one real place and at least one fully imagined place, as identified in the tour descriptions.

- [ ] CT-02: Exhibit educational content is relevant to the exhibit it belongs to.
  - Action: Open the layered content (overview and deeper dive) for two different exhibits.
  - Expected: All text in each panel directly discusses that exhibit's subject/artwork/place; no content about an unrelated topic appears.

- [ ] CT-03: Related tour suggestions are thematically relevant to the completed tour.
  - Action: Finish a tour and review the suggested related tours.
  - Expected: Each suggested tour shares at least one attribute with the completed tour (same theme, period, culture, or venue type); no unrelated tours are suggested.