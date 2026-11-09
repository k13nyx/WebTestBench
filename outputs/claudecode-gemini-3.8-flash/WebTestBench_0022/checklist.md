# Test Checklist

## Functionality
- [ ] FT-01: Add a new ingredient to the pantry list
  - Action: Enter "Spinach" in the ingredient name field, set quantity to "200g", select a date 2 days from today in the optional expiration date picker, and click "Add Ingredient".
  - Expected: "Spinach" appears in the pantry table displaying "200g" and the selected expiration date.

- [ ] FT-02: Add an ingredient without an expiration date
  - Action: Enter "Olive Oil", set quantity to "500ml", leave the expiration date input blank, and click "Add Ingredient".
  - Expected: "Olive Oil" is added to the pantry list with expiration date shown as "None" or "N/A".

- [ ] FT-03: Remove an ingredient from the pantry
  - Action: Click the "Delete" icon button on a default pantry item row (e.g., "Eggs").
  - Expected: The item is immediately removed from the pantry list view.

- [ ] FT-04: Generate a multi-day meal plan with dietary preferences
  - Action: Select the "Vegetarian" and "Budget-Friendly" preference checkboxes, choose "3 Days" from the duration dropdown, and click "Generate Meal Plan".
  - Expected: A 3-day meal plan renders displaying breakfast, lunch, and dinner recipes that align with vegetarian and budget-friendly criteria.

- [ ] FT-05: Prioritize ingredients nearing expiration
  - Action: Ensure an ingredient (e.g., "Milk") expires tomorrow and click "Generate Meal Plan".
  - Expected: "Milk" is scheduled into meals on Day 1 rather than later days in the plan.

- [ ] FT-06: Display exact ingredient usage per recipe
  - Action: Inspect any generated recipe card on the day-by-day plan.
  - Expected: The recipe lists exact quantities deducted from pantry inventory (e.g., "Uses: 100g of 200g Spinach").

- [ ] FT-07: Generate grocery list for missing ingredients
  - Action: Click the "Grocery List" tab/section after generating a meal plan that requires ingredients not available in the pantry.
  - Expected: A grocery list is populated showing all missing items and their required shortfall quantities.

- [ ] FT-08: Lock a specific meal
  - Action: Click the "Lock" button on Day 1 Lunch.
  - Expected: The meal card reflects a locked state and cannot be replaced during partial regeneration.

- [ ] FT-09: Lock an entire day
  - Action: Click the "Lock Day" button located in the header of Day 2.
  - Expected: All meal cards under Day 2 show locked indicators.

- [ ] FT-10: Regenerate unlocked meals while preserving locked items
  - Action: With Day 1 Lunch locked and all other meals unlocked, click "Regenerate Unlocked".
  - Expected: Day 1 Lunch recipe remains identical, while unlocked meals update with new recipes.

## Constraint
- [ ] CS-01: Prevent adding pantry item with missing name or non-positive quantity
  - Action: Leave the ingredient name input empty, enter "0" in quantity, and click "Add Ingredient".
  - Expected: Form submission is blocked, and validation messages "Ingredient name is required" and "Quantity must be greater than 0" are displayed.

- [ ] CS-02: Enforce dietary preference restriction
  - Action: Select the "Vegetarian" filter and click "Generate Meal Plan".
  - Expected: Zero recipes containing meat, poultry, or seafood are included anywhere in the generated plan.

- [ ] CS-03: Disable regeneration when all meals are locked
  - Action: Lock every meal across all planned days.
  - Expected: The "Regenerate Unlocked" button becomes disabled or shows a tooltip stating "All meals are locked".

## Interaction
- [ ] IX-01: Toggle meal lock state icon
  - Action: Click the lock icon button on any unlocked meal card.
  - Expected: The icon transitions from an open padlock to a closed padlock with highlighted active styling.

- [ ] IX-02: Expand recipe details card
  - Action: Click "View Recipe" on any scheduled meal card.
  - Expected: The card expands or opens a modal revealing step-by-step cooking instructions and prep time.

- [ ] IX-03: Check off grocery list items
  - Action: Click the checkbox next to any item in the grocery list.
  - Expected: The item text displays a strikethrough style and the checkbox shows a checked state.

## Content
- [ ] CT-01: Day-by-day plan layout structure
  - Action: Review the generated meal plan interface.
  - Expected: Plan is chronologically organized by day headers (e.g., "Day 1", "Day 2") with distinct meal slots (Breakfast, Lunch, Dinner).

- [ ] CT-02: Grocery list item data integrity
  - Action: Compare an ingredient shortfall from a recipe against the grocery list item.
  - Expected: Item name, quantity deficit, and measurement unit exactly match the difference between recipe requirements and pantry inventory.