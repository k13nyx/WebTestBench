# Test Checklist

## Functionality
- [ ] FT-01: Add an ingredient to the pantry with name, quantity, and expiration date
  - Action: Enter an ingredient name, a quantity (with unit), and an expiration date, then submit the add form.
  - Expected: The ingredient appears in the pantry list showing its name, quantity, and expiration date.

- [ ] FT-02: Add an ingredient without an expiration date (optional field)
  - Action: Enter an ingredient name and quantity only, leaving the expiration date empty, then submit.
  - Expected: The ingredient is added to the pantry list with no expiration date shown, and no error is displayed.

- [ ] FT-03: Edit the quantity of an existing pantry ingredient
  - Action: Change the quantity of a listed pantry ingredient and save.
  - Expected: The pantry list displays the updated quantity for that ingredient.

- [ ] FT-04: Remove an ingredient from the pantry
  - Action: Delete an ingredient from the pantry list.
  - Expected: The ingredient no longer appears in the pantry list.

- [ ] FT-05: Generate a multi-day meal plan
  - Action: Click the button to generate a meal plan (default preferences, default pantry).
  - Expected: A day-by-day plan is displayed with a recipe assigned to each day of the plan.

- [ ] FT-06: Each planned day shows exact ingredient usage amounts
  - Action: Open/inspect any day in the generated plan.
  - Expected: For each recipe, the plan lists each ingredient it uses with an exact quantity (e.g., "200 g spinach"), drawn from the pantry where available.

- [ ] FT-07: Plan prioritizes ingredients close to expiring
  - Action: Generate a plan when the pantry contains at least one ingredient with an expiration date sooner than others, and compare which recipes are scheduled first.
  - Expected: The ingredient(s) with the nearest expiration date are used in the earliest day(s) of the plan rather than in later days.

- [ ] FT-08: Generate a grocery list of missing items
  - Action: After generating a plan, open the grocery list.
  - Expected: The grocery list contains only ingredients required by the plan that are missing or insufficient in the pantry, each with the total quantity needed.

- [ ] FT-09: Apply the "vegetarian" preference when generating a plan
  - Action: Select the vegetarian preference and generate a meal plan.
  - Expected: Every recipe in the generated plan is vegetarian.

- [ ] FT-10: Apply the "high-protein" preference when generating a plan
  - Action: Select the high-protein preference and generate a meal plan.
  - Expected: Every recipe in the generated plan is marked as high-protein.

- [ ] FT-11: Apply the "budget-friendly" preference when generating a plan
  - Action: Select the budget-friendly preference and generate a meal plan.
  - Expected: Every recipe in the generated plan is marked as budget-friendly.

## Constraint
- [ ] CS-01: Cannot add an ingredient without a name or quantity
  - Action: Submit the add-ingredient form with the name field, or the quantity field, left empty.
  - Expected: The ingredient is not added, and an error message identifies the missing required field.

- [ ] CS-02: Cannot generate a meal plan when the pantry is empty
  - Action: Remove all pantry ingredients, then attempt to generate a meal plan.
  - Expected: Generation is blocked with a message explaining the pantry must contain ingredients; no plan is displayed.

- [ ] CS-03: Regeneration does not change locked meals or days
  - Action: Lock one meal (or one full day) in an existing plan, then trigger regeneration.
  - Expected: The locked meal/day keeps exactly the same recipe as before; only unlocked meals/days change.

## Interaction
- [ ] IX-01: Locking a meal shows a clear locked state
  - Action: Click the lock control on a specific meal.
  - Expected: The meal visibly changes to a locked state (e.g., lock icon/label) and a control to unlock it is available.

- [ ] IX-02: Regenerate produces a different plan for unlocked slots
  - Action: With nothing locked, click regenerate on an existing plan.
  - Expected: At least some unlocked meals change to different recipes, and the plan remains fully displayed without errors.

- [ ] IX-03: Regeneration preserves the previously locked selection after repeated use
  - Action: Lock a meal, regenerate twice in a row.
  - Expected: After both regenerations, the locked meal still shows the same original recipe while other unlocked days may differ between runs.

## Content
- [ ] CT-01: All recipes and displayed food content match the selected preference labels
  - Action: Review recipe names, descriptions, and images in a generated plan against its applied preference(s).
  - Expected: Recipe titles, descriptions, and images are relevant to the recipe shown and consistent with the selected preference (vegetarian / high-protein / budget-friendly); no mismatched or unrelated food content appears.

- [ ] CT-02: Ingredient usage amounts in the plan are consistent with the recipe and pantry data
  - Action: Compare the ingredient quantities shown for a planned recipe against the pantry quantities and the grocery list totals.
  - Expected: Units match across plan, pantry, and grocery list; pantry usage never exceeds the quantity on hand, and grocery list amounts equal plan requirement minus pantry stock.