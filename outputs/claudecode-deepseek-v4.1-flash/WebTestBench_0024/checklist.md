# Test Checklist

## Functionality
- [ ] FT-01: Browse curated story collections from the landing page
  - Action: Load the home page and view the curated collections section.
  - Expected: At least one curated collection is displayed, each showing a title and its list of story cards.

- [ ] FT-02: Open a detailed page for a story
  - Action: Click any story card in a collection.
  - Expected: A detail page opens showing the story title, full body text, and its labeled topic(s).

- [ ] FT-03: Search stories by keyword
  - Action: Enter a valid keyword (e.g., "festival") in the search field and submit.
  - Expected: Results list shows only stories matching the keyword.

- [ ] FT-04: Filter stories by topic
  - Action: Select the "history" (then "food", then "neighborhoods") topic filter.
  - Expected: The story list updates to show only stories tagged with the selected topic.

- [ ] FT-05: Save a story to favorites
  - Action: On a story detail page, click the "Save" / favorites control.
  - Expected: The story is added to the favorites list and the control shows a saved state.

- [ ] FT-06: Revisit the favorites list
  - Action: Open the favorites list view after saving one or more stories.
  - Expected: All previously saved stories are listed and each opens its detail page when clicked.

- [ ] FT-07: Expand an expandable timeline
  - Action: On a story with a timeline, click a timeline entry.
  - Expected: The entry expands to reveal its full description.

- [ ] FT-08: Browse an image gallery
  - Action: On a story with a gallery, navigate through its images.
  - Expected: Each image loads fully and the current image is identifiable within the gallery.

- [ ] FT-09: Play an embedded audio or video clip
  - Action: Click play on an embedded clip in a story.
  - Expected: The clip plays with audible sound / visible video and can be paused.

## Constraint
- [ ] CS-01: Search with no matching keyword
  - Action: Enter a keyword that matches no story (e.g., "zzzz") and submit.
  - Expected: A "no results found" empty-state message is shown; no unrelated stories appear.

- [ ] CS-02: Submit an empty search query
  - Action: Submit the search field with no text entered.
  - Expected: The app does not error; it shows the default/unfiltered story list or blocks the empty search.

- [ ] CS-03: Apply a topic filter with no matching stories
  - Action: Apply a topic filter combined with a keyword that yields no matches.
  - Expected: A clear empty-state message is shown and no stories from other topics are displayed.

- [ ] CS-04: Prevent duplicate favorites
  - Action: Save the same story twice.
  - Expected: The story appears only once in the favorites list; no duplicate entry is created.

- [ ] CS-05: Favorites persist across navigation
  - Action: Save a story, navigate to another page, then return to the favorites list.
  - Expected: The saved story is still present in the favorites list.

## Interaction
- [ ] IX-01: Timeline expand/collapse toggle
  - Action: Click an expanded timeline entry a second time.
  - Expected: The entry collapses back to its collapsed state.

- [ ] IX-02: Gallery navigation controls respond
  - Action: Use the next/previous controls (or thumbnails) in an image gallery.
  - Expected: The displayed image advances/retreats and the active indicator updates accordingly.

- [ ] IX-03: Save action provides feedback
  - Action: Click the "Save" control on a story.
  - Expected: The control visibly changes state (e.g., fills/changes icon) and a confirmation toast or message appears.

- [ ] IX-04: Favorites count indicator updates
  - Action: Save and then remove a story from favorites.
  - Expected: The favorites count/badge increments on save and decrements on removal without a page reload.

## Content
- [ ] CT-01: Stories align with the city-culture theme
  - Action: Review all stories across the collections.
  - Expected: Every story relates to city culture (history, festivals, traditional food, or hidden attractions); no off-topic content.

- [ ] CT-02: Topic labels are accurate
  - Action: Check the topic tag(s) shown on each story against its content.
  - Expected: Each story is tagged with at least one correct topic ("history," "food," or "neighborhoods") that matches its content.

- [ ] CT-03: Images and media are relevant
  - Action: Review images, galleries, and embedded clips for each story.
  - Expected: All displayed media is directly relevant to that story's subject and loads without broken placeholders.