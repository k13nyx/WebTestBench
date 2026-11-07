# Test Result

## Functionality

- [X] FT-01: User can create/set the decision topic title
  - Action: Locate the decision topic/title field, enter "Laptop Purchase", and confirm (blur or Save).
  - Expected: The page displays "Laptop Purchase" as the decision topic title (persists in view).

- [X] FT-02: User can add a new comparison criterion
  - Action: In the Criteria section, enter "Battery Life" in the criterion name field and click "Add Criterion".
  - Expected: "Battery Life" appears as a new criterion row with its own weight input and a new score column for every option.

- [X] FT-03: User can assign a weight to each criterion
  - Action: Set the weight of "Battery Life" to 3 and confirm.
  - Expected: The criterion's weight field shows 3, and the weight is used in the weighted calculation (see FT-06).

- [X] FT-04: User can add multiple options to compare
  - Action: In the Options section, add two options named "Model A" and "Model B" using "Add Option".
  - Expected: Both options appear as rows in the comparison matrix and both appear in the ranking list.

- [X] FT-05: User can enter a score per criterion for each option
  - Action: In the "Model A" row, enter 5 for "Price" and 2 for "Battery Life".
  - Expected: Both values are stored and displayed in the corresponding cells of the matrix.

- [ ] FT-06: Weighted score is automatically calculated for each option
  - Action: With weights (Price = 2, Battery Life = 3) and scores (Model A: Price 5, Battery 2), read the weighted score shown for "Model A".
  - Expected: Weighted score equals the sum of (score × weight) across all criteria = (5×2)+(2×3) = 16; every option shows a numeric weighted score.
  - Bug Report:
    - Issue: Incorrect Calculation Formula (weighted average, not weighted sum)
    - Actual: Every option does show a numeric weighted score, but it is a normalized weighted average on a 0–10 scale, not a sum. With Price = 25% and the new Battery Life = 3% (the app has no absolute/raw weight input — weights are percentages on a 1–100 slider), "Model A (2024)" (Price 5, Battery Life 2) displayed **1.7**, i.e. (2×0.25 + 5×0.25) / (0.30+0.25+0.25+0.20+0.03) = 1.699 → "1.7", not 16. The ranking shows it as "1.7/10".

- [X] FT-07: Simple ranking of options is displayed
  - Action: Observe the Ranking section with the default options present.
  - Expected: All options are listed in descending order of weighted score, each with a rank position (1, 2, 3…) and its weighted score.

- [X] FT-08: User can rename an option and a criterion
  - Action: Rename option "Model A" to "Model A (2024)" and rename criterion "Battery Life" to "Battery".
  - Expected: The new names appear in the matrix and in the ranking list; the renamed criterion's column header updates and its scores are preserved.

- [X] FT-09: User can reorder options
  - Action: Move the last option up one position (Move up control / drag) in the options list.
  - Expected: The option's row order in the matrix matches the new position; scores and weighted score stay attached to that option.

- [X] FT-10: User can reorder criteria
  - Action: Move the last criterion up one position (Move up control / drag) in the criteria list.
  - Expected: The criterion's score column moves to the new position together with its name, weight, and all option scores.

- [X] FT-11: User can remove an option
  - Action: Click remove/delete on option "Model B" and confirm if prompted.
  - Expected: "Model B" disappears from the matrix and from the ranking list; the other options and their scores are unchanged.

- [X] FT-12: User can remove a criterion
  - Action: Click remove/delete on criterion "Battery" and confirm if prompted.
  - Expected: The criterion row and its score column are removed for all options, and every option's weighted score is recalculated without it.

## Constraint

- [ ] CS-01: Blank or duplicate option/criterion names are rejected
  - Action: Click "Add Option" with an empty name field, then click "Add Criterion" with a name that already exists (e.g. "Price").
  - Expected: No blank and no duplicate entry is created; a validation message is shown or the action is blocked.
  - Bug Report:
    - Issue: Missing Duplicate-Name Validation
    - Actual: The blank-name half is handled — "Add Option" and "Add" are disabled while their name fields are empty. The duplicate half is not: entering "Price" (already an existing criterion) and clicking "Add" created a second criterion row "Price (10%)" with a duplicate "Price (10%)" column in the matrix (Total Weight went to 110%). Likewise, entering the existing option name "MacBook Pro 14"" and clicking "Add Option" created a second identical option row and a second "MacBook Pro 14"" entry in the ranking list. No validation message or error was shown in either case.

- [X] CS-02: Invalid criterion weights are rejected
  - Action: Enter "-2" in a criterion weight field, then enter "abc" in the same field.
  - Expected: Neither value is accepted; the field keeps the last valid weight (or shows an error), and no weighted score is computed from the invalid input.

- [X] CS-03: Invalid or empty scores do not corrupt the calculation
  - Action: Enter "abc" in an option's score cell, then clear the cell to empty.
  - Expected: The invalid entry is rejected, the option's weighted score is recalculated using only valid numeric scores (empty treated as 0), and no "NaN"/"undefined" value is shown.

## Interaction

- [X] IX-01: Weighted scores update instantly when a score changes
  - Action: Change one option's score for a weighted criterion, without clicking any "Calculate" button and without reloading the page.
  - Expected: That option's weighted score updates immediately to the new correct value.

- [X] IX-02: Ranking order updates instantly when a weight changes
  - Action: Increase the weight of the criterion where the last-ranked option scores highest, without reloading the page.
  - Expected: All weighted scores update and the ranking list immediately re-sorts, moving that option up if its weighted score now exceeds the others.

- [ ] IX-03: Empty state is handled gracefully
  - Action: Remove all options from the board (or open a board with none).
  - Expected: The ranking area shows an empty/placeholder message instead of stale rows or error text, and the page remains usable (criteria can still be edited).
  - Bug Report:
    - Issue: Missing Empty-State Placeholder (section removed instead)
    - Actual: After deleting all four options, the entire "Ranking" section (heading and list) is removed from the page — no empty/placeholder message such as "No options yet" is displayed. The matrix also renders only its header row ("Option | Performance (30%) | … | Score") with no empty-state row. No stale rows or error text are shown and the page remains usable (a new criterion "Portability" could still be added, sliders still editable), but the required empty/placeholder message is absent.

## Content

- [X] CT-01: Page content is labelled and relevant to weighted decision comparison
  - Action: Read the page heading, section headings, and control labels (Topic, Criteria, Weight, Options, Ranking).
  - Expected: Each section is clearly labelled for its decision-comparison purpose; no placeholder text (e.g. "Lorem ipsum", "TODO") and no content unrelated to decision comparison.

- [X] CT-02: Matrix headers, labels, and numbers are complete and correctly formatted
  - Action: Inspect every column header and row label of the comparison matrix, and the numbers in the weighted score / ranking columns.
  - Expected: Every column shows a criterion name with its weight, every row shows an option name, and all displayed numbers share a consistent format (e.g. one or two decimals); no value appears as "NaN", "null", or "undefined".

### Notes on two deviations worth flagging beyond the checklist
- The app models criterion weight as a **percentage share** (1–100 slider, "Total Weight" indicator) and computes a **normalized weighted average on a 0–10 scale**, not the raw-weight/weighted-sum model assumed by FT-03/FT-06. It also does not enforce the total weight to equal 100% (observed totals of 110%, 151%, 161%).
- All 25 icon-only controls (edit, move up/down, delete, weight sliders, criterion name fields) have no `aria-label` or `title`, so they are unlabelled for assistive technology; the ranking positions 1–3 are conveyed only by trophy/medal/award icons with no text label.