# Test Checklist

## Functionality
- [ ] FT-01: Record a new income transaction.
  - Action: Open the transaction entry form, select type "Income", fill in a description, amount, date, and category, then save.
  - Expected: The new income transaction appears in the transaction list with type "Income" and the entered amount.
- [ ] FT-02: Record a new expense transaction.
  - Action: Open the transaction entry form, select type "Expense", fill in a description, amount, date, and category, then save.
  - Expected: The new expense transaction appears in the transaction list with type "Expense" and the entered amount.
- [ ] FT-03: Create financial records of each supported type (invoice, bill, payment).
  - Action: Create one invoice, one bill, and one payment record using default data.
  - Expected: All three records appear in the records list with the correct type label (Invoice / Bill / Payment) and amounts.
- [ ] FT-04: Assign a transaction to a category and an account.
  - Action: Edit an existing transaction and change its category to a different existing category and its account to a different existing account, then save.
  - Expected: The transaction list shows the transaction with the newly selected category and account.
- [ ] FT-05: Create a custom category.
  - Action: Open category management, create a new category (e.g., "Travel"), and save.
  - Expected: The new category appears in the category list and is selectable in the transaction category dropdown.
- [ ] FT-06: Edit and adjust an existing entry.
  - Action: Open an existing transaction, change its amount and description, and save the changes.
  - Expected: The updated amount and description are shown in the transaction list; the old values are gone.
- [ ] FT-07: Delete an entry.
  - Action: Delete an existing transaction or record and confirm the deletion.
  - Expected: The item is removed from the transaction/records list and no longer appears anywhere in the app.
- [ ] FT-08: Filter records by date range.
  - Action: Set the date filter to a range covering only some of the default records.
  - Expected: Only records with dates inside the selected range are displayed.
- [ ] FT-09: Filter records by category.
  - Action: Select a category that some default records belong to in the category filter.
  - Expected: Only records assigned to the selected category are displayed.
- [ ] FT-10: View monthly profit and loss report.
  - Action: Open the reports section and select a month that contains default transactions.
  - Expected: A profit and loss report for that month is displayed, showing income, expenses, and profit/loss figures.
- [ ] FT-11: Mark and unmark a record as tax-related.
  - Action: Toggle the tax-related control on an existing record, then toggle it off again.
  - Expected: The record is included in tax-related views when marked and excluded when unmarked.
- [ ] FT-12: Generate a tax summary.
  - Action: Mark at least one record as tax-related, then open/generate the tax summary.
  - Expected: The tax summary displays only tax-marked records with their amounts and a tax-related total figure.
- [ ] FT-13: Print the tax summary.
  - Action: With the tax summary open, click the "Print" button.
  - Expected: The browser print dialog (or a print-friendly view) opens showing the tax summary content.

## Constraint
- [ ] CS-01: Cannot save a transaction with missing required fields.
  - Action: Submit the transaction form with the amount field empty (and again with the description empty).
  - Expected: The save is rejected and a validation error indicates the missing required field; no new record is created.
- [ ] CS-02: Cannot save a transaction with a zero or negative amount.
  - Action: Enter 0 and then a negative value (e.g., -50) in the amount field and submit.
  - Expected: The save is rejected with a validation error stating the amount must be greater than zero; no record is created.
- [ ] CS-03: Cannot delete a category that is assigned to existing records.
  - Action: Attempt to delete a category that is used by at least one default transaction.
  - Expected: The deletion is blocked with a message indicating the category is in use; the category and its transactions remain.

## Interaction
- [ ] IX-01: Success confirmation after saving a record.
  - Action: Save a new transaction or financial record.
  - Expected: A visible success confirmation (e.g., toast or inline message) appears immediately after saving.
- [ ] IX-02: Tax-related toggle gives immediate visual feedback on the record.
  - Action: Click the tax-related toggle on a record in the list or detail view.
  - Expected: The record's tax indicator changes state (e.g., checkbox checked/unchecked or badge shown/hidden) immediately without a manual refresh.

## Content
- [ ] CT-01: Dashboard totals match the underlying records.
  - Action: Compare the dashboard's total income, total expenses, and net balance against the amounts of the default transactions in the list.
  - Expected: Dashboard income equals the sum of all income transactions, expenses equal the sum of all expense transactions, and balance equals income minus expenses.
- [ ] CT-02: Monthly P&L report values match the underlying transactions.
  - Action: Compare the selected month's report figures (income, expenses, profit/loss) against that month's default transactions.
  - Expected: Report income, expenses, and profit/loss exactly match the sums of the corresponding transactions for that month.