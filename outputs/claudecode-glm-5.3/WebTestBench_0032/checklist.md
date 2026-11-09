# Test Checklist

## Functionality

- [ ] FT-01: Create a financial goal
  - Action: Open the Goals section, enter a goal name (e.g., "Emergency Fund") and a target amount, then save.
  - Expected: The new goal appears in the goals list showing the entered name and target amount.

- [ ] FT-02: Define a monthly budget
  - Action: Select an existing category, enter a monthly budget amount, and save.
  - Expected: The budget is stored and displayed as that category's budget for the chosen month.

- [ ] FT-03: Log an expense in a non-primary currency
  - Action: Add an expense with an amount and a currency different from the primary currency (e.g., EUR or GBP), then save.
  - Expected: The expense appears in the expense list showing the exact amount and currency entered.

- [ ] FT-04: Assign an expense to a category
  - Action: While adding an expense, choose a category from the category selector and save.
  - Expected: The saved expense is displayed with the selected category in the expense list.

- [ ] FT-05: Primary currency selection converts all summaries
  - Action: Change the primary currency (e.g., from USD to EUR).
  - Expected: All summary figures (total spending, budget comparisons, chart values) re-display converted into the newly selected primary currency.

- [ ] FT-06: Filter expenses by date range
  - Action: Apply a date range that includes only some of the default expenses.
  - Expected: Only expenses dated within the range are listed; expenses outside the range are excluded.

- [ ] FT-07: Filter expenses by category
  - Action: Apply the category filter for one existing category.
  - Expected: Only expenses assigned to that category are shown.

- [ ] FT-08: Filter expenses by goal
  - Action: Apply the goal filter for one existing goal.
  - Expected: Only expenses linked to that goal are shown.

- [ ] FT-09: Combine all three filters
  - Action: Apply a date range, a category, and a goal filter at the same time.
  - Expected: The list shows only expenses that satisfy all three conditions simultaneously.

- [ ] FT-10: Budget vs. spending chart by category
  - Action: Open the category comparison chart for a month that has budgets set.
  - Expected: Each category shows its actual spending next to its monthly budget (a clear spending-vs-budget comparison).

- [ ] FT-11: Spending over time chart
  - Action: Open the spending-over-time chart.
  - Expected: The chart shows spending totals per time period (e.g., per month) matching the logged expense data.

## Constraint

- [ ] CS-01: Expense form rejects invalid input
  - Action: Attempt to save an expense with an empty amount, or a non-numeric / negative / zero amount.
  - Expected: The expense is not saved and a validation error is displayed.

- [ ] CS-02: Goal form rejects invalid input
  - Action: Attempt to save a goal with an empty name, or an empty / negative target amount.
  - Expected: The goal is not saved and the invalid fields are indicated.

- [ ] CS-03: Monthly budget rejects invalid amount
  - Action: Attempt to save a monthly budget with a negative or zero amount.
  - Expected: The budget is not saved and a validation error is displayed.

## Interaction

- [ ] IX-01: Feedback after logging an expense
  - Action: Save a new expense via the expense form.
  - Expected: A success confirmation (message/toast) appears and the new expense is immediately visible in the list.

- [ ] IX-02: Filters update the list instantly
  - Action: Change a filter value (e.g., switch category) while viewing the expense list.
  - Expected: The list refreshes immediately to show the matching expenses without a full page reload.

- [ ] IX-03: Resetting filters restores the full list
  - Action: With active filters applied, reset/clear the filters.
  - Expected: The expense list returns to showing all default expenses.

## Content

- [ ] CT-01: All summary amounts are labeled in the primary currency
  - Action: Inspect every summary total, budget figure, and chart value on the page.
  - Expected: Each amount is labeled with the primary currency's symbol/code (e.g., "$" or "USD"), with no mixed or unlabeled currencies.

- [ ] CT-02: Chart labels match the actual data
  - Action: Inspect chart titles, axis labels, and legends.
  - Expected: The category chart uses the real category names, the time chart uses the real time periods (e.g., month names), and no placeholder or empty labels appear.

- [ ] CT-03: Expense list entries are complete and accurate
  - Action: Inspect a row of an expense logged in a foreign currency.
  - Expected: The row displays the original amount with its currency code as entered, plus its date, category, and assigned goal — nothing missing or garbled.