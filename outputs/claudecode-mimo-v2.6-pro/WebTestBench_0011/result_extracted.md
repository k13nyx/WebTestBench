# Test Result

## Functionality
- [X] FT-01: Record a one-off income transaction.
  - Action: Open the "Add Transaction" form, set Type = "Income", Recurrence = "One-off", enter an amount (e.g., 1500), a date, pick an existing Category, Project, and Payment Method, set Status = "Paid", click "Save".
  - Expected: The new income transaction appears in the transaction list with all entered values and is counted in total income.

- [ ] FT-02: Record a one-off expense transaction.
  - Action: Open the "Add Transaction" form, set Type = "Expense", Recurrence = "One-off", enter an amount (e.g., 400), a date, pick an existing Category, Project, and Payment Method, set Status = "Pending", click "Save".
  - Expected: The new expense transaction appears in the transaction list with all entered values and is counted in total expenses.
  - Bug Report:
    - Issue: Pending Expense Not Counted in Total Expenses
    - Actual: The transaction appears in the list with all entered values ("Office Supplies QA | Nov 8, 2026 | • | Operations | Office & Utilities | Pending | -$400"), but it is not counted in Total Expenses — the dashboard Total Expenses metric stays at $73,800 (labeled "Paid transactions") and never includes the $400; the amount is only reflected in the Pending card's "$33,598 out" figure.

- [ ] FT-03: Record a recurring transaction.
  - Action: Open the "Add Transaction" form, set Recurrence = "Monthly", fill in type, amount, date, category, project, payment method, and status, then click "Save".
  - Expected: The transaction is saved and labeled as recurring with its frequency shown, and it appears in the transaction list.
  - Bug Report:
    - Issue: Missing Recurrence Frequency Label on Transaction Row
    - Actual: The transaction is saved and appears in the list ("Software Subscription QA | Nov 8, 2026 | • | Product Development | Software & Tools | Expected | -$99") and is marked recurring only by an unlabeled repeat icon (lucide-repeat) next to its name; the frequency ("Monthly") is never shown on the row — it is only visible after opening the row's Edit dialog.

- [X] FT-04: Assign category, project, and payment method to a transaction.
  - Action: When recording a transaction, select one existing Category, one existing Project, and one existing Payment Method from their dropdowns, then save.
  - Expected: All three assignments are saved and shown on the transaction's row in the list.

- [X] FT-05: Mark a transaction's payment status.
  - Action: Set the Status field of a transaction to "Paid", then create another with "Pending" and another with "Expected".
  - Expected: Each transaction displays exactly the status that was set (paid / pending / expected), one status per transaction.

- [ ] FT-06: Filter transactions.
  - Action: Apply filters using values from the default data: Type, Category, Project, Payment Method, Status, and a date range; then clear all filters.
  - Expected: The transaction list shows only transactions matching the applied filters, and clearing filters restores the full default list.
  - Bug Report:
    - Issue: Missing Filter Controls (Payment Method, Date Range)
    - Actual: The filter bar provides only Search, Type, Status, Category, Project (plus Date/Amount/Name sorting) — there is no Payment Method filter and no date-range filter, so the specified filtering cannot be performed. The available filters do work correctly (Status=Expected → "4 of 26 transactions", Type=Income → "12 of 26", Project=Operations → "5 of 26", combined filters apply AND logic) and the "Clear" button restores the full list ("26 of 26 transactions").

- [X] FT-07: Sort transactions.
  - Action: Sort the transaction list by Date and by Amount, toggling ascending and descending order for each.
  - Expected: The list reorders according to the selected field and direction, with no transactions added or removed.

- [ ] FT-08: View historical cash flow chart.
  - Action: Open the dashboard's historical cash flow chart section.
  - Expected: A chart displays past income, expenses, and net cash flow over time, derived from the default transactions.
  - Bug Report:
    - Issue: Chart Data Not Derived from Transactions; Net Cash Flow Series Missing
    - Actual: The "Cash Flow Overview" chart plots only Income and Expenses areas (legend: Income / Expenses / Forecast) — net cash flow over time is not displayed as a series or in the tooltip ("Aug | Income: $52,000 | Expenses: $38,000"). Its values are not derived from the transactions: e.g., the Aug tooltip shows Income $52,000 / Expenses $38,000 while the transaction list's only August item is "Annual Subscription | Aug 10, 2026 | +$9,600" (actual Aug expenses $0); Sep shows $61,000/$42,000 vs actual $34,000/$3,600.

