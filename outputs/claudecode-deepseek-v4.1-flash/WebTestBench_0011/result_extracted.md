# Test Result

## Functionality
- [X] FT-01: Record a one-off income transaction
  - Action: Click "Add Transaction", select type "Income", enter amount, date, category, project, payment method, status, and save.
  - Expected: The one-off income appears in the transaction list with the entered values.
  - Evidence: Created "QA Income Mar" (Income, $1,000, Nov 20, 2026); it appears in the list as `QA Income Mar | Nov 20, 2026 | Marketing Campaigns | Client Services | paid | +$1,000`.

- [X] FT-02: Record a one-off expense transaction
  - Action: Click "Add Transaction", select type "Expense", enter amount, date, category, project, payment method, status, and save.
  - Expected: The one-off expense appears in the transaction list with the entered values.
  - Evidence: Created "QA Expense Ops" (Expense, $500, Nov 8, 2026, Marketing, Operations); list shows `-$500`.

- [X] FT-03: Record a recurring income/expense
  - Action: Create a transaction and set recurrence (e.g., monthly) with a start date.
  - Expected: The transaction is saved as recurring and its schedule is shown (e.g., "Monthly").
  - Evidence: Toggling "Recurring Transaction" reveals a frequency selector (Weekly/Monthly/Quarterly/Yearly); after saving, the record shows a repeat indicator icon (`lucide-repeat`) and the Edit record shows frequency = "Monthly" (start date = the Date field).

- [X] FT-04: Assign category, project, and payment method to a transaction
  - Action: In the transaction form, select values for Category, Project, and Payment Method from the available options.
  - Expected: The three attributes are saved and displayed on the transaction record.
  - Evidence: Edit modal for "QA Income Mar" shows Category = Client Services, Project = Marketing Campaigns, Payment Method = PayPal (category/project also shown on the list card).

- [X] FT-05: Mark transaction status as paid, pending, or expected
  - Action: Set the status field to each of "Paid", "Pending", and "Expected" and save.
  - Expected: The selected status is stored and visibly shown for that transaction.
  - Evidence: QA Income Mar → `paid`, QA Expense Ops → `expected`, QA Test Income 2 → `pending`, each rendered on the record.

- [X] FT-06: Filter transactions
  - Action: Apply a filter (e.g., by category, project, status, or date range).
  - Expected: Only transactions matching the filter criteria are listed.
  - Evidence: Selecting Status = "Expected" changed the list to "4 of 23 transactions", all with status `expected`; the Status filter button showed a "1" badge; clearing restored "23 of 23".

- [X] FT-07: Sort transactions
  - Action: Apply a sort (e.g., by date or amount, ascending/descending).
  - Expected: The transaction list reorders accordingly.
  - Evidence: Sort field options are Date/Amount/Name. Selecting Amount reordered by magnitude ($35,000 … -$500); toggling the direction button reversed the order (‑$500 … $35,000).

- [X] FT-08: View historical cash flow chart
  - Action: Open the historical cash flow chart.
  - Expected: A chart renders showing past income/expense (or net balance) over time.
  - Evidence: Dashboard "Cash Flow Overview — Historical data and 3-month forecast" renders a recharts area chart with month axis (Jul–Mar) and Income/Expenses/Forecast legend (note: its data is not transaction-driven — see CT-01).

- [X] FT-09: View cash balance forecast
  - Action: Open the forecast view.
  - Expected: A projection of future cash balances is shown, derived from expected payments and recurring items.
  - Evidence: /forecast shows Current Balance $15,300, Projected (3 months) $55,566, a 3-Month Forecast chart, and an Upcoming Transactions list.

- [X] FT-10: Create a custom view for a business area
  - Action: Create a custom view (e.g., "Marketing") with defined filters/scope.
  - Expected: The new view is saved and listed among the available views.
  - Evidence: Created "QA Marketing View" (scoped to Project = Marketing Campaigns); it now appears under CUSTOM VIEWS in the sidebar.

- [X] FT-11: Switch between custom views with tailored summaries
  - Action: Select a saved custom view (e.g., "Marketing", "Operations").
  - Expected: The summary updates to reflect only that view's data.
  - Evidence: Marketing Overview → Expenses $3,500, recent = only marketing items; Operations → Expenses $60,500, all Operations; TechCorp Client → Income $30,000, all Client: TechCorp. Summary and recent list update in place (URL stays `/`).

