# Test Checklist

## Functionality
- [ ] FT-01: User can define a new financial goal
  - Action: Open the goal-creation form, enter a name (e.g., "Emergency Fund") and a target amount, and save.
  - Expected: The goal is saved and appears in the goals list with its name and target amount.

- [ ] FT-02: User can define monthly budgets per category
  - Action: Open the budget form, set a monthly budget for at least two categories (e.g., Groceries 400, Rent 1200), and save.
  - Expected: Each budget is listed showing category, monthly amount, and applies to the current month's summaries.

- [ ] FT-03: User can log an expense in a non-primary currency and assign it to a category and goal
  - Action: Add an expense with amount 50, currency EUR, a date, a category (e.g., "Dining"), and a goal (e.g., "Vacation Fund"); save.
  - Expected: The expense appears in the expense list showing amount with "EUR", its category, and its assigned goal.

- [ ] FT-04: User can select a primary currency
  - Action: Use the primary-currency selector to switch from the current primary currency to another (e.g., USD → EUR).
  - Expected: The selection persists and all summary totals on the page are immediately re-displayed in EUR.

- [ ] FT-05: Summaries convert multi-currency expenses into the primary currency
  - Action: With USD as primary currency, view the total-spent summary while default expenses in other currencies (e.g., EUR, JPY) exist.
  - Expected: The summary shows a single USD total; no foreign-currency amounts are summed unconverted into it.

- [ ] FT-06: Chart compares spending vs. budget by category
  - Action: View the "Spending by Category" chart.
  - Expected: A chart renders with one entry per budgeted category, visually showing actual spending against that category's budget.

- [ ] FT-07: Chart shows spending over time
  - Action: View the "Spending Over Time" chart.
  - Expected: A chart renders showing total spending per time period (e.g., per month), with each period's spending value plotted.

- [ ] FT-08: Expense list can be filtered by date range
  - Action: Set a start and end date covering only some default expenses, and apply the filter.
  - Expected: The list shows only expenses dated within the range; expenses outside it are hidden.

- [ ] FT-09: Expense list can be filtered by category
  - Action: Select a single category in the category filter.
  - Expected: The list shows only expenses in that category; clearing the filter restores the full list.

- [ ] FT-10: Expense list can be filtered by goal
  - Action: Select a specific goal in the goal filter.
  - Expected: The list shows only expenses assigned to that goal.

## Constraint
- [ ] CS-01: Expense cannot be saved with missing required fields
  - Action: Open the add-expense form, leave required fields (e.g., amount, date, category) empty, and submit.
  - Expected: The expense is rejected, a validation indication appears on the missing fields, and no new row is added to the list.

- [ ] CS-02: Invalid expense amounts are rejected
  - Action: Enter an expense with amount 0 or a negative/non-numeric value and attempt to save.
  - Expected: The save is blocked with a validation message; the expense is not added.

- [ ] CS-03: Only one monthly budget per category
  - Action: Try to create a second budget for a category that already has a budget for the same month.
  - Expected: The duplicate is prevented (error message, or the existing budget is updated rather than a second entry created).

- [ ] CS-04: Expenses cannot reference non-existent categories or goals
  - Action: Open the add-expense form and inspect the category and goal fields.
  - Expected: Category and goal are chosen from the existing defined options only; free-text entries for undefined categories/goals are not accepted.

## Interaction
- [ ] IX-01: Success feedback after adding an item
  - Action: Save a new goal, budget, and expense.
  - Expected: Each successful save produces a visible confirmation (e.g., toast or success message) and the relevant list/summary updates without a manual page reload.

- [ ] IX-02: Filtering updates results live, including an empty state
  - Action: Apply a filter combination that matches no default expenses (e.g., a category with no expenses in a narrow date range).
  - Expected: The list updates to show an explicit "no results" message rather than an unexplained blank area or stale rows.

- [ ] IX-03: Chart hover reveals values
  - Action: Hover over a bar/segment in the category chart and a point/period in the time chart.
  - Expected: A tooltip (or equivalent) shows the specific value(s), e.g., category spend vs. budget, and the amount for the hovered time period.

## Content
- [ ] CT-01: Default data is present and spans multiple currencies and categories
  - Action: Load the page fresh and inspect the goals, budgets, and expense lists.
  - Expected: Pre-existing goals, monthly budgets, and sample expenses across several currencies, categories, and dates are displayed, sufficient to exercise filters and charts.

- [ ] CT-02: Monetary values are labeled with the correct currency
  - Action: Inspect expense list rows, budget entries, and summary totals.
  - Expected: Every monetary value displays a currency symbol or code; per-expense amounts show the entered currency, summaries show the primary currency only.