# Test Checklist

## Functionality
- [ ] FT-01: Create an income transaction
  - Action: Navigate to the transactions page, click "Add Income", enter a valid amount, select an account and category from the dropdowns, and click "Save".
  - Expected: The new income transaction appears in the transactions list with the correct amount, account, and category.
- [ ] FT-02: Create an expense transaction
  - Action: Click "Add Expense", enter an amount, select an expense category, and click "Save".
  - Expected: The expense transaction appears in the transaction history and reduces the overall balance.
- [ ] FT-03: Create a financial record (invoice/bill)
  - Action: Navigate to records management, click "New Record", select type "Invoice", fill in client details, amount, and due date, then click "Create".
  - Expected: The invoice is saved and listed in the records overview table with an "Unpaid" or "Pending" status.
- [ ] FT-04: Edit an existing financial record
  - Action: Click the "Edit" icon on an existing transaction, change the category and amount, and click "Update".
  - Expected: The transaction list updates to display the modified category and amount.
- [ ] FT-05: Filter records by date range
  - Action: Select a custom start date and end date in the date filter bar, then click "Apply Filter".
  - Expected: The transaction table displays only records with dates falling within the chosen date range.
- [ ] FT-06: Filter records by category
  - Action: Select a specific category from the category filter dropdown.
  - Expected: Only records matching the selected category are displayed in the list.
- [ ] FT-07: Create a custom category
  - Action: Navigate to category settings, click "Add Category", type a new category name, and click "Save".
  - Expected: The new category is saved and appears as an option in transaction category dropdowns.
- [ ] FT-08: Mark an entry as tax-related
  - Action: Open a transaction for editing, check the "Tax-related" checkbox, and save.
  - Expected: The transaction is saved with an active tax-related badge or indicator next to its name.
- [ ] FT-09: View monthly Profit and Loss report
  - Action: Navigate to the Reports section and select "Monthly Profit & Loss".
  - Expected: The screen displays a monthly breakdown of total income, total expenses, and the calculated net profit or loss.
- [ ] FT-10: Trigger print for tax summary report
  - Action: Navigate to the Tax Summary page and click the "Print" button.
  - Expected: The browser's native print preview dialog opens showing the formatted tax summary document.

## Constraint
- [ ] CS-01: Prevent submission with empty required fields
  - Action: Open the "Add Transaction" modal, leave the "Amount" field empty, and click "Save".
  - Expected: The form is not submitted and an inline validation error message appears stating that amount is required.
- [ ] CS-02: Reject invalid numeric amount inputs
  - Action: Type negative numbers or non-numeric characters (e.g., "-50" or "abc") into the "Amount" field and attempt to submit.
  - Expected: The system blocks the submission and displays an error indicating that amount must be a positive number.
- [ ] CS-03: Date filter start date cannot exceed end date
  - Action: Set the date filter "Start Date" to a date later than the "End Date" and click "Apply Filter".
  - Expected: The system prevents filtering and displays a validation alert stating the start date must precede the end date.

## Interaction
- [ ] IX-01: Confirmation modal before record deletion
  - Action: Click the "Delete" button on an existing transaction entry.
  - Expected: A confirmation modal opens asking to confirm the deletion before the record is permanently removed.
- [ ] IX-02: Dynamic summary recalculation on record modification
  - Action: Edit an existing income entry to increase its amount and return to the main dashboard.
  - Expected: Dashboard summary cards immediately reflect the updated total balance without requiring a manual page refresh.

## Content
- [ ] CT-01: Financial status dashboard metric cards
  - Action: Navigate to the main dashboard.
  - Expected: Prominent stat cards display "Total Income", "Total Expenses", and "Net Balance" with valid currency formatting.
- [ ] CT-02: Monthly Profit and Loss table content
  - Action: Open the Profit and Loss report view.
  - Expected: The table clearly lists distinct line items for operating income, itemized expense categories, and calculated net margin.
- [ ] CT-03: Tax summary report data alignment
  - Action: Open the Tax Summary report.
  - Expected: The report lists only transactions flagged as "Tax-related" along with their relevant taxable totals and categories.