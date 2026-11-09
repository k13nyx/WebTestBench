All checklist items have been executed and verified. Here is the complete test report.

# Test Result

## Functionality

- [X] FT-01: User can create a decision topic
  - Action: Enter a topic name (e.g., "Choose a laptop") into the topic input field and confirm/save it.
  - Expected: The topic name is displayed as the title of the decision page.

- [X] FT-02: User can add a comparison criterion with a weight
  - Action: Enter a criterion name (e.g., "Price") and a weight value (e.g., 3), then click the "Add Criterion" button.
  - Expected: The criterion "Price" with weight 3 appears in the criteria list on the same page.

- [X] FT-03: User can add a comparison option
  - Action: Enter an option name (e.g., "Option A") and click the "Add Option" button; repeat for a second option.
  - Expected: Both options appear on the page, each with a score input for every defined criterion.

- [X] FT-04: User can enter a score for each option per criterion
  - Action: For Option A, enter a score (e.g., 8) for the "Price" criterion and a different score (e.g., 5) for Option A's next criterion.
  - Expected: Both scores are saved and visible in their respective score inputs for Option A.

- [X] FT-05: Weighted score is automatically calculated for each option
  - Action: With criteria weights (e.g., Price=3, Quality=2) and Option A scores (Price=8, Quality=5), check Option A's weighted score.
  - Expected: The weighted score equals the sum of (score × weight) / sum of weights (e.g., (8×3 + 5×2) / (3+2) = 6.8), displayed without manual recalculation.

- [X] FT-06: Ranking of options is displayed and correctly ordered
  - Action: Enter scores so Option A totals higher than Option B and view the ranking section.
  - Expected: Options are listed from highest to lowest weighted score, with Option A ranked #1 and Option B ranked #2.

- [X] FT-07: User can rename an option and a criterion
  - Action: Edit the name of an option (e.g., "Option A" → "MacBook") and a criterion (e.g., "Price" → "Cost"), then confirm the edit.
  - Expected: The new names are displayed everywhere on the page (score table headers/rows, ranking) while scores, weights, and calculations remain unchanged.

- [X] FT-08: User can reorder options and criteria
  - Action: Use the reorder control (e.g., up/down arrow or drag handle) to move the last option to the first position and the last criterion to the first position.
  - Expected: The option and criterion appear in their new positions; all scores, weights, weighted totals, and ranking values stay correct.

- [X] FT-09: User can remove an option and a criterion
  - Action: Remove one option and then one criterion via their delete/remove buttons.
  - Expected: The removed option and criterion disappear from the page, and all weighted scores and the ranking update to reflect only the remaining data.

## Constraint

- [ ] CS-01: Criterion cannot be added without a name
  - Action: Leave the criterion name field empty and click "Add Criterion".
  - Expected: No new criterion is created; an inline validation message (e.g., "Criterion name is required") is shown.
  - Bug Report:
    - Issue: Missing inline validation message (disabled-button validation only)
    - Actual: With the criterion name field empty, the "Add" button is disabled and unclickable; a forced click on it creates no criterion (criteria count unchanged, 2 → 2). However, no inline validation message (e.g., "Criterion name is required") is displayed anywhere on the page — the empty-field feedback is only the disabled button state.

- [ ] CS-02: Option cannot be added without a name
  - Action: Leave the option name field empty and click "Add Option".
  - Expected: No new option is created; an inline validation message indicating the option name is required is shown.
  - Bug Report:
    - Issue: Missing inline validation message (disabled-button validation only)
    - Actual: With the option name field empty, the "Add Option" button is disabled and unclickable; a forced click on it creates no option (option rows unchanged, 2 → 2). However, no inline validation message indicating the option name is required is displayed anywhere on the page.

