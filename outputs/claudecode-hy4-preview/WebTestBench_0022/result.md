# Test Result

## Functionality

- [X] FT-01: Add an ingredient to the pantry with quantity and optional expiration date
  - Action: Fill the pantry "Add ingredient" form with name, quantity, unit, and an expiration date, then submit.
  - Expected: The ingredient appears in the pantry list showing its name, quantity with unit, and the expiration date.

- [X] FT-02: Add an ingredient without an expiration date
  - Action: Submit the pantry form with name and quantity only, leaving expiration date empty.
  - Expected: The ingredient is saved and displayed with no expiration date shown (or "No expiration" state), not an error.

- [ ] FT-03: Edit and remove a pantry ingredient
  - Action: Change the quantity of an existing default pantry ingredient, then delete a different default ingredient.
  - Expected: The edited row shows the new quantity, and the deleted ingredient disappears from the pantry list.
  - Bug Report:
    - Issue: Missing edit control — quantity of an existing ingredient cannot be changed
    - Actual: Every pantry row exposes only a single trash-icon (delete) button; there is no edit/pencil button, no `aria-label="edit"`, and clicking the row or its name does not open any dialog (0 `[role="dialog"]` elements appear). The default ingredient "Pasta" was deleted successfully and disappeared from the list, so the remove half works, but the edit half is impossible — the row's quantity can never be modified, so "The edited row shows the new quantity" is not met.

- [X] FT-04: Generate a multi-day meal plan from the pantry
  - Action: With the default pantry data present, choose a number of days (e.g., 3) and click "Generate meal plan".
  - Expected: A day-by-day plan renders with one section per day, and each day lists at least one named recipe/meal.

- [ ] FT-05: Plan prioritizes ingredients closest to expiring
  - Action: Note the default pantry ingredient with the earliest expiration date, then generate a multi-day plan.
  - Expected: That near-expiry ingredient is used in a recipe on Day 1 (or the earliest day), ahead of ingredients with later expiration dates.
  - Bug Report:
    - Issue: Expiry-based prioritization is ineffective — soonest-expiring ingredients are never scheduled
    - Actual: In the default 3-day plan (Preferences: Budget Friendly), the default pantry ingredient with the earliest expiration date — Spinach (2024-12-14) — is not used in any recipe on Day 1 or on any day; neither is the next-earliest, Bread (2024-12-15). Day 1 instead uses Chicken Breast / Greek Yogurt / Tomatoes / Cheese / Rice / Pasta / Olive Oil, and the plan asks to buy an additional 700–1100 g of Chicken Breast while Spinach, Eggs, Milk, Bread and Butter stay completely unused. The only pantry item with a future expiry, Zucchini (badge "4 days"), is also never scheduled. The planner gives expired items only a flat +5 score bonus (no ordering by date), so recipes are ranked by ingredient coverage instead of urgency.

- [X] FT-06: Vegetarian preference produces a meat-free plan
  - Action: Select the "Vegetarian" preference and generate a plan.
  - Expected: No recipe in any day contains meat, poultry, fish, or seafood ingredients.

- [ ] FT-07: High-protein preference produces a protein-forward plan
  - Action: Select the "High-protein" preference and generate a plan.
  - Expected: Every day's recipes are labeled as high-protein (or show a per-day protein amount), and each day includes at least one protein-source ingredient.
  - Bug Report:
    - Issue: No high-protein label and no per-day protein amount rendered
    - Actual: With only "High Protein" selected the recipe pool is indeed protein-based (Day 1: Cheesy Scrambled Eggs on Toast / Garlic Chicken Stir-Fry / Chicken Rice Bowl; Day 2: Spinach & Tomato Omelette / Bell Pepper Egg Cups / Garlic Chicken Stir-Fry; Day 3: Spinach & Tomato Omelette / Bell Pepper Egg Cups / Bell Pepper Egg Cups), and each day does include a protein source. However no meal card, day card or summary anywhere in the plan shows a "high-protein"/"High Protein" badge or any protein amount in grams — the cards render only total time, servings and ingredient count (e.g. "35m · 2 · 5 items"). The only "High Protein" text on the page belongs to the preference toggle itself.

