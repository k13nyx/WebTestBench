# Test Checklist

## Functionality
- [ ] FT-01: Add a new ingredient to the pantry with name, quantity, unit, and optional expiration date
  - Action: Fill in the pantry form (name "Black Beans", quantity "2", unit "cans", expiration "2026-11-20") and click **Add Ingredient**.
  - Expected: The item appears in the pantry list showing "Black Beans — 2 cans" and expiration date "2026-11-20"; no error message appears.
- [ ] FT-02: Default pantry items are listed with their quantity and expiration date
  - Action: Load the page and review the pantry list without adding anything.
  - Expected: Every pre-existing item shows its name, a non-empty quantity with unit, and an expiration date (or a clear "no date" indicator when absent); the list is not empty.
- [ ] FT-03: Update the quantity of an existing pantry item and remove an item
  - Action: Change the quantity of one default pantry item and save it; then delete a different item.
  - Expected: The edited item shows the new quantity after save/reload, and the deleted item is no longer present in the pantry list.
- [ ] FT-04: Generate a multi-day meal plan
  - Action: Set the number of days (e.g., 3 or 5) and click **Generate Plan**.
  - Expected: A plan is displayed containing exactly one section per selected day, and each day shows recipes with their meal slot (e.g., breakfast/lunch/dinner).
- [ ] FT-05: Each planned recipe shows exactly how much of each ingredient is used
  - Action: Open any recipe card in the generated plan.
  - Expected: The card lists every ingredient with a specific numeric amount and unit (e.g., "Onion — 1 whole", not just "Onion").
- [ ] FT-06: Produce a grocery list of ingredients that are missing
  - Action: Click **Grocery List** (or the equivalent action) after generating a plan.
  - Expected: A list appears containing ingredients required by the plan but not available in the pantry, each with the needed quantity; the list is not empty when the pantry lacks plan ingredients.
- [ ] FT-07: Preferences change the generated meal plan
  - Action: Generate a plan with **Vegetarian** selected and note the recipes; then enable **High-Protein** and/or **Budget-Friendly** and regenerate.
  - Expected: The vegetarian plan contains no meat/fish dishes, and enabling high-protein or budget changes the set of recipes shown (different recipes appear from the unfiltered baseline).
- [ ] FT-08: Lock a single meal, regenerate, and keep it unchanged
  - Action: Lock one specific meal in the plan, click **Regenerate**, and compare before/after.
  - Expected: The locked meal keeps the same recipe and ingredient amounts; the other meals/days are regenerated (at least one other meal changes).
- [ ] FT-09: Lock an entire day, regenerate, and keep it unchanged
  - Action: Lock a whole day (e.g., Day 2), click **Regenerate**, and compare before/after.
  - Expected: Day 2 keeps the exact same recipes and amounts it had before; the remaining days are regenerated with new content.

## Constraint
- [ ] CS-01: Pantry entries require a name and a quantity
  - Action: Submit the pantry form with an empty name, then with an empty quantity.
  - Expected: Each submission is rejected with a visible validation message and no new item is added to the pantry list.
- [ ] CS-02: Expiration date is optional
  - Action: Add an ingredient filling only name, quantity, and unit, leaving the expiration field blank, and save.
  - Expected: The item is added successfully and appears in the pantry with a "no date"/blank expiration indicator rather than an error.
- [ ] CS-03: Grocery list lists only items not already covered by the pantry
  - Action: Generate a plan and open the grocery list; cross-check several entries against the pantry list.
  - Expected: No item fully in stock in the pantry is listed as missing, and no ingredient appears twice in the grocery list.
- [ ] CS-04: Planned usage never exceeds the quantity on hand
  - Action: Compare the amounts shown for each pantry ingredient in the plan against that ingredient's available quantity.
  - Expected: For every pantry ingredient, the total amount consumed by the plan is less than or equal to the quantity on hand (no recipe uses more than is available).
- [ ] CS-05: Regenerating preserves the plan settings and the locked entries
  - Action: Select 4 days with **Vegetarian** enabled, lock one meal, then click **Regenerate**.
  - Expected: The plan still covers 4 days, vegetarian recipes are still shown, and the locked meal is still present and unchanged.

## Interaction
- [ ] IX-01: Ingredients close to expiring are visibly flagged and prioritized
  - Action: Locate the default pantry items that expire soonest (within a few days of today) and inspect their rows; also trigger a plan generation.
  - Expected: Near-expiry items show a distinct visual marker such as an "Expires soon"/expiry badge, and in the generated plan the meals using those ingredients appear ahead of (or are clearly prioritized over) meals using later-expiring items.
- [ ] IX-02: Lock control reflects and toggles its state
  - Action: Click the lock control on one meal, observe it, then click it again.
  - Expected: After the first click the item shows a locked indicator (icon/text change); after the second click the locked indicator is removed and the item is unlocked.
- [ ] IX-03: Preference controls show which preferences are active
  - Action: Click the **Vegetarian**, **High-Protein**, and **Budget-Friendly** toggles one at a time.
  - Expected: Each clicked control shows a distinct selected/active visual state, and unselected controls show an inactive state.
- [ ] IX-04: Grocery list items can be marked as obtained
  - Action: Click the check-off control on one grocery list item.
  - Expected: The item's visual state changes to a completed/marked state (strikethrough or checkmark) and it is distinguishable from unchecked items.

## Content
- [ ] CT-01: Each recipe shows complete, meaningful recipe content
  - Action: Open two different recipe cards in the generated plan.
  - Expected: Each displays a recipe name, an ingredient list with amounts, and preparation instructions/steps; no card is blank or shows placeholder text.
- [ ] CT-02: Recipes match the selected dietary preference
  - Action: Generate a plan with **Vegetarian** enabled and inspect every recipe's ingredient list.
  - Expected: No recipe lists meat, poultry, or fish ingredients; all listed ingredients are vegetarian-compatible.
- [ ] CT-03: Plan days and meals are clearly labeled
  - Action: View the generated plan for a multi-day selection.
  - Expected: Each day has a distinct visible header (e.g., "Day 1", "Day 2" with date) and each meal within a day is labeled with its slot, so days and meals can be told apart without ambiguity.