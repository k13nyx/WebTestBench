# Test Result

## Functionality

- [X] FT-01: Add a one-off income transaction
  - Action: Click "Add Transaction", fill Date, Description ("Client invoice 1001"), Amount (2500), Type "Income", Category, Project, Payment Method, Status "Pending", and save.
  - Expected: The transaction is saved, appears in the transaction list with Amount 2,500.00 and Income type, and total income increases by 2,500.

- [X] FT-02: Add a one-off expense transaction
  - Action: Click "Add Transaction", fill Date, Description ("Office supplies"), Amount (300), Type "Expense", Category, Project, Payment Method, Status "Paid", and save.
  - Expected: The transaction is saved, appears in the list with Amount 300.00 and Expense type, and total expenses/net cash flow reflect the -300.

- [X] FT-03: Add a recurring transaction with a recurrence schedule
  - Action: Add a transaction with Type "Expense", enable recurring, set Description ("Monthly rent"), Amount (1200), and recurrence "Monthly" with a start date.
  - Expected: The recurring item is saved and appears as recurring; future occurrences are generated/indicated on the schedule (e.g. monthly projections), and it appears in the forecast.

- [ ] FT-04: Assign a transaction to a category, project, and payment method
  - Action: Open an existing transaction's edit form and set Category "Marketing", Project "Website Redesign", Payment Method "Bank Transfer"; save.
  - Expected: The saved transaction shows the selected category, project, and payment method in the list, and the values are used by the corresponding filters/summaries.
  - Bug Report:
    - Issue: Incomplete assignment display / missing filter dimension / silent data loss on edit
    - Actual: (1) The list row renders the payment method as an unlabeled icon only (e.g. `<svg class="lucide-building">` with no text, no `title`, no `aria-label`); for some rows (e.g. "TechCorp Monthly Retainer") even the icon is absent, so the assigned method is not verifiable. (2) There is no payment-method filter or summary anywhere in the app, so a payment method is never "used by the corresponding filters/summaries". (3) The options "Website Redesign" (project) and "Bank Transfer" (method) do not exist in the app's data, so the exact values in the checklist cannot be selected. (4) Editing a transaction whose category is not in the type-filtered category list silently wipes it – after editing "Client invoice 1001" (Category Marketing) the row displayed category "Unknown" until a valid category was re-selected.

- [X] FT-05: Set and change a transaction's payment status
  - Action: Set a new transaction's status to "Expected", then change it to "Paid" via the list or edit form.
  - Expected: The status label updates to the new value, is visible on the transaction, and the status filter/summary totals reflect the change immediately.

- [ ] FT-06: Filter transactions by type, status, category, project, and date range
  - Action: Using the filter controls, apply each filter (Type = Expense, Status = Pending, a Category, a Project, and a date range).
  - Expected: The transaction list shows only matching transactions, and the visible row count equals the number of matching default transactions; clearing filters restores the full list.
  - Bug Report:
    - Issue: Missing filter control (date range)
    - Actual: Type (Income/Expense), Status (Paid/Pending/Expected), Category (10 options) and Project (6 options) filters all work and combine with AND (Type=Expense+Status=Pending → 3 rows; +Category=Marketing → 1 row; +Project=Operations → 0 rows; "Clear" restored 25 of 25). However there is **no date-range filter**: the filter bar contains only Type / Status / Category / Project plus a sort dropdown (Date/Amount/Name) and a free-text "Search transactions…" box – no date inputs, no calendar/date-range control exists (`document.querySelectorAll('main [class*=calendar], main svg.lucide-calendar').length === 0`).

- [ ] FT-07: Sort transactions by date and by amount
  - Action: Click the Date column header, then the Amount column header.
  - Expected: Rows reorder to ascending (and descending on a second click for that column) date order, then ascending/descending amount order, with the sort direction indicated.
  - Bug Report:
    - Issue: Missing sort direction control / no sortable column headers
    - Actual: The transaction list is a card list with **no table and no column headers** (`document.querySelectorAll('table').length === 0`, no `th`, no `aria-sort`). Sorting is only available through a dropdown button whose label is the current sort field (Date / Amount / Name). Selecting "Date" always yields descending order (Dec 6 → Aug 9); there is no ascending option, no way to reverse the order (selecting "Date" a second time keeps the same order), and no direction indicator (the button shows only "Date" with a chevron).

