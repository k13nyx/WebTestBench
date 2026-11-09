# Test Checklist

## Functionality
- [ ] FT-01: User can view all default financial goals and monthly budgets.
  - Action: Open the Goals and Budgets section.
  - Expected: Every default goal shows its name, target amount, and progress. Every default monthly budget shows its category, limit, and month.
- [ ] FT-02: Expense list shows all default expenses with their core fields.
  - Action: Open the Expenses list with no filters applied.
  - Expected: Every default expense row shows date, description, amount, category, and goal. The row count matches the default data.
- [ ] FT-03: Add Expense form offers multiple currencies.
  - Action: Click "Add Expense" and open the Currency dropdown. Close the form without saving.
  - Expected: The dropdown lists at least 3 currencies, each with its code and name. No expense is saved.
- [ ] FT-04: Selecting a primary currency converts all summaries to that currency.
  - Action: Note the current primary currency. Open Settings, select a different currency, and save. Check the dashboard totals. Restore the original currency afterward.
  - Expected: All dashboard totals, budget figures, and goal amounts display in the newly selected currency with its symbol.
- [ ] FT-05: Date range filter shows only expenses within the range.
  - Action: Set "From" and "To" dates that cover part of the default expense dates. Click "Apply".
  - Expected: Only expenses dated within the range (inclusive) appear. Expenses outside the range are hidden.
- [ ] FT-06: Category filter shows only expenses in the selected category.
  - Action: Select one category in the Category filter and apply it.
  - Expected: Only expenses assigned to that category appear.
- [ ] FT-07: Goal filter shows only expenses linked to the selected goal.
  - Action: Select one goal in the Goal filter and apply it.
  - Expected: Only expenses linked to that goal appear.
- [ ] FT-08: Combined filters return the intersection of all criteria.
  - Action: Set a date range, one category, and one goal together. Apply the filters.
  - Expected: Only expenses matching all three criteria appear. Each visible row matches every selected filter.
- [ ] FT-09: "Budget vs. Spending by Category" chart matches the default data.
  - Action: Open the category comparison chart. Compare each category's bars to the budget limit and the expense total for that category in the default data.
  - Expected: Each category shows a budget bar and a spending bar. The values match the budgets and expense totals for the displayed period.
- [ ] FT-10: "Spending Over Time" chart matches the default expense data.
  - Action: Open the spending-over-time chart. Compare each period's value to the sum of that period's expenses in the expense list.
  - Expected: Each period's point or bar matches the expense total for that period, in the primary currency.

## Constraint
- [ ] CS-01: Expense cannot be saved with required fields empty.
  - Action: Open "Add Expense", leave Amount, Category, Currency, and Date blank, and click "Save".
  - Expected: The form is not saved. Each empty required field shows an error message. No new row appears in the expense list.
- [ ] CS-02: Expense amount must be a positive number.
  - Action: Open "Add Expense", enter "-5" in Amount, fill the other required fields, and click "Save". Repeat with "0" and "abc".
  - Expected: Each attempt is rejected with an error such as "Amount must be greater than zero" or "Enter a valid number". No expense is saved.
- [ ] CS-03: Date range filter rejects a start date later than the end date.
  - Action: Set "From" to a date after "To" and click "Apply".
  - Expected: An error such as "Start date must be before end date" appears. The list does not show results for the invalid range.
- [ ] CS-04: Changing the primary currency does not alter stored expenses.
  - Action: Note the amount and currency code of several default expenses. Change the primary currency, then return to the expense list. Restore the original currency afterward.
  - Expected: Each expense still shows its original amount and currency code. Only the summaries change.

## Interaction
- [ ] IX-01: Result count updates after every filter change.
  - Action: Apply a date range, then a category, then a goal, and observe the result label.
  - Expected: The label (for example, "Showing X of Y expenses") updates to match the visible rows after each change.
- [ ] IX-02: Hovering a chart bar shows a tooltip with its details.
  - Action: Hover over one category bar in "Budget vs. Spending by Category" and one point in "Spending Over Time".
  - Expected: A tooltip appears showing the category or period name and its values in the primary currency.
- [ ] IX-03: "Clear" resets all filters and restores the full list.
  - Action: Apply a date range, category, and goal. Click "Clear" or "Reset Filters".
  - Expected: All filter fields return to their default values. The expense list shows all default expenses again, and the result count matches the full total.

## Content
- [ ] CT-01: Category labels are meaningful and consistent.
  - Action: Review the category names in the expense list, filter dropdown, and both charts.
  - Expected: Each category uses the same name in every location. No label is blank, generic, or reads "undefined".
- [ ] CT-02: Each expense amount shows the currency it was logged in.
  - Action: Review the amount column in the expense list for default expenses in different currencies.
  - Expected: Each amount displays the correct symbol or code for its original currency (for example, a EUR expense shows "€" or "EUR", not the primary currency).
- [ ] CT-03: No placeholder or error text appears on any page.
  - Action: Review the dashboard, goals, budgets, expense list, and both charts.
  - Expected: No visible text reads "undefined", "NaN", "null", "lorem ipsum", or "TODO". No chart shows an empty or broken label.