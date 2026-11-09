# Test Result

## Functionality

- [X] FT-01: User can choose a prompt category
  - Action: Click a predefined category in the category list (e.g., "Poetry").
  - Expected: "Poetry" becomes the active category, and the app indicates it as the current selection.

- [X] FT-02: User can generate a random prompt for the chosen category
  - Action: With a category active, click the "Generate" button.
  - Expected: A random creative prompt is displayed in the main prompt display area.

- [X] FT-03: Repeated generation produces varied prompts
  - Action: Keep the same category selected and click "Generate" 5 times.
  - Expected: At least 2 distinct prompt texts are shown across the 5 generations (output is randomized, not one fixed prompt).

- [X] FT-04: User can mark a prompt as favorite and see it in favorites
  - Action: Generate a prompt, click its favorite control (e.g., star / "Add to Favorites"), then open the favorites list.
  - Expected: The marked prompt appears in the favorites list with its full text.

- [X] FT-05: Viewed prompts are recorded in the history list
  - Action: Generate 3 prompts (same or different categories), then inspect the history section.
  - Expected: All 3 prompts appear in the history list, one entry per viewed prompt, with text matching what was displayed.

- [X] FT-06: User can revisit a prompt from the history
  - Action: Click any entry in the history list.
  - Expected: The selected prompt is re-displayed in the prompt display area with its full original text.

- [X] FT-07: User can add a new category
  - Action: Use the add-category control, enter a unique name (e.g., "Sci-Fi Ideas"), and confirm/save.
  - Expected: "Sci-Fi Ideas" appears in the category list and can be selected.

- [ ] FT-08: User can modify a category
  - Action: Edit the "Sci-Fi Ideas" category, change its name to "Space Opera", and save.
  - Expected: The category list shows "Space Opera"; the old name "Sci-Fi Ideas" no longer appears.
  - Bug Report:
    - Issue: Element Occlusion
    - Actual: The edit (pencil) control on the category card cannot be clicked. A decorative gradient overlay div (`absolute top-0 right-0 w-16 h-16 ... bg-gradient-to-bl from-primary/30 to-transparent rounded-tr-xl`, `pointer-events: auto`) is rendered on top of the edit/delete buttons in the card's top-right corner; Playwright's click on the edit button times out with "\<div ... opacity-40>\</div> intercepts pointer events", and `document.elementFromPoint()` at the button's center returns the overlay on every category card. The edit dialog never opens, so the name cannot be changed to "Space Opera" — the category remains "Sci-Fi Ideas".

- [ ] FT-09: User can delete a category
  - Action: Delete the "Space Opera" category via its delete control and confirm.
  - Expected: "Space Opera" is removed from the category list and can no longer be selected.
  - Bug Report:
    - Issue: Element Occlusion / Unresponsive Button
    - Actual: The delete (trash) control on category cards cannot be clicked — it is fully covered by the same `pointer-events: auto` gradient overlay (click attempt times out with "intercepts pointer events"); no delete confirmation ever appears and no category can be deleted, so the list never changes. (Additionally, "Space Opera" could never be created in the first place because the rename in FT-08 is blocked by the same occlusion bug.)

## Constraint

- [X] CS-01: Prompt generation requires an active category
  - Action: On a fresh page load with no category chosen, attempt to click "Generate".
  - Expected: No prompt is displayed — the button is disabled or a message asks the user to choose a category first.

- [X] CS-02: Category cannot be added with an empty name
  - Action: Open the add-category control, leave the name empty (or whitespace only), and confirm.
  - Expected: The category is not added; a validation message is shown and the category list is unchanged.

- [ ] CS-03: Category names must be unique
  - Action: Attempt to add a category named exactly like an existing one (e.g., "Poetry").
  - Expected: The duplicate is not added; the list still contains only one "Poetry" entry.
  - Bug Report:
    - Issue: Missing duplicate-name validation
    - Actual: Adding a category named "Poetry" (exactly matching the existing one) succeeds: a toast notification "Category added" appears and a second "Poetry" card (empty description) is appended to the category list. After the attempt the list contains two "Poetry" entries instead of only one.

- [ ] CS-04: Category cannot be renamed to an empty or duplicate name
  - Action: Edit a category and try saving with an empty name, then with an existing category's name (e.g., "Poetry").
  - Expected: Both saves are rejected with a message; the category keeps its original name.
  - Bug Report:
    - Issue: Element Occlusion (feature unreachable)
    - Actual: The rename form can never be reached — the edit control on every category card is occluded by a `pointer-events: auto` gradient overlay (click times out with "intercepts pointer events"), so neither the empty-name nor the duplicate-name ("Poetry") rename attempt could be performed. The rename validation is unverifiable/unreachable for any user. (Corroborating: the app performs no uniqueness check when adding categories either, see CS-03.)

- [X] CS-05: History is limited to the current visit
  - Action: Generate prompts to populate the history, then reload the page.
  - Expected: The history list is empty after reload — viewed-prompt entries do not carry over between visits.

## Interaction

- [X] IX-01: Category selection is visually indicated
  - Action: Click "Poetry", then click "Fantasy Landscapes".
  - Expected: The clicked category shows a selected style (e.g., highlight/border) that moves to the newly clicked category; the previous selection loses it.

- [X] IX-02: Favorite toggle gives immediate visual feedback
  - Action: With a prompt shown, click its favorite toggle twice (mark, then unmark).
  - Expected: The favorite icon/state visibly switches on each click (e.g., filled ↔ outline star), and the prompt is added to / removed from the favorites list accordingly.

- [ ] IX-03: Deleting a category updates the list immediately
  - Action: Delete a category and observe the category list.
  - Expected: The category disappears from the list in place without a full page reload; the remaining categories stay visible and selectable.
  - Bug Report:
    - Issue: Element Occlusion / Unresponsive Button
    - Actual: No category can be deleted at all — the delete control on each card is covered by a `pointer-events: auto` decorative gradient overlay, so pointer clicks never reach it (Playwright click times out with "intercepts pointer events"). No delete confirmation appears and the category list never updates in response to delete attempts (the remaining categories do remain visible/selectable).

## Content

- [ ] CT-01: All five predefined categories are present on load
  - Action: Inspect the category list on first page load.
  - Expected: The list includes "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming Topics".
  - Bug Report:
    - Issue: Wrong text (naming deviation)
    - Actual: The category list on first load contains "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming" — the fifth category is named "Brainstorming" (💡, description "Unlock creative ideas and fresh perspectives"), not "Brainstorming Topics" as expected.

- [X] CT-02: Generated prompts match the selected category's theme
  - Action: Generate prompts under at least two categories (e.g., "Poetry" and "Fantasy Landscapes") and read them.
  - Expected: Each prompt clearly belongs to its category (e.g., a Poetry prompt is about writing a poem; a Fantasy Landscapes prompt describes an imaginative place).

- [X] CT-03: Prompt text is a coherent creative prompt, not a placeholder
  - Action: Generate several prompts across different categories and inspect the text closely.
  - Expected: Every prompt is a complete, readable creative-writing prompt — no empty output, lorem ipsum, "undefined", or broken template fragments.
