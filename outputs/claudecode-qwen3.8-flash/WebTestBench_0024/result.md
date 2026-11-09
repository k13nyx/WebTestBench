All testing is complete. Final verification summary: audio element exists on Artisan Quarter (native `<audio controls>`), the video plays but is a Rickroll placeholder, and two Unsplash images fail to load (confirmed `naturalWidth === 0` after `networkidle`) — visible on the homepage and on story pages.

# Test Result

## Functionality
- [X] FT-01: Homepage displays curated story collections
  - Action: Open the site's home page and scan the main area.
  - Expected: At least one curated collection section is visible, each containing story cards with titles belonging to the city-culture theme.
  - Verified: "Collections" section shows 4 curated collections (Ancient Wonders, Culinary Heritage, Living Traditions, Local Secrets) with story counts; "Featured Stories" section shows 3 culture-themed story cards; "Explore Stories" grid shows all 8 stories.

- [X] FT-02: Story card opens a detailed story page
  - Action: Click any story card in a collection on the home page.
  - Expected: A detail page for that story opens, showing the story's full content (title matches the clicked card, plus body text/media), not just the card view.
  - Verified: Clicking "The Ancient Roman Baths" card navigated to `/story/ancient-roman-baths`; page h1 "The Ancient Roman Baths" matched the card, with 4 body paragraphs, Gallery, Historical Timeline, Quick Info, and Save/Share controls.

- [X] FT-03: Keyword search returns matching stories
  - Action: Type a keyword taken from an existing default story's title (e.g., a word in a festival story name) into the search field and submit.
  - Expected: Results list includes that story; clicking the result opens its detail page.
  - Verified: Searching "Carnival" narrowed the Explore Stories grid to exactly "The Carnival of Masks"; clicking the result opened `/story/carnival-of-masks` with matching h1.

- [X] FT-04: Topic filter shows only that topic's stories
  - Action: Select the topic filter "food" (then repeat with "history" and "neighborhoods").
  - Expected: Only stories tagged with the selected topic remain listed; stories from other topics disappear.
  - Verified: "Food & Drink" → 4 cards, all Food-tagged (Street Food Odyssey, Wine Harvest, Midnight Bakeries, Jewish Quarter); "History" → 4 cards, all History-tagged; "Neighborhoods" → 3 cards, all Neighborhoods-tagged. Stories from other topics disappeared in each case.

- [X] FT-05: Visitor can save a story to favorites
  - Action: Open a default story's detail page and click the "Favorite"/"Save" control (heart/star button).
  - Expected: The control registers the save (state changes, see IX-04) and the story appears in the favorites list.
  - Verified: Clicking "Save for later" on The Carnival of Masks changed the button to "Saved", nav badge to "1", and the story appeared in `/favorites` ("1 story saved for your trip").

- [X] FT-06: Favorites list is revisitable during the trip
  - Action: After saving 2 stories, navigate to the favorites page/section, then reload the browser and return to favorites.
  - Expected: Both saved stories are still listed in favorites and each opens its correct detail page.
  - Verified: Roman Baths + Carnival saved; after full browser reload, `/favorites` still listed "2 stories saved for your trip" with both cards; clicking each opened `/story/ancient-roman-baths` and `/story/carnival-of-masks` respectively (h1s matched).

## Constraint
- [X] CS-01: A story cannot be favorited twice
  - Action: Open one story, click Favorite, click Favorite again, then click Favorite a third time; finally open the favorites list.
  - Expected: The control toggles on/off/on; the favorites list contains exactly one entry for that story (no duplicates, and none after the second click removed it).
  - Verified: 1st click → "Saved", badge "1"; 2nd click → "Save for later", badge removed (0 entries); 3rd click → "Saved", badge "1". Favorites page showed exactly one card for The Carnival of Masks, header count "1 story".

- [X] CS-02: Search with no matches shows an explicit empty result state
  - Action: Search for a nonsense keyword, e.g., "zzzqqq123".
  - Expected: A clear "no stories found" (or equivalent) message is shown; the page does not crash, show a blank list, or display unrelated stories.
  - Verified: Filtered grid showed the message "No stories match your filters" with a "Clear filters" affordance; the grid contained zero story cards; page did not crash.

- [X] CS-03: Filter and search cannot produce contradictory results
  - Action: With topic filter "history" active, search a keyword that only exists in a "food" story; then search a keyword that exists in a "history" story.
  - Expected: The first combination yields no results (or an empty-state message); the second yields only the matching history story. Results never include stories outside the active filter.
  - Verified: History filter + "gelato" (Street Food Odyssey only) → empty state, 0 cards. History filter + "Carnival" → only "The Carnival of Masks" (🏛️ History, 🎭 Festivals). No result ever fell outside the active filter.

- [X] CS-04: Empty favorites list renders a defined empty state
  - Action: On a fresh session (no favorites saved), open the favorites page/section.
  - Expected: An empty-state message such as "No saved stories yet" is displayed instead of a broken or blank list.
  - Verified: On a fresh session, `/favorites` rendered heading "No favorites yet" with paragraph "Start exploring and save stories you want to revisit during your trip..." and a "Start exploring" link; header showed "0 stories saved for your trip".

