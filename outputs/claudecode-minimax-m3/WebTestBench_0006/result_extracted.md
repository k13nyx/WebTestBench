# Test Result

## Functionality

- [X] FT-01: User can create a new income transaction
  - Action: Click "Add Income" or equivalent, enter amount, date, category, description, and save
  - Expected: Transaction appears in the records list with type "Income" and the entered values
- [X] FT-02: User can create a new expense transaction
  - Action: Click "Add Expense" or equivalent, enter amount, date, category, description, and save
  - Expected: Transaction appears in the records list with type "Expense" and the entered values
- [ ] FT-03: User can create invoice, bill, and payment records
  - Action: Use the create-record function to add one of each record type (Invoice, Bill, Payment) and save
  - Expected: Each record type appears in the records list with its correct type label
  - Bug Report:
    - Issue: Missing Record Types (only Income/Expense supported)
    - Actual: The Add Transaction modal's Type selector offers only "Income" and "Expense" (the list page's Type filter offers only "All Types / Income / Expense"); no Invoice, Bill or Payment option exists anywhere in the app. Creating records with Reference values INV-TEST-001, BILL-TEST-001 and PAY-TEST-001 produced rows "QA Invoice Rec | Sales Revenue | INV-TEST-001 | +$500.00", "QA Bill Rec | Office Supplies | BILL-TEST-001 | -$300.00" and "QA Payment Rec | Office Supplies | PAY-TEST-001 | -$200.00" — the reference is only a free-text identifier; the records list columns (DATE, DESCRIPTION, CATEGORY, REFERENCE, AMOUNT, TAX, ACTIONS) show no Invoice/Bill/Payment type label, and the only type distinction rendered is the +/− amount sign.
- [X] FT-04: User can assign transactions to customizable categories or accounts
  - Action: Create a transaction and select a category from the available list (using default categories)
  - Expected: The chosen category is saved and visible on the transaction
