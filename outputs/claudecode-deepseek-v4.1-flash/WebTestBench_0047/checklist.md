# Test Checklist

## Functionality
- [ ] FT-01: User can create a decision topic.
  - Action: Enter a topic name (e.g., "Choose a laptop") and submit it.
  - Expected: The topic is created and its name appears as the heading of the page.

- [ ] FT-02: User can add a comparison criterion.
  - Action: In the topic, add a new criterion named e.g. "Price".
  - Expected: "Price" appears in the criteria list, ready for weighting.

- [ ] FT-03: User can assign a weight to each criterion.
  - Action: Set a weight value (e.g., 5) on the "Price" criterion.
  - Expected: The weight is saved and displayed next to "Price".

- [ ] FT-04: User can add multiple options to compare.
  - Action: Add two or more options (e.g., "Laptop A", "Laptop B").
  - Expected: All options appear as columns/rows on the same page, each linked to the criteria.

- [ ] FT-05: User can enter a score per criterion for each option.
  - Action: Enter a numeric score for "Laptop A" under "Price".
  - Expected: The score is stored for that option-criterion pair and remains visible.

- [ ] FT-06: A weighted score is calculated automatically for each option.
  - Action: Assign weights to criteria and enter scores for an option.
  - Expected: Each option shows an automatically calculated weighted score (sum of score × weight) with no manual calculation needed.

- [ ] FT-07: A ranking of options is displayed.
  - Action: After scores/weights are entered, view the ranking area.
  - Expected: All options are listed in order from highest to lowest weighted score.

- [ ] FT-08: User can rename an option.
  - Action: Rename "Laptop A" to "Laptop X".
  - Expected: The new name appears everywhere the old name appeared (headers, scores, ranking).

- [ ] FT-09: User can rename a criterion.
  - Action: Rename "Price" to "Cost".
  - Expected: The new name appears in the criteria list, score headers, and weights.

- [ ] FT-10: User can reorder options.
  - Action: Move "Laptop B" above "Laptop A".
  - Expected: The options display in the new order, with scores and weighted results preserved and correctly attached.

- [ ] FT-11: User can reorder criteria.
  - Action: Move "Cost" criterion above another criterion.
  - Expected: The criteria display in the new order, with weights and scores preserved.

- [ ] FT-12: User can remove an option.
  - Action: Delete "Laptop B".
  - Expected: "Laptop B" and all its scores are removed, and the ranking/weighted scores update to exclude it.

- [ ] FT-13: User can remove a criterion.
  - Action: Delete the "Cost" criterion.
  - Expected: "Cost" and its per-option scores are removed, and each option's weighted score recalculates without it.

## Constraint
- [ ] CS-01: A topic cannot be created without a name.
  - Action: Submit the topic field empty.
  - Expected: Submission is blocked and a validation message is shown; no empty-named topic is created.

- [ ] CS-02: A criterion or option cannot be added with an empty name.
  - Action: Add a criterion/option with a blank name.
  - Expected: The addition is blocked with a validation message; no blank-named entry appears.

- [ ] CS-03: Weights accept only valid numeric values.
  - Action: Enter a non-numeric or negative weight (e.g., "abc" or -1).
  - Expected: The invalid input is rejected and does not corrupt the weighted-score calculation.

- [ ] CS-04: Scores accept only valid numeric values within the allowed range.
  - Action: Enter a non-numeric or out-of-range score (e.g., "abc" or 999).
  - Expected: The invalid input is rejected/shown as an error; the weighted score is not computed from invalid data.

- [ ] CS-05: Weighted scores and ranking stay consistent when weights change.
  - Action: Change a criterion's weight after scores are entered.
  - Expected: Every option's weighted score and the ranking order recalculate to reflect the new weight.

## Interaction
- [ ] IX-01: Weighted scores and ranking update immediately on input change.
  - Action: Edit a score or weight value.
  - Expected: The affected option's weighted score and the ranking order refresh instantly without a manual "recalculate" or page reload.

## Content
- [ ] CT-01: All displayed text is relevant to building and comparing a decision.
  - Action: Review labels, headings, and any sample/default content on the page.
  - Expected: Text refers to decision topics, criteria, weights, scores, and rankings; no irrelevant or placeholder (e.g., "lorem ipsum") content is present.