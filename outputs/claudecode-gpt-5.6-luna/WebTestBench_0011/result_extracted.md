# Test Result

## Functionality

- [ ] FT-01: Record a one-off income transaction.
  - Action: Select **Add Transaction**, choose **Income** and **One-off**, enter valid date and amount values, and select **Save**.
  - Expected: The transaction appears in the transaction list as a one-off income record.
  - Bug Report:
    - Issue: Incorrect transaction type and missing one-off control
    - Actual: The form has no **One-off** option. After selecting the default **Income** type and saving `QA One-off Income` for `$1,234.56`, the list displayed it as `-$1,235`, an expense amount.

- [ ] FT-02: Record a one-off expense transaction.
  - Action: Select **Add Transaction**, choose **Expense** and **One-off**, enter valid date and amount values, and select **Save**.
  - Expected: The transaction appears in the transaction list as a one-off expense record.
  - Bug Report:
    - Issue: Missing one-off transaction option
    - Actual: The expense transaction was saved as `-$321`, but the form provides no **One-off** selection or visible one-off state. It appears only as a generic expense record.

- [ ] FT-03: Record recurring income and expense transactions.
  - Action: Add valid recurring **Income** and **Expense** transactions, selecting a recurrence frequency and start date for each.
  - Expected: Each transaction is saved with its recurrence details and appears in the recurring transaction list.
  - Bug Report:
    - Issue: Recurring transaction details are not displayed or validated
    - Actual: A recurring transaction was saved as `QA Recurring Income` with `-$500`, and no recurrence details or recurring transaction list were displayed. The form also allowed a recurring submission without explicitly selecting a start date or confirming recurrence details.

- [ ] FT-04: Assign transaction classification details.
  - Action: For a transaction, select a **Category**, **Project**, and **Payment Method**, then save it.
  - Expected: The saved transaction displays all three selected classification values.
  - Bug Report:
    - Issue: Classification details were not assigned
    - Actual: The saved QA transactions displayed `Unknown` for category/project, and no payment method was selected or displayed.

- [X] FT-05: Assign and display transaction payment status.
  - Action: Save transactions with each available status: **Paid**, **Pending**, and **Expected**.
  - Expected: Each transaction displays the selected status and remains associated with the correct amount and type.

- [ ] FT-06: Filter transactions using dashboard filters.
  - Action: Apply filters for category, project, payment method, status, and date range using the available filter controls.
  - Expected: The list contains only transactions matching every active filter.
  - Bug Report:
    - Issue: Payment method filter is unavailable
    - Actual: The transaction page exposed Type, Status, Category, Project, and Date controls, but no Payment Method filter. Only Type and Status filtering were exercised successfully.

- [ ] FT-07: Sort transactions by supported fields.
  - Action: Sort the transaction list by date and amount in both ascending and descending order.
  - Expected: The transaction list follows the selected field and direction each time.
  - Bug Report:
    - Issue: Required sorting behavior could not be performed
    - Actual: The visible controls exposed a Date control, but no Amount sort control or ascending/descending amount options were available during testing.

- [ ] FT-08: View historical cash flow charts.
  - Action: Select a historical time range from the cash flow chart controls.
  - Expected: The chart displays historical income, expenses, and net cash flow for the selected period.
  - Bug Report:
    - Issue: Historical range control is unavailable
    - Actual: The dashboard chart displayed month labels and Income, Expenses, and Forecast legends, but no historical time-range selector was available.

- [X] FT-09: View a future cash balance forecast.
  - Action: Open the forecast section and select a future period that contains upcoming expected or recurring transactions.
  - Expected: The forecast displays projected cash balances that account for the included upcoming income and expenses.

- [X] FT-10: Create and switch between custom business views.
  - Action: Create a custom view for a business area such as **Marketing**, save it, then create or select another view such as **Operations** or a specific client.
  - Expected: Each saved view is available for selection and switching views updates the displayed transactions and summaries to that view’s criteria.

## Constraint

