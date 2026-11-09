# Test Checklist

## Functionality
- [ ] FT-01: Browse curated collections
  - Action: Navigate to the curated collections section on the main page and click on any collection card.
  - Expected: The selected collection opens and displays its list of associated cultural stories.
- [ ] FT-02: Open story detail page
  - Action: Click on a story card from a collection or story catalog.
  - Expected: Navigates to the dedicated story detail page displaying the full narrative, title, and topic tags.
- [ ] FT-03: Keyword search for cultural stories
  - Action: Type a valid keyword (e.g., "festival") into the search bar and press Enter.
  - Expected: The story list updates to show only stories containing the search term in their title or text.
- [ ] FT-04: Filter stories by cultural topic
  - Action: Click on a specific topic filter button (e.g., "History", "Food", or "Neighborhoods").
  - Expected: The story listing updates to display exclusively stories assigned to the selected topic.
- [ ] FT-05: Play embedded audio or video clips
  - Action: Click the "Play" button on an embedded audio or video player within a story page.
  - Expected: Media playback starts successfully with accessible pause and volume controls.
- [ ] FT-06: Add story to favorites list
  - Action: Click the "Save to Favorites" button on any story card or detail page.
  - Expected: The story is added to the user's favorites list and the button state reflects it is saved.
- [ ] FT-07: View saved stories in favorites list
  - Action: Navigate to the "Favorites" section or page.
  - Expected: All previously saved stories are listed with links to access their detailed pages.
- [ ] FT-08: Remove story from favorites list
  - Action: Click the "Remove" or un-favorite button next to an item in the Favorites list.
  - Expected: The story is removed from the Favorites list immediately.

## Constraint
- [ ] CS-01: Non-matching search query handling
  - Action: Enter a non-existent search term (e.g., "zzxxqq99") in the search input and submit.
  - Expected: Displays a "No stories found" message without crashing or displaying unrelated content.
- [ ] CS-02: Empty favorites list state
  - Action: Open the Favorites page when no stories have been favorited.
  - Expected: Displays an empty-state message (e.g., "No saved stories yet") with a prompt to explore stories.
- [ ] CS-03: Prevent duplicate entries in favorites
  - Action: Click the "Save to Favorites" button on an already favorited story.
  - Expected: The story remains in the favorites list exactly once without creating duplicate entries.
- [ ] CS-04: Conflicting search and filter criteria
  - Action: Select the "Food" topic filter and search for a term exclusively related to another topic (e.g., "Ancient Architecture").
  - Expected: Displays zero matching results with guidance to clear filters, rather than overriding the active topic filter.

## Interaction
- [ ] IX-01: Expandable timeline toggle
  - Action: Click on a collapsed event item in the story's interactive timeline.
  - Expected: The item expands smoothly to reveal full details and dates; clicking it again collapses the item.
- [ ] IX-02: Image gallery navigation
  - Action: Click the next/previous navigation arrows or thumbnail items in an image gallery.
  - Expected: The gallery transitions to display the selected image with an updated caption.
- [ ] IX-03: Favorite button state feedback
  - Action: Click the favorite/bookmark icon on a story card.
  - Expected: The icon immediately changes visual state (e.g., filled icon color) and displays a brief confirmation indicator.
- [ ] IX-04: Clear active topic filters
  - Action: Click the "Clear Filters" button or click an active topic filter button a second time.
  - Expected: Filter selection is cleared and the full default list of stories is restored.

## Content
- [ ] CT-01: Story cultural relevance and completeness
  - Action: Inspect the content across story detail pages.
  - Expected: Stories contain authentic cultural information covering the city's history, festivals, traditional foods, or hidden attractions without placeholder text.
- [ ] CT-02: Media asset integrity
  - Action: Inspect all image galleries, embedded videos, and audio clips across story pages.
  - Expected: All media files load completely without broken image icons, missing file errors, or non-functional playback streams.
- [ ] CT-03: Curated collection thematic alignment
  - Action: Review the titles and descriptions of all curated collections on the main page.
  - Expected: Collections display descriptive titles and introductory text clearly defining their specific cultural focus.