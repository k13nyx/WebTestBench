# Test Checklist

**Preconditions:** Desktop browser, app opened on the decision page with its default decision board (a pre-existing topic, criteria with weights, and options). Creation items add to that board; edit items operate on existing entries.

## Functionality
- [ ] FT-01: User can create/set the decision topic title
  - Action: Locate the decision topic/title field, enter "Laptop Purchase", and confirm (blur or Save).
  - Expected: The page displays "Laptop Purchase" as the decision topic title (persists in view).

- [ ] FT-02: User can add a new comparison criterion
  - Action: In the Criteria section, enter "Battery Life" in the criterion name field and click "Add Criterion".
  - Expected: "Battery Life" appears as a new criterion row with its own weight input and a new score column for every option.

- [ ] FT-03: User can assign a weight to each criterion
  - Action: Set the weight of "Battery Life" to 3 and confirm.
  - Expected: The criterion's weight field shows 3, and the weight is used in the weighted calculation (see FT-06).

- [ ] FT-04: User can add multiple options to compare
  - Action: In the Options section, add two options named "Model A" and "Model B" using "Add Option".
  - Expected: Both options appear as rows in the comparison matrix and both appear in the ranking list.

- [ ] FT-05: User can enter a score per criterion for each option
  - Action: In the "Model A" row, enter 5 for "Price" and 2 for "Battery Life".
  - Expected: Both values are stored and displayed in the corresponding cells of the matrix.

- [ ] FT-06: Weighted score is automatically calculated for each option
  - Action: With weights (Price = 2, Battery Life = 3) and scores (Model A: Price 5, Battery 2), read the weighted score shown for "Model A".
  - Expected: Weighted score equals the sum of (score × weight) across all criteria = (5×2)+(2×3) = 16; every option shows a numeric weighted score.

- [ ] FT-07: Simple ranking of options is displayed
  - Action: Observe the Ranking section with the default options present.
  - Expected: All options are listed in descending order of weighted score, each with a rank position (1, 2, 3…) and its weighted score.

- [ ] FT-08: User can rename an option and a criterion
  - Action: Rename option "Model A" to "Model A (2024)" and rename criterion "Battery Life" to "Battery".
  - Expected: The new names appear in the matrix and in the ranking list; the renamed criterion's column header updates and its scores are preserved.

- [ ] FT-09: User can reorder options
  - Action: Move the last option up one position (Move up control / drag) in the options list.
  - Expected: The option's row order in the matrix matches the new position; scores and weighted score stay attached to that option.

- [ ] FT-10: User can reorder criteria
  - Action: Move the last criterion up one position (Move up control / drag) in the criteria list.
  - Expected: The criterion's score column moves to the new position together with its name, weight, and all option scores.

- [ ] FT-11: User can remove an option
  - Action: Click remove/delete on option "Model B" and confirm if prompted.
  - Expected: "Model B" disappears from the matrix and from the ranking list; the other options and their scores are unchanged.

- [ ] FT-12: User can remove a criterion
  - Action: Click remove/delete on criterion "Battery" and confirm if prompted.
  - Expected: The criterion row and its score column are removed for all options, and every option's weighted score is recalculated without it.

## Constraint
- [ ] CS-01: Blank or duplicate option/criterion names are rejected
  - Action: Click "Add Option" with an empty name field, then click "Add Criterion" with a name that already exists (e.g. "Price").
  - Expected: No blank and no duplicate entry is created; a validation message is shown or the action is blocked.

- [ ] CS-02: Invalid criterion weights are rejected
  - Action: Enter "-2" in a criterion weight field, then enter "abc" in the same field.
  - Expected: Neither value is accepted; the field keeps the last valid weight (or shows an error), and no weighted score is computed from the invalid input.

- [ ] CS-03: Invalid or empty scores do not corrupt the calculation
  - Action: Enter "abc" in an option's score cell, then clear the cell to empty.
  - Expected: The invalid entry is rejected, the option's weighted score is recalculated using only valid numeric scores (empty treated as 0), and no "NaN"/"undefined" value is shown.

## Interaction
- [ ] IX-01: Weighted scores update instantly when a score changes
  - Action: Change one option's score for a weighted criterion, without clicking any "Calculate" button and without reloading the page.
  - Expected: That option's weighted score updates immediately to the new correct value.

- [ ] IX-02: Ranking order updates instantly when a weight changes
  - Action: Increase the weight of the criterion where the last-ranked option scores highest, without reloading the page.
  - Expected: All weighted scores update and the ranking list immediately re-sorts, moving that option up if its weighted score now exceeds the others.

- [ ] IX-03: Empty state is handled gracefully
  - Action: Remove all options from the board (or open a board with none).
  - Expected: The ranking area shows an empty/placeholder message instead of stale rows or error text, and the page remains usable (criteria can still be edited).

## Content
- [ ] CT-01: Page content is labelled and relevant to weighted decision comparison
  - Action: Read the page heading, section headings, and control labels (Topic, Criteria, Weight, Options, Ranking).
  - Expected: Each section is clearly labelled for its decision-comparison purpose; no placeholder text (e.g. "Lorem ipsum", "TODO") and no content unrelated to decision comparison.

- [ ] CT-02: Matrix headers, labels, and numbers are complete and correctly formatted
  - Action: Inspect every column header and row label of the comparison matrix, and the numbers in the weighted score / ranking columns.
  - Expected: Every column shows a criterion name with its weight, every row shows an option name, and all displayed numbers share a consistent format (e.g. one or two decimals); no value appears as "NaN", "null", or "undefined".