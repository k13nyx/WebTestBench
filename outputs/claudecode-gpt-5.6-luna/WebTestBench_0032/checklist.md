# Test Checklist

## Functionality
- [ ] FT-01: User can define multiple financial goals.
  - Action: Open **Goals**, enter a goal name, target amount, and target date, then save at least two distinct goals.
  - Expected: Each saved goal appears in the goals list with its correct name, target amount, and target date.

- [ ] FT-02: User can define monthly budgets for spending categories.
  - Action: Open **Budgets**, select a category and month, enter a budget amount, and save budgets for at least two categories.
  - Expected: Each budget appears with the correct category, month, and amount.

- [ ] FT-03: User can log expenses in different currencies and assign categories.
  - Action: Open **Expenses**, enter valid expense details using two supported currencies, select a category for each expense, and save them.
  - Expected: Each expense appears with its amount, currency, date, and assigned category.

- [ ] FT-04: User can select a primary currency.
  - Action: Open the currency setting, select a supported currency, and save the preference.
  - Expected: The selected currency is displayed as the primary currency.

- [ ] FT-05: Expense and budget summaries are converted and displayed in the primary currency.
  - Action: Select a primary currency different from at least one currency used by the available expense data.
  - Expected: All summary totals, budget totals, and spending comparisons are shown in the selected primary currency.

- [ ] FT-06: User can view spending compared with budget by category.
  - Action: Open the category spending chart using the available default expenses and budgets.
  - Expected: The chart shows spending and budget values for each displayed category in the primary currency.

- [ ] FT-07: User can view spending trends over time.
  - Action: Open the spending-over-time chart using the available default expense data.
  - Expected: The chart displays spending for distinct dates or time periods and uses the primary currency.

- [ ] FT-08: User can filter expenses by date range.
  - Action: Set a start date and end date in the expense filters.
  - Expected: The expense list contains only records whose dates fall within the selected range.

- [ ] FT-09: User can filter expenses by category and goal.
  - Action: Select an available category, then select an available goal in the expense filters.
  - Expected: The expense list contains only records matching the selected category and goal.

## Constraint
- [ ] CS-01: An expense cannot be saved without a category.
  - Action: Open the expense form, leave **Category** empty, complete the other required fields, and attempt to save.
  - Expected: The expense is not saved and the category field shows a required-field validation message.

- [ ] CS-02: Invalid or missing expense values are rejected.
  - Action: Attempt to save expenses with an empty amount, an invalid amount, or an unsupported currency.
  - Expected: The expense is not saved and the invalid field displays a clear validation message.

- [ ] CS-03: Budget comparisons use one consistent primary currency.
  - Action: Change the primary currency and inspect summary totals and both spending charts.
  - Expected: Every monetary value in summaries and charts uses the newly selected currency; no mixed-currency total is displayed.

- [ ] CS-04: Applying filters cannot display records outside the selected criteria.
  - Action: Apply a date range, category, and goal filter together.
  - Expected: Every displayed expense satisfies all three active filter criteria.

## Interaction
- [ ] IX-01: Successful saves provide visible confirmation and update the relevant list.
  - Action: Save a goal, budget, or expense with valid information.
  - Expected: A success confirmation appears and the new record is visible in the corresponding list without requiring a page refresh.

- [ ] IX-02: Filter controls update the expense list and can be cleared.
  - Action: Apply any expense filter, then use **Clear Filters** or reset each filter.
  - Expected: The list updates when the filter is applied and returns to the unfiltered default data when filters are cleared.

## Content
- [ ] CT-01: Financial records display complete and relevant details.
  - Action: Review the goals, budgets, and expense lists.
  - Expected: Each record displays the relevant name or description, amount, currency, date or month, category, and goal information where applicable.

- [ ] CT-02: Charts contain understandable labels and legends.
  - Action: Review the category and time-based spending charts.
  - Expected: Each chart identifies its categories or time periods, distinguishes spending from budget where applicable, and labels monetary values in the primary currency.