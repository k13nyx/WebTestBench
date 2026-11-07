# Test Checklist

## Functionality
- [ ] FT-01: Add an ingredient to the pantry with quantity and optional expiration date
  - Action: Fill the pantry "Add ingredient" form with name, quantity, unit, and an expiration date, then submit.
  - Expected: The ingredient appears in the pantry list showing its name, quantity with unit, and the expiration date.

- [ ] FT-02: Add an ingredient without an expiration date
  - Action: Submit the pantry form with name and quantity only, leaving expiration date empty.
  - Expected: The ingredient is saved and displayed with no expiration date shown (or "No expiration" state), not an error.

- [ ] FT-03: Edit and remove a pantry ingredient
  - Action: Change the quantity of an existing default pantry ingredient, then delete a different default ingredient.
  - Expected: The edited row shows the new quantity, and the deleted ingredient disappears from the pantry list.

- [ ] FT-04: Generate a multi-day meal plan from the pantry
  - Action: With the default pantry data present, choose a number of days (e.g., 3) and click "Generate meal plan".
  - Expected: A day-by-day plan renders with one section per day, and each day lists at least one named recipe/meal.

- [ ] FT-05: Plan prioritizes ingredients closest to expiring
  - Action: Note the default pantry ingredient with the earliest expiration date, then generate a multi-day plan.
  - Expected: That near-expiry ingredient is used in a recipe on Day 1 (or the earliest day), ahead of ingredients with later expiration dates.

- [ ] FT-06: Vegetarian preference produces a meat-free plan
  - Action: Select the "Vegetarian" preference and generate a plan.
  - Expected: No recipe in any day contains meat, poultry, fish, or seafood ingredients.

- [ ] FT-07: High-protein preference produces a protein-forward plan
  - Action: Select the "High-protein" preference and generate a plan.
  - Expected: Every day's recipes are labeled as high-protein (or show a per-day protein amount), and each day includes at least one protein-source ingredient.

- [ ] FT-08: Budget-friendly preference produces a low-cost plan
  - Action: Select the "Budget-friendly" preference and generate a plan.
  - Expected: Recipes are labeled budget-friendly (or show a cost/per-serving figure), and no premium-cost ingredient is scheduled.

- [ ] FT-09: Each recipe shows the exact amount of every ingredient used
  - Action: Expand/open any recipe in the generated plan.
  - Expected: The recipe lists each of its ingredients with an explicit quantity and unit (e.g., "2 cups spinach", "200 g chicken"), for every ingredient.

- [ ] FT-10: Grocery list is produced for missing items
  - Action: Generate the plan and open the grocery list section.
  - Expected: A list of items not available in the pantry appears, each with the name and the amount needed.

- [ ] FT-11: Lock a single meal and regenerate the rest
  - Action: Lock one meal in one day, click "Regenerate", then inspect the new plan.
  - Expected: The locked meal (recipe and ingredients) is unchanged, while at least one other unlocked meal differs from the previous plan.

- [ ] FT-12: Lock an entire day and regenerate the rest
  - Action: Lock a whole day, click "Regenerate", then inspect the new plan.
  - Expected: Every meal in the locked day is unchanged, while meals in at least one unlocked day differ from the previous plan.

## Constraint
- [ ] CS-01: Ingredient cannot be added without a name or quantity
  - Action: Submit the pantry form with an empty name, then again with an empty/zero quantity.
  - Expected: Both submissions are blocked; a validation message appears and no blank ingredient is added to the pantry list.

- [ ] CS-02: Planned usage never exceeds available pantry stock without a grocery entry
  - Action: Sum the amounts of one default pantry ingredient used across all recipes in the generated plan and compare to its pantry quantity.
  - Expected: Total usage is less than or equal to pantry quantity, or the shortfall appears with an explicit amount on the grocery list.

- [ ] CS-03: Expired ingredients are flagged and excluded from the plan
  - Action: Add an ingredient with a past expiration date, then generate a plan.
  - Expected: The ingredient is marked "Expired" in the pantry and is not scheduled in any recipe in the plan.

- [ ] CS-04: Grocery list excludes items already covered by the pantry
  - Action: Generate the plan, then check the grocery list against a pantry ingredient that fully covers its planned usage.
  - Expected: That ingredient does not appear on the grocery list.

## Interaction
- [ ] IX-01: Lock control shows a persistent locked state
  - Action: Click the lock control on a meal.
  - Expected: The meal displays a visible locked indicator, and the indicator is still present on that meal after regenerating.

- [ ] IX-02: Preference toggles reflect selection and can be cleared
  - Action: Click a preference toggle, then click it again to deselect it.
  - Expected: The toggle appears selected when on and unselected when off, with no preference applied after deselection.

- [ ] IX-03: Regenerate refreshes the plan in place without clearing the pantry
  - Action: Click "Regenerate" on an existing plan.
  - Expected: The day-by-day plan area updates with a new plan on the same page, and the pantry list remains fully intact and unchanged.

## Content
- [ ] CT-01: Recipes and their media are food-relevant and render correctly
  - Action: Review every recipe name and any recipe image/icon in the generated plan.
  - Expected: All names describe actual dishes/meals, all images load without broken placeholders, and every image depicts food or a meal.

- [ ] CT-02: Day labels, quantities, and units are complete and well-formed
  - Action: Review all day headers, ingredient amounts in recipes, and grocery list entries.
  - Expected: Days are labeled sequentially (Day 1, Day 2, …), every amount shows a number plus a valid unit, and no placeholder text such as "undefined", "NaN", or "Lorem ipsum" appears anywhere.