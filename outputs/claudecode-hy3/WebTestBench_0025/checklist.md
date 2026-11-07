# Test Checklist

## Functionality
- [ ] FT-01: Predefined categories are available for selection
  - Action: Open the webpage.
  - Expected: The category list shows exactly: "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming Topics".

- [ ] FT-02: User can select a category
  - Action: Click on a category (e.g., "Poetry").
  - Expected: The category becomes selected/active and is indicated as the current context.

- [ ] FT-03: Generate a random prompt for the selected category
  - Action: With a category selected, click the "Generate" button.
  - Expected: A prompt text relevant to the selected category is displayed.

- [ ] FT-04: Mark a prompt as a favorite
  - Action: With a generated prompt visible, click the "Favorite" button.
  - Expected: The prompt is stored in the favorites list and is retrievable as a favorite.

- [ ] FT-05: View history of prompts viewed in this visit
  - Action: Generate several prompts, then open the "History" section.
  - Expected: A list of all prompts viewed during this session is displayed.

- [ ] FT-06: Revisit a prompt from history
  - Action: Click a prompt entry in the History list.
  - Expected: The selected prompt is displayed again in the main prompt area.

- [ ] FT-07: Add a new category
  - Action: Click "Add Category", enter a name, and save.
  - Expected: The new category appears in the category list and is selectable.

- [ ] FT-08: Modify an existing category
  - Action: Select a category, click "Edit", change its name, and save.
  - Expected: The category list shows the updated name and the change persists.

- [ ] FT-09: Delete a category
  - Action: Select a category and click "Delete", then confirm.
  - Expected: The category is removed from the category list.

## Constraint
- [ ] CS-01: Generating a prompt requires a selected category
  - Action: Without selecting any category, click "Generate".
  - Expected: No prompt is generated; the system prevents generation (button disabled or an error/guidance message shown).

- [ ] CS-02: Category name cannot be empty when adding/editing
  - Action: Click "Add Category" (or "Edit"), leave the name blank, and save.
  - Expected: The save is rejected with a message indicating a name is required; no blank category is created.

- [ ] CS-03: Deleting the currently selected category is handled safely
  - Action: Select a category, delete it, then attempt to generate.
  - Expected: After deletion, no category is selected and generation is blocked until a new category is chosen (no crash/error state).

## Interaction
- [ ] IX-01: Each generate click produces a new prompt
  - Action: Click "Generate" multiple times for the same category.
  - Expected: A visibly different prompt appears on each click (or a clear "new prompt generated" indicator shows).

- [ ] IX-02: Favoriting gives clear visual feedback
  - Action: Click "Favorite" on a prompt.
  - Expected: A visual indicator (e.g., filled star/heart) appears, confirming favorite status.

- [ ] IX-03: Switching category updates prompt context
  - Action: Select "Poetry", generate; then select "Short Stories".
  - Expected: The prompt area reflects the newly selected category context for the next generation.

## Content
- [ ] CT-01: Generated prompts match the selected category theme
  - Action: Select each category and generate prompts.
  - Expected: Every generated prompt is clearly relevant to and consistent with its category's theme.

- [ ] CT-02: History entries show correct category association
  - Action: Generate prompts across different categories and view History.
  - Expected: Each history entry displays the prompt text alongside the correct category label it was generated from.