- [ ] FT-08: Budget-friendly preference produces a low-cost plan
  - Action: Select the "Budget-friendly" preference and generate a plan.
  - Expected: Recipes are labeled budget-friendly (or show a cost/per-serving figure), and no premium-cost ingredient is scheduled.
  - Bug Report:
    - Issue: No budget-friendly label and no cost / per-serving figure rendered
    - Actual: With only "Budget Friendly" selected the plan contains Greek Yogurt Parfait, Tomato Pasta Primavera and Chicken Rice Bowl, but no recipe card shows a "budget-friendly" badge, a price, or a cost-per-serving value — the recipe data carries no cost field and the cards render only "5m · 1 · 1 items" style meta. No cost figure appears anywhere in the plan, so the "labeled budget-friendly (or show a cost/per-serving figure)" requirement is unmet.

- [ ] FT-09: Each recipe shows the exact amount of every ingredient used
  - Action: Expand/open any recipe in the generated plan.
  - Expected: The recipe lists each of its ingredients with an explicit quantity and unit (e.g., "2 cups spinach", "200 g chicken"), for every ingredient.
  - Bug Report:
    - Issue: Recipe cards are not expandable and do not list ingredient quantities
    - Actual: Clicking the recipe name / card ("Chicken Rice Bowl") produces no dialog and no expansion (dialog count stays 0 before and after the click); the card only shows the description plus "35m · 2 · 5 items". Per-recipe quantities with units exist only in the separate "Ingredient Usage" panel (e.g. "Chicken Rice Bowl: 300 g"), not inside the recipe itself, so the recipe does not list each of its ingredients with an explicit quantity and unit.

- [X] FT-10: Grocery list is produced for missing items
  - Action: Generate the plan and open the grocery list section.
  - Expected: A list of items not available in the pantry appears, each with the name and the amount needed.

- [X] FT-11: Lock a single meal and regenerate the rest
  - Action: Lock one meal in one day, click "Regenerate", then inspect the new plan.
  - Expected: The locked meal (recipe and ingredients) is unchanged, while at least one other unlocked meal differs from the previous plan.

- [ ] FT-12: Lock an entire day and regenerate the rest
  - Action: Lock a whole day, click "Regenerate", then inspect the new plan.
  - Expected: Every meal in the locked day is unchanged, while meals in at least one unlocked day differ from the previous plan.
  - Bug Report:
    - Issue: Missing day-level lock control
    - Actual: The "Day 1" header contains only the title element (`<h3 …>Day 1</h3>`) and zero buttons — there is no lock toggle, no "lock day" affordance, and clicking the day heading or header does nothing. Only individual meal cards have a lock button (title="Lock meal"), so an entire day cannot be locked before regenerating.

## Constraint

- [ ] CS-01: Ingredient cannot be added without a name or quantity
  - Action: Submit the pantry form with an empty name, then again with an empty/zero quantity.
  - Expected: Both submissions are blocked; a validation message appears and no blank ingredient is added to the pantry list.
  - Bug Report:
    - Issue: Silent rejection — submissions are blocked but no validation message is shown
    - Actual: Submitting "Add to Pantry" with an empty name (quantity 5) and then with a valid name ("ZeroQtyTest") but quantity 0 both correctly added nothing — pantry stayed at 16 rows and the dialog stayed open — but no feedback was rendered: there were 0 elements with `role="alert"`, `aria-live`, or `.text-destructive`, no toast, and the inputs carry no `required`/`min` attributes. The user gets no indication why the form will not submit.

- [X] CS-02: Planned usage never exceeds available pantry stock without a grocery entry
  - Action: Sum the amounts of one default pantry ingredient used across all recipes in the generated plan and compare to its pantry quantity.
  - Expected: Total usage is less than or equal to pantry quantity, or the shortfall appears with an explicit amount on the grocery list.