- [X] FT-09: View future cash balance forecast.
  - Action: Open the forecast section of the dashboard.
  - Expected: A projected future cash balance is shown that incorporates upcoming expected/pending payments and recurring transactions.

- [X] FT-10: Create a custom view for a business area.
  - Action: Create a new custom view (e.g., name "Marketing") with filters targeting one default category or project, and save it.
  - Expected: The new view is listed in the custom view switcher and can be selected.

- [X] FT-11: Switch between custom views.
  - Action: Switch from the default view to a saved custom view, then to another saved custom view (e.g., "Operations").
  - Expected: Each switch loads that view's filtered transactions and tailored dashboard summary automatically, without manually re-applying filters.

## Constraint
- [ ] CS-01: Transaction cannot be saved with missing required fields.
  - Action: Open the "Add Transaction" form and click "Save" while leaving name/description, amount, and date empty.
  - Expected: The transaction is not saved; inline validation errors mark the empty required fields.
  - Bug Report:
    - Issue: Missing Inline Validation Errors on Required Fields
    - Actual: The save is correctly blocked (dialog stays open, list count unchanged "24 of 24 transactions"), but no inline validation errors are rendered: no error messages appear and the empty required fields are not marked (no aria-invalid attributes, no error styling/text) — the fields only enter the native HTML5 :invalid state via the browser's transient constraint-validation popup.

- [X] CS-02: Amount must be a valid positive number.
  - Action: In the "Add Transaction" form, enter "abc" in Amount and save; then enter "-50" and save.
  - Expected: Both saves are rejected with a validation error on the Amount field; no invalid transaction is created.

- [ ] CS-03: Recurring transaction requires a recurrence frequency.
  - Action: Set Recurrence = "Recurring" (or similar) without selecting a frequency (e.g., monthly/weekly), fill all other fields, and save.
  - Expected: Saving is blocked with a validation error requesting a recurrence frequency.
  - Bug Report:
    - Issue: Missing Recurrence Frequency Validation on Save
    - Actual: With Recurrence toggled on and no frequency explicitly selected (the frequency selector silently pre-defaults to "Monthly"), clicking Save succeeds without any validation error — the dialog closes and the transaction is created ("Validation Test QA ... -$99", list count becomes "25 of 25 transactions") instead of being blocked with a request for a recurrence frequency.

## Interaction
- [ ] IX-01: Success confirmation after saving a transaction.
  - Action: Save a valid new transaction from the "Add Transaction" form.
  - Expected: A success toast (e.g., "Transaction saved successfully") is displayed and then dismisses automatically.
  - Bug Report:
    - Issue: Missing Success Toast Confirmation
    - Actual: After saving a valid transaction the dialog simply closes with no feedback — no success toast/notification is displayed at any point: the notifications region ("Notifications (F8)") is empty at ~400ms after saving and remains empty at ~5s (observed on three separate saves).

- [X] IX-02: Filters and sorting apply immediately.
  - Action: Change a filter selection or click a sort control on the transactions view.
  - Expected: The transaction list updates in place immediately, without a full page reload or requiring an extra "Apply" page load.

- [X] IX-03: View switching updates the dashboard in place.
  - Action: Select a different custom view from the view switcher.
  - Expected: The dashboard summary and transaction list refresh immediately to reflect the newly selected view.

## Content
- [X] CT-01: Dashboard shows cash flow-relevant summary metrics.
  - Action: Inspect the dashboard summary area using the default data.
  - Expected: Total Income, Total Expenses, and Net Cash Flow are displayed, and their values are consistent with the default transactions shown in the list.

- [ ] CT-02: Transaction rows show full recorded details.
  - Action: Inspect any transaction row in the list.
  - Expected: Each row displays amount, date, type (income/expense), category, project, payment method, status, and recurrence (one-off/recurring with frequency).
  - Bug Report:
    - Issue: Incomplete Row Details (Recurrence Frequency Not Displayed)
    - Actual: Rows display amount, date, type (sign + trending icon), category chip, project and status chip, but recurrence is conveyed only by an unlabeled repeat icon — the frequency (e.g., "Monthly") is never shown on the row and one-off rows carry no recurrence label; the payment method is likewise shown only as an unlabeled icon (building/credit-card/wallet/zap/arrow-right-left) without its name or accessible label.

- [X] CT-03: Custom view summary is scoped to its business area.
  - Action: Open a saved custom view filtered to one business area (e.g., "Marketing") and compare its summary totals to the full dashboard.
  - Expected: The view's summary counts only transactions matching its filters (e.g., marketing totals exclude operations/other-area transactions).
