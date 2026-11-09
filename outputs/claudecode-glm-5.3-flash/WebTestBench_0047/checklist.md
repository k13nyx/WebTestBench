# Test Checklist

## Functionality
- [ ] FT-01: User can create a decision topic with a title
  - Action: Enter a title (e.g., "Which laptop to buy") in the topic/name input and click the create/add button.
  - Expected: The topic "Which laptop to buy" is created and displayed as the page's decision topic.
- [ ] FT-02: User can add a comparison criterion
  - Action: Enter "Price" in the criterion input and click the "Add Criterion" (or equivalent) button.
  - Expected: "Price" appears in the criteria list with its own weight input.
- [ ] FT-03: User can assign a weight to each criterion
  - Action: Set the weight input of criterion "Price" to 3, and the weight of criterion "Quality" to 1.
  - Expected: Both weights are saved and displayed as 3 and 1 respectively.
- [ ] FT-04: User can add multiple options
  - Action: Add two options named "Laptop A" and "Laptop B" via the option add control.
  - Expected: Both options appear in the comparison table, each with a score entry for every criterion.
- [ ] FT-05: User can enter a score per criterion for each option
  - Action: For "Laptop A", enter score 8 for "Price" and 6 for "Quality"; for "Laptop B", enter 5 for "Price" and 9 for "Quality".
  - Expected: All entered scores are stored and displayed in the corresponding table cells.
- [ ] FT-06: Weighted score is calculated automatically per option
  - Action: With weights Price=3, Quality=1 and Laptop A scores 8 and 6.
  - Expected: Laptop A's displayed weighted score equals the weighted average (8×3 + 6×1) ÷ (3+1) = 7.5, computed without any manual "calculate" action.
- [ ] FT-07: Ranking of options is displayed in correct order
  - Action: View the ranking section after entering scores for both options (Laptop A weighted 7.5; Laptop B = (5×3+9×1)÷4 = 6).
  - Expected: Options are listed from highest to lowest weighted score: Laptop A ranked #1, Laptop B ranked #2.
- [ ] FT-08: User can rename a criterion and an option
  - Action: Rename criterion "Price" to "Cost" and option "Laptop A" to "MacBook" using the rename/edit control.
  - Expected: New names appear everywhere (criteria list, score table, ranking) and existing weights and scores are preserved unchanged.
- [ ] FT-09: User can reorder criteria and options
  - Action: Use the move up/down control to move criterion "Quality" above "Cost", and move option "Laptop B" above "MacBook".
  - Expected: The new order is reflected in both the comparison table and the criteria list.
- [ ] FT-10: User can remove a criterion
  - Action: Click the remove/delete control on criterion "Quality".
  - Expected: "Quality" disappears from the criteria list and table, and all options' weighted scores are recalculated excluding it.
- [ ] FT-11: User can remove an option
  - Action: Click the remove/delete control on option "Laptop B".
  - Expected: The option's row disappears from the comparison table and ranking, and remaining options' data is unchanged.

## Constraint
- [ ] CS-01: Blank criterion/option names are rejected
  - Action: Leave the criterion input empty and click "Add Criterion"; repeat for the option input.
  - Expected: No empty entry is created (input shows a validation message or the add is ignored).
- [ ] CS-02: Weight must be a valid non-negative number
  - Action: Enter "-2" and then "abc" into a criterion's weight input.
  - Expected: Invalid values are rejected or corrected (error message shown, value not stored); weighted scores never become negative/NaN.
- [ ] CS-03: Score must be a valid number
  - Action: Enter "abc" (or leave non-numeric content) into a score cell for an option.
  - Expected: The invalid input is rejected, cleared, or shows a validation error; the weighted score calculation does not break.
- [ ] CS-04: Reordering does not detach scores from their owner
  - Action: Reorder options (move Laptop B above MacBook) after scores are entered.
  - Expected: Each option keeps exactly its own scores and weighted score; no scores shift to another option.

## Interaction
- [ ] IX-01: Weighted score and ranking update live when a weight changes
  - Action: While viewing the ranking, change criterion "Cost" weight from 3 to 1.
  - Expected: All options' weighted scores and their ranking positions update immediately without page reload or clicking a recalculate button.
- [ ] IX-02: Score entry updates results immediately
  - Action: Change Laptop A's "Quality" score from 6 to 10 and observe.
  - Expected: Laptop A's weighted score cell updates immediately upon entry (no separate save/confirm step required).

## Content
- [ ] CT-01: Decision topic title is prominently displayed
  - Action: View the page after creating the topic.
  - Expected: The topic title (e.g., "Which laptop to buy") is visible as the page heading/label.
- [ ] CT-02: Ranking displays option names, rank positions, and weighted scores
  - Action: View the ranking section with at least two scored options.
  - Expected: Each ranking row shows the option's name, its rank number (1, 2, …), and its weighted score value.
- [ ] CT-03: Comparison table shows all criteria with their weights visible
  - Action: View the comparison table with 2 criteria having weights 3 and 1.
  - Expected: Every criterion appears in the table labeled with its name and its assigned weight (e.g., "Cost (3)"), and each option row has a score cell for every criterion.