# Test Result

## Functionality

- [ ] FT-01: Create an income transaction
  - Action: Click "Add Transaction", set Type to "Income", enter Amount 500.00, use today's date, pick any existing Category and Account, click "Save".
  - Expected: The transaction appears at the top of the Transactions list showing Income, 500.00, and the selected Category and Account.
  - Bug Report:
    - Issue: Missing Element (Account selector)
    - Actual: The Add Transaction dialog has no Account field, so an Account cannot be picked. The save button is labelled "Add Income", not "Save". The saved row shows "Consulting" and "+$500.00" at the top of the list, but no "Income" label and no Account.

- [ ] FT-02: Create an expense transaction
  - Action: Click "Add Transaction", set Type to "Expense", enter Amount 120.00, use today's date, pick any existing Category and Account, click "Save".
  - Expected: The transaction appears in the Transactions list showing Expense, 120.00, and the selected Category and Account.
  - Bug Report:
    - Issue: Missing Element (Account selector)
    - Actual: The dialog has no Account field, so an Account cannot be picked. The save button is labelled "Add Expense", not "Save". The saved row shows "Utilities" and "-$120.00" at the top of the list, but no "Expense" label and no Account.

- [ ] FT-03: Create an invoice
  - Action: Go to "Invoices", click "New Invoice", select an existing customer, add one line item of 300.00, set a due date 30 days out, click "Save".
  - Expected: The invoice appears in the Invoices list with status "Unpaid" and total 300.00.
  - Bug Report:
    - Issue: Missing Feature (Invoices page)
    - Actual: The navigation has no "Invoices" item (only Dashboard, Transactions, Categories, Reports, Tax Summary). Loading /invoices shows the app's 404 page ("NotFound"). No "New Invoice" button exists.

- [ ] FT-04: Create a bill
  - Action: Go to "Bills", click "New Bill", select an existing vendor, enter Amount 200.00 and a due date, click "Save".
  - Expected: The bill appears in the Bills list with status "Unpaid" and amount 200.00.
  - Bug Report:
    - Issue: Missing Feature (Bills page)
    - Actual: The navigation has no "Bills" item. Loading /bills shows the app's 404 page ("NotFound"). No "New Bill" button exists.

- [ ] FT-05: Record a full payment against an invoice
  - Action: Open the invoice from FT-03, click "Record Payment", enter the full outstanding amount, select an account, click "Save Payment".
  - Expected: Status changes to "Paid", outstanding balance shows 0.00, and the payment appears in the invoice's payment history.
  - Bug Report:
    - Issue: Blocked by Missing Feature (Invoices)
    - Actual: FT-03 could not create an invoice, and no invoices exist. There is no invoice to open and no "Record Payment" control anywhere in the app. Also, no Account selector exists in the transaction form (see FT-01).

- [X] FT-06: Edit an existing transaction
  - Action: Open any existing transaction, change its Category to a different existing category and its Amount to 250.00, click "Save".
  - Expected: The Transactions list row shows the new Category and Amount, and the old values no longer appear.

- [X] FT-07: Filter transactions by date range
  - Action: On "Transactions", set From to the 1st and To to the last day of a month that has data, click "Apply".
  - Expected: Only transactions dated within that range are listed, and no transactions outside it appear.

- [X] FT-08: Filter transactions by category
  - Action: Open the "Category" filter, select an existing category with transactions.
  - Expected: Only transactions assigned to that category are listed, and the count matches the rows shown.

- [ ] FT-09: View the monthly Profit & Loss report
  - Action: Go to "Reports" > "Profit & Loss", select a month with data, click "Generate".
  - Expected: The report displays the sections "Total Income", "Total Expenses", and "Net Profit" for that month.
  - Bug Report:
    - Issue: Missing Element (Profit & Loss view, Generate button)
    - Actual: The Reports page has no "Profit & Loss" sub-view and no "Generate" button. The report renders on month selection with the sections "Total Income", "Total Expenses", and "Net Profit/Loss" (not "Net Profit"). The month list only covers December 2025 to November 2026, so the 2024 seed data cannot be reported.

- [ ] FT-10: View dashboard financial status
  - Action: Open "Dashboard".
  - Expected: Tiles display "Income", "Expenses", and "Net Profit" for the current month, plus "Outstanding Invoices" and "Upcoming Bills".
  - Bug Report:
    - Issue: Missing Element (Outstanding Invoices, Upcoming Bills tiles)
    - Actual: The dashboard shows "Total Balance", "Monthly Income", "Monthly Expenses", and "Net Profit/Loss". There are no "Outstanding Invoices" or "Upcoming Bills" tiles. The labels differ slightly from the expected "Income", "Expenses", and "Net Profit".

- [ ] FT-11: Mark a transaction as tax-related
  - Action: Open an existing transaction, check "Tax-related", click "Save".
  - Expected: The Transactions list shows a "Tax" tag on that row, and it is included when the "Tax-related" filter is applied.
  - Bug Report:
    - Issue: Missing Element (Tax tag, Tax-related filter)
    - Actual: After ticking "Tax Related" and saving, the row's Tax column shows a "✓" glyph, with no "Tax" tag text. The filter bar offers only "All Types" and "All Categories", so there is no Tax-related filter.

