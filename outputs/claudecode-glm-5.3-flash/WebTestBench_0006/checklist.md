# Test Checklist

## Functionality
- [ ] FT-01: User can create an income transaction
  - Action: Open the "Add Transaction" / "New Record" form, select type "Income", enter amount (e.g., 500), date, and description, then submit.
  - Expected: The income transaction is saved and appears in the transaction list with the correct amount, date, and description.
- [ ] FT-02: User can create an expense transaction
  - Action: Open the form, select type "Expense", enter amount (e.g., 120), date, and description, then submit.
  - Expected: The expense transaction is saved and appears in the transaction list.
- [ ] FT-03: User can create an invoice record
  - Action: Navigate to the invoices/bills section, click "New Invoice", fill in required fields (e.g., customer name, amount, date), and save.
  - Expected: The invoice is created and listed with its details.
- [ ] FT-04: User can create a bill or payment record
  - Action: Create a new bill or payment record with valid details and save it.
  - Expected: The record is created and appears in the corresponding records list.
- [ ] FT-05: User can edit an existing entry
  - Action: Open an existing transaction/invoice, change its amount or description, and save.
  - Expected: The updated value is reflected in the record and in any dependent summaries.
- [ ] FT-06: User can delete an entry
  - Action: Delete an existing transaction/record and confirm (if prompted).
  - Expected: The record is removed from the list and no longer counts toward reports.
- [ ] FT-07: User can create a custom category/account
  - Action: Go to the categories/accounts section, click "Add Category", enter a name (e.g., "Office Supplies"), and save.
  - Expected: The new category appears in the category list and is selectable when creating records.
- [ ] FT-08: User can assign a category to a transaction
  - Action: Create or edit a transaction and choose a category from the category selector, then save.
  - Expected: The transaction displays its assigned category.
- [ ] FT-09: Filter records by date range
  - Action: Set a date-range filter (e.g., current month) on the records list.
  - Expected: Only records whose dates fall within the range are displayed.
- [ ] FT-10: Filter records by category
  - Action: Select a specific category in the filter control.
  - Expected: Only records assigned to that category are displayed.
- [ ] FT-11: Monthly profit and loss report shows correct totals
  - Action: Open the reports view for a month that has known income and expense records.
  - Expected: The report shows total income, total expenses, and net profit/loss equal to the sum of that month's records.
- [ ] FT-12: User can mark a record as tax-related
  - Action: Edit or create a record and toggle the "Tax-related" flag, then save.
  - Expected: The record is visibly marked as tax-related (e.g., badge or flag shown in the list).
- [ ] FT-13: Tax summary generates correct totals and is printable
  - Action: Open the tax summary view and use the print action (or print preview).
  - Expected: The summary lists tax-related records and their total, and a print dialog/preview can be triggered.

## Constraint
- [ ] CS-01: Cannot save a record with empty required fields
  - Action: Submit the new-record form leaving required fields (e.g., amount or date) blank.
  - Expected: The form is not submitted and a validation message is shown.
- [ ] CS-02: Amount must be a valid positive number
  - Action: Enter an invalid amount (e.g., "abc", negative, or 0) and submit.
  - Expected: Submission is blocked with a clear validation error; no record is created.
- [ ] CS-03: Category name must be unique/non-empty
  - Action: Attempt to create a category with an empty name or a name that already exists.
  - Expected: Creation is blocked with a validation message; no duplicate or blank category is added.

## Interaction
- [ ] IX-01: Dashboard reflects financial status after adding a record
  - Action: Note the dashboard totals, then add a new income transaction and return to the dashboard.
  - Expected: The dashboard totals (e.g., income, balance, profit) update to include the new record.
- [ ] IX-02: Confirmation feedback after saving or deleting
  - Action: Save a new record, then delete a record.
  - Expected: The app shows clear feedback (e.g., success toast/message) for each action and the list updates without requiring a manual reload.
- [ ] IX-03: Filtering controls update the list immediately
  - Action: Change the date or category filter while viewing records.
  - Expected: The visible list refreshes to match the new filter without a full page reload or manual refresh action.

## Content
- [ ] CT-01: Dashboard displays meaningful financial figures
  - Action: Open the dashboard.
  - Expected: It shows bookkeeping-specific content (e.g., total income, total expenses, net profit/loss) with correctly formatted currency values that match existing records.
- [ ] CT-02: Report and tax summary content is accurate and relevant
  - Action: Compare the monthly P&L report and tax summary against the records in the transaction list.
  - Expected: Record names, categories, amounts, and totals shown in the reports match the actual records; no placeholder or irrelevant content is displayed.