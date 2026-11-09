# Test Checklist

## Functionality
- [ ] FT-01: User can add an income source to their profile
  - Action: Open the profile page, add an income source (e.g., "Salary" with amount), and save.
  - Expected: The income source is saved and listed under the profile's income sources.

- [ ] FT-02: User can add an expense category with a monthly budget
  - Action: Add an expense category (e.g., "Groceries") with a monthly budget amount and save.
  - Expected: The category appears in the expense category list showing its budget amount.

- [ ] FT-03: User can add a savings goal
  - Action: Add a savings goal (e.g., "Emergency Fund") with a target amount and save.
  - Expected: The goal is saved and displayed in the savings goals section.

- [ ] FT-04: User can log a transaction assigned to a category
  - Action: Create a transaction with a date, amount (e.g., 50), and category "Groceries", then submit.
  - Expected: The transaction is saved and appears in the transaction history with the entered details.

- [ ] FT-05: Monthly summary compares actual spending to budget for each category
  - Action: Open the monthly summary for the current month.
  - Expected: Each expense category row displays its budgeted amount, actual spent amount, and the difference between them.

- [ ] FT-06: Transaction history can be filtered by date range
  - Action: Set a start date and end date in the history filters and apply.
  - Expected: Only transactions dated within the selected range are listed.

- [ ] FT-07: Transaction history can be filtered by category
  - Action: Select a category (e.g., "Groceries") in the history filter and apply.
  - Expected: Only transactions assigned to that category are listed.

- [ ] FT-08: Date range and category filters work together
  - Action: Apply a date range filter and a category filter simultaneously.
  - Expected: Only transactions that fall within the date range AND belong to the selected category are listed.

## Constraint
- [ ] CS-01: Transaction cannot be submitted with empty required fields
  - Action: Leave the amount and/or category field empty and attempt to submit the transaction.
  - Expected: Submission is blocked with a validation error, and no transaction is created.

- [ ] CS-02: Negative or non-numeric transaction amounts are rejected
  - Action: Enter a negative amount (e.g., -20) or non-numeric text in the amount field and submit.
  - Expected: A validation error is shown and the transaction is not saved.

- [ ] CS-03: Date range filter rejects an invalid range
  - Action: Set the start date later than the end date and apply the filter.
  - Expected: A validation error is shown (or the range is corrected); the system never displays results for an impossible range.

## Interaction
- [ ] IX-01: Overspending is highlighted in the monthly summary
  - Action: Ensure one category's actual spending exceeds its budget, then view the monthly summary.
  - Expected: The over-budget category is visually highlighted (e.g., red indicator or "Over budget" label); under-budget categories are not highlighted.

- [ ] IX-02: Monthly summary updates after a transaction is logged
  - Action: Note a category's "actual spent" value, log a new transaction in that category, then view the monthly summary.
  - Expected: The category's actual spent amount reflects the new transaction (increased by its amount).

- [ ] IX-03: Clearing filters restores the full transaction list
  - Action: Apply date/category filters, then clear/reset the filters.
  - Expected: The complete, unfiltered transaction history is displayed again.

## Content
- [ ] CT-01: Transaction history entries show complete, accurate details
  - Action: Review the transaction history list.
  - Expected: Each entry displays its date, amount, and assigned category name, matching the values entered when logged.

- [ ] CT-02: Monthly summary categories match the profile's expense categories
  - Action: Compare the categories listed in the monthly summary with the expense categories in the profile.
  - Expected: The same category names and budget amounts appear in both places.

- [ ] CT-03: Savings goals display accurate target and progress data
  - Action: Review the savings goals section.
  - Expected: Each goal shows its name, target amount, and current saved amount consistent with the data entered.