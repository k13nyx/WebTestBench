# Test Checklist

## Functionality
- [ ] FT-01: Browse curated city-culture collections
  - Action: Open the main explore page and review the available collections.
  - Expected: Existing curated collections are displayed and can be selected.

- [ ] FT-02: Open a story detail page
  - Action: Select any story from a collection.
  - Expected: A dedicated detail page opens with the story title, description, and cultural content.

- [ ] FT-03: Search stories by keyword
  - Action: Enter a keyword appearing in an existing story title or description into the search field and submit the search.
  - Expected: The results display stories matching the entered keyword.

- [ ] FT-04: Filter stories by topic
  - Action: Apply the “history,” “food,” and “neighborhoods” topic filters one at a time.
  - Expected: Each filter displays only stories assigned to its selected topic.

- [ ] FT-05: Save and revisit a favorite story
  - Action: Select the save/favorite control on an existing story, open the Favorites list, and select the saved story.
  - Expected: The story appears in Favorites and can be reopened from that list.

- [ ] FT-06: Remove a story from Favorites
  - Action: Remove a saved story using its save/favorite control or the Favorites list.
  - Expected: The story is removed from the Favorites list.

## Constraint
- [ ] CS-01: Prevent unmatched search results from showing unrelated stories
  - Action: Search for a keyword that does not appear in any existing story.
  - Expected: No unrelated stories are displayed, and a clear empty-results state is shown.

- [ ] CS-02: Enforce combined search and topic filtering
  - Action: Enter a keyword, apply a topic filter, and review the results.
  - Expected: Every result matches both the keyword and the selected topic.

- [ ] CS-03: Prevent duplicate favorites
  - Action: Save the same story more than once.
  - Expected: The story appears only once in the Favorites list.

- [ ] CS-04: Keep Favorites state consistent
  - Action: Save a story, navigate away, return to Favorites, and then remove the story.
  - Expected: The saved story remains available until removed, and disappears immediately after removal.

## Interaction
- [ ] IX-01: Expand and collapse the story timeline
  - Action: Select a collapsed timeline entry on a story detail page, then select it again.
  - Expected: The entry expands to show its details and collapses back without affecting other page content.

- [ ] IX-02: Navigate the story image gallery
  - Action: Use the gallery next and previous controls on a story detail page.
  - Expected: The displayed image changes to the selected image, and the gallery indicates the current position when such an indicator is provided.

- [ ] IX-03: Use embedded audio or video controls
  - Action: Start an embedded audio or video clip, pause it, and resume playback.
  - Expected: The clip starts, pauses, and resumes through the visible media controls.

- [ ] IX-04: Provide visible feedback for favorite changes
  - Action: Select the favorite control for an unsaved story and then select it again.
  - Expected: The control visibly changes to indicate saved and unsaved states, and each action updates the Favorites state.

## Content
- [ ] CT-01: Display the required city-culture topics
  - Action: Review the existing collections and stories.
  - Expected: Content includes stories about the city’s history, festivals, traditional food, and hidden attractions.

- [ ] CT-02: Keep story media relevant to its story
  - Action: Open several story detail pages and review their text, images, timelines, and embedded clips.
  - Expected: Each displayed media item and supporting text directly relates to the selected city story.

- [ ] CT-03: Preserve story content integrity across views
  - Action: Compare a story’s title and summary in its collection card with the corresponding detail page.
  - Expected: The detail page represents the same story and does not display mismatched title, summary, or media content.