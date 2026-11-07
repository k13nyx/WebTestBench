All tests executed. The title reverted to "Buy a Laptop" (empty name was rejected/silently reverted, with no validation message). Let me compile the complete results.

# Test Result

## Functionality

- [X] FT-01: Create a decision topic
  - Action: Enter a topic name (e.g., "Buy a Laptop") into the topic field and confirm/create it.
  - Expected: The decision topic is saved and displayed as the page's active decision title.
  - Verified: Clicked **New Decision**, then edited the active title heading and entered "Buy a Laptop"; the h1 title now reads "Buy a Laptop" and is displayed as the active decision title.

- [X] FT-02: Define comparison criteria
  - Action: Use the add-criteria control to create at least two criteria (e.g., "Price", "Performance").
  - Expected: Each new criterion appears in the criteria list/grid on the page.
  - Verified: Added "Price" and "Performance" via the "Add new criterion…" field + Add button; both appear in the Criteria section and as table columns.

- [X] FT-03: Assign a weight to each criterion
  - Action: Enter a numeric weight value (e.g., 3) for each defined criterion.
  - Expected: Each criterion displays its assigned weight value.
  - Verified: Each criterion shows its assigned weight (e.g., 10%, 11%, 1%) next to the name and in the column header. Note: weights are configured via a **percentage slider (min 1%)**, not a free-form numeric field like "3"; the displayed/assigned weight value requirement is met.

- [X] FT-04: Add multiple options on a single page
  - Action: Use the add-option control to add at least two options (e.g., "Model A", "Model B").
  - Expected: All added options appear together on the same page without navigation.
  - Verified: Added "Model A" and "Model B" via "Add new option…" + Add Option; both render in the same Options & Scores table and Ranking section.

- [X] FT-05: Enter scores per criterion for each option
  - Action: For one option, enter a score in the cell corresponding to each criterion.
  - Expected: Each entered score is stored and displayed in its criterion/option cell.
  - Verified: Entered Model A scores (Price 8, Performance 6) and Model B scores (Price 5, Performance 9/10); values persisted in their respective spinner cells.

- [X] FT-06: View automatically calculated weighted score
  - Action: With weights and scores entered, view the score area for an option.
  - Expected: A weighted score (sum of score × weight per criterion) is displayed for the option without manual calculation.
  - Verified: Score cell computed automatically (e.g., Model A = 7.0, Model B = 7.4 / 10) with no manual calculate action.

- [X] FT-07: View a ranking of options
  - Action: With multiple options scored, view the ranking section.
  - Expected: Options are listed in ranked order (highest weighted score first) with rank positions shown.
  - Verified: Ranking section lists options ordered highest-first (e.g., Model B 7.4 then Model A 7.0). Note: rank is conveyed by list order (top item also gets a highlight/icon); explicit numeric "1/2/3" badges are not rendered.

- [X] FT-08: Rename an option
  - Action: Edit an option's name field (e.g., change "Model A" to "Model X") and save.
  - Expected: The option is displayed under its new name everywhere it appears.
  - Verified: Renamed "Model A" → "Model X"; the new name appears in both the Options table and the Ranking section.

- [X] FT-09: Reorder options
  - Action: Move an option up/down using the reorder control (drag or move button).
  - Expected: The option's position in the list/grid changes accordingly.
  - Verified: Clicked Model B's "move up" control; Model B moved above Model X in the table (Model B's up-button then became disabled as it is first).

- [X] FT-10: Remove an option
  - Action: Use the remove control on one option.
  - Expected: The option and its scores disappear from the page and ranking.
  - Verified: Removed "Model X"; it disappeared from the Options table and from the Ranking section.

- [X] FT-11: Rename a criterion
  - Action: Edit a criterion's name (e.g., change "Price" to "Cost") and save.
  - Expected: The criterion is displayed under its new name across all options.
  - Verified: Renamed "Price" → "Cost"; the new name appears in the Criteria list and as the table column header "Cost (11%)".

