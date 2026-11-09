# Test Checklist

## Functionality
- [ ] FT-01: Record a one-off income or expense transaction
  - Action: Click "Add Transaction", enter an amount, select type "Income", choose recurrence "One-off", assign Category "Sales", Project "Website Redesign", Payment Method "Bank Transfer", set Status to "Paid", and click "Save".
  - Expected: The transaction is saved and appears in the transactions list with all assigned attributes.
- [ ] FT-02: Record a recurring expense transaction
  - Action: Click "Add Transaction", enter an amount, select type "Expense", choose recurrence "Recurring" (Monthly), assign Category "Software", Payment Method "Credit Card", set Status to "Expected", and click "Save".
  - Expected: The transaction is registered as a recurring item and scheduled into the future cash flow schedule.
- [ ] FT-03: Filter transactions by status, category, and project
  - Action: In the filter panel, select Status "Pending", Category "Operations", and Project "Internal".
  - Expected: The transaction table displays only transactions that match all three selected filter criteria.
- [ ] FT-04: Sort transactions by date and amount
  - Action: Click the "Amount" column header once, then click it a second time.
  - Expected: First click sorts transactions in ascending order of amount; second click sorts transactions in descending order.
- [ ] FT-05: Create and save a custom view for a business area
  - Action: Apply filters for Project "Marketing", click "Save View", enter the name "Marketing Overview", and click "Confirm".
  - Expected: The view is saved and listed under the custom views menu.
- [ ] FT-06: Switch between custom views to update summaries
  - Action: Select "Marketing Overview" from the custom views dropdown, then switch to "Operations".
  - Expected: The dashboard summary metrics and transaction list update immediately to reflect only the selected view's scope.
- [ ] FT-07: View future cash balance forecast
  - Action: Navigate to the "Forecast" tab and select a projection period of "Next 30 Days".
  - Expected: The forecast displays projected cash balances calculated from scheduled recurring transactions and pending/expected payments.

## Constraint
- [ ] CS-01: Prevent saving a transaction with empty required fields
  - Action: Click "Add Transaction", leave the "Amount" and "Category" fields blank, and click "Save".
  - Expected: The form is not submitted, and validation error messages appear under "Amount" and "Category".
- [ ] CS-02: Restrict transaction amount to positive numeric values
  - Action: Enter "-150" into the "Amount" field of the transaction form and click "Save".
  - Expected: The input is rejected with an error message stating "Amount must be greater than zero".
- [ ] CS-03: Prevent saving duplicate custom view names
  - Action: Click "Save View", enter an already existing view name (e.g., "Marketing Overview"), and click "Confirm".
  - Expected: The view is not saved, and an error message "A view with this name already exists" is displayed.

## Interaction
- [ ] IX-01: Display success toast notification upon transaction creation
  - Action: Fill out all required fields in the "Add Transaction" modal and click "Save".
  - Expected: The modal closes and a temporary success toast notification stating "Transaction recorded successfully" appears.
- [ ] IX-02: Display tooltip details on historical cash flow chart hover
  - Action: Hover the cursor over any data point on the historical cash flow chart.
  - Expected: A tooltip appears showing the date, total inflow, total outflow, and net balance for that period.
- [ ] IX-03: Quick status change directly from transaction table
  - Action: Click the status badge of a transaction marked "Pending" and select "Paid" from the inline dropdown.
  - Expected: The badge updates to "Paid" with corresponding style/color change without requiring a full page refresh.
- [ ] IX-04: Prompt confirmation when deleting a custom view
  - Action: Click the "Delete" icon next to a saved custom view.
  - Expected: A confirmation dialog opens asking "Are you sure you want to delete this view?" before deletion occurs.

## Content
- [ ] CT-01: Dashboard summary KPI cards display accurate totals
  - Action: Review the top dashboard cards (Current Balance, Total Income, Total Expenses, Net Cash Flow).
  - Expected: Each card displays formatted currency values that match the calculated sums of the currently visible transactions.
- [ ] CT-02: Historical cash flow chart displays distinct income and expense series
  - Action: View the historical cash flow chart area.
  - Expected: The chart displays clearly labeled axes, time intervals (e.g., Month/Week), and distinct visual indicators/colors for Income vs. Expense series.
- [ ] CT-03: Forecast chart visually distinguishes projected data from actual data
  - Action: Inspect the forecast visualization timeline.
  - Expected: Projected balances and upcoming expected items are visually differentiated (e.g., dashed lines or "Projected" label) from settled historical data.