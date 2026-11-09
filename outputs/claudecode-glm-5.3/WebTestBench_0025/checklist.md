# Test Checklist

## Functionality

- [ ] FT-01: User can choose a prompt category
  - Action: Click a predefined category in the category list (e.g., "Poetry").
  - Expected: "Poetry" becomes the active category, and the app indicates it as the current selection.

- [ ] FT-02: User can generate a random prompt for the chosen category
  - Action: With a category active, click the "Generate" button.
  - Expected: A random creative prompt is displayed in the main prompt display area.

- [ ] FT-03: Repeated generation produces varied prompts
  - Action: Keep the same category selected and click "Generate" 5 times.
  - Expected: At least 2 distinct prompt texts are shown across the 5 generations (output is randomized, not one fixed prompt).

- [ ] FT-04: User can mark a prompt as favorite and see it in favorites
  - Action: Generate a prompt, click its favorite control (e.g., star / "Add to Favorites"), then open the favorites list.
  - Expected: The marked prompt appears in the favorites list with its full text.

- [ ] FT-05: Viewed prompts are recorded in the history list
  - Action: Generate 3 prompts (same or different categories), then inspect the history section.
  - Expected: All 3 prompts appear in the history list, one entry per viewed prompt, with text matching what was displayed.

- [ ] FT-06: User can revisit a prompt from the history
  - Action: Click any entry in the history list.
  - Expected: The selected prompt is re-displayed in the prompt display area with its full original text.

- [ ] FT-07: User can add a new category
  - Action: Use the add-category control, enter a unique name (e.g., "Sci-Fi Ideas"), and confirm/save.
  - Expected: "Sci-Fi Ideas" appears in the category list and can be selected.

- [ ] FT-08: User can modify a category
  - Action: Edit the "Sci-Fi Ideas" category, change its name to "Space Opera", and save.
  - Expected: The category list shows "Space Opera"; the old name "Sci-Fi Ideas" no longer appears.

- [ ] FT-09: User can delete a category
  - Action: Delete the "Space Opera" category via its delete control and confirm.
  - Expected: "Space Opera" is removed from the category list and can no longer be selected.

## Constraint

- [ ] CS-01: Prompt generation requires an active category
  - Action: On a fresh page load with no category chosen, attempt to click "Generate".
  - Expected: No prompt is displayed — the button is disabled or a message asks the user to choose a category first.

- [ ] CS-02: Category cannot be added with an empty name
  - Action: Open the add-category control, leave the name empty (or whitespace only), and confirm.
  - Expected: The category is not added; a validation message is shown and the category list is unchanged.

- [ ] CS-03: Category names must be unique
  - Action: Attempt to add a category named exactly like an existing one (e.g., "Poetry").
  - Expected: The duplicate is not added; the list still contains only one "Poetry" entry.

- [ ] CS-04: Category cannot be renamed to an empty or duplicate name
  - Action: Edit a category and try saving with an empty name, then with an existing category's name (e.g., "Poetry").
  - Expected: Both saves are rejected with a message; the category keeps its original name.

- [ ] CS-05: History is limited to the current visit
  - Action: Generate prompts to populate the history, then reload the page.
  - Expected: The history list is empty after reload — viewed-prompt entries do not carry over between visits.

## Interaction

- [ ] IX-01: Category selection is visually indicated
  - Action: Click "Poetry", then click "Fantasy Landscapes".
  - Expected: The clicked category shows a selected style (e.g., highlight/border) that moves to the newly clicked category; the previous selection loses it.

- [ ] IX-02: Favorite toggle gives immediate visual feedback
  - Action: With a prompt shown, click its favorite toggle twice (mark, then unmark).
  - Expected: The favorite icon/state visibly switches on each click (e.g., filled ↔ outline star), and the prompt is added to / removed from the favorites list accordingly.

- [ ] IX-03: Deleting a category updates the list immediately
  - Action: Delete a category and observe the category list.
  - Expected: The category disappears from the list in place without a full page reload; the remaining categories stay visible and selectable.

## Content

- [ ] CT-01: All five predefined categories are present on load
  - Action: Inspect the category list on first page load.
  - Expected: The list includes "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming Topics".

- [ ] CT-02: Generated prompts match the selected category's theme
  - Action: Generate prompts under at least two categories (e.g., "Poetry" and "Fantasy Landscapes") and read them.
  - Expected: Each prompt clearly belongs to its category (e.g., a Poetry prompt is about writing a poem; a Fantasy Landscapes prompt describes an imaginative place).

- [ ] CT-03: Prompt text is a coherent creative prompt, not a placeholder
  - Action: Generate several prompts across different categories and inspect the text closely.
  - Expected: Every prompt is a complete, readable creative-writing prompt — no empty output, lorem ipsum, "undefined", or broken template fragments.