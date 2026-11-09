# Test Result

## Functionality
- [X] FT-01: Add an ingredient with an expiration date to the pantry
  - Action: In the pantry section, fill in ingredient name, quantity, and expiration date, then click the "Add" button.
  - Expected: The new ingredient appears in the pantry list showing its name, quantity, and expiration date.

- [X] FT-02: Add an ingredient without an expiration date
  - Action: In the pantry section, fill in only ingredient name and quantity (leave expiration date empty), then click "Add".
  - Expected: The ingredient is saved and displayed in the pantry list with no expiration error.

- [X] FT-03: Generate a multi-day meal plan
  - Action: Click the "Generate Meal Plan" button without changing any settings.
  - Expected: A day-by-day plan is displayed (e.g., Day 1, Day 2, Day 3), with each day showing one or more recipes.

- [X] FT-04: Each recipe shows exact ingredient quantities used
  - Action: Open any recipe in the generated plan and view its ingredient list.
  - Expected: Every ingredient is listed with a specific amount (e.g., "Rice: 200 g"), not just a name.

- [X] FT-05: Grocery list is produced for missing items
  - Action: After generating a meal plan, open the grocery list section.
  - Expected: The grocery list shows ingredients required by the plan that are missing (or insufficient) in the pantry, with the needed quantities.

- [X] FT-06: Regeneration replaces unlocked days with new recipes
  - Action: Leave at least one day unlocked (or unlock all), click "Regenerate", and compare the unlocked days' recipes before and after.
  - Expected: Unlocked days show different recipes than before.

- [X] FT-07: Vegetarian preference produces a meat-free plan
  - Action: Select the "Vegetarian" preference, click "Generate Meal Plan", and inspect all recipe ingredient lists.
  - Expected: Every recipe in the plan contains no meat or fish ingredients.

- [ ] FT-08: Ingredients closest to expiring are prioritized in earliest days
  - Action: Identify the pantry item (from default data) with the earliest expiration date, generate a plan, and check which day's recipes use it.
  - Expected: That item is used in the recipes of Day 1 (or the earliest days), not left unused while later days are planned.
  - Bug Report:
    - Issue: Expiration-based prioritization not applied (feature gap)
    - Actual: The default-data item with the earliest expiration date is Spinach (2024-12-14, confirmed via app state). After generating a plan with default settings (verified across two separate generations), Spinach is not used in any day's recipes — Day 1 or otherwise. The "Ingredient Usage" section lists only Chicken Breast, Rice, Greek Yogurt, Onions, Bell Peppers, Garlic, and Olive Oil (plus Pasta/Tomatoes/Cheese on the second run) — no spinach recipe appears anywhere in the plan, while all 5 days are fully planned. Spinach was only used (in Day 1) when the Vegetarian preference was selected, so default-settings generation leaves the earliest-expiring item completely unused.

- [X] FT-09: Preferences can be applied to regeneration
  - Action: With an existing plan, select "High-Protein" and click "Regenerate".
  - Expected: The regenerated unlocked days reflect the high-protein preference (recipes emphasize protein-rich ingredients).

## Constraint
- [X] CS-01: Cannot add a pantry ingredient with empty required fields
  - Action: Click the pantry "Add" button with the ingredient name or quantity left empty.
  - Expected: The ingredient is not added; a validation message or blocked submission indicates the required fields.

- [X] CS-02: Grocery list excludes items already covered by the pantry
  - Action: Compare the grocery list against the pantry and the plan's ingredient requirements.
  - Expected: Items with sufficient quantity in the pantry do not appear on the grocery list; only missing/insufficient items are listed.

- [X] CS-03: Locked days remain identical after regeneration
  - Action: Lock one day (and its meals), click "Regenerate", and compare the locked day's recipes before and after.
  - Expected: The locked day's recipes are unchanged and in the same order.

- [X] CS-04: Ingredient usage cannot silently exceed pantry stock
  - Action: For any ingredient in the plan, check its usage across all days against its pantry quantity and grocery list.
  - Expected: Usage beyond pantry quantity is accounted for on the grocery list (shortfall amount), never omitted.

## Interaction
- [X] IX-01: Lock control shows clear on/off state
  - Action: Click the lock control on a day or meal, then click it again.
  - Expected: The control visibly toggles (e.g., open vs. closed lock icon or label change) so locked and unlocked states are distinguishable at a glance.

- [X] IX-02: Feedback is shown when a plan is generated
  - Action: Click "Generate Meal Plan" and observe the interface.
  - Expected: A loading indicator or success confirmation appears, and the plan section refreshes with the new plan.

- [X] IX-03: Selected preference is visibly highlighted
  - Action: Click a preference option (e.g., "Vegetarian") before generating.
  - Expected: The selected option shows a visible selected state (highlight/checkbox), and others appear unselected.

- [X] IX-04: Newly added pantry item appears immediately
  - Action: Add a valid ingredient to the pantry and observe the pantry list.
  - Expected: The new entry appears in the list immediately, without requiring a page reload.

## Content
- [ ] CT-01: Pantry list displays complete and accurate ingredient data
  - Action: Review each pantry item shown from the default data.
  - Expected: Every item displays its name, quantity (with unit), and — where present — its expiration date, matching the stored values.
  - Bug Report:
    - Issue: Missing data display (expiration date values never rendered)
    - Actual: Each pantry card shows only category, name, quantity with unit (e.g., "Chicken Breast", "500 g"), and a status badge. The stored expiration date values (2024-12-14 … 2024-12-30, confirmed via app state) are not displayed anywhere: all 12 dated default items show only a generic red "Expired" badge, and the added item shows "68 days" — no actual date value (no "2027-01-15", no "Dec 16, 2024"), and no title/tooltip attribute carries it. The displayed data therefore cannot be matched against the stored expiration dates.

- [X] CT-02: Plan days and meals are clearly labeled
  - Action: Review the generated plan layout.
  - Expected: Each day is labeled in order (e.g., "Day 1", "Day 2"), and each recipe shows a meal-appropriate title and meal slot (e.g., breakfast/lunch/dinner), with no placeholder text.

- [X] CT-03: Expiring pantry items are visually distinguished
  - Action: Compare pantry items with early expiration dates against items with later or no dates.
  - Expected: Items close to expiring are visibly flagged (e.g., "expiring soon" label or highlighted date), while others are not.
