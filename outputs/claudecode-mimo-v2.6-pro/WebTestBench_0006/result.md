All test items have been executed. Here is the complete checklist with updated statuses:

# Test Result

## Functionality
- [X] FT-01: Record a new income transaction.
  - Action: Open the transaction entry form, select type "Income", fill in a description, amount, date, and category, then save.
  - Expected: The new income transaction appears in the transaction list with type "Income" and the entered amount.
- [X] FT-02: Record a new expense transaction.
  - Action: Open the transaction entry form, select type "Expense", fill in a description, amount, date, and category, then save.
  - Expected: The new expense transaction appears in the transaction list with type "Expense" and the entered amount.
- [ ] FT-03: Create financial records of each supported type (invoice, bill, payment).
  - Action: Create one invoice, one bill, and one payment record using default data.
  - Expected: All three records appear in the records list with the correct type label (Invoice / Bill / Payment) and amounts.
  - Bug Report:
    - Issue: Missing Feature — no financial records (invoice/bill/payment) functionality exists
    - Actual: The app has no records list and no record-type concept anywhere (scanned all pages: Dashboard, Transactions, Categories, Reports, Tax Summary — no "invoice", "bill", "payment", or "record" UI exists). The transaction entry form's Type dropdown offers only "Income" and "Expense", so no Invoice/Bill/Payment records can be created or displayed.
- [ ] FT-04: Assign a transaction to a category and an account.
  - Action: Edit an existing transaction and change its category to a different existing category and its account to a different existing account, then save.
  - Expected: The transaction list shows the transaction with the newly selected category and account.
  - Bug Report:
    - Issue: Missing Field — no account assignment on transactions
    - Actual: The category change works (edited a transaction from "Consulting" to "Sales Revenue" and the list reflects it), but the Add/Edit Transaction dialog contains no account field (fields are only Type, Date, Description, Amount, Category, Reference, Notes, Tax Related) and the transaction list has no account column. There is no account selector or account management anywhere in the app (only a static "Across all accounts" label on the dashboard), so a transaction cannot be assigned to an account.
- [X] FT-05: Create a custom category.
  - Action: Open category management, create a new category (e.g., "Travel"), and save.
  - Expected: The new category appears in the category list and is selectable in the transaction category dropdown.
- [X] FT-06: Edit and adjust an existing entry.
  - Action: Open an existing transaction, change its amount and description, and save the changes.
  - Expected: The updated amount and description are shown in the transaction list; the old values are gone.
- [X] FT-07: Delete an entry.
  - Action: Delete an existing transaction or record and confirm the deletion.
  - Expected: The item is removed from the transaction/records list and no longer appears anywhere in the app.
- [X] FT-08: Filter records by date range.
  - Action: Set the date filter to a range covering only some of the default records.
  - Expected: Only records with dates inside the selected range are displayed.
- [X] FT-09: Filter records by category.
  - Action: Select a category that some default records belong to in the category filter.
  - Expected: Only records assigned to the selected category are displayed.
- [ ] FT-10: View monthly profit and loss report.
  - Action: Open the reports section and select a month that contains default transactions.
  - Expected: A profit and loss report for that month is displayed, showing income, expenses, and profit/loss figures.
  - Bug Report:
    - Issue: Limited Date Range — report month selector cannot reach months containing the data
    - Actual: The Reports month dropdown offers only the last 12 months (November 2026 back to December 2025; verified by scrolling and keyboard navigation that no more options exist). All default transactions are dated Oct–Dec 2024, which are not selectable, so a P&L report for a month containing default transactions cannot be displayed. (The report itself renders correctly for a selectable month: November 2026 shows Income $555.55, Expenses $250.75, Net +$304.80.)
- [X] FT-11: Mark and unmark a record as tax-related.
  - Action: Toggle the tax-related control on an existing record, then toggle it off again.
  - Expected: The record is included in tax-related views when marked and excluded when unmarked.
- [X] FT-12: Generate a tax summary.
  - Action: Mark at least one record as tax-related, then open/generate the tax summary.
  - Expected: The tax summary displays only tax-marked records with their amounts and a tax-related total figure.
