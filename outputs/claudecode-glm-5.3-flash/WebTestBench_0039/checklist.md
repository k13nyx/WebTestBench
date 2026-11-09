# Test Checklist

## Functionality
- [ ] FT-01: Create a profile with an income source
  - Action: Open the profile creation page, enter an income source (e.g., "Salary", $3,000/month), and save the profile.
  - Expected: Profile is created and the income source "Salary" with amount $3,000 is listed on the profile.
- [ ] FT-02: Add an expense category with a budget amount
  - Action: In the profile, add an expense category (e.g., "Groceries") with a monthly budget of $500 and save.
  - Expected: "Groceries" appears in the expense categories list with its $500 budget shown.
- [ ] FT-03: Add a savings goal
  - Action: Add a savings goal (e.g., "Vacation", target $2,000) to the profile and save.
  - Expected: "Vacation" appears in the savings goals list with its $2,000 target shown.
- [ ] FT-04: Log an income transaction
  - Action: Log a new transaction with amount $3,000, type income, description "Paycheck", date today, and save.
  - Expected: The transaction appears in the transaction history with its amount, date, and description.
- [ ] FT-05: Log an expense transaction assigned to a category
  - Action: Log an expense of $120, assign it to the "Groceries" category, and save.
  - Expected: The transaction appears in history assigned to "Groceries", and Groceries' actual spending in the summary increases by $120.
- [ ] FT-06: Monthly summary compares actual spending vs. budget per category
  - Action: Open the monthly summary for the current month after logging transactions in at least two categories.
  - Expected: Each category shows its budgeted amount, actual spending, and the difference/remaining amount, matching the logged transactions.
- [ ] FT-07: Filter transactions by date range
  - Action: Set a date range covering only last month and apply it to the transaction history.
  - Expected: Only transactions dated within that range are displayed; all others are hidden.
- [ ] FT-08: Filter transactions by category
  - Action: Select the "Groceries" category filter in the transaction history.
  - Expected: Only transactions assigned to "Groceries" are displayed.

## Constraint
- [ ] CS-01: Cannot save transaction with missing required fields
  - Action: Open the add-transaction form, leave the amount and/or category empty, and click Save.
  - Expected: The transaction is not created and a validation message indicates the missing required field(s).
- [ ] CS-02: Amount must be a valid positive number
  - Action: Enter an amount of "0", "-50", or non-numeric text (e.g., "abc") in the transaction amount field and save.
  - Expected: The transaction is rejected with a validation error and no invalid transaction appears in history.
- [ ] CS-03: Duplicate category names are not allowed
  - Action: Add an expense category named "Groceries" when "Groceries" already exists, then save.
  - Expected: The duplicate is rejected with an error message and no second "Groceries" category is created.
- [ ] CS-04: Savings goal target must be a positive amount
  - Action: Add a savings goal with a target of "0" or a negative value and save.
  - Expected: The goal is rejected with a validation error and is not added to the goals list.

## Interaction
- [ ] IX-01: Success feedback after saving a transaction
  - Action: Log a valid transaction and save it.
  - Expected: A success confirmation (message/toast) appears, and the new transaction is immediately visible in the transaction list without a page reload.
- [ ] IX-02: Summary highlights overspending categories
  - Action: In a category, log expenses exceeding its budget (e.g., $600 spent on a $500 "Groceries" budget) and view the monthly summary.
  - Expected: The "Groceries" category is visually highlighted (e.g., red indicator/"over budget" label) and shows the overspent amount.
- [ ] IX-03: Filters update the transaction list dynamically
  - Action: Apply or change a date-range or category filter and observe the transaction list.
  - Expected: The list refreshes immediately to show only matching transactions, and clearing the filter restores the full history.
- [ ] IX-04: Monthly summary responds to newly logged transactions
  - Action: With the monthly summary open, log a new expense and return to the summary.
  - Expected: The affected category's actual spending and remaining budget update to include the new transaction.

## Content
- [ ] CT-01: Transaction history shows complete details for each entry
  - Action: Open the transaction history and inspect logged transactions.
  - Expected: Each entry displays its date, description, amount, and assigned category, with amounts correctly formatted as currency.
- [ ] CT-02: Monthly summary shows period and totals consistent with logged data
  - Action: View the monthly summary for the current month.
  - Expected: The summary is labeled with the month it covers, and totals (total income, total spending, per-category amounts) exactly match the logged transactions for that month.
- [ ] CT-03: Profile page accurately displays all saved profile data
  - Action: Open the profile page after saving income sources, categories, and goals.
  - Expected: Every saved income source, expense category (with budget), and savings goal (with target) is listed with correct names and amounts — no missing or altered entries.