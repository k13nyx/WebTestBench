# Test Result

## Functionality

- [X] **FT-01: Predefined prompt categories are available**
  - **Action:** Open the creative prompt generator webpage and inspect the category controls.
  - **Expected:** The categories **Short Stories**, **Poetry**, **Character Sketches**, **Fantasy Landscapes**, and **Brainstorming Topics** are available for selection.

- [X] **FT-02: User can select a prompt category**
  - **Action:** Select each predefined category one at a time.
  - **Expected:** The selected category is visibly identified as the active category.

- [X] **FT-03: User can generate a random prompt**
  - **Action:** Select a category and activate **Generate Random Prompt**.
  - **Expected:** A prompt is displayed and it is relevant to the selected category.

- [X] **FT-04: User can generate prompts repeatedly**
  - **Action:** With a category selected, activate **Generate Random Prompt** multiple times.
  - **Expected:** Each activation completes successfully and displays a prompt without clearing the selected category or breaking the page.

- [X] **FT-05: User can mark a displayed prompt as a favorite**
  - **Action:** Generate a prompt and activate its **Favorite** control.
  - **Expected:** The prompt is marked as a favorite and its favorite state is visibly indicated.

- [X] **FT-06: User can remove a prompt from favorites**
  - **Action:** Activate the favorite control again for a prompt already marked as a favorite.
  - **Expected:** The prompt is no longer marked as a favorite.

- [X] **FT-07: User can view prompts from the current visit in history**
  - **Action:** Generate or view several prompts, then open the **History** area.
  - **Expected:** The history lists the prompts viewed during the current visit.

- [X] **FT-08: User can revisit a prompt from history**
  - **Action:** Select a prompt listed in **History**.
  - **Expected:** The selected historical prompt is displayed again in the main prompt area.

- [X] **FT-09: User can add a custom category**
  - **Action:** Open category customization, enter a new category name, and activate **Add** or **Save**.
  - **Expected:** The new category appears in the category controls and can be selected.

- [X] **FT-10: User can modify a category**
  - **Action:** Open the edit control for an existing category, change its name, and save the change.
  - **Expected:** The updated category name replaces the old name wherever categories are displayed.

- [X] **FT-11: User can delete a category**
  - **Action:** Open the delete control for a custom category and confirm deletion if prompted.
  - **Expected:** The category is removed from the category controls and can no longer be selected.

## Constraint

- [X] **CS-01: Prompt generation requires a selected category**
  - **Action:** Open the page without selecting a category and activate **Generate Random Prompt**.
  - **Expected:** No prompt is generated, and the interface clearly indicates that a category must be selected first.

- [ ] **CS-02: Empty category names cannot be saved**
  - **Action:** In category customization, attempt to add or rename a category using an empty name or whitespace-only name.
  - **Expected:** The category is not saved and the interface identifies the category name as required.
  - **Bug Report:**
    - **Issue:** Missing validation feedback
    - **Actual:** A whitespace-only category name could not be submitted because the **Add Category** button remained disabled, but the interface did not identify the category name as required or display a validation message.

- [ ] **CS-03: Duplicate category names cannot be created**
  - **Action:** Attempt to add or rename a category to a name that already exists, such as **Poetry**.
  - **Expected:** The duplicate category is not saved.
  - **Bug Report:**
    - **Issue:** Duplicate category allowed
    - **Actual:** A second custom category named **Poetry** was successfully added, resulting in two categories with the same name.

- [X] **CS-04: Deleting a category requires explicit confirmation**
  - **Action:** Activate the delete control for a category and inspect the resulting interaction before confirming.
  - **Expected:** The category remains available until the deletion is explicitly confirmed.

- [X] **CS-05: History contains only prompts viewed during the current visit**
  - **Action:** Generate prompts, end the visit, then start a new visit to the webpage and open **History**.
  - **Expected:** Prompts from the previous visit are not presented as the new visit’s history.

## Interaction

- [X] **IX-01: Active category state updates immediately**
  - **Action:** Select one category, then select a different category.
  - **Expected:** The newly selected category receives the active visual state and the previously selected category loses it.

- [X] **IX-02: Favorite control provides immediate feedback**
  - **Action:** Mark a displayed prompt as a favorite.
  - **Expected:** The favorite control changes state immediately so the user can tell the action succeeded.

- [X] **IX-03: Category management controls provide completion feedback**
  - **Action:** Successfully add, rename, or delete a category.
  - **Expected:** The updated category list is shown immediately and any open customization state closes or indicates completion.

## Content

- [X] **CT-01: Generated prompts match their selected categories**
  - **Action:** Generate prompts separately for **Short Stories**, **Poetry**, **Character Sketches**, **Fantasy Landscapes**, and **Brainstorming Topics**.
  - **Expected:** Each displayed prompt’s subject and format clearly correspond to the selected category.