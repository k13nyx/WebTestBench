# Test Result

## Functionality
- [ ] FT-01: One-off income transaction can be recorded with full attribution
  - Action: Click "Add Transaction"; enter description "Client invoice #101", amount 2500, type Income, date, category "Sales", project "Client A", payment method "Bank Transfer", status "Paid"; save.
  - Expected: Transaction is saved and appears in the transactions list showing all entered values (description, amount, category, project, payment method, status = Paid, type = Income).
  - Bug Report:
    - Issue: Missing field value in list rendering / missing option values
    - Actual: The save itself works — the row renders "Client invoice #101 | Nov 8, 2026 | • | Client: TechCorp | Product Sales | Paid | +$2,500" and the Edit dialog confirms `Wire Transfer` was stored. But (a) the **payment method is never shown as a value in the list row** — it appears only as an unlabelled `<svg class="lucide-arrow-right-left">` with no text, `title`, or `aria-label`, so the entered method is not readable in the list; and (b) the checklist's literal option values do not exist: Category options are `Client Services / Product Sales / Consulting / Subscriptions` (income) and `Salaries / Marketing / Software & Tools / Office & Utilities / Travel / Professional Services` (expense) — no "Sales"; projects are `Marketing Campaigns / Operations / Client: TechCorp / Client: RetailMax / Product Development / General` — no "Client A"; payment methods are `Business Checking / Business Credit Card / PayPal / Stripe / Wire Transfer` — no "Bank Transfer" (closest equivalents were recorded instead).

- [X] FT-02: Recurring expense can be recorded with a repeat interval
  - Action: Add a transaction of type Expense, description "Software subscription", amount 99, category "Operations", payment method "Credit Card", and set it as recurring with a monthly interval and a next due date; save.
  - Expected: Transaction is saved, visibly flagged as recurring (e.g., "Monthly" badge), and its upcoming instance appears in the upcoming/recurring list.
  - Verified: Saved with type Expense, −$99, interval select present after toggling "Recurring Transaction" (`Weekly | Monthly | Quarterly | Yearly`, default Monthly); the row is visibly flagged with a `lucide-repeat` icon next to the description; `Business Credit Card` renders as the `lucide-credit-card` icon. A recurring item with a future due date (verified separately: "Cloud backup subscription", Dec 1 2026, Monthly) appears in the Forecast → "Upcoming Transactions" list (count went 5 → 6, row "Cloud backup subscription | Dec 1, 2026 | expected −$50"). Note: the interval is indicated by an icon only — no textual "Monthly" badge in the list; "Credit Card" exists as "Business Credit Card" and "Operations" is a project, not a category (category Software & Tools used).

- [X] FT-03: Transaction status can be changed between Paid, Pending, and Expected
  - Action: Open an existing "Pending" transaction and change its status to "Paid" (via edit or an inline status control); save.
  - Expected: The list row now shows status "Paid", and summary totals/status filters reflect the new status.
  - Verified: Row-menu → Edit → Status = Paid → "Update Transaction". Row changed to "Conference Sponsorship | Nov 15, 2026 | • | Marketing Campaigns | Marketing | Paid | −$5,000". Dashboard summaries followed: Total Expenses $72,300 → $77,300, Net +$14,300 → +$9,300, Pending card $42,000 → $46,950 ("$75,000 in / $28,050 out"). Status filter (Paid) returned "16 of 21 transactions" (correct paid count). Status was reverted to Pending afterwards.

- [ ] FT-04: Filtering narrows the transaction list to matching records
  - Action: Apply filters: status = "Paid" and category = "Operations"; then change to payment method = "Credit Card".
  - Expected: Only transactions matching all active filters are shown; non-matching rows disappear; clearing filters restores the full list.
  - Bug Report:
    - Issue: Missing filter control / invalid filter value
    - Actual: The transactions toolbar exposes only four filter buttons — **Type, Status, Category, Project — there is no Payment Method filter**, so "change to payment method = Credit Card" cannot be performed. Also "Operations" is not offered as a *category* (it is a project). With the available filters, narrowing works correctly: Status=Paid → "17 of 23"; Category=Salaries → 3 rows (`Team Salaries` Dec 7/Nov 7/Oct 8) with a "Category1" active-filter badge; clearing all filters restored "23 of 23".

- [ ] FT-05: Sorting orders transactions by the chosen column
  - Action: Click the column header "Amount" to sort ascending, then descending; repeat with "Date".
  - Expected: Rows reorder correctly (e.g., ascending amount = smallest → largest; descending = largest → smallest), including after numeric comparison of currency values.
  - Bug Report:
    - Issue: Missing sortable column headers / incorrect numeric sort semantics
    - Actual: The list is a card list with **no column headers at all** — sorting is only reachable through a "Sort by" combobox (`Date | Amount | Name`) plus a separate direction-toggle button, so the described interaction is impossible. Additionally, Amount sorting compares **absolute magnitude, not signed value**: "ascending" produced `−$0, −$99, −$800, −$1,200, … −$28,000, … +$35,000` and descending the reverse, instead of −$28,000 → +$35,000. Date sorting is correct (asc: Aug 10 → Dec 7; desc: Dec 7 → Aug 10).

