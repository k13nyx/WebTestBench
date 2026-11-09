# Test Result

## Functionality

- [X] FT-01: Create and display a decision topic
  - Action: Enter a decision topic in the topic field and submit or confirm it.
  - Expected: The topic is saved and displayed as the decision title on the page.

- [X] FT-02: Add comparison criteria with weights
  - Action: Add at least two criteria and assign a weight to each.
  - Expected: Each criterion appears in the comparison area with its assigned weight.

- [X] FT-03: Add multiple options on the same page
  - Action: Add at least three options without navigating away from the decision page.
  - Expected: All options appear together in the comparison interface.

- [X] FT-04: Enter scores for every option and criterion
  - Action: Enter a score for each option under each available criterion.
  - Expected: Every score is displayed in the correct option-and-criterion cell.

- [X] FT-05: Calculate weighted scores automatically
  - Action: Enter valid weights and scores for multiple options.
  - Expected: A weighted score is automatically shown for each option and reflects its entered scores and criterion weights.

- [X] FT-06: Display an option ranking
  - Action: Complete scores for at least two options with different weighted scores.
  - Expected: A ranking is displayed with options ordered from highest weighted score to lowest weighted score.

- [X] FT-07: Rename an option
  - Action: Rename an existing option and confirm the change.
  - Expected: The new option name appears everywhere that option is shown, including its scores and ranking entry.

- [X] FT-08: Reorder options
  - Action: Move an option to a different position using the available reorder control.
  - Expected: The option appears in the new position while retaining its scores and weighted score.

- [X] FT-09: Remove an option
  - Action: Remove an existing option.
  - Expected: The option, its scores, weighted score, and ranking entry are removed from the page.

- [X] FT-10: Rename a criterion
  - Action: Rename an existing criterion and confirm the change.
  - Expected: The new criterion name appears in the criterion header and remains associated with its weight and scores.

- [X] FT-11: Reorder criteria
  - Action: Move a criterion to a different position.
  - Expected: The criterion appears in the new position while retaining its weight and all option scores.

- [X] FT-12: Remove a criterion
  - Action: Remove an existing criterion.
  - Expected: The criterion, its weight, and its score cells are removed, and each option’s weighted score and ranking are recalculated without that criterion.

## Constraint

- [X] CS-01: Keep option scores associated with the correct criterion
  - Action: Reorder or rename a criterion after entering scores for multiple options.
  - Expected: Each score remains associated with the same criterion and option; no score moves to a different criterion or option.

- [X] CS-02: Keep ranking consistent with weighted scores
  - Action: Change a score or criterion weight so that one option should rank above another.
  - Expected: The ranking order changes to match the updated weighted scores, with no option shown in an incorrect position.

- [X] CS-03: Prevent removed data from affecting calculations
  - Action: Remove an option or criterion after completing the comparison.
  - Expected: Removed options and criteria no longer contribute to any displayed weighted score or ranking.

## Interaction

- [X] IX-01: Update weighted scores after score changes
  - Action: Change a valid score for one option and criterion.
  - Expected: The affected option’s weighted score updates automatically without requiring a page refresh.

- [X] IX-02: Update weighted scores after weight changes
  - Action: Change the weight assigned to an existing criterion.
  - Expected: Weighted scores and the ranking update automatically to reflect the new weight.

- [X] IX-03: Preserve the comparison context during edits
  - Action: Rename, reorder, or remove an option or criterion while viewing the comparison page.
  - Expected: The page remains on the decision comparison view and visibly reflects the edit immediately.

## Content

- [X] CT-01: Display complete and correctly labeled comparison data
  - Action: Review the completed decision page and ranking.
  - Expected: The decision topic, criterion names, criterion weights, option names, entered scores, weighted scores, and ranking positions are all visible and correctly associated.