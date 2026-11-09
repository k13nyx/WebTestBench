# Test Checklist

## Functionality
- [ ] FT-01: Browse curated collections
  - Action: Open the homepage and locate the curated collections section.
  - Expected: Multiple collections are displayed (e.g., history, festivals, food, hidden gems), each containing listed stories that can be opened.

- [ ] FT-02: Open a story detail page
  - Action: Click on any story card/title from a collection listing.
  - Expected: A dedicated detail page opens showing the story's full title, body text, and media elements.

- [ ] FT-03: Expandable timeline on story page
  - Action: Open a story that contains a timeline and click the timeline control.
  - Expected: The timeline expands to reveal chronological entries/events of the story.

- [ ] FT-04: Image gallery navigation
  - Action: Open a story's image gallery and click the next/previous navigation control.
  - Expected: The displayed image changes to the next/previous image in the set.

- [ ] FT-05: Play embedded audio/video clip
  - Action: Open a story containing an embedded clip and click its play button.
  - Expected: The audio/video clip starts playing within the page.

- [ ] FT-06: Search stories by keyword
  - Action: Type a keyword from an existing story title (e.g., "festival") into the search box and submit.
  - Expected: A results list appears containing only stories matching the keyword.

- [ ] FT-07: Filter stories by topic
  - Action: Apply the "history" topic filter (then repeat with "food" and "neighborhoods").
  - Expected: The listing updates to show only stories belonging to the selected topic.

- [ ] FT-08: Save a story to favorites
  - Action: Open a story and click its save/favorite control.
  - Expected: The story is added to the favorites list.

- [ ] FT-09: Revisit saved favorites
  - Action: After saving at least two stories, navigate to the favorites list.
  - Expected: The favorites page lists all previously saved stories, each openable to its detail page.

## Constraint
- [ ] CS-01: Search with no matching results
  - Action: Enter a nonsense keyword (e.g., "zzzzqqq") and submit the search.
  - Expected: An explicit "no results found" message is shown; no broken/blank page or error appears.

- [ ] CS-02: Duplicate favorites are not created
  - Action: Click the save control on an already-saved story (or save it again from its detail page).
  - Expected: The story appears only once in the favorites list.

- [ ] CS-03: Empty favorites state
  - Action: With no stories saved, open the favorites list.
  - Expected: An empty-state message (e.g., "No saved stories yet") is displayed instead of an empty/broken view.

## Interaction
- [ ] IX-01: Save control reflects state immediately
  - Action: Click the save/favorite control on a story.
  - Expected: The control visually changes to a "saved/filled" state right away without a page reload.

- [ ] IX-02: Timeline can be collapsed again
  - Action: Expand a story timeline, then click the timeline control again.
  - Expected: The timeline collapses back to its original compact state.

- [ ] IX-03: Gallery indicates the currently viewed image
  - Action: Navigate through the image gallery.
  - Expected: The gallery highlights the active image (e.g., thumbnail selection or counter like "2/5") as the user navigates.

## Content
- [ ] CT-01: Stories match the city-culture themes
  - Action: Open three stories from different collections.
  - Expected: Each story's content is about the city's history, festivals, traditional food, or hidden attractions — no off-topic content.

- [ ] CT-02: Gallery images are relevant to their story
  - Action: Open the image gallery of a story about a specific topic (e.g., food).
  - Expected: All displayed images depict subjects matching that story's topic.

- [ ] CT-03: Filter labels and embedded media are on-theme
  - Action: Review the topic filter options and play one embedded clip.
  - Expected: Filters include "history," "food," and "neighborhoods"; the clip's subject matches its story's topic.