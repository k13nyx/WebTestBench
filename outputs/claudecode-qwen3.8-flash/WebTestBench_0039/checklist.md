# Test Checklist

## Functionality
- [ ] FT-01: User can create a profile containing income sources
  - Action: Open the profile page, add an income source (e.g., "Salary", amount 5000) and save.
  - Expected: The income source "Salary — $5,000" is listed in the profile after saving.

- [ ] FT-02: User can create expense categories with a monthly budget
  - Action: Add a new expense category "Groceries" with monthly budget $400 and save.
  - Expected: "Groceries" appears in the category list showing budget $400.

- [ ] FT-03: User can create savings goals
  - Action: Add a savings goal "Emergency Fund" with target amount $6,000 and save.
  - Expected: Goal "Emergency Fund — $6,000" is displayed in the savings goals section.

- [ ] FT-04: User can log a transaction and assign it to a category
  - Action: Log a transaction (date: current month, amount $50, description "Supermarket") assigned to category "Groceries" and submit.
  - Expected: The transaction appears in history with amount $50 and category "Groceries".

- [ ] FT-05: Monthly summary compares actual spending to budget per category
  - Action: Open the Monthly Summary for the current month.
  - Expected: Each expense category shows both "Spent" (actual) and "Budget" values, e.g., Groceries: $150 of $400.

- [ ] FT-06: Overspending categories are highlighted in the summary
  - Action: Open the Monthly Summary for a month where default data has a category whose actual spending exceeds its budget.
  - Expected: That category row/card is visually flagged (e.g., red text/badge "Over budget" or a warning icon) and other categories are not.

- [ ] FT-07: Transaction history can be filtered by date range
  - Action: In Transaction History, set a start and end date covering only part of the default transactions and apply.
  - Expected: Only transactions dated within that range are listed; all others disappear.

- [ ] FT-08: Transaction history can be filtered by category
  - Action: Select a single existing category in the category filter and apply.
  - Expected: Only transactions belonging to that category are listed.

- [ ] FT-09: Date range and category filters combine
  - Action: Apply both a date range and a category filter at the same time.
  - Expected: Result list contains only transactions matching BOTH criteria (intersection, not union).

## Constraint
- [ ] CS-01: Transaction cannot be saved with missing or invalid fields
  - Action: Submit the add-transaction form with no amount, and separately with a non-numeric/negative amount, and with no category selected.
  - Expected: Submission is blocked and a validation message names the offending field; no new row appears in history.

- [ ] CS-02: Transactions can only be assigned to defined categories
  - Action: Open the category selector on the add-transaction form.
  - Expected: Only categories defined in the profile are selectable; there is no free-text entry that accepts an undefined category name.

- [ ] CS-03: Categories within budget are never marked as overspending
  - Action: Check a category in the Monthly Summary whose actual spending is less than or equal to its budget.
  - Expected: It shows no "Over budget" flag/highlight and is shown as remaining/under budget.

- [ ] CS-04: Invalid date range is rejected or handled
  - Action: Set the filter start date later than the end date and apply.
  - Expected: Either a message states the range is invalid, or the filter shows no transactions — the page must not crash or silently show all transactions.

## Interaction
- [ ] IX-01: Saving a transaction produces confirmation and updates lists
  - Action: Log a valid transaction and observe the interface after submit.
  - Expected: A success confirmation (toast/message) is shown, the form clears, and the new transaction appears in the history list without re-creating data.

- [ ] IX-02: New profile category becomes available immediately
  - Action: Create a new expense category in the profile, then open the add-transaction form and the Monthly Summary.
  - Expected: The new category appears as an option in the transaction form and as a row with $0 spent in the summary.

- [ ] IX-03: Applying or clearing filters updates the list in place
  - Action: Apply a category filter, then reset/clear it.
  - Expected: The history list re-renders to the filtered set and then back to the full default set; a "no results" state is shown if a filter matches nothing.

## Content
- [ ] CT-01: Summary figures are consistent with logged transactions
  - Action: Compare the "Spent" amount for each category in the Monthly Summary against the sum of that category's transactions for the same month in history.
  - Expected: The two values match exactly for every category (no unaccounted or double-counted transactions).

- [ ] CT-02: Transaction rows display complete, correct data
  - Action: Inspect the columns of the default transactions in history.
  - Expected: Every row shows date, amount, description, and category, with no blank/placeholder values such as "null", "TBD", or "Lorem ipsum".

- [ ] CT-03: Savings goals show progress toward the target
  - Action: Open the savings goals section.
  - Expected: Each goal shows its name, target amount, and a progress indicator or remaining amount that is relevant to budgeting (not generic filler text).