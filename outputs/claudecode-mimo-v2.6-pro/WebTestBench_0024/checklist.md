# Test Checklist

## Functionality
- [ ] FT-01: Curated collections are visible and browsable on the main page.
  - Action: Open the website's home page and view the collections section.
  - Expected: Multiple curated collections are displayed and each collection can be opened to list its stories.

- [ ] FT-02: A story's detailed page opens from its collection.
  - Action: Click a story card (e.g., the first story in the "History" collection).
  - Expected: The browser navigates to that story's detail page showing its title, text, and media.

- [ ] FT-03: Keyword search returns matching stories.
  - Action: Type "market" into the search bar and submit.
  - Expected: Only stories containing "market" in title or content are listed; each listed story opens correctly.

- [ ] FT-04: Topic filters restrict results to the selected topic.
  - Action: Apply the "history" filter, then "food", then "neighborhoods", one at a time.
  - Expected: Each filter shows only stories of that topic; switching filters updates the result list accordingly.

- [ ] FT-05: Expandable timeline expands and collapses.
  - Action: On a story detail page containing a timeline, click its first collapsed entry.
  - Expected: The entry expands to reveal its content; clicking it again collapses it.

- [ ] FT-06: Image gallery navigates between images.
  - Action: On a story page with an image gallery, click the "Next" and "Previous" controls.
  - Expected: The displayed image changes with each click; "Previous"/"Next" is disabled at the first/last image.

- [ ] FT-07: Embedded audio or video clip plays.
  - Action: Click the play control of an embedded audio/video clip on a story page.
  - Expected: The clip starts playing with audible sound (or moving video) and can be paused.

- [ ] FT-08: A story can be saved to the favorites list.
  - Action: Click the "Save"/favorite button on a story detail page.
  - Expected: The story appears in the favorites list page.

- [ ] FT-09: Favorites list can be revisited during the trip.
  - Action: After saving a story, navigate to other pages, then open the favorites list page again (also after a page reload).
  - Expected: The previously saved story is still listed and its detail page opens from the list.

- [ ] FT-10: A story can be removed from the favorites list.
  - Action: Click the remove/unsave control for a saved story on the favorites list page.
  - Expected: The story disappears from the favorites list immediately and is not listed after reload.

## Constraint
- [ ] CS-01: A search with no matches must not show unrelated stories.
  - Action: Search for a non-existent keyword such as "zzqxwv9999".
  - Expected: A "no results" message is shown and zero story cards are displayed.

- [ ] CS-02: A story must not appear under a topic it is not tagged with.
  - Action: Open the "food" filter results and inspect every listed story's topic label.
  - Expected: No story labeled "history" or "neighborhoods" appears in the "food" results.

- [ ] CS-03: Saving the same story twice must not create a duplicate favorites entry.
  - Action: Click the "Save" button on the same story twice (save, unsave is not required — click save on an already-saved story).
  - Expected: The favorites list contains exactly one entry for that story.

- [ ] CS-04: Search and filter combined must both be satisfied.
  - Action: Apply the "history" filter, then search the keyword "food" (or another term present only in non-history stories).
  - Expected: The result list contains only stories that are both tagged "history" and matching the keyword; empty results otherwise.

## Interaction
- [ ] IX-01: The save button shows a clear saved/unsaved state change.
  - Action: Click the "Save" button on a story page, then click it again to unsave.
  - Expected: The button's appearance changes on each click (e.g., outline ↔ filled bookmark) reflecting the current saved state.

- [ ] IX-02: Story cards give hover feedback.
  - Action: Hover the mouse cursor over a story card in a collection list.
  - Expected: The card shows a visible hover effect (highlight, shadow, or link styling) and the cursor changes to a pointer.

- [ ] IX-03: The active topic filter shows a selected state.
  - Action: Click the "history" filter chip/button.
  - Expected: The "history" filter is visually marked as active (e.g., highlighted/different color) while other filters remain unmarked.

## Content
- [ ] CT-01: Collections cover the required cultural themes.
  - Action: View the collections section on the main page.
  - Expected: Collections covering history, festivals, traditional food, and hidden attractions are present, each with a relevant title and description.

- [ ] CT-02: Images and embedded media are relevant and fully functional.
  - Action: Open 2–3 story pages and view all their images and embedded clips.
  - Expected: No broken/placeholder images or unloaded media; every image/clip relates to the story's subject (city history, festival, food, or location).

- [ ] CT-03: Story content matches its topic label and is real content.
  - Action: Open one story per topic (history, food, neighborhoods) and read its body text.
  - Expected: The text clearly concerns that topic's subject, and contains no placeholder text (e.g., "Lorem ipsum") or empty sections.