# Test Result

## Functionality

- [X] FT-01: User can generate a random prompt from a selected category.
  - Action: Select "Short Stories" in the category selector, then click "Generate Prompt".
  - Expected: A prompt appears in the prompt display area, and it is a short-story prompt.
- [X] FT-02: Generating again replaces the displayed prompt with a new one from the same category.
  - Action: With "Poetry" selected, click "Generate Prompt" three times.
  - Expected: Each click shows a prompt, and the displayed prompt changes at least once across the three clicks.
- [X] FT-03: User can mark a prompt as a favorite.
  - Action: Generate a prompt, then click the favorite button (star icon).
  - Expected: The star becomes filled, and the prompt appears in the "Favorites" list.
- [X] FT-04: User can remove a prompt from favorites.
  - Action: Click the filled star on a favorited prompt.
  - Expected: The star becomes outlined, and the prompt is removed from the "Favorites" list.
- [X] FT-05: Viewed prompts are recorded in the history, newest first.
  - Action: Generate three different prompts, then check the "History" panel.
  - Expected: All three prompts are listed in the History panel, with the most recent at the top.
- [X] FT-06: Clicking a history entry redisplays that prompt.
  - Action: Generate a prompt, generate another, then click the first prompt in the "History" panel.
  - Expected: The prompt display area shows the first prompt's exact text.
- [ ] FT-07: User can add a new category.
  - Action: Click "Add Category", enter "Limericks", and click "Save".
  - Expected: "Limericks" appears in the category selector, and selecting it followed by "Generate Prompt" produces a prompt.
  - Bug Report:
    - Issue: Category Created But Generates No Prompt
    - Actual: "Limericks" was created and appears as a category card, but clicking it and then "Generate Another" left the display unchanged, still showing a prompt labeled "FANTASY LANDSCAPES". No Limericks prompt was produced. The form's submit button is labeled "Add Category", not "Save", and there is no "Generate Prompt" button.
- [X] FT-08: User can rename and delete a category.
  - Action: Select "Limericks", click "Edit", change the name to "Haiku", click "Save"; then click "Delete" on "Haiku" and confirm.
  - Expected: The selector shows "Haiku" after the rename, and "Haiku" is no longer in the selector after deletion.

## Constraint

- [ ] CS-01: Prompt generation is blocked when no category is selected.
  - Action: On a fresh page load with no category selected, click "Generate Prompt".
  - Expected: No prompt is displayed, and the message "Please select a category" appears (or the button is disabled).
  - Bug Report:
    - Issue: Missing Control / Expected Message Absent
    - Actual: On a fresh load there is no "Generate Prompt" button (no generate control exists in the DOM), and the text "Please select a category" does not appear. The page shows "Choose Your Muse" with no prompt. Generation only happens after a category card is clicked, so the blocked-state behavior the checklist describes is not present.
- [ ] CS-02: Category cannot be saved with an empty name.
  - Action: Click "Add Category", leave the name field blank, and click "Save".
  - Expected: The category is not created, and the message "Category name is required" appears.
  - Bug Report:
    - Issue: Missing Validation Message
    - Actual: With the name blank, the submit button "Add Category" is disabled, so no save occurs. The category was not created, but the text "Category name is required" does not appear anywhere on the page.
- [ ] CS-03: Duplicate category names are rejected.
  - Action: Click "Add Category", enter "poetry" (lowercase), and click "Save".
  - Expected: The category is not created, and the message "Category name already exists" appears.
  - Bug Report:
    - Issue: Duplicate Category Accepted
    - Actual: Entering "poetry" and clicking "Add Category" created a new category card "📖 poetry" alongside "Poetry". No "Category name already exists" message appeared. The duplicate check is missing or case-sensitive.
- [X] CS-04: Deleting a category requires confirmation, and cancelling keeps it.
  - Action: Click "Delete" on "Poetry", then click "Cancel" in the confirmation prompt.
  - Expected: "Poetry" remains in the category selector with its prompts intact.

## Interaction

- [X] IX-01: Favorite state updates immediately on click without a page reload.
  - Action: Click the star icon on a prompt, then observe the icon without reloading.
  - Expected: The star's fill state changes instantly, and the page URL and layout do not reload.
- [ ] IX-02: A success message confirms a category was added.
  - Action: Add a category named "Villains" and click "Save".
  - Expected: A success notification reading "Category 'Villains' added" appears and disappears automatically within about 5 seconds.
  - Bug Report:
    - Issue: Incorrect Notification Text
    - Actual: The notification reads "Category added" and does not include the name "Villains". It was visible at about 0.3s and 3.3s and gone by about 6.3s, so the auto-dismiss timing is consistent with the checklist.
- [X] IX-03: Editing a category opens a pre-filled input and "Cancel" reverts changes.
  - Action: Click "Edit" on "Poetry", change the text to "Verse", then click "Cancel".
  - Expected: The input initially shows "Poetry", and after cancelling, the selector still shows "Poetry" unchanged.

## Content

- [ ] CT-01: The category list contains exactly the five predefined categories.
  - Action: Open the category selector and read all entries.
  - Expected: The list shows "Short Stories", "Poetry", "Character Sketches", "Fantasy Landscapes", and "Brainstorming Topics", and nothing else.
  - Bug Report:
    - Issue: Incorrect Category Label
    - Actual: The fifth predefined category is labeled "Brainstorming", not "Brainstorming Topics". The other four names match, and the list has exactly five entries in the initial state, before any test-created categories were added.
- [X] CT-02: Prompts generated for each predefined category match that category's theme.
  - Action: For each of the five categories, click "Generate Prompt" three times and read each prompt.
  - Expected: Every prompt fits its category (e.g., Poetry prompts involve verse, rhyme, or imagery; Character Sketches prompts describe a person or character).
- [X] CT-03: Favorites and History entries show the correct prompt text and category label.
  - Action: Favorite a "Fantasy Landscapes" prompt, then compare the Favorites and History entries with the prompt display area.
  - Expected: Both lists show the same full prompt text and the label "Fantasy Landscapes".
- [X] CT-04: No placeholder or error text appears in any prompt or label.
  - Action: Browse all five categories, generate prompts, and review the favorites, history, and selector.
  - Expected: No text reads "undefined", "null", "lorem ipsum", "[object Object]", or is blank.

---

**Notes on the run**

- **Control mismatch:** The app has no "Generate Prompt" or "Save" button, and no category selector dropdown. Categories are clickable cards, and generation happens on card click, which then offers "Generate Another". I tested the equivalent controls. Favorites are text buttons ("Add to Favorites" / "Favorited"), not a star. FT-03 and IX-01 pass on behavior, but the star wording does not match the UI.
- **Left-over test data:** The app still has the extra categories "poetry" (from CS-03) and "Villains" (from IX-02). The deleted "Haiku" was removed. I did not clean up these two categories.
- **FT-06 ambiguity:** The checklist's "first prompt in History" is ambiguous with newest-first ordering. I clicked the oldest entry, and its exact text was redisplayed.
- **Budget:** About 32 tool calls were used out of the 100 allowed.