# Test Checklist

## Functionality
- [ ] FT-01: Browse the tour catalog
  - Action: Open the site's tour catalog/homepage.
  - Expected: A list of tours is displayed, each with a title and its type (museum, art gallery, historical site, or cultural landmark).
- [ ] FT-02: Select and start a tour
  - Action: Click a tour in the catalog to open it.
  - Expected: The tour opens and displays its first room/area with its exhibits.
- [ ] FT-03: Move between rooms/areas
  - Action: Use the tour's next/back navigation to move through at least two different rooms or areas.
  - Expected: Each click loads the next/previous room, showing that room's exhibits and title.
- [ ] FT-04: Open layered exhibit content
  - Action: Click on an exhibit within a room.
  - Expected: A content panel opens with layered sections: an overview, a deeper dive, and related items.
- [ ] FT-05: Take an in-tour quiz
  - Action: Open a quiz inside a tour, select an answer, and submit it.
  - Expected: The quiz registers the answer and displays a result/feedback (correct or incorrect).
- [ ] FT-06: Use the in-tour timeline
  - Action: Open a timeline element inside a tour and select one of its entries.
  - Expected: The selected timeline entry reveals its associated information.
- [ ] FT-07: Bookmark a tour
  - Action: Click the bookmark control on a tour in the catalog.
  - Expected: The tour is saved and appears in the bookmarks list.
- [ ] FT-08: Mark a tour as "in progress"
  - Action: Start a tour and navigate to a room other than the first one.
  - Expected: The tour's status shows as "in progress" (in the catalog or tour list).
- [ ] FT-09: Resume a tour where left off
  - Action: Leave a tour mid-way, then choose to resume it from the catalog.
  - Expected: The tour reopens at the last visited room/area, not at the beginning.
- [ ] FT-10: Search for tours
  - Action: Enter a keyword (e.g., a theme or place name) in the search field.
  - Expected: The catalog shows only tours matching the keyword.
- [ ] FT-11: Filter tours by attributes
  - Action: Apply filters for theme, historical period, culture, and difficulty level (one at a time).
  - Expected: Each filter narrows the list to tours having the selected attribute value.

## Constraint
- [ ] CS-01: Multiple filters combine restrictively
  - Action: Apply two or more filters at once (e.g., culture + difficulty).
  - Expected: Only tours matching ALL applied filters are shown; non-matching tours are excluded.
- [ ] CS-02: Empty search results are handled
  - Action: Enter a search term that matches no tour (e.g., "zzzz").
  - Expected: An explicit "no results" state is shown and no unrelated tours are listed.
- [ ] CS-03: Quiz cannot be submitted unanswered
  - Action: Open a quiz and attempt to submit without selecting any answer.
  - Expected: Submission is blocked or the quiz prompts that an answer must be selected; no result is shown.

## Interaction
- [ ] IX-01: Exhibit panel opens and closes cleanly
  - Action: Click an exhibit to open its content, then close the panel.
  - Expected: The panel opens on click and closes via its close control, returning to the same room view.
- [ ] IX-02: Switch between content layers
  - Action: In an open exhibit panel, switch between "overview", "deeper dive", and "related items".
  - Expected: Each selection immediately displays that layer's content while the panel stays open.
- [ ] IX-03: Tour progress indicator updates
  - Action: Navigate through rooms in a tour.
  - Expected: A visible progress indicator (e.g., "Room 3 of 6" or a progress bar) updates after each navigation.

## Content
- [ ] CT-01: Catalog covers the required tour variety
  - Action: Review the full catalog.
  - Expected: Tours include museums, art galleries, historical sites, and cultural landmarks, and include both real and clearly labeled fully imagined places.
- [ ] CT-02: Exhibit content is educational and on-theme
  - Action: Open the layered content of at least three exhibits across different tours.
  - Expected: All text is relevant to its tour's subject, reads as real educational content, and contains no placeholder/lorem text.
- [ ] CT-03: End-of-tour suggestions are relevant
  - Action: Reach the end of a tour and review the suggested related tours.
  - Expected: Suggestions are actual tours from the catalog that relate to the completed tour's theme, period, or culture, and each can be opened.