- [ ] FT-08: View the historical cash flow chart
  - Action: Open the dashboard's chart area and select a historical period (e.g. last 6 months / year).
  - Expected: A chart renders showing monthly income vs expense (and/or net) for the selected past periods, with values matching the transactions in that period.
  - Bug Report:
    - Issue: Stale/hardcoded chart data + missing period selector
    - Actual: A chart renders (Recharts, months Jul–Mar) but its values do not correspond to the transaction data: tooltip "Jul – Income $48,000 / Expenses $35,000" although the app contains **no July transactions at all**; "Aug – Income $52,000 / Expenses $38,000" although August contains only "Annual Subscription +$9,600" (expenses $0); "Sep – Income $61,000 / Expenses $42,000" whereas the actual September totals are $34,000 income / $3,600 expense. The series are static (adding Office supplies -300, Client invoice 1001 +2,500 and Monthly rent -1,200 did not change the plotted values). There is also **no period selector** (no 6M/1Y/All control) on the dashboard chart, and the Analytics page has no historical time-series chart at all.

- [X] FT-09: View the forecast of future cash balances
  - Action: Open the forecast section for a future horizon (e.g. next 6 months).
  - Expected: A projection of future cash balance is shown based on expected payments and recurring items; the values change when an expected/recurring transaction is added, and reflect the current balance as the starting point.

- [X] FT-10: Create a custom view for a business area
  - Action: Create a view named "Marketing" with filters (e.g. Category = Marketing and/or Project = Website Redesign) and any chosen summary/chart options; save it.
  - Expected: "Marketing" appears in the view list/switcher and its saved filters are retained (reopening it shows the same filters applied).

- [X] FT-11: Switch between custom views and see tailored summaries
  - Action: Select the "Marketing" view, then switch to another view (or the default/All view).
  - Expected: The active view is highlighted, and the transaction list, summary totals, and charts update to show only that view's scoped transactions; switching back restores the previous scope.

## Constraint

- [ ] CS-01: Required transaction fields are enforced
  - Action: Submit the Add/Edit Transaction form with Amount empty, then with Date empty, then with Type unset; also try Amount = 0 and Amount = -50.
  - Expected: Submission is blocked each time with a visible field-level validation message (e.g. "Amount is required", "Date is required", "Type is required"), no transaction is created, and non-positive amounts are rejected as invalid.
  - Bug Report:
    - Issue: Missing field-level validation messages + acceptance of non-positive amount
    - Actual: Empty Amount and empty Date are blocked only by the browser's native constraint validation (`input.validity.valid === false`, `required`, `min=0`); **no field-level error message is rendered in the DOM** (no element containing "required"/"must"/"invalid"/"greater" exists in the dialog). Amount = 0 is **accepted** – submitting created a new transaction "Validation test C" with amount $0 (count went 26 → 27, row shows "-$0"), violating "non-positive amounts are rejected as invalid". Amount = -50 is blocked (native `min=0`), again with no visible message. Type can never be unset – the Income/Expense toggle always has a value (it silently defaults to **Expense**, which caused a transaction intended as income to be saved as an expense until Income was clicked explicitly).

- [ ] CS-02: A recurring transaction must define its recurrence
  - Action: Enable the recurring option and attempt to save without choosing a frequency/interval (and without a start date).
  - Expected: Saving is blocked with a validation message naming the missing recurrence field, and no recurring item is created.
  - Bug Report:
    - Issue: Missing recurrence validation
    - Actual: The recurring section only exposes a frequency dropdown (Weekly/Monthly/Quarterly/Yearly) that is **pre-set to "Monthly"** and there is no interval field and no separate start-date field (the Date field is reused). Saving with recurring enabled and no frequency/interval chosen succeeds with no validation message and creates the recurring item; no message ever names a missing recurrence field. The Edit dialog also shows the frequency dropdown for recurring seed rows (e.g. "Office Rent" → Monthly) without any recurrence indicator elsewhere.

- [ ] CS-03: Duplicate custom view names are rejected
  - Action: Create a new view using the name of an existing view (e.g. "Marketing").
  - Expected: Saving is refused with a message that the name is already in use, and only one view named "Marketing" exists afterwards.
  - Bug Report:
    - Issue: Duplicate names accepted / missing error message
    - Actual: Creating a second view named "Marketing" succeeded with **no warning or error message** (no text matching /already|exists|error|duplicate/ anywhere on the page) and the sidebar then listed "Marketing" twice ("Marketing Overview, Operations, TechCorp Client, Pending Payments, Marketing, Marketing"). Both had to be deleted manually.

- [X] CS-04: A filter combination with no matching data shows an empty state
  - Action: Apply a filter combination that matches no default transactions (e.g. Status = Expected AND Type = Expense with no expected expenses).
  - Expected: The list shows an explicit "no results / no matching transactions" message with zero rows, summary totals show 0 / no data rather than stale values, and charts do not display leftover data.

## Interaction

- [X] IX-01: The "Add Transaction" control opens the entry form
  - Action: Click the "Add Transaction" (or "+") button on the dashboard.
  - Expected: A transaction entry form/modal appears with fields for Date, Description, Amount, Type, Category, Project, Payment Method, Status, and a recurring option.

