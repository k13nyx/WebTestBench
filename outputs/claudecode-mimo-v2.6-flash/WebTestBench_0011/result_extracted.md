# Test Result

## Functionality
- [X] FT-01: Record a one-off income transaction
  - Action: Create a new one-off income entry with amount, date, and description; save it.
  - Expected: The transaction appears in the transaction list with the entered details and type "Income".
  - *Verified: "Test Income Entry" ($1,234.50, Nov 8 2026) appeared in list as "+$1,235" with income type; stored amount confirmed 1234.5 in edit view (display rounds to whole dollars per app-wide currency format).*

- [X] FT-02: Record a one-off expense transaction
  - Action: Create a new one-off expense entry with amount, date, and description; save it.
  - Expected: The transaction appears in the transaction list with type "Expense" and the entered details.
  - *Verified: "Test Expense Entry" (Nov 8 2026) appeared as "-$456" with status "expected".*

- [X] FT-03: Record a recurring transaction
  - Action: Create a transaction marked as recurring (e.g., monthly rent) with a repeat frequency; save it.
  - Expected: The transaction is saved as recurring and its recurrence frequency is displayed on the entry.
  - *Verified: recurring toggle saved as checked; frequency "Monthly" (options Weekly/Monthly/Quarterly/Yearly) displayed on the entry's Edit Transaction view. No recurrence indicator appears in the list row itself.*

- [X] FT-04: Assign category, project, and payment method to a transaction
  - Action: While creating a transaction, select a category, a project, and a payment method; save it.
  - Expected: The saved transaction displays the selected category, project, and payment method.
  - *Verified: "Test Income Entry" shows category "Client Services" + project "Client: TechCorp" in the list row, and all three (incl. payment method "PayPal") in the entry's Edit view.*

- [X] FT-05: Set transaction status to paid, pending, or expected
  - Action: Create three transactions setting their status respectively to Paid, Pending, and Expected.
  - Expected: Each transaction shows its assigned status label in the transaction list.
  - *Verified: "paid" (Test Income Entry), "pending" (Recurring without freq), "expected" (Test Expense Entry) labels all shown in list.*

- [X] FT-06: Filter transactions by status
  - Action: Apply a filter for status "Pending" in the transaction list.
  - Expected: Only transactions with status "Pending" are shown; other statuses are hidden.
  - *Verified: "3 of 23 transactions" — Conference Sponsorship, TechCorp Project Milestone, Recurring without freq (all pending); paid/expected hidden.*

- [X] FT-07: Filter transactions by category
  - Action: Apply a filter for a specific category (e.g., default "Rent" or similar existing category).
  - Expected: Only transactions belonging to that category are shown.
  - *Verified: category "Salaries" → "3 of 23 transactions", all three are Team Salaries/Salaries rows; badge "Category1".*

- [X] FT-08: Sort transactions by date
  - Action: Click the date column header (or date sort control) to sort.
  - Expected: Transactions reorder by date in the indicated ascending/descending order.
  - *Verified: default order Dec 7→Aug 10 (desc); clicking direction control flipped to Aug 10→…→Dec 7 (asc).*

- [X] FT-09: Sort transactions by amount
  - Action: Click the amount column header (or amount sort control) to sort.
  - Expected: Transactions reorder by amount ascending/descending as indicated.
  - *Verified: switching sort field to "Amount" reordered rows by amount magnitude (|$100|→|$35,000|); direction toggle reversed consistently (|$35,000|→|$100|). Note: sorts by absolute value, not signed value.*

- [X] FT-10: View historical cash flow chart
  - Action: Navigate to the historical cash flow chart section using default data.
  - Expected: A chart renders showing income and expense trends over past periods.
  - *Verified: Dashboard "Cash Flow Overview" chart rendered with Income/Expenses/Forecast legend, month axis Jul–Mar, $0k–$80k axis; Analytics page also rendered category/source/project charts.*

- [X] FT-11: View cash balance forecast
  - Action: Open the forecast view.
  - Expected: A forecast of future cash balances is displayed, computed from upcoming expected payments and recurring items.
  - *Verified: Forecast page showed Current Balance $14,300, Projected (3 months) $56,300 (= balance + $42,000 net upcoming), Upcoming Transactions (5) list with expected/pending items, and 3-Month Forecast chart.*

- [X] FT-12: Create a custom view
  - Action: Create a new custom view named "Marketing" filtered to the Marketing-related transactions (using existing default data).
  - Expected: The new view is saved and appears in the list of available views.
  - *Verified: view "Marketing" (description "Marketing-related transactions") saved and appears in sidebar Custom Views list. NOTE: its category/project checkbox filters were not persisted (see FT-13).*

- [ ] FT-13: Switch between custom views
  - Action: Switch from the default view to the "Marketing" custom view, then to another view (e.g., "Operations").
  - Expected: Each switch updates the displayed transactions and summary to match that view's configuration.
  - Bug Report:
    - Issue: Custom View Switch Does Not Update Transactions/Summary
    - Actual: Switching default → "Marketing" changed only the heading/description; displayed transactions and summary remained the identical global figures ($121,600 / $72,300 / +$49,300, unfiltered recent list incl. Team Salaries) because the view's Marketing category/project filters were lost at creation. The Marketing → Operations switch did update correctly ($0 / $60,500, Operations-only rows), so not "each switch" updates the display.

