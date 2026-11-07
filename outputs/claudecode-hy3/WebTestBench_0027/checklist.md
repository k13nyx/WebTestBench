# Test Checklist

## Functionality
- [ ] FT-01: User can browse and select a tour from the catalog
  - Action: Open the tour catalog and click on any tour card.
  - Expected: The selected tour's tour view (rooms/areas) opens.

- [ ] FT-02: User can move through different rooms or areas within a tour
  - Action: From within a tour, click the navigation control to go to the next room/area.
  - Expected: The view changes to show the next room/area of the tour.

- [ ] FT-03: User can click an exhibit to open its educational content
  - Action: Within a tour room, click on a clickable exhibit.
  - Expected: A content panel opens for that exhibit.

- [ ] FT-04: User can access layered content (overview, deeper dive, related items)
  - Action: Open an exhibit's content panel and click each layer tab/link (Overview, Deeper Dive, Related Items).
  - Expected: Each layer displays its corresponding content.

- [ ] FT-05: User can complete an interactive quiz within a tour
  - Action: Open the quiz element inside a tour and submit answers.
  - Expected: The quiz accepts input and shows a result/completion state.

- [ ] FT-06: User can interact with a timeline within a tour
  - Action: Open the timeline element and select/scrub a point on it.
  - Expected: The timeline responds and displays the corresponding information.

- [ ] FT-07: User can mark/bookmark a tour as "in progress"
  - Action: On a tour's page, click the "Mark as in progress" / bookmark control.
  - Expected: The tour is recorded as in progress (e.g., badge/bookmark state changes).

- [ ] FT-08: User can resume a previously started tour where they left off
  - Action: Open a tour already marked in progress and select "Resume".
  - Expected: The tour opens at the room/area the user last viewed.

- [ ] FT-09: User can search for tours
  - Action: Type a keyword into the search box and submit.
  - Expected: Catalog shows only tours matching the keyword.

- [ ] FT-10: User can filter tours by theme, historical period, culture, and difficulty
  - Action: Apply one or more filters (theme, historical period, culture, difficulty).
  - Expected: Catalog updates to show only tours matching the selected filters.

- [ ] FT-11: User can view related tour suggestions at the end of a tour
  - Action: Reach the end of a completed tour.
  - Expected: A list of related tour suggestions is displayed.

## Constraint
- [ ] CS-01: Resume is only available for tours marked "in progress"
  - Action: On a tour that has NOT been marked in progress, look for the "Resume" option.
  - Expected: Resume is disabled or not shown.

- [ ] CS-02: Filters only return tours matching all selected criteria
  - Action: Apply combined filters (e.g., culture = "Ancient Egypt" + theme = "Art").
  - Expected: Every shown tour matches all selected filter values.

- [ ] CS-03: Difficulty filter accepts only defined difficulty levels
  - Action: Open the difficulty filter control.
  - Expected: Only the defined options (e.g., Beginner, Intermediate, Advanced) are selectable.

## Interaction
- [ ] IX-01: Clicking an exhibit opens a visible content panel
  - Action: Click a clickable exhibit.
  - Expected: A content panel/overlay becomes visible on screen.

- [ ] IX-02: A confirmation indicator appears when a tour is marked "in progress"
  - Action: Click "Mark as in progress" on a tour.
  - Expected: A visible confirmation (toast/badge/label) confirms the action.

- [ ] IX-03: Navigating between rooms/areas visibly updates the scene
  - Action: Move from one room/area to another within a tour.
  - Expected: The displayed scene/view changes to reflect the new location.

## Content
- [ ] CT-01: Catalog cards display relevant tour metadata
  - Action: Inspect a tour card in the catalog.
  - Expected: It shows title, theme, historical period, culture, and difficulty.

- [ ] CT-02: Exhibit educational content is present and relevant to the tour theme
  - Action: Open an exhibit's layered content (overview, deeper dive, related items).
  - Expected: Content is present and directly relevant to that tour's subject/theme.

- [ ] CT-03: Related-tour suggestions are thematically/culturally related to the completed tour
  - Action: Review the related tour suggestions shown at the end of a tour.
  - Expected: Each suggested tour shares the completed tour's theme, period, or culture.