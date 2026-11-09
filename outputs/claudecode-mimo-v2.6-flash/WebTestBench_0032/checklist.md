# Test Checklist

## Functionality
- [ ] FT-01: Create a financial goal with a name and target amount
  - Action: Open the goals section, create a new goal (e.g., "Vacation Fund", target 2000) and save.
  - Expected: The goal appears in the goals list with its name and target amount intact after reload.
- [ ] FT-02: Create a monthly budget for a category
  - Action: Open the budgets section, set a monthly amount (e.g., "Groceries" = 400) for the current month and save.
  - Expected: The budget is saved and displayed for that category and month.
- [ ] FT-03: Log an expense in a non-primary currency and assign it to a category and goal
  - Action: Add an expense with amount 50, currency EUR (when primary is USD), category "Groceries", a date, and an assigned goal, then save.
  - Expected: The expense appears in the expense list showing amount, currency, category, and goal as entered.
- [ ] FT-04: Select a primary currency
  - Action: Choose a primary currency (e.g., USD) in the currency setting.
  - Expected: The setting is saved as the primary currency and applies to the whole page.
- [ ] FT-05: Filter the expense list by date range
  - Action: Set a start and end date covering only part of the expense history and apply.
  - Expected: Only expenses dated within the range remain visible in the list.
- [ ] FT-06: Filter the expense list by category
  - Action: Select a single category filter (e.g., "Groceries") and apply.
  - Expected: Only expenses belonging to that category are shown.
- [ ] FT-07: Filter the expense list by goal
  - Action: Select a single goal filter and apply.
  - Expected: Only expenses assigned to that goal are shown.
- [ ] FT-08: Combine date range, category, and goal filters
  - Action: Apply all three filters at once with criteria that match a subset of expenses.
  - Expected: The list shows only expenses satisfying all three conditions simultaneously.

## Constraint
- [ ] CS-01: Expense cannot be saved with missing required fields
  - Action: Leave the amount (or category) empty and attempt to save an expense.
  - Expected: Saving is blocked and an inline validation message identifies the missing required field; no partial expense is created.
- [ ] CS-02: Expense amount must be a positive number
  - Action: Enter an amount of 0 or a negative value and attempt to save.
  - Expected: Saving is rejected with a validation error; the expense is not added.
- [ ] CS-03: Expense requires a valid currency selection
  - Action: Attempt to save an expense without choosing a currency.
  - Expected: Saving is blocked with a validation message prompting for a currency.
- [ ] CS-04: Invalid date range is rejected in filters
  - Action: Set the filter start date later than the end date and apply.
  - Expected: The filter does not apply; an error message indicates the start date must be on or before the end date.

## Interaction
- [ ] IX-01: Summaries and charts refresh after adding an expense
  - Action: Note the current category total, add a new expense in that category, and observe the summary and chart.
  - Expected: The category total and its chart bar/segment update to include the new expense without a manual refresh.
- [ ] IX-02: Budget-vs-spending chart displays per category
  - Action: Navigate to the charts section with at least one budget and one expense present.
  - Expected: A chart shows, for each category, both its budget and its actual spending, and the values match the recorded budgets/expenses.
- [ ] IX-03: Spending-over-time chart displays correctly
  - Action: View the time-series chart covering the dates of existing expenses.
  - Expected: A chart plots spending across the selected time periods and reflects the expense dates and amounts entered.
- [ ] IX-04: Clearing filters restores the full expense list
  - Action: Apply one or more filters, then reset/clear all filters.
  - Expected: All previously hidden expenses reappear in the list.

## Content
- [ ] CT-01: All summary totals are displayed in the primary currency with its symbol/code
  - Action: With primary currency set to USD, review every summary total (category totals, grand total, chart axis/labels).
  - Expected: Every total is labeled with the primary currency (e.g., "$" or "USD"); no summary shows a raw secondary-currency value.
- [ ] CT-02: Multi-currency expenses are converted consistently in summaries
  - Action: Compare the summary total against the sum of logged expenses entered in different currencies.
  - Expected: Each non-primary expense contributes an amount converted into the primary currency, and the grand total equals the sum of those converted values.
- [ ] CT-03: Charts use correct category and period labels
  - Action: Inspect the labels on both charts.
  - Expected: Each chart element is labeled with the actual category name or time period it represents, with no missing, blank, or mismatched labels.
- [ ] CT-04: Expense rows display complete, relevant data
  - Action: Review any row in the expense list.
  - Expected: The row shows the expense description/amount, its currency, its category, its date, and its assigned goal, all matching what was entered.