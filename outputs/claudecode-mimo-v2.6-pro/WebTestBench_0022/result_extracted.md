# Test Result

## Functionality
- [X] FT-01: Add a pantry ingredient with name and quantity.
  - Action: Click "Add Ingredient", enter "Rice" with quantity "500 g", and confirm.
  - Expected: "Rice — 500 g" appears in the pantry list.

- [ ] FT-02: Add an expiration date to a pantry ingredient.
  - Action: Edit pantry item "Rice" and set expiration date to a date 2 days from today.
  - Expected: The item displays the entered expiration date.
  - Bug Report:
    - Issue: Missing Edit Functionality (expiration date cannot be set on an existing item)
    - Actual: Pantry rows expose only a single delete (trash) button; there is no edit control, and clicking the row/name does nothing. The expiration date of the existing "Rice" item therefore cannot be edited. (Workaround evidence: setting an expiration at add time is possible, but the entered date "2026-11-10" is displayed only as a relative "2 days" badge, not the entered date.)

- [ ] FT-03: Edit and delete pantry items.
  - Action: Change quantity of "Rice" to "300 g", then delete the item.
  - Expected: Quantity updates to "300 g"; after deletion the item is removed from the pantry list.
  - Bug Report:
    - Issue: Missing Edit Functionality (quantity update not possible)
    - Actual: The quantity of "Rice" cannot be changed to "300 g" — pantry items have no edit UI (only a delete button; row click does nothing). Deletion itself works: clicking the trash button removes the item from the list (verified repeatedly).

- [X] FT-04: Generate a multi-day meal plan from pantry contents.
  - Action: Click "Generate Meal Plan" (e.g., for 3 days) with pantry items populated.
  - Expected: A day-by-day plan is displayed with at least one recipe per day, covering the requested number of days.

- [ ] FT-05: Select a dietary preference and generate a matching plan.
  - Action: Select the "Vegetarian" preference and generate the meal plan.
  - Expected: Every recipe in the plan is labeled/flagged as vegetarian.
  - Bug Report:
    - Issue: Missing Preference Label/Flag on Recipes
    - Actual: With "Vegetarian" enabled the plan does filter to vegetarian recipes (Greek Yogurt Parfait, Tomato Pasta Primavera, Spinach & Cheese Quesadilla), but no recipe is labeled/flagged as vegetarian anywhere — each card shows only the meal-slot badge ("Breakfast"/"Lunch"/"Dinner") and no tag text.

- [ ] FT-06: High-protein and budget-friendly preferences are selectable and applied.
  - Action: Select "High-protein", generate the plan; then select "Budget-friendly" and regenerate.
  - Expected: Each generated plan contains recipes tagged with the selected preference.
  - Bug Report:
    - Issue: Missing Preference Tags on Recipes
    - Actual: Both toggles are selectable and do change plan content (High-protein produced an egg-heavy plan: Bell Pepper Egg Cups, Cheesy Scrambled Eggs on Toast; Budget-friendly produced Greek Yogurt Parfait, Chicken Rice Bowl, Garlic Chicken Stir-Fry, Tomato Pasta Primavera), but no recipe in either plan displays a tag with the selected preference — recipe cards contain no tags at all.

- [ ] FT-07: Show exact per-ingredient usage amounts for each recipe.
  - Action: Expand any recipe in the generated plan.
  - Expected: Each ingredient lists the exact amount used (e.g., "Rice: 150 g"), not just the ingredient name.
  - Bug Report:
    - Issue: Non-Expandable Recipe Card / Missing Recipe Ingredient List
    - Actual: Recipe cards cannot be expanded — clicking a card produces no change and no expand button/chevron exists. The card shows only name, description, time, servings and an "N items" count (e.g., "5 items") with no per-ingredient amounts. Per-recipe amounts ("Chicken Rice Bowl: 300 g") appear only in the aggregate "Ingredient Usage" panel grouped by ingredient, not as a recipe's own ingredient list.

