# Test Checklist

## Functionality
- [ ] FT-01: Set decision topic title
  - Action: Click the decision topic header field, enter "New Laptop Selection", and press Enter or click outside the field.
  - Expected: The topic title is updated and displays "New Laptop Selection".
- [ ] FT-02: Add comparison criterion with weight
  - Action: Click "Add Criterion", enter name "Battery Life", set weight to "3", and confirm.
  - Expected: "Battery Life" is added to the criteria list with a weight of 3.
- [ ] FT-03: Add comparison option
  - Action: Click "Add Option", enter name "Model X", and confirm.
  - Expected: "Model X" appears as a new option in the comparison matrix with score input fields for each criterion.
- [ ] FT-04: Enter criterion score for an option
  - Action: Enter score "8" into the "Battery Life" score field for "Model X".
  - Expected: The score field displays "8" and saves the value for "Model X".
- [ ] FT-05: Automatic weighted score calculation
  - Action: Enter valid scores for all criteria on an option with defined weights.
  - Expected: The total weighted score for that option is automatically calculated (sum of score × weight) and displayed without page refresh.
- [ ] FT-06: View simple ranking of options
  - Action: Score multiple options with differing values and navigate to the ranking section.
  - Expected: Options are listed in order from highest to lowest total weighted score with rank positions (e.g., #1, #2).
- [ ] FT-07: Rename criterion and option
  - Action: Click the edit name button on an existing criterion and an existing option, input new names, and confirm.
  - Expected: Both the criterion and option immediately display their new names across the matrix and ranking views.
- [ ] FT-08: Reorder criteria
  - Action: Use the reorder control (drag handle or move up/down arrows) to change the position of a criterion.
  - Expected: The criterion moves to the new position in both the criteria list and the comparison table columns/rows.
- [ ] FT-09: Reorder options
  - Action: Use the reorder control (drag handle or move up/down arrows) to change the manual display order of options.
  - Expected: The option moves to the target position in the comparison table.
- [ ] FT-10: Remove criterion and option
  - Action: Click the "Delete" button on an existing criterion and an existing option, and confirm deletion.
  - Expected: The selected criterion and option are removed from the page, and the remaining options' weighted scores and ranks recalculate accordingly.

## Constraint
- [ ] CS-01: Validate required name fields
  - Action: Clear the name field of the topic, a criterion, or an option and attempt to save.
  - Expected: The system prevents saving and displays a validation message indicating the field cannot be empty.
- [ ] CS-02: Validate criterion weight input
  - Action: Enter a negative number or non-numeric characters (e.g., "-2", "abc") into a criterion weight field and attempt to submit.
  - Expected: The input is rejected with an error message indicating weight must be a positive number.
- [ ] CS-03: Validate score input boundaries
  - Action: Enter a non-numeric character or out-of-range value into an option's score field.
  - Expected: The input is rejected or flagged with an error preventing calculation with invalid data.
- [ ] CS-04: Preserve calculation integrity on criterion deletion
  - Action: Delete a criterion that has assigned weights and existing scores across multiple options.
  - Expected: The removed criterion is excluded from calculations, and all options' weighted totals update immediately without data corruption.

## Interaction
- [ ] IX-01: Real-time dynamic ranking reorder
  - Action: Increase a lower-ranked option's score such that its total weighted score exceeds the #1 ranked option.
  - Expected: The ranking list dynamically reorders in real-time, placing the updated option at #1 without requiring a page reload.
- [ ] IX-02: Deletion confirmation prompt
  - Action: Click the delete icon on any criterion or option that contains scores.
  - Expected: A confirmation modal or prompt appears warning that scores will be lost before permanently deleting.

## Content
- [ ] CT-01: Single-page comparison matrix display
  - Action: View the main application page.
  - Expected: The decision topic, criteria with weights, options with individual criterion scores, and total weighted scores are visible together in a clear, single-page matrix layout.
- [ ] CT-02: Ranking summary clarity
  - Action: Inspect the ranking section after scoring at least two options.
  - Expected: Each ranked entry clearly displays its rank position, option name, and final calculated score.