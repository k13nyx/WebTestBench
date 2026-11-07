# Test Checklist

## Functionality
- [ ] FT-01: Browse curated story collections on the homepage
  - Action: Open the website homepage.
  - Expected: A curated collection of story cards (e.g., history, festivals, food, hidden attractions) is displayed and browsable.

- [ ] FT-02: Open a detailed page for an individual story
  - Action: Click the title or card of any story in the collection.
  - Expected: A detailed story page opens showing the full story content.

- [ ] FT-03: Search stories by keyword
  - Action: Type a keyword into the search box and submit.
  - Expected: Only stories whose title or content match the keyword are shown.

- [ ] FT-04: Filter stories by topic
  - Action: Click the "history", "food", or "neighborhoods" topic filter.
  - Expected: The story list updates to show only stories belonging to the selected topic.

- [ ] FT-05: Save a story to the favorites list
  - Action: On a story (card or detail page), click the "Save" / favorite button.
  - Expected: The story is added to the favorites list.

- [ ] FT-06: Revisit saved favorites during the trip
  - Action: Click the "Favorites" link/section.
  - Expected: All previously saved stories are listed and openable.

## Constraint
- [ ] CS-01: Search with no matching keyword shows an empty state
  - Action: Enter a keyword with no matching stories and submit.
  - Expected: A clear "no results" message is shown; the app does not crash or error.

- [ ] CS-02: A story cannot be saved to favorites more than once
  - Action: Click "Save" on a story already in favorites.
  - Expected: No duplicate entry appears in the favorites list.

- [ ] CS-03: Selecting a topic filter restricts results to that topic only
  - Action: Apply the "food" filter.
  - Expected: No stories categorized under other topics (e.g., history) appear in the results.

## Interaction
- [ ] IX-01: Expandable timeline expands and collapses on click
  - Action: Click the timeline element on a story detail page.
  - Expected: The timeline expands to show entries, and clicks again to collapse it.

- [ ] IX-02: Image gallery navigates between images
  - Action: Click the next/thumbnail control in a story's image gallery.
  - Expected: The displayed image changes to the selected/next image.

- [ ] IX-03: Embedded audio/video clip plays on activation
  - Action: Click the play control on an embedded audio or video clip.
  - Expected: The clip begins playing.

- [ ] IX-04: Favorite button reflects saved state
  - Action: Click "Save" on a story.
  - Expected: The button shows a saved/active visual state (e.g., filled icon or "Saved" label).

## Content
- [ ] CT-01: Stories cover the required cultural themes
  - Action: Review the story collection and detail pages.
  - Expected: Content exists for history, festivals, traditional food, and hidden attractions.

- [ ] CT-02: Gallery and media are relevant to the city/culture theme
  - Action: Inspect images and audio/video on story pages.
  - Expected: All media directly relate to the specific story's city, culture, or topic.

- [ ] CT-03: Each story has a clear title, topic label, and descriptive text
  - Action: Open several story detail pages.
  - Expected: Every story displays a title, a topic/category label, and readable descriptive content.