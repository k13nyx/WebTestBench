# Test Checklist

## Functionality
- [ ] FT-01: Record a one-off income transaction with full assignment
  - Action: Open "Add Transaction", set type = Income, enter amount, select a Category, a Project, a Payment Method, and set Status = Paid, then save.
  - Expected: The income transaction appears in the transaction list with the chosen category, project, payment method, and status.

- [ ] FT-02: Record a one-off expense transaction
  - Action: Open "Add Transaction", set type = Expense, enter amount, assign category/project/payment method, set status, then save.
  - Expected: The expense transaction is saved and shown in the list as an expense.

- [ ] FT-03: Record a recurring income or expense
  - Action: Open "Add Transaction", enable the recurring option, choose a recurrence schedule (e.g., monthly), set type and details, then save.
  - Expected: The transaction is saved and appears as recurring (e.g., marked "Recurring" and generating repeat entries per schedule).

- [ ] FT-04: Mark a transaction as paid, pending, or expected
  - Action: Edit an existing transaction and set its Status to each of Paid, Pending, and Expected in turn.
  - Expected: The status field reflects the selected value (Paid / Pending / Expected) after each change.

- [ ] FT-05: Filter transactions
  - Action: Apply a filter (e.g., by Category = "Utilities" or Status = "Pending") using the filter controls.
  - Expected: Only transactions matching the filter criteria are displayed in the list.

- [ ] FT-06: Sort transactions
  - Action: Click a sortable column header (e.g., Date or Amount) to toggle ascending/descending order.
  - Expected: The transaction list reorders according to the selected column and direction.

- [ ] FT-07: View historical cash flow chart
  - Action: Open the dashboard's historical cash flow chart view.
  - Expected: A chart showing past income and expenses over time is displayed with data present.

- [ ] FT-08: View future cash balance forecast
  - Action: Open the forecast view.
  - Expected: A projected future cash balance is shown based on upcoming expected/pending payments and recurring items.

- [ ] FT-09: Create a custom view for a business area
  - Action: Use "Create Custom View", name it (e.g., "Marketing"), and configure its scope/filters.
  - Expected: A new custom view named "Marketing" is created and listed among available views.

- [ ] FT-10: Switch between custom views
  - Action: Click between the default view and a created custom view (e.g., "Marketing" ↔ "Operations").
  - Expected: The dashboard content switches to reflect the selected view's scope.

- [ ] FT-11: View tailored summary in a custom view
  - Action: Open a custom view (e.g., "Marketing").
  - Expected: The summary and transaction list show only data relevant to that business area (e.g., marketing-related items).

## Constraint
- [ ] CS-01: Cannot save a transaction missing required fields
  - Action: Attempt to save an "Add Transaction" form with a missing required field (e.g., empty Amount or no Category/Status).
  - Expected: Save is blocked and a validation message indicates the missing required field(s).

- [ ] CS-02: Custom view excludes out-of-scope transactions
  - Action: Create a view scoped to one area (e.g., "Operations") and inspect its transaction list.
  - Expected: Transactions assigned to other areas (e.g., "Marketing") do not appear in the scoped view.

- [ ] CS-03: Forecast uses only expected/pending and recurring items
  - Action: Review the forecast after marking a transaction as Paid vs Expected.
  - Expected: Paid historical transactions are excluded from the future projection, while expected/pending and recurring items are included.

## Interaction
- [ ] IX-01: Confirmation after recording a transaction
  - Action: Save a new transaction successfully.
  - Expected: A success confirmation (toast/banner) appears indicating the transaction was recorded.

- [ ] IX-02: Charts and forecast refresh after a new transaction
  - Action: Add a new transaction, then return to the charts/forecast view.
  - Expected: The cash flow chart and forecast update to include the newly added transaction's effect.

## Content
- [ ] CT-01: Cash flow charts are correctly labeled
  - Action: Inspect the historical cash flow chart axes and legend.
  - Expected: The time axis shows dates, the value axis shows currency amounts, and the legend clearly distinguishes income from expenses.

- [ ] CT-02: Default categories, projects, and payment methods are relevant
  - Action: Open the Category, Project, and Payment Method selectors.
  - Expected: The available default options are relevant to a small business (e.g., categories like Rent/Utilities, projects like client or department names, methods like Bank/Cash/Card).