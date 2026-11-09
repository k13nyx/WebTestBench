# Test Checklist

## Functionality
- [ ] FT-01: User can create a decision topic
  - Action: Enter a topic name (e.g., "Choose a Laptop") into the topic/title field and confirm (save/create).
  - Expected: The topic is created and stored; no error occurs.

- [ ] FT-02: User can define multiple comparison criteria
  - Action: Add two criteria (e.g., "Price", "Performance") using the add-criteria control.
  - Expected: Both criteria appear as separate criteria entries (rows/columns) ready to be weighted.

- [ ] FT-03: User can assign a weight to each criterion
  - Action: Set weight "3" for "Price" and weight "5" for "Performance".
  - Expected: Each criterion displays its assigned weight and the values persist after saving/refreshing the page state.

- [ ] FT-04: User can add multiple options on the single page
  - Action: Add three options (e.g., "Laptop A", "Laptop B", "Laptop C").
  - Expected: All three options are listed on the same page, each with a score field per criterion.

- [ ] FT-05: User can enter a score per criterion for each option
  - Action: Enter scores for "Laptop A" (e.g., Price=4, Performance=2) and for the other options.
  - Expected: Each entered score is saved and displayed in the corresponding option–criterion cell.

- [ ] FT-06: Weighted score is automatically calculated per option
  - Action: With weights Price=3, Performance=5 and Laptop A scores Price=4, Performance=2, view Laptop A's weighted score.
  - Expected: The weighted score shows 22 (4×3 + 2×5), computed automatically with no manual calculation or button press required beyond entering scores.

- [ ] FT-07: A ranking of options is displayed
  - Action: After entering scores for all options, view the ranking section.
  - Expected: All options are listed ranked by weighted score from highest to lowest, including each option's total score.

- [ ] FT-08: User can rename an option and a criterion
  - Action: Rename "Laptop A" to "Laptop A (Refurb)" and rename "Price" to "Cost".
  - Expected: The new names appear everywhere the item is shown (scores table and ranking); the item's scores/weights are unchanged.

- [ ] FT-09: User can reorder options and criteria
  - Action: Move "Laptop C" above "Laptop A", and move "Performance" before "Price".
  - Expected: Both items appear at their new positions after the move; all associated scores/weights move with them.

- [ ] FT-10: User can remove an option
  - Action: Remove "Laptop B".
  - Expected: "Laptop B" disappears from the options table and from the ranking; other options' data is unchanged.

- [ ] FT-11: User can remove a criterion
  - Action: Remove the "Price" criterion.
  - Expected: "Price" is removed from the criteria list and from every option's score entry; the page no longer asks for that score.

## Constraint
- [ ] CS-01: Required names cannot be empty
  - Action: Attempt to create a topic, add a criterion, and add an option each with an empty name.
  - Expected: All three actions are blocked with an inline validation message; no empty item is created.

- [ ] CS-02: Weights and scores must be valid numbers
  - Action: Attempt to enter a non-numeric weight (e.g., "abc") and a non-numeric score (e.g., "xyz"); also attempt a negative weight.
  - Expected: The invalid input is rejected with a validation message, and the stored weight/score remains the previous valid value.

- [ ] CS-03: Removing a criterion leaves all other data intact
  - Action: With 3 criteria and 3 options scored, remove one criterion.
  - Expected: Scores for the remaining criteria are unchanged, and each option's weighted score is recomputed using only the remaining criteria (no leftover values from the removed criterion).

## Interaction
- [ ] IX-01: Weighted score updates immediately when a score or weight changes
  - Action: Change Laptop A's "Performance" score from 2 to 5, then change the "Performance" weight from 5 to 1.
  - Expected: Laptop A's weighted score recalculates and refreshes on screen right after each change, without a page reload.

- [ ] IX-02: Ranking updates automatically after data changes
  - Action: After changing a score or weight so that the order of totals changes, view the ranking.
  - Expected: The ranking re-sorts immediately so the option with the highest weighted score is listed first.

- [ ] IX-03: Reorder actions give immediate visual feedback
  - Action: Use the move-up/move-down control on an option row and on a criterion column.
  - Expected: The item visibly jumps to the adjacent position instantly, and no other item's data shifts incorrectly.

- [ ] IX-04: Removal requires confirmation and reflects instantly
  - Action: Click the remove control on an option, confirm the removal, then repeat for a criterion.
  - Expected: A confirmation prompt appears before deletion; after confirming, the item disappears from the page immediately.

## Content
- [ ] CT-01: Decision topic title is displayed prominently
  - Action: Create topic "Choose a Laptop" and observe the page.
  - Expected: The exact text "Choose a Laptop" is displayed as the page's heading/topic title.

- [ ] CT-02: Displayed labels and values match the user's input exactly
  - Action: Review the criteria names, option names, weights, scores, weighted totals, and ranking after entering test data.
  - Expected: Every displayed label and number exactly matches what was entered or calculated — no typos, truncations, placeholder text, or unrelated content.