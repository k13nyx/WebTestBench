# Test Result

## Functionality

- [X] FT-01: Create an income transaction
  - Action: Open the new transaction form, enter a description, amount 500, a date in the current month, select type "Income", and submit.
  - Expected: A row appears in the transaction list with type "Income", amount 500, and the entered date/description; it is included in income totals.

- [X] FT-02: Create an expense transaction
  - Action: Open the new transaction form, enter a description, amount 200, a date in the current month, select type "Expense", and submit.
  - Expected: A row appears in the transaction list with type "Expense" and amount 200; it is included in expense totals.

- [ ] FT-03: Create invoice, bill, and payment records
  - Action: Use the record creation control and create one record of each available type (Invoice, Bill, Payment) with valid default values.
  - Expected: All three are saved, appear in the records list labeled with their type, and each can be opened for viewing/editing.
  - Bug Report:
    - Issue: Missing Feature — no Invoice/Bill/Payment record types exist
    - Actual: The only creation control is "Add Transaction", whose Type dropdown contains exactly two options ("Income|income", "Expense|expense"). There is no records page or record-type selector anywhere: navigating to /invoices, /bills, and /payments each returns the 404 page ("404 Error: User attempted to access non-existent route"). The word "invoice" appears 0 times in the UI text of all five pages; "bill" appears only once, as the description text of a default transaction ("Electric Bill"). None of the three record types could be created.

- [X] FT-04: Create a custom category and assign a transaction to it
  - Action: Open category management, add category "Test Category", then edit a default transaction and set its category to "Test Category".
  - Expected: The new category is saved, appears in the category dropdown/filter list, and the edited transaction row displays "Test Category".

- [ ] FT-05: Create a custom account and assign a transaction to it
  - Action: Open account management, add account "Test Account", then edit a default transaction and assign it to "Test Account".
  - Expected: The new account is saved, appears in the account dropdown/filter list, and the edited transaction row displays "Test Account".
  - Bug Report:
    - Issue: Missing Feature — no account management and no account field on transactions
    - Actual: There is no "Accounts" entry in the sidebar navigation (only Dashboard, Transactions, Categories, Reports, Tax Summary) and no account management control on the Categories page. Navigating to /accounts returns the 404 page. The transaction form contains only Type, Date, Description, Amount, Category, Reference, Notes and Tax Related — no Account selector. The Transactions filter bar offers only All Types and All Categories — no account filter. The string "account" appears just once in the whole app, as static dashboard text "Across all accounts" beneath a Total Balance figure that never changes.

- [X] FT-06: View monthly profit and loss report
  - Action: Open Reports → Profit & Loss and select the current month.
  - Expected: The report shows total income, total expenses, and net profit/loss for that month; net equals income minus expenses and matches that month's records.

- [X] FT-07: Dashboard shows financial status summary
  - Action: Navigate to the dashboard and read the summary values after FT-01 and FT-02.
  - Expected: Dashboard displays total income, total expenses, and net/balance; net equals income minus expenses and reflects the 500 income and 200 expense added.

- [X] FT-08: Filter records by date range
  - Action: Apply the date filter to a narrow range (e.g., one day or one week) that covers only part of the default records.
  - Expected: Only records whose date falls inside the range are listed; visible count is greater than 0 and less than the unfiltered total.

- [X] FT-09: Filter records by category
  - Action: Select one existing default category in the category filter and apply it.
  - Expected: Only records assigned to that category are listed; every visible row shows that category.

- [X] FT-10: Edit an existing entry
  - Action: Edit a default transaction, change its amount to 123.45 and its description, and save.
  - Expected: The row shows the updated amount and description, and dashboard/P&L totals reflect 123.45 instead of the old value.

- [X] FT-11: Delete an existing entry
  - Action: Delete the transaction created in FT-01 and confirm if prompted.
  - Expected: The row is removed from the list and no longer appears in filtered views or dashboard totals.

- [X] FT-12: Mark items as tax-related and generate tax summary
  - Action: Enable the "Tax related" flag on one default income record and one default expense record, then open the Tax Summary report.
  - Expected: The summary lists exactly those marked records, shows separate totals for tax-related income and expenses, and omits unmarked records.

## Constraint

- [X] CS-01: Required fields block saving a transaction
  - Action: Submit the new transaction form with description, amount, and date all left empty.
  - Expected: No record is created (list count unchanged), and inline validation messages are shown on each required field.

- [X] CS-02: Invalid amounts are rejected
  - Action: Enter amount "abc" and submit; then enter "-50" and submit.
  - Expected: Both submissions are rejected with a validation message and no record containing an invalid amount is saved.

- [X] CS-03: Removing the tax-related flag removes the item from the tax summary
  - Action: Turn off the "Tax related" flag on the income record marked in FT-12, then reopen the Tax Summary report.
  - Expected: That record is no longer listed and its amount is excluded from the summary totals.

## Interaction

- [ ] IX-01: Confirmation message after saving a record
  - Action: Create one valid transaction and observe the interface immediately after submitting.
  - Expected: A confirmation message/toast is displayed (e.g., "Transaction saved") without any error state.
  - Bug Report:
    - Issue: Missing Feedback — no confirmation/toast after a successful save
    - Actual: After clicking "Add Income"/"Add Expense" (and after "Update Income"/"Update Expense"), the dialog simply closes and the new row appears with no user feedback. The Radix toast viewport is present in the DOM (`region "Notifications (F8)"` containing an empty `list`, plus a second `region "Notifications alt+T"`), but it stays empty. Polling the page six times over 1.5 s after submission found no element with role status/alert and no occurrence of "saved", "success", "created" or "added" anywhere in `document.body.innerText`.

- [X] IX-02: Dashboard totals update without a page reload
  - Action: Note the dashboard net total, create an expense of 100, then return to the dashboard without reloading the browser.
  - Expected: The displayed totals update and net is 100 lower than before; no stale numbers are shown.

- [X] IX-03: Print the tax summary
  - Action: Open the Tax Summary report and click the Print button.
  - Expected: The browser print preview opens and contains the summary headings and totals in a clean printable layout.

## Content

- [X] CT-01: Labels use correct bookkeeping terminology with no placeholder text
  - Action: Review the main navigation, dashboard, record form labels, and report headings.
  - Expected: All text uses bookkeeping terms (Income, Expense, Category, Account, Profit & Loss, Tax Summary); no "Lorem ipsum", "TODO", "undefined", or empty labels appear.

- [ ] CT-02: Currency values are formatted consistently everywhere
  - Action: Inspect monetary values in the transaction list, dashboard, monthly P&L, and tax summary.
  - Expected: Every amount shows the same currency symbol and two-decimal format, income and expense are clearly distinguished, and no total displays blank or "NaN".
  - Bug Report:
    - Issue: Inconsistent Currency Formatting — two-decimal rule not applied on dashboard and P&L
    - Actual: The transaction list and tax summary format every amount with two decimals and a sign prefix ("-$100.00", "+$123.45", "+$47,673.45", "$0.00"), but the dashboard summary cards and the monthly P&L report truncate the cents: Dashboard renders "Total Balance $74,931", "Monthly Income $0", "Monthly Expenses $300", "Net Profit/Loss -$300"; Reports renders "Total Income $0", "Total Expenses $300", "Net Profit/Loss -$300" and category rows "$300". The same values are therefore displayed both as "$300" and "$300.00" depending on the screen, so the two-decimal format is not applied consistently everywhere (the currency symbol "$" is consistent and no total is blank or "NaN").