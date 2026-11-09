# Test Result

## Functionality
- [X] FT-01: Curated collections are browsable from the home page.
  - Action: Open the home page and click a curated collection.
  - Expected: Each collection shows a title and its stories, and clicking it displays that collection's story list.
- [ ] FT-02: Story detail page opens from a story card.
  - Action: Click any story card in a collection.
  - Expected: The detail page shows the story title, introduction text, and sections for timeline, image gallery, and media clips.
  - Bug Report:
    - Issue: Missing Section (Media Clips)
    - Actual: On `/story/ancient-roman-baths` the page has the title, intro, "Historical Timeline" and "Gallery" headings, but no media clips section. The DOM contains 0 `audio`, 0 `video`, and 0 `iframe` elements.
- [X] FT-03: Image gallery can be navigated.
  - Action: On a story page, click a gallery image to open it, then use "Next" and "Previous" to step through all images.
  - Expected: The enlarged image changes in order for each click and every gallery image can be reached.
- [ ] FT-04: Embedded audio and video clips play.
  - Action: On a story page, press play on the embedded audio clip, then on the video clip, then pause each.
  - Expected: Each clip starts playing, its audio and video are output, and pause stops it.
  - Bug Report:
    - Issue: Unresponsive Media Player / Missing Video Clip
    - Actual: On `/story/artisan-quarter` the audio element has `readyState` 0 and `networkState` 3 (no source loaded), and `play()` never resolved (the call hung until the tool timed out). No `video` element exists on any tested story page. On `/story/carnival-of-masks` a "Watch the Story" play button is rendered, but no media element backs it.
- [ ] FT-05: Keyword search returns matching stories.
  - Action: Type "festival" in the search box and press Enter or click the search button.
  - Expected: Results list only stories whose title or text contains "festival", and the count of results is shown.
  - Bug Report:
    - Issue: Missing Result Count
    - Actual: Searching "festival" lists two stories (The Wine Harvest Festival, The Carnival of Masks), but no result count appears anywhere in the DOM. The Carnival of Masks card's visible title and summary do not contain "festival", so it was probably matched through its tag, which is not in the stated match rule.
- [X] FT-06: Topic filter shows only stories in that topic.
  - Action: Click the "food" filter on the stories list.
  - Expected: Only stories tagged "food" are listed, and the other topics ("history", "neighborhoods") are not.
- [X] FT-07: Story can be saved to Favorites.
  - Action: On a story detail page, click "Save".
  - Expected: The story is added to the Favorites list.
- [X] FT-08: Saved stories can be reopened from Favorites.
  - Action: Open "Favorites" from the navigation and click a saved story.
  - Expected: The Favorites page lists the saved story, and clicking it opens its detail page.

## Constraint
- [ ] CS-01: Empty search does not run.
  - Action: Leave the search box empty and click the search button.
  - Expected: No search is executed, the current results stay unchanged, and no error appears.
  - Bug Report:
    - Issue: Unexpected Results Reset
    - Actual: With the two "festival" results showing, the search box was cleared and the Explore button clicked. The Explore Stories grid changed from 2 results to all 8 stories (Roman Baths, Street Food, Carnival, Artisan Quarter, Wine Harvest, Midnight Bakeries, Bell Tower Keepers, Jewish Quarter). No error appeared.
- [X] CS-02: Keyword and topic filter combine.
  - Action: Select the "history" filter, then search for a keyword that appears only in a "food" story.
  - Expected: No "food" story is shown; results include only stories that match both the keyword and the "history" topic.
- [ ] CS-03: A story cannot be saved twice.
  - Action: Save a story, return to its page, and click the saved button again.
  - Expected: The story appears exactly once in Favorites.
  - Bug Report:
    - Issue: Unexpected Unsave on Repeat Click
    - Actual: After saving "The Ancient Roman Baths", returning to its page and clicking "Saved" changed the button to "Save for later" and removed the story. Favorites then showed "0 stories saved" with the empty state. Re-saving gives exactly one entry, so duplication does not occur, but the story does not appear once after the second click.
