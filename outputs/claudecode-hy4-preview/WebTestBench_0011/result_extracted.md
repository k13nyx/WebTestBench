# Test Result

## Functionality

- [X] FT-01: User can record a new one-off income transaction
  - Action: Open the dashboard, click the primary "Add Transaction" / "New Transaction" button, select type "Income", enter a description, amount (e.g., 1500), today's date, leave recurrence off, and save.
  - Expected: The transaction saves successfully and appears in the transaction list with type Income, the entered description, date, and amount (positive value, e.g. 1,500.00).

- [X] FT-02: User can record a new one-off expense transaction
  - Action: Click "Add Transaction", select type "Expense", enter a description, amount (e.g., 250), a date, leave recurrence off, and save.
  - Expected: The transaction saves and appears in the transaction list with type Expense and the amount displayed as an outgoing value (e.g., -250.00 or in the Expenses column), and it is excluded from Total Income.

- [ ] FT-03: User can record a recurring transaction and its future occurrences are generated
  - Action: Click "Add Transaction", select type Expense, set recurrence/frequency (e.g., Monthly), enter amount 500, a start date within the current month, and save.
  - Expected: The transaction is saved as recurring (badge/label such as "Recurring" or "Monthly" is shown), and an occurrence appears in each upcoming month within the forecast horizon (e.g., next 3 months each show -500.00).
  - Bug Report:
    - Issue: Recurring occurrences not generated / no textual recurring label
    - Actual: Enabling "Recurring Transaction" reveals a Frequency selector (Monthly default) and the row is saved with only a `lucide-repeat` icon next to the title — no "Recurring"/"Monthly" text badge. No future occurrences are generated: the Forecast "Upcoming Transactions" list showed the item once only ("FT03 Monthly Software Recurring, Nov 10, 2026, pending, -$500") with no Dec 10 / Jan 10 occurrences, and "Projected (3 months)" was $57,050 = Current Balance $14,300 + the one-time sum of the 8 stored upcoming items ($42,750), i.e. the -$500 was never expanded month by month.

- [ ] FT-04: User can assign a transaction to a category, a project, and a payment method
  - Action: Create a new transaction, then select a value from each of the "Category", "Project", and "Payment Method" fields (using existing options from the default data) and save.
  - Expected: The saved transaction row displays all three assigned values, and the transaction is retrievable when filtering by each one individually.
  - Bug Report:
    - Issue: Payment method not retrievable/shown as a value — no payment method filter exists
    - Actual: A transaction saved with Category "Office & Utilities", Project "Operations", Payment Method "Business Credit Card" renders as "FT02 Office Supplies | Nov 8, 2026 | • | Operations | Office & Utilities | Pending | -$250" — category badge and project label are text, but the payment method appears only as an untitled `lucide-credit-card` icon with no label. The filter bar offers only Type, Status, Category, Project (plus a Date/Amount/Name sort), so there is no way to filter the list by payment method; the transaction cannot be retrieved by that assignment.

- [ ] FT-05: User can mark a transaction as Paid, Pending, or Expected
  - Action: Create a new transaction and set its status to "Expected"; save. Then edit the same transaction and change the status to "Paid".
  - Expected: The transaction displays the status "Expected" after the first save and "Paid" after the edit; both changes persist after a page reload.
  - Bug Report:
    - Issue: State is not persisted — all records and edits are lost on reload
    - Actual: The new transaction showed "Expected" after the first save and "Paid" after editing it (row: "FT05 Expected Client Invoice | Nov 15, 2026 | • | Unknown | Unknown | Paid | +$2,000"), but after `page.reload()` the row was gone and the list reverted to "20 of 20 transactions" (the seeded data). No persistence layer exists — localStorage and sessionStorage are both empty, so neither the created transaction nor the status change survives a reload.

- [X] FT-06: User can filter the transaction list
  - Action: Using the default transactions, apply a filter for one existing category, then add a status filter of "Paid". Clear filters afterwards.
  - Expected: Only transactions matching the selected category (and then also the "Paid" status) are displayed; the count and totals reflect only the filtered set; clearing filters restores the full list.

