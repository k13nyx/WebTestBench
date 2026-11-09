All 20 checklist items are now executed. Here is the complete checklist with updated statuses.

# Test Result

## Functionality
- [X] FT-01: User can create a decision topic on the page.
  - Action: Enter a decision topic title (e.g., "Best Laptop for Work") in the topic input/field and confirm it (e.g., click "Save"/"Set" or click outside the field).
  - Expected: The page accepts the title and displays the decision topic "Best Laptop for Work" as the active topic.

- [X] FT-02: User can add a comparison criterion with a weight.
  - Action: Add a criterion named "Price" with weight 3.
  - Expected: The criterion "Price" appears in the criteria list/comparison table with weight 3 shown.

- [X] FT-03: User can add an option to compare.
  - Action: Add an option named "Option A".
  - Expected: "Option A" appears as a row/column in the comparison area with score inputs per criterion.

- [X] FT-04: User can enter a score for an option on a criterion.
  - Action: In the "Option A" row, enter score 8 in the cell for criterion "Price".
  - Expected: The cell displays 8 and the score is accepted.

- [ ] FT-05: Weighted score is automatically calculated and displayed per option.
  - Action: With at least 2 criteria (weights 3 and 2) and 2 options, enter scores so the expected weighted totals differ (e.g., Option A: 8×3 + 4×2 = 32; Option B: 5×3 + 9×2 = 33), then read each option's weighted score.
  - Expected: Each option shows a weighted score equal to the sum of (score × weight) across all its criteria — 32 for Option A, 33 for Option B.
  - Bug Report:
    - Issue: Incorrect Weighted Score Calculation (weight-normalized average instead of weighted sum)
    - Actual: With criteria "Price" (weight 3) and "Quality" (weight 2) and scores Option A = 8/4, Option B = 5/9, the comparison table shows weighted scores 6.4 for Option A and 6.6 for Option B (ranking: "Option A 6.4/10", "Option B 6.6/10"). The app computes Σ(score×weight)÷Σ(weight) (32÷5 = 6.4, 33÷5 = 6.6) instead of the expected raw weighted sums 32 and 33.

- [X] FT-06: Options are ranked by weighted score, highest first.
  - Action: With the scores from FT-05 (Option A = 32, Option B = 33), view the ranking section.
  - Expected: A ranking lists "Option B" first (rank 1) and "Option A" second (rank 2), ordered by descending weighted score.

- [X] FT-07: User can rename a criterion.
  - Action: Rename criterion "Price" to "Cost".
  - Expected: The criterion is displayed as "Cost" everywhere it appears (criteria list, comparison table headers) with its weight unchanged.

- [X] FT-08: User can rename an option.
  - Action: Rename option "Option A" to "Laptop A".
  - Expected: The option is displayed as "Laptop A" in the comparison table and in the ranking.

- [X] FT-09: User can reorder criteria.
  - Action: Move criterion "Price" to a different position among the criteria (e.g., click move-up/move-down control or drag it).
  - Expected: The criteria appear in the new order in the comparison table, with each criterion keeping its weight and its per-option scores.

- [X] FT-10: User can reorder options.
  - Action: Move "Option B" to a different position among the options (e.g., click move-up/move-down control or drag it).
  - Expected: The options appear in the new order in the comparison table, each keeping its scores and weighted score.

- [X] FT-11: User can remove a criterion.
  - Action: Remove criterion "Price" (which has weight 3 and scores entered).
  - Expected: "Price" no longer appears in the criteria list or comparison table, and remaining criteria and options are still shown.

- [X] FT-12: User can remove an option.
  - Action: Remove option "Option A".
  - Expected: "Option A" no longer appears in the comparison table or in the ranking.

## Constraint
- [X] CS-01: A criterion or option cannot be created/saved with an empty name.
  - Action: Attempt to add a criterion and an option with an empty (or whitespace-only) name.
  - Expected: The entry is rejected or blocked with a validation message; no nameless criterion/option is added.

- [X] CS-02: Weight values must be valid (numeric and non-negative).
  - Action: Enter "-2" and "abc" as a criterion's weight.
  - Expected: The invalid weight is rejected or not applied (validation message shown); the weighted score calculation does not use the invalid value.

- [X] CS-03: Score values must be valid numeric input.
  - Action: Enter "abc" into an option's score cell for a criterion.
  - Expected: The score is rejected or not applied (validation message shown); the option's weighted score does not change based on the invalid input.

- [ ] CS-04: Removing a criterion leaves no stale data in calculations.
  - Action: With weights 3 ("Price") and 2 ("Quality") and Option A scores 8 and 4 (weighted score 32), remove criterion "Price", then read Option A's weighted score.
  - Expected: Option A's weighted score recalculates to 8 (only Quality: 4×2), with no residual contribution from the removed criterion.
  - Bug Report:
    - Issue: Incorrect Weighted Score Calculation (recalculated value does not match expected weighted sum)
    - Actual: With "Price" (weight 3) and "Quality" (weight 2) and Option A scores Price=8 / Quality=4, the pre-removal weighted score displays 6.4 (checklist assumes 32). After removing "Price", Option A's weighted score immediately recalculates to 4.0 ("Option A 4.0/10" in the ranking) instead of the expected 8 (4×2). The removed criterion leaves no residual contribution (score went 6.4 → 4.0 cleanly), but the app divides by remaining total weight (4×2÷2 = 4.0) rather than showing the raw weighted sum 8.

## Interaction
- [X] IX-01: Added criteria and options appear immediately on the single comparison page.
  - Action: Add criterion "Battery" and option "Option C", then observe the page without reloading or navigating.
  - Expected: Both new entries appear in the comparison area immediately, on the same page, without a page reload.

- [X] IX-02: Weighted score and ranking update automatically when scores or weights change.
  - Action: Change an existing score (or weight) and observe the weighted score and ranking without clicking any "calculate" button.
  - Expected: The affected option's weighted score and the ranking order update automatically to reflect the new values.

## Content
- [X] CT-01: The displayed decision topic matches the entered topic exactly.
  - Action: Set the topic to "Best Laptop for Work" and read the displayed topic text.
  - Expected: The page shows exactly "Best Laptop for Work" (no truncation or leftover placeholder text).

- [X] CT-02: The ranking lists each option exactly once with its correct name and weighted score.
  - Action: With 2+ options present, compare the ranking entries against the options and their weighted scores in the comparison table.
  - Expected: Every option appears in the ranking exactly once — no missing, duplicated, or mismatched option names or weighted scores.