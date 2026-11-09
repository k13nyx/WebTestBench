# Test Checklist

## Functionality
- [ ] FT-01: Homepage displays curated story collections
  - Action: Open the site's home page and scan the main area.
  - Expected: At least one curated collection section is visible, each containing story cards with titles belonging to the city-culture theme.

- [ ] FT-02: Story card opens a detailed story page
  - Action: Click any story card in a collection on the home page.
  - Expected: A detail page for that story opens, showing the story's full content (title matches the clicked card, plus body text/media), not just the card view.

- [ ] FT-03: Keyword search returns matching stories
  - Action: Type a keyword taken from an existing default story's title (e.g., a word in a festival story name) into the search field and submit.
  - Expected: Results list includes that story; clicking the result opens its detail page.

- [ ] FT-04: Topic filter shows only that topic's stories
  - Action: Select the topic filter "food" (then repeat with "history" and "neighborhoods").
  - Expected: Only stories tagged with the selected topic remain listed; stories from other topics disappear.

- [ ] FT-05: Visitor can save a story to favorites
  - Action: Open a default story's detail page and click the "Favorite"/"Save" control (heart/star button).
  - Expected: The control registers the save (state changes, see IX-04) and the story appears in the favorites list.

- [ ] FT-06: Favorites list is revisitable during the trip
  - Action: After saving 2 stories, navigate to the favorites page/section, then reload the browser and return to favorites.
  - Expected: Both saved stories are still listed in favorites and each opens its correct detail page.

## Constraint
- [ ] CS-01: A story cannot be favorited twice
  - Action: Open one story, click Favorite, click Favorite again, then click Favorite a third time; finally open the favorites list.
  - Expected: The control toggles on/off/on; the favorites list contains exactly one entry for that story (no duplicates, and none after the second click removed it).

- [ ] CS-02: Search with no matches shows an explicit empty result state
  - Action: Search for a nonsense keyword, e.g., "zzzqqq123".
  - Expected: A clear "no stories found" (or equivalent) message is shown; the page does not crash, show a blank list, or display unrelated stories.

- [ ] CS-03: Filter and search cannot produce contradictory results
  - Action: With topic filter "history" active, search a keyword that only exists in a "food" story; then search a keyword that exists in a "history" story.
  - Expected: The first combination yields no results (or an empty-state message); the second yields only the matching history story. Results never include stories outside the active filter.

- [ ] CS-04: Empty favorites list renders a defined empty state
  - Action: On a fresh session (no favorites saved), open the favorites page/section.
  - Expected: An empty-state message such as "No saved stories yet" is displayed instead of a broken or blank list.

## Interaction
- [ ] IX-01: Timeline expands and collapses on click
  - Action: On a story detail page with a timeline, click a timeline entry/section header to expand it, then click again to collapse.
  - Expected: Expanded content reveals the detailed event text; collapsing hides it again; both toggles respond immediately to clicks.

- [ ] IX-02: Image gallery opens and navigates between images
  - Action: Click a gallery thumbnail on a story detail page; use next/previous controls (or arrow behavior) to move through the images; then close the gallery.
  - Expected: The selected image opens in the gallery view, navigation steps through each image in order, and closing returns to the story page.

- [ ] IX-03: Embedded audio/video clip plays
  - Action: On a story detail page, press play on an embedded audio or video clip.
  - Expected: Playback starts (progress/playing state advances or audible sound), and pause stops it. The media element is not a dead/broken player.

- [ ] IX-04: Favorite action gives immediate visual feedback
  - Action: Click the Favorite control on a story detail page and observe the button and any confirmation message.
  - Expected: The button visibly changes state (e.g., filled heart/star vs. outline) at the moment of the click, and any success toast/label appears without a page reload.

## Content
- [ ] CT-01: Default stories cover all four cultural themes
  - Action: Browse the collections and inspect story titles/tags on the home page.
  - Expected: Stories exist for each required theme: history, festivals, traditional food, and hidden attractions (all four represented, none replaced by unrelated topics).

- [ ] CT-02: Story detail pages contain complete, consistent content
  - Action: Open three different default story detail pages and compare against their cards.
  - Expected: Each detail page shows the story's title, descriptive body text, its topic tag(s), and at least one interactive element (timeline, gallery, or media clip); titles match the cards exactly.

- [ ] CT-03: All images and media are relevant and load correctly
  - Action: Inspect images in collections, galleries, and story pages across the site.
  - Expected: Every image renders (no broken-image icons or empty placeholders) and depicts content relevant to the city's culture theme (e.g., food photos on food stories, not generic stock unrelated to the story).

**Total: 17 items** (FT: 6, CS: 4, IX: 4, CT: 3) — every item maps to a stated requirement in the instruction, uses default data only, and yields a binary PASS/FAIL.