- [X] FT-13: Print the tax summary.
  - Action: With the tax summary open, click the "Print" button.
  - Expected: The browser print dialog (or a print-friendly view) opens showing the tax summary content.

## Constraint
- [X] CS-01: Cannot save a transaction with missing required fields.
  - Action: Submit the transaction form with the amount field empty (and again with the description empty).
  - Expected: The save is rejected and a validation error indicates the missing required field; no new record is created.
- [ ] CS-02: Cannot save a transaction with a zero or negative amount.
  - Action: Enter 0 and then a negative value (e.g., -50) in the amount field and submit.
  - Expected: The save is rejected with a validation error stating the amount must be greater than zero; no record is created.
  - Bug Report:
    - Issue: Invalid Input Accepted — zero amount saves without validation error
    - Actual: Entering amount 0 and submitting created a transaction successfully ("CS Test Zero" appeared in the list as "-$0.00") with no validation error; the amount input has `min="0"`, so zero passes validation. (The negative case was rejected by native validation with "Value must be greater than or equal to 0.", but the zero case is accepted and no "greater than zero" validation exists.)
- [ ] CS-03: Cannot delete a category that is assigned to existing records.
  - Action: Attempt to delete a category that is used by at least one default transaction.
  - Expected: The deletion is blocked with a message indicating the category is in use; the category and its transactions remain.
  - Bug Report:
    - Issue: Unprotected Deletion — in-use category can be deleted
    - Actual: Deleting the "Travel" category (used by 2 transactions, incl. default "Business Trip - Conference") was not blocked. The confirmation dialog only states "Transactions using this category will not be deleted" and, after confirming, the category was removed (Expense Categories count dropped from 9 to 8) with no "category in use" message; the affected transactions remained but lost their category (shown as blank/"Unknown" in lists and reports).

## Interaction
- [ ] IX-01: Success confirmation after saving a record.
  - Action: Save a new transaction or financial record.
  - Expected: A visible success confirmation (e.g., toast or inline message) appears immediately after saving.
  - Bug Report:
    - Issue: Missing Success Feedback — no confirmation after save
    - Actual: No toast, status, alert, or inline success message appears after saving. Verified with full body-text diffs captured at ~150 ms and ~1 s after saving a new transaction (twice), updating a transaction (twice), and creating a category — the only new content was the updated list row itself.
- [X] IX-02: Tax-related toggle gives immediate visual feedback on the record.
  - Action: Click the tax-related toggle on a record in the list or detail view.
  - Expected: The record's tax indicator changes state (e.g., checkbox checked/unchecked or badge shown/hidden) immediately without a manual refresh.

## Content
- [ ] CT-01: Dashboard totals match the underlying records.
  - Action: Compare the dashboard's total income, total expenses, and net balance against the amounts of the default transactions in the list.
  - Expected: Dashboard income equals the sum of all income transactions, expenses equal the sum of all expense transactions, and balance equals income minus expenses.
  - Bug Report:
    - Issue: Incorrect Dashboard Figures — totals missing and balance inconsistent with records
    - Actual: The dashboard shows "Total Balance $74,931 (Across all accounts)", which does not equal income minus expenses ($47,592.50 − $36,485.99 = $11,106.51 with default data; $11,411.31 after test entries). The dashboard also has no total income/total expenses figures at all — only current-month cards (Monthly Income $556, Monthly Expenses $251, Net Profit/Loss $305 for Nov 2026), which reflect only that month's transactions, not the sums of all income/expense transactions as expected.
- [ ] CT-02: Monthly P&L report values match the underlying transactions.
  - Action: Compare the selected month's report figures (income, expenses, profit/loss) against that month's default transactions.
  - Expected: Report income, expenses, and profit/loss exactly match the sums of the corresponding transactions for that month.
  - Bug Report:
    - Issue: Unverifiable Report Data — report month selector excludes months containing the default transactions
    - Actual: The Reports month selector offers only Nov 2026–Dec 2025, so no month containing the default transactions (Oct–Dec 2024) can be selected and the specified comparison against default transactions cannot be performed. For reference, on the only selectable month with transactions (November 2026) the report figures did match its transactions exactly (income $555.55, expenses $250.75, profit +$304.80), but this cannot be confirmed for the default data set the checklist targets.