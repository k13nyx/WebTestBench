# Test Checklist

## Functionality
- [ ] FT-01: One-off transaction can be recorded with all attributes.
  - Action: Click "Add Transaction", select Type "Expense", enter Amount 250.00, Date today, Description "Test ad spend", Category "Marketing", Project "Spring Campaign", Payment Method "Credit Card", Status "Paid", then click "Save".
  - Expected: The transaction appears in the transaction list with all entered values shown in their columns.
- [ ] FT-02: Recurring transaction can be created.
  - Action: Click "Add Transaction", select Type "Income", enter Amount 1000.00, check "Recurring", set Frequency "Monthly", Start Date 2026-12-01, leave End Date empty, then click "Save".
  - Expected: The transaction appears in the list with a "Recurring" indicator and "Monthly" shown as its frequency.
- [ ] FT-03: Transaction status can be changed among Paid, Pending, and Expected.
  - Action: On a Pending transaction in the list, change its Status to "Paid", reload the page, then change it to "Expected".
  - Expected: Status updates immediately after each change and persists after reload (shows "Paid", then "Expected").
- [ ] FT-04: Transactions can be filtered by status.
  - Action: Open the "Status" filter, select only "Pending", then clear the filter.
  - Expected: Only Pending transactions are listed while the filter is applied; clearing the filter restores all transactions.
- [ ] FT-05: Transactions can be sorted by a column.
  - Action: Click the "Date" column header once, then click it again.
  - Expected: First click sorts newest to oldest; second click sorts oldest to newest; order is correct for every row.
- [ ] FT-06: Historical cash flow chart updates for a selected date range.
  - Action: Open the "Cash Flow" chart, select date range "Last 6 Months".
  - Expected: Chart displays six monthly periods, each showing income and expense bars that match the default data for that month.
- [ ] FT-07: Forecast shows projected cash balances including expected and recurring items.
  - Action: Open the "Forecast" view and select "Next 90 Days".
  - Expected: A projected balance is shown for each period, and upcoming Expected transactions and recurring items within the period are included in the projection.
- [ ] FT-08: Custom view can be created for a business area.
  - Action: Click "New View", enter Name "Marketing", set Category filter "Marketing", then click "Save View".
  - Expected: The view "Marketing" appears in the view switcher and can be selected.
- [ ] FT-09: Switching to a custom view shows a tailored summary.
  - Action: Select the "Marketing" view from the view switcher, then select "All Transactions".
  - Expected: In "Marketing", the summary cards (Total Income, Total Expenses, Net) and transaction list include only Marketing-category items; switching back shows full totals again.

## Constraint
- [ ] CS-01: Transaction cannot be saved with a required field empty.
  - Action: Click "Add Transaction", leave Amount empty, fill other fields, then click "Save".
  - Expected: Save is blocked, Amount field shows "Amount is required", and no transaction is added to the list.
- [ ] CS-02: Amount must be a positive number.
  - Action: Enter Amount 0 and save; then enter Amount -50 and save.
  - Expected: Both attempts are rejected with "Amount must be greater than 0" and no transaction is created.
- [ ] CS-03: Recurring transaction cannot have an end date before its start date.
  - Action: Check "Recurring", set Start Date 2026-12-01 and End Date 2026-11-01, then click "Save".
  - Expected: Save is blocked with "End Date must be after Start Date"; no transaction is created.
- [ ] CS-04: Custom view names must be unique.
  - Action: With a "Marketing" view already existing, click "New View", enter Name "Marketing", then click "Save View".
  - Expected: Save is blocked with "A view with this name already exists"; no duplicate view is created.
- [ ] CS-05: Deleting a custom view does not delete its transactions.
  - Action: Note the count of transactions in the "Marketing" view, delete the "Marketing" view, then open "All Transactions" and check the Marketing-category transactions.
  - Expected: The view is removed from the switcher, and all Marketing-category transactions still exist in "All Transactions".

## Interaction
- [ ] IX-01: Successful save shows a confirmation and closes the form.
  - Action: Complete a valid transaction (per FT-01) and click "Save".
  - Expected: A toast "Transaction saved" appears, the form closes, and the new row is highlighted in the list.
- [ ] IX-02: Hovering a chart bar shows its values.
  - Action: Hover the mouse over the income bar and the expense bar for any month in the "Cash Flow" chart.
  - Expected: A tooltip shows the month name, the exact Income value, and the exact Expense value for that bar.
- [ ] IX-03: Deleting a custom view requires confirmation.
  - Action: Click "Delete View" for "Marketing", then click "Cancel" in the confirmation dialog; repeat and click "Confirm".
  - Expected: After "Cancel", the view remains unchanged; after "Confirm", the view is removed and the view switcher shows "All Transactions" as active.

## Content
- [ ] CT-01: Default data labels are relevant to a small business.
  - Action: Review the category, project, and payment method dropdowns and the transaction list descriptions.
  - Expected: All names are business-related (e.g., expense and income categories, project names, payment methods) with no placeholder text such as "Lorem", "Test", or "Untitled".
- [ ] CT-02: Chart totals match the transaction list.
  - Action: Select date range "Last 6 Months" in the "Cash Flow" chart, then sum the Income and Expense amounts from the transaction list for the same period.
  - Expected: The chart's total income and total expenses equal the list sums exactly.
- [ ] CT-03: Forecast ending balance is arithmetically correct.
  - Action: Note the Opening Balance, total expected income, and total expected expenses shown for "Next 90 Days", then compute Opening Balance + Income − Expenses.
  - Expected: The forecast's projected ending balance equals the computed value to the cent.