- [ ] CS-01: Prevent saving transactions with missing required fields.
  - Action: Open **Add Transaction**, leave a required field such as amount, date, type, or status empty, and select **Save**.
  - Expected: The transaction is not saved and the missing field is identified with a validation message.
  - Bug Report:
    - Issue: Missing required-field validation message
    - Actual: Submitting the blank transaction form did not save a record, but it also did not identify any missing field or display a validation message.

- [X] CS-02: Restrict transaction status to valid values.
  - Action: Open the transaction status control and inspect the available options.
  - Expected: The control permits only **Paid**, **Pending**, or **Expected** statuses.

- [ ] CS-03: Require recurrence details for recurring transactions.
  - Action: Select **Recurring** without choosing a recurrence frequency or start date, then attempt to save.
  - Expected: The transaction is not saved and the missing recurrence details are identified.
  - Bug Report:
    - Issue: Missing recurrence-detail validation
    - Actual: Recurring mode supplied a default `Monthly` frequency and retained a default date, with no validation requiring the user to explicitly provide recurrence details or identifying missing fields.

- [ ] CS-04: Keep one-off transactions from generating repeated entries.
  - Action: Review a saved one-off transaction across later dates or in the forecast.
  - Expected: The one-off transaction appears only on its original date and does not create future occurrences.
  - Bug Report:
    - Issue: One-off state is not supported or identifiable
    - Actual: The transaction form provided no one-off mode or one-off indicator, so the saved records could not be verified as one-off transactions.

- [X] CS-05: Use only eligible transactions in forecasts.
  - Action: Compare the forecast inputs with transactions marked **Paid**, **Pending**, **Expected**, and recurring future items.
  - Expected: The forecast includes upcoming expected and recurring items according to their dates and excludes transactions that are outside the selected forecast period.

## Interaction

- [ ] IX-01: Confirm successful transaction saves.
  - Action: Save a valid transaction.
  - Expected: A visible success confirmation appears, and the transaction list and relevant summary values refresh to include the saved record.
  - Bug Report:
    - Issue: Missing success confirmation
    - Actual: The transaction list refreshed and showed the saved record, but no visible success toast or confirmation appeared in the Notifications region.

- [ ] IX-02: Update results when filters or sorting change.
  - Action: Apply a filter, change the sort order, and then clear the filter.
  - Expected: Results update after each action, and clearing the filter restores the unfiltered transaction list.
  - Bug Report:
    - Issue: Sorting portion of interaction could not be verified
    - Actual: Status and Type filters updated the result count, and clearing filters restored `23 of 23 transactions`, but no sort-by-date or sort-by-amount interaction was available to verify.

- [ ] IX-03: Reveal chart details on interaction.
  - Action: Hover over historical chart points or bars.
  - Expected: A tooltip identifies the date or period and the corresponding income, expense, and net cash flow values.
  - Bug Report:
    - Issue: Incomplete chart tooltip
    - Actual: Hovering displayed `Nov`, `income: $68,000`, and `expenses: $45,000`, but no net cash flow value was included.

- [X] IX-04: Indicate the active custom view.
  - Action: Switch between two saved custom views.
  - Expected: The selected view is visibly marked as active, and its tailored transactions and summary values replace the previous view’s content.

## Content

- [ ] CT-01: Display complete transaction information.
  - Action: Inspect transaction rows and their details.
  - Expected: Each transaction clearly shows amount, income or expense type, date, category, project, payment method, recurrence state, and payment status where applicable.
  - Bug Report:
    - Issue: Incomplete transaction row information
    - Actual: Rows showed amounts, dates, category/project-like labels, and payment statuses, but did not show payment method or recurrence state. The QA-created records also displayed `Unknown` classification values.

- [X] CT-02: Keep financial values semantically clear.
  - Action: Review transaction lists, summaries, charts, and forecasts containing both income and expenses.
  - Expected: Currency formatting is consistent, income and expenses are distinguishable, and net cash flow values use the correct signs and labels.

- [X] CT-03: Label historical and forecast data distinctly.
  - Action: Inspect the cash flow chart and forecast section.
  - Expected: Historical actuals and future projections are clearly labeled, with readable time periods, legends, and forecast terminology.
