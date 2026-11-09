# Test Checklist

## Functionality
- [ ] FT-01: Curated collections are browsable from the home page.
  - Action: Open the home page and click a curated collection.
  - Expected: Each collection shows a title and its stories, and clicking it displays that collection's story list.
- [ ] FT-02: Story detail page opens from a story card.
  - Action: Click any story card in a collection.
  - Expected: The detail page shows the story title, introduction text, and sections for timeline, image gallery, and media clips.
- [ ] FT-03: Image gallery can be navigated.
  - Action: On a story page, click a gallery image to open it, then use "Next" and "Previous" to step through all images.
  - Expected: The enlarged image changes in order for each click and every gallery image can be reached.
- [ ] FT-04: Embedded audio and video clips play.
  - Action: On a story page, press play on the embedded audio clip, then on the video clip, then pause each.
  - Expected: Each clip starts playing, its audio and video are output, and pause stops it.
- [ ] FT-05: Keyword search returns matching stories.
  - Action: Type "festival" in the search box and press Enter or click the search button.
  - Expected: Results list only stories whose title or text contains "festival", and the count of results is shown.
- [ ] FT-06: Topic filter shows only stories in that topic.
  - Action: Click the "food" filter on the stories list.
  - Expected: Only stories tagged "food" are listed, and the other topics ("history", "neighborhoods") are not.
- [ ] FT-07: Story can be saved to Favorites.
  - Action: On a story detail page, click "Save".
  - Expected: The story is added to the Favorites list.
- [ ] FT-08: Saved stories can be reopened from Favorites.
  - Action: Open "Favorites" from the navigation and click a saved story.
  - Expected: The Favorites page lists the saved story, and clicking it opens its detail page.

## Constraint
- [ ] CS-01: Empty search does not run.
  - Action: Leave the search box empty and click the search button.
  - Expected: No search is executed, the current results stay unchanged, and no error appears.
- [ ] CS-02: Keyword and topic filter combine.
  - Action: Select the "history" filter, then search for a keyword that appears only in a "food" story.
  - Expected: No "food" story is shown; results include only stories that match both the keyword and the "history" topic.
- [ ] CS-03: A story cannot be saved twice.
  - Action: Save a story, return to its page, and click the saved button again.
  - Expected: The story appears exactly once in Favorites.
- [ ] CS-04: Unsaving removes a story from Favorites.
  - Action: On a saved story, click the saved button to unsave it, then open Favorites.
  - Expected: The story no longer appears in the Favorites list.
- [ ] CS-05: Favorites persist after page reload.
  - Action: Save a story, reload the page, and open Favorites.
  - Expected: The saved story is still listed, and its detail page shows the saved state.
- [ ] CS-06: Media does not play automatically.
  - Action: Open a story page that contains audio or video, and wait 5 seconds without pressing play.
  - Expected: No audio plays and no video starts playing.

## Interaction
- [ ] IX-01: Search with no matches shows a message.
  - Action: Search for "zzzxqv".
  - Expected: A message such as "No stories found" appears in place of results, with no broken layout.
- [ ] IX-02: Saving gives immediate feedback.
  - Action: On a story detail page, click "Save".
  - Expected: The button label changes to "Saved" and a success toast "Added to Favorites" appears.
- [ ] IX-03: Timeline entries expand and collapse.
  - Action: Click a timeline entry on a story page, then click it again.
  - Expected: The first click expands the entry to show its description and the entry's indicator changes; the second click collapses it.

## Content
- [ ] CT-01: Stories under each topic filter are relevant to that topic.
  - Action: Apply the "history", "food", and "neighborhoods" filters one at a time and read the titles and summaries shown.
  - Expected: Every listed story's title and summary clearly relate to the selected topic.
- [ ] CT-02: Gallery images are relevant and load correctly.
  - Action: Open the gallery on three different story pages and step through every image.
  - Expected: All images load (none broken or blank) and each depicts the subject of its story.
- [ ] CT-03: Embedded media clips load and match their story.
  - Action: Play the audio and video clip on three different story pages.
  - Expected: Each clip loads without an error message and its content matches the story's topic.