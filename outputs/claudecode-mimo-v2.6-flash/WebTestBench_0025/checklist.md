# Test Checklist

## Functionality
- [ ] FT-01: Select a predefined category and generate a random prompt
  - Action: Click the "Short Stories" category, then click the generate button.
  - Expected: A random writing prompt is displayed on the page.
- [ ] FT-02: Generate prompts for all five predefined categories
  - Action: Sequentially select "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming Topics", generating one prompt each.
  - Expected: Each category produces a displayed prompt without errors.
- [ ] FT-03: Mark a prompt as favorite
  - Action: Generate a prompt, then click the favorite (star/heart) control.
  - Expected: The prompt is added to the favorites list and remains listed there.
- [ ] FT-04: Remove a prompt from favorites
  - Action: Click the favorite control on an already-favorited prompt.
  - Expected: The prompt is removed from the favorites list.
- [ ] FT-05: View history of prompts viewed in this visit
  - Action: Generate at least three different prompts, then open the history view.
  - Expected: History lists all three prompts most recently viewed, in order.
- [ ] FT-06: Revisit a prompt from history
  - Action: Click an entry in the history list.
  - Expected: That prompt is displayed again in the main prompt area.
- [ ] FT-07: Add a new category
  - Action: Use the category management control to add a category named "Sci-Fi Shorts".
  - Expected: "Sci-Fi Shorts" appears in the selectable category list and can be used to generate prompts.
- [ ] FT-08: Modify an existing category
  - Action: Edit a category's name (e.g., rename "Poetry" to "Poetry & Verse") via the category management control.
  - Expected: The updated name is shown in the category list and is selectable.
- [ ] FT-09: Delete a category
  - Action: Delete a custom category via the category management control.
  - Expected: The category disappears from the selectable category list.

## Constraint
- [ ] CS-01: Cannot add a category with an empty name
  - Action: Open the add-category form, leave the name field empty, and submit.
  - Expected: No new category is created; an error/validation message is shown.
- [ ] CS-02: Cannot add a duplicate category name
  - Action: Attempt to add a category with a name that already exists (e.g., "Poetry").
  - Expected: The duplicate is rejected with a validation message; the list still contains only one "Poetry".
- [ ] CS-03: Cannot generate a prompt without a selected category
  - Action: With no category selected, click the generate button.
  - Expected: No prompt is produced; a message prompts the user to select a category.
- [ ] CS-04: Deleting a category does not leave it selectable
  - Action: Delete a category, then inspect the category selection list.
  - Expected: The deleted category is absent and cannot be chosen.
- [ ] CS-05: History is limited to the current visit
  - Action: Generate prompts, reload the page, then open the history view.
  - Expected: The history is empty after reload (favorites behavior is not asserted here).

## Interaction
- [ ] IX-01: Selected category is visually indicated
  - Action: Click a category in the list.
  - Expected: The chosen category is visually highlighted as active; only one category appears active at a time.
- [ ] IX-02: Favorite control toggles visual state
  - Action: Click the favorite control once, then click it again.
  - Expected: The control shows an active/filled state after the first click and returns to the inactive state after the second.
- [ ] IX-03: History updates immediately after generating
  - Action: Generate a new prompt, then open the history view without reloading.
  - Expected: The new prompt appears at the top of history instantly.
- [ ] IX-04: Generating a new prompt replaces the previously displayed one
  - Action: Note the current prompt, then click the generate button again.
  - Expected: The main prompt area shows a new prompt, replacing the old one, without page navigation.

## Content
- [ ] CT-01: Prompts match the theme of their category
  - Action: Generate one prompt in each of the five predefined categories and read each.
  - Expected: Every prompt is relevant to its category (e.g., a "Poetry" prompt is a poetry-writing idea, a "Fantasy Landscapes" prompt describes a fantasy setting).
- [ ] CT-02: Predefined category names are displayed correctly
  - Action: Inspect the category list on page load.
  - Expected: The list contains exactly "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming Topics" with correct spelling.
- [ ] CT-03: History and favorites display complete prompt text
  - Action: Generate a long prompt, favorite it, then view the favorites list and history list.
  - Expected: Both lists show the full prompt text (or a clearly labeled truncation), with the category it belongs to identifiable.