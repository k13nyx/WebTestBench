# Test Checklist

## Functionality
- [ ] FT-01: Add an income transaction
  - Action: Create a new income transaction with amount, date, and category using the default data categories.
  - Expected: The income transaction is saved and appears in the transaction list with correct amount, date, and category.
- [ ] FT-02: Add an expense transaction
  - Action: Create a new expense transaction with amount, date, and category.
  - Expected: The expense transaction is saved and appears in the transaction list marked as an expense.
- [ ] FT-03: Create an invoice record
  - Action: Create a new invoice with a payee, amount, and due date.
  - Expected: The invoice is saved and visible in the financial records list.
- [ ] FT-04: Create a bill and record a payment against it
  - Action: Create a new bill, then record a payment applied to that bill.
  - Expected: The bill is created, and the payment is linked to it with updated balance/status.
- [ ] FT-05: Edit an existing transaction
  - Action: Change the amount and category of an existing transaction, then save.
  - Expected: The transaction list shows the updated amount and category.
- [ ] FT-06: Delete an existing transaction
  - Action: Delete a transaction from the records list.
  - Expected: The transaction is removed from the list and no longer counted in totals.
- [ ] FT-07: Create a custom category and assign it
  - Action: Create a new category, then create a transaction using that category.
  - Expected: The new category is selectable and the transaction displays it.
- [ ] FT-08: Create a custom account and assign a record to it
  - Action: Create a new account, then assign an existing or new record to that account.
  - Expected: The account is saved and the record shows the assigned account.
- [ ] FT-09: View monthly profit and loss report
  - Action: Open the profit and loss report for a month containing both income and expense default data.
  - Expected: The report displays total income, total expense, and net profit/loss for that month.
- [ ] FT-10: View financial dashboard
  - Action: Navigate to the dashboard.
  - Expected: The dashboard shows current financial status summaries (e.g., income, expenses, balance) consistent with the records.
- [ ] FT-11: Filter records by date range
  - Action: Apply a date-range filter to the transaction list.
  - Expected: Only transactions within the selected date range are displayed.
- [ ] FT-12: Filter records by category
  - Action: Select a category filter on the records list.
  - Expected: Only transactions belonging to the selected category are displayed.
- [ ] FT-13: Generate a tax summary
  - Action: Mark at least one transaction as tax-related, then generate the tax summary.
  - Expected: The tax summary displays totals derived from the tax-related items.

## Constraint
- [ ] CS-01: Cannot save a transaction with empty required fields
  - Action: Attempt to save a new transaction with empty amount and/or missing category.
  - Expected: The transaction is not saved, and a validation error identifies the missing required fields.
- [ ] CS-02: Amount must be a valid positive number
  - Action: Attempt to save a transaction with a negative, zero, or non-numeric amount.
  - Expected: The transaction is not saved, and an error message indicates the amount is invalid.
- [ ] CS-03: Tax summary excludes non-tax-related items
  - Action: Generate the tax summary when records exist both marked and not marked as tax-related.
  - Expected: Only items marked as tax-related are included in the tax summary totals.

## Interaction
- [ ] IX-01: Confirmation feedback after saving a record
  - Action: Save a new transaction.
  - Expected: A success message or confirmation appears indicating the record was saved, and the list updates to include it.
- [ ] IX-02: Report reflects edits immediately
  - Action: Edit a transaction amount, then reopen the profit and loss report for that month.
  - Expected: The report totals update to reflect the edited amount without requiring a reload.
- [ ] IX-03: Print action opens a printable tax summary
  - Action: Click the print action on the tax summary.
  - Expected: A print dialog opens showing the tax summary formatted for printing.

## Content
- [ ] CT-01: Dashboard figures match underlying records
  - Action: Compare dashboard summary figures against the transaction list totals for the same period.
  - Expected: Dashboard figures are identical to the transaction list totals.
- [ ] CT-02: Tax summary content matches tax-related records
  - Action: Review the generated tax summary against the records marked as tax-related.
  - Expected: The summary lists correct items, categories, and totals matching those records.