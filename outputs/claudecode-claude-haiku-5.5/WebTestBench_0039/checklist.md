# Test Checklist

## Functionality
- [ ] FT-01: Add an income source to the profile
  - Action: Open the Profile page, click "Add Income Source", enter a name and a monthly amount, then click "Save".
  - Expected: The new income source appears in the Income Sources list with the entered name and amount, and it persists after a page reload.
- [ ] FT-02: Add an expense category with a monthly budget
  - Action: On the Profile page, click "Add Expense Category", enter a name and a monthly budget, then click "Save".
  - Expected: The category appears in the Expense Categories list with the budget shown.
- [ ] FT-03: Add a savings goal
  - Action: On the Profile page, click "Add Savings Goal", enter a name and a target amount, then click "Save".
  - Expected: The goal appears in the Savings Goals list with its name and target amount.
- [ ] FT-04: Log a transaction and assign it to a category
  - Action: Click "Add Transaction", enter amount, date, and description, select an existing expense category, then click "Save".
  - Expected: The transaction appears in the Transaction History with the correct amount, date, description, and assigned category.
- [ ] FT-05: Monthly summary shows budget, actual, and remaining per category
  - Action: Open the "Monthly Summary" page and select the current month that has default transactions.
  - Expected: Each expense category row shows its Budget, Actual Spent, and Remaining (Budget minus Actual) values.
- [ ] FT-06: Filter transaction history by date range
  - Action: In Transaction History, set "From" and "To" dates covering only part of the default data, then click "Apply".
  - Expected: Only transactions dated within the range (inclusive) are listed.
- [ ] FT-07: Filter transaction history by category
  - Action: In Transaction History, select one category in the "Category" filter, then click "Apply".
  - Expected: Only transactions assigned to that category are listed.
- [ ] FT-08: Clear filters restores full history
  - Action: Apply a date range and a category filter, then click "Clear Filters".
  - Expected: Both filter fields reset to empty and the full transaction history is displayed.

## Constraint
- [ ] CS-01: Transaction requires amount, date, and category
  - Action: Click "Add Transaction", leave the amount blank, and click "Save". Repeat with the category left unselected and then with the date cleared.
  - Expected: Each attempt is blocked with a required-field message on the missing field, and no transaction is added to the history.
- [ ] CS-02: Transaction amount must be a positive number
  - Action: In the Add Transaction form, enter "-20" in Amount and click "Save". Then enter "abc".
  - Expected: Both entries are rejected with a validation message, and the transaction is not saved.
- [ ] CS-03: Date range filter rejects start date later than end date
  - Action: In Transaction History, set "From" to a date after the "To" date and click "Apply".
  - Expected: A validation message appears, and the transaction list is not filtered to an invalid range.
- [ ] CS-04: Duplicate category names are rejected
  - Action: On the Profile page, click "Add Expense Category" and enter the exact name of an existing default category, then click "Save".
  - Expected: The save is blocked with a message indicating the category name already exists, and no duplicate appears in the list.
- [ ] CS-05: Budget and savings goal amounts must be positive
  - Action: Click "Add Expense Category" and enter "0" as the budget and click "Save". Repeat for "Add Savings Goal" with target amount "-500".
  - Expected: Each save is blocked with a validation message, and no entry is created.

## Interaction
- [ ] IX-01: Success message and form reset after saving a transaction
  - Action: Add a valid transaction using "Add Transaction" and click "Save".
  - Expected: A success message (toast) appears confirming the transaction was saved, and the form fields clear or the form closes.
- [ ] IX-02: Overspent categories are visually highlighted
  - Action: Open the Monthly Summary for the month with default data and compare the category rows.
  - Expected: Each category where Actual Spent exceeds Budget shows a visible highlight (red color and an "Over budget" label with the overspent amount). Categories at or under budget show no highlight.
- [ ] IX-03: Filter results update immediately with a record count
  - Action: In Transaction History, apply a category filter and then a date range filter.
  - Expected: The list refreshes without a page reload, and a count label (for example, "Showing X transactions") matches the number of rows displayed.
- [ ] IX-04: Validation errors clear when the input is corrected
  - Action: Click "Save" on an invalid Add Transaction form to trigger the error, then correct the amount to a positive number and click "Save" again.
  - Expected: The error message next to the amount field disappears once the value is valid, and the save succeeds.

## Content
- [ ] CT-01: Summary actual amounts match the transactions
  - Action: For one expense category on the Monthly Summary, note the Actual Spent value. Then filter Transaction History to the same category and month and add up the amounts listed.
  - Expected: The sum of the filtered transaction amounts equals the Actual Spent value shown in the summary.
- [ ] CT-02: Filtered history contains only matching records
  - Action: Apply a date range and category filter together in Transaction History, then check every listed row.
  - Expected: Every row has a date within the selected range and the selected category. No non-matching rows appear.
- [ ] CT-03: Category options match the profile categories
  - Action: Open the Category dropdown in the Add Transaction form and the Category filter in Transaction History. Compare them to the Expense Categories list on the Profile page.
  - Expected: Both dropdowns list exactly the same expense categories as the profile, with no missing, stale, or misspelled entries.
- [ ] CT-04: Summary categories and labels are relevant to the budgeting content
  - Action: Review the default categories, income sources, and savings goals on the Profile page and the Monthly Summary page.
  - Expected: All labels, category names, and summary headings are budgeting-related with no placeholder text (such as "Lorem ipsum" or "Item 1") and no broken labels.