- [X] FT-08: Generate a grocery list of missing items.
  - Action: Generate a meal plan and open the "Grocery List" section.
  - Expected: The list contains only items needed by the plan but absent (or insufficient) in the pantry, with required quantities.

- [ ] FT-09: Lock a single meal and regenerate the rest.
  - Action: Click the lock control on one recipe in Day 1, then click "Regenerate".
  - Expected: The locked recipe remains unchanged; all unlocked meals are replaced with new recipes.
  - Bug Report:
    - Issue: Incomplete Regeneration (not all unlocked meals replaced)
    - Actual: The locked Day 1 recipe remained identical across every regeneration, but unlocked meals were not all replaced: in 3 consecutive regenerations 2 of 8 unlocked slots kept the identical recipe (Day 2 & Day 3 Breakfast stayed "Greek Yogurt Parfait" every time while Budget-friendly was on — these slots never changed across ~7 samples), and in a no-preference run 2 of 8 unlocked slots again repeated ("Chicken Rice Bowl" in Day 1 Dinner and Day 2 Lunch).

- [X] FT-10: Lock an entire day and regenerate the rest.
  - Action: Lock all meals of Day 2 (or use the day-level lock control), then regenerate.
  - Expected: Day 2's recipes are unchanged; other days are regenerated.

## Constraint
- [ ] CS-01: Cannot add an ingredient without a name or quantity.
  - Action: Click "Add Ingredient" and confirm with empty name and/or empty quantity fields.
  - Expected: The ingredient is not added and a validation message appears; the form remains open.
  - Bug Report:
    - Issue: Missing Validation Message
    - Actual: Clicking "Add to Pantry" with empty name and quantity silently does nothing — the item is not added and the form remains open, but no validation message appears anywhere (no inline error text, no role="alert" element, no toast/notification, no aria-invalid marking on the fields).

- [ ] CS-02: Cannot add an ingredient with a non-positive or invalid quantity.
  - Action: Enter quantity "-5" and "0" (and non-numeric text) for a new ingredient.
  - Expected: Each input is rejected with a validation message; no item is added.
  - Bug Report:
    - Issue: Invalid Quantity Accepted / Missing Validation Message
    - Actual: Entering quantity "-5" and confirming adds the item successfully with "‑5 g" displayed in the pantry list — the negative quantity is neither rejected nor flagged with a validation message. Quantity "0" is silently rejected (item not added, dialog stays open) but with no validation message; non-numeric text cannot even be typed into the number input (no message either).

- [X] CS-03: Pantry usage never exceeds available quantity across the plan.
  - Action: Generate a plan with a limited-quantity pantry item (e.g., "Eggs: 2") and total the usage shown per recipe.
  - Expected: Total planned usage of any ingredient never exceeds its pantry quantity; any excess appears in the grocery list instead.

- [ ] CS-04: Plan generation is blocked when the pantry is empty.
  - Action: Delete all pantry items and click "Generate Meal Plan".
  - Expected: No plan is generated and a message prompts the user to add pantry items first.
  - Bug Report:
    - Issue: Missing Empty-Pantry Guard (Incorrect Form/Flow Submission)
    - Actual: After deleting every pantry item (pantry shows "Your pantry is empty. Add some items to get started!"), clicking the plan-generation button still created a full 3-day plan, confirmed by the toast "Meal Plan Generated! Created 3-day plan with 3 locked meals preserved." No plan was blocked and no message prompting to add pantry items first appeared. (Note: the button was labeled "Regenerate Plan" since a prior plan existed — the app offers no way to clear a plan without a page refresh.)

- [X] CS-05: Locked meals/days cannot be changed by regeneration.
  - Action: Lock a meal, click "Regenerate" multiple times.
  - Expected: The locked meal's recipe and ingredient usage stay identical across every regeneration.