- [ ] FT-05: User can view a monthly profit and loss report
  - Action: Navigate to the Reports section and open the "Profit and Loss" report for a month containing default data
  - Expected: Report displays total income, total expenses, and net profit/loss for that month
  - Bug Report:
    - Issue: Report Month Selector Cannot Reach Data (no "Profit and Loss" report route)
    - Actual: /reports is the only report (routes /reports/profit-loss, /reports/profit-and-loss, /reports/pnl all render the app's 404 page) and shows a monthly P&L, but its month picker lists exactly 12 options — November 2026 back to December 2025. All default transactions are dated Oct 5 – Dec 15, 2024, so no month containing default data is selectable; with the default data loaded the report shows "November 2026 / Total Income $0 / Total Expenses $0 / Net Profit/Loss +$0 / No data for this period". URL parameters (?month=2024-12, ?month=12-2024, ?date=2024-12, ?year=2024&month=12, ?period=2024-12) are ignored — the report still shows November 2026.
- [X] FT-06: User can filter records by date range
  - Action: Apply a date range filter on the records list (e.g., a specific month)
  - Expected: Only transactions within that date range are displayed
- [X] FT-07: User can filter records by category
  - Action: Select a category from the category filter on the records list
  - Expected: Only transactions assigned to that category are displayed
- [ ] FT-08: User can edit an existing transaction
  - Action: Open an existing default transaction, change the amount or description, and save
  - Expected: Updated values are reflected in the records list and any reports/dashboard totals
  - Bug Report:
    - Issue: Data Loss on Edit (Category Silently Cleared)
    - Actual: Editing "QA Income Record" (category "Sales Revenue") to $1,500.00 did apply the amount and updated the list/totals (Total Income +$48,592.50 → +$49,092.50), but the saved row lost its category: "Nov 7, 2026 | QA Income Record EDITED | (blank) | — | +$1,500.00", and the Reports page then listed the $1,500 under "Income by Category: Unknown" instead of "Sales Revenue". The Edit modal had shown the placeholder "Select category" rather than the record's category. The failure is prefill-dependent: a description-only edit of the default record "Electric Bill" pre-filled "Utilities" and saved cleanly, while the Edit modal for "Bank Interest" also showed "Select category".
- [X] FT-09: User can delete a transaction
  - Action: Select an existing transaction and click the delete/remove action
  - Expected: The transaction is removed from the records list and excluded from totals
- [X] FT-10: User can mark a transaction as tax-related
  - Action: Open or create a transaction, enable the "Tax-related" flag, and save
  - Expected: The transaction is visibly flagged as tax-related in the records list
- [X] FT-11: User can generate a tax summary report
  - Action: Navigate to the tax section and open the tax summary report
  - Expected: A summary is displayed listing only tax-related transactions with totals
- [X] FT-12: User can print the tax summary
  - Action: From the tax summary view, click "Print"
  - Expected: The browser print dialog opens with a print-formatted view of the tax summary
- [ ] FT-13: User can view a dashboard of financial status
  - Action: Navigate to the Dashboard
  - Expected: Dashboard shows key financial indicators (e.g., total income, total expenses, balance) based on default data
  - Bug Report:
    - Issue: Static Dashboard Values (Total Balance not derived from data) + Default Data Not Reflected
    - Actual: With the 18 default transactions loaded, the Dashboard shows "Total Balance $74,931", "Monthly Income $0", "Monthly Expenses $0", "Net Profit/Loss $0", an "Expenses by Category" panel listing 6 category names with no amounts, and an "Income vs Expenses" chart whose bars all read $0k. The Total Balance card is hard-coded: it remained $74,931 after adding a $25.00 expense, after editing an income to $1,500.00 and after deleting a $5.00 expense, and it matches no total in the data (default transactions sum to income $47,592.50, expenses $36,485.99, net $11,106.51). The monthly cards are scoped to the current month (Nov 2026), which contains no default transactions.

## Constraint

- [X] CS-01: Cannot save a transaction with missing required fields
  - Action: Click "Save" on a new transaction form with the amount or date field left empty
  - Expected: The form is not saved and a validation error indicates which required fields are missing
- [X] CS-02: Amount must accept only positive numeric values
  - Action: Enter a negative number or non-numeric text (e.g., "-50" or "abc") in the amount field and attempt to save
  - Expected: The entry is rejected with a validation error; negative or non-numeric amounts are not saved
- [X] CS-03: Tax summary includes only transactions marked as tax-related
  - Action: Compare the tax summary's transaction list against the full records list filtered by the "Tax-related" flag
  - Expected: Every item in the tax summary has the tax-related flag; no non-tax items appear, and no tax-marked items are missing

## Interaction

- [ ] IX-01: Success notification appears after creating a transaction
  - Action: Successfully create a new income or expense transaction
  - Expected: A success message/toast/banner confirms the transaction was created
  - Bug Report:
    - Issue: Missing Success Notification (Unresponsive Feedback)
    - Actual: After successfully saving a new income transaction ("QA Income Record", +$1,000.00, which appeared in the list and raised Total Income to +$48,592.50), no toast, banner or message appeared. The app's live regions ("Notifications (F8)" and "Notifications alt+T") stayed empty, and a DOM scan polled every 110 ms for 1.5 s after the save found no element containing "success", "created" or "added" text. The same absence occurred after an edit and after a delete — the modal simply closes with no confirmation.
- [X] IX-02: Dashboard updates after transactions are added, edited, or deleted
  - Action: Note a dashboard total, then add, edit, or delete a transaction and return to the dashboard
  - Expected: The dashboard totals reflect the change without requiring a manual page refresh
- [X] IX-03: Filter results update immediately when a filter is applied
  - Action: Change the date range or category filter on the records list
  - Expected: The list updates without requiring an additional "Apply" click

## Content

- [X] CT-01: Profit and loss totals match the underlying transactions
  - Action: Manually sum the income and expense transactions for a given month and compare to the report
  - Expected: The report's total income, total expenses, and net profit/loss equal the manual sums
- [X] CT-02: Tax summary clearly identifies tax-related items
  - Action: Open the tax summary report
  - Expected: Each listed item shows an identifiable label (e.g., date, amount, description, tax flag) so it can be reviewed for tax purposes
