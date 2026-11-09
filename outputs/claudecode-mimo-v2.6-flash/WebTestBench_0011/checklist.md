# Test Checklist

## Functionality
- [ ] FT-01: Record a one-off income transaction
  - Action: Create a new one-off income entry with amount, date, and description; save it.
  - Expected: The transaction appears in the transaction list with the entered details and type "Income".

- [ ] FT-02: Record a one-off expense transaction
  - Action: Create a new one-off expense entry with amount, date, and description; save it.
  - Expected: The transaction appears in the transaction list with type "Expense" and the entered details.

- [ ] FT-03: Record a recurring transaction
  - Action: Create a transaction marked as recurring (e.g., monthly rent) with a repeat frequency; save it.
  - Expected: The transaction is saved as recurring and its recurrence frequency is displayed on the entry.

- [ ] FT-04: Assign category, project, and payment method to a transaction
  - Action: While creating a transaction, select a category, a project, and a payment method; save it.
  - Expected: The saved transaction displays the selected category, project, and payment method.

- [ ] FT-05: Set transaction status to paid, pending, or expected
  - Action: Create three transactions setting their status respectively to Paid, Pending, and Expected.
  - Expected: Each transaction shows its assigned status label in the transaction list.

- [ ] FT-06: Filter transactions by status
  - Action: Apply a filter for status "Pending" in the transaction list.
  - Expected: Only transactions with status "Pending" are shown; other statuses are hidden.

- [ ] FT-07: Filter transactions by category
  - Action: Apply a filter for a specific category (e.g., default "Rent" or similar existing category).
  - Expected: Only transactions belonging to that category are shown.

- [ ] FT-08: Sort transactions by date
  - Action: Click the date column header (or date sort control) to sort.
  - Expected: Transactions reorder by date in the indicated ascending/descending order.

- [ ] FT-09: Sort transactions by amount
  - Action: Click the amount column header (or amount sort control) to sort.
  - Expected: Transactions reorder by amount ascending/descending as indicated.

- [ ] FT-10: View historical cash flow chart
  - Action: Navigate to the historical cash flow chart section using default data.
  - Expected: A chart renders showing income and expense trends over past periods.

- [ ] FT-11: View cash balance forecast
  - Action: Open the forecast view.
  - Expected: A forecast of future cash balances is displayed, computed from upcoming expected payments and recurring items.

- [ ] FT-12: Create a custom view
  - Action: Create a new custom view named "Marketing" filtered to the Marketing-related transactions (using existing default data).
  - Expected: The new view is saved and appears in the list of available views.

- [ ] FT-13: Switch between custom views
  - Action: Switch from the default view to the "Marketing" custom view, then to another view (e.g., "Operations").
  - Expected: Each switch updates the displayed transactions and summary to match that view's configuration.

- [ ] FT-14: Custom view shows tailored summary
  - Action: Open a custom view scoped to a specific business area.
  - Expected: The summary figures (totals/balances) reflect only the transactions belonging to that view.

## Constraint
- [ ] CS-01: Cannot create a transaction with an empty amount
  - Action: Attempt to save a new transaction with the amount field left empty.
  - Expected: The save is blocked and a validation message is shown for the required amount field.

- [ ] CS-02: Cannot create a transaction without selecting income or expense type
  - Action: Attempt to save a transaction without choosing between income and expense.
  - Expected: The save is blocked with a validation error indicating the type is required.

- [ ] CS-03: Amount must be a positive number
  - Action: Enter a negative or non-numeric amount and attempt to save.
  - Expected: The save is blocked with a validation message stating the amount must be a positive number.

- [ ] CS-04: Recurring transaction requires a repeat frequency
  - Action: Mark a transaction as recurring but leave the frequency unset; attempt to save.
  - Expected: The save is blocked with a validation message requiring a recurrence frequency.

## Interaction
- [ ] IX-01: Success confirmation after saving a transaction
  - Action: Save a valid new transaction.
  - Expected: A success message (toast/confirmation) appears and the new transaction is immediately visible in the list.

- [ ] IX-02: Forecast chart updates after status change
  - Action: Change a transaction's status from "Expected" to "Paid" (or vice versa) and view the forecast.
  - Expected: The forecast display reflects the updated status without requiring a page reload.

- [ ] IX-03: Filter chips/controls reflect active filters and can be cleared
  - Action: Apply a status filter, then clear it.
  - Expected: The active filter is visibly indicated while applied, and clearing it restores the full transaction list.

## Content
- [ ] CT-01: Transaction list displays accurate amounts and labels
  - Action: Review default transactions in the list, comparing amounts, category names, and status labels.
  - Expected: Every row shows correctly formatted currency amounts, valid category/project names, and status labels matching Paid/Pending/Expected.

- [ ] CT-02: Charts and forecast display consistent totals with the transaction list
  - Action: Compare the income/expense totals shown in charts and summaries against the filtered transaction list for the same period.
  - Expected: The chart and forecast figures are consistent with the sum of transactions shown in the list for that period.