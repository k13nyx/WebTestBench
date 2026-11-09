# Test Result

## Functionality

- [X] FT-01: Browse curated story collections from the landing page
  - Action: Load the home page and view the curated collections section.
  - Expected: At least one curated collection is displayed, each showing a title and its list of story cards.

- [X] FT-02: Open a detailed page for a story
  - Action: Click any story card in a collection.
  - Expected: A detail page opens showing the story title, full body text, and its labeled topic(s).

- [X] FT-03: Search stories by keyword
  - Action: Enter a valid keyword (e.g., "festival") in the search field and submit.
  - Expected: Results list shows only stories matching the keyword.

- [X] FT-04: Filter stories by topic
  - Action: Select the "history" (then "food", then "neighborhoods") topic filter.
  - Expected: The story list updates to show only stories tagged with the selected topic.

- [X] FT-05: Save a story to favorites
  - Action: On a story detail page, click the "Save" / favorites control.
  - Expected: The story is added to the favorites list and the control shows a saved state.

- [X] FT-06: Revisit the favorites list
  - Action: Open the favorites list view after saving one or more stories.
  - Expected: All previously saved stories are listed and each opens its detail page when clicked.

- [ ] FT-07: Expand an expandable timeline
  - Action: On a story with a timeline, click a timeline entry.
  - Expected: The entry expands to reveal its full description.
  - Bug Report:
    - Issue: Non-interactive timeline entries (missing expandable behavior)
    - Actual: Timeline entries are static `<div>`s — they have no button role, no `cursor-pointer`, and no click handler. Full descriptions are always rendered (e.g., "19 BC Construction Begins — Emperor Augustus commissions the first public baths on this site"), so clicking an entry produces no state change. Only a section-level "Show 2 more"/"Show less" button toggles additional entries; individual entries cannot be expanded/collapsed. Reproduced on story `/story/ancient-roman-baths` and `/story/bell-tower-keepers`.

- [X] FT-08: Browse an image gallery
  - Action: On a story with a gallery, navigate through its images.
  - Expected: Each image loads fully and the current image is identifiable within the gallery.

- [X] FT-09: Play an embedded audio or video clip
  - Action: Click play on an embedded clip in a story.
  - Expected: The clip plays with audible sound / visible video and can be paused.

## Constraint

- [X] CS-01: Search with no matching keyword
  - Action: Enter a keyword that matches no story (e.g., "zzzz") and submit.
  - Expected: A "no results found" empty-state message is shown; no unrelated stories appear.

- [X] CS-02: Submit an empty search query
  - Action: Submit the search field with no text entered.
  - Expected: The app does not error; it shows the default/unfiltered story list or blocks the empty search.

- [X] CS-03: Apply a topic filter with no matching stories
  - Action: Apply a topic filter combined with a keyword that yields no matches.
  - Expected: A clear empty-state message is shown and no stories from other topics are displayed.

- [X] CS-04: Prevent duplicate favorites
  - Action: Save the same story twice.
  - Expected: The story appears only once in the favorites list; no duplicate entry is created.

- [X] CS-05: Favorites persist across navigation
  - Action: Save a story, navigate to another page, then return to the favorites list.
  - Expected: The saved story is still present in the favorites list.

## Interaction

- [ ] IX-01: Timeline expand/collapse toggle
  - Action: Click an expanded timeline entry a second time.
  - Expected: The entry collapses back to its collapsed state.
  - Bug Report:
    - Issue: Non-interactive timeline entries (no expand/collapse toggle)
    - Actual: Timeline entries are never expandable, so there is no "expanded" state to collapse. Clicking an entry (e.g., "19 BC Construction Begins", "64 AD Great Fire") triggers no DOM/state change; entries are static divs. Only the separate "Show more"/"Show less" button at the section level toggles the list length, not individual entries.

- [X] IX-02: Gallery navigation controls respond
  - Action: Use the next/previous controls (or thumbnails) in an image gallery.
  - Expected: The displayed image advances/retreats and the active indicator updates accordingly.

- [ ] IX-03: Save action provides feedback
  - Action: Click the "Save" control on a story.
  - Expected: The control visibly changes state (e.g., fills/changes icon) and a confirmation toast or message appears.
  - Bug Report:
    - Issue: Missing confirmation toast/message on save
    - Actual: The control changes state ("Save for later" → "Saved") and the favorites badge updates, but NO confirmation toast or message is displayed. A MutationObserver on the document body captured only the favorites-badge count nodes during save/remove; the Sonner toaster `<ol>` (located in `region[aria-label="Notifications (F8)"]`) remained empty and no toast element (`data-sonner-toast`) was ever added.

- [X] IX-04: Favorites count indicator updates
  - Action: Save and then remove a story from favorites.
  - Expected: The favorites count/badge increments on save and decrements on removal without a page reload.

## Content

- [X] CT-01: Stories align with the city-culture theme
  - Action: Review all stories across the collections.
  - Expected: Every story relates to city culture (history, festivals, traditional food, or hidden attractions); no off-topic content.

- [X] CT-02: Topic labels are accurate
  - Action: Check the topic tag(s) shown on each story against its content.
  - Expected: Each story is tagged with at least one correct topic ("history," "food," or "neighborhoods") that matches its content.

- [ ] CT-03: Images and media are relevant
  - Action: Review images, galleries, and embedded clips for each story.
  - Expected: All displayed media is directly relevant to that story's subject and loads without broken placeholders.
  - Bug Report:
    - Issue: Broken image placeholders (media fails to load)
    - Actual: For the story "The Bell Tower Keepers" (`/story/bell-tower-keepers`), the cover image and the first gallery image do not load:
      - Cover: `https://images.unsplash.com/photo-1564429238857-4b5912e6a71f?w=1200` → `naturalWidth = 0`, and an independent `new Image()` load returns `onerror`.
      - Gallery "Image 1": `https://images.unsplash.com/photo-1564429238984-df62e09c3de4?w=800` → `naturalWidth = 0` (independent load errors).
      Both render as broken placeholders while other images on the same page (e.g., gallery Image 2) load normally (naturalWidth = 800/1200). Additionally, the "Watch the Story" clip on `/story/carnival-of-masks` is an unrelated generic YouTube embed (`https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1`), which does not correspond to the story's subject.
