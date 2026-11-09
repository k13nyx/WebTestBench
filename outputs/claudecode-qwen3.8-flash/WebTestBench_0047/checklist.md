# Test Checklist

## Functionality
- [ ] FT-01: User can create/set a decision topic displayed on the page
  - Action: Enter a topic name (e.g., "Best Laptop to Buy") and confirm/commit it; reload not required
  - Expected: The topic title is displayed at the top of the comparison page
- [ ] FT-02: User can add comparison criteria
  - Action: Use the "Add Criterion" control to add a new criterion (e.g., "Price")
  - Expected: New criterion appears as a column/row in the scoring matrix with a name and weight field
- [ ] FT-03: User can assign a weight to each criterion
  - Action: Enter a numeric weight (e.g., 3) for an existing criterion
  - Expected: Weight value is saved and displayed next to that criterion
- [ ] FT-04: User can add multiple options to compare on a single page
  - Action: Click "Add Option" twice, naming each (e.g., "Option A", "Option B")
  - Expected: Both options appear in the same page's matrix/table — no navigation to another page required
- [ ] FT-05: User can enter a score per criterion for each option
  - Action: Fill the score cell at each option × criterion intersection (e.g., Option A / Price = 8)
  - Expected: Each entered score is displayed in its cell; every option has an input for every criterion
- [ ] FT-06: Weighted score is automatically calculated per option
  - Action: With 2 criteria (weights 3 and 1) and scores entered, view each option's weighted score
  - Expected: Weighted score equals Σ(score × weight) [e.g., scores 8 and 4 → (8×3)+(4×1) = 28]; no manual "calculate" step needed
- [ ] FT-07: A ranking of options is displayed based on weighted scores
  - Action: Give options differing weighted scores and view the ranking section
  - Expected: Options are listed in descending weighted-score order with rank positions (1st, 2nd, …); highest score is rank 1
- [ ] FT-08: User can rename both criteria and options
  - Action: Edit the name of one criterion and one option to new text
  - Expected: New names appear everywhere they are referenced (matrix headers, ranking list)
- [ ] FT-09: User can remove an option and a criterion
  - Action: Delete one option and one criterion using their remove controls
  - Expected: They disappear from the matrix, ranking, and totals; remaining rows/columns and scores stay correct
- [ ] FT-10: Default data is present on first load
  - Action: Open the page without creating anything
  - Expected: At least one topic, one criterion (with weight), one option, and score inputs are pre-populated and usable

## Constraint
- [ ] CS-01: Invalid score input is rejected or handled safely
  - Action: Enter non-numeric text (e.g., "abc") or a value outside the stated score scale (e.g., −5 or 999 if scale is 0–10) into a score cell
  - Expected: Input is rejected/clamped with a visible message or correction; weighted score never shows NaN/undefined/crash
- [ ] CS-02: Weight must be a valid number
  - Action: Set a criterion's weight to empty, text, or a negative value
  - Expected: Rejected or defaulted to a valid value; ranking and weighted scores never display NaN or break
- [ ] CS-03: Empty names are not accepted
  - Action: Attempt to add/rename an option or criterion with a blank name
  - Expected: Block the action with validation feedback; no blank-named row/column appears in ranking or matrix
- [ ] CS-04: System stays in a consistent state when entities are removed
  - Action: Remove the only remaining criterion (or option), then check weighted score and ranking
  - Expected: No stale scores/ranks referencing removed items; page shows an empty or "add criterion/option" state instead of errors
- [ ] CS-05: Weighted score and ranking always reflect current weights
  - Action: After scores are set, change a criterion's weight (e.g., 3 → 1)
  - Expected: Recomputed weighted scores match the new weights exactly; ranking order updates if positions change — no "Apply" button required

## Interaction
- [ ] IX-01: Results update live on any edit
  - Action: Change one score cell while watching the weighted score and ranking area
  - Expected: Weighted score and ranking re-render immediately after the edit (no page reload)
- [ ] IX-02: User can reorder options and criteria
  - Action: Use reorder controls (drag handles or move up/down buttons) to change the order of one option and one criterion
  - Expected: Display order changes for matrix columns/rows and ranking list; scores follow their rows/columns correctly after reorder
- [ ] IX-03: Clear visual feedback for add/rename/remove actions
  - Action: Add an option, rename a criterion, then remove an option
  - Expected: Each action produces visible confirmation (new row appears, name changes in place, row disappears — optionally with a toast); no ghost/stale UI left behind
- [ ] IX-04: Top-ranked option is visually distinguished
  - Action: View the ranking with at least two scored options
  - Expected: The #1 option is visibly highlighted (badge, color, or "Best choice" marker) so the user can identify the winner at a glance

## Content
- [ ] CT-01: Matrix and ranking content stay aligned with the decision theme
  - Action: Inspect the page with multiple criteria, options, and scores entered
  - Expected: Every displayed label (topic, criterion names, option names, weights, scores, ranks) matches what was entered — no placeholder text like "Lorem ipsum", "Criterion 1 (edit me)", or broken/empty fields
- [ ] CT-02: Weighted-score breakdown is transparent and relevant
  - Action: View the weighted score area for one option
  - Expected: The score shown corresponds to the actual criterion weights and scores on the page (spot-check one value by hand); no unrelated or hardcoded numbers