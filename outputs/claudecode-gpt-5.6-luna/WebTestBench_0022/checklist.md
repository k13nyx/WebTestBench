# Test Checklist

## Functionality
- [ ] FT-01: Existing pantry entries display ingredient names, quantities, units, and expiration dates when available.
  - Action: Open the **Pantry** list and inspect the default pantry entries.
  - Expected: Every entry shows its ingredient name and current quantity; entries with expiration dates show those dates.

- [ ] FT-02: User can update the quantity of an existing pantry item.
  - Action: Edit the quantity for one default pantry item and select **Save**.
  - Expected: The new quantity is saved and remains displayed after leaving and returning to the **Pantry** list.

- [ ] FT-03: User can set or change an expiration date for an existing pantry item.
  - Action: Select an existing pantry item, enter an expiration date, and select **Save**.
  - Expected: The selected expiration date appears on that pantry entry.

- [ ] FT-04: User can generate a multi-day meal plan.
  - Action: Select a planning duration of at least two days and select **Generate meal plan**.
  - Expected: A meal plan is generated with a separate section for every requested day.

- [ ] FT-05: Each planned day contains recipe information.
  - Action: Inspect every day in the generated **Meal plan**.
  - Expected: Each day displays at least one recipe with a recipe name and sufficient details to identify the meal.

- [ ] FT-06: Each recipe identifies the exact pantry ingredients and amounts it uses.
  - Action: Expand or inspect each planned recipe.
  - Expected: Every listed ingredient includes a specific quantity and unit, and pantry ingredients used by the recipe are identifiable.

- [ ] FT-07: The application generates a grocery list for missing ingredients.
  - Action: Review the **Grocery list** after generating a meal plan.
  - Expected: The list contains each ingredient needed but unavailable in sufficient pantry quantity, including the quantity and unit to buy.

- [ ] FT-08: User can generate plans using supported preferences.
  - Action: Generate a plan separately with **Vegetarian**, **High-protein**, and **Budget-friendly** selected.
  - Expected: Each generated plan reflects the selected preference: vegetarian plans contain no meat or seafood, high-protein plans identify protein-focused meals or amounts, and budget-friendly plans identify lower-cost meal choices.

- [ ] FT-09: User can lock a meal or day and regenerate only the remaining plan.
  - Action: Select **Lock** on one meal or day, then select **Regenerate plan**.
  - Expected: The locked meal or day remains unchanged, while unlocked meals or days are regenerated without requiring the user to start a new plan.

## Constraint
- [ ] CS-01: Pantry quantities cannot be saved as empty, zero, or negative values.
  - Action: Edit an existing pantry quantity using an empty value, `0`, and a negative number, selecting **Save** after each attempt.
  - Expected: Each invalid value is rejected with a validation message, and the invalid quantity is not saved.

- [ ] CS-02: Expiration dates are optional.
  - Action: Leave the expiration date blank for an existing pantry item and select **Save**.
  - Expected: The item saves successfully without an expiration date and remains available for meal planning.

- [ ] CS-03: Meal planning prioritizes food that is closest to expiring when usable.
  - Action: Generate a plan using default pantry data containing items with different expiration dates.
  - Expected: Recipes use the soonest-expiring usable ingredients before later-expiring or undated ingredients where the recipes and selected preferences allow.

- [ ] CS-04: Generated recipes respect the selected dietary preference.
  - Action: Select **Vegetarian** and generate a meal plan.
  - Expected: No planned recipe or listed ingredient contains meat, poultry, fish, or seafood.

- [ ] CS-05: Planned pantry usage does not exceed available quantities.
  - Action: Compare each recipe’s stated pantry usage with the corresponding pantry quantities.
  - Expected: The total planned usage of every pantry item is no greater than its available quantity; any shortfall appears in the **Grocery list**.

- [ ] CS-06: Locked meals and days are excluded from regeneration.
  - Action: Lock one meal and one full day, then select **Regenerate plan**.
  - Expected: Neither locked selection changes, while only unlocked selections can change.

## Interaction
- [ ] IX-01: Saving a pantry change provides clear completion feedback.
  - Action: Change an existing pantry quantity or expiration date and select **Save**.
  - Expected: A visible success confirmation appears, and the updated value is immediately shown in the pantry list.

- [ ] IX-02: Generating or regenerating a plan updates the displayed plan and grocery list.
  - Action: Generate a plan, change an unlocked planning option or preference, and select **Regenerate plan**.
  - Expected: The affected unlocked plan content and **Grocery list** refresh to reflect the new result without displaying stale entries.

- [ ] IX-03: Lock controls clearly show locked and unlocked states.
  - Action: Select **Lock** on a meal or day, then select the same control again if available.
  - Expected: The control visibly changes to a **Locked** state after the first action and returns to an unlocked state after the second action.

## Content
- [ ] CT-01: Day labels and meal order are clear and chronological.
  - Action: Review the generated multi-day plan from the first day to the last.
  - Expected: Every requested day has a distinct, readable label, and days appear in chronological order without missing or duplicate day labels.

- [ ] CT-02: Ingredient names are consistent across the pantry, recipes, and grocery list.
  - Action: Compare ingredients appearing in the **Pantry**, recipe details, and **Grocery list**.
  - Expected: The same ingredient is represented with consistent naming, and pantry quantities, recipe usage, and missing quantities are understandable.

- [ ] CT-03: Preference and expiration information is visible in the generated plan.
  - Action: Generate a plan with a supported preference and inspect the recipe and meal details.
  - Expected: The plan clearly identifies the selected preference context and shows which near-expiration pantry ingredients are being used when applicable.