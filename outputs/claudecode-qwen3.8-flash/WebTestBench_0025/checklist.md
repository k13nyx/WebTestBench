# Test Checklist

## Functionality
- [ ] FT-01: All five predefined categories are available
  - Action: Load the page and inspect the category selector (tabs/list/dropdown).
  - Expected: "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming Topics" are all present and individually selectable.

- [ ] FT-02: User can select a category as active
  - Action: Click the "Poetry" category.
  - Expected: Poetry is registered as the active category and stays active until another category is chosen.

- [ ] FT-03: Generating produces a prompt for the active category
  - Action: With "Fantasy Landscapes" selected, click the "Generate Prompt" button.
  - Expected: One readable prompt is displayed in the prompt output area.

- [ ] FT-04: Generation is random across repeated clicks
  - Action: Keep the same category selected and click "Generate Prompt" 5 times.
  - Expected: At least two different prompt texts appear (not identical every time).

- [ ] FT-05: User can favorite a generated prompt
  - Action: Generate a prompt, click the "Favorite" control, then open the Favorites view.
  - Expected: The prompt appears in Favorites exactly once, with its text and its category label.

- [ ] FT-06: History lists prompts viewed during this visit
  - Action: Generate 3 prompts, switching categories at least once, then open History.
  - Expected: All 3 prompts are listed in the order they were viewed, each labeled with its category.

- [ ] FT-07: User can revisit a prompt from History
  - Action: Click an entry in the History list.
  - Expected: That prompt's full text is redisplayed in the prompt output area and its category is shown/selected.

- [ ] FT-08: User can add a new custom category
  - Action: Open category customization, add a category named "Sci-Fi Hooks", and save.
  - Expected: "Sci-Fi Hooks" appears in the category selector and can be selected as active.

- [ ] FT-09: Custom categories support generation
  - Action: Select "Sci-Fi Hooks", click "Generate Prompt".
  - Expected: A non-empty prompt is generated and displayed for the custom category.

- [ ] FT-10: User can modify an existing category
  - Action: Use edit/rename on "Poetry" to change it to "Poetry & Verses", then save.
  - Expected: The new name appears in the selector; the old name is gone; selecting it still generates a prompt.

- [ ] FT-11: User can delete a category
  - Action: Delete "Brainstorming Topics" from the category customization controls.
  - Expected: "Brainstorming Topics" no longer appears anywhere in the category selector.

## Constraint
- [ ] CS-01: Blank category names are rejected
  - Action: Open add-category, leave the name field empty, click Save/Add.
  - Expected: No category is created, a validation message is shown, and the category list is unchanged.

- [ ] CS-02: Duplicate category names are rejected
  - Action: Attempt to add a second category named "Poetry" (which already exists).
  - Expected: The add is refused with a message such as "category already exists"; only one "Poetry" entry remains.

- [ ] CS-03: Deleting the active category leaves a valid state
  - Action: Select "Poetry", then delete "Poetry".
  - Expected: Another remaining category is automatically active, "Generate Prompt" still works, and the prompt area is not left blank/broken.

## Interaction
- [ ] IX-01: Active category is visually distinguished
  - Action: Click "Fantasy Landscapes" and compare it with the unselected categories.
  - Expected: The selected category shows a distinct visual state (highlight, filled background, or border) that other categories do not have.

- [ ] IX-02: Favorite control reflects and toggles its state
  - Action: Click "Favorite" on a displayed prompt, then click the same control again.
  - Expected: The control visibly switches to an active/filled state, then back to inactive, and the entry is removed from Favorites.

- [ ] IX-03: Confirmation feedback on favorite actions
  - Action: Favorite a prompt, then un-favorite it, watching the interface.
  - Expected: A toast or inline message confirms each action (e.g. "Added to favorites" / "Removed from favorites").

- [ ] IX-04: History updates automatically after each generation
  - Action: With the History panel open, click "Generate Prompt" twice.
  - Expected: A new history entry appears after each click without any manual refresh or navigation.

## Content
- [ ] CT-01: Prompts match the theme of their category
  - Action: Generate 3 prompts each for "Fantasy Landscapes" and for "Brainstorming Topics".
  - Expected: Fantasy prompts describe settings/places/worlds; brainstorming prompts pose topics or ideas; no prompt is mismatched to its selected category.

- [ ] CT-02: Prompt and category content is real, non-placeholder text
  - Action: Generate a prompt for each of the 5 predefined categories and inspect Favorites/History entries.
  - Expected: Every displayed prompt is complete readable text; no "lorem ipsum", "TODO", "sample", empty strings, or unresolved template tokens such as `{subject}` appear.