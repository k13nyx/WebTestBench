# Test Checklist

## Functionality
- [ ] FT-01: Pantry list shows each ingredient's name, quantity, and expiration date.
  - Action: Open the Pantry page and review the default ingredient rows.
  - Expected: Each row shows name, quantity with unit, and expiration date. Items with no expiration show "No expiration" or a blank date, with no error.
- [ ] FT-02: User can add a pantry ingredient with quantity and optional expiration date.
  - Action: Click "Add Ingredient", enter a name, quantity 1, and leave Expiration empty. Click "Save".
  - Expected: A new row appears in the pantry list with quantity 1 and no expiration date.
- [ ] FT-03: Generated plan shows day-by-day meals, each with a named recipe.
  - Action: Set plan length to 3 days, select no preferences, and click "Generate Plan".
  - Expected: Day 1, Day 2, and Day 3 sections appear. Each has Breakfast, Lunch, and Dinner slots, and each slot shows a recipe name.
- [ ] FT-04: Ingredients closest to expiry are used in the earliest meals.
  - Action: Note the default pantry item with the earliest expiration date. Generate a 3-day plan.
  - Expected: That ingredient appears in a Day 1 recipe, and it is used before items with later expiration dates.
- [ ] FT-05: Each recipe lists the exact amount of each ingredient it uses.
  - Action: Click the Day 1 Dinner recipe.
  - Expected: Each ingredient shows a specific quantity and unit, such as "Eggs: 2 pcs". The amount does not exceed the pantry quantity.
- [ ] FT-06: Grocery list shows missing and insufficient ingredients with the shortfall amount.
  - Action: Generate a 3-day plan and open the "Grocery List" tab.
  - Expected: Each ingredient the plan needs beyond pantry stock is listed with its shortfall quantity. Fully stocked ingredients are not listed.
- [ ] FT-07: Vegetarian preference limits the plan to vegetarian recipes.
  - Action: Check "Vegetarian" and click "Generate Plan".
  - Expected: Every recipe in the plan is labeled "Vegetarian", and no meal slot shows a recipe with meat or fish.
- [ ] FT-08: Locked meals and days are kept when the plan is regenerated.
  - Action: Click the lock icon on Day 1 Breakfast and on the Day 2 header. Click "Regenerate".
  - Expected: Day 1 Breakfast and all Day 2 meals keep the same recipes and amounts. Other unlocked meals change.
- [ ] FT-09: Regenerating updates unlocked meals and the grocery list to match.
  - Action: Note the grocery list. Lock Day 1, then click "Regenerate".
  - Expected: Day 2 and Day 3 meals change. The grocery list reflects only the new unlocked recipes' shortfalls.

## Constraint
- [ ] CS-01: Pantry form rejects an empty name or a non-positive quantity.
  - Action: Click "Add Ingredient", leave Name empty, enter quantity 0, and click "Save". Then enter quantity -1 and click "Save".
  - Expected: An error message appears for each invalid field ("Name is required", "Quantity must be greater than 0"). The item is not saved.
- [ ] CS-02: Planned usage never exceeds the pantry quantity for any ingredient.
  - Action: Generate a 7-day plan. Add up each ingredient's usage across all days.
  - Expected: The total used for each ingredient is less than or equal to its pantry quantity. Any remainder needed appears on the grocery list.
- [ ] CS-03: Pantry items already past their expiration date are not used in the plan.
  - Action: Identify a default pantry item whose expiration date is before 2026-11-09. Generate a 3-day plan.
  - Expected: That item appears in no recipe, and it is labeled "Expired" in the pantry list.
- [ ] CS-04: Regenerate is blocked when every meal is locked.
  - Action: Lock every meal slot across all days. Click "Regenerate".
  - Expected: Regenerate is disabled, or a message appears saying "All meals are locked". No recipes change.

## Interaction
- [ ] IX-01: Generating a plan shows a loading state and disables the button until results appear.
  - Action: Click "Generate Plan" and observe the button and plan area.
  - Expected: A loading indicator appears and "Generate Plan" is disabled. Both return to normal when the plan is displayed.
- [ ] IX-02: Lock toggle changes its icon and label immediately.
  - Action: Click the lock icon on Day 1 Lunch, then click it again.
  - Expected: The first click changes the icon to locked and the label to "Locked". The second click reverts both to unlocked, without a page reload.
- [ ] IX-03: Clicking a recipe expands its ingredient list inline.
  - Action: Click the Day 1 Breakfast recipe name.
  - Expected: The ingredient list and amounts expand beneath the recipe. Clicking again collapses it.
- [ ] IX-04: Pantry items expiring within 3 days are highlighted with an "Expiring soon" badge.
  - Action: Open the Pantry page and locate any default item expiring within 3 days of 2026-11-09.
  - Expected: The row shows an "Expiring soon" badge and a highlighted color. Items expiring later show no badge.

## Content
- [ ] CT-01: Recipe ingredients and units match pantry items and their stored units.
  - Action: Generate a 3-day plan. Open each recipe and compare its ingredients and units with the pantry list.
  - Expected: Every ingredient exists in the pantry or the grocery list. Units match the pantry unit for that ingredient (no "cup" for a "pcs" item, for example).
- [ ] CT-02: High-protein recipes show accurate protein content.
  - Action: Check "High-protein" and click "Generate Plan". Open each recipe.
  - Expected: Each recipe is labeled "High-protein" and states at least 20 g protein per serving.
- [ ] CT-03: Day headers show consecutive calendar dates starting today.
  - Action: Generate a 3-day plan and read the Day 1, Day 2, and Day 3 headers.
  - Expected: Day 1 is dated 2026-11-09, followed by 2026-11-10 and 2026-11-11, with no gaps or duplicates.