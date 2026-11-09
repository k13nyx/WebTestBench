# Test Result

## Functionality
- [X] FT-01: Filter catalog by multiple criteria
  - Action: Select specific options in the "Theme", "Historical Period", "Culture", and "Difficulty Level" filter dropdowns in the catalog.
  - Expected: The tour catalog updates to display only tours matching all selected filter attributes.

- [X] FT-02: Search tours by keyword
  - Action: Enter a search term into the catalog search bar and press Enter.
  - Expected: The catalog updates to show only tours whose titles, descriptions, or locations match the search keyword.

- [X] FT-03: Navigate between tour rooms or areas
  - Action: Open a tour and click the "Next Room" or area navigation arrow.
  - Expected: The tour viewport updates to display the next room or area in the sequence.

- [X] FT-04: Open layered exhibit content
  - Action: Click on an interactive exhibit hotspot within a room.
  - Expected: An educational overlay opens displaying the exhibit "Overview", "Deep Dive", and "Related Items" sections.

- [X] FT-05: Complete an interactive in-tour quiz
  - Action: Navigate to a room containing a quiz, select an answer option, and click "Submit Answer".
  - Expected: The system evaluates the response and displays immediate feedback indicating whether the answer was correct or incorrect.

- [ ] FT-06: Navigate an interactive in-tour timeline
  - Action: Click on a specific milestone date on an in-room timeline widget.
  - Expected: The timeline focuses on the chosen date and updates the adjacent informational text and image for that milestone.
  - Bug Report:
    - Issue: Non-interactive Timeline Widget
    - Actual: Milestone dates on the timeline tab are rendered as static, non-clickable elements without click handlers; clicking a date does not focus on it or update any adjacent informational text and image.

- [X] FT-07: Bookmark a tour
  - Action: Click the "Bookmark" icon on any tour card in the catalog.
  - Expected: The tour is added to the user's "Saved Tours" or bookmarked list.

- [X] FT-08: Resume an in-progress tour
  - Action: Navigate partway through a tour (e.g., Room 3), return to the main dashboard, and click "Resume Tour".
  - Expected: The tour opens directly to the exact room (Room 3) where the user previously stopped.

- [ ] FT-09: Launch a suggested tour from the completion screen
  - Action: Reach the final area of a tour, view the completion screen, and click on one of the "Recommended Tours" cards.
  - Expected: The current tour closes and the selected recommended tour launches immediately.
  - Bug Report:
    - Issue: Missing Recommended Tour Cards on Completion Screen
    - Actual: The completion screen modal only renders "Stay Here" and "Explore More" buttons; it does not display any "Recommended Tours" cards to launch directly from the completion screen.

## Constraint
- [X] CS-01: Empty search and filter results handling
  - Action: Apply filter combinations and search terms that match no available tours.
  - Expected: The catalog displays a "No tours found matching your criteria" message and does not render empty tour cards.

- [X] CS-02: Tour navigation boundary restriction
  - Action: Navigate to the first room of a tour and inspect the "Previous Room" navigation control.
  - Expected: The "Previous Room" button is disabled or hidden, preventing navigation before the starting room.

- [ ] CS-03: Quiz submission requires answer selection
  - Action: Attempt to click the "Submit Answer" button on an interactive quiz without choosing an option.
  - Expected: The submission is blocked, the button remains disabled, and a prompt asks the user to select an answer first.
  - Bug Report:
    - Issue: Missing Disabled Submission Button and Validation Prompt
    - Actual: The "Submit Answer" button is not rendered in the DOM when no answer option is chosen; there is no disabled button shown and no validation prompt displayed asking the user to select an answer first.

## Interaction
- [X] IX-01: Exhibit hotspot hover feedback
  - Action: Hover the mouse cursor over an interactive exhibit point within a tour area.
  - Expected: The cursor changes to a pointer and the hotspot displays a visual indicator (such as a pulse animation or tooltip label).

- [ ] IX-02: Switch tabs within layered exhibit content
  - Action: In an open exhibit modal, click sequentially between the "Overview", "Deep Dive", and "Related Items" tabs.
  - Expected: The view switches active states immediately and renders the respective tab's content without reloading the modal.
  - Bug Report:
    - Issue: Missing Dedicated "Related Items" Tab
    - Actual: The exhibit modal only provides "Overview", "Deep Dive", "Timeline", and "Quiz" tabs. "Related Items" is rendered as a static sub-section inside the Deep Dive tab rather than an independent clickable tab.

- [ ] IX-03: Tour progress status badge indicator
  - Action: Begin moving through rooms in a newly started tour and check its card in the catalog.
  - Expected: The tour card displays an "In Progress" badge with an updated progress percentage or room counter.
  - Bug Report:
    - Issue: Progress Badge Lacks Percentage or Room Counter
    - Actual: The tour card displays an "In Progress" badge with a play icon, but does not include an updated progress percentage or room counter.

## Content
- [ ] CT-01: Catalog inclusion of real and imagined landmarks
  - Action: Browse the tour catalog listing.
  - Expected: Tours explicitly feature both real-world cultural/historical sites and fully imagined or fictional destinations, labeled appropriately.
  - Bug Report:
    - Issue: Missing Labels for Real and Imagined/Fictional Destinations
    - Actual: Tours in the catalog lack labels identifying whether a destination is a real-world cultural/historical site or a fully imagined/fictional landmark (cards display only theme and difficulty tags).

- [X] CT-02: Comprehensive exhibit educational detail
  - Action: Open the "Deep Dive" tab of an exhibit detail view.
  - Expected: The panel displays in-depth historical or artistic context, high-resolution media, and verified educational commentary.

- [X] CT-03: Relevancy of end-of-tour suggestions
  - Action: Complete a tour and inspect the "Related Tours" section at the end.
  - Expected: All suggested tours share related metadata (such as matching theme, historical period, or cultural origin) with the completed tour.