## Constraint
- [X] CS-01: Cannot save a transaction with missing required fields
  - Action: Attempt to save a transaction leaving amount or date empty.
  - Expected: Save is blocked and an error indicates the required field(s).
  - Evidence: With Amount/Date empty, the dialog stays open and no record is created; the form uses native validation — the inputs carry `required` and report "Please fill out this field." (`checkValidity()` false).

- [X] CS-02: Recurring transaction requires an interval and start date
  - Action: Set a transaction to recurring without specifying recurrence frequency or start date.
  - Expected: Save is blocked with a message requiring the recurrence details.
  - Evidence: With "Recurring Transaction" on and Date cleared, clicking save was blocked (dialog remained open, date field reports "Please fill out this field."). Frequency always defaults to a value (Monthly), so an empty frequency is not possible while the Start Date is enforced.

- [ ] CS-03: Forecast only includes expected and recurring items
  - Action: Compare forecast figures against pending/paid transactions that are not expected/recurring.
  - Expected: Paid/pending one-off items do not alter the future forecast projection.
  - Bug Report:
    - Issue: Incorrect forecast inclusion (paid and pending one-off items change the projection).
    - Actual: Adding a PAID one-off income of $10,000 (dated 2026-12-20) raised "Projected (3 months)" from $55,566 to $65,566 and Current Balance from $15,300 to $25,300. Adding a PENDING one-off income of $10,000 raised "Projected (3 months)" to $75,566 and increased "Upcoming Transactions" from 5 to 6 (the pending item also appears in the "Expected and pending payments" list). Paid/pending one-off items clearly do alter the future projection.

## Interaction
- [ ] IX-01: Confirmation feedback after saving a transaction
  - Action: Save a valid transaction.
  - Expected: A success confirmation (e.g., toast/message) appears.
  - Bug Report:
    - Issue: No success confirmation is shown.
    - Actual: Saving a valid transaction closes the dialog and adds the row, but no toast/message appears. A DOM `MutationObserver` running from the moment of save recorded only the new list row ("QA Toast Probe | Nov 8, 2026 … -$50") and an unrelated chart node; no toast, notification, or `aria-live` content was ever added (sonner/radix notification regions remained empty).

- [ ] IX-02: Chart and summary update when filters/views change
  - Action: Change the active filter or switch to another custom view.
  - Expected: The chart and summary reflect the new selection without requiring a page reload.
  - Bug Report:
    - Issue: Chart does not update when the selection changes (only the summary does).
    - Actual: Switching custom views (Dashboard → Marketing Overview → Operations → TechCorp Client) updates the summary tiles and recent-transactions list, but the "Cash Flow Overview" chart renders byte-identical SVG paths (`.recharts-area-curve` `d` values) for every view — the chart never reflects the active view.

## Content
- [ ] CT-01: Chart data matches recorded transactions
  - Action: Compare the historical chart values against the transactions in the list for the same period.
  - Expected: Displayed chart figures correspond accurately to the underlying recorded data.
  - Bug Report:
    - Issue: The historical "Cash Flow Overview" chart is not derived from recorded transactions.
    - Actual: Chart tooltips show fixed monthly figures (Jul $48,000/$35,000 … Nov Income $68,000 / Expenses $45,000 …) that do not match the transactions for those months (Nov paid income is ≈ $16,000). Decisive proof: adding a $500,000 PAID income dated 2026-11-25 changed "Total Income" to $597,600, yet the chart's Nov tooltip remained exactly "$68,000 Income / $45,000 Expenses". (Note: the Analytics page breakdowns DO track the data correctly — e.g., Income by Source "Client Services $31,000" includes the added $1,000 income — but the dashboard historical chart does not.)

- [X] CT-02: Custom view summary reflects only its defined scope
  - Action: Open a custom view scoped to a specific project/client.
  - Expected: The summary contains only transactions belonging to that scope; unrelated data is excluded.
  - Evidence: Operations view → Paid Expenses $60,500 (= 28,000 + 4,500 + 28,000, all Operations) with recent list entirely Operations; Marketing Overview → Paid Expenses $3,500 (Google Ads only); TechCorp Client → Income $30,000 (= 15,000 + 15,000 TechCorp retainers). Totals reconcile exactly to the scoped transactions.
