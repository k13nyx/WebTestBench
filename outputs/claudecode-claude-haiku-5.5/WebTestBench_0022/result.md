Testing is complete: 4 items pass and 16 fail. Notes on how I ran it:

- The app's labels differ from the checklist: the form submits via "Add to Pantry" (not "Save"), and the plan buttons read "Generate Meal Plan" / "Regenerate Plan".
- For FT-03 I turned off the default "Budget Friendly" preference to match "no preferences".
- A test item, "QA Test Item" (1 g), was added to the pantry (FT-02) and is still there.
- My first CS-04 attempt used a faulty selector and accidentally triggered a Regenerate; that does not count as a result. The valid CS-04 run is the one reported.
- Lock toggles were driven by script, because the lock buttons carry no visible text.

# Test Result

## Functionality

- [ ] FT-01: Pantry list shows each ingredient's name, quantity, and expiration date.
  - Action: Open the Pantry page and review the default ingredient rows.
  - Expected: Each row shows name, quantity with unit, and expiration date. Items with no expiration show "No expiration" or a blank date, with no error.
  - Bug Report:
    - Issue: Missing Expiration Date Display
    - Actual: Every pantry row shows only name and quantity (e.g., "Chicken Breast / 500 g" with an "Expired" or no badge). No expiration date text appears in any row; a DOM text search of the Pantry panel found no dates.
- [X] FT-02: User can add a pantry ingredient with quantity and optional expiration date.
  - Action: Click "Add Ingredient", enter a name, quantity 1, and leave Expiration empty. Click "Save".
  - Expected: A new row appears in the pantry list with quantity 1 and no expiration date.
- [X] FT-03: Generated plan shows day-by-day meals, each with a named recipe.
  - Action: Set plan length to 3 days, select no preferences, and click "Generate Plan".
  - Expected: Day 1, Day 2, and Day 3 sections appear. Each has Breakfast, Lunch, and Dinner slots, and each slot shows a recipe name.
- [ ] FT-04: Ingredients closest to expiry are used in the earliest meals.
  - Action: Note the default pantry item with the earliest expiration date. Generate a 3-day plan.
  - Expected: That ingredient appears in a Day 1 recipe, and it is used before items with later expiration dates.
  - Bug Report:
    - Issue: Expiry Priority Not Verifiable
    - Actual: Expiration dates are not rendered or present in the DOM, so the earliest-expiring default item cannot be identified. Day 1 recipes (Cheesy Scrambled Eggs on Toast, Bell Pepper Egg Cups) consume items labeled "Expired" (Eggs, Milk, Bread, Cheese), so the priority ordering cannot be confirmed.
- [ ] FT-05: Each recipe lists the exact amount of each ingredient it uses.
  - Action: Click the Day 1 Dinner recipe.
  - Expected: Each ingredient shows a specific quantity and unit, such as "Eggs: 2 pcs". The amount does not exceed the pantry quantity.
  - Bug Report:
    - Issue: Recipe Ingredient Details Missing
    - Actual: Clicking the Day 1 Dinner recipe ("Tomato Pasta Primavera") heading or its "6 items" indicator changed nothing. No dialog or ingredient list with quantities appeared; the card text stayed "Dinner / Tomato Pasta Primavera / Classic pasta with fresh tomatoes and herbs / 30m / 4 / 6 items".
- [ ] FT-06: Grocery list shows missing and insufficient ingredients with the shortfall amount.
  - Action: Generate a 3-day plan and open the "Grocery List" tab.
  - Expected: Each ingredient the plan needs beyond pantry stock is listed with its shortfall quantity. Fully stocked ingredients are not listed.
- [ ] FT-07: Vegetarian preference limits the plan to vegetarian recipes.
  - Action: Check "Vegetarian" and click "Generate Plan".
  - Expected: Every recipe in the plan is labeled "Vegetarian", and no meal slot shows a recipe with meat or fish.
  - Bug Report:
    - Issue: Missing Vegetarian Label
    - Actual: With Vegetarian on, the regenerated plan contains only meat- and fish-free recipes (Cheesy Scrambled Eggs on Toast, Tomato Pasta Primavera, Spinach & Cheese Quesadilla, Bell Pepper Egg Cups), but no recipe card displays a "Vegetarian" label; a DOM text search for "Vegetarian" in the plan panel returned only the preference toggle.