- [X] FT-07: User can sort the transaction list
  - Action: Click the "Amount" column header to sort, then click again to reverse it. Repeat for the "Date" column.
  - Expected: Rows reorder into ascending order on first click and descending on the second for Amount, and the same toggle behaviour works for Date.

- [ ] FT-08: Historical cash flow chart is displayed and reflects the recorded transactions
  - Action: With no filters applied, open the dashboard's chart section.
  - Expected: A chart of past cash flow renders with a time axis of past periods (e.g., months), showing income and expense values; the most recent period's income and expense values match the figures obtainable from the transaction list for that period.
  - Bug Report:
    - Issue: Chart renders static sample data that does not match the transaction records
    - Actual: The "Cash Flow Overview" chart renders months Jul–Mar with tooltips Aug "Income: $52,000 Expenses: $38,000", Sep "$61,000 / $42,000", Oct "$55,000 / $40,000", Nov "$68,000 / $45,000", Dec "$72,000 / $48,000". The sums computed from the transaction list for those same months are Aug $9,600 / $0, Sep $34,000 / $3,600, Oct $28,000 / $32,700, Nov $76,500 / $41,750, Dec $15,000 / $28,000. Every period differs, e.g. the most recent period Dec shows $72,000 income in the chart versus $15,000 of December income in the list.

- [X] FT-09: Forecast of future cash balances is displayed
  - Action: Open the forecast section of the dashboard and read the projected balance for the next month.
  - Expected: A projected future cash balance is shown for upcoming periods, and the next period's projected balance equals the current balance plus upcoming expected/recurring income minus upcoming expected/recurring expenses.

- [X] FT-10: User can create a custom view for a business area
  - Action: Use the "New View" / "Create View" control, name it (e.g., "Marketing"), set its scope by selecting a filter (e.g., category "Marketing" or project/client from the default data), and save.
  - Expected: The new view is created and appears as a selectable entry in the view switcher/list.

- [ ] FT-11: User can switch between custom views and see tailored summaries
  - Action: Select the custom view created in FT-10, then switch back to the default/all-transactions view.
  - Expected: When the custom view is active, the transaction list, summary figures, and charts show only the transactions within that view's scope, and the totals differ from (are a subset of) the unfiltered totals. Switching back restores the full, unfiltered figures.
  - Bug Report:
    - Issue: Chart panel is not scoped to the active view (static chart data)
    - Actual: Activating the "FT10 Marketing C" view (scope: category Marketing) correctly retitled the page and scoped the summary ($0 income / $3,500 expenses / -$3,500 net versus $112,600 / $72,300 / +$40,300 unfiltered) and scoped the Recent Transactions list to "Conference Sponsorship" and "Google Ads Campaign"; switching back restored the full figures. However, the cash flow chart tooltips were byte-identical in both states (Aug 52,000/38,000 … Feb 70,000/48,000), so the chart does not reflect the view's scope.

## Constraint

- [ ] CS-01: Transaction cannot be saved with missing or invalid required fields
  - Action: Open "Add Transaction" and attempt to save with the amount empty. Repeat with amount "0", then with amount "-100", then with the date field cleared.
  - Expected: Each attempt is blocked — the record is not created, it does not appear in the transaction list, and a validation message is shown near the offending field.
  - Bug Report:
    - Issue: Zero-amount transaction accepted; validation relies on native browser bubbles only
    - Actual: Empty amount → blocked ("Please fill out this field."), amount "-100" → blocked ("Value must be greater than or equal to 0."), cleared date → blocked ("Please fill out this field."); the list stayed at 20 of 20 for those three. Amount "0", however, was accepted: the dialog closed and the list became "21 of 21 transactions" with a new $0 expense row ("CS01b"). In all blocked cases the only message was the browser's native validation bubble — the form renders no inline error text next to the offending field.

