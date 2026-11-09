# Test Result

## Functionality
- [X] FT-01: Select a predefined category
  - Action: Click on the "Short stories" category option.
  - Expected: "Short stories" is selected and set as the active category.
- [X] FT-02: Generate a random prompt
  - Action: With an active category selected, click the "Generate Prompt" button.
  - Expected: A new prompt text appears in the main prompt display area.
- [X] FT-03: Mark a prompt as favorite
  - Action: Click the "Favorite" button on the currently displayed prompt.
  - Expected: The prompt is added to the "Favorites" list view.
- [X] FT-04: Remove a prompt from favorites
  - Action: Click the "Favorite" button again on a previously favorited prompt.
  - Expected: The prompt is removed from the "Favorites" list view.
- [X] FT-05: Record viewed prompt into visit history
  - Action: Generate three successive prompts using the "Generate Prompt" button.
  - Expected: All three prompts appear in the "History" panel in chronological order.
- [X] FT-06: Revisit a previous prompt from history
  - Action: Click on an earlier prompt entry in the "History" list.
  - Expected: The selected historical prompt is displayed again in the main prompt viewer.
- [X] FT-07: Add a new custom category
  - Action: Click "Add Category", enter "Sci-Fi" in the name field, and click "Save".
  - Expected: "Sci-Fi" appears in the category list and is immediately selectable.
- [X] FT-08: Modify an existing category
  - Action: Click "Edit" on an existing category, change the title to "Micro Fiction", and click "Save".
  - Expected: The category displays the updated name "Micro Fiction" in the category list.
- [X] FT-09: Delete a category
  - Action: Click the "Delete" button on a category and confirm the action.
  - Expected: The category is permanently removed from the category list.

## Constraint
- [ ] CS-01: Prevent adding a category with an empty name
  - Action: Click "Add Category", leave the input field blank, and click "Save".
  - Expected: Submission is blocked and an error message "Category name cannot be empty" is displayed.
  - Bug Report:
    - Issue: Missing Error Message
    - Actual: While submission is blocked by the submit button being disabled, no error message "Category name cannot be empty" is displayed.
- [ ] CS-02: Prevent creating duplicate category names
  - Action: Click "Add Category", enter "Poetry" (an existing category), and click "Save".
  - Expected: Submission is blocked and an error message "Category already exists" is displayed.
  - Bug Report:
    - Issue: Duplicate Category Allowed
    - Actual: Submission is not blocked when entering existing category name "Poetry"; a duplicate category is created and "Category added" toast is displayed without showing the error message "Category already exists".
- [ ] CS-03: Disallow prompt generation without an active category
  - Action: Attempt to click the "Generate Prompt" button when no category is selected.
  - Expected: The "Generate Prompt" button remains disabled or prompts "Please select a category first".
  - Bug Report:
    - Issue: Missing Element
    - Actual: When no category is selected, the "Generate Prompt" button is not rendered in the DOM; instead, only a static "Choose Your Muse" placeholder message is shown without an interactive or disabled button that prompts "Please select a category first".

## Interaction
- [X] IX-01: Toggle visual state on the favorite icon
  - Action: Click the favorite heart icon next to the active prompt.
  - Expected: The heart icon transitions from an unfilled outline to a filled active state immediately.
- [X] IX-02: Highlight active category selection
  - Action: Click on the "Character sketches" category card.
  - Expected: The selected card receives an active visual focus state (distinct background or border highlight).
- [X] IX-03: Category deletion confirmation modal
  - Action: Click the "Delete" icon on any category.
  - Expected: A confirmation dialog appears asking the user to confirm before deletion is processed.

## Content
- [ ] CT-01: Display all default predefined categories on initial load
  - Action: Open the webpage.
  - Expected: The category list displays exactly "Short stories", "Poetry", "Character sketches", "Fantasy landscapes", and "Brainstorming topics".
  - Bug Report:
    - Issue: Incorrect Category Name
    - Actual: The category list displays "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming" (the fifth category is named "Brainstorming" instead of "Brainstorming topics").
- [X] CT-02: Category-relevant prompt content display
  - Action: Select "Fantasy landscapes" and click "Generate Prompt".
  - Expected: The generated prompt text contains descriptive themes specific to world-building or fantasy landscapes.