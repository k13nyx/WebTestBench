# Test Checklist

## Functionality
- [ ] FT-01: One-off income transaction can be recorded with full attribution
  - Action: Click "Add Transaction"; enter description "Client invoice #101", amount 2500, type Income, date, category "Sales", project "Client A", payment method "Bank Transfer", status "Paid"; save.
  - Expected: Transaction is saved and appears in the transactions list showing all entered values (description, amount, category, project, payment method, status = Paid, type = Income).

- [ ] FT-02: Recurring expense can be recorded with a repeat interval
  - Action: Add a transaction of type Expense, description "Software subscription", amount 99, category "Operations", payment method "Credit Card", and set it as recurring with a monthly interval and a next due date; save.
  - Expected: Transaction is saved, visibly flagged as recurring (e.g., "Monthly" badge), and its upcoming instance appears in the upcoming/recurring list.

- [ ] FT-03: Transaction status can be changed between Paid, Pending, and Expected
  - Action: Open an existing "Pending" transaction and change its status to "Paid" (via edit or an inline status control); save.
  - Expected: The list row now shows status "Paid", and summary totals/status filters reflect the new status.

- [ ] FT-04: Filtering narrows the transaction list to matching records
  - Action: Apply filters: status = "Paid" and category = "Operations"; then change to payment method = "Credit Card".
  - Expected: Only transactions matching all active filters are shown; non-matching rows disappear; clearing filters restores the full list.

- [ ] FT-05: Sorting orders transactions by the chosen column
  - Action: Click the column header "Amount" to sort ascending, then descending; repeat with "Date".
  - Expected: Rows reorder correctly (e.g., ascending amount = smallest → largest; descending = largest → smallest), including after numeric comparison of currency values.

- [ ] FT-06: Historical cash flow chart renders from recorded transactions
  - Action: Open the dashboard chart section; ensure the historical view (e.g., monthly Income vs. Expense bars/lines over past periods) is displayed.
  - Expected: A chart is rendered with income and expense series per time period; the period totals for default data match the sum of that period's transactions.

- [ ] FT-07: Forecast projects future balances from Expected payments and recurring items
  - Action: Open the forecast section; compare the projected balance for the next period against: current balance + sum of Expected income − (sum of Expected expenses + due recurring expenses).
  - Expected: A forecast (chart or table) shows future periods with balances, and the math includes upcoming Expected transactions and recurring items; totals match manual calculation within rounding.

- [ ] FT-08: Custom view can be created scoped to a business area
  - Action: Click "Create View" (or equivalent); name it "Marketing", scope it to category "Marketing" (e.g., via its filters), and save.
  - Expected: "Marketing" appears in the view selector/tab bar and can be selected.

- [ ] FT-09: Switching views applies tailored filters and summaries
  - Action: Select the "Marketing" view, then switch back to the "All Transactions"/default view.
  - Expected: The transaction list, summary totals, and any view-specific chart immediately reflect only the Marketing scope, and revert to the full dataset when returning to the default view.

- [ ] FT-10: Summary totals reflect the active view/filter
  - Action: With the default view, record the displayed Total Income, Total Expenses, and Net Cash Flow; independently sum the default transactions.
  - Expected: Summary cards/section show Total Income, Total Expenses, and Net (Income − Expenses); values equal the manual sums and update when a narrower filter or custom view is applied.

## Constraint
- [ ] CS-01: Required fields are enforced on transaction save
  - Action: Open "Add Transaction", leave description and/or amount empty, attempt to save.
  - Expected: Save is blocked, a visible validation message names the missing field(s), and no new row is added to the list.

- [ ] CS-02: Invalid amounts are rejected
  - Action: Enter amount "abc", then "0", then "-50" in the amount field and attempt to save.
  - Expected: All three are rejected with a clear error (e.g., "Enter a positive number"); the form does not submit.

- [ ] CS-03: Status is limited to exactly Paid / Pending / Expected
  - Action: Inspect the status control on the transaction form and in the list.
  - Expected: Status is a selection among only Paid, Pending, Expected (no free-text entry, no fourth state); every transaction shows one of these three.

- [ ] CS-04: Recurring transactions require an interval; one-off transactions have none
  - Action: Mark a transaction as "Recurring" but leave the repeat interval unset and save; then save as "One-time".
  - Expected: The recurring save is blocked with a validation message until an interval (e.g., Monthly) is chosen; the one-time save succeeds and shows no recurrence data.

- [ ] CS-05: A custom view requires a name and a scope
  - Action: Open "Create View" and submit with an empty name; then submit with a name but no filters/category selected.
  - Expected: Both attempts are blocked with validation feedback; the view is not added to the view selector.

## Interaction
- [ ] IX-01: Saving a transaction gives feedback and updates the UI in place
  - Action: Add a new transaction and submit.
  - Expected: A success message/toast (or equivalent confirmation) appears, the modal/form closes, and the new transaction appears in the list without requiring a manual page reload.

- [ ] IX-02: Filter, sort, and view changes propagate instantly to charts and summaries
  - Action: Change a filter (e.g., project = "Client A") and observe the rest of the dashboard.
  - Expected: The list, summary totals, and charts/forecast update in response to the change with no stale values left from the previous filter.

- [ ] IX-03: Chart elements expose their data on hover
  - Action: Hover over bars/points on the historical cash flow chart and the forecast chart.
  - Expected: A tooltip shows the period and the income/expense (or projected balance) values for that point.

## Content
- [ ] CT-01: Default dataset is present and exercises all documented features
  - Action: Load the dashboard fresh (before adding any data).
  - Expected: Pre-existing transactions are shown spanning multiple categories, projects, and payment methods, including recurring items, and transactions in each of Paid, Pending, and Expected states, so the chart and forecast render non-empty.

- [ ] CT-02: Labels and values are domain-appropriate with no placeholder content
  - Action: Review the dashboard: nav/view names, chart axes/legends, category and payment-method options, and all amounts.
  - Expected: No lorem ipsum, "TODO", or "undefined/NaN/placeholder" text appears; amounts use consistent currency formatting; legend/labels clearly distinguish Income vs. Expense and Historical vs. Forecast.