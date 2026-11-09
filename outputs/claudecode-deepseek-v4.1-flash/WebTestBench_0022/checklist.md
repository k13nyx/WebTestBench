# Test Checklist

## Functionality
- [ ] FT-01: User can add an ingredient to the pantry list
  - Action: Enter an ingredient name (e.g., "Eggs") and a quantity (e.g., "12" or "1 dozen"), then confirm adding it.
  - Expected: The ingredient appears in the pantry list with the entered name and quantity.

- [ ] FT-02: User can attach an optional expiration date to a pantry ingredient
  - Action: Add or edit an ingredient and set an expiration date; optionally delete the date.
  - Expected: The expiration date is saved and shown when set, and the ingredient is still valid when no date is provided.

- [ ] FT-03: User can edit and delete existing pantry ingredients
  - Action: Change the quantity of an existing ingredient, then delete another ingredient.
  - Expected: The edited quantity is updated and the deleted ingredient is removed from the list.

- [ ] FT-04: User can generate a multi-day meal plan
  - Action: Set a number of days and trigger plan generation.
  - Expected: A plan is produced covering exactly the requested number of days.

- [ ] FT-05: User can view the plan day-by-day with recipes
  - Action: Inspect the generated plan.
  - Expected: Each day lists its meal(s) with a named recipe, grouped under a clear day heading.

- [ ] FT-06: Each recipe indicates exactly how much of each ingredient is used
  - Action: Open a recipe within the plan.
  - Expected: Every ingredient in the recipe shows a specific quantity used (not just a name).

- [ ] FT-07: User can view a grocery list of missing items
  - Action: Generate a plan that requires ingredients not fully in the pantry.
  - Expected: A grocery list is shown containing the missing ingredients with the amounts still needed.

- [ ] FT-08: User can lock meals/days and regenerate the rest
  - Action: Lock one meal (and separately one full day), then regenerate the plan.
  - Expected: Locked meals/days stay identical while the unlocked portions are regenerated into a new plan.

- [ ] FT-09: User can apply a preference to the generated plan
  - Action: Select vegetarian, high-protein, or budget-friendly and generate the plan.
  - Expected: The generated plan reflects the selected preference's intent across all days.

## Constraint
- [ ] CS-01: Empty or missing required pantry fields are rejected
  - Action: Attempt to add an ingredient with a blank name or blank quantity.
  - Expected: The ingredient is not added and an error message indicates the required fields.

- [ ] CS-02: Non-positive or non-numeric quantities are rejected
  - Action: Enter a quantity of "0", "-3", or "abc".
  - Expected: The value is rejected with a validation message and no invalid entry is saved.

- [ ] CS-03: Near-expiry ingredients are prioritized earlier in the plan
  - Action: Add two equivalent ingredients, set one to expire in 1–2 days and the other with no expiry, then generate the plan.
  - Expected: The soon-to-expire ingredient is scheduled earlier/before the non-expiring one in the day-by-day plan.

- [ ] CS-04: Locked meals and days are never altered by regeneration
  - Action: Lock a specific meal and a specific day, change preferences or unlock others, then regenerate.
  - Expected: The locked meal and locked day's contents remain byte-for-byte unchanged.

- [ ] CS-05: Ingredients already covered by the pantry are excluded from the grocery list
  - Action: Generate a plan where the pantry fully covers some required ingredients but not others.
  - Expected: Fully covered ingredients do not appear on the grocery list; only the shortfall items do.

- [ ] CS-06: Vegetarian preference excludes non-vegetarian recipes
  - Action: Select vegetarian and generate the plan.
  - Expected: No recipe containing meat, poultry, or seafood appears anywhere in the plan.

## Interaction
- [ ] IX-01: User receives feedback after regeneration
  - Action: Trigger regeneration after locking some meals.
  - Expected: A visible confirmation indicates the plan was regenerated, and the display updates without a full page reload.

- [ ] IX-02: Soon-to-expire pantry items are visually flagged
  - Action: Add an ingredient with an expiration date within the next few days and view the pantry list.
  - Expected: The item is visibly highlighted/marked as near-expiry or expired.

## Content
- [ ] CT-01: Recipe content is coherent and matches the theme of meal planning
  - Action: Review recipes across the generated plan.
  - Expected: Each recipe has a plausible meal name with realistic ingredient lists; no placeholder or irrelevant content.

- [ ] CT-02: Quantities, units, and dates are displayed consistently
  - Action: Inspect ingredient quantities, expiration dates, and grocery-list amounts.
  - Expected: All values use consistent unit formats and a clear date format throughout.