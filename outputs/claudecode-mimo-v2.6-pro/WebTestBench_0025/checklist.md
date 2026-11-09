# Test Checklist

## Functionality
- [ ] FT-01: User can select a category and generate a prompt
  - Action: Click the "Short Stories" category, then click the "Generate Prompt" button
  - Expected: A non-empty prompt text is displayed in the prompt area
- [ ] FT-02: User can generate a prompt again after the first generation
  - Action: Click "Generate Prompt" a second time while a category is selected
  - Expected: A prompt is displayed again in the prompt area (regeneration succeeds)
- [ ] FT-03: User can mark a prompt as favorite
  - Action: Generate a prompt, then click its "Favorite" (star) control
  - Expected: The prompt appears in the Favorites list
- [ ] FT-04: User can unmark a favorited prompt
  - Action: Click the "Favorite" (star) control again on a prompt already in Favorites
  - Expected: The prompt is removed from the Favorites list
- [ ] FT-05: History lists prompts viewed during the current visit
  - Action: Generate prompts from two different categories, then open the History section
  - Expected: Both generated prompts are listed in the History section
- [ ] FT-06: User can revisit a prompt from history
  - Action: Click an entry in the History list
  - Expected: The full text of that exact prompt is displayed in the prompt area
- [ ] FT-07: User can add a new category
  - Action: Enter "Mystery Plots" in the add-category input and confirm (e.g., click "Add Category")
  - Expected: "Mystery Plots" appears in the category list and is selectable
- [ ] FT-08: User can modify an existing category
  - Action: Use the edit control on the "Poetry" category, rename it to "Poems & Verse", and save
  - Expected: The category list shows "Poems & Verse" instead of "Poetry"
- [ ] FT-09: User can delete a category
  - Action: Use the delete control on the "Brainstorming Topics" category and confirm
  - Expected: "Brainstorming Topics" is removed from the category list

## Constraint
- [ ] CS-01: Category cannot be created with an empty name
  - Action: Clear the add-category input and click "Add Category"
  - Expected: No category is created; a validation message (e.g., "Category name is required") is shown
- [ ] CS-02: Category cannot be created with a duplicate name
  - Action: Enter "Poetry" (an existing default category) in the add-category input and click "Add Category"
  - Expected: No duplicate category is created; a validation message indicating the name already exists is shown
- [ ] CS-03: Prompt cannot be generated without a selected category
  - Action: On fresh load (no category selected), click "Generate Prompt"
  - Expected: No prompt is generated; a message asking to select a category is shown
- [ ] CS-04: A prompt cannot be duplicated in the Favorites list
  - Action: Click the "Favorite" control on a prompt twice in quick succession (mark, then unmark, then mark again)
  - Expected: The Favorites list contains that prompt exactly once (never two identical entries)

## Interaction
- [ ] IX-01: Category selection shows an active state
  - Action: Click the "Poetry" category
  - Expected: "Poetry" is visually highlighted/marked as the active category
- [ ] IX-02: Favorite control reflects its state visually
  - Action: Toggle the "Favorite" (star) control on and off
  - Expected: The control shows an "on" state (e.g., filled star) when favorited and an "off" state (e.g., empty star) when not
- [ ] IX-03: Feedback is shown after category add, modify, and delete
  - Action: Add a new category, rename it, then delete it
  - Expected: After each action, a confirmation message (e.g., "Category added", "Category updated", "Category deleted") is displayed

## Content
- [ ] CT-01: All predefined categories are present with correct names
  - Action: Load the page and inspect the category list
  - Expected: The list contains exactly "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming Topics"
- [ ] CT-02: Generated prompts are relevant to the selected category
  - Action: Select "Fantasy Landscapes" and generate a prompt; repeat with "Poetry"
  - Expected: Each generated prompt's text clearly relates to its selected category (e.g., the Fantasy Landscapes prompt describes a fantasy setting)
- [ ] CT-03: History entries show the full text of previously viewed prompts
  - Action: Generate a prompt, note its text, then open the History list
  - Expected: The History entry displays the same full prompt text that was shown in the prompt area