- [ ] FT-06: Historical cash flow chart renders from recorded transactions
  - Action: Open the dashboard chart section; ensure the historical view (e.g., monthly Income vs. Expense bars/lines over past periods) is displayed.
  - Expected: A chart is rendered with income and expense series per time period; the period totals for default data match the sum of that period's transactions.
  - Bug Report:
    - Issue: Chart data not derived from transactions (hardcoded series)
    - Actual: The Recharts "Cash Flow Overview" renders with Income/Expenses/Forecast legend and Jul–Mar axis, but the per-period values are static demo numbers that match no recorded data (tooltip readings): **Aug $52,000 / $38,000** (actual Aug: income $9,600, expenses $0), **Sep $61,000 / $42,000** (actual: $34,000 / $3,600), **Oct $55,000 / $40,000** (actual: $28,000 / $32,700), **Nov $68,000 / $45,000** (actual paid: $15,000 / $36,000), Dec $72,000 / $48,000. Values also never change when data changes (adding/removing transactions, switching views). For contrast, the Analytics page *is* data-derived: "Income by Source" = Client Services $30,000 + Product Sales $26,500 + Consulting $20,500 + Subscriptions $9,600 = $86,600, exactly matching the paid-income sum.

- [ ] FT-07: Forecast projects future balances from Expected payments and recurring items
  - Action: Open the forecast section; compare the projected balance for the next period against: current balance + sum of Expected income − (sum of Expected expenses + due recurring expenses).
  - Expected: A forecast (chart or table) shows future periods with balances, and the math includes upcoming Expected transactions and recurring items; totals match manual calculation within rounding.
  - Bug Report:
    - Issue: Forecast chart uses hardcoded values; chart shows no balances
    - Actual: The KPI math is correct — Current Balance $14,300 (=86,600−72,300) and Projected (3 months) $56,300 = 14,300 + (25,000+35,000+15,000) − (5,000+28,000) over the 5 upcoming pending/expected items (which include the recurring instances TechCorp Retainer Dec 6 and Team Salaries Dec 7); after adding a −$50 expected recurring item it updated to $56,250 and the item appeared in "Upcoming Transactions" (5→6). However the "3-Month Forecast" chart does **not** derive from or display that balance: tooltips read Jan income $65,000/expenses $46,000/net $19,000, Feb $70,000/$48,000/$22,000, Mar $75,000/$50,000/$25,000 — periods for which **no transactions exist**, they conflict with the $56,300 card, they are unchanged by the new −$50 recurring item, and Jan–Mar recurring items (retainer +15,000, salaries −28,000, rent −4,500 ≈ −17,500/month) are not projected at all.

- [X] FT-08: Custom view can be created scoped to a business area
  - Action: Click "Create View" (or equivalent); name it "Marketing", scope it to category "Marketing" (e.g., via its filters), and save.
  - Expected: "Marketing" appears in the view selector/tab bar and can be selected.
  - Verified: /views page → name "Marketing", "Marketing" category checkbox checked (`aria-checked="true"`), submitted → sidebar Custom Views list became `Marketing Overview, Operations, TechCorp Client, Pending Payments, Marketing` and selecting it switched the dashboard into that view.

- [ ] FT-09: Switching views applies tailored filters and summaries
  - Action: Select the "Marketing" view, then switch back to the "All Transactions"/default view.
  - Expected: The transaction list, summary totals, and any view-specific chart immediately reflect only the Marketing scope, and revert to the full dataset when returning to the default view.
  - Bug Report:
    - Issue: Chart not scoped to active view (stale values)
    - Actual: List and summaries scoped correctly and instantly — heading became "Marketing", Total Income $0, Total Expenses $3,500, Net −$3,500, Pending −$5,000 ("$0 in / $5,000 out"), and only Marketing-category rows remained (Conference Sponsorship, Google Ads Campaign; `Marketing Software` correctly excluded as category "Software & Tools"); returning to Dashboard restored $86,600 / $72,300 / +$14,300 and the 5-item recent list. **But the "Cash Flow Overview" chart did not reflect the view scope**: hovering the same period while the Marketing view was active still returned the global hardcoded values "Sep | Income: $61,000 | Expenses: $42,000" (Marketing scope should be $0 income, ≤$3,500 expenses).

