# Test Checklist

## Functionality
- [ ] FT-01: User can add an income source to their profile
  - Action: Open the default profile page, locate the "Income Sources" section, click "Add Income Source", enter a source name (e.g. "Freelance") and a monthly amount (e.g. 500), then save.
  - Expected: The new income source appears in the Income Sources list with its name and amount, and the profile's total monthly income updates to include it.

- [ ] FT-02: User can add an expense category with a monthly budget
  - Action: In the "Expense Categories" section, click "Add Category", enter a name (e.g. "Transport") and a monthly budget amount (e.g. 200), then save.
  - Expected: The category appears in the Expense Categories list showing its name and budget amount (200).

- [ ] FT-03: User can create a savings goal with a target amount
  - Action: In the "Savings Goals" section, click "Add Goal", enter a goal name (e.g. "Emergency Fund") and a target amount (e.g. 5000), then save.
  - Expected: The goal appears in the Savings Goals list with its name, target amount, and a current saved amount (starting at 0 or its existing value).

- [ ] FT-04: User can log a transaction and assign it to an existing expense category
  - Action: Open the transaction entry form, enter an amount (e.g. 45), a date within the current month, a description (e.g. "Bus pass"), select an existing category from the category dropdown, and submit.
  - Expected: A success confirmation appears and the new transaction appears in the transaction history list with its date, description, amount, and the selected category name.

- [ ] FT-05: Monthly summary shows budget vs. actual spending for every expense category
  - Action: Open the "Monthly Summary" view for the current month.
  - Expected: Every expense category defined in the profile is listed with three values: its monthly budget, its actual spending for the month, and the remaining amount (or spent/budget comparison).

- [ ] FT-06: Monthly summary totals income and spending correctly against logged transactions
  - Action: Note the total of all income sources and the sum of all transaction amounts dated in the current month, then compare with the totals shown in the Monthly Summary.
  - Expected: Summary "Total Income" equals the sum of income source amounts, and "Total Spending" equals the sum of logged transactions for that month.

- [ ] FT-07: Savings goal progress reflects amounts assigned to it
  - Action: Log a transaction assigned to the savings goal (or use an existing default savings transaction), then open the Savings Goals section.
  - Expected: The goal's current saved amount increases by the logged amount, and a progress indicator (e.g. "X of Y" or a percentage) matches current/target.

- [ ] FT-08: User can filter transaction history by category
  - Action: On the transaction history view, select one existing category (e.g. "Groceries") in the "Category" filter and apply the filter.
  - Expected: Only transactions assigned to that category are displayed; every visible row's category column matches the selected category, and no other categories appear.

- [ ] FT-09: User can filter transaction history by date range
  - Action: Set the "From" date to the first day of last month and the "To" date to the last day of last month, then apply the filter.
  - Expected: The history list shows only transactions with dates inside the selected range; every visible row's date falls between From and To inclusive.

## Constraint
- [ ] CS-01: Transaction cannot be saved without an amount and a category
  - Action: Open the transaction form, leave the amount field empty and the category unselected, and submit.
  - Expected: Submission is blocked, a validation message is shown for the amount and the category, and no new row is added to the transaction history.

- [ ] CS-02: Transaction rejects zero, negative, and non-numeric amounts
  - Action: Attempt to submit a transaction with amount "0", then with "-50", then with "abc".
  - Expected: Each attempt is rejected with a validation message; no transaction is created and the history list is unchanged.

- [ ] CS-03: Expense category cannot be created with a blank name or negative budget
  - Action: Click "Add Category", leave the name blank and enter a budget of "-100", then save. Repeat with a valid name and a blank budget.
  - Expected: Both attempts are blocked with a validation message; no invalid category is added to the Expense Categories list.

- [ ] CS-04: Invalid date range (start after end) is prevented or reported
  - Action: Set the filter "From" date to a later date than the "To" date and apply the filter.
  - Expected: Either the filter is blocked with a clear message (e.g. "Start date must be before end date"), or the history shows an explicit empty state; the app does not crash or display an unfiltered list.

- [ ] CS-05: Filtering that matches no transactions shows an empty state, not an error
  - Action: Apply a category and date range combination that contains no transactions (e.g. a category with no entries in a past month).
  - Expected: The transaction list shows a clear "No transactions found" (or equivalent) message with zero rows, and the filter controls remain usable.

## Interaction
- [ ] IX-01: Overspent categories are visually highlighted in the monthly summary
  - Action: In the Monthly Summary, identify a category whose actual spending exceeds its budget (log an extra transaction if none exists), then view that row.
  - Expected: That row is visually distinguished from on-budget rows (e.g. red text/background and/or an "Over Budget" / "Overspent" label), while categories within budget are not highlighted.

- [ ] IX-02: Success confirmation appears after a transaction is logged
  - Action: Submit a valid transaction.
  - Expected: A confirmation message (e.g. "Transaction added") appears immediately, and the form is cleared or reset for the next entry.

- [ ] IX-03: Applying filters updates the history list without a page reload
  - Action: With the transaction history open, change the category filter and apply it.
  - Expected: The visible transaction rows update in place to the filtered set; the page does not reload and the previously selected filter values remain shown in the controls.

- [ ] IX-04: Clearing filters restores the full transaction history
  - Action: After applying a category and date range filter, click the "Clear" / "Reset" filters control.
  - Expected: All filter inputs return to their default state and the full, unfiltered transaction history is displayed again.

## Content
- [ ] CT-01: All currency amounts are displayed with a consistent, correct currency format
  - Action: Inspect amounts shown in Income Sources, Expense Categories, Monthly Summary, Savings Goals, and the transaction history.
  - Expected: Every amount uses the same currency symbol and decimal formatting (e.g. "$1,200.00"), and none appear blank, as "NaN", or as "undefined".

- [ ] CT-02: Summary and history labels match the profile's actual categories, goals, and income sources
  - Action: Compare the category names listed in the Monthly Summary and the category filter dropdown against the Expense Categories defined in the profile; do the same for savings goals.
  - Expected: Names match exactly with no duplicates, no missing entries, and no sample/placeholder names (e.g. "Category 1", "Foo", "Lorem ipsum").

- [ ] CT-03: All page text is budgeting-specific and free of placeholder content
  - Action: Read all headings, section titles, button labels, and empty-state messages across the profile, summary, and history pages.
  - Expected: All text relates to budgeting (income, expenses, categories, budget, savings goals, transactions, filters); no lorem ipsum, "TODO", or generic template text is present.