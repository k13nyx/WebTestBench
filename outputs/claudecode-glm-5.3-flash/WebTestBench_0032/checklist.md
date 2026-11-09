# Test Checklist

## Functionality
- [ ] FT-01: Create a new financial goal
  - Action: Open the goals section, click the add-goal control, enter a name (e.g., "Vacation Fund") and a target amount, then save.
  - Expected: The goal "Vacation Fund" appears in the goals list with its target amount displayed.
- [ ] FT-02: Create a monthly budget for a category
  - Action: In the budgets section, add or edit a monthly budget for an existing category (e.g., "Groceries" = 500 in primary currency) and save.
  - Expected: The monthly budget of 500 for "Groceries" is shown and persists after reload.
- [ ] FT-03: Log a new expense in the primary currency
  - Action: Use the "Add Expense" form: enter amount 50, currency = primary currency, pick a category (e.g., "Groceries"), set today's date, save.
  - Expected: The expense appears in the expense list with amount 50, its category, and today's date.
- [ ] FT-04: Log an expense in a non-primary currency
  - Action: Add an expense with amount 100, currency = a non-primary currency (e.g., EUR if primary is USD), assign a category, save.
  - Expected: The expense is saved; the list shows it with its original currency (e.g., €100), and any summary/total reflects its converted value in the primary currency.
- [ ] FT-05: Assign an expense to a goal
  - Action: Add or edit an expense and select an existing goal (e.g., "Vacation Fund") in the goal field, then save.
  - Expected: The expense list (and/or goal detail) shows the expense linked to that goal.
- [ ] FT-06: Change the primary currency
  - Action: Open the currency settings, change the primary currency (e.g., USD → EUR), and confirm.
  - Expected: All summary totals, budgets, and chart values are re-displayed using the new primary currency symbol/code.
- [ ] FT-07: Category comparison chart shows spending vs budget
  - Action: With at least one expense and one budget defined, view the "spending by category" chart.
  - Expected: The chart displays each category's spending alongside/against its monthly budget, in the primary currency, and matches the expense totals.
- [ ] FT-08: Over-time chart shows spending trend
  - Action: With expenses on at least two different dates, view the "spending over time" chart.
  - Expected: The chart shows spending distributed across the time periods (e.g., days/months) in the primary currency, consistent with the logged expense dates.
- [ ] FT-09: Filter expense list by date range
  - Action: Set a start and end date in the date-range filter that covers only some of the logged expenses.
  - Expected: The expense list shows only expenses dated within the range; totals update accordingly.
- [ ] FT-10: Filter expense list by category
  - Action: Select a single category (e.g., "Groceries") in the category filter.
  - Expected: Only expenses assigned to "Groceries" remain in the list.
- [ ] FT-11: Filter expense list by goal
  - Action: Select an existing goal in the goal filter.
  - Expected: Only expenses linked to that goal remain in the list.
- [ ] FT-12: Combine multiple filters
  - Action: Apply a date range AND a category AND a goal filter simultaneously.
  - Expected: The list shows only expenses satisfying all three filters at once.
- [ ] FT-13: Clear/reset filters
  - Action: After applying filters, click the clear/reset (or "All") control.
  - Expected: All logged expenses are shown again, unfiltered.

## Constraint
- [ ] CS-01: Expense cannot be saved with missing required fields
  - Action: Open the "Add Expense" form, leave the amount (or category) empty, and click save/submit.
  - Expected: The expense is not created; a validation message is shown for the empty required field.
- [ ] CS-02: Expense cannot be saved with an invalid date range filter
  - Action: In the date filter, set a start date that is after the end date.
  - Expected: The filter is rejected, corrected, or shows a validation message — not an empty/garbled result presented as valid.
- [ ] CS-03: Every expense must belong to a valid category
  - Action: Inspect the "Add Expense" form's category field and attempt to save without a selectable/valid category.
  - Expected: The category field only offers existing categories (plus default ones) and saving is blocked until one is chosen — no uncategorized expense is created.
- [ ] CS-04: A primary currency must be set before summaries are meaningful
  - Action: On first load (or after clearing settings), check the summary/chart area's currency handling.
  - Expected: A primary currency is pre-selected (default data) or the app requires one to be chosen; summaries never display without a defined currency.

## Interaction
- [ ] IX-01: Adding an expense updates list and summaries immediately
  - Action: Add a valid expense and observe the expense list, totals, and charts without reloading the page.
  - Expected: The new expense appears in the list and the summary totals/charts reflect it immediately (no manual refresh required).
- [ ] IX-02: Over-budget category is visually highlighted
  - Action: Log expenses in a category until its spending exceeds its monthly budget, then view the budget/category chart or budget list.
  - Expected: The over-budget category is visually distinguished (e.g., red color, warning icon, or "over budget" label).
- [ ] IX-03: Chart elements respond to hover with details
  - Action: Hover over a bar/segment/point in either chart.
  - Expected: A tooltip or highlight shows the specific value (amount in primary currency and the category or period name).

## Content
- [ ] CT-01: Default sample data is present on first load
  - Action: Open the page fresh (no user actions).
  - Expected: At least some default data is visible (e.g., default categories like "Groceries", sample expenses or budgets) so the page is usable immediately.
- [ ] CT-02: All monetary values display the correct currency symbol/code
  - Action: Review the expense list, summaries, budgets, and charts.
  - Expected: Every amount is displayed with a currency symbol or code; original currencies show their own symbol, and all aggregated summaries show the primary currency's symbol consistently.