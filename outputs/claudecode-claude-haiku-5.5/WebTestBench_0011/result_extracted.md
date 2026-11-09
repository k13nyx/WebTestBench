# Test Result

## Functionality
- [ ] FT-01: One-off transaction can be recorded with all attributes.
  - Action: Click "Add Transaction", select Type "Expense", enter Amount 250.00, Date today, Description "Test ad spend", Category "Marketing", Project "Spring Campaign", Payment Method "Credit Card", Status "Paid", then click "Save".
  - Expected: The transaction appears in the transaction list with all entered values shown in their columns.
  - Bug Report:
    - Issue: Missing Element / Incorrect Form Options
    - Actual: The Project dropdown has no "Spring Campaign" (options: Marketing Campaigns, Operations, Client: TechCorp, Client: RetailMax, Product Development, General). The Payment Method dropdown has no "Credit Card" (options: Business Checking, Business Credit Card, PayPal, Stripe, Wire Transfer). The submit button is labeled "Add Transaction", not "Save". The transaction did save (Expense, Marketing, Paid, -$250, Nov 9, 2026, project Marketing Campaigns), but the list row shows no Payment Method column.

- [ ] FT-02: Recurring transaction can be created.
  - Action: Click "Add Transaction", select Type "Income", enter Amount 1000.00, check "Recurring", set Frequency "Monthly", Start Date 2026-12-01, leave End Date empty, then click "Save".
  - Expected: The transaction appears in the list with a "Recurring" indicator and "Monthly" shown as its frequency.
  - Bug Report:
    - Issue: Missing Element / Recurring Not Persisted
    - Actual: After checking "Recurring", only a Frequency combobox (defaulting to "Monthly") appeared. No Start Date or End Date fields exist. The saved row is a single pending income of $1,000 dated Nov 9, 2026, category "Unknown", with no "Recurring" indicator and no "Monthly" label. The transaction was also gone after a page reload.

- [ ] FT-03: Transaction status can be changed among Paid, Pending, and Expected.
  - Action: On a Pending transaction in the list, change its Status to "Paid", reload the page, then change it to "Expected".
  - Expected: Status updates immediately after each change and persists after reload (shows "Paid", then "Expected").
  - Bug Report:
    - Issue: Status Not Persisted
    - Actual: On "Conference Sponsorship" (pending), the row menu "Mark as Paid" updated the badge to "paid" immediately. After reload it showed "pending" again. The row menu has no "Expected" option, so I used Edit → Status "Expected" → "Update Transaction", which updated the badge to "expected" immediately. The reload-persistence requirement failed.

- [X] FT-04: Transactions can be filtered by status.
  - Action: Open the "Status" filter, select only "Pending", then clear the filter.
  - Expected: Only Pending transactions are listed while the filter is applied; clearing the filter restores all transactions.

- [ ] FT-05: Transactions can be sorted by a column.
  - Action: Click the "Date" column header once, then click it again.
  - Expected: First click sorts newest to oldest; second click sorts oldest to newest; order is correct for every row.
  - Bug Report:
    - Issue: Incorrect Sort Direction / Missing Column Header
    - Actual: There are no column headers. Sorting is a "Date" combobox plus a direction button. The default order was already newest-first. The first click produced oldest-first (Aug 11 → Dec 8). The second click produced newest-first. Order is correct within each direction, but the first click does not sort newest to oldest as specified.

- [ ] FT-06: Historical cash flow chart updates for a selected date range.
  - Action: Open the "Cash Flow" chart, select date range "Last 6 Months".
  - Expected: Chart displays six monthly periods, each showing income and expense bars that match the default data for that month.
  - Bug Report:
    - Issue: Missing Element
    - Actual: No "Cash Flow" chart exists on Analytics (it shows Expenses by Category, Income by Source, and Project Performance). The Dashboard "Cash Flow Overview" chart shows nine months (Jul–Mar), with no date-range selector and no "Last 6 Months" option.

- [ ] FT-07: Forecast shows projected cash balances including expected and recurring items.
  - Action: Open the "Forecast" view and select "Next 90 Days".
  - Expected: A projected balance is shown for each period, and upcoming Expected transactions and recurring items within the period are included in the projection.
  - Bug Report:
    - Issue: Missing Element / Recurring Items Absent
    - Actual: The Forecast page has no "Next 90 Days" selector. It shows a fixed "3-Month Forecast" chart with Jan, Feb, and Mar labels and no per-period balance text. "Projected (3 months)" shows $56,300, which equals $14,300 + $42,000. The Upcoming list includes expected and pending items (5 items). The recurring income from FT-02 is absent.

- [X] FT-08: Custom view can be created for a business area.
  - Action: Click "New View", enter Name "Marketing", set Category filter "Marketing", then click "Save View".
  - Expected: The view "Marketing" appears in the view switcher and can be selected.

- [ ] FT-09: Switching to a custom view shows a tailored summary.
  - Action: Select the "Marketing" view from the view switcher, then select "All Transactions".
  - Expected: In "Marketing", the summary cards (Total Income, Total Expenses, Net) and transaction list include only Marketing-category items; switching back shows full totals again.
  - Bug Report:
    - Issue: Missing Element
    - Actual: The Marketing view was correct: Total Income $0, Total Expenses $3,500, Net −$3,500, and Recent Transactions listed only Marketing items (Google Ads Campaign, Conference Sponsorship). Returning via the Dashboard restored $86,600 / $72,300 / +$14,300. However, no "All Transactions" option exists in the view switcher.

