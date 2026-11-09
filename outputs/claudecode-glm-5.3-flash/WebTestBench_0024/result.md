All tests executed. Compiling the final report.

# Test Result

## Functionality

- [X] FT-01: Curated story collections are visible on the homepage
  - Action: Open the site homepage and view the collections area.
  - Expected: At least one curated collection (e.g., "History", "Festivals", "Food", "Hidden Attractions") is displayed with story cards in each.

- [X] FT-02: User can open a story's detail page from a collection
  - Action: Click a story card in any collection.
  - Expected: A detail page opens showing the story's title, topic, and full story content.

- [X] FT-03: Expandable timeline expands and collapses in a story detail page
  - Action: Open a story with a timeline section and click its header/expand control.
  - Expected: Timeline events (e.g., dated entries) become visible; clicking again collapses them.

- [X] FT-04: Image gallery is viewable in a story detail page
  - Action: Open a story with an image gallery and browse the images (e.g., click thumbnails or next/prev arrows).
  - Expected: Multiple images display and the user can navigate between them without errors.

- [ ] FT-05: Embedded audio clip plays in a story detail page
  - Action: Open a story containing an audio clip and press the play control.
  - Expected: Audio begins playing (play state indicated); pause/stop also works.
  - Bug Report:
    - Issue: Unplayable / Broken Media Source
    - Actual: Only "The Artisan Quarter" story has an audio player ("Listen to the Story" — native `<audio controls>` with source `/audio/artisan-quarter.mp3`). Pressing play produces no playback: the audio stays paused at currentTime 0 (readyState 0). Root cause: the server returns HTTP 200 but with content-type `text/html` and the SPA's index.html body (first bytes `<!do`) instead of an mp3 file — the media fails to decode with MediaError code 4 (SRC_NOT_SUPPORTED). The audio source is broken; no play state is ever indicated.

- [X] FT-06: Embedded video clip plays in a story detail page
  - Action: Open a story containing a video clip and press the play control.
  - Expected: Video content plays visibly in the page with working play/pause controls.

- [X] FT-07: Keyword search returns matching stories
  - Action: Enter a keyword that matches an existing story (e.g., a festival or dish name from the default data) into the search box and submit.
  - Expected: Only stories relevant to the keyword are listed in the results.

- [X] FT-08: Topic filter narrows the story list
  - Action: Apply a topic filter such as "History" (or "Food", "Neighborhoods") from the filter controls.
  - Expected: Only stories belonging to that topic are displayed; other topics are excluded.

- [X] FT-09: User can save a story to favorites
  - Action: Open any story (or view its card) and click the save/favorite control (e.g., a heart or "Save" button).
  - Expected: The story is marked as saved (control shows saved/active state).

- [X] FT-10: Saved stories appear in the favorites list
  - Action: Save one or more stories, then open the favorites list/page.
  - Expected: All saved stories are listed with their titles and can be opened from the list.

- [X] FT-11: User can remove a story from favorites
  - Action: In the favorites list (or on a saved story), click the remove/unsave control.
  - Expected: The story is removed from the favorites list.

## Constraint

- [X] CS-01: Search with no matching results shows an empty state, not an error
  - Action: Enter a nonsense keyword (e.g., "zzzqqq") into the search box and submit.
  - Expected: A "no results" style message is shown; no broken page, crash, or unrelated stories listed.

- [X] CS-02: Applying a topic filter excludes stories of other topics
  - Action: Apply the "Food" filter, then check the listed stories against their displayed topics.
  - Expected: Every listed story is tagged "Food"; no "History" or "Neighborhoods" stories appear.

- [X] CS-03: A story cannot be saved twice as a duplicate favorite
  - Action: Save a story, then click the save control on the same story again.
  - Expected: The favorites list still contains only one entry for that story (the control toggles to "saved"/remove state instead of adding a duplicate).

- [X] CS-04: Favorites persist when navigating away and returning
  - Action: Save a story, navigate to another page (e.g., a different collection), then return to the favorites list.
  - Expected: The saved story is still present in the favorites list.

## Interaction

- [X] IX-01: Filter selection updates the story list immediately
  - Action: Click a topic filter (e.g., "History") while viewing the story list.
  - Expected: The visible list updates right away to show only matching stories, and the active filter is visibly indicated as selected.

- [X] IX-02: Clearing filters/search restores the full story list
  - Action: After filtering or searching, click the clear/reset control (or clear the search box).
  - Expected: All stories are shown again, as before the filter/search was applied.

- [X] IX-03: Saving a story gives immediate visual feedback
  - Action: Click the save/favorite control on a story.
  - Expected: The control's appearance changes immediately (e.g., heart fills in, label changes to "Saved"), without requiring a page reload.

## Content

- [X] CT-01: Every story belongs to one of the supported topics
  - Action: Browse the story list and detail pages and check each story's topic label.
  - Expected: Each story shows a topic among "History", "Festivals", "Food", "Neighborhoods", or "Hidden Attractions" (culture-themed categories).

- [X] CT-02: Story detail pages contain complete culture-themed content
  - Action: Open 2–3 stories from different topics and read their detail pages.
  - Expected: Each page has a meaningful description of the city's culture (history, festival, food, or attraction) — no placeholder text like "Lorem ipsum" or empty sections.

- [ ] CT-03: Gallery and media content is relevant to its story
  - Action: Open a story's image gallery and audio/video clip and inspect them.
  - Expected: Images and media depict content matching the story's subject (e.g., a food story shows food imagery); no broken/missing images or unplayable media.
  - Bug Report:
    - Issue: Unplayable Media / Broken Image
    - Actual: Gallery images are relevant and load correctly (e.g., "The Ancient Roman Baths - Image 1/2/3" all render, alt-text matched to subject; Artisan Quarter gallery: 7/7 images loaded). However, the audio narration clip on "The Artisan Quarter" is unplayable — the source `/audio/artisan-quarter.mp3` returns the SPA's index.html (content-type text/html, MediaError code 4), so the "Listen to the Story" media never plays. Additionally, one related-story card image on the "Carnival of Masks" detail page is broken (alt "The Bell Tower Keepers", URL `https://images.unsplash.com/photo-1564429238857-4b5912e6a71f?w=1200` loads with naturalWidth=0). Per the expected criterion "no broken/missing images or unplayable media," this is a deviation.