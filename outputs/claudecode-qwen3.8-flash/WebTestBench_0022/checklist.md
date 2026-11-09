# Test Checklist

## Functionality
- [ ] FT-01: Add pantry ingredient with quantity and expiration date
  - Action: In the "Add Ingredient" form, enter name "Spinach", quantity "200 g", expiration date "2026-11-10", and submit.
  - Expected: "Spinach" appears in the pantry list showing both "200 g" and "2026-11-10".

- [ ] FT-02: Expiration date is optional when adding an ingredient
  - Action: Add an ingredient with name "Rice" and quantity "1 kg", leaving the expiration date field empty, and submit.
  - Expected: Submission succeeds and "Rice" is listed with quantity "1 kg" and no expiration date (blank/"—"), with no error.

- [ ] FT-03: Generate a multi-day meal plan from the current pantry
  - Action: With the default pantry present, click "Generate Plan" for a 3-day span.
  - Expected: A plan renders covering 3 consecutive days, with at least one recipe assigned to each day.

- [ ] FT-04: Plan is displayed day-by-day with recipes per meal
  - Action: Inspect the generated plan section.
  - Expected: Days are shown as separate, labeled blocks (e.g., "Day 1 / Mon Nov 9"), each listing meals (Breakfast/Lunch/Dinner) with a named recipe under each.

- [ ] FT-05: Exact ingredient usage amounts are shown
  - Action: Open any recipe card in the plan and view its ingredient lines.
  - Expected: Each ingredient line shows a specific amount used (e.g., "Spinach — 100 g"), not just the ingredient name.

- [ ] FT-06: Grocery list is produced for missing/insufficient items
  - Action: After generating the plan, view the "Grocery List" section.
  - Expected: The list contains only items not available (or not available in sufficient quantity) in the pantry, each with a required amount.

- [ ] FT-07: Lock an individual meal
  - Action: Click the "Lock" control on one meal slot (e.g., Day 2 Dinner).
  - Expected: That meal is marked locked and its recipe assignment is retained.

- [ ] FT-08: Lock an entire day
  - Action: Click the "Lock Day" control on one day block (e.g., Day 1).
  - Expected: The day block is marked locked and all of its meal assignments are retained.

- [ ] FT-09: Regenerate the rest of the plan without starting over
  - Action: With one meal and one day locked, click "Regenerate Plan".
  - Expected: A new plan is produced for the unlocked days/meals; the plan remains a complete multi-day plan (no empty unlocked slots).

- [ ] FT-10: Simple preferences are applied to the generated plan
  - Action: Enable the "Vegetarian" and "Budget-friendly" preference toggles, then click "Generate Plan".
  - Expected: Every recipe in the plan is labeled/tagged as satisfying both selected preferences (no meat-containing or non-budget recipes appear).

## Constraint
- [ ] CS-01: Ingredient name and quantity are required
  - Action: Submit the "Add Ingredient" form with the name empty, then again with the quantity empty.
  - Expected: Both submissions are blocked with a validation message; no partial item is added to the pantry list.

- [ ] CS-02: Plan never uses more of an ingredient than the pantry holds
  - Action: Sum the per-recipe usage amounts for one constrained pantry item (e.g., "Spinach") across the whole plan and compare to the pantry quantity.
  - Expected: Total used ≤ quantity on hand; any shortfall appears only on the grocery list, and no ingredient shows a negative remaining amount.

- [ ] CS-03: Locked meals and locked days are immutable after regeneration
  - Action: With Day 1 locked and Day 3 Dinner locked, click "Regenerate Plan" twice.
  - Expected: The recipes assigned to Day 1 (all meals) and Day 3 Dinner are identical before and after each regeneration; only unlocked slots change.

- [ ] CS-04: Food closest to expiring is prioritized
  - Action: Ensure the pantry holds an expiring-soon item (expiration within the plan range) and an equivalent non-expiring item, then click "Generate Plan".
  - Expected: The soon-expiring item is used in the plan on or before its expiration date, and it is not displaced by the later-expiring/equivalent item.

## Interaction
- [ ] IX-01: Lock controls reflect state visibly and toggle back
  - Action: Click "Lock" on an unlocked meal, then click it again.
  - Expected: On the first click the control shows a locked state (e.g., filled lock icon / "Locked" label); on the second click it returns to the unlocked state with no page reload.

- [ ] IX-02: Generation gives immediate feedback and updates the view in place
  - Action: Click "Generate Plan" / "Regenerate Plan".
  - Expected: A busy/loading indication appears, followed by a success confirmation (e.g., toast or "Plan generated for 3 days"), and the plan + grocery list areas refresh without a full page reload.

- [ ] IX-03: Expiring-soon pantry items are flagged in the UI
  - Action: Load the page with default data and inspect the pantry list.
  - Expected: Items whose expiration date is within/near the plan window are visually flagged (e.g., "Use by Nov 10" warning style), while items with no date or distant dates are not flagged.

## Content
- [ ] CT-01: Default pantry data is present on load
  - Action: Open the page without adding anything.
  - Expected: The pantry list shows several pre-existing ingredients, each with a quantity, and at least one with an expiration date.

- [ ] CT-02: Recipe content is consistent with the displayed plan
  - Action: Compare the recipe name and ingredient list on each recipe card with the plan's meal assignment and usage amounts.
  - Expected: Every recipe shown has a real dish name and an ingredient list whose items/amounts match the usage figures reported for that recipe (no blank, "Recipe #N", or placeholder text).

- [ ] CT-03: Grocery list entries are relevant and non-duplicated
  - Action: Review the grocery list against the pantry and the plan.
  - Expected: Every entry is an ingredient actually required by a planned recipe and missing/short in the pantry; no item already fully covered by the pantry appears, and no ingredient is listed twice.