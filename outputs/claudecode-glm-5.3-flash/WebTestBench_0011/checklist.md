# Test Checklist

## Functionality
- [ ] FT-01: Add a one-off income transaction
  - Action: Open the "Add Transaction" form, select type "Income", frequency "One-off", enter a valid amount (e.g., 1000), assign a category, project, and payment method, save.
  - Expected: The transaction is saved and appears in the transaction list with the correct amount, type, and assignments.
- [ ] FT-02: Add a one-off expense transaction
  - Action: Add an expense with frequency "One-off", amount (e.g., 250), category, project, and payment method, save.
  - Expected: The transaction appears in the list marked as an expense with the entered details.
- [ ] FT-03: Add a recurring transaction
  - Action: Add a transaction with frequency "Recurring" (e.g., monthly) and save.
  - Expected: The transaction is saved with its recurrence visible (e.g., "Monthly") in the transaction list.
- [ ] FT-04: Edit an existing transaction
  - Action: Open an existing transaction from the list, change its amount or category, save.
  - Expected: The list and any summary figures reflect the updated values.
- [ ] FT-05: Delete a transaction
  - Action: Delete a transaction from the list and confirm (if prompted).
  - Expected: The transaction no longer appears in the list.
- [ ] FT-06: Mark a transaction status
  - Action: Change a transaction's status to "Paid" (and verify another shows "Pending" / "Expected").
  - Expected: The status is updated and displayed in the list (e.g., a "Paid" badge).
- [ ] FT-07: View historical cash flow chart
  - Action: Open the historical cash flow chart section of the dashboard.
  - Expected: A chart renders showing past income and expenses/balance over time, consistent with the recorded transactions.
- [ ] FT-08: View cash balance forecast
  - Action: Open the forecast view.
  - Expected: A future balance projection is displayed that accounts for upcoming "Expected" payments and recurring items.
- [ ] FT-09: Create a custom view for a business area
  - Action: Create a new custom view named "Marketing" (or similar), optionally tied to specific categories/projects, and save it.
  - Expected: The view is saved and selectable from the views switcher.
- [ ] FT-10: Switch to a custom view and see its tailored summary
  - Action: Switch to the saved custom view.
  - Expected: The dashboard shows summaries/charts filtered to that view's scope (e.g., only marketing-related transactions).

## Constraint
- [ ] CS-01: Amount field rejects invalid input
  - Action: In the transaction form, enter a negative value, zero, or non-numeric text in the amount field and attempt to save.
  - Expected: Submission is blocked with a clear validation message; no invalid transaction is created.
- [ ] CS-02: Required fields must be filled
  - Action: Submit the transaction form with empty required fields (e.g., amount or type).
  - Expected: The form is not saved and highlights the missing required field(s).
- [ ] CS-03: Filters combine without showing out-of-scope data
  - Action: Apply two filters together (e.g., status "Expected" and a specific category).
  - Expected: Only transactions matching ALL active filters are listed; no unrelated transactions appear.

## Interaction
- [ ] IX-01: Filter updates the transaction list immediately
  - Action: Select a filter option (e.g., status "Pending").
  - Expected: The transaction list updates immediately to show only matching transactions without requiring a page reload.
- [ ] IX-02: Sort toggles the transaction ordering
  - Action: Click a column header (e.g., "Amount" or "Date") to sort; click again to reverse.
  - Expected: The list re-orders accordingly and the sort direction is indicated (e.g., arrow icon).
- [ ] IX-03: Saving a transaction gives visible feedback
  - Action: Save a new transaction.
  - Expected: A success confirmation (e.g., toast or highlighted row) appears, and the new transaction is visible in the list.
- [ ] IX-04: Chart details are inspectable
  - Action: Hover over a point/bar in the cash flow chart.
  - Expected: A tooltip or label shows the exact value and period for that data point.

## Content
- [ ] CT-01: Dashboard summary figures are accurate
  - Action: Compare the dashboard totals (e.g., total income, total expenses, current balance) with the transactions in the list.
  - Expected: Displayed figures match the sums of the underlying transactions.
- [ ] CT-02: Transaction rows show all assigned attributes
  - Action: Inspect transactions in the list.
  - Expected: Each row displays its amount, type (income/expense), status, and assigned category, project, and payment method.
- [ ] CT-03: Charts have labeled axes and legends
  - Action: Inspect the cash flow and forecast charts.
  - Expected: Axes, time periods, and series (income vs. expense) are labeled or have a legend, and values are readable and correctly formatted as currency.