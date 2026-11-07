# Test Checklist

## Functionality
- [ ] FT-01: The five predefined categories are available on load
  - Action: Load the page and read the category selector/list.
  - Expected: Exactly the categories "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming Topics" are listed and clickable.

- [ ] FT-02: A category can be selected as the active category
  - Action: Click the "Poetry" category.
  - Expected: "Poetry" becomes the active/selected category and the prompt area is scoped to it (Generate action targets Poetry).

- [ ] FT-03: A random prompt can be generated for the selected category
  - Action: With "Short Stories" selected, click the "Generate" (or "Generate Prompt") button.
  - Expected: A single non-empty prompt text appears in the prompt display area within the page (no navigation away).

- [ ] FT-04: Repeated generation returns a different prompt
  - Action: Click "Generate" 3 consecutive times in the same category.
  - Expected: At least 2 of the 3 displayed prompts are different from each other.

- [ ] FT-05: A displayed prompt can be marked as a favorite
  - Action: Generate a prompt, then click the "Favorite" (heart/star) control on it.
  - Expected: The prompt is added to the "Favorites" section and appears there with its full text.

- [ ] FT-06: A favorited prompt can be un-favorited
  - Action: In the "Favorites" section, click the favorite toggle on the prompt added in FT-05.
  - Expected: That prompt is removed from the "Favorites" section.

- [ ] FT-07: Every generated prompt is recorded in the visit history
  - Action: Generate 2 prompts in "Character Sketches", then open the "History" section.
  - Expected: Both generated prompts are listed in History with their text and their category name.

- [ ] FT-08: A history entry can be revisited
  - Action: Generate a new prompt, then click an older entry in the "History" list.
  - Expected: The prompt display area shows that older prompt's text again, and its category is re-selected/indicated.

- [ ] FT-09: A new custom category can be added and used
  - Action: Use the "Add Category" control, enter "Sci-Fi Worlds", save it, then select "Sci-Fi Worlds" and click "Generate".
  - Expected: "Sci-Fi Worlds" appears in the category list and a prompt is generated from it.

- [ ] FT-10: An existing category can be modified (renamed)
  - Action: Rename "Brainstorming Topics" to "Idea Sparks" and save.
  - Expected: The category list shows "Idea Sparks" and the old name no longer appears.

- [ ] FT-11: A category can be deleted
  - Action: Delete the category created in FT-09 and confirm the deletion.
  - Expected: The category is removed from the category list and can no longer be selected.

*(Note: FT-01 through FT-11 = 11 items. Total checklist is 20 items.)*

## Constraint
- [ ] CS-01: No prompt can be generated when no category is selected
  - Action: On a fresh load (no category selected), click "Generate".
  - Expected: No prompt is produced; the button is disabled or a prompt instructs the user to select a category first.

- [ ] CS-02: A category cannot be saved with an empty or whitespace-only name
  - Action: Open "Add Category", leave the name field empty, and save.
  - Expected: The category is not created and a validation message is shown.

- [ ] CS-03: Duplicate category names are rejected
  - Action: Add a new category named "Poetry" (already existing) and save.
  - Expected: The duplicate is not created and a "name already exists" message is shown.

- [ ] CS-04: Category deletion requires confirmation and can be cancelled
  - Action: Start deleting "Fantasy Landscapes", then choose "Cancel" in the confirmation.
  - Expected: "Fantasy Landscapes" remains in the category list and remains selectable.

- [ ] CS-05: History is scoped to the current visit only
  - Action: Generate 2 prompts, then reload the page in the same browser.
  - Expected: The "History" section is empty after reload (it does not show prompts from the previous visit).

## Interaction
- [ ] IX-01: The selected category is visually highlighted
  - Action: Click "Fantasy Landscapes", then click "Poetry".
  - Expected: Only "Poetry" shows the selected/active visual state; "Fantasy Landscapes" returns to the default state.

- [ ] IX-02: The favorite control reflects the prompt's favorite state
  - Action: Generate a prompt, note the favorite control, click it, then click it again.
  - Expected: The control visibly switches to a "favorited" state on the first click and back to the "not favorited" state on the second click.

- [ ] IX-03: History is ordered with the most recent prompt first
  - Action: Generate prompt A, then prompt B, then prompt C, and open "History".
  - Expected: The top entry of the History list is C, followed by B, then A.

- [ ] IX-04: Empty states are shown when Favorites and History have no entries
  - Action: On a fresh load with no prompts generated, open the "Favorites" section and the "History" section.
  - Expected: Each shows a clear empty-state message (e.g., "No favorites yet" / "No prompts viewed yet") rather than a blank panel.

## Content
- [ ] CT-01: Generated prompts match the selected category's theme
  - Action: Generate one prompt in each of "Poetry" and "Fantasy Landscapes".
  - Expected: The "Poetry" prompt is clearly poetry-related and the "Fantasy Landscapes" prompt is clearly about a fantastical place/setting; neither is generic or off-topic filler text.

- [ ] CT-02: Page content is relevant to a creative prompt generator
  - Action: Read the page title, main heading, section labels, and any icons/imagery.
  - Expected: All text and visuals relate to creative writing/prompt generation; no placeholder text (e.g., "Lorem ipsum"), no broken images, and no off-theme content.