- [ ] FT-08: Locked meals and days are kept when the plan is regenerated.
  - Action: Click the lock icon on Day 1 Breakfast and on the Day 2 header. Click "Regenerate".
  - Expected: Day 1 Breakfast and all Day 2 meals keep the same recipes and amounts. Other unlocked meals change.
  - Bug Report:
    - Issue: Missing Day-Level Lock Control
    - Actual: The "Day 2" header (and every day header) has no lock control; only per-meal "Lock meal" buttons exist, so the Day 2 lock could not be performed. Partial check: with Day 1 Breakfast locked and Regenerate clicked, "Cheesy Scrambled Eggs on Toast" was kept while unlocked meals changed (e.g., Day 1 Lunch: Garlic Chicken Stir-Fry → Chicken Rice Bowl).
- [ ] FT-09: Regenerating updates unlocked meals and the grocery list to match.
  - Action: Note the grocery list. Lock Day 1, then click "Regenerate".
  - Expected: Day 2 and Day 3 meals change. The grocery list reflects only the new unlocked recipes' shortfalls.
  - Bug Report:
    - Issue: Missing Day-Level Lock Control
    - Actual: Day headers have no lock control, so "Lock Day 1" cannot be performed as specified. Only individual meals can be locked; the per-meal locking and regeneration behavior is covered under FT-08.

## Constraint

- [ ] CS-01: Pantry form rejects an empty name or a non-positive quantity.
  - Action: Click "Add Ingredient", leave Name empty, enter quantity 0, and click "Save". Then enter quantity -1 and click "Save".
  - Expected: An error message appears for each invalid field ("Name is required", "Quantity must be greater than 0"). The item is not saved.
  - Bug Report:
    - Issue: Missing Form Validation Messages
    - Actual: With Name empty and Quantity 0, clicking "Add to Pantry" left the "Add Pantry Item" dialog open with no error text. With Name empty and Quantity -1, the result was the same. Neither "Name is required" nor "Quantity must be greater than 0" appeared, and no pantry row was added.
- [ ] CS-02: Planned usage never exceeds the pantry quantity for any ingredient.
  - Action: Generate a 7-day plan. Add up each ingredient's usage across all days.
  - Expected: The total used for each ingredient is less than or equal to its pantry quantity. Any remainder needed appears on the grocery list.
  - Bug Report:
    - Issue: Planned Usage Exceeds Pantry Quantity
    - Actual: In the 7-day plan, the summed per-recipe amounts far exceed pantry stock: Chicken Breast 4600 g planned vs 500 g in pantry; Rice 3600 g vs 1000 g; Eggs 32 pcs vs 12 pcs. The Ingredient Usage section shows "500 / 4600 g" for Chicken Breast, and the remainder appears on the grocery list only as a "Need to buy" figure.
- [ ] CS-03: Pantry items already past their expiration date are not used in the plan.
  - Action: Identify a default pantry item whose expiration date is before 2026-11-09. Generate a 3-day plan.
  - Expected: That item appears in no recipe, and it is labeled "Expired" in the pantry list.
  - Bug Report:
    - Issue: Expired Items Used in Plan
    - Actual: Items labeled "Expired" in the pantry are consumed by planned recipes. Cheesy Scrambled Eggs on Toast uses Milk 50 ml, Bread 0.25 loaf, Eggs 4 pcs, and Butter 20 g; Garlic Chicken Stir-Fry uses Chicken Breast 400 g. Chicken Breast, Milk, Bread, Eggs, Butter, and Cheese are all labeled "Expired".
- [ ] CS-04: Regenerate is blocked when every meal is locked.
  - Action: Lock every meal slot across all days. Click "Regenerate".
  - Expected: Regenerate is disabled, or a message appears saying "All meals are locked". No recipes change.
  - Bug Report:
    - Issue: No Lock-All Guard
    - Actual: After all 21 meal slots were locked (21 "Unlock meal" buttons), "Regenerate Plan" stayed enabled and no "All meals are locked" message appeared. Clicking it showed "Meal Plan Generated! Created 7-day plan with 21 locked meals preserved." The recipes did not change, but the button was not disabled and no message was shown.