- [X] FT-12: Reorder criteria
  - Action: Move a criterion left/right or up/down using the reorder control.
  - Expected: The criterion's column/position updates and remains aligned with its scores.
  - Verified: Moved "Performance" left of "Cost"; column order updated to Performance(10%)→Cost(11%) and Model B's score cell (10) stayed aligned under Performance.

- [X] FT-13: Remove a criterion
  - Action: Use the remove control on one criterion.
  - Expected: The criterion and its score column are removed, and weighted scores/ranking recalculate.
  - Verified: Removed "Cost"; its column disappeared and Model B's weighted score recalculated from 7.4 → 10.0/10 (now only Performance remains at 1% weight).

## Constraint

- [ ] CS-01: Decision topic name is required
  - Action: Attempt to create a decision topic with an empty name field.
  - Expected: Submission is blocked and a "name required" message is shown; no topic is created.
  - Bug Report:
    - Issue: Missing validation message / incomplete required-field enforcement
    - Actual: Clearing the title and pressing Enter silently reverts to the previous name ("Buy a Laptop") — no empty topic is created, but **no "name required" message or error is displayed**. Additionally, the "New Decision" create action auto-generates a default name ("New Decision") and never prompts for or validates a required name, so the required-name rule is not enforced at creation time.

- [X] CS-02: Criterion weight must be a valid positive number
  - Action: Enter a non-numeric, zero, or negative value into a criterion weight field.
  - Expected: The invalid value is rejected (or an error is shown) and not accepted as a weight.
  - Verified: Weight is a range slider with no text entry, so non-numeric/negative input is impossible. Pressing Home (slider minimum) clamps to a **minimum of 1%**, so a zero/non-positive weight cannot be stored. Invalid values are rejected.

- [X] CS-03: Option score must be a valid number
  - Action: Enter a non-numeric value (e.g., text) into a score cell.
  - Expected: The invalid value is rejected (or an error is shown) and not stored as a score.
  - Verified: Score cells are `<input type="number" min="0" max="10">`. A `fill("abc")` is rejected by the control, and typing the letter "a" leaves the stored value unchanged ("10"); the invalid text is not stored.

## Interaction

- [X] IX-01: Weighted score recalculates automatically on input change
  - Action: Change a score or a criterion weight after scores exist.
  - Expected: The affected option's weighted score updates immediately without a manual "calculate" action.
  - Verified: Changed Model B's Performance score; its weighted score updated immediately (6.9 → 7.4 → 10.0) with no manual recalculation step.

- [X] IX-02: Ranking updates automatically on score/weight change
  - Action: Change a score or weight so that an option's weighted score overtakes another.
  - Expected: The ranking order updates immediately to reflect the new scores.
  - Verified: Raising Model B's score made it overtake Model A; the Ranking section reordered instantly (Model B moved to first).

## Content

- [X] CT-01: Page heading reflects the decision theme
  - Action: Create a topic named "Buy a Laptop" and view the page header.
  - Expected: The displayed page title/heading matches the created decision topic name.
  - Verified: The page's h1 heading reads "Buy a Laptop", matching the created decision topic.

- [X] CT-02: All section labels are present and correctly associated
  - Action: Inspect the page for criteria, options, weights, scores, and ranking areas.
  - Expected: Each section is clearly labeled and the labels correctly correspond to their data (e.g., score columns map to the right criteria).
  - Verified: Sections are labeled — "Criteria" (with "Total Weight: X%"), "Options & Scores" table ("Option", "Performance (1%)", "Score" headers), and "Ranking". Column headers include criterion name + weight (e.g., "Performance (1%)") and stay aligned with their score cells after rename/reorder/remove.

---

### Summary
- **Passed:** 18 / 19 items
- **Failed:** 1 item — **CS-01** (name-required rule is enforced only by silent revert, with no "name required" validation message, and the "New Decision" flow bypasses naming entirely).
- **Notable observations:** Weights are percentage-based (slider, min 1%), not arbitrary numeric weights; weighted score is a normalized weighted average out of 10; ranking conveys position by order rather than explicit numbered badges.