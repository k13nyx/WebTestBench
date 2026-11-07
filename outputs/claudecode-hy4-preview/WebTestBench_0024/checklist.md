# Test Checklist

## Functionality
- [ ] FT-01: Homepage displays curated story collections
  - Action: Load the site's homepage.
  - Expected: At least one curated collection (e.g., a themed collection card with a title and cover image) is visible and clickable.

- [ ] FT-02: Opening a collection lists the stories it contains
  - Action: Click any collection card on the homepage.
  - Expected: A collection page opens showing that collection's title and a list/grid of multiple story cards belonging to it.

- [ ] FT-03: A story can be opened to its own detail page
  - Action: From a collection or story listing, click a story card.
  - Expected: A dedicated story detail page opens showing that story's title and body content.

- [ ] FT-04: Story detail page contains the required interactive sections
  - Action: Open any story detail page and scroll through it.
  - Expected: The page contains an expandable timeline section, an image gallery section, and at least one embedded audio or video clip section.

- [ ] FT-05: Keyword search returns matching stories
  - Action: Type a keyword that appears in a default story's title (e.g., a word from a visible story title) into the search box and submit.
  - Expected: The results list shows only stories containing that keyword, and the searched keyword appears in each returned story's title or text.

- [ ] FT-06: Filtering by a topic returns only stories of that topic
  - Action: Apply the topic filter "history".
  - Expected: Every displayed story result is tagged with/assigned to the "history" topic; no story from another topic is shown.

- [ ] FT-07: Embedded audio clip plays
  - Action: On a story detail page containing an audio clip, click the audio player's play control.
  - Expected: Audio playback starts (progress/time indicator advances) and no error message appears.

- [ ] FT-08: Embedded video clip plays
  - Action: On a story detail page containing a video clip, click the video's play control.
  - Expected: Video playback starts (frames/timeline progress) and no error message appears.

- [ ] FT-09: A story can be saved to the favorites list
  - Action: On a story detail page (or story card), click the "Favorite"/"Save" control, then open the Favorites page/list.
  - Expected: The saved story appears in the favorites list with its title.

- [ ] FT-10: Saved favorites can be revisited and reopened
  - Action: Navigate away to another page, return to the Favorites list, then click a favorited story.
  - Expected: The story is still listed and clicking it opens its full story detail page.

## Constraint
- [ ] CS-01: Searching with no matches shows an empty state instead of failing
  - Action: Enter a nonsense keyword (e.g., "zzzzqqq123") into search and submit.
  - Expected: A "no results" / empty-state message is displayed, the page does not crash, and the search box remains usable.

- [ ] CS-02: The same story cannot be duplicated in the favorites list
  - Action: Favorite a story, then click the same story's favorite control again to remove it; re-add it once.
  - Expected: After re-adding, the favorites list contains exactly one entry for that story, and removing it leaves zero entries.

- [ ] CS-03: Search and topic filter narrow results together
  - Action: Apply the "food" topic filter, then enter a keyword that matches only some of the filtered stories.
  - Expected: Results satisfy both conditions (matching keyword AND "food" topic); filter and search remain active simultaneously.

- [ ] CS-04: Clearing search and filters restores the full story listing
  - Action: Clear the search box and deselect/reset the active topic filter.
  - Expected: The full default set of stories is shown again, identical in count to the original unfiltered listing.

## Interaction
- [ ] IX-01: Timeline entries expand and collapse on click
  - Action: On a story detail page, click a timeline entry, then click it again.
  - Expected: The first click reveals that entry's detail text; the second click hides it. Collapsed entries do not show their detail text.

- [ ] IX-02: Image gallery navigates between images
  - Action: In a story's gallery, click the next arrow/dot control, then the previous control.
  - Expected: The displayed main image changes to the next gallery image, and then returns to the previous image.

- [ ] IX-03: Favorite control toggles its visual state immediately
  - Action: Click the favorite control on a story, then click it again.
  - Expected: The control visibly changes to a "saved" state (e.g., filled/highlighted icon or "Saved" label) on the first click and reverts to the unsaved state on the second.

## Content
- [ ] CT-01: Topic filter options include the required topics
  - Action: Open the topic filter control on the browse/search page.
  - Expected: Available topic options include at least "history", "food", and "neighborhoods".

- [ ] CT-02: All story content matches the city-culture theme
  - Action: Open three different default stories and read their titles, topic tags, and body text.
  - Expected: Each story relates to city culture — history, festivals, traditional food, neighborhoods, or hidden attractions. No off-theme or placeholder ("Lorem ipsum") content is shown.

- [ ] CT-03: All story images load and are relevant to their story
  - Action: Open two story detail pages and view each cover image and gallery images.
  - Expected: Every image renders fully (no broken-image icons or empty frames) and depicts subject matter consistent with that story's title and text.