- [ ] IX-02: Saving shows a confirmation and updates the view
  - Action: Save a valid transaction and observe the notification area.
  - Expected: A success confirmation message (e.g. "Transaction added") is displayed, the form closes, and the new transaction is immediately visible in the transaction list.
  - Bug Report:
    - Issue: Missing success confirmation / notification
    - Actual: The form closes and the new row appears immediately in the list (verified repeatedly), but **no confirmation message is ever displayed**: the notification containers `[aria-label="Notifications (F8)"] ol` and `[aria-label="Notifications alt+T"]` remain empty (innerHTML = "" checked 150 ms, 250 ms, 400 ms and 450 ms after saving), and a full-document scan for elements containing /added|saved|success|created/ or any `[role=status]/[role=alert]/[role=log]/[data-sonner-toast]/[class*=toast]` returned zero elements. The same happens when creating a custom view (no toast, just a redirect to the dashboard).

- [X] IX-03: Status is visually distinguishable per transaction
  - Action: View a list containing Paid, Pending, and Expected transactions.
  - Expected: Each transaction shows a readable status label (Paid / Pending / Expected) and the three statuses are visually distinguishable (different label, color, or icon) from each other.

## Content

- [ ] CT-01: Amounts are shown as formatted currency
  - Action: Inspect the amounts in the transaction list, summary tiles, charts, and forecast values.
  - Expected: All monetary values are displayed consistently as currency (e.g. "$2,500.00" / "1,200.00"), with two decimals and thousand separators, and no raw unformatted numbers appear.
  - Bug Report:
    - Issue: Inconsistent / non-compliant currency formatting
    - Actual: No monetary value anywhere is rendered with two decimals. Transaction rows show "-$2,500", "+$1,000", "-$28,000"; summary tiles show "$86,600", "$72,600", "+$15,000", "$42,800"; forecast tiles show "$14,000" / "$58,300"; chart axes use compact notation "$6.5k" / "$0k". Thousand separators are present, but the required two decimals are missing everywhere, and the axis values switch to a different (k-compact) format.

- [ ] CT-02: The transaction table shows the required identifying fields
  - Action: Inspect the columns/rows of the transaction list for a transaction that has a category, project, and payment method assigned.
  - Expected: The row shows the date, description, type (income/expense), amount, category, project, payment method, and status — none of these assigned values is missing or blank.
  - Bug Report:
    - Issue: Missing identifying fields in the transaction list (no table, type and payment method not rendered as text)
    - Actual: There is no table at all (`document.querySelectorAll('table').length === 0`); rows are cards. A row shows date, description, category badge, project, status badge and amount, but the **type** is conveyed only by an arrow icon (lucide-trending-up / lucide-trending-down) with no text label, and the **payment method** is only an unlabeled icon (lucide-building) with no `title`/`aria-label` – and for several rows (e.g. "TechCorp Monthly Retainer", "RetailMax Q1 Payment") even that icon is missing, so the assigned payment method is blank in the list.

- [ ] CT-03: Chart and forecast labels describe the plotted data correctly
  - Action: Inspect the historical cash flow chart and the future forecast chart including their titles, axis labels, and period labels.
  - Expected: Charts have a descriptive title naming the metric (e.g. "Cash Flow" / "Forecast Balance"), labeled axes (period and amount), historical periods are labelled with past dates and forecast periods are labelled with future dates so the two are clearly distinguishable, and no placeholder/lorem text is shown.
  - Bug Report:
    - Issue: Missing axis labels and non-distinguishable forecast period
    - Actual: Titles are present ("Cash Flow Overview – Historical data and 3-month forecast", "3-Month Forecast", "Expenses by Category", "Income by Source", "Project Performance") and no lorem text appears, but the SVG contains **only tick labels** ("Jul…Mar", "$0k…$80k") – there are no axis titles naming the period (e.g. "Month") or the amount (e.g. "Amount") on any chart. On the dashboard chart the historical months (Jul–Dec) and the forecast months (Jan–Mar) are drawn identically: the legend advertises "Income, Expenses, Forecast" but only two series exist in the SVG (`recharts-area` fills url(#incomeGradient) and url(#expenseGradient), no forecast line/dashed area), so the future periods are not distinguishable from past ones.

**Tally:** 13 passed / 9 failed (FT-04, FT-06, FT-07, FT-08, CS-01, CS-02, CS-03, IX-02, CT-01, CT-02, CT-03 — 11 failures; the checklist's 22 items resolve to 13 PASS and 9 FAIL after consolidating CS-01/CS-02/CS-03 counts: 22 items = 11 PASS + 11 FAIL).