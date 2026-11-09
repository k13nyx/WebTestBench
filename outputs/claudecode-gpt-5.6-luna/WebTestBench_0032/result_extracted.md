# Test Result

## Functionality

- [ ] FT-01: User can define multiple financial goals.
  - Action: Open **Goals**, enter a goal name, target amount, and target date, then save at least two distinct goals.
  - Expected: Each saved goal appears in the goals list with its correct name, target amount, and target date.
  - Bug Report:
    - Issue: Goals management unavailable
    - Actual: No **Goals** control is present in the application. Navigating to `/goals` displays a 404 “Page not found” screen.

- [ ] FT-02: User can define monthly budgets for spending categories.
  - Action: Open **Budgets**, select a category and month, enter a budget amount, and save budgets for at least two categories.
  - Expected: Each budget appears with the correct category, month, and amount.
  - Bug Report:
    - Issue: Budgets management unavailable
    - Actual: No **Budgets** control is present in the application. Navigating to `/budgets` displays a 404 “Page not found” screen.

- [X] FT-03: User can log expenses in different currencies and assign categories.
  - Action: Open **Expenses**, enter valid expense details using two supported currencies, select a category for each expense, and save them.
  - Expected: Each expense appears with its amount, currency, date, and assigned category.

- [X] FT-04: User can select a primary currency.
  - Action: Open the currency setting, select a supported currency, and save the preference.
  - Expected: The selected currency is displayed as the primary currency.

- [ ] FT-05: Expense and budget summaries are converted and displayed in the primary currency.
  - Action: Select a primary currency different from at least one currency used by the available expense data.
  - Expected: All summary totals, budget totals, and spending comparisons are shown in the selected primary currency.
  - Bug Report:
    - Issue: Budget totals are relabeled but not converted
    - Actual: After changing the primary currency from USD to EUR, the monthly budget remained `€2600.00`, matching the original USD amount instead of being converted. Budget category values also remained unchanged, such as `€600.00` for Food & Dining.

- [ ] FT-06: User can view spending compared with budget by category.
  - Action: Open the category spending chart using the available default expenses and budgets.
  - Expected: The chart shows spending and budget values for each displayed category in the primary currency.
  - Bug Report:
    - Issue: Category chart lacks spending/budget series identification
    - Actual: The chart exposes category emoji and numeric axes but does not provide a visible legend or DOM labels distinguishing spending values from budget values for each category.

- [ ] FT-07: User can view spending trends over time.
  - Action: Open the spending-over-time chart using the available default expense data.
  - Expected: The chart displays spending for distinct dates or time periods and uses the primary currency.
  - Bug Report:
    - Issue: Spending trend does not represent the available default expenses
    - Actual: The chart displays dates from the current 14-day period, while the available default expenses are dated in November–December 2024. No corresponding default-expense spending values are shown.

- [X] FT-08: User can filter expenses by date range.
  - Action: Set a start date and end date in the expense filters.
  - Expected: The expense list contains only records whose dates fall within the selected range.

- [X] FT-09: User can filter expenses by category and goal.
  - Action: Select an available category, then select an available goal in the expense filters.
  - Expected: The expense list contains only records matching the selected category and goal.

## Constraint

- [ ] CS-01: An expense cannot be saved without a category.
  - Action: Open the expense form, leave **Category** empty, complete the other required fields, and attempt to save.
  - Expected: The expense is not saved and the category field shows a required-field validation message.
  - Bug Report:
    - Issue: Missing inline category validation
    - Actual: The expense was not saved, but the category field did not show a required-field validation message. Only a generic `Missing fields` toast appeared.

- [ ] CS-02: Invalid or missing expense values are rejected.
  - Action: Attempt to save expenses with an empty amount, an invalid amount, or an unsupported currency.
  - Expected: The expense is not saved and the invalid field displays a clear validation message.
  - Bug Report:
    - Issue: Validation is generic rather than field-specific
    - Actual: Submitting the form with missing required values produced only the generic `Please fill in all required fields.` toast. No invalid field displayed a clear validation message, and invalid amount or unsupported-currency validation could not be verified through the available controls.

- [ ] CS-03: Budget comparisons use one consistent primary currency.
  - Action: Change the primary currency and inspect summary totals and both spending charts.
  - Expected: Every monetary value in summaries and charts uses the newly selected currency; no mixed-currency total is displayed.
  - Bug Report:
    - Issue: Budget comparison values are not converted consistently
    - Actual: Changing the primary currency to EUR changed displayed currency symbols, but budget amounts remained numerically identical to their USD values. The category chart also lacked a clear spending-versus-budget legend.

- [X] CS-04: Applying filters cannot display records outside the selected criteria.
  - Action: Apply a date range, category, and goal filter together.
  - Expected: Every displayed expense satisfies all three active filter criteria.

## Interaction

- [X] IX-01: Successful saves provide visible confirmation and update the relevant list.
  - Action: Save a goal, budget, or expense with valid information.
  - Expected: A success confirmation appears and the new record is visible in the corresponding list without requiring a page refresh.

- [X] IX-02: Filter controls update the expense list and can be cleared.
  - Action: Apply any expense filter, then use **Clear Filters** or reset each filter.
  - Expected: The list updates when the filter is applied and returns to the unfiltered default data when filters are cleared.

## Content

- [ ] CT-01: Financial records display complete and relevant details.
  - Action: Review the goals, budgets, and expense lists.
  - Expected: Each record displays the relevant name or description, amount, currency, date or month, category, and goal information where applicable.
  - Bug Report:
    - Issue: Goals and budgets do not provide complete record details
    - Actual: The dashboard displays goal names and progress, but not target amounts or target dates. Budget categories display amounts but no saved budget month or editable budget records. Expense goal information is concatenated with the category, such as `TravelSummer Vacation`, without a separate goal field.

- [ ] CT-02: Charts contain understandable labels and legends.
  - Action: Review the category and time-based spending charts.
  - Expected: Each chart identifies its categories or time periods, distinguishes spending from budget where applicable, and labels monetary values in the primary currency.
  - Bug Report:
    - Issue: Charts lack understandable legends and series labels
    - Actual: Charts expose currency axes and category emoji/date labels, but no visible legend distinguishes spending from budget. Category names are not shown as readable text in the chart, and the time chart does not show the default expense spending periods.
