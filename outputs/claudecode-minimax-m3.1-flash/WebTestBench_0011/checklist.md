# Test Checklist

## Functionality
- [ ] FT-01: Add a one-off income transaction
  - Action: Click "Add Transaction", fill Date, Description ("Client invoice 1001"), Amount (2500), Type "Income", Category, Project, Payment Method, Status "Pending", and save.
  - Expected: The transaction is saved, appears in the transaction list with Amount 2,500.00 and Income type, and total income increases by 2,500.
- [ ] FT-02: Add a one-off expense transaction
  - Action: Click "Add Transaction", fill Date, Description ("Office supplies"), Amount (300), Type "Expense", Category, Project, Payment Method, Status "Paid", and save.
  - Expected: The transaction is saved, appears in the list with Amount 300.00 and Expense type, and total expenses/net cash flow reflect the -300.
- [ ] FT-03: Add a recurring transaction with a recurrence schedule
  - Action: Add a transaction with Type "Expense", enable recurring, set Description ("Monthly rent"), Amount (1200), and recurrence "Monthly" with a start date.
  - Expected: The recurring item is saved and appears as recurring; future occurrences are generated/indicated on the schedule (e.g. monthly projections), and it appears in the forecast.
- [ ] FT-04: Assign a transaction to a category, project, and payment method
  - Action: Open an existing transaction's edit form and set Category "Marketing", Project "Website Redesign", Payment Method "Bank Transfer"; save.
  - Expected: The saved transaction shows the selected category, project, and payment method in the list, and the values are used by the corresponding filters/summaries.
- [ ] FT-05: Set and change a transaction's payment status
  - Action: Set a new transaction's status to "Expected", then change it to "Paid" via the list or edit form.
  - Expected: The status label updates to the new value, is visible on the transaction, and the status filter/summary totals reflect the change immediately.
- [ ] FT-06: Filter transactions by type, status, category, project, and date range
  - Action: Using the filter controls, apply each filter (Type = Expense, Status = Pending, a Category, a Project, and a date range).
  - Expected: The transaction list shows only matching transactions, and the visible row count equals the number of matching default transactions; clearing filters restores the full list.
- [ ] FT-07: Sort transactions by date and by amount
  - Action: Click the Date column header, then the Amount column header.
  - Expected: Rows reorder to ascending (and descending on a second click for that column) date order, then ascending/descending amount order, with the sort direction indicated.
- [ ] FT-08: View the historical cash flow chart
  - Action: Open the dashboard's chart area and select a historical period (e.g. last 6 months / year).
  - Expected: A chart renders showing monthly income vs expense (and/or net) for the selected past periods, with values matching the transactions in that period.
- [ ] FT-09: View the forecast of future cash balances
  - Action: Open the forecast section for a future horizon (e.g. next 6 months).
  - Expected: A projection of future cash balance is shown based on expected payments and recurring items; the values change when an expected/recurring transaction is added, and reflect the current balance as the starting point.
- [ ] FT-10: Create a custom view for a business area
  - Action: Create a view named "Marketing" with filters (e.g. Category = Marketing and/or Project = Website Redesign) and any chosen summary/chart options; save it.
  - Expected: "Marketing" appears in the view list/switcher and its saved filters are retained (reopening it shows the same filters applied).
- [ ] FT-11: Switch between custom views and see tailored summaries
  - Action: Select the "Marketing" view, then switch to another view (or the default/All view).
  - Expected: The active view is highlighted, and the transaction list, summary totals, and charts update to show only that view's scoped transactions; switching back restores the previous scope.

## Constraint
- [ ] CS-01: Required transaction fields are enforced
  - Action: Submit the Add/Edit Transaction form with Amount empty, then with Date empty, then with Type unset; also try Amount = 0 and Amount = -50.
  - Expected: Submission is blocked each time with a visible field-level validation message (e.g. "Amount is required", "Date is required", "Type is required"), no transaction is created, and non-positive amounts are rejected as invalid.
- [ ] CS-02: A recurring transaction must define its recurrence
  - Action: Enable the recurring option and attempt to save without choosing a frequency/interval (and without a start date).
  - Expected: Saving is blocked with a validation message naming the missing recurrence field, and no recurring item is created.
- [ ] CS-03: Duplicate custom view names are rejected
  - Action: Create a new view using the name of an existing view (e.g. "Marketing").
  - Expected: Saving is refused with a message that the name is already in use, and only one view named "Marketing" exists afterwards.
- [ ] CS-04: A filter combination with no matching data shows an empty state
  - Action: Apply a filter combination that matches no default transactions (e.g. Status = Expected AND Type = Expense with no expected expenses).
  - Expected: The list shows an explicit "no results / no matching transactions" message with zero rows, summary totals show 0 / no data rather than stale values, and charts do not display leftover data.

## Interaction
- [ ] IX-01: The "Add Transaction" control opens the entry form
  - Action: Click the "Add Transaction" (or "+") button on the dashboard.
  - Expected: A transaction entry form/modal appears with fields for Date, Description, Amount, Type, Category, Project, Payment Method, Status, and a recurring option.
- [ ] IX-02: Saving shows a confirmation and updates the view
  - Action: Save a valid transaction and observe the notification area.
  - Expected: A success confirmation message (e.g. "Transaction added") is displayed, the form closes, and the new transaction is immediately visible in the transaction list.
- [ ] IX-03: Status is visually distinguishable per transaction
  - Action: View a list containing Paid, Pending, and Expected transactions.
  - Expected: Each transaction shows a readable status label (Paid / Pending / Expected) and the three statuses are visually distinguishable (different label, color, or icon) from each other.

## Content
- [ ] CT-01: Amounts are shown as formatted currency
  - Action: Inspect the amounts in the transaction list, summary tiles, charts, and forecast values.
  - Expected: All monetary values are displayed consistently as currency (e.g. "$2,500.00" / "1,200.00"), with two decimals and thousand separators, and no raw unformatted numbers appear.
- [ ] CT-02: The transaction table shows the required identifying fields
  - Action: Inspect the columns/rows of the transaction list for a transaction that has a category, project, and payment method assigned.
  - Expected: The row shows the date, description, type (income/expense), amount, category, project, payment method, and status — none of these assigned values is missing or blank.
- [ ] CT-03: Chart and forecast labels describe the plotted data correctly
  - Action: Inspect the historical cash flow chart and the future forecast chart including their titles, axis labels, and period labels.
  - Expected: Charts have a descriptive title naming the metric (e.g. "Cash Flow" / "Forecast Balance"), labeled axes (period and amount), historical periods are labelled with past dates and forecast periods are labelled with future dates so the two are clearly distinguishable, and no placeholder/lorem text is shown.