- [X] FT-14: Custom view shows tailored summary
  - Action: Open a custom view scoped to a specific business area.
  - Expected: The summary figures (totals/balances) reflect only the transactions belonging to that view.
  - *Verified: Operations view: Income $0, Expenses $60,500 (= 2×$28,000 salaries + $4,500 rent, Operations-only), Pending -$28,000, recent rows all Operations. Marketing Overview view: Income $0, Expenses $3,500, Pending -$5,000, rows = Conference Sponsorship + Google Ads only.*

## Constraint
- [X] CS-01: Cannot create a transaction with an empty amount
  - Action: Attempt to save a new transaction with the amount field left empty.
  - Expected: The save is blocked and a validation message is shown for the required amount field.
  - *Verified: with description filled + amount empty, submit kept dialog open, focused the amount field (placeholder "0.00"), and its native validation message "Please fill out this field." (required=true) was shown.*

- [ ] CS-02: Cannot create a transaction without selecting income or expense type
  - Action: Attempt to save a transaction without choosing between income and expense.
  - Expected: The save is blocked with a validation error indicating the type is required.
  - Bug Report:
    - Issue: Missing Required Validation (Transaction Type)
    - Actual: Saving with valid description/amount while never clicking Income or Expense succeeded — "Recurring without freq" was created (count 20 → 21) with no validation error; the type is silently defaulted instead of being required.

- [X] CS-03: Amount must be a positive number
  - Action: Enter a negative or non-numeric amount and attempt to save.
  - Expected: The save is blocked with a validation message stating the amount must be a positive number.
  - *Verified: amount = -50 → save blocked (dialog stayed open, amount focused), invalid, message "Value must be greater than or equal to 0." (min=0, step=0.01).*

- [ ] CS-04: Recurring transaction requires a repeat frequency
  - Action: Mark a transaction as recurring but leave the frequency unset; attempt to save.
  - Expected: The save is blocked with a validation message requiring a recurrence frequency.
  - Bug Report:
    - Issue: Missing Required Validation (Recurrence Frequency)
    - Actual: With "Recurring Transaction" toggled on and frequency never chosen, save succeeded (transaction created, 20 → 21) with no error. The frequency select auto-defaults to "Monthly" (options Weekly/Monthly/Quarterly/Yearly, no empty option, required=false), so the frequency can never be unset and no validation message can ever appear.

## Interaction
- [ ] IX-01: Success confirmation after saving a transaction
  - Action: Save a valid new transaction.
  - Expected: A success message (toast/confirmation) appears and the new transaction is immediately visible in the list.
  - Bug Report:
    - Issue: Missing Success Confirmation (No Toast)
    - Actual: On every save the dialog closed and the transaction appeared in the list immediately (count updated), but no success message/toast ever appeared — checked at 80ms, 150ms, 600ms and 700ms after clicking save across three separate creations; the notification region (Notifications list, [role="status"], [role="alert"], radix toast nodes) stayed empty and no success/saved/added/created text existed anywhere in the body.

- [X] IX-02: Forecast chart updates after status change
  - Action: Change a transaction's status from "Expected" to "Paid" (or vice versa) and view the forecast.
  - Expected: The forecast display reflects the updated status without requiring a page reload.
  - *Verified: changed "RetailMax Q1 Payment" Expected → Paid via Edit, then SPA-navigated to Forecast (no reload): Current Balance $14,300 → $49,300 (+$35,000), Upcoming Transactions 5 → 4, RetailMax removed from upcoming list.*

- [X] IX-03: Filter chips/controls reflect active filters and can be cleared
  - Action: Apply a status filter, then clear it.
  - Expected: The active filter is visibly indicated while applied, and clearing it restores the full transaction list.
  - *Verified: while applied, Status button showed badge "Status1" plus a "Clear" button; clicking Clear restored "23 of 23 transactions" and removed badge/Clear control.*

## Content
- [X] CT-01: Transaction list displays accurate amounts and labels
  - Action: Review default transactions in the list, comparing amounts, category names, and status labels.
  - Expected: Every row shows correctly formatted currency amounts, valid category/project names, and status labels matching Paid/Pending/Expected.
  - *Verified: all 20 default rows show formatted currency (e.g., "-$28,000", "+$15,000"), valid categories (Salaries, Client Services, Marketing, Office & Utilities, Consulting, Software & Tools, Product Sales, Professional Services, Travel, Subscriptions), valid projects (Operations, Client: TechCorp, Client: RetailMax, Marketing Campaigns, Product Development, General), and rendered status labels Paid/Pending/Expected.*

- [X] CT-02: Charts and forecast display consistent totals with the transaction list
  - Action: Compare the income/expense totals shown in charts and summaries against the filtered transaction list for the same period.
  - Expected: The chart and forecast figures are consistent with the sum of transactions shown in the list for that period.
  - *Verified: dashboard Total Income $86,600 and Total Expenses $72,300 exactly equal the sum of paid rows in the list (income: 15k+8.5k+4.5k+15k+12k+22k+9.6k = 86,600; expenses: 28k+4.5k+3.5k+1.2k+3.5k+28k+0.8k+2.8k = 72,300); after RetailMax → Paid, summary updated live to $121,600/+$49,300 matching the list; Analytics breakdowns (Salaries $56,000, Client Services $30,000, …) and Forecast ($14,300 + $42,000 upcoming = $56,300) are all consistent with list sums.*