- [ ] CS-03: Expired ingredients are flagged and excluded from the plan
  - Action: Add an ingredient with a past expiration date, then generate a plan.
  - Expected: The ingredient is marked "Expired" in the pantry and is not scheduled in any recipe in the plan.
  - Bug Report:
    - Issue: Expired ingredients are flagged but still scheduled in recipes
    - Actual: The newly added "Old Tofu" (expiration 2026-11-01) is correctly badged "Expired" and is not scheduled, but expired default items are used heavily in the plan: Chicken Breast (expired 2024-12-16) is scheduled for 1200 g across four "Chicken Rice Bowl" meals against only 500 g in the pantry, Greek Yogurt (expired 2024-12-16) 600 g vs 500 g, Tomatoes (expired 2024-12-15) 8 pcs vs 6 pcs, Onions (expired 2024-12-25) 6 pcs vs 4 pcs, plus expired Cheese, Garlic and Bell Peppers. Expired stock is only given a reduced score bonus instead of being excluded.

- [X] CS-04: Grocery list excludes items already covered by the pantry
  - Action: Generate the plan, then check the grocery list against a pantry ingredient that fully covers its planned usage.
  - Expected: That ingredient does not appear on the grocery list.

## Interaction

- [X] IX-01: Lock control shows a persistent locked state
  - Action: Click the lock control on a meal.
  - Expected: The meal displays a visible locked indicator, and the indicator is still present on that meal after regenerating.

- [X] IX-02: Preference toggles reflect selection and can be cleared
  - Action: Click a preference toggle, then click it again to deselect it.
  - Expected: The toggle appears selected when on and unselected when off, with no preference applied after deselection.

- [X] IX-03: Regenerate refreshes the plan in place without clearing the pantry
  - Action: Click "Regenerate" on an existing plan.
  - Expected: The day-by-day plan area updates with a new plan on the same page, and the pantry list remains fully intact and unchanged.

## Content

- [X] CT-01: Recipes and their media are food-relevant and render correctly
  - Action: Review every recipe name and any recipe image/icon in the generated plan.
  - Expected: All names describe actual dishes/meals, all images load without broken placeholders, and every image depicts food or a meal.

- [X] CT-02: Day labels, quantities, and units are complete and well-formed
  - Action: Review all day headers, ingredient amounts in recipes, and grocery list entries.
  - Expected: Days are labeled sequentially (Day 1, Day 2, …), every amount shows a number plus a valid unit, and no placeholder text such as "undefined", "NaN", or "Lorem ipsum" appears anywhere.

---

### Evidence notes
- Passing highlights: grocery list rendered `Greek Yogurt 100 g / Pasta 800 g / Tomatoes 2 pcs / Onions 2 pcs / Chicken Breast 700 g` (FT-10, CS-02), while fully-covered Rice (1000/1000 g) and Olive Oil (500/160 ml) were correctly absent (CS-04). Locking Day 1 Lunch kept "Tomato Pasta Primavera" fixed while Day 2 Dinner and Day 3 Dinner changed to "Tomato Pasta Primavera" and "Garlic Chicken Stir-Fry" (FT-11); the locked card kept its `ring-2` highlight, "Locked - won't change on regenerate" text and `title="Unlock meal"` (IX-01); the pantry kept all 17 rows unchanged after regeneration (IX-03).
- Content scan found 0 `undefined` / `NaN` / `Lorem ipsum` strings, sequential "Day 1 / Day 2 / Day 3" headers, and 0 `<img>` elements on the page (all icons are inline SVG, so no broken placeholders) — all recipe names are real dishes (CT-01, CT-02).
- Expiry context: the seeded default pantry dates (2024-12-14 … 2024-12-30) are all in the past relative to the system date (2026-11-08), so every default item renders an "Expired" badge; this is the state the checks above were executed against.