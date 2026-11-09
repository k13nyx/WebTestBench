# Test Checklist

*Assumption: the weighted score is the sum of (score × weight) across all criteria. If the app normalizes by total weight, update FT-05 and CT-01.*

## Functionality
- [ ] FT-01: User can create a decision topic with a title.
  - Action: Enter "Choose a Laptop" in the topic title field and click the create/save topic control.
  - Expected: Topic "Choose a Laptop" is displayed, and the criteria and options sections appear on the same page.
- [ ] FT-02: User can add a comparison criterion with a name and weight.
  - Action: Enter criterion name "Price" with weight "3" and click "Add Criterion".
  - Expected: "Price" appears in the criteria list with weight 3.
- [ ] FT-03: User can add multiple options to compare.
  - Action: Add an option named "Option A", then add an option named "Option B".
  - Expected: Both "Option A" and "Option B" appear as separate rows in the comparison.
- [ ] FT-04: User can enter a score per criterion for each option.
  - Action: Enter score "8" for "Option A" under "Price".
  - Expected: The value 8 is displayed in the "Option A" / "Price" cell.
- [ ] FT-05: Each option shows a weighted score calculated automatically.
  - Action: For criteria "Price" (weight 3) and "Quality" (weight 2), enter Price = 8 and Quality = 5 for "Option A".
  - Expected: "Option A" shows a weighted score of 34 (8×3 + 5×2) without any manual calculation step.
- [ ] FT-06: User can view a ranking of options by weighted score.
  - Action: Locate the ranking section after scoring at least two options.
  - Expected: Options are listed with rank numbers starting at 1, ordered from highest to lowest weighted score.
- [ ] FT-07: User can rename an option.
  - Action: Rename "Option A" to "Laptop X" using its edit control and confirm.
  - Expected: The option row shows "Laptop X" and retains its scores.
- [ ] FT-08: User can rename a criterion.
  - Action: Rename "Price" to "Cost" using its edit control and confirm.
  - Expected: The criterion shows "Cost" and retains its weight and scores.
- [ ] FT-09: User can reorder options.
  - Action: Move "Option B" above "Option A" using its move control (or drag handle).
  - Expected: "Option B" appears above "Option A" in the comparison view.
- [ ] FT-10: User can reorder criteria.
  - Action: Move "Quality" above "Cost" using its move control (or drag handle).
  - Expected: "Quality" appears above "Cost" in the criteria list and in the score table column order.
- [ ] FT-11: User can remove an option.
  - Action: Remove "Option B" using its remove control and confirm if prompted.
  - Expected: "Option B" disappears from the comparison and from the ranking.
- [ ] FT-12: User can remove a criterion.
  - Action: Remove "Quality" using its remove control and confirm if prompted.
  - Expected: "Quality" disappears from the criteria list and from every option's score row.

## Constraint
- [ ] CS-01: Topic cannot be created without a title.
  - Action: Leave the topic title field empty and click the create/save topic control.
  - Expected: A validation message is shown, no topic is created, and the criteria and options sections stay hidden.
- [ ] CS-02: Criterion cannot be added with a blank name or a non-numeric weight.
  - Action: Click "Add Criterion" with the name empty and the weight "3"; then enter name "Speed" with weight "abc" and click "Add Criterion".
  - Expected: Each attempt shows a validation message, and no criterion is added to the list.
- [ ] CS-03: Score entry rejects non-numeric values.
  - Action: Enter "abc" in the "Option A" / "Price" score cell and press Enter or move focus away.
  - Expected: A validation message is shown, the value is not saved, and the previous score (or empty cell) remains.
- [ ] CS-04: Option cannot be added with a blank name.
  - Action: Click the add option control with the name field empty.
  - Expected: A validation message is shown, and no new option row is created.

## Interaction
- [ ] IX-01: Weighted scores update immediately when a score or weight changes.
  - Action: Change "Option A" / "Price" score from 8 to 10 and press Enter or move focus away; then change the "Price" weight from 3 to 4.
  - Expected: Without a page reload, "Option A"'s weighted score updates after each change to the value matching the formula in FT-05.
- [ ] IX-02: Ranking re-sorts immediately when scores or weights change.
  - Action: With "Option B" ranked below "Option A", raise "Option B"'s score so its weighted total exceeds "Option A"'s.
  - Expected: Without a page reload, the ranking updates so "Option B" moves to rank 1 and rank numbers stay sequential.

## Content
- [ ] CT-01: Ranking values match the comparison table and contain no invalid placeholders.
  - Action: Compare each option's weighted score in the table with its value in the ranking section, including after adding a new option with no scores entered.
  - Expected: Values are identical in both places and are numbers; no "NaN", "undefined", or blank total is displayed.
- [ ] CT-02: Renamed names appear consistently everywhere.
  - Action: Rename "Option A" to "Laptop X" and "Price" to "Cost", then check the score table headers, option rows, and ranking.
  - Expected: "Laptop X" and "Cost" appear in every location, and no old name remains anywhere on the page.