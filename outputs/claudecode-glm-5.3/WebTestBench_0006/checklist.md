# Test Checklist

## Functionality
- [ ] FT-01: Add an income transaction
  - Action: Open the transactions/entries section, click "Add Transaction" (or equivalent), select type "Income", enter a description, amount, date, and choose an existing category and account, then save.
  - Expected: The new income transaction appears in the transaction list with the entered description, amount, date, category, and account.

- [ ] FT-02: Add an expense transaction
  - Action: Click "Add Transaction", select type "Expense", enter a description, amount, date, category, and account, then save.
  - Expected: The new expense transaction appears in the transaction list, clearly identified as an expense (e.g., type label or negative amount display).

- [ ] FT-03: Create a financial record (invoice, bill, or payment)
  - Action: Open the records section (e.g., "Invoices / Bills / Payments"), create a new bill record with a party name, amount, and date, and save it.
  - Expected: The new bill record appears in the records list with the entered details and is assignable to a category and/or account.

- [ ] FT-04: Review and edit an existing entry
  - Action: Locate a default transaction in the list, open its edit view, change the amount (and optionally the category), save, then reload the page.
  - Expected: The transaction list shows the updated amount/category after saving and the change persists after page reload.

- [ ] FT-05: Create a custom category and assign a transaction to it
  - Action: In category management, create a new category (e.g., "Consulting"), then edit any default transaction to use this category and save.
  - Expected: The new category is selectable and the transaction's category field displays "Consulting" after saving.

- [ ] FT-06: Create a custom account and assign a transaction to it
  - Action: In account management, create a new account (e.g., "Business Checking"), then edit any default transaction to use this account and save.
  - Expected: The new account is selectable and the transaction's account field displays "Business Checking" after saving.

- [ ] FT-07: Filter transactions by date range
  - Action: On the transactions list, set a date range that covers at least one default transaction (start date ≤ its date ≤ end date) and apply the filter.
  - Expected: Only transactions dated within the selected range are displayed; transactions outside the range are hidden.

- [ ] FT-08: Filter transactions by category
  - Action: On the transactions list, apply a category filter for one category that has at least one default transaction.
  - Expected: Only transactions belonging to the selected category are displayed.

- [ ] FT-09: View monthly profit and loss summary
  - Action: Open the reports section and view the monthly profit & loss report for a month that contains default transactions.
  - Expected: The report displays total income, total expenses, and net profit/loss for the selected month.

- [ ] FT-10: Mark an item as tax-related and generate a printable tax summary
  - Action: Mark one default transaction as tax-related (e.g., check a "Tax-related" flag), open the tax summary, and click the print button/control.
  - Expected: The tax summary opens a printable view (browser print preview) showing tax-related entries and their total.

## Constraint
- [ ] CS-01: Transaction cannot be saved with empty required fields
  - Action: Open the add-transaction form, leave required fields (e.g., amount or date) empty, and attempt to save.
  - Expected: The transaction is not saved, no new list entry appears, and a validation message indicates the missing required field(s).

- [ ] CS-02: Transaction amount rejects non-numeric input
  - Action: Open the add-transaction form, fill all required fields, but enter non-numeric text (e.g., "abc") in the amount field, and attempt to save.
  - Expected: The transaction is not saved and a validation message (or blocked input) indicates the amount must be a valid number.

- [ ] CS-03: Invalid date range yields empty results without errors
  - Action: Apply a date filter where the start date is later than the end date.
  - Expected: The list shows no transactions (empty state) and the page does not crash or display a system error.

## Interaction
- [ ] IX-01: Confirmation shown after saving a transaction
  - Action: Save a valid new transaction (see FT-01).
  - Expected: A visible success confirmation (toast or message such as "Transaction saved") appears, or the form visibly closes and the list visibly updates — success is not silent.

- [ ] IX-02: Edit form opens pre-populated with the entry's current values
  - Action: Click the edit control on any default transaction in the list.
  - Expected: The edit form opens immediately, pre-filled with that transaction's existing description, amount, date, category, and account values.

- [ ] IX-03: Dashboard figures update after adding a transaction
  - Action: Note the dashboard's income/expense/balance totals, add a new expense transaction (see FT-02), then view the dashboard again without reloading.
  - Expected: The dashboard totals update to reflect the new transaction (e.g., total expenses increase by the entered amount).

## Content
- [ ] CT-01: Dashboard figures accurately summarize stored transactions
  - Action: Compare the dashboard's total income and total expense figures against the transaction list for the same period.
  - Expected: Dashboard totals equal the mathematical sum of the matching income and expense transactions shown in the list.

- [ ] CT-02: Monthly P&L figures are internally consistent
  - Action: For one month, verify the P&L report's total income, total expenses, and net profit against that month's transactions (via date filter, FT-07).
  - Expected: Net profit equals total income minus total expenses, and both totals match the month's filtered transactions.

- [ ] CT-03: Tax summary contains only tax-related items
  - Action: Mark one default transaction as tax-related (see FT-10), open the tax summary, and inspect its contents and total.
  - Expected: The summary lists only entries flagged tax-related, each with a correct amount, and the summary total equals the sum of those listed amounts.