- [X] FT-12: Generate a tax summary
  - Action: Go to "Tax Summary", select a tax year that has tax-flagged transactions, click "Generate".
  - Expected: The summary lists each category with the total of its tax-flagged transactions for that year, plus a grand total.

- [ ] FT-13: Print the tax summary
  - Action: On "Tax Summary", click "Print" and review the print preview.
  - Expected: The preview shows the summary table and the selected tax year in the header, and the navigation menu and action buttons are hidden.
  - Bug Report:
    - Issue: Print Layout Defect (action buttons not hidden)
    - Actual: With print media emulated, the navigation is hidden and the header "Fiscal Year 2026" and the summary table are shown. The "Print Report" button and the year selector ("2026") remain visible.

## Constraint

- [ ] CS-01: Block saving a transaction with required fields empty
  - Action: Click "Add Transaction", leave Amount, Date, and Category empty, click "Save".
  - Expected: Save is blocked, "Required" messages appear under each empty field, and no transaction is created.
  - Bug Report:
    - Issue: Missing Validation Messages
    - Actual: With Date, Amount, and Category empty, clicking save left the dialog open and created no row (row count unchanged). No "Required" text appeared under any field.

- [ ] CS-02: Reject a non-positive transaction amount
  - Action: Click "Add Transaction", enter Amount 0, click "Save"; then enter -50 and click "Save".
  - Expected: Both attempts show "Amount must be greater than 0", and no transaction is saved.
  - Bug Report:
    - Issue: Missing Validation Message
    - Actual: Amount 0 and Amount -50 were both rejected (no row created, row count unchanged), but neither attempt showed "Amount must be greater than 0" anywhere in the dialog.

- [ ] CS-03: Block a payment that exceeds the outstanding balance
  - Action: Open an unpaid invoice with a known outstanding balance X, click "Record Payment", enter X + 1, click "Save Payment".
  - Expected: The message "Payment exceeds outstanding balance" appears, and the balance and status are unchanged.
  - Bug Report:
    - Issue: Blocked by Missing Feature (Invoices)
    - Actual: No unpaid invoice exists. /invoices returns 404, and there is no "Record Payment" control in the app.

## Interaction

- [ ] IX-01: Show a success toast after saving a transaction
  - Action: Create a valid transaction via "Add Transaction" and click "Save".
  - Expected: A toast reading "Transaction saved" appears and disappears automatically within about 5 seconds.
  - Bug Report:
    - Issue: Missing Toast
    - Actual: After saving valid transactions (three times), the text "Transaction saved" was never observed. I polled the page for 3 to 6 seconds after each save.

- [ ] IX-02: Confirm before deleting a transaction
  - Action: Click the trash icon on a transaction, then click "Cancel" in the dialog; repeat and click "Delete".
  - Expected: The dialog "Delete this transaction?" appears. "Cancel" keeps the transaction in the list, and "Delete" removes it.
  - Bug Report:
    - Issue: Dialog Text Mismatch
    - Actual: The trash icon opens a dialog titled "Delete Transaction" that reads "Are you sure you want to delete this transaction? This action cannot be undone." The text "Delete this transaction?" does not appear. The Cancel and Delete behaviour itself is correct: Cancel kept the row, and Delete removed it.

## Content

- [X] CT-01: Report totals match underlying transactions
  - Action: Note Total Income and Total Expenses in the P&L report for a month, then filter Transactions to that month and add up the Income and Expense rows.
  - Expected: The report totals match the sums to the cent, and Net Profit equals Income minus Expenses.

- [ ] CT-02: Labels are relevant and free of placeholder text
  - Action: Open the Category and Account dropdowns, the Invoices and Bills lists, and the Dashboard and Reports pages.
  - Expected: Category, account, customer, and vendor names are relevant bookkeeping labels, and no "undefined", "NaN", "Lorem", "Test", or "Untitled" text appears.
  - Bug Report:
    - Issue: Missing Pages (Invoices, Bills, Account dropdown)
    - Actual: /invoices and /bills return 404, so the Invoices and Bills lists could not be checked. No Account dropdown exists. The Category options (Sales Revenue, Consulting, Interest Income, Other Income, Office Supplies, Rent, Utilities, Salaries, Marketing, Travel, Software, Insurance) and the Dashboard and Reports labels contain no placeholder text. My own QA entries were named "QA Test …" and were not used in this judgement.

---

**Notes:**
- FT-07 and FT-12 passed even though the "Apply" and "Generate" buttons the checklist names do not exist. Filters and summaries apply automatically, and the expected results are met.
- Transactions I created during the run were lost after a page reload (the list returned to the 18 seed rows). Data is not persisted across reloads.
- Counted results: 5 PASS (FT-06, FT-07, FT-08, FT-12, CT-01), 24 FAIL, 0 skipped. About 37 of the 100 tool-call budget were used.