## Constraint
- [ ] CS-01: Transaction cannot be saved with a required field empty.
  - Action: Click "Add Transaction", leave Amount empty, fill other fields, then click "Save".
  - Expected: Save is blocked, Amount field shows "Amount is required", and no transaction is added to the list.
  - Bug Report:
    - Issue: Incorrect Validation Message
    - Actual: Save was blocked and no transaction was added (count stayed at 20). The dialog stayed open, but the message is the browser's native "Please fill out this field.", not "Amount is required".

- [ ] CS-02: Amount must be a positive number.
  - Action: Enter Amount 0 and save; then enter Amount -50 and save.
  - Expected: Both attempts are rejected with "Amount must be greater than 0" and no transaction is created.
  - Bug Report:
    - Issue: Validation Bypass / Incorrect Validation Message
    - Actual: Amount 0 was accepted: "Zero amount test" was saved as a pending "-$0" transaction (count went 20 → 21). Amount -50 was blocked only by the native message "Value must be greater than or equal to 0." The required text "Amount must be greater than 0" never appeared.

- [ ] CS-03: Recurring transaction cannot have an end date before its start date.
  - Action: Check "Recurring", set Start Date 2026-12-01 and End Date 2026-11-01, then click "Save".
  - Expected: Save is blocked with "End Date must be after Start Date"; no transaction is created.
  - Bug Report:
    - Issue: Missing Element
    - Actual: Checking "Recurring" showed no Start Date or End Date inputs, so the dates could not be entered. The validation message could not be triggered.

- [ ] CS-04: Custom view names must be unique.
  - Action: With a "Marketing" view already existing, click "New View", enter Name "Marketing", then click "Save View".
  - Expected: Save is blocked with "A view with this name already exists"; no duplicate view is created.
  - Bug Report:
    - Issue: Duplicate View Name Allowed
    - Actual: With a "Marketing" view present in the sidebar, submitting the form with the same name redirected to the dashboard. The sidebar then showed two "Marketing" entries. No "A view with this name already exists" message appeared.

- [X] CS-05: Deleting a custom view does not delete its transactions.
  - Action: Note the count of transactions in the "Marketing" view, delete the "Marketing" view, then open "All Transactions" and check the Marketing-category transactions.
  - Expected: The view is removed from the switcher, and all Marketing-category transactions still exist in "All Transactions".

## Interaction
- [ ] IX-01: Successful save shows a confirmation and closes the form.
  - Action: Complete a valid transaction (per FT-01) and click "Save".
  - Expected: A toast "Transaction saved" appears, the form closes, and the new row is highlighted in the list.
  - Bug Report:
    - Issue: Missing Feedback Toast
    - Actual: The form closed and the new row "Test ad spend" appeared in the list. The notification region was empty immediately after save, so no "Transaction saved" toast was present. No row highlight was observed.

- [X] IX-02: Hovering a chart bar shows its values.
  - Action: Hover the mouse over the income bar and the expense bar for any month in the "Cash Flow" chart.
  - Expected: A tooltip shows the month name, the exact Income value, and the exact Expense value for that bar.

- [ ] IX-03: Deleting a custom view requires confirmation.
  - Action: Click "Delete View" for "Marketing", then click "Cancel" in the confirmation dialog; repeat and click "Confirm".
  - Expected: After "Cancel", the view remains unchanged; after "Confirm", the view is removed and the view switcher shows "All Transactions" as active.
  - Bug Report:
    - Issue: Missing Confirmation Dialog / Missing Element
    - Actual: No "Delete View" control was found on the view page. The action button on the "Marketing" sidebar item removed the view immediately, with no confirmation dialog and no Cancel option. No "All Transactions" entry is shown as active.

## Content
- [X] CT-01: Default data labels are relevant to a small business.
  - Action: Review the category, project, and payment method dropdowns and the transaction list descriptions.
  - Expected: All names are business-related (e.g., expense and income categories, project names, payment methods) with no placeholder text such as "Lorem", "Test", or "Untitled".

- [ ] CT-02: Chart totals match the transaction list.
  - Action: Select date range "Last 6 Months" in the "Cash Flow" chart, then sum the Income and Expense amounts from the transaction list for the same period.
  - Expected: The chart's total income and total expenses equal the list sums exactly.
  - Bug Report:
    - Issue: Missing Element / Not Testable
    - Actual: No "Last 6 Months" range control exists, and the Cash Flow Overview chart exposes no total income or total expense values. The comparison could not be performed.

- [ ] CT-03: Forecast ending balance is arithmetically correct.
  - Action: Note the Opening Balance, total expected income, and total expected expenses shown for "Next 90 Days", then compute Opening Balance + Income − Expenses.
  - Expected: The forecast's projected ending balance equals the computed value to the cent.
  - Bug Report:
    - Issue: Missing Element / Not Testable
    - Actual: There is no "Next 90 Days" view, and the Forecast page shows no labeled Opening Balance, expected income, or expected expense totals. The only projected figure is "Projected (3 months)" $56,300. It equals $14,300 + $75,000 in − $33,000 out, derived from Dashboard figures, but the required 90-day breakdown is not shown.