- [X] CS-02: A transaction holds exactly one status at a time, from the allowed set
  - Action: Open a default transaction and inspect its status field; attempt to set both "Paid" and "Pending" at once, then check that no status other than Paid / Pending / Expected is offered.
  - Expected: The status selector offers exactly the three options Paid, Pending, and Expected; only one can be active, and no other status value is selectable.

- [ ] CS-03: A custom view cannot be created without a name and a defined scope
  - Action: Open "New View" and attempt to save with the name field empty; then enter a name but leave the filter/scope unselected and save.
  - Expected: Both attempts are blocked — no view is added to the view switcher — and a validation message indicates the missing name or missing scope.
  - Bug Report:
    - Issue: View with no scope can be created
    - Actual: With an empty name the submit was blocked (native "Please fill out this field." on `#name`, still on /views, no view added). With the name "CS03 NoScope Test" and no Type/Status/Category/Project selection, clicking "Create View" was accepted: the app navigated to the dashboard and the sidebar switcher contained ["Marketing Overview", "Operations", "TechCorp Client", "Pending Payments", "CS03 NoScope Test"], with no validation message shown.

- [ ] CS-04: Forecast and upcoming totals exclude transactions already marked Paid
  - Action: Note the next period's projected balance. Change a pending/expected upcoming transaction (e.g., the largest one) to "Paid", then re-read the next period's forecast.
  - Expected: Once marked Paid, that transaction is no longer counted as an upcoming cash movement in the forecast; the projected balance/future totals decrease by exactly that transaction's amount, and the historic/paid figures remain unchanged.
  - Bug Report:
    - Issue: Projected balance does not decrease when an upcoming item is marked Paid; paid/historic figures change instead
    - Actual: "TechCorp Project Milestone" (+$25,000, pending, Nov 12) was edited to Paid. It was correctly removed from the forecast (Upcoming Transactions went from 6 to 5 entries and the upcoming subtotal from $42,000 to $17,000, i.e. exactly -$25,000), but the projected balance did not decrease: "Projected (3 months)" stayed at $57,300 before and after, while "Current Balance" rose from $15,300 to $40,300 (+$25,000) and the dashboard's paid Total Income rose from $87,600 to $112,600 — so the historic/paid figures did not remain unchanged.

## Interaction

- [X] IX-01: Transaction list and summary figures update immediately after adding a transaction
  - Action: With the dashboard open, note the Total Income / Net Cash Flow figures, add a new income transaction of 1,000 without reloading the page, then observe the figures.
  - Expected: The new row appears at the top of (or within) the list and the relevant summary figure increases by exactly 1,000, with no manual refresh required.

- [X] IX-02: Filter and sort controls update the list immediately
  - Action: Change a filter dropdown value, then immediately change the sort order, without reloading the page.
  - Expected: The transaction list re-renders instantly after each change, showing the newly matching and newly ordered rows, with no full page reload.

- [X] IX-03: Chart data points expose their value on hover
  - Action: Hover the mouse pointer over a data point/bar on the historical cash flow chart.
  - Expected: A tooltip/popover appears next to the cursor showing that point's period label and its cash flow value, and it disappears when the pointer moves away.

## Content

- [X] CT-01: Dashboard summary tiles are clearly labelled and show consistent currency-formatted figures
  - Action: Inspect the summary area of the unfiltered dashboard and compare its figures against the transaction list.
  - Expected: Each summary figure is clearly labelled (e.g., Total Income, Total Expenses, Net Cash Flow, Current Balance) and displayed in consistent currency formatting; Total Income minus Total Expenses equals Net Cash Flow, and both match the sums computed from the transaction list.

- [X] CT-02: Categories, projects, and payment methods are business-relevant and displayed consistently
  - Action: Open the Category, Project, and Payment Method selectors and inspect the available options; then inspect several transaction rows in the list.
  - Expected: All options are relevant to small-business cash flow (e.g., income/expense categories, client or project names, payment methods such as bank transfer, card, cash) with no placeholder, lorem ipsum, or unrelated sample entries, and each transaction row shows the same labels that were assigned to it.