## Interaction

- [ ] IX-01: Generating a plan shows a loading state and disables the button until results appear.
  - Action: Click "Generate Plan" and observe the button and plan area.
  - Expected: A loading indicator appears and "Generate Plan" is disabled. Both return to normal when the plan is displayed.
  - Bug Report:
    - Issue: Loading State Not Observed
    - Actual: I sampled the Regenerate button every 100 ms for about 600 ms after clicking it. It was never disabled, and no spinner or progress indicator appeared; the plan updated without a visible loading state. The initial "Generate Meal Plan" click returned with the plan already rendered.
- [X] IX-02: Lock toggle changes its icon and label immediately.
  - Action: Click the lock icon on Day 1 Lunch, then click it again.
  - Expected: The first click changes the icon to locked and the label to "Locked". The second click reverts both to unlocked, without a page reload.
- [ ] IX-03: Clicking a recipe expands its ingredient list inline.
  - Action: Click the Day 1 Breakfast recipe name.
  - Expected: The ingredient list and amounts expand beneath the recipe. Clicking again collapses it.
  - Bug Report:
    - Issue: Recipe Does Not Expand
    - Actual: Clicking the Day 1 Breakfast recipe name ("Cheesy Scrambled Eggs on Toast") produced no inline expansion; the card text stayed "Breakfast / Cheesy Scrambled Eggs on Toast / Fluffy eggs with melted cheese on crispy toast / 13m / 2 / 5 items / Locked - won't change on regenerate", with no ingredient list. The same happened for the Day 1 Dinner recipe.
- [ ] IX-04: Pantry items expiring within 3 days are highlighted with an "Expiring soon" badge.
  - Action: Open the Pantry page and locate any default item expiring within 3 days of 2026-11-09.
  - Expected: The row shows an "Expiring soon" badge and a highlighted color. Items expiring later show no badge.
  - Bug Report:
    - Issue: Missing Expiring-Soon Badge
    - Actual: No pantry row shows an "Expiring soon" badge or highlight. Only "Expired" badges appear (13 rows). Because expiration dates are not displayed anywhere, I could not identify any item expiring within 3 days of 2026-11-09.

## Content

- [ ] CT-01: Recipe ingredients and units match pantry items and their stored units.
  - Action: Generate a 3-day plan. Open each recipe and compare its ingredients and units with the pantry list.
  - Expected: Every ingredient exists in the pantry or the grocery list. Units match the pantry unit for that ingredient (no "cup" for a "pcs" item, for example).
  - Bug Report:
    - Issue: Recipe Ingredients Not Accessible
    - Actual: Recipe ingredient lists could not be opened (see FT-05), so per-recipe ingredients and units could not be compared with the pantry. The Ingredient Usage section lists only pantry ingredients, and its units (g, ml, pcs, heads, loaf) match the pantry units, with no mismatch observed.
- [ ] CT-02: High-protein recipes show accurate protein content.
  - Action: Check "High-protein" and click "Generate Plan". Open each recipe.
  - Expected: Each recipe is labeled "High-protein" and states at least 20 g protein per serving.
  - Bug Report:
    - Issue: Missing High-Protein Label and Protein Content
    - Actual: With High Protein on and the plan regenerated, no recipe card shows a "High-protein" label, and no protein amount (grams per serving) appears anywhere in the Meal Plan panel. Recipe cards show only time, servings, and item count.
- [ ] CT-03: Day headers show consecutive calendar dates starting today.
  - Action: Generate a 3-day plan and read the Day 1, Day 2, and Day 3 headers.
  - Expected: Day 1 is dated 2026-11-09, followed by 2026-11-10 and 2026-11-11, with no gaps or duplicates.
  - Bug Report:
    - Issue: Day Headers Missing Dates
    - Actual: Day headers read only "Day 1", "Day 2", and "Day 3" (and "Day 1" through "Day 7" in the 7-day plan). No calendar date (e.g., 2026-11-09) appears in any header.