- [X] FT-10: Summary totals reflect the active view/filter
  - Action: With the default view, record the displayed Total Income, Total Expenses, and Net Cash Flow; independently sum the default transactions.
  - Expected: Summary cards/section show Total Income, Total Expenses, and Net (Income − Expenses); values equal the manual sums and update when a narrower filter or custom view is applied.
  - Verified: Cards show Total Income **$86,600**, Total Expenses **$72,300**, Net Cash Flow **+$14,300** (= 86,600 − 72,300), plus a Pending card $42,000 ("$75,000 in / $33,000 out"). Manual sums of the 15 paid default rows: income 15,000+15,000+8,500+4,500+12,000+22,000+9,600 = 86,600 ✓; expenses 28,000+28,000+4,500+3,500+1,200+3,500+800+2,800 = 72,300 ✓. Totals also updated on view change (Marketing view → 0 / 3,500 / −3,500) and on a status change (see FT-03).

## Constraint
- [X] CS-01: Required fields are enforced on transaction save
  - Action: Open "Add Transaction", leave description and/or amount empty, attempt to save.
  - Expected: Save is blocked, a visible validation message names the missing field(s), and no new row is added to the list.
  - Verified: With both empty, the submit was blocked (`#description.required = true`, `#amount.required = true`, `validity.valid = false`), focus moved to the Description field and its native validation bubble appeared, the dialog stayed open, and the counter remained "20 of 20" (no new row). Note: the message is the browser's native "Please fill out this field" bubble pointing at each field — the app renders no custom inline error text.

- [ ] CS-02: Invalid amounts are rejected
  - Action: Enter amount "abc", then "0", then "-50" in the amount field and attempt to save.
  - Expected: All three are rejected with a clear error (e.g., "Enter a positive number"); the form does not submit.
  - Bug Report:
    - Issue: Missing validation — zero amount accepted
    - Actual: **"0" was accepted and a transaction was saved** with an empty/zero amount — a row "CS02 test | Nov 8, 2026 | • | Unknown | Unknown | Paid | −$0" appeared in the list (count went 20 → 21) and the form submitted (dialog closed). "abc" is only rejected incidentally by the browser (input[type=number] silently drops letters — `fill('abc')` throws "Cannot type text into input[type=number]", value stays ""), and "−50" is rejected only by the native min rule (`validity.valid = false`, message "Value must be greater than or equal to 0."). No application-level error such as "Enter a positive number" is ever displayed, and `min="0"` itself permits 0.

- [X] CS-03: Status is limited to exactly Paid / Pending / Expected
  - Action: Inspect the status control on the transaction form and in the list.
  - Expected: Status is a selection among only Paid, Pending, Expected (no free-text entry, no fourth state); every transaction shows one of these three.
  - Verified: Form Status control is a Radix select combobox whose option list is exactly `Paid | Pending | Expected` (default "Pending") — no text input, no fourth value. The list filter popover offers exactly the same three checkboxes (`paid`, `pending`, `expected`), and the view-builder "Filter by Status" section likewise only `paid/pending/expected`. Every one of the 20 default rows renders a lowercase status badge in that set.

- [X] CS-04: Recurring transactions require an interval; one-off transactions have none
  - Action: Mark a transaction as "Recurring" but leave the repeat interval unset and save; then save as "One-time".
  - Expected: The recurring save is blocked with a validation message until an interval (e.g., Monthly) is chosen; the one-time save succeeds and shows no recurrence data.
  - Verified: Enabling the "Recurring Transaction" switch reveals an interval select that is **always populated** (default value "Monthly", options `Weekly | Monthly | Quarterly | Yearly`), so a recurring record can never be saved without an interval — the described "unset interval" state does not exist and therefore no blocking message could be triggered (no validation message is shown or needed). One-off save: "Client invoice #101" saved successfully and its row contains no repeat icon and no interval data (icons: `trending-up, arrow-right-left, ellipsis`).

- [ ] CS-05: A custom view requires a name and a scope
  - Action: Open "Create View" and submit with an empty name; then submit with a name but no filters/category selected.
  - Expected: Both attempts are blocked with validation feedback; the view is not added to the view selector.
  - Bug Report:
    - Issue: Missing validation — scope not required
    - Actual: Empty-name submit stayed on /views and added no view (`#name.required = true`, native bubble only — no app-level feedback text). The second attempt was **not blocked**: with name "Marketing QA" and *no* Type/Status/Category/Project filters checked, the app created the view, navigated to `/`, and added "Marketing QA" to the Custom Views selector (verified in the sidebar list `…, Pending Payments, Marketing QA`). The unscoped view was deleted afterwards.

