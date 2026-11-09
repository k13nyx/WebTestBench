# Test Checklist

## Functionality
- [ ] FT-01: Create an income transaction
  - Action: Click "Add Transaction", set Type to "Income", enter Amount 500.00, use today's date, pick any existing Category and Account, click "Save".
  - Expected: The transaction appears at the top of the Transactions list showing Income, 500.00, and the selected Category and Account.
- [ ] FT-02: Create an expense transaction
  - Action: Click "Add Transaction", set Type to "Expense", enter Amount 120.00, use today's date, pick any existing Category and Account, click "Save".
  - Expected: The transaction appears in the Transactions list showing Expense, 120.00, and the selected Category and Account.
- [ ] FT-03: Create an invoice
  - Action: Go to "Invoices", click "New Invoice", select an existing customer, add one line item of 300.00, set a due date 30 days out, click "Save".
  - Expected: The invoice appears in the Invoices list with status "Unpaid" and total 300.00.
- [ ] FT-04: Create a bill
  - Action: Go to "Bills", click "New Bill", select an existing vendor, enter Amount 200.00 and a due date, click "Save".
  - Expected: The bill appears in the Bills list with status "Unpaid" and amount 200.00.
- [ ] FT-05: Record a full payment against an invoice
  - Action: Open the invoice from FT-03, click "Record Payment", enter the full outstanding amount, select an account, click "Save Payment".
  - Expected: Status changes to "Paid", outstanding balance shows 0.00, and the payment appears in the invoice's payment history.
- [ ] FT-06: Edit an existing transaction
  - Action: Open any existing transaction, change its Category to a different existing category and its Amount to 250.00, click "Save".
  - Expected: The Transactions list row shows the new Category and Amount, and the old values no longer appear.
- [ ] FT-07: Filter transactions by date range
  - Action: On "Transactions", set From to the 1st and To to the last day of a month that has data, click "Apply".
  - Expected: Only transactions dated within that range are listed, and no transactions outside it appear.
- [ ] FT-08: Filter transactions by category
  - Action: Open the "Category" filter, select an existing category with transactions.
  - Expected: Only transactions assigned to that category are listed, and the count matches the rows shown.
- [ ] FT-09: View the monthly Profit & Loss report
  - Action: Go to "Reports" > "Profit & Loss", select a month with data, click "Generate".
  - Expected: The report displays the sections "Total Income", "Total Expenses", and "Net Profit" for that month.
- [ ] FT-10: View dashboard financial status
  - Action: Open "Dashboard".
  - Expected: Tiles display "Income", "Expenses", and "Net Profit" for the current month, plus "Outstanding Invoices" and "Upcoming Bills".
- [ ] FT-11: Mark a transaction as tax-related
  - Action: Open an existing transaction, check "Tax-related", click "Save".
  - Expected: The Transactions list shows a "Tax" tag on that row, and it is included when the "Tax-related" filter is applied.
- [ ] FT-12: Generate a tax summary
  - Action: Go to "Tax Summary", select a tax year that has tax-flagged transactions, click "Generate".
  - Expected: The summary lists each category with the total of its tax-flagged transactions for that year, plus a grand total.
- [ ] FT-13: Print the tax summary
  - Action: On "Tax Summary", click "Print" and review the print preview.
  - Expected: The preview shows the summary table and the selected tax year in the header, and the navigation menu and action buttons are hidden.

## Constraint
- [ ] CS-01: Block saving a transaction with required fields empty
  - Action: Click "Add Transaction", leave Amount, Date, and Category empty, click "Save".
  - Expected: Save is blocked, "Required" messages appear under each empty field, and no transaction is created.
- [ ] CS-02: Reject a non-positive transaction amount
  - Action: Click "Add Transaction", enter Amount 0, click "Save"; then enter -50 and click "Save".
  - Expected: Both attempts show "Amount must be greater than 0", and no transaction is saved.
- [ ] CS-03: Block a payment that exceeds the outstanding balance
  - Action: Open an unpaid invoice with a known outstanding balance X, click "Record Payment", enter X + 1, click "Save Payment".
  - Expected: The message "Payment exceeds outstanding balance" appears, and the balance and status are unchanged.

## Interaction
- [ ] IX-01: Show a success toast after saving a transaction
  - Action: Create a valid transaction via "Add Transaction" and click "Save".
  - Expected: A toast reading "Transaction saved" appears and disappears automatically within about 5 seconds.
- [ ] IX-02: Confirm before deleting a transaction
  - Action: Click the trash icon on a transaction, then click "Cancel" in the dialog; repeat and click "Delete".
  - Expected: The dialog "Delete this transaction?" appears. "Cancel" keeps the transaction in the list, and "Delete" removes it.

## Content
- [ ] CT-01: Report totals match underlying transactions
  - Action: Note Total Income and Total Expenses in the P&L report for a month, then filter Transactions to that month and add up the Income and Expense rows.
  - Expected: The report totals match the sums to the cent, and Net Profit equals Income minus Expenses.
- [ ] CT-02: Labels are relevant and free of placeholder text
  - Action: Open the Category and Account dropdowns, the Invoices and Bills lists, and the Dashboard and Reports pages.
  - Expected: Category, account, customer, and vendor names are relevant bookkeeping labels, and no "undefined", "NaN", "Lorem", "Test", or "Untitled" text appears.