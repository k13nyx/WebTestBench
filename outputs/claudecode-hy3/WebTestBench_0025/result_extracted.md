# Test Result

## Functionality

- [ ] FT-01: Predefined categories are available for selection
  - Action: Open the webpage.
  - Expected: The category list shows exactly: "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming Topics".
  - Bug Report:
    - Issue: Incorrect/Incomplete Category Name
    - Actual: The category list shows "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming" — the fifth category is labeled "Brainstorming" instead of the expected "Brainstorming Topics".

- [X] FT-02: User can select a category
  - Action: Click on a category (e.g., "Poetry").
  - Expected: The category becomes selected/active and is indicated as the current context.
  - (Verified: Poetry button became `[active]` and the prompt area context chip updated to "Poetry".)

- [X] FT-03: Generate a random prompt for the selected category
  - Action: With a category selected, click the "Generate" button.
  - Expected: A prompt text relevant to the selected category is displayed.
  - (Verified: After selecting Poetry, a poetry-themed prompt was displayed; the generate control is labeled "Generate Another".)

- [X] FT-04: Mark a prompt as a favorite
  - Action: With a generated prompt visible, click the "Favorite" button.
  - Expected: The prompt is stored in the favorites list and is retrievable as a favorite.
  - (Verified: Favorites count became "1", button changed to "Favorited" [active], and the prompt appeared in the Favorites list with its category label.)

- [X] FT-05: View history of prompts viewed in this visit
  - Action: Generate several prompts, then open the "History" section.
  - Expected: A list of all prompts viewed during this session is displayed.
  - (Verified: History section listed all generated prompts, count incremented to "10".)

- [X] FT-06: Revisit a prompt from history
  - Action: Click a prompt entry in the History list.
  - Expected: The selected prompt is displayed again in the main prompt area.
  - (Verified: Clicking the "Describe the color blue..." history entry reloaded that exact prompt into the main prompt area.)

- [X] FT-07: Add a new category
  - Action: Click "Add Category", enter a name, and save.
  - Expected: The new category appears in the category list and is selectable.
  - (Verified: Added "My Test Category"; it appeared in the list with its description and a "Category added" notification was shown.)

- [ ] FT-08: Modify an existing category
  - Action: Select a category, click "Edit", change its name, and save.
  - Expected: The category list shows the updated name and the change persists.
  - Bug Report:
    - Issue: Element Occlusion (control unreachable by user)
    - Actual: The Edit control is a `<div role="button">` at the card's top-right, but a decorative gradient overlay (`div.absolute.top-0.right-0.w-16.h-16.bg-gradient-to-bl.from-primary/30...`) sits on top and intercepts pointer events. `document.elementFromPoint` at the control's coordinates returns the overlay, not the control, so a real click never reaches it (Playwright real-click timed out due to interception). The edit handler itself exists (a forced DOM dispatch opened the "Edit Category" dialog), but it cannot be triggered through normal user interaction.

- [ ] FT-09: Delete a category
  - Action: Select a category and click "Delete", then confirm.
  - Expected: The category is removed from the category list.
  - Bug Report:
    - Issue: Element Occlusion (control unreachable by user)
    - Actual: Same gradient-overlay occlusion as FT-08 covers the Delete control (`<div role="button">` at the card's top-right). Normal pointer clicks are intercepted by the overlay (`document.elementFromPoint` returns the overlay), so the delete action cannot be invoked by a user. (A forced DOM dispatch was also unable to confirm removal through the intended flow, with the control remaining occluded.)

## Constraint

- [X] CS-01: Generating a prompt requires a selected category
  - Action: Without selecting any category, click "Generate".
  - Expected: No prompt is generated; the system prevents generation (button disabled or an error/guidance message shown).
  - (Verified: On initial load with no category selected, no Generate control is present; the prompt area shows guidance "Select a category above to begin your creative journey," so generation is prevented.)

- [X] CS-02: Category name cannot be empty when adding/editing
  - Action: Click "Add Category" (or "Edit"), leave the name blank, and save.
  - Expected: The save is rejected with a message indicating a name is required; no blank category is created.
  - (Verified: In the "Add New Category" dialog, the "Add Category" submit button is `[disabled]` while the Name field is empty, preventing submission; no blank category is created. Note: prevention is via a disabled submit button rather than an explicit text error message.)

- [ ] CS-03: Deleting the currently selected category is handled safely
  - Action: Select a category, delete it, then attempt to generate.
  - Expected: After deletion, no category is selected and generation is blocked until a new category is chosen (no crash/error state).
  - Bug Report:
    - Issue: Element Occlusion (delete control unreachable by user)
    - Actual: The Delete control is occluded by the same decorative gradient overlay described in FT-08/FT-09, so it cannot be clicked through normal interaction. Consequently the post-deletion safe-handling behavior (deselection + blocked generation) cannot be validated via the intended UI flow.

## Interaction

- [X] IX-01: Each generate click produces a new prompt
  - Action: Click "Generate" multiple times for the same category.
  - Expected: A visibly different prompt appears on each click (or a clear "new prompt generated" indicator shows).
  - (Verified: Consecutive clicks for Poetry produced "Describe grief as if it were a physical place..." then "Describe the color blue without using the word 'blue'...", clearly different prompts.)

- [X] IX-02: Favoriting gives clear visual feedback
  - Action: Click "Favorite" on a prompt.
  - Expected: A visual indicator (e.g., filled star/heart) appears, confirming favorite status.
  - (Verified: The button label changed to "Favorited" with `[active]` state, and the prompt appeared in the Favorites list with a heart/star icon indicator.)

- [X] IX-03: Switching category updates prompt context
  - Action: Select "Poetry", generate; then select "Short Stories".
  - Expected: The prompt area reflects the newly selected category context for the next generation.
  - (Verified: After switching to Short Stories, the context chip updated to "Short Stories" and a narrative-themed prompt was generated.)

## Content

- [X] CT-01: Generated prompts match the selected category theme
  - Action: Select each category and generate prompts.
  - Expected: Every generated prompt is clearly relevant to and consistent with its category's theme.
  - (Verified: Poetry → poetic lines; Short Stories → narrative starter; Character Sketches → character concept; Fantasy Landscapes → world/landscape description; Brainstorming → open question prompt. All consistent with their themes.)

- [X] CT-02: History entries show correct category association
  - Action: Generate prompts across different categories and view History.
  - Expected: Each history entry displays the prompt text alongside the correct category label it was generated from.
  - (Verified: History entries display the prompt text with the matching category label and icon, e.g., a Short Stories prompt labeled "Short Stories" (📖) and Poetry prompts labeled "Poetry" (🪶).)
