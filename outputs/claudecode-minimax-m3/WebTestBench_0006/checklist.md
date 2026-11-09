# Test Checklist

## Functionality
- [ ] FT-01: User can create a new income transaction
  - Action: Click "Add Income" or equivalent, enter amount, date, category, description, and save
  - Expected: Transaction appears in the records list with type "Income" and the entered values
- [ ] FT-02: User can create a new expense transaction
  - Action: Click "Add Expense" or equivalent, enter amount, date, category, description, and save
  - Expected: Transaction appears in the records list with type "Expense" and the entered values
- [ ] FT-03: User can create invoice, bill, and payment records
  - Action: Use the create-record function to add one of each record type (Invoice, Bill, Payment) and save
  - Expected: Each record type appears in the records list with its correct type label
- [ ] FT-04: User can assign transactions to customizable categories or accounts
  - Action: Create a transaction and select a category from the available list (using default categories)
  - Expected: The chosen category is saved and visible on the transaction
- [ ] FT-05: User can view a monthly profit and loss report
  - Action: Navigate to the Reports section and open the "Profit and Loss" report for a month containing default data
  - Expected: Report displays total income, total expenses, and net profit/loss for that month
- [ ] FT-06: User can filter records by date range
  - Action: Apply a date range filter on the records list (e.g., a specific month)
  - Expected: Only transactions within that date range are displayed
- [ ] FT-07: User can filter records by category
  - Action: Select a category from the category filter on the records list
  - Expected: Only transactions assigned to that category are displayed
- [ ] FT-08: User can edit an existing transaction
  - Action: Open an existing default transaction, change the amount or description, and save
  - Expected: Updated values are reflected in the records list and any reports/dashboard totals
- [ ] FT-09: User can delete a transaction
  - Action: Select an existing transaction and click the delete/remove action
  - Expected: The transaction is removed from the records list and excluded from totals
- [ ] FT-10: User can mark a transaction as tax-related
  - Action: Open or create a transaction, enable the "Tax-related" flag, and save
  - Expected: The transaction is visibly flagged as tax-related in the records list
- [ ] FT-11: User can generate a tax summary report
  - Action: Navigate to the tax section and open the tax summary report
  - Expected: A summary is displayed listing only tax-related transactions with totals
- [ ] FT-12: User can print the tax summary
  - Action: From the tax summary view, click "Print"
  - Expected: The browser print dialog opens with a print-formatted view of the tax summary
- [ ] FT-13: User can view a dashboard of financial status
  - Action: Navigate to the Dashboard
  - Expected: Dashboard shows key financial indicators (e.g., total income, total expenses, balance) based on default data

## Constraint
- [ ] CS-01: Cannot save a transaction with missing required fields
  - Action: Click "Save" on a new transaction form with the amount or date field left empty
  - Expected: The form is not saved and a validation error indicates which required fields are missing
- [ ] CS-02: Amount must accept only positive numeric values
  - Action: Enter a negative number or non-numeric text (e.g., "-50" or "abc") in the amount field and attempt to save
  - Expected: The entry is rejected with a validation error; negative or non-numeric amounts are not saved
- [ ] CS-03: Tax summary includes only transactions marked as tax-related
  - Action: Compare the tax summary's transaction list against the full records list filtered by the "Tax-related" flag
  - Expected: Every item in the tax summary has the tax-related flag; no non-tax items appear, and no tax-marked items are missing

## Interaction
- [ ] IX-01: Success notification appears after creating a transaction
  - Action: Successfully create a new income or expense transaction
  - Expected: A success message/toast/banner confirms the transaction was created
- [ ] IX-02: Dashboard updates after transactions are added, edited, or deleted
  - Action: Note a dashboard total, then add, edit, or delete a transaction and return to the dashboard
  - Expected: The dashboard totals reflect the change without requiring a manual page refresh
- [ ] IX-03: Filter results update immediately when a filter is applied
  - Action: Change the date range or category filter on the records list
  - Expected: The list updates without requiring an additional "Apply" click

## Content
- [ ] CT-01: Profit and loss totals match the underlying transactions
  - Action: Manually sum the income and expense transactions for a given month and compare to the report
  - Expected: The report's total income, total expenses, and net profit/loss equal the manual sums
- [ ] CT-02: Tax summary clearly identifies tax-related items
  - Action: Open the tax summary report
  - Expected: Each listed item shows an identifiable label (e.g., date, amount, description, tax flag) so it can be reviewed for tax purposes