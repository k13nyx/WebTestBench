# Test Checklist

## Functionality

- [ ] FT-01: User can create a decision topic
  - Action: Enter a topic name (e.g., "Choose a laptop") into the topic input field and confirm/save it.
  - Expected: The topic name is displayed as the title of the decision page.

- [ ] FT-02: User can add a comparison criterion with a weight
  - Action: Enter a criterion name (e.g., "Price") and a weight value (e.g., 3), then click the "Add Criterion" button.
  - Expected: The criterion "Price" with weight 3 appears in the criteria list on the same page.

- [ ] FT-03: User can add a comparison option
  - Action: Enter an option name (e.g., "Option A") and click the "Add Option" button; repeat for a second option.
  - Expected: Both options appear on the page, each with a score input for every defined criterion.

- [ ] FT-04: User can enter a score for each option per criterion
  - Action: For Option A, enter a score (e.g., 8) for the "Price" criterion and a different score (e.g., 5) for Option A's next criterion.
  - Expected: Both scores are saved and visible in their respective score inputs for Option A.

- [ ] FT-05: Weighted score is automatically calculated for each option
  - Action: With criteria weights (e.g., Price=3, Quality=2) and Option A scores (Price=8, Quality=5), check Option A's weighted score.
  - Expected: The weighted score equals the sum of (score × weight) / sum of weights (e.g., (8×3 + 5×2) / (3+2) = 6.8), displayed without manual recalculation.

- [ ] FT-06: Ranking of options is displayed and correctly ordered
  - Action: Enter scores so Option A totals higher than Option B and view the ranking section.
  - Expected: Options are listed from highest to lowest weighted score, with Option A ranked #1 and Option B ranked #2.

- [ ] FT-07: User can rename an option and a criterion
  - Action: Edit the name of an option (e.g., "Option A" → "MacBook") and a criterion (e.g., "Price" → "Cost"), then confirm the edit.
  - Expected: The new names are displayed everywhere on the page (score table headers/rows, ranking) while scores, weights, and calculations remain unchanged.

- [ ] FT-08: User can reorder options and criteria
  - Action: Use the reorder control (e.g., up/down arrow or drag handle) to move the last option to the first position and the last criterion to the first position.
  - Expected: The option and criterion appear in their new positions; all scores, weights, weighted totals, and ranking values stay correct.

- [ ] FT-09: User can remove an option and a criterion
  - Action: Remove one option and then one criterion via their delete/remove buttons.
  - Expected: The removed option and criterion disappear from the page, and all weighted scores and the ranking update to reflect only the remaining data.

## Constraint

- [ ] CS-01: Criterion cannot be added without a name
  - Action: Leave the criterion name field empty and click "Add Criterion".
  - Expected: No new criterion is created; an inline validation message (e.g., "Criterion name is required") is shown.

- [ ] CS-02: Option cannot be added without a name
  - Action: Leave the option name field empty and click "Add Option".
  - Expected: No new option is created; an inline validation message indicating the option name is required is shown.

- [ ] CS-03: Criterion weight must be a valid positive number
  - Action: Enter an invalid weight (e.g., "abc", -1, or leave blank) and attempt to save the criterion.
  - Expected: The weight is rejected with an error message; the criterion is not saved with the invalid weight, and calculations are unchanged.

- [ ] CS-04: Scores must stay within the allowed score range
  - Action: Enter an out-of-range score (e.g., 99 or -5) into an option's score field for a criterion.
  - Expected: The invalid score is rejected or clamped with an error message, and the weighted score is not recalculated using the invalid value.

## Interaction

- [ ] IX-01: Weighted score and ranking update immediately when a score changes
  - Action: Change Option B's score for a weighted criterion from 5 to 10 and observe the weighted score and ranking.
  - Expected: Option B's weighted total and the ranking order update instantly on the same page without a page reload or manual "recalculate" action.

- [ ] IX-02: Weighted scores and ranking update immediately when a weight changes
  - Action: Change a criterion's weight (e.g., from 3 to 1) while scores remain entered.
  - Expected: All options' weighted scores and the ranking recompute instantly to reflect the new weight.

- [ ] IX-03: New criterion or option appears immediately on the page
  - Action: Add a new criterion (or option) after scores already exist.
  - Expected: A new score input column/row appears immediately for all existing options, and the weighted scores include the new criterion (treated as unscored/zero as defined) without page reload.

## Content

- [ ] CT-01: All decision components are visible on a single page
  - Action: View the page with a topic, 2+ criteria, and 2+ options entered.
  - Expected: Topic title, criteria with weights, options with per-criterion score inputs, weighted totals, and the ranking are all simultaneously visible on one page, each labeled clearly.

- [ ] CT-02: Displayed values match the entered data exactly
  - Action: Cross-check every displayed criterion name, weight, option name, and score against what was entered or edited.
  - Expected: Every label, weight, and score shown on the page (including in the ranking) exactly matches the current entered values, with no stale or mismatched data.