# Test Result

## Functionality
- [X] FT-01: User can add an income source to their profile
  - Action: Open the profile page, add an income source (e.g., "Salary" with amount), and save.
  - Expected: The income source is saved and listed under the profile's income sources.
- [X] FT-02: User can add an expense category with a monthly budget
  - Action: Add an expense category (e.g., "Groceries") with a monthly budget amount and save.
  - Expected: The category appears in the expense category list showing its budget amount.
- [X] FT-03: User can add a savings goal
  - Action: Add a savings goal (e.g., "Emergency Fund") with a target amount and save.
  - Expected: The goal is saved and displayed in the savings goals section.
- [X] FT-04: User can log a transaction assigned to a category
  - Action: Create a transaction with a date, amount (e.g., 50), and category "Groceries", then submit.
  - Expected: The transaction is saved and appears in the transaction history with the entered details.
- [ ] FT-05: Monthly summary compares actual spending to budget for each category
  - Action: Open the monthly summary for the current month.
  - Expected: Each expense category row displays its budgeted amount, actual spent amount, and the difference between them.
  - Bug Report:
    - Issue: Missing Element (difference value not displayed per category row)
    - Actual: Budget Overview (November 2026) rows show only two values, e.g. "Housing | $0 / $1,500", "Food & Dining | $0 / $600" — budgeted and actual amounts are shown, but no difference (e.g. "$1,500 remaining") appears for any under-budget category. Only the over-budget row displays a difference ("Over budget by $20" for Groceries).
- [X] FT-06: Transaction history can be filtered by date range
  - Action: Set a start date and end date in the history filters and apply.
  - Expected: Only transactions dated within the selected range are listed.
- [X] FT-07: Transaction history can be filtered by category
  - Action: Select a category (e.g., "Groceries") in the history filter and apply.
  - Expected: Only transactions assigned to that category are listed.
- [X] FT-08: Date range and category filters work together
  - Action: Apply a date range filter and a category filter simultaneously.
  - Expected: Only transactions that fall within the date range AND belong to the selected category are listed.

## Constraint
- [ ] CS-01: Transaction cannot be submitted with empty required fields
  - Action: Leave the amount and/or category field empty and attempt to submit the transaction.
  - Expected: Submission is blocked with a validation error, and no transaction is created.
  - Bug Report:
    - Issue: Missing validation error message (silent blocking only)
    - Actual: With amount and/or category empty the "Add Transaction" button is simply disabled, so clicking/Enter does nothing and no transaction is created — but no validation error message is ever displayed (dialog innerText and toast region remain empty). Additionally, the form's submit handler performs no validation of its own: a forced form submission with an empty amount created a "-$0" transaction with an empty description (subsequently deleted during cleanup).
- [ ] CS-02: Negative or non-numeric transaction amounts are rejected
  - Action: Enter a negative amount (e.g., -20) or non-numeric text in the amount field and submit.
  - Expected: A validation error is shown and the transaction is not saved.
  - Bug Report:
    - Issue: Missing validation error message for invalid amounts
    - Actual: Entering "-20" keeps the "Add Transaction" button disabled (no error text appears anywhere; no toast), and non-numeric text cannot be entered at all (input type=number silently ignores it, value stays empty). The transaction is indeed not saved, but no validation error message is shown as required.
- [ ] CS-03: Date range filter rejects an invalid range
  - Action: Set the start date later than the end date and apply the filter.
  - Expected: A validation error is shown (or the range is corrected); the system never displays results for an impossible range.
  - Bug Report:
    - Issue: Invalid date range silently accepted (no validation error, no correction)
    - Actual: With "From date" = 2026-11-10 and "To date" = 2026-11-01 the values remain unchanged (not corrected), no validation error or warning message/toast appears, and the list simply shows "No transactions match your filters" — the impossible range is never flagged to the user.

## Interaction
- [X] IX-01: Overspending is highlighted in the monthly summary
  - Action: Ensure one category's actual spending exceeds its budget, then view the monthly summary.
  - Expected: The over-budget category is visually highlighted (e.g., red indicator or "Over budget" label); under-budget categories are not highlighted.
- [X] IX-02: Monthly summary updates after a transaction is logged
  - Action: Note a category's "actual spent" value, log a new transaction in that category, then view the monthly summary.
  - Expected: The category's actual spent amount reflects the new transaction (increased by its amount).
- [X] IX-03: Clearing filters restores the full transaction list
  - Action: Apply date/category filters, then clear/reset the filters.
  - Expected: The complete, unfiltered transaction history is displayed again.

## Content
- [X] CT-01: Transaction history entries show complete, accurate details
  - Action: Review the transaction history list.
  - Expected: Each entry displays its date, amount, and assigned category name, matching the values entered when logged.
- [X] CT-02: Monthly summary categories match the profile's expense categories
  - Action: Compare the categories listed in the monthly summary with the expense categories in the profile.
  - Expected: The same category names and budget amounts appear in both places.
- [X] CT-03: Savings goals display accurate target and progress data
  - Action: Review the savings goals section.
  - Expected: Each goal shows its name, target amount, and current saved amount consistent with the data entered.
