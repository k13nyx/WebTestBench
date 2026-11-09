# Test Checklist

## Functionality
- [ ] FT-01: Record a one-off income transaction
  - Action: Click "Add Transaction", select type "Income", enter description "Website redesign invoice", amount (e.g., 1500), today's date, a category, a project, a payment method, and status "Paid"; save.
  - Expected: New transaction appears in the transaction list showing the entered amount, date, category, project, payment method, and status.

- [ ] FT-02: Record a one-off expense transaction
  - Action: Click "Add Transaction", select type "Expense", fill in amount, date, category, project, payment method, status "Pending"; save.
  - Expected: Expense appears in the list with the entered values and is reflected in the dashboard expense totals.

- [ ] FT-03: Record a recurring item
  - Action: Click "Add Transaction", enable "Recurring", set frequency (e.g., monthly), fill amount/category/payment method; save.
  - Expected: Item is saved with a recurrence indicator and generates/preview future occurrences per the schedule.

- [ ] FT-04: Change a transaction's status
  - Action: Open an existing "Expected" transaction from the list, change status to "Paid", save.
  - Expected: Status shows "Paid" in the list, and the dashboard totals/counts update to include it as paid.

- [ ] FT-05: Filter transactions
  - Action: Apply a category filter (e.g., "Rent") and a status filter (e.g., "Pending") on the transaction list.
  - Expected: Only transactions matching both filters are shown; clearing filters restores the full list.

- [ ] FT-06: Sort transactions
  - Action: Click the amount column header (or sort control) to sort ascending, then descending.
  - Expected: List reorders correctly by amount in both directions; toggling by date also orders chronologically.

- [ ] FT-07: View historical cash flow chart
  - Action: Navigate to the cash flow chart/section and select a historical period (e.g., last 6 months).
  - Expected: Chart renders income vs. expenses over past periods, consistent with the recorded/default transactions.

- [ ] FT-08: View future cash balance forecast
  - Action: Open the forecast view (e.g., "Forecast" tab).
  - Expected: A projected future balance is shown for upcoming periods, calculated from expected/pending payments and recurring items.

- [ ] FT-09: Create a custom view
  - Action: Use "Create View" (or equivalent), name it "Marketing", set filters to the marketing category/project, save.
  - Expected: "Marketing" appears in the view list and opening it shows only marketing transactions with a matching summary.

- [ ] FT-10: Switch between custom views
  - Action: Switch from "Marketing" to another saved view (e.g., "Operations"), then back.
  - Expected: Each switch shows that view's own filtered transactions and tailored summary (income, expenses, balance) with no carry-over of the previous view's data.

## Constraint
- [ ] CS-01: Required fields enforced on transaction form
  - Action: Open "Add Transaction", leave amount and description empty, click Save.
  - Expected: Form is rejected with a validation message; no transaction is added to the list.

- [ ] CS-02: Invalid amount rejected
  - Action: Enter a non-numeric or negative amount (e.g., "abc" or -50) in the amount field and save.
  - Expected: Save is blocked with an error; no transaction is created.

- [ ] CS-03: Duplicate custom view name rejected
  - Action: Attempt to create a new custom view named identically to an existing one (e.g., "Marketing").
  - Expected: Creation is blocked with an error message; no duplicate view is added.

- [ ] CS-04: Summary totals match underlying transactions
  - Action: Compare the dashboard's income, expense, and balance figures against the sum of the visible/default transaction list.
  - Expected: Summary totals equal the sum of the listed transactions (no mismatch or missing entries).

## Interaction
- [ ] IX-01: Confirmation on saving a transaction
  - Action: Save a valid transaction.
  - Expected: A success toast/message appears (e.g., "Transaction saved") and the form closes or resets.

- [ ] IX-02: Filter updates list immediately
  - Action: Apply a filter on the transactions list.
  - Expected: The list updates instantly without a full page reload; filter control shows the active selection.

- [ ] IX-03: Chart tooltip on hover
  - Action: Hover over a point/bar in the historical cash flow chart.
  - Expected: Tooltip shows the period's income, expense, and/or net value for that point.

- [ ] IX-04: View switching updates summary instantly
  - Action: Click between two saved views using the view switcher.
  - Expected: Summary numbers and chart refresh immediately to reflect the selected view.

## Content
- [ ] CT-01: Transaction list shows all key attributes
  - Action: Inspect the default transactions list.
  - Expected: Each row displays date, description, category, project, payment method, amount, status, and a paid/pending/expected indicator that matches its data.

- [ ] CT-02: Default data is relevant to small-business finance
  - Action: Review default categories, payment methods, and sample transactions.
  - Expected: Content is business-cash-flow themed (e.g., categories like Rent, Software, Client Payments; methods like Bank Transfer, Credit Card) with no unrelated placeholder data.

- [ ] CT-03: Chart labels and legends are clear and relevant
  - Action: Inspect the historical chart and forecast chart labels, axes, and legends.
  - Expected: Income and expense series are clearly labeled and distinguished; forecast chart shows future periods labeled with upcoming dates.