- [X] CS-04: Unsaving removes a story from Favorites.
  - Action: On a saved story, click the saved button to unsave it, then open Favorites.
  - Expected: The story no longer appears in the Favorites list.
- [X] CS-05: Favorites persist after page reload.
  - Action: Save a story, reload the page, and open Favorites.
  - Expected: The saved story is still listed, and its detail page shows the saved state.
- [X] CS-06: Media does not play automatically.
  - Action: Open a story page that contains audio or video, and wait 5 seconds without pressing play.
  - Expected: No audio plays and no video starts playing.

## Interaction
- [X] IX-01: Search with no matches shows a message.
  - Action: Search for "zzzxqv".
  - Expected: A message such as "No stories found" appears in place of results, with no broken layout.
- [ ] IX-02: Saving gives immediate feedback.
  - Action: On a story detail page, click "Save".
  - Expected: The button label changes to "Saved" and a success toast "Added to Favorites" appears.
  - Bug Report:
    - Issue: Missing Success Toast
    - Actual: The button label changed to "Saved" and the nav count went to 1, but "Added to Favorites" is absent from the DOM. The notification region was empty right after the click and still had no toast text 800 ms later.
- [ ] IX-03: Timeline entries expand and collapse.
  - Action: Click a timeline entry on a story page, then click it again.
  - Expected: The first click expands the entry to show its description and the entry's indicator changes; the second click collapses it.
  - Bug Report:
    - Issue: Unresponsive Timeline Entry
    - Actual: Timeline entries are not interactive: the entry container has 0 buttons and no `aria-expanded`. The description ("Emperor Augustus commissions the first public baths on this site") is visible before any click. Clicking the entry heading, the entry container, and then the heading again left the entry text unchanged, with no expand or collapse.

## Content
- [X] CT-01: Stories under each topic filter are relevant to that topic.
  - Action: Apply the "history", "food", and "neighborhoods" filters one at a time and read the titles and summaries shown.
  - Expected: Every listed story's title and summary clearly relate to the selected topic.
- [X] CT-02: Gallery images are relevant and load correctly.
  - Action: Open the gallery on three different story pages and step through every image.
  - Expected: All images load (none broken or blank) and each depicts the subject of its story.
- [ ] CT-03: Embedded media clips load and match their story.
  - Action: Play the audio and video clip on three different story pages.
  - Expected: Each clip loads without an error message and its content matches the story's topic.
  - Bug Report:
    - Issue: Broken Media Clip / Missing Media
    - Actual: Across the three story pages checked, only the Artisan Quarter has a clip. Its audio (`/audio/artisan-quarter.mp3`) reports `readyState` 0 and `networkState` 3, and playback never started. The Carnival of Masks and A Street Food Odyssey pages have no audio or video. No video clip exists on any page.

---

**Notes**
- Playwright tool budget: about 84 of 100 calls used.
- CT-02 is marked PASS on load status and alt text only (all gallery images on the Carnival, Street Food and Artisan Quarter pages have `naturalWidth > 0`). Whether each photo depicts its story can't be judged from the DOM alone, so this is a partial verification.
- Gallery Next/Previous controls have no accessible names (icon-only). They work correctly, but screen readers can't identify them.
- The filter state does not refresh results reliably. After Food → History with a keyword active, the grid kept the Food-filtered result (Street Food) under the History filter. Clicking the topic chips in a different order produces different results, so this sequence is worth a separate check.
- CT-01 note: The Jewish Quarter appears under Neighborhoods but is tagged History and Food & Drink, not Neighborhoods. Its summary is about a quarter, so I judged it relevant.
- Clicking Play on the Artisan Quarter audio hung the Playwright evaluate call until it timed out, which supports the FT-04 failure.