# Test Checklist

## Functionality
- [ ] FT-01: Create an income record (invoice/payment received)
  - Action: Open "Add Record", select type "Income", fill amount/date, click "Save".
  - Expected: The new income record appears in the records list.
- [ ] FT-02: Create an expense record (bill/payment made)
  - Action: Open "Add Record", select type "Expense", fill amount/date, click "Save".
  - Expected: The new expense record appears in the records list.
- [ ] FT-03: Assign a record to a category
  - Action: On an existing record, open its edit view, choose a category, click "Save".
  - Expected: The record displays the selected category label.
- [ ] FT-04: Assign a record to an account
  - Action: On an existing record, open its edit view, choose an account, click "Save".
  - Expected: The record displays the selected account.
- [ ] FT-05: Edit/adjust an existing entry
  - Action: Open a record, change its amount or date, click "Save".
  - Expected: The updated values are reflected in the records list.
- [ ] FT-06: View monthly profit and loss summary
  - Action: Navigate to "Reports" and open "Profit & Loss", select a month.
  - Expected: Report shows total income, total expenses, and net profit/loss for the month.
- [ ] FT-07: View financial status dashboard
  - Action: Navigate to the "Dashboard" page.
  - Expected: Dashboard displays summarized financial status (totals/balances).
- [ ] FT-08: Filter records by date range
  - Action: Open the records view, set a date range filter, click "Apply".
  - Expected: Only records within the date range are shown.
- [ ] FT-09: Filter records by category
  - Action: Open the records view, select a category filter, click "Apply".
  - Expected: Only records of the selected category are shown.
- [ ] FT-10: Create and manage custom categories
  - Action: Open "Categories", click "Add Category", enter a name, save; then edit/delete it.
  - Expected: Category appears in the category list and is selectable on records.
- [ ] FT-11: Mark a record as tax-related
  - Action: Open a record, toggle "Tax-related" on, click "Save".
  - Expected: The record is flagged as tax-related (e.g., a tax indicator is shown).
- [ ] FT-12: Generate and view tax summary
  - Action: Navigate to "Tax Summary" report.
  - Expected: A tax summary report is generated and displayed.

## Constraint
- [ ] CS-01: Required fields must be validated on record creation
  - Action: Open "Add Record" and click "Save" with amount, date, or type left empty.
  - Expected: Save is blocked and a validation error identifies the missing required field(s).
- [ ] CS-02: Amount must be valid before saving
  - Action: Enter a non-numeric or zero/negative amount and click "Save".
  - Expected: Save is blocked with an error stating the amount is invalid.
- [ ] CS-03: Tax summary includes only tax-related items
  - Action: Generate the tax summary with some records marked tax-related and others not.
  - Expected: Only tax-related records appear in the summary; non-tax records are excluded.
- [ ] CS-04: Profit & Loss totals reconcile
  - Action: On the monthly P&L report, sum displayed income and expense line items.
  - Expected: Net profit/loss equals total income minus total expenses.

## Interaction
- [ ] IX-01: Confirmation after saving a record
  - Action: Create or edit a record and click "Save".
  - Expected: A success message/toast confirms the record was saved.
- [ ] IX-02: Print dialog from tax summary
  - Action: Open the tax summary and click the "Print" button.
  - Expected: The browser print dialog opens showing the tax summary.

## Content
- [ ] CT-01: Reports use correct financial labels
  - Action: Open the P&L and Tax Summary reports.
  - Expected: Reports clearly label "Income", "Expenses", and "Net Profit/Loss" (and "Tax") with relevant, correctly spelled text.
- [ ] CT-02: Category and account options are relevant
  - Action: Open the category/account selectors on a record.
  - Expected: Listed categories/accounts are finance-relevant (e.g., Revenue, Utilities, Bank) with no irrelevant or placeholder entries.