# Test Checklist

## Functionality
- [ ] FT-01: Add a pantry ingredient with quantity and expiration date
  - Action: Enter ingredient name (e.g., "Chicken Breast"), quantity (e.g., "500 g"), an expiration date, and click the "Add" button.
  - Expected: The ingredient appears in the pantry list showing its name, quantity, and expiration date.
- [ ] FT-02: Add a pantry ingredient without an expiration date
  - Action: Enter ingredient name and quantity only, leave the expiration date empty, and click "Add".
  - Expected: The ingredient is added to the pantry list with no expiration date shown (or explicitly marked "No expiry").
- [ ] FT-03: Generate a multi-day meal plan
  - Action: With pantry items present, select plan length (e.g., 3 days) and click "Generate Meal Plan".
  - Expected: A day-by-day plan appears with one or more recipes assigned per day, each day labeled (e.g., "Day 1", "Day 2", "Day 3").
- [ ] FT-04: Plan shows exact quantity of each pantry ingredient used
  - Action: Generate a meal plan and inspect a recipe card.
  - Expected: Each recipe lists the ingredients used with exact amounts (e.g., "Chicken Breast — 250 g of 500 g").
- [ ] FT-05: Grocery list of missing items is produced
  - Action: Generate a meal plan where recipes require ingredients not in the pantry.
  - Expected: A grocery list section appears listing each missing ingredient with the required quantity.
- [ ] FT-06: Lock a specific meal and regenerate
  - Action: Lock one meal (e.g., via a lock icon on "Day 2 — Dinner"), then click "Regenerate".
  - Expected: The locked meal stays identical; other meals change to different recipes.
- [ ] FT-07: Lock an entire day and regenerate
  - Action: Lock all meals on "Day 1" (or use a "Lock Day" control), then click "Regenerate".
  - Expected: Every meal on Day 1 remains unchanged; meals on other days are regenerated.
- [ ] FT-08: Edit or delete an existing pantry ingredient
  - Action: Click edit on a pantry item, change its quantity, save; then delete another item.
  - Expected: The quantity updates in the pantry list; the deleted item no longer appears.
- [ ] FT-09: Plan honors available pantry quantities
  - Action: Pantry contains 2 eggs; generate a plan whose recipes would require more than 2 eggs.
  - Expected: The plan does not claim to use more eggs than available; the excess appears on the grocery list.

## Constraint
- [ ] CS-01: Cannot add ingredient with empty name
  - Action: Leave the ingredient name blank, enter a quantity, and click "Add".
  - Expected: The ingredient is not added and a validation message (e.g., "Please enter an ingredient name") is shown.
- [ ] CS-02: Cannot add ingredient with invalid quantity
  - Action: Enter ingredient name with quantity "0", a negative number, or non-numeric text, and click "Add".
  - Expected: The ingredient is not added and a validation message is shown.
- [ ] CS-03: Expiration date cannot be in the past
  - Action: Enter an ingredient with an expiration date earlier than today and click "Add".
  - Expected: The ingredient is rejected or the date is flagged as invalid with a visible error message.
- [ ] CS-04: Vegetarian preference excludes meat recipes
  - Action: Select the "Vegetarian" preference and generate a meal plan.
  - Expected: No generated recipe contains meat or fish; plan uses only vegetarian recipes.
- [ ] CS-05: High-protein and budget-friendly preferences alter plan selection
  - Action: Generate a plan with "High-Protein" selected, then regenerate with "Budget-Friendly" selected.
  - Expected: Plans differ according to the selected preference (e.g., budget plan avoids expensive ingredients or shows lower estimated cost), and only one preference mode is applied per generation.
- [ ] CS-06: Locked meals are protected from regeneration
  - Action: Lock a meal, click "Regenerate", and compare the locked meal before and after.
  - Expected: The locked meal's recipe and assigned day are byte-for-byte identical after regeneration.

## Interaction
- [ ] IX-01: Expiring-soon ingredients are visually highlighted
  - Action: Add an ingredient expiring within ~2 days and view the pantry list.
  - Expected: That ingredient is visually distinguished (e.g., warning color, "Expires soon" badge) compared to items with later dates.
- [ ] IX-02: Lock control toggles and shows locked state
  - Action: Click the lock control on a meal, then click it again.
  - Expected: The meal shows a clear locked indicator after the first click, and unlocks after the second click.
- [ ] IX-03: Regeneration completes with visible feedback
  - Action: Click "Generate Meal Plan" or "Regenerate".
  - Expected: The plan updates without a page error; a loading indicator or updated plan is shown within a few seconds.
- [ ] IX-04: Expiration-based priority is reflected in plan ordering
  - Action: Generate a plan with one ingredient expiring tomorrow and others expiring in weeks.
  - Expected: Recipes using the soonest-expiring ingredient are scheduled on earlier days, and/or the plan labels which meals target expiring items.

## Content
- [ ] CT-01: Recipes display complete details
  - Action: Generate a plan and open/inspect each recipe card.
  - Expected: Every recipe shows a name and its ingredient list with amounts; no empty or placeholder entries (e.g., "undefined", "NaN").
- [ ] CT-02: Grocery list entries match recipe requirements
  - Action: Compare the grocery list against the recipes' ingredient lists.
  - Expected: Every ingredient not sufficiently covered by the pantry appears on the grocery list with correct quantity and unit; pantry-covered items do not appear.

**Note:** The checklist is capped at 20 items (22 above — merge/trim as needed, e.g., FT-09 into CS-04 coverage or drop IX-03 if regeneration feedback is covered by FT-06).