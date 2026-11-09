# Test Result

Application: LedgerFlow - Simple Bookkeeping (http://localhost:6006/)
Method: Playwright DOM/accessibility inspection only (no screenshots).

## Functionality

- [X] FT-01: User can create an expense transaction.
  - Action: Open the "Add Transaction" form, enter an amount, pick a category, select type "Expense", and click "Save".
  - Expected: The expense is saved and appears in the transaction list with the entered amount and category.

- [X] FT-02: User can create an income transaction.
  - Action: Open the "Add Transaction" form, enter an amount, pick a category, select type "Income", and click "Save".
  - Expected: The income is saved and appears in the transaction list with the entered amount and category.

- [ ] FT-03: User can create a financial record of type "Invoice".
  - Action: Open the "Create Record" form, choose "Invoice", fill in the required fields, and click "Save".
  - Expected: The invoice is created and listed under the records with type "Invoice".
  - Bug Report:
    - Issue: Missing feature — no "Create Record" form and no "Invoice" record type exist in the application.
    - Actual: "No 'Create Record' form exists. The only creation entry point is the 'Add Transaction' button, whose type selector offers only 'Expense' and 'Income' (no Invoice/Bill/Payment). No records list, route, or menu entry references Invoice."

- [ ] FT-04: User can create a financial record of type "Bill".
  - Action: Open the "Create Record" form, choose "Bill", fill in the required fields, and click "Save".
  - Expected: The bill is created and listed under the records with type "Bill".
  - Bug Report:
    - Issue: Missing feature — no "Create Record" form and no "Bill" record type exist in the application.
    - Actual: "The 'Add Transaction' form only supports type 'Expense' or 'Income'. There is no 'Bill' option and no records section in which a bill could be listed."

- [ ] FT-05: User can create a financial record of type "Payment".
  - Action: Open the "Create Record" form, choose "Payment", fill in the required fields, and click "Save".
  - Expected: The payment is created and listed under the records with type "Payment".
  - Bug Report:
    - Issue: Missing feature — no "Create Record" form and no "Payment" record type exist in the application.
    - Actual: "The 'Add Transaction' form only supports type 'Expense' or 'Income'. There is no 'Payment' option and no records section in which a payment could be listed."

- [X] FT-06: User can create a custom category.
  - Action: Open category management, click "Add Category", enter a name, and click "Save".
  - Expected: The new category is saved and selectable in the transaction/record category list.

- [X] FT-07: User can assign a record to a category or account.
  - Action: Create or edit a record and select a category/account from the dropdown, then save.
  - Expected: The record displays the selected category/account when viewed.

- [X] FT-08: User can view a monthly profit and loss report.
  - Action: Open the "Reports" section and select a month.
  - Expected: The report shows total income, total expense, and computed profit/loss for the selected month.

- [X] FT-09: User can view the financial dashboard.
  - Action: Open the dashboard.
  - Expected: Dashboard displays summary figures for income, expenses, and current financial status.

- [X] FT-10: User can edit an existing entry.
  - Action: Open a saved transaction, change the amount or category, and click "Save".
  - Expected: The transaction list and related totals reflect the updated values.

- [X] FT-11: User can filter records by date.
  - Action: Apply a date range filter in the record/transaction list.
  - Expected: Only records within the selected date range are displayed.

- [X] FT-12: User can filter records by category.
  - Action: Select a specific category in the list filter.
  - Expected: Only records belonging to the selected category are displayed.

- [X] FT-13: User can mark an item as tax-related.
  - Action: Open a transaction/record and enable the "Tax-related" option, then save.
  - Expected: The item is flagged as tax-related and indicated as such in its entry.

- [X] FT-14: User can generate a basic tax summary.
  - Action: Open the "Tax Summary" section and trigger generation.
  - Expected: A summary lists the tax-related items with their totals.

- [X] FT-15: User can print the tax summary.
  - Action: Open the tax summary and click "Print".
  - Expected: The print dialog opens with the tax summary content prepared for printing.

## Constraint

- [X] CS-01: Transaction cannot be saved with an empty amount.
  - Action: Submit the "Add Transaction" form with the amount field left blank.
  - Expected: Save is blocked and an error indicates the amount is required.

- [X] CS-02: Non-numeric amount is rejected.
  - Action: Enter letters/symbols in the amount field and submit.
  - Expected: Save is blocked and an error indicates the amount must be a valid number.

- [ ] CS-03: Duplicate category names are prevented.
  - Action: Create a category with a name that already exists.
  - Expected: Creation is blocked and a message indicates the category already exists.
  - Bug Report:
    - Issue: Duplicate category names are allowed; no uniqueness validation on the category name field.
    - Actual: "A category named 'QA Custom Category' was created; creating a second category with the same name 'QA Custom Category' succeeded, and the category selector now lists 'QA Custom Category' twice. No error/message indicated the category already exists."

## Interaction

- [ ] IX-01: Success feedback appears after a record is created.
  - Action: Successfully save a new transaction or financial record.
  - Expected: A success message/toast confirms the record was saved.
  - Bug Report:
    - Issue: No success message/toast is shown after a record is created.
    - Actual: "After saving a transaction the dialog simply closes and the new row appears; both notification regions — 'Notifications (F8)' and 'Notifications alt+T' — were empty, and a MutationObserver on document.body captured no success message/toast node (only the dialog, the category option list, and the new table row)."

- [X] IX-02: Dashboard and totals update after adding an entry.
  - Action: Add a new transaction and return to the dashboard/report.
  - Expected: The dashboard totals recompute to include the newly added entry.

- [X] IX-03: Deleting a record requires confirmation.
  - Action: Click "Delete" on an existing record.
  - Expected: A confirmation prompt appears before the record is removed.

## Content

- [X] CT-01: Displayed labels and fields match bookkeeping terminology.
  - Action: Inspect forms, lists, and menus across the app.
  - Expected: Labels reference income, expenses, categories, accounts, invoices, bills, payments, and tax—not unrelated web content.
  - Note: Labels are bookkeeping-appropriate (Income, Expenses, Transactions, Categories, Reports, Tax Summary, Tax Related, Reference, Notes). No unrelated web copy is present. Note that invoice/bill/payment terminology is absent because those features do not exist (see FT-03/04/05).

- [X] CT-02: Report and dashboard figures are numerically consistent.
  - Action: Compare a monthly report's income/expense totals against the sum of the underlying listed transactions for that month.
  - Expected: Reported totals equal the sum of the corresponding transactions.
  - Note: The November 2026 report (Income $500.00, Expenses $200.00, Net +$300.00) equals the sum of the listed Nov 2026 transactions ("QA Test Income Beta" +$500.00, "QA Test Expense Alpha" −$200.00).