# Test Checklist

## Functionality
- [ ] FT-01: Create a decision topic
  - Action: Enter a topic name (e.g., "Buy a Laptop") into the topic field and confirm/create it.
  - Expected: The decision topic is saved and displayed as the page's active decision title.

- [ ] FT-02: Define comparison criteria
  - Action: Use the add-criteria control to create at least two criteria (e.g., "Price", "Performance").
  - Expected: Each new criterion appears in the criteria list/grid on the page.

- [ ] FT-03: Assign a weight to each criterion
  - Action: Enter a numeric weight value (e.g., 3) for each defined criterion.
  - Expected: Each criterion displays its assigned weight value.

- [ ] FT-04: Add multiple options on a single page
  - Action: Use the add-option control to add at least two options (e.g., "Model A", "Model B").
  - Expected: All added options appear together on the same page without navigation.

- [ ] FT-05: Enter scores per criterion for each option
  - Action: For one option, enter a score in the cell corresponding to each criterion.
  - Expected: Each entered score is stored and displayed in its criterion/option cell.

- [ ] FT-06: View automatically calculated weighted score
  - Action: With weights and scores entered, view the score area for an option.
  - Expected: A weighted score (sum of score × weight per criterion) is displayed for the option without manual calculation.

- [ ] FT-07: View a ranking of options
  - Action: With multiple options scored, view the ranking section.
  - Expected: Options are listed in ranked order (highest weighted score first) with rank positions shown.

- [ ] FT-08: Rename an option
  - Action: Edit an option's name field (e.g., change "Model A" to "Model X") and save.
  - Expected: The option is displayed under its new name everywhere it appears.

- [ ] FT-09: Reorder options
  - Action: Move an option up/down using the reorder control (drag or move button).
  - Expected: The option's position in the list/grid changes accordingly.

- [ ] FT-10: Remove an option
  - Action: Use the remove control on one option.
  - Expected: The option and its scores disappear from the page and ranking.

- [ ] FT-11: Rename a criterion
  - Action: Edit a criterion's name (e.g., change "Price" to "Cost") and save.
  - Expected: The criterion is displayed under its new name across all options.

- [ ] FT-12: Reorder criteria
  - Action: Move a criterion left/right or up/down using the reorder control.
  - Expected: The criterion's column/position updates and remains aligned with its scores.

- [ ] FT-13: Remove a criterion
  - Action: Use the remove control on one criterion.
  - Expected: The criterion and its score column are removed, and weighted scores/ranking recalculate.

## Constraint
- [ ] CS-01: Decision topic name is required
  - Action: Attempt to create a decision topic with an empty name field.
  - Expected: Submission is blocked and a "name required" message is shown; no topic is created.

- [ ] CS-02: Criterion weight must be a valid positive number
  - Action: Enter a non-numeric, zero, or negative value into a criterion weight field.
  - Expected: The invalid value is rejected (or an error is shown) and not accepted as a weight.

- [ ] CS-03: Option score must be a valid number
  - Action: Enter a non-numeric value (e.g., text) into a score cell.
  - Expected: The invalid value is rejected (or an error is shown) and not stored as a score.

## Interaction
- [ ] IX-01: Weighted score recalculates automatically on input change
  - Action: Change a score or a criterion weight after scores exist.
  - Expected: The affected option's weighted score updates immediately without a manual "calculate" action.

- [ ] IX-02: Ranking updates automatically on score/weight change
  - Action: Change a score or weight so that an option's weighted score overtakes another.
  - Expected: The ranking order updates immediately to reflect the new scores.

## Content
- [ ] CT-01: Page heading reflects the decision theme
  - Action: Create a topic named "Buy a Laptop" and view the page header.
  - Expected: The displayed page title/heading matches the created decision topic name.

- [ ] CT-02: All section labels are present and correctly associated
  - Action: Inspect the page for criteria, options, weights, scores, and ranking areas.
  - Expected: Each section is clearly labeled and the labels correctly correspond to their data (e.g., score columns map to the right criteria).