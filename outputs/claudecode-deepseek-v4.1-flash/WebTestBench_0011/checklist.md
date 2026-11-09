# Test Checklist

## Functionality
- [ ] FT-01: Record a one-off income transaction
  - Action: Click "Add Transaction", select type "Income", enter amount, date, category, project, payment method, status, and save.
  - Expected: The one-off income appears in the transaction list with the entered values.

- [ ] FT-02: Record a one-off expense transaction
  - Action: Click "Add Transaction", select type "Expense", enter amount, date, category, project, payment method, status, and save.
  - Expected: The one-off expense appears in the transaction list with the entered values.

- [ ] FT-03: Record a recurring income/expense
  - Action: Create a transaction and set recurrence (e.g., monthly) with a start date.
  - Expected: The transaction is saved as recurring and its schedule is shown (e.g., "Monthly").

- [ ] FT-04: Assign category, project, and payment method to a transaction
  - Action: In the transaction form, select values for Category, Project, and Payment Method from the available options.
  - Expected: The three attributes are saved and displayed on the transaction record.

- [ ] FT-05: Mark transaction status as paid, pending, or expected
  - Action: Set the status field to each of "Paid", "Pending", and "Expected" and save.
  - Expected: The selected status is stored and visibly shown for that transaction.

- [ ] FT-06: Filter transactions
  - Action: Apply a filter (e.g., by category, project, status, or date range).
  - Expected: Only transactions matching the filter criteria are listed.

- [ ] FT-07: Sort transactions
  - Action: Apply a sort (e.g., by date or amount, ascending/descending).
  - Expected: The transaction list reorders accordingly.

- [ ] FT-08: View historical cash flow chart
  - Action: Open the historical cash flow chart.
  - Expected: A chart renders showing past income/expense (or net balance) over time.

- [ ] FT-09: View cash balance forecast
  - Action: Open the forecast view.
  - Expected: A projection of future cash balances is shown, derived from expected payments and recurring items.

- [ ] FT-10: Create a custom view for a business area
  - Action: Create a custom view (e.g., "Marketing") with defined filters/scope.
  - Expected: The new view is saved and listed among the available views.

- [ ] FT-11: Switch between custom views with tailored summaries
  - Action: Select a saved custom view (e.g., "Marketing", "Operations").
  - Expected: The summary updates to reflect only that view's data.

## Constraint
- [ ] CS-01: Cannot save a transaction with missing required fields
  - Action: Attempt to save a transaction leaving amount or date empty.
  - Expected: Save is blocked and an error indicates the required field(s).

- [ ] CS-02: Recurring transaction requires an interval and start date
  - Action: Set a transaction to recurring without specifying recurrence frequency or start date.
  - Expected: Save is blocked with a message requiring the recurrence details.

- [ ] CS-03: Forecast only includes expected and recurring items
  - Action: Compare forecast figures against pending/paid transactions that are not expected/recurring.
  - Expected: Paid/pending one-off items do not alter the future forecast projection.

## Interaction
- [ ] IX-01: Confirmation feedback after saving a transaction
  - Action: Save a valid transaction.
  - Expected: A success confirmation (e.g., toast/message) appears.

- [ ] IX-02: Chart and summary update when filters/views change
  - Action: Change the active filter or switch to another custom view.
  - Expected: The chart and summary reflect the new selection without requiring a page reload.

## Content
- [ ] CT-01: Chart data matches recorded transactions
  - Action: Compare the historical chart values against the transactions in the list for the same period.
  - Expected: Displayed chart figures correspond accurately to the underlying recorded data.

- [ ] CT-02: Custom view summary reflects only its defined scope
  - Action: Open a custom view scoped to a specific project/client.
  - Expected: The summary contains only transactions belonging to that scope; unrelated data is excluded.