## Interaction
- [ ] IX-01: Indication of food close to expiring prioritized in the plan.
  - Action: Set one pantry item's expiration date to 1–2 days from today and generate the plan.
  - Expected: The near-expiry item is used in the earliest day(s) of the plan and is visually flagged (e.g., "expiring soon" badge/label) in the pantry and/or plan.
  - Bug Report:
    - Issue: No Expiry-Based Prioritization in Plan / Missing "Expiring Soon" Indication
    - Actual: With "Fresh Berries" (200 g, expiration 2026-11-10, i.e., 2 days out) in the pantry, no generated plan ever uses the item — it appears in no recipe and in no Ingredient Usage entry on any day, so it is not used in the earliest day(s) or anywhere else. The pantry shows only a relative "2 days" countdown badge and the plan shows no expiry flags at all (no "expiring soon" label in pantry or plan). Note: an existing item's expiration could not be set (no edit UI, see FT-02), so the date had to be provided when adding the item.

- [X] IX-02: Lock state is visually distinguishable and toggleable.
  - Action: Click the lock control on a meal; observe it; click again to unlock.
  - Expected: Locked meals show a clear locked indicator (e.g., lock icon/label); unlocking removes it.

- [ ] IX-03: Preference change is reflected after regeneration.
  - Action: Generate a plan, change preference from "None" to "Budget-friendly", regenerate.
  - Expected: The displayed plan visibly updates and recipes show the new preference tag.
  - Bug Report:
    - Issue: Missing Preference Tag on Recipes
    - Actual: The plan visibly updates after switching from no preference to "Budget-friendly" and regenerating (e.g., Day 1 changes from Bell Pepper Egg Cups / Chicken Rice Bowl / Garlic Chicken Stir-Fry to Greek Yogurt Parfait / Garlic Chicken Stir-Fry / Chicken Rice Bowl), but the recipes show no "budget-friendly" preference tag — recipe cards display no preference tags whatsoever.

- [X] IX-04: Regenerate action confirms completion.
  - Action: Click "Regenerate" on the plan.
  - Expected: The interface indicates regeneration completed (e.g., updated plan content or a brief confirmation), without errors.

## Content
- [ ] CT-01: Recipes in the plan are relevant meal recipes with required details.
  - Action: Review each recipe in the generated plan.
  - Expected: Every entry shows a real meal name, an ingredient list with quantities, and preference tags matching the theme (vegetarian/high-protein/budget-friendly) — no unrelated or placeholder text.
  - Bug Report:
    - Issue: Incomplete Recipe Details (no ingredient list with quantities, no preference tags)
    - Actual: Entries show real meal names and descriptions (e.g., "Chicken Rice Bowl — Simple and satisfying rice bowl with seasoned chicken", no placeholder text), but only an "N items" count instead of an ingredient list with quantities, and no vegetarian/high-protein/budget-friendly preference tags on any entry.

- [ ] CT-02: Pantry list displays accurate name, quantity, and expiration data.
  - Action: Compare each pantry entry against the data entered when added.
  - Expected: Each entry shows exactly the entered name, quantity, and expiration date (or "No expiration" when omitted), with no truncation or mismatch.
  - Bug Report:
    - Issue: Incorrect Expiration Display / Missing "No expiration" Indicator
    - Actual: The item added as name "Fresh Berries", quantity "200 g", expiration "2026-11-10" shows the name and quantity correctly but displays only a relative "2 days" badge instead of the entered expiration date; items added without a date (e.g., "Rice — 1000 g", "Pasta — 500 g", "Olive Oil — 500 ml") show no "No expiration" indicator at all (only name and quantity).

- [X] CT-03: Grocery list entries match missing items with correct quantities.
  - Action: Cross-check grocery list items against pantry contents and recipe usage.
  - Expected: Every grocery item is genuinely missing/short in the pantry, and its quantity equals the plan's total need minus pantry stock.
