# Test Checklist

## Functionality
- [ ] FT-01: User can create a simple profile with an income source
  - Action: Open the profile setup page, enter a profile name and at least one income source (e.g., "Salary") with a monthly amount, then save.
  - Expected: Profile is created and the income source with its amount is displayed on the profile page.

- [ ] FT-02: User can add an expense category with a monthly budget
  - Action: In the expense categories section, add a category (e.g., "Groceries") with a monthly budget amount, then save.
  - Expected: The new category with its budget amount appears in the category list.

- [ ] FT-03: User can add a savings goal
  - Action: In the savings goals section, add a goal (e.g., "Emergency Fund") with a target amount, then save.
  - Expected: The savings goal with its target amount appears in the goals list.

- [ ] FT-04: User can log a transaction and assign it to a category
  - Action: Open the transaction log, fill in amount, date, and description, select an expense category from the category dropdown, then save.
  - Expected: Transaction is saved and appears in the transaction history with its amount, date, description, and assigned category.

- [ ] FT-05: Monthly summary compares actual spending to budget for each category
  - Action: Open the monthly summary for the current month.
  - Expected: Every expense category shows both its budgeted amount and its actual spent amount for that month.

- [ ] FT-06: Transaction history can be filtered by date range
  - Action: In the transaction history, set a start and end date that covers only part of the default transactions, then apply the filter.
  - Expected: Only transactions dated within the selected range are displayed.

- [ ] FT-07: Transaction history can be filtered by category
  - Action: In the transaction history, select a single expense category in the category filter, then apply.
  - Expected: Only transactions assigned to the selected category are displayed.

## Constraint
- [ ] CS-01: Transaction cannot be saved with empty required fields
  - Action: Open the add-transaction form, leave amount (and/or date and category) empty, and attempt to save.
  - Expected: Transaction is not saved and a validation message identifies the missing required field(s).

- [ ] CS-02: Transaction cannot be saved with an invalid amount
  - Action: Enter a non-numeric value (e.g., "abc") or a negative number (e.g., "-50") in the amount field and attempt to save.
  - Expected: Transaction is rejected with an error message and no transaction is created.

- [ ] CS-03: Logging a transaction that exceeds a category's budget is permitted
  - Action: Log a transaction whose amount is larger than the remaining budget of its assigned category.
  - Expected: Transaction is saved successfully; overspending is handled via the summary, not blocked at entry.

- [ ] CS-04: Date range filter with start date after end date returns no transactions
  - Action: Set the history filter's start date later than its end date, then apply.
  - Expected: No transactions are displayed (or an empty-state / invalid-range message appears); the full history is NOT returned.

## Interaction
- [ ] IX-01: Overspending is visually highlighted in the monthly summary
  - Action: In the monthly summary, locate a category whose actual spending exceeds its budget.
  - Expected: That category is visually distinguished (e.g., warning color or "over budget" badge) from categories within budget.

- [ ] IX-02: Confirmation appears after a transaction is saved
  - Action: Fill and save a valid transaction.
  - Expected: A success message or toast confirms the transaction was logged.

- [ ] IX-03: New transaction appears immediately without a page reload
  - Action: Save a valid transaction, then open the transaction history and monthly summary.
  - Expected: The new transaction and its updated category totals appear without manually refreshing the page.

- [ ] IX-04: Clearing filters restores the full transaction history
  - Action: Apply a date or category filter, then click "Clear filters" (or equivalent reset control).
  - Expected: The complete default transaction history is displayed again.

## Content
- [ ] CT-01: Transaction history entries display complete, relevant details
  - Action: Inspect the entries in the transaction history.
  - Expected: Each entry shows date, description, amount, and assigned category, consistent with the logged data.

- [ ] CT-02: Category filter options match the expense categories defined in the profile
  - Action: Open the category filter in the transaction history and compare its options against the profile's expense category list.
  - Expected: The filter lists exactly the defined expense categories — no missing or extra options.

- [ ] CT-03: Summary figures are arithmetically correct
  - Action: For one category, sum its displayed transactions for the current month and compare with the summary's actual-spending figure.
  - Expected: The summary's actual-spending amount equals the sum of that category's transactions for the month.