## Interaction
- [ ] IX-01: Saving a transaction gives feedback and updates the UI in place
  - Action: Add a new transaction and submit.
  - Expected: A success message/toast (or equivalent confirmation) appears, the modal/form closes, and the new transaction appears in the list without requiring a manual page reload.
  - Bug Report:
    - Issue: No success feedback
    - Actual: The dialog closes and the new row appears in place (counter 20 → 21/22/23 as applicable) without reload — but **no confirmation of any kind is shown**: the mounted "Notifications (F8)" region's `<ul>` stays empty and DOM scans 150 ms and 750 ms after each of four successful saves (insert and update) found zero `[data-sonner-toast]`, `[role="status"]`, `[role="alert"]`, or list-item text.

- [ ] IX-02: Filter, sort, and view changes propagate instantly to charts and summaries
  - Action: Change a filter (e.g., project = "Client A") and observe the rest of the dashboard.
  - Expected: The list, summary totals, and charts/forecast update in response to the change with no stale values left from the previous filter.
  - Bug Report:
    - Issue: Charts/forecast not reactive (stale values)
    - Actual: View/summary propagation works — selecting the Marketing view instantly switched summaries to $0 / $3,500 / −$3,500 and the list to Marketing rows; a status change instantly updated the dashboard cards. But (1) the **charts never update**: under the Marketing view the overview chart still reported "Sep Income $61,000 / Expenses $42,000", and the forecast chart still reported Jan–Mar $65,000/$70,000/$75,000 income after a new −$50 expected recurring item was added (while the Projected card correctly moved $56,300 → $56,250). (2) The Transactions page's own filter/sort controls (the only "filter" affordances, and they include a Project filter) have **no summary or chart on that page to propagate to** — the dashboard exposes no filters at all — so a filter change can never update charts/summaries as described.

- [X] IX-03: Chart elements expose their data on hover
  - Action: Hover over bars/points on the historical cash flow chart and the forecast chart.
  - Expected: A tooltip shows the period and the income/expense (or projected balance) values for that point.
  - Verified: `.recharts-tooltip-wrapper` responds to hover on both charts. Dashboard overview: "Aug | Income: $52,000 | Expenses: $38,000" … "Mar | Income: $75,000 | Expenses: $50,000" (period + both series). Forecast chart: "Jan (Projected) | Income: $65,000 | Expenses: $46,000 | Net: $19,000", "Feb (Projected) … Net: $22,000", "Mar (Projected) … Net: $25,000". (Values are correct as *tooltips*; their data provenance is covered by the FT-06/FT-07 failures.)

## Content
- [X] CT-01: Default dataset is present and exercises all documented features
  - Action: Load the dashboard fresh (before adding any data).
  - Expected: Pre-existing transactions are shown spanning multiple categories, projects, and payment methods, including recurring items, and transactions in each of Paid, Pending, and Expected states, so the chart and forecast render non-empty.
  - Verified: Fresh load shows 20 transactions ("20 of 20"): 10 categories (Salaries, Client Services, Consulting, Product Sales, Subscriptions, Marketing, Software & Tools, Office & Utilities, Travel, Professional Services), 6 projects (Operations, Marketing Campaigns, Client: TechCorp, Client: RetailMax, Product Development, General), ≥4 distinct payment-method icons (building, zap, credit-card, wallet, arrow-left-right), 7 recurring rows (`lucide-repeat`: Team Salaries ×3, TechCorp Monthly Retainer ×3, Office Rent, AWS Hosting, Marketing Software, Annual Subscription), and all three statuses (15 paid / 2 pending / 3 expected). Dashboard chart renders Jul–Mar with both series; Forecast renders 5 upcoming items and non-zero projections.

- [X] CT-02: Labels and values are domain-appropriate with no placeholder content
  - Action: Review the dashboard: nav/view names, chart axes/legends, category and payment-method options, and all amounts.
  - Expected: No lorem ipsum, "TODO", or "undefined/NaN/placeholder" text appears; amounts use consistent currency formatting; legend/labels clearly distinguish Income vs. Expense and Historical vs. Forecast.
  - Verified: A full-text scan found **zero** occurrences of `undefined`, `NaN`, `lorem`, `TODO`, `placeholder`, or `[object`. All amounts are consistently formatted as `$X,XXX` (e.g. $86,600, −$28,000, +$2,500) with `+$`/`−$` signs for direction. Nav/view names are domain-real (Dashboard, Transactions, Analytics, Forecast; Marketing Overview, Operations, TechCorp Client, Pending Payments); category and payment-method option lists are business-appropriate; chart axes are labelled `$0k…$80k` with month ticks; the legend reads `Income / Expenses / Forecast` under "Historical data and 3-month forecast", and forecast points are labelled "(Projected)". Minor content defects observed: payment methods are conveyed by icon only (no text label or accessible name — e.g. `zap` vs `wallet` are ambiguous), the Analytics "Expenses by Category" legend lists 5 of the 6 pie slices (Software & Tools, $2,000, missing, so the legend sums to $70,300 vs $72,300), and rows whose optional fields were left blank display the fallback label "Unknown".
