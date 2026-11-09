# Test Checklist

## Functionality
- [ ] FT-01: Default categories are available on load
  - Action: Open the webpage and inspect the category list.
  - Expected: Exactly these five categories are shown: "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", "Brainstorming Topics".

- [ ] FT-02: Selecting a category enables prompt generation
  - Action: Click any category (e.g., "Poetry"), then click the "Generate" button.
  - Expected: A random prompt text is displayed for the selected category.

- [ ] FT-03: Generating again returns a different prompt
  - Action: Click "Generate" three more times while "Poetry" is selected.
  - Expected: Each click displays a new prompt; the text is not identical to the immediately previous prompt.

- [ ] FT-04: User can add a new category
  - Action: Use the add-category input, enter "Sci-Fi Worlds", and confirm.
  - Expected: "Sci-Fi Worlds" appears in the category list and is selectable.

- [ ] FT-05: User can modify an existing category
  - Action: Rename the "Poetry" category to "Modern Poetry" and save.
  - Expected: The list shows "Modern Poetry" and "Poetry" is no longer listed; previously generated prompts remain intact.

- [ ] FT-06: User can delete a category
  - Action: Delete the "Brainstorming Topics" category and confirm if prompted.
  - Expected: "Brainstorming Topics" is removed from the list and is no longer selectable.

- [ ] FT-07: User can mark a prompt as a favorite
  - Action: Generate a prompt and click the "Favorite" (star) control.
  - Expected: The prompt is saved and appears in the Favorites list.

- [ ] FT-08: Favorites list displays saved prompts
  - Action: Mark two different prompts as favorites, then open the Favorites section.
  - Expected: Both prompts are listed with their full text.

- [ ] FT-09: History records prompts viewed in this visit
  - Action: Generate and view three prompts in sequence, then open the History section.
  - Expected: All three prompts appear, most recent first, with the full prompt text.

- [ ] FT-10: User can revisit a prompt from history
  - Action: Click a prompt entry in History.
  - Expected: That prompt is displayed in the main prompt area.

## Constraint
- [ ] CS-01: Generation is blocked without a selected category
  - Action: On fresh load with no category selected, click "Generate".
  - Expected: No prompt is generated; an instruction such as "Select a category first" is shown.

- [ ] CS-02: Empty category name is rejected
  - Action: In the add-category input, submit with an empty or whitespace-only value.
  - Expected: No new category is added; a validation message is shown.

- [ ] CS-03: Duplicate category name is prevented
  - Action: Attempt to add a category named exactly "Poetry" (already existing).
  - Expected: The category is not added and a duplicate/exists message is shown.

- [ ] CS-04: Unfavoriting removes a prompt from Favorites
  - Action: Click the "Favorite" control again on a prompt already marked favorite.
  - Expected: The prompt is removed from the Favorites list.

- [ ] CS-05: History contains only the current visit's prompts
  - Action: Note the History entries, reload the page.
  - Expected: History is empty on the new visit (no prompts from the previous visit).

## Interaction
- [ ] IX-01: Active category is visually indicated
  - Action: Click a category and observe the list.
  - Expected: The selected category is visibly highlighted (e.g., background/border change).

- [ ] IX-02: Favorite toggle gives immediate visual feedback
  - Action: Click the star icon on the displayed prompt.
  - Expected: The star immediately switches between filled and unfilled to reflect the state.

- [ ] IX-03: Newly generated prompt replaces the previous one instantly
  - Action: Click "Generate" and observe the prompt area.
  - Expected: The prompt area updates immediately with the new prompt, without requiring a page reload.

- [ ] IX-04: New history entry appears at the top immediately
  - Action: Generate a new prompt while the History section is visible.
  - Expected: The new prompt is added to the top of History without a reload.

## Content
- [ ] CT-01: Prompts are relevant to the selected category
  - Action: Generate one prompt per default category and read each.
  - Expected: Each prompt's content matches its category theme (e.g., "Poetry" prompts reference verse/poetic form).

- [ ] CT-02: Generated prompts contain real content
  - Action: Generate five prompts and inspect the text.
  - Expected: All prompts are complete, readable sentences; no placeholders such as "lorem ipsum", "TODO", or empty strings.

- [ ] CT-03: Displayed text matches actual stored data
  - Action: Compare the main prompt area text with its entry in Favorites and History.
  - Expected: The text is character-for-character identical across all three views.