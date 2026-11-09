# Test Result

## Functionality
- [X] FT-01: Create an income transaction
  - Action: Navigate to the transaction creation form, enter a valid amount, select the "Income" type, assign a category, choose a date, and submit.
  - Expected: The new income transaction appears in the transaction list with correct details and an updated balance.

- [X] FT-02: Create an expense transaction
  - Action: Navigate to the transaction creation form, enter a valid amount, select the "Expense" type, assign an expense category, choose a date, and submit.
  - Expected: The expense transaction is successfully saved and listed with the expense indicator (e.g., negative value or distinct color coding).

- [ ] FT-03: Create a basic invoice or bill record
  - Action: Navigate to the records/invoicing section, fill in the payee/payer name, amount, due date, select the category, and submit the record.
  - Expected: A new record is created and displayed in the unpaid/pending records list.
  - Bug Report:
    - Issue: Feature Not Implemented
    - Actual: The application does not contain a records/invoicing section, bill creation module, or unpaid/pending records list. The navigation and routing (`/`, `/transactions`, `/categories`, `/reports`, `/tax-summary`) only provide transaction and category tracking; no invoice or bill management functionality exists in the codebase or UI.

- [X] FT-04: Edit an existing transaction
  - Action: Select an existing transaction, click "Edit", modify the amount or category, and save the changes.
  - Expected: The transaction list reflects the updated details immediately.

- [X] FT-05: Delete a transaction
  - Action: Locate a transaction, click "Delete", and confirm the deletion prompt.
  - Expected: The transaction is permanently removed from the list and the balance adjusts accordingly.

- [X] FT-06: Create a custom category
  - Action: Go to category settings/management, click "Add Category", enter a unique name, select type (income/expense), and save.
  - Expected: The new category is created and becomes available in the category dropdown when adding or editing transactions.

- [X] FT-07: Filter transactions by date range
  - Action: On the transaction overview page, set a start date and an end date in the date filter inputs.
  - Expected: Only transactions that occurred within the specified date range are displayed in the list.

- [X] FT-08: Filter transactions by category
  - Action: Select a specific category from the category filter dropdown on the transactions list page.
  - Expected: The transaction list displays only items belonging to the selected category.

- [ ] FT-09: View monthly profit and loss breakdown
  - Action: Navigate to the Reports section and select the "Profit & Loss" view for a specific month.
  - Expected: A detailed breakdown of total income, total expenses, and net profit/loss for that month is presented in a structured report.
  - Bug Report:
    - Issue: Missing Dedicated Profit & Loss View
    - Actual: The Reports page (`/reports`) displays monthly summary metrics (Total Revenue, Total Expenses, Net Income, Savings Rate) and category bar breakdowns for a selected month, but does not provide a selectable or dedicated "Profit & Loss" view or a detailed itemized profit and loss financial breakdown.

- [X] FT-10: Trigger print for tax summary report
  - Action: Navigate to the Tax Summary page and click the "Print" button.
  - Expected: The browser's native print preview dialog opens showing the formatted tax summary document.

## Constraint
- [X] CS-01: Prevent submission of empty transaction forms
  - Action: Attempt to submit a new transaction with all fields left blank.
  - Expected: The form is not submitted, and required field validation errors are displayed for missing mandatory inputs (e.g., amount, date).

- [X] CS-02: Disallow negative or non-numeric amount values
  - Action: Enter a negative number (e.g., "-50") or alphabetic characters into the transaction amount input and attempt to save.
  - Expected: Input validation prevents entry or submission, prompting an error indicating that a valid positive number is required.

- [ ] CS-03: Validate date filter range logic
  - Action: In the date range filter, set a "From" date that is later than the "To" date and apply the filter.
  - Expected: The system rejects the input or displays a validation warning, preventing an invalid search query.
  - Bug Report:
    - Issue: Missing Date Range Validation
    - Actual: When setting a "From" date that is later than the "To" date (e.g., From: 02/01/2026, To: 01/01/2026), the system displays no validation warning or error message; it silently applies the invalid query and displays 0 transactions.

## Interaction
- [X] IX-01: Toggle tax-related status on transaction
  - Action: In the transaction creation/edit modal, toggle the "Tax-related" checkbox or switch, and submit the form.
  - Expected: The transaction updates with a visual indicator (e.g., tax badge/icon) confirming its tax-related status.

- [ ] IX-02: Dynamic recalculation of totals on transaction update
  - Action: Edit an existing transaction's amount from the dashboard or transactions page and observe the displayed summary totals (e.g., Total Balance, Monthly Income).
  - Expected: All related summary cards and metrics immediately update to reflect the changed amount without requiring a full page refresh.
  - Bug Report:
    - Issue: State Inconsistency / Static Account Metric
    - Actual: While Monthly Income and Net Profit/Loss dynamically recalculate upon editing a transaction, the "Total Balance" stat card on the dashboard is derived from a static initial `accounts` state (`accounts.reduce((sum, acc) => sum + acc.balance, 0)`) in `Index.tsx` that does not update when transactions are created, edited, or deleted.

## Content
- [ ] CT-01: Dashboard financial status metrics display
  - Action: Navigate to the main dashboard.
  - Expected: The dashboard displays key financial indicators including Total Income, Total Expenses, and Net Balance for the current period clearly labeled with currency symbols.
  - Bug Report:
    - Issue: Metric Label Discrepancy
    - Actual: The dashboard stat cards do not display Total Income, Total Expenses, and Net Balance for the current period; instead, they display "Total Balance" (static accounts sum), "Monthly Income", "Monthly Expenses", and "Net Profit/Loss". Cumulative "Total Income", "Total Expenses", and "Net Balance" are not provided on the dashboard.

- [ ] CT-02: Accurate display of monthly profit and loss data
  - Action: In the Reports or Profit & Loss view, examine the numbers shown for income, expenses, and net profit.
  - Expected: The sum of income minus the sum of expenses equals the displayed net profit/loss, and itemized category totals match the aggregated figures.
  - Bug Report:
    - Issue: Missing Dedicated Profit and Loss View
    - Actual: The application lacks a dedicated "Profit & Loss" view with itemized profit and loss data lines; `/reports` only shows aggregated monthly cards and category bar breakdowns without a comprehensive P&L financial statement format.

- [X] CT-03: Tax summary report data alignment
  - Action: Open the Tax Summary report.
  - Expected: The report lists only transactions flagged as "Tax-related" along with their relevant taxable totals and categories.
