# Test Checklist

## Functionality
- [ ] FT-01: User can create a new financial goal with a name and target amount.
  - Action: Click "Add Goal" (or equivalent), enter a goal name (e.g., "Vacation") and target amount, save.
  - Expected: The new goal appears in the goals list and is available for selection when assigning expenses.

- [ ] FT-02: User can create a new monthly budget by category for a specific month/year.
  - Action: Click "Add Budget" (or equivalent), select a category, enter an amount, choose month/year, save.
  - Expected: The new budget appears in the budgets list and is reflected in the category-vs-budget chart.

- [ ] FT-03: User can log a new expense specifying amount, currency, category, and date.
  - Action: Click "Add Expense", fill in amount, currency (e.g., USD, EUR, JPY), category, and date, save.
  - Expected: The expense appears in the expense list and contributes to the relevant summaries.

- [ ] FT-04: User can assign an existing expense to a financial goal.
  - Action: When logging or editing an expense, select a goal from the goals dropdown.
  - Expected: The expense is linked to the chosen goal and counts toward it.

- [ ] FT-05: User can select a primary currency for the application.
  - Action: Open settings/preferences and choose a primary currency (e.g., USD).
  - Expected: The selected currency is saved and used as the display currency throughout the app.

- [ ] FT-06: User can view a chart comparing spending vs. budget by category.
  - Action: Navigate to the category summary/chart view.
  - Expected: A chart is displayed showing actual spend vs. budgeted amount for each category in the primary currency.

- [ ] FT-07: User can view a chart showing spending over time.
  - Action: Navigate to the time/trend chart view.
  - Expected: A chart is displayed plotting expense totals across time (e.g., by day/week/month) in the primary currency.

- [ ] FT-08: User can filter the expense list by a date range.
  - Action: Set a start date and end date in the expense list filter controls, apply.
  - Expected: Only expenses with dates within the selected range are shown.

- [ ] FT-09: User can filter the expense list by category.
  - Action: Select one or more categories from the category filter, apply.
  - Expected: Only expenses belonging to the selected category(ies) are shown.

- [ ] FT-10: User can filter the expense list by financial goal.
  - Action: Select a goal from the goal filter, apply.
  - Expected: Only expenses assigned to the selected goal are shown.

## Constraint
- [ ] CS-01: Required fields cannot be empty when creating an expense, goal, or budget.
  - Action: Try to submit the expense/goal/budget form with one required field left blank.
  - Expected: Submission is blocked and a clear validation message identifies the missing field.

- [ ] CS-02: All monetary summaries and charts must display values in the chosen primary currency, regardless of the expense's original currency.
  - Action: Log expenses in mixed currencies (e.g., USD, EUR) while primary currency is USD; view summaries and charts.
  - Expected: Every displayed amount is converted to and shown in the primary currency; original currencies are not used in totals/charts.

- [ ] CS-03: Expenses logged in non-primary currencies must be accepted and converted, not rejected.
  - Action: Log an expense using a currency different from the primary currency.
  - Expected: The expense is saved successfully and its converted primary-currency value appears in summaries.

## Interaction
- [ ] IX-01: Adding a new expense immediately updates the category-vs-budget chart and time chart.
  - Action: Open the charts, then log a new expense.
  - Expected: Both charts reflect the new expense without requiring a manual page reload.

- [ ] IX-02: Changing filters on the expense list dynamically refreshes the displayed expenses.
  - Action: Apply or change a date/category/goal filter on the expense list.
  - Expected: The list updates immediately to show only matching expenses; no manual refresh required.

- [ ] IX-03: Changing the primary currency immediately updates all monetary summaries and charts.
  - Action: Switch the primary currency from, e.g., USD to EUR in settings.
  - Expected: All totals, charts, and budget comparisons re-render with values converted to the new primary currency.

## Content
- [ ] CT-01: Chart labels and category names in the category-vs-budget chart must match the categories defined in budgets/expenses.
  - Action: Create categories (e.g., "Food", "Transport") and view the category chart.
  - Expected: The chart uses the exact same category names as those configured by the user.

- [ ] CT-02: Pre-existing default data (sample goals, budgets, or expenses) must be relevant to a budgeting application.
  - Action: Load the application on first use and inspect any pre-populated goals/budgets/expenses.
  - Expected: Default items use realistic budgeting categories, currencies, and amounts that align with the app's purpose; no placeholder text like "Lorem ipsum" or unrelated content is shown.