# Test Checklist

## Functionality
- [ ] FT-01: Create a decision topic with a name
  - Action: Enter a topic name (e.g., "Choose a laptop") in the topic field and confirm with the Add/Save button.
  - Expected: The topic name is accepted, appears as the page heading/section title, and a criteria area is available for the new topic.

- [ ] FT-02: Add multiple comparison criteria to the topic
  - Action: Add criteria named "Price", "Performance", and "Battery" using the add-criterion control (repeat three times).
  - Expected: Each new criterion appears as a separate row/column entry with its name, weight field, and score inputs; no entry overwrites another.

- [ ] FT-03: Assign a weight to each criterion
  - Action: Set weights to 50 for Price, 30 for Performance, and 20 for Battery.
  - Expected: Each criterion displays its entered weight next to it and the value is retained for use in scoring.

- [ ] FT-04: Add multiple options to compare
  - Action: Add three options named "Budget", "Mid-range", and "Flagship" (use the app's preloaded options if any exist, otherwise add these).
  - Expected: All three options appear in the comparison area with a score input per criterion and a score/total field; all are on the same page without navigation.

- [ ] FT-05: Enter scores per criterion for each option
  - Action: For Budget enter 8/6/10, for Mid-range enter 6/7/7, and for Flagship enter 4/9/5 against Price/Performance/Battery respectively.
  - Expected: Each entered value stays in its own option × criterion cell; no value bleeds into other rows or columns.

- [ ] FT-06: Weighted score is calculated automatically per option
  - Action: Observe the weighted score shown for Budget after entering 8, 6, and 10 with weights 50/30/20.
  - Expected: Budget shows a weighted score of 7.8 (0.5×8 + 0.3×6 + 0.2×10, displayed as 7.8 or 78%) without any manual calculation step or extra button press.

- [ ] FT-07: Ranking of options is displayed
  - Action: View the ranking area after all scores are entered.
  - Expected: Options are listed in descending weighted-score order (Flagship 6.3, Budget 7.8 → Budget first, then Mid-range 6.7, then Flagship 6.3) with a rank number/position for each.

- [ ] FT-08: Rename an option
  - Action: Change the option named "Budget" to "Cheap model" using its rename/edit control and save.
  - Expected: The new name appears in the option's score row, in the ranking list, and anywhere else the option is referenced; the old name is gone.

- [ ] FT-09: Rename a criterion
  - Action: Change the criterion "Battery" to "Battery life" and save.
  - Expected: The new name appears as the criterion header/label for all options' score inputs, and its weight and scores remain attached to it.

- [ ] FT-10: Reorder options
  - Action: Use the move up / move down control on the "Flagship" option.
  - Expected: The option changes position in the comparison list (and its ranking/row position updates accordingly), with the other options keeping their relative order.

- [ ] FT-11: Reorder criteria
  - Action: Use the move up / move down control on the "Battery" criterion.
  - Expected: The criterion's column/label moves to the new position and all options' scores stay aligned with the correct criterion.

- [ ] FT-12: Remove an option
  - Action: Click the delete/remove control on the "Mid-range" option and confirm.
  - Expected: The option disappears from the comparison area and from the ranking, its scores are cleared, and the remaining options are re-ranked.

- [ ] FT-13: Remove a criterion
  - Action: Click the delete/remove control on the "Performance" criterion and confirm.
  - Expected: The criterion and its score column are removed for every option, and weighted scores and the ranking are recalculated from the remaining criteria.

## Constraint
- [ ] CS-01: Duplicate option names are rejected
  - Action: Try to add a second option named "Flagship" while one already exists.
  - Expected: The duplicate is either rejected with a visible message or auto-renamed; two distinct rows never share the same name.

- [ ] CS-02: Invalid score input is rejected or clamped
  - Action: Enter a non-numeric value and an out-of-range value (e.g., 500 and "-2") into an option's score field.
  - Expected: The invalid entry is rejected with a visible error, or clamped to the allowed range; the weighted score and ranking never show NaN, blank, or a negative contribution.

- [ ] CS-03: Removing a criterion leaves no orphaned data
  - Action: Remove a criterion and inspect every remaining option's score cells and weighted score.
  - Expected: No empty column, stale value, or leftover score from the deleted criterion remains; each remaining option has exactly one score per surviving criterion.

## Interaction
- [ ] IX-01: Weighted scores recalculate live when a score changes
  - Action: Change the Budget option's Price score from 8 to 2 and observe the weighted score and ranking without clicking any save/calculate button.
  - Expected: The weighted score updates immediately (7.8 → 5.8) and the ranking reorders without a page reload.

- [ ] IX-02: Ranking updates immediately when weights change
  - Action: Change the Price weight from 50 to 90 and observe the weighted scores and the ranking order.
  - Expected: Weighted scores and ranking positions update in place immediately, with no stale values left from the previous weights.

## Content
- [ ] CT-01: Topic title matches what the user entered
  - Action: Compare the heading/label displayed on the page with the topic name typed in FT-01.
  - Expected: The displayed title is exactly the entered topic name, with no placeholder, generic "Untitled", or truncated text.

- [ ] CT-02: Entered names, weights, scores and ranks are displayed accurately
  - Action: Compare every visible criterion name, option name, weight value, entered score, weighted score, and rank number against what was typed/expected.
  - Expected: All text matches exactly (no ellipses, mojibake, off-by-one rank numbering, or weights/score values differing from the entered ones), and no leftover sample/placeholder text remains.