- [ ] CS-03: Criterion weight must be a valid positive number
  - Action: Enter an invalid weight (e.g., "abc", -1, or leave blank) and attempt to save the criterion.
  - Expected: The weight is rejected with an error message; the criterion is not saved with the invalid weight, and calculations are unchanged.
  - Bug Report:
    - Issue: Missing weight input field — invalid-weight validation cannot be performed
    - Actual: The action cannot be executed: the criterion weight can only be set via a range slider constrained to min 1 / max 100 (step 1). There is no weight text/number input field in the "Add Criterion" form or in the criterion rows, so invalid weights ("abc", -1, or blank) cannot be entered or submitted, and no weight-validation error message exists anywhere in the UI.

- [X] CS-04: Scores must stay within the allowed score range
  - Action: Enter an out-of-range score (e.g., 99 or -5) into an option's score field for a criterion.
  - Expected: The invalid score is rejected or clamped with an error message, and the weighted score is not recalculated using the invalid value.

## Interaction

- [X] IX-01: Weighted score and ranking update immediately when a score changes
  - Action: Change Option B's score for a weighted criterion from 5 to 10 and observe the weighted score and ranking.
  - Expected: Option B's weighted total and the ranking order update instantly on the same page without a page reload or manual "recalculate" action.

- [X] IX-02: Weighted scores and ranking update immediately when a weight changes
  - Action: Change a criterion's weight (e.g., from 3 to 1) while scores remain entered.
  - Expected: All options' weighted scores and the ranking recompute instantly to reflect the new weight.

- [X] IX-03: New criterion or option appears immediately on the page
  - Action: Add a new criterion (or option) after scores already exist.
  - Expected: A new score input column/row appears immediately for all existing options, and the weighted scores include the new criterion (treated as unscored/zero as defined) without page reload.

## Content

- [X] CT-01: All decision components are visible on a single page
  - Action: View the page with a topic, 2+ criteria, and 2+ options entered.
  - Expected: Topic title, criteria with weights, options with per-criterion score inputs, weighted totals, and the ranking are all simultaneously visible on one page, each labeled clearly.

- [X] CT-02: Displayed values match the entered data exactly
  - Action: Cross-check every displayed criterion name, weight, option name, and score against what was entered or edited.
  - Expected: Every label, weight, and score shown on the page (including in the ranking) exactly matches the current entered values, with no stale or mismatched data.

---

**Test Notes (evidence summary):**
- The app expresses criterion weights on a 1–100 scale via a slider (not a free-text number). Weights 30 / 20 / 10 were used as the proportional equivalents of 3 / 2 / 1 from the checklist examples, and the expected formula held exactly: Option A = (8×30 + 5×20) / 50 = **6.8** (FT-05), matching (8×3 + 5×2) / (3+2).
- FT-06 ranking: Option A #1 (6.8/10), Option B #2 (4.4/10), highest → lowest.
- FT-07/08: after rename (Option A → MacBook, Price → Cost) and reorder (Option B → first row, Quality → first column), scores stayed attached to the correct criteria and all totals were unchanged (6.8 / 4.4).
- FT-09: after removing the disposable option and criterion, weighted scores reverted to 6.8 / 4.4 and the ranking reflected only remaining data.
- CS-04: entering 99 clamped the score input to 10 (weighted recalculated as 8.8 using the clamped value); entering -5 clamped to 0 (weighted 4.8); the invalid values 99/-5 were never used in calculations.
- IX-01: Option B score 5 → 10 on Quality produced instant weighted update 4.4 → 6.4 and instant ranking refresh (no reload). IX-02: Cost weight 30 → 10 instantly recomputed MacBook 6.8 → 6.0 and Option B 6.4 → 8.0, flipping the ranking to Option B #1. IX-03: adding a "Warranty" criterion after scores existed immediately created a new score input for every option, with unscored warranty treated as 0 (Option B 6.0 = (10×20+4×10+0×10)/40, MacBook 4.5).
- CT-01/02 final cross-check on one page: topic "Choose a laptop"; criteria Quality 20% / Cost 10% / Warranty 10% (Total Weight: 40%); options Option B (10, 4, unscored → 6.0) and MacBook (5, 8, unscored → 4.5); ranking Option B #1 6.0/10, MacBook #2 4.5/10 — all displayed values matched the entered data exactly.