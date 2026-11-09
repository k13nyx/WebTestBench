# Test Checklist

## Functionality
- [ ] FT-01: User can record an income transaction
  - Action: Open the transactions view, click "Add Transaction", select type "Income", enter a description, amount, date, and a category, then save.
  - Expected: The new income entry appears in the transaction list with type "Income" and the entered details.

- [ ] FT-02: User can record an expense transaction
  - Action: Click "Add Transaction", select type "Expense", enter description, amount, date, and category, then save.
  - Expected: The new expense entry appears in the transaction list with type "Expense".

- [ ] FT-03: User can create financial records of each supported type
  - Action: Using the records module, create one Invoice, one Bill, and one Payment, each with an amount and category/account assignment, and save.
  - Expected: All three records appear in the records list, each labeled with its correct type.

- [ ] FT-04: User can edit an existing entry
  - Action: Open an existing transaction, change its amount and category, and save.
  - Expected: The entry re-displays with the updated amount and category.

- [ ] FT-05: User can delete an existing entry
  - Action: Delete a transaction from the list, confirming if prompted.
  - Expected: The entry no longer appears in the list, and dashboard/report totals recompute without it.

- [ ] FT-06: User can create a custom category and assign it
  - Action: In the categories/accounts settings, add a new category (e.g., "Freelance"), then assign it to a transaction via the category dropdown.
  - Expected: The new category is listed in settings and selectable in the transaction form; the transaction saves with it.

- [ ] FT-07: User can filter records by date range
  - Action: Apply a start and end date filter to the transactions/records list.
  - Expected: Only entries dated within the selected range are displayed.

- [ ] FT-08: User can filter records by category
  - Action: Select a category in the filter control.
  - Expected: Only entries assigned to that category are displayed.

- [ ] FT-09: User can view a monthly profit and loss report
  - Action: Open the Reports section and select the current/default month.
  - Expected: The report displays total income, total expenses, and net profit/loss for that month.

- [ ] FT-10: User can generate a tax summary
  - Action: Open the tax summary tool and generate/view the summary.
  - Expected: A tax summary page/section is displayed with tax figures available for review.

## Constraint
- [ ] CS-01: Invalid amounts are rejected
  - Action: Attempt to save a transaction with amount "0", a negative value, and non-numeric text.
  - Expected: Save is blocked and a validation error message is shown for each invalid amount.

- [ ] CS-02: Required fields must be provided
  - Action: Attempt to save a transaction with the description, amount, or category left empty.
  - Expected: The record is not created and the missing required fields are flagged.

- [ ] CS-03: In-use categories are protected
  - Action: Attempt to delete a category that is assigned to at least one existing transaction.
  - Expected: Deletion is blocked or reassignment is required; no transaction is left without a category.

- [ ] CS-04: Profit and loss calculation is consistent
  - Action: For a given month, sum income entries and expense entries from the transaction list, then compare against the P&L report figures.
  - Expected: Report net = (total income − total expenses) exactly matches the manually summed values.

## Interaction
- [ ] IX-01: Save actions give immediate feedback
  - Action: Create a transaction and save it.
  - Expected: A success message/toast or confirmation is displayed, and the form/list reflects the new entry without a manual page reload.

- [ ] IX-02: Tax-related flag can be toggled and persists
  - Action: Open an entry and toggle its "Tax-related" checkbox/indicator off and on, then save and reopen the entry.
  - Expected: The toggle state persists and the entry shows a visible tax indicator in the list.

- [ ] IX-03: Tax summary can be printed
  - Action: From the tax summary view, trigger the Print action.
  - Expected: A print dialog or print-friendly view of the tax summary opens containing the summary content.

## Content
- [ ] CT-01: Default data is present on first load
  - Action: Open the application's dashboard/transactions view.
  - Expected: Pre-existing sample transactions, records, and categories are displayed; the dashboard is not empty.

- [ ] CT-02: Tax summary content is accurate
  - Action: Compare the tax summary against entries marked "Tax-related".
  - Expected: The summary lists only tax-marked entries, and its totals equal the sum of those entries.

- [ ] CT-03: Content is bookkeeping-appropriate and well-formatted
  - Action: Review dashboard, reports, and forms for labels, headings, and amounts.
  - Expected: All text is relevant to bookkeeping (no placeholder/lorem text), and monetary values display with currency formatting.