# Test Checklist

## Functionality
- [ ] FT-01: Add a pantry ingredient with name and quantity.
  - Action: Click "Add Ingredient", enter "Rice" with quantity "500 g", and confirm.
  - Expected: "Rice — 500 g" appears in the pantry list.

- [ ] FT-02: Add an expiration date to a pantry ingredient.
  - Action: Edit pantry item "Rice" and set expiration date to a date 2 days from today.
  - Expected: The item displays the entered expiration date.

- [ ] FT-03: Edit and delete pantry items.
  - Action: Change quantity of "Rice" to "300 g", then delete the item.
  - Expected: Quantity updates to "300 g"; after deletion the item is removed from the pantry list.

- [ ] FT-04: Generate a multi-day meal plan from pantry contents.
  - Action: Click "Generate Meal Plan" (e.g., for 3 days) with pantry items populated.
  - Expected: A day-by-day plan is displayed with at least one recipe per day, covering the requested number of days.

- [ ] FT-05: Select a dietary preference and generate a matching plan.
  - Action: Select the "Vegetarian" preference and generate the meal plan.
  - Expected: Every recipe in the plan is labeled/flagged as vegetarian.

- [ ] FT-06: High-protein and budget-friendly preferences are selectable and applied.
  - Action: Select "High-protein", generate the plan; then select "Budget-friendly" and regenerate.
  - Expected: Each generated plan contains recipes tagged with the selected preference.

- [ ] FT-07: Show exact per-ingredient usage amounts for each recipe.
  - Action: Expand any recipe in the generated plan.
  - Expected: Each ingredient lists the exact amount used (e.g., "Rice: 150 g"), not just the ingredient name.

- [ ] FT-08: Generate a grocery list of missing items.
  - Action: Generate a meal plan and open the "Grocery List" section.
  - Expected: The list contains only items needed by the plan but absent (or insufficient) in the pantry, with required quantities.

- [ ] FT-09: Lock a single meal and regenerate the rest.
  - Action: Click the lock control on one recipe in Day 1, then click "Regenerate".
  - Expected: The locked recipe remains unchanged; all unlocked meals are replaced with new recipes.

- [ ] FT-10: Lock an entire day and regenerate the rest.
  - Action: Lock all meals of Day 2 (or use the day-level lock control), then regenerate.
  - Expected: Day 2's recipes are unchanged; other days are regenerated.

## Constraint
- [ ] CS-01: Cannot add an ingredient without a name or quantity.
  - Action: Click "Add Ingredient" and confirm with empty name and/or empty quantity fields.
  - Expected: The ingredient is not added and a validation message appears; the form remains open.

- [ ] CS-02: Cannot add an ingredient with a non-positive or invalid quantity.
  - Action: Enter quantity "-5" and "0" (and non-numeric text) for a new ingredient.
  - Expected: Each input is rejected with a validation message; no item is added.

- [ ] CS-03: Pantry usage never exceeds available quantity across the plan.
  - Action: Generate a plan with a limited-quantity pantry item (e.g., "Eggs: 2") and total the usage shown per recipe.
  - Expected: Total planned usage of any ingredient never exceeds its pantry quantity; any excess appears in the grocery list instead.

- [ ] CS-04: Plan generation is blocked when the pantry is empty.
  - Action: Delete all pantry items and click "Generate Meal Plan".
  - Expected: No plan is generated and a message prompts the user to add pantry items first.

- [ ] CS-05: Locked meals/days cannot be changed by regeneration.
  - Action: Lock a meal, click "Regenerate" multiple times.
  - Expected: The locked meal's recipe and ingredient usage stay identical across every regeneration.

## Interaction
- [ ] IX-01: Indication of food close to expiring prioritized in the plan.
  - Action: Set one pantry item's expiration date to 1–2 days from today and generate the plan.
  - Expected: The near-expiry item is used in the earliest day(s) of the plan and is visually flagged (e.g., "expiring soon" badge/label) in the pantry and/or plan.

- [ ] IX-02: Lock state is visually distinguishable and toggleable.
  - Action: Click the lock control on a meal; observe it; click again to unlock.
  - Expected: Locked meals show a clear locked indicator (e.g., lock icon/label); unlocking removes it.

- [ ] IX-03: Preference change is reflected after regeneration.
  - Action: Generate a plan, change preference from "None" to "Budget-friendly", regenerate.
  - Expected: The displayed plan visibly updates and recipes show the new preference tag.

- [ ] IX-04: Regenerate action confirms completion.
  - Action: Click "Regenerate" on the plan.
  - Expected: The interface indicates regeneration completed (e.g., updated plan content or a brief confirmation), without errors.

## Content
- [ ] CT-01: Recipes in the plan are relevant meal recipes with required details.
  - Action: Review each recipe in the generated plan.
  - Expected: Every entry shows a real meal name, an ingredient list with quantities, and preference tags matching the theme (vegetarian/high-protein/budget-friendly) — no unrelated or placeholder text.

- [ ] CT-02: Pantry list displays accurate name, quantity, and expiration data.
  - Action: Compare each pantry entry against the data entered when added.
  - Expected: Each entry shows exactly the entered name, quantity, and expiration date (or "No expiration" when omitted), with no truncation or mismatch.

- [ ] CT-03: Grocery list entries match missing items with correct quantities.
  - Action: Cross-check grocery list items against pantry contents and recipe usage.
  - Expected: Every grocery item is genuinely missing/short in the pantry, and its quantity equals the plan's total need minus pantry stock.