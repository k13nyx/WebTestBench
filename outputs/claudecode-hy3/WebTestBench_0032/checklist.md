# Test Checklist

## Functionality
- [ ] FT-01: Create a financial goal
  - Action: Open the goals section and add a new financial goal with a name and target amount.
  - Expected: The goal appears in the goals list with its defined name and target.

- [ ] FT-02: Create a monthly budget
  - Action: Open the budgets section and add a monthly budget with an amount and period.
  - Expected: The monthly budget is saved and visible in the budgets list.

- [ ] FT-03: Log an expense with amount and currency
  - Action: Open "Add Expense" and enter an amount and select a currency (e.g., USD, EUR).
  - Expected: The expense is recorded and shown in the expense list with its amount and currency.

- [ ] FT-04: Assign an expense to a category
  - Action: When logging an expense, select a category from the category list.
  - Expected: The expense is saved and displays the chosen category.

- [ ] FT-05: Choose a primary currency
  - Action: Open settings and select a primary currency (e.g., USD).
  - Expected: The selected currency is marked as primary and saved.

- [ ] FT-06: View all summaries in the primary currency
  - Action: Open the summary/dashboard view after setting a primary currency.
  - Expected: All totals and summaries are displayed in the primary currency.

- [ ] FT-07: View spending-vs-budget chart by category
  - Action: Open the charts view.
  - Expected: A chart shows each category's spending compared to its budget.

- [ ] FT-08: View spending-over-time chart
  - Action: Open the charts view.
  - Expected: A chart shows spending totals across time periods (e.g., by month).

- [ ] FT-09: Filter expense list by date range
  - Action: Apply a date range filter (start and end date) to the expense list.
  - Expected: Only expenses within the selected date range are displayed.

- [ ] FT-10: Filter expense list by category
  - Action: Select a category filter on the expense list.
  - Expected: Only expenses assigned to the selected category are displayed.

- [ ] FT-11: Filter expense list by goal
  - Action: Select a goal filter on the expense list.
  - Expected: Only expenses linked to the selected goal are displayed.

## Constraint
- [ ] CS-01: Required fields enforced when logging an expense
  - Action: Attempt to submit an expense with a missing amount, currency, or category.
  - Expected: The expense is rejected with a clear validation error for the missing field.

- [ ] CS-02: Non-primary currency expenses converted in summaries
  - Action: Log an expense in a non-primary currency (e.g., EUR) and view the summary in the primary currency (e.g., USD).
  - Expected: The expense total is converted and shown in the primary currency, not the original currency.

- [ ] CS-03: Date range filter validity enforced
  - Action: Apply a filter where the end date is earlier than the start date.
  - Expected: The filter is rejected with an error, and no invalid date range is applied.

## Interaction
- [ ] IX-01: Confirmation after creating goal, budget, or expense
  - Action: Successfully add a goal, a budget, and an expense.
  - Expected: A success confirmation (toast or message) appears after each successful creation.

- [ ] IX-02: Charts and summaries update on data change or filter
  - Action: Log a new expense or apply a filter, then view charts/summary.
  - Expected: Charts and summaries immediately reflect the new expense or active filter.

## Content
- [ ] CT-01: Currency labels shown correctly in summaries
  - Action: Review the summary and expense views.
  - Expected: Each monetary value shows the correct currency symbol/code of the displayed (primary) currency.

- [ ] CT-02: Chart labels are relevant and accurate
  - Action: Inspect the category and time charts.
  - Expected: Axes and legends show correct category names, time periods, and a spending-vs-budget reference with no irrelevant or placeholder text.