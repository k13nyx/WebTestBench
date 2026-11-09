# Test Result

## Functionality
- [X] FT-01: User can create an income transaction
  - Action: Open the "Add Transaction" / "New Record" form, select type "Income", enter amount (e.g., 500), date, and description, then submit.
  - Expected: The income transaction is saved and appears in the transaction list with the correct amount, date, and description.
- [X] FT-02: User can create an expense transaction
  - Action: Open the form, select type "Expense", enter amount (e.g., 120), date, and description, then submit.
  - Expected: The expense transaction is saved and appears in the transaction list.
- [ ] FT-03: User can create an invoice record
  - Action: Navigate to the invoices/bills section, click "New Invoice", fill in required fields (e.g., customer name, amount, date), and save.
  - Expected: The invoice is created and listed with its details.
  - Bug Report:
    - Issue: Missing Feature — No invoice section exists
    - Actual: The app has no invoices/bills section (nav contains only Dashboard, Transactions, Categories, Reports, Tax Summary). The Add Transaction form offers only "Income"/"Expense" types, and the type filter offers only "All Types/Income/Expense". Invoices exist only as a free-text "Reference" field (placeholder "Invoice #, Receipt #, etc.") on regular transactions — there is no way to create an invoice record with a customer name, and no "New Invoice" button anywhere.
- [ ] FT-04: User can create a bill or payment record
  - Action: Create a new bill or payment record with valid details and save it.
  - Expected: The record is created and appears in the corresponding records list.
  - Bug Report:
    - Issue: Missing Feature — No bill/payment record type
    - Actual: No bills or payments section or record type exists anywhere in the app. The only record type is the generic transaction (Income/Expense); a "bill" can only be approximated as a plain expense transaction, with no dedicated records list, due dates, or payment status.
- [X] FT-05: User can edit an existing entry
  - Action: Open an existing transaction/invoice, change its amount or description, and save.
  - Expected: The updated value is reflected in the record and in any dependent summaries.
- [X] FT-06: User can delete an entry
  - Action: Delete an existing transaction/record and confirm (if prompted).
  - Expected: The record is removed from the list and no longer counts toward reports.
- [X] FT-07: User can create a custom category/account
  - Action: Go to the categories/accounts section, click "Add Category", enter a name (e.g., "Office Supplies"), and save.
  - Expected: The new category appears in the category list and is selectable when creating records.
- [X] FT-08: User can assign a category to a transaction
  - Action: Create or edit a transaction and choose a category from the category selector, then save.
  - Expected: The transaction displays its assigned category.
- [X] FT-09: Filter records by date range
  - Action: Set a date-range filter (e.g., current month) on the records list.
  - Expected: Only records whose dates fall within the range are displayed.
- [X] FT-10: Filter records by category
  - Action: Select a specific category in the filter control.
  - Expected: Only records assigned to that category are displayed.
- [X] FT-11: Monthly profit and loss report shows correct totals
  - Action: Open the reports view for a month that has known income and expense records.
  - Expected: The report shows total income, total expenses, and net profit/loss equal to the sum of that month's records.
- [X] FT-12: User can mark a record as tax-related
  - Action: Edit or create a record and toggle the "Tax-related" flag, then save.
  - Expected: The record is visibly marked as tax-related (e.g., badge or flag shown in the list).
- [X] FT-13: Tax summary generates correct totals and is printable
  - Action: Open the tax summary view and use the print action (or print preview).
  - Expected: The summary lists tax-related records and their total, and a print dialog/preview can be triggered.

## Constraint
- [X] CS-01: Cannot save a record with empty required fields
  - Action: Submit the new-record form leaving required fields (e.g., amount or date) blank.
  - Expected: The form is not submitted and a validation message is shown.
- [ ] CS-02: Amount must be a valid positive number
  - Action: Enter an invalid amount (e.g., "abc", negative, or 0) and submit.
  - Expected: Submission is blocked with a clear validation error; no record is created.
  - Bug Report:
    - Issue: Incorrect Form Submission — zero (and negative) amounts are accepted
    - Actual: Submitting with amount "0" created a record ("QA Zero Amount — -$0.00") with no validation error. The native input only enforces min="0", so 0 passes. Additionally, a negative amount ("-5") bypassed validation in one submit attempt and was saved as a record displayed with malformed text "--$5.00" (double minus sign) and it distorted the expense totals. Only non-numeric text ("abc") is blocked by the number input, and negative values are blocked only by native browser validation — not by app-level checks.
- [ ] CS-03: Category name must be unique/non-empty
  - Action: Attempt to create a category with an empty name or a name that already exists.
  - Expected: Creation is blocked with a validation message; no duplicate or blank category is added.
  - Bug Report:
    - Issue: Incorrect Form Submission — duplicate category names accepted
    - Actual: Creating a category named "Office Supplies" (which already exists) succeeded without any validation message — the category list then contained two "Office Supplies" entries (13 total). Only the empty-name case is blocked (native "Please fill out this field." message).

## Interaction
- [X] IX-01: Dashboard reflects financial status after adding a record
  - Action: Note the dashboard totals, then add a new income transaction and return to the dashboard.
  - Expected: The dashboard totals (e.g., income, balance, profit) update to include the new record.
- [ ] IX-02: Confirmation feedback after saving or deleting
  - Action: Save a new record, then delete a record.
  - Expected: The app shows clear feedback (e.g., success toast/message) for each action and the list updates without requiring a manual reload.
  - Bug Report:
    - Issue: Missing Feedback — no success toast/message after save or delete
    - Actual: After saving (create and edit) and after deleting a record, no success toast, message, or any notification appears — the notification/live regions remain empty (verified via DOM query 800ms after save and immediately after delete). The list itself does update immediately without a manual reload, but the "clear feedback" requirement is not met for either action.
- [X] IX-03: Filtering controls update the list immediately
  - Action: Change the date or category filter while viewing records.
  - Expected: The visible list refreshes to match the new filter without a full page reload or manual refresh action.

## Content
- [X] CT-01: Dashboard displays meaningful financial figures
  - Action: Open the dashboard.
  - Expected: It shows bookkeeping-specific content (e.g., total income, total expenses, net profit/loss) with correctly formatted currency values that match existing records.
- [X] CT-02: Report and tax summary content is accurate and relevant
  - Action: Compare the monthly P&L report and tax summary against the records in the transaction list.
  - Expected: Record names, categories, amounts, and totals shown in the reports match the actual records; no placeholder or irrelevant content is displayed.
