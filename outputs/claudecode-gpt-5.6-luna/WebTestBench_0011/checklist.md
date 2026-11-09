# Test Checklist

## Functionality
- [ ] FT-01: Record a one-off income transaction.
  - Action: Select **Add Transaction**, choose **Income** and **One-off**, enter valid date and amount values, and select **Save**.
  - Expected: The transaction appears in the transaction list as a one-off income record.

- [ ] FT-02: Record a one-off expense transaction.
  - Action: Select **Add Transaction**, choose **Expense** and **One-off**, enter valid date and amount values, and select **Save**.
  - Expected: The transaction appears in the transaction list as a one-off expense record.

- [ ] FT-03: Record recurring income and expense transactions.
  - Action: Add valid recurring **Income** and **Expense** transactions, selecting a recurrence frequency and start date for each.
  - Expected: Each transaction is saved with its recurrence details and appears in the recurring transaction list.

- [ ] FT-04: Assign transaction classification details.
  - Action: For a transaction, select a **Category**, **Project**, and **Payment Method**, then save it.
  - Expected: The saved transaction displays all three selected classification values.

- [ ] FT-05: Assign and display transaction payment status.
  - Action: Save transactions with each available status: **Paid**, **Pending**, and **Expected**.
  - Expected: Each transaction displays the selected status and remains associated with the correct amount and type.

- [ ] FT-06: Filter transactions using dashboard filters.
  - Action: Apply filters for category, project, payment method, status, and date range using the available filter controls.
  - Expected: The list contains only transactions matching every active filter.

- [ ] FT-07: Sort transactions by supported fields.
  - Action: Sort the transaction list by date and amount in both ascending and descending order.
  - Expected: The transaction list follows the selected field and direction each time.

- [ ] FT-08: View historical cash flow charts.
  - Action: Select a historical time range from the cash flow chart controls.
  - Expected: The chart displays historical income, expenses, and net cash flow for the selected period.

- [ ] FT-09: View a future cash balance forecast.
  - Action: Open the forecast section and select a future period that contains upcoming expected or recurring transactions.
  - Expected: The forecast displays projected cash balances that account for the included upcoming income and expenses.

- [ ] FT-10: Create and switch between custom business views.
  - Action: Create a custom view for a business area such as **Marketing**, save it, then create or select another view such as **Operations** or a specific client.
  - Expected: Each saved view is available for selection and switching views updates the displayed transactions and summaries to that view’s criteria.

## Constraint
- [ ] CS-01: Prevent saving transactions with missing required fields.
  - Action: Open **Add Transaction**, leave a required field such as amount, date, type, or status empty, and select **Save**.
  - Expected: The transaction is not saved and the missing field is identified with a validation message.

- [ ] CS-02: Restrict transaction status to valid values.
  - Action: Open the transaction status control and inspect the available options.
  - Expected: The control permits only **Paid**, **Pending**, or **Expected** statuses.

- [ ] CS-03: Require recurrence details for recurring transactions.
  - Action: Select **Recurring** without choosing a recurrence frequency or start date, then attempt to save.
  - Expected: The transaction is not saved and the missing recurrence details are identified.

- [ ] CS-04: Keep one-off transactions from generating repeated entries.
  - Action: Review a saved one-off transaction across later dates or in the forecast.
  - Expected: The one-off transaction appears only on its original date and does not create future occurrences.

- [ ] CS-05: Use only eligible transactions in forecasts.
  - Action: Compare the forecast inputs with transactions marked **Paid**, **Pending**, **Expected**, and recurring future items.
  - Expected: The forecast includes upcoming expected and recurring items according to their dates and excludes transactions that are outside the selected forecast period.

## Interaction
- [ ] IX-01: Confirm successful transaction saves.
  - Action: Save a valid transaction.
  - Expected: A visible success confirmation appears, and the transaction list and relevant summary values refresh to include the saved record.

- [ ] IX-02: Update results when filters or sorting change.
  - Action: Apply a filter, change the sort order, and then clear the filter.
  - Expected: Results update after each action, and clearing the filter restores the unfiltered transaction list.

- [ ] IX-03: Reveal chart details on interaction.
  - Action: Hover over historical chart points or bars.
  - Expected: A tooltip identifies the date or period and the corresponding income, expense, and net cash flow values.

- [ ] IX-04: Indicate the active custom view.
  - Action: Switch between two saved custom views.
  - Expected: The selected view is visibly marked as active, and its tailored transactions and summary values replace the previous view’s content.

## Content
- [ ] CT-01: Display complete transaction information.
  - Action: Inspect transaction rows and their details.
  - Expected: Each transaction clearly shows amount, income or expense type, date, category, project, payment method, recurrence state, and payment status where applicable.

- [ ] CT-02: Keep financial values semantically clear.
  - Action: Review transaction lists, summaries, charts, and forecasts containing both income and expenses.
  - Expected: Currency formatting is consistent, income and expenses are distinguishable, and net cash flow values use the correct signs and labels.

- [ ] CT-03: Label historical and forecast data distinctly.
  - Action: Inspect the cash flow chart and forecast section.
  - Expected: Historical actuals and future projections are clearly labeled, with readable time periods, legends, and forecast terminology.