## Interaction
- [X] IX-01: Timeline expands and collapses on click
  - Action: On a story detail page with a timeline, click a timeline entry/section header to expand it, then click again to collapse.
  - Expected: Expanded content reveals the detailed event text; collapsing hides it again; both toggles respond immediately to clicks.
  - Verified: Roman Baths timeline's section control "Show 2 more" immediately revealed 2 additional events with their detailed text (3→5 entries), and clicking it again ("Show less") immediately hid them (5→3). Note: expansion works via the timeline's Show more/Show less control; individual entries are not themselves click-toggle targets, but the expand→reveal→collapse→hide behavior responded instantly.

- [X] IX-02: Image gallery opens and navigates between images
  - Action: Click a gallery thumbnail on a story detail page; use next/previous controls (or arrow behavior) to move through the images; then close the gallery.
  - Expected: The selected image opens in the gallery view, navigation steps through each image in order, and closing returns to the story page.
  - Verified: Clicking "Image 1" opened a full-screen lightbox showing Image 1; Next advanced 1→2 (and 3→1 wraparound verified); Prev went 1→3; the ✕ button closed the overlay and returned to the story page.

- [X] IX-03: Embedded audio/video clip plays
  - Action: On a story detail page, press play on an embedded audio or video clip.
  - Expected: Playback starts (progress/playing state advances or audible sound), and pause stops it. The media element is not a dead/broken player.
  - Verified: On The Carnival of Masks, clicking play in "Watch the Story" mounted a YouTube embed with autoplay; the player's video element reported `paused: false` with `currentTime` advancing 25.03s → 27.55s over 2.5s, and clicking stopped it (`paused: true`). The Artisan Quarter additionally has a native `<audio controls>` element. (Content-relevance of the clip is reported separately under CT-03.)

- [X] IX-04: Favorite action gives immediate visual feedback
  - Action: Click the Favorite control on a story detail page and observe the button and any confirmation message.
  - Expected: The button visibly changes state (e.g., filled heart/star vs. outline) at the moment of the click, and any success toast/label appears without a page reload.
  - Verified: Button label/icon flipped "Save for later" ↔ "Saved" instantly on each click, and the nav "Favorites" badge updated 0→1→0→1 in the same client session (URL unchanged, no page reload).

## Content
- [X] CT-01: Default stories cover all four cultural themes
  - Action: Browse the collections and inspect story titles/tags on the home page.
  - Expected: Stories exist for each required theme: history, festivals, traditional food, and hidden attractions (all four represented, none replaced by unrelated topics).
  - Verified: History (Ancient Roman Baths, Carnival of Masks, Bell Tower Keepers, Jewish Quarter); Festivals (Carnival of Masks, Wine Harvest Festival); Traditional food (A Street Food Odyssey, The Midnight Bakeries, Jewish Quarter); Hidden attractions via 💎 Hidden Gems (Roman Baths, Artisan Quarter, Midnight Bakeries, Bell Tower Keepers). "Neighborhoods" is an additional, on-theme topic, not a replacement.

- [X] CT-02: Story detail pages contain complete, consistent content
  - Action: Open three different default story detail pages and compare against their cards.
  - Expected: Each detail page shows the story's title, descriptive body text, its topic tag(s), and at least one interactive element (timeline, gallery, or media clip); titles match the cards exactly.
  - Verified: Roman Baths (h1 = card title, 4 body paragraphs, tags 🏛️/💎, Timeline + Gallery), Carnival of Masks (h1 match, body, tags 🏛️/🎭, video + Gallery), Street Food Odyssey (h1 match, body, tags 🍝/🏘️, 3-image Gallery) — and the remaining 5 stories were also scanned with matching titles, 15–19 article paragraphs, header tags, and ≥1 interactive section each.

- [ ] CT-03: All images and media are relevant and load correctly
  - Action: Inspect images in collections, galleries, and story pages across the site.
  - Expected: Every image renders (no broken-image icons or empty placeholders) and depicts content relevant to the city's culture theme (e.g., food photos on food stories, not generic stock unrelated to the story).
  - Bug Report:
    - Issue: Broken images and off-topic embedded media
    - Actual: Two Unsplash URLs fail to load (`complete && naturalWidth === 0`): `images.unsplash.com/photo-1564429238857-4b5912e6a71f` ("The Bell Tower Keepers" hero — broken on the homepage and on the Carnival of Masks related-stories card) and `images.unsplash.com/photo-1564429238984-df62e09c3de4` ("The Bell Tower Keepers - Image 1" gallery thumbnail on its own story page). Additionally, the "Watch the Story" video on The Carnival of Masks embeds YouTube ID `dQw4w9WgXcQ` (Rick Astley's "Never Gonna Give You Up" — a placeholder Rickroll), which is unrelated to the city's carnival/festival theme.

---

**Score: 16/17 PASS.** The app solidly implements collections, story details, search, topic filters, favorites (toggle, dedup, persistence via reload), timelines, gallery lightbox, and a working video player. The only failure is content/media quality (CT-03): two broken Unsplash images and a placeholder Rickroll video embedded as story media.