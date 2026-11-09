# Test Checklist

## Functionality
- [ ] FT-01: Tour catalog displays default tours of real and imagined venues
  - Action: Open the home/catalog page and scroll through the tour listings.
  - Expected: Multiple tour cards are shown, each with a title, thumbnail, and venue type (museum, gallery, historical site, or landmark); the catalog includes both real places and fully imagined places.

- [ ] FT-02: User can enter a tour from the catalog
  - Action: Click the primary button (e.g., "Start Tour" / "Explore") on a default tour card.
  - Expected: The tour viewer opens on the tour's first room/area with a name and visible exhibits.

- [ ] FT-03: User can move between rooms/areas within a tour
  - Action: Use the room navigation (e.g., "Next"/"Previous" or a room map) to visit at least 2 different rooms in one tour.
  - Expected: Each navigation switch displays that room's content and exhibits; no error or blank view.

- [ ] FT-04: Clicking an exhibit opens layered educational content
  - Action: Click on an exhibit hotspot/item in a room, then follow the in-panel links to the deeper level and a related item.
  - Expected: Panel shows an Overview section, a "Deeper dive" (expand/next level) section reachable from it, and a "Related items" list that opens linked content.

- [ ] FT-05: In-tour quiz is interactive
  - Action: Open a quiz element in a tour that has one, select an answer for each question, and click "Submit".
  - Expected: The quiz records the selections and displays feedback (correct/incorrect and/or score).

- [ ] FT-06: In-tour timeline is interactive
  - Action: Open the timeline element and click/advance through at least 2 events/entries.
  - Expected: Selecting each event displays its associated date and description content.

- [ ] FT-07: Search discovers tours by keyword
  - Action: Type a term matching a default tour's title or subject (e.g., "Egypt") into the search field and submit.
  - Expected: The catalog updates to show only tours matching the term.

- [ ] FT-08: Filters narrow tours by theme, period, culture, and difficulty
  - Action: Apply each filter type in turn (theme, historical period, culture, difficulty level) using values present in the default data.
  - Expected: Results show only tours whose metadata matches the selected filter value(s).

- [ ] FT-09: User can bookmark a tour as "in progress"
  - Action: Click the bookmark / "Mark in progress" control on a tour, then locate the "In Progress"/"My Tours" section.
  - Expected: The tour appears in the in-progress list with its saved status reflected in the catalog.

- [ ] FT-10: Resume returns the user to where they left off
  - Action: Navigate to room 2+ of a tour, leave the tour, then reopen it from the in-progress list (or via a "Resume" button).
  - Expected: The tour opens directly on the last room visited, not the first room.

- [ ] FT-11: Related tour suggestions appear at the end of a tour
  - Action: Navigate to the final room/end point of a tour and click a suggested tour card.
  - Expected: A "Related tours"/"You might also like" section is shown, and clicking a suggestion opens that tour.

## Constraint
- [ ] CS-01: Search/filter with no matches shows an empty state
  - Action: Enter a nonsense search term (e.g., "zzzqqxx") or apply a filter combination with no matching tours.
  - Expected: A clear "no tours found" message is shown; no stale tour cards remain and no error occurs.

- [ ] CS-02: Quiz answer cannot be submitted without selecting an option
  - Action: Open a quiz, leave at least one question unanswered, and click "Submit".
  - Expected: Submission is blocked or the unanswered question is flagged; no score is recorded for empty answers.

- [ ] CS-03: Bookmark state toggles without duplicates
  - Action: Click "Mark in progress" on a tour twice, or remove it from the in-progress list.
  - Expected: The tour is listed only once; once removed, it no longer appears in the in-progress list.

## Interaction
- [ ] IX-01: Active room is visually indicated
  - Action: Move between rooms using the tour's navigation.
  - Expected: The current room is highlighted/selected in the navigation UI, distinguishing it from other rooms.

- [ ] IX-02: Exhibit content panel closes and returns to the room
  - Action: Open an exhibit's layered content, then close it via its close button (or backdrop click / Escape).
  - Expected: The panel/modal dismisses and the room view is restored without reloading the tour to the first room.

- [ ] IX-03: Bookmark action gives immediate feedback
  - Action: Click the bookmark / "in progress" control on a tour.
  - Expected: The control's state visibly changes (e.g., filled icon, label change, or confirmation toast) at the moment of the action.

## Content
- [ ] CT-01: Tours display required classification metadata
  - Action: Inspect 3+ tour cards/detail views in the catalog.
  - Expected: Each tour shows its theme, historical period, culture, and difficulty level, and these values are consistent with the filter options.

- [ ] CT-02: Exhibit media and text are relevant and intact
  - Action: Open exhibits across 2+ tours and inspect images, icons, and text.
  - Expected: All images load without broken placeholders, and text/media are directly relevant to the tour's venue and subject (including imagined venues, whose content matches the imagined setting).

- [ ] CT-03: Related tour suggestions are topically connected
  - Action: Complete a tour and read the end-of-tour suggestions.
  - Expected: Each suggested tour shares at least one attribute (theme, period, culture, or venue type) with the tour just finished; links resolve to real catalog tours.