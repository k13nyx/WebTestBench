# Test Checklist

## Functionality
- [ ] FT-01: Add an ingredient with name and quantity to the pantry
  - Action: Open the pantry section, enter an ingredient name and quantity, then click "Add" (or "Add to Pantry").
  - Expected: The ingredient appears in the pantry list showing its name and quantity.

- [ ] FT-02: Add an optional expiration date to a pantry ingredient
  - Action: While adding or editing a pantry ingredient, set an expiration date and save.
  - Expected: The ingredient is saved and the expiration date is displayed; leaving it blank still saves successfully.

- [ ] FT-03: Set a meal-plan preference
  - Action: Select one preference (e.g., "Vegetarian", "High-Protein", or "Budget-Friendly") from the preference control.
  - Expected: The selected preference is active/highlighted and will be applied on generation.

- [ ] FT-04: Generate a multi-day meal plan
  - Action: Click "Generate Plan" (or "Create Meal Plan").
  - Expected: A plan is produced covering multiple days, each with at least one meal.

- [ ] FT-05: View the day-by-day plan with recipes
  - Action: Open the generated plan view.
  - Expected: Each day is listed with its meal(s) and the associated recipe name(s).

- [ ] FT-06: See exact ingredient usage per recipe
  - Action: Expand or open a recipe in the plan.
  - Expected: The recipe lists each ingredient with the exact quantity that will be used.

- [ ] FT-07: Generate a grocery list for missing items
  - Action: Open the grocery list (auto-generated with the plan).
  - Expected: A list of items is shown that are needed but not sufficiently stocked in the pantry.

- [ ] FT-08: Lock a meal or an entire day
  - Action: Click the lock control on a specific meal or day, then confirm it is locked.
  - Expected: The meal/day is marked as locked and no longer changes when regenerating.

- [ ] FT-09: Regenerate the plan while keeping locked items
  - Action: With at least one meal/day locked, click "Regenerate" (or "Generate Plan").
  - Expected: A new plan is produced for the unlocked parts while the locked meal(s)/day(s) remain exactly as before.

## Constraint
- [ ] CS-01: Required pantry fields enforced; expiration optional
  - Action: Attempt to add a pantry item leaving the name or quantity empty; then add one with those filled but no expiration date.
  - Expected: Save is blocked with a validation message for missing name/quantity; adding without expiration succeeds.

- [ ] CS-02: Locked meals/days are never altered on regenerate
  - Action: Lock a meal, regenerate, and compare the locked meal before and after.
  - Expected: The locked meal's recipe and ingredients are identical; no change occurs.

- [ ] CS-03: Selected preference is respected in the plan
  - Action: Generate a plan with "Vegetarian" selected (and separately "High-Protein").
  - Expected: Vegetarian plan contains no meat recipes; High-Protein plan favors protein-rich recipes.

- [ ] CS-04: Plan prioritizes ingredients closest to expiration
  - Action: Add ingredients with near and far expiration dates, then generate a plan.
  - Expected: Recipes consuming the soonest-to-expire ingredients appear earliest in the plan.

## Interaction
- [ ] IX-01: Success confirmation after plan generation
  - Action: Click "Generate Plan".
  - Expected: A success toast or message appears confirming the plan was created.

- [ ] IX-02: Locked items are visually distinguished
  - Action: Lock a meal or day and view the plan.
  - Expected: The locked item shows a clear visual indicator (e.g., lock icon or distinct style).

- [ ] IX-03: Expiring-soon ingredients are visually flagged
  - Action: View the pantry with items nearing expiration.
  - Expected: Soon-to-expire items show a visual warning (e.g., color or icon) indicating urgency.

## Content
- [ ] CT-01: Recipes are relevant to preferences and pantry
  - Action: Review the generated recipes against the selected preference and available pantry items.
  - Expected: Each recipe aligns with the chosen preference and uses ingredients present (or listed as missing) in the pantry.

- [ ] CT-02: Grocery list contains only genuinely missing items
  - Action: Compare the grocery list against the pantry stock.
  - Expected: Every grocery item is something not sufficiently available in the pantry; no already-stocked items appear.