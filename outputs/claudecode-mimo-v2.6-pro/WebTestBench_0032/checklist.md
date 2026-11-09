# Test Checklist

## Functionality
- [ ] FT-01: The user can create several financial goals, each with a name and a target amount.
  - Action: Open the goal creation form and create two goals: "Vacation" with target 2000 and "New Laptop" with target 1500.
  - Expected: Both goals are saved and listed in the Goals section with their names and target amounts.

- [ ] FT-02: The user can define monthly budgets per category.
  - Action: Open the budget creation form and create two budgets for the current month: "Groceries" 500 and "Transport" 200.
  - Expected: Both budgets are saved and listed in the Budgets section with their month, category, and amount.

- [ ] FT-03: The user can log an expense with amount, date, currency, and category.
  - Action: Log an expense: amount 45, currency set to a currency different from the primary currency (e.g., EUR), category "Groceries", date today.
  - Expected: The expense is saved and appears in the expense list.

- [ ] FT-04: The user can assign an expense to a financial goal.
  - Action: When logging an expense (amount 25, any valid currency, today's date), select the goal "Vacation" and a category.
  - Expected: The expense is saved and the expense list shows it assigned to the goal "Vacation".

- [ ] FT-05: The user can choose a primary currency, and all summaries are shown in that currency.
  - Action: Set the primary currency to USD via the primary currency selector, then open the summary section.
  - Expected: The setting is applied and every summary figure is displayed in USD.

- [ ] FT-06: Expenses logged in other currencies are converted into the primary currency in summaries.
  - Action: With primary currency USD, view the summaries containing an expense logged in a different currency (e.g., the 45 EUR expense from FT-03).
  - Expected: The summary totals include that expense converted and displayed in USD.

- [ ] FT-07: A chart shows spending compared to budget by category.
  - Action: With budgets and expenses in place (e.g., from FT-02 and FT-03), open the spending-vs-budget chart.
  - Expected: For each category with a budget, the chart shows both the budgeted amount and the actual spending of that category, in the primary currency.

- [ ] FT-08: A chart shows spending over time.
  - Action: With expenses dated across different periods, open the spending-over-time chart.
  - Expected: The chart shows total spending for each month that contains expenses, in the primary currency.

- [ ] FT-09: The expense list can be filtered by date range.
  - Action: Set the date range filter to a range that contains only some of the existing expenses (e.g., the current month).
  - Expected: The list shows exactly the expenses dated within the range and excludes all expenses outside it.

- [ ] FT-10: The expense list can be filtered by category.
  - Action: Select in the category filter a category that has expenses (e.g., "Groceries").
  - Expected: The list shows only expenses whose category matches the selected one.

- [ ] FT-11: The expense list can be filtered by goal.
  - Action: Select in the goal filter a goal that has expenses assigned (e.g., "Vacation").
  - Expected: The list shows only expenses assigned to that goal; expenses with no goal or a different goal are excluded.

- [ ] FT-12: Filters can be combined to narrow the expense list.
  - Action: Apply a date range filter and a category filter at the same time (e.g., current month + "Groceries").
  - Expected: The list shows only expenses that match both filters simultaneously.

## Constraint
- [ ] CS-01: An expense cannot be saved with a missing, zero, or negative amount.
  - Action: Attempt to log an expense with the amount left blank, then with 0, then with -10 (other fields valid).
  - Expected: Each attempt is rejected with a validation message and no expense is added to the expense list.

- [ ] CS-02: An expense cannot be saved without a category.
  - Action: Fill in an expense (amount 25, currency, date) but leave the category unselected, then submit.
  - Expected: Submission is rejected with a validation message and no expense is added to the expense list.

- [ ] CS-03: Goals and budgets cannot be saved without a name or with a non-positive amount.
  - Action: Try to save a goal with an empty name; try to save a budget with amount 0; try to save a budget with amount -100.
  - Expected: Each attempt is rejected with a validation message and no goal or budget is added.

- [ ] CS-04: An invalid date range cannot be applied to the expense filter.
  - Action: In the date range filter, set the end date earlier than the start date.
  - Expected: A validation error is shown and the invalid range is not applied (the expense list is unchanged).

## Interaction
- [ ] IX-01: Saving an entry gives success feedback and the new entry appears immediately.
  - Action: Save a new goal, then a new budget, then a new expense, observing the UI after each save.
  - Expected: Each save displays a success confirmation and the new entry is immediately visible in its list without a page reload.

- [ ] IX-02: Summaries and charts refresh when spending data changes.
  - Action: Log one more expense, then view the summary figures and both charts without reloading the page.
  - Expected: The summary totals and both charts immediately include the newly logged expense.

## Content
- [ ] CT-01: Chart labels match the underlying data.
  - Action: With existing expenses in at least two categories and two different months, view both charts.
  - Expected: The by-category chart is labeled with exactly the category names used in the expense list, and the over-time chart is labeled with the months that contain expenses (no missing or placeholder labels).

- [ ] CT-02: Each expense row shows its original amount, currency, and exact category/goal labels.
  - Action: Inspect in the expense list the row of an expense logged as 45 EUR in category "Groceries" for goal "Vacation".
  - Expected: The row shows the amount 45.00 with EUR (the currency it was logged in) and the labels "Groceries" and "Vacation" exactly as assigned.