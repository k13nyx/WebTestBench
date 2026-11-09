# Test Result

## Functionality
- [ ] FT-01: Add an income source to the profile
  - Action: Open the Profile page, click "Add Income Source", enter a name and a monthly amount, then click "Save".
  - Expected: The new income source appears in the Income Sources list with the entered name and amount, and it persists after a page reload.
  - Bug Report:
    - Issue: Data Not Persisted
    - Actual: Before reload, "Side Gig — $300 / monthly" appeared in the Income Sources list. After a page reload and reopening Profile > Income, the list shows only "Salary $5,500 / monthly" and "Freelance $800 / monthly"; "Side Gig" is gone.
- [X] FT-02: Add an expense category with a monthly budget
  - Action: On the Profile page, click "Add Expense Category", enter a name and a monthly budget, then click "Save".
  - Expected: The category appears in the Expense Categories list with the budget shown.
- [X] FT-03: Add a savings goal
  - Action: On the Profile page, click "Add Savings Goal", enter a name and a target amount, then click "Save".
  - Expected: The goal appears in the Savings Goals list with its name and target amount.
- [X] FT-04: Log a transaction and assign it to a category
  - Action: Click "Add Transaction", enter amount, date, and description, select an existing expense category, then click "Save".
  - Expected: The transaction appears in the Transaction History with the correct amount, date, description, and assigned category.
- [ ] FT-05: Monthly summary shows budget, actual, and remaining per category
  - Action: Open the "Monthly Summary" page and select the current month that has default transactions.
  - Expected: Each expense category row shows its Budget, Actual Spent, and Remaining (Budget minus Actual) values.
  - Bug Report:
    - Issue: Missing Remaining Values and Monthly Summary Page
    - Actual: No "Monthly Summary" page exists; the navigation has only Dashboard, Transactions, Budget, and Goals. The Budget page ("Budget Overview", November 2026) shows each category as "Actual / Budget" (for example, "$62.5 / $600" for Food & Dining) with no Remaining value on any row, and there is no month selector. The default transactions are dated December, which cannot be selected.
- [X] FT-06: Filter transaction history by date range
  - Action: In Transaction History, set "From" and "To" dates covering only part of the default data, then click "Apply".
  - Expected: Only transactions dated within the range (inclusive) are listed.
- [X] FT-07: Filter transaction history by category
  - Action: In Transaction History, select one category in the "Category" filter, then click "Apply".
  - Expected: Only transactions assigned to that category are listed.
- [X] FT-08: Clear filters restores full history
  - Action: Apply a date range and a category filter, then click "Clear Filters".
  - Expected: Both filter fields reset to empty and the full transaction history is displayed.

## Constraint
- [ ] CS-01: Transaction requires amount, date, and category
  - Action: Click "Add Transaction", leave the amount blank, and click "Save". Repeat with the category left unselected and then with the date cleared.
  - Expected: Each attempt is blocked with a required-field message on the missing field, and no transaction is added to the history.
  - Bug Report:
    - Issue: Silent Block Without Required-Field Message
    - Actual: With the amount blank and no category, the "Add Transaction" button is disabled and no required-field message appears. With the amount and description filled, no category selected, the button is disabled and no message appears. With a category selected and the date cleared, the button is still disabled and no message appears on the date field.
- [ ] CS-02: Transaction amount must be a positive number
  - Action: In the Add Transaction form, enter "-20" in Amount and click "Save". Then enter "abc".
  - Expected: Both entries are rejected with a validation message, and the transaction is not saved.
  - Bug Report:
    - Issue: Missing Validation Message for Negative Amount
    - Actual: Entering "-20" disables the "Add Transaction" button, so nothing is saved, but no validation message appears anywhere in the form. The Amount input is a native number field, so "abc" could not be entered as text and was not separately submitted.
- [ ] CS-03: Date range filter rejects start date later than end date
  - Action: In Transaction History, set "From" to a date after the "To" date and click "Apply".
  - Expected: A validation message appears, and the transaction list is not filtered to an invalid range.
  - Bug Report:
    - Issue: Invalid Date Range Accepted Without Message
    - Actual: With From = 2025-12-10 and To = 2025-12-05, no validation message appears, and the transaction list is filtered to zero rows.
- [ ] CS-04: Duplicate category names are rejected
  - Action: On the Profile page, click "Add Expense Category" and enter the exact name of an existing default category, then click "Save".
  - Expected: The save is blocked with a message indicating the category name already exists, and no duplicate appears in the list.
  - Bug Report:
    - Issue: Duplicate Category Created
    - Actual: Adding "Housing" with a budget of 100 succeeded with no message. Expense Categories now lists "Housing" twice (Budget: $1,500/mo and Budget: $100/mo), and the Add Transaction category dropdown also lists "Housing" twice.
- [ ] CS-05: Budget and savings goal amounts must be positive
  - Action: Click "Add Expense Category" and enter "0" as the budget and click "Save". Repeat for "Add Savings Goal" with target amount "-500".
  - Expected: Each save is blocked with a validation message, and no entry is created.
  - Bug Report:
    - Issue: Non-Positive Budget and Target Accepted
    - Actual: Category "Travel" with budget 0 was saved and shows "Budget: $0/mo". Savings goal "Negative Goal" with target -500 was saved and shows "of -$500" in the Savings Goals list. No validation message appeared in either case.

## Interaction
- [ ] IX-01: Success message and form reset after saving a transaction
  - Action: Add a valid transaction using "Add Transaction" and click "Save".
  - Expected: A success message (toast) appears confirming the transaction was saved, and the form fields clear or the form closes.
  - Bug Report:
    - Issue: Missing Success Toast
    - Actual: After saving "Team lunch" ($42.50), the dialog closed and the transaction appeared in the list, but no toast or notification element appeared. The notifications region was empty in the snapshot taken immediately after saving and again 300–500 ms later.
- [X] IX-02: Overspent categories are visually highlighted
  - Action: Open the Monthly Summary for the month with default data and compare the category rows.
  - Expected: Each category where Actual Spent exceeds Budget shows a visible highlight (red color and an "Over budget" label with the overspent amount). Categories at or under budget show no highlight.
- [ ] IX-03: Filter results update immediately with a record count
  - Action: In Transaction History, apply a category filter and then a date range filter.
  - Expected: The list refreshes without a page reload, and a count label (for example, "Showing X transactions") matches the number of rows displayed.
  - Bug Report:
    - Issue: Missing Record Count Label
    - Actual: With category "Food & Dining" and range 2025-12-02 to 2025-12-05, the list refreshed in place to 2 rows (Grocery shopping, Restaurant dinner), but no "Showing X transactions" label exists anywhere on the page.
- [ ] IX-04: Validation errors clear when the input is corrected
  - Action: Click "Save" on an invalid Add Transaction form to trigger the error, then correct the amount to a positive number and click "Save" again.
  - Expected: The error message next to the amount field disappears once the value is valid, and the save succeeds.
  - Bug Report:
    - Issue: No Inline Validation Error Shown
    - Actual: With amount -20, the "Save" button is disabled, so no error is triggered and no error message appears next to the amount field. After changing the amount to 20 and clicking "Save", the transaction saved and the dialog closed, but there was no error message to clear.

## Content
- [X] CT-01: Summary actual amounts match the transactions
  - Action: For one expense category on the Monthly Summary, note the Actual Spent value. Then filter Transaction History to the same category and month and add up the amounts listed.
  - Expected: The sum of the filtered transaction amounts equals the Actual Spent value shown in the summary.
- [X] CT-02: Filtered history contains only matching records
  - Action: Apply a date range and category filter together in Transaction History, then check every listed row.
  - Expected: Every row has a date within the selected range and the selected category. No non-matching rows appear.
- [ ] CT-03: Category options match the profile categories
  - Action: Open the Category dropdown in the Add Transaction form and the Category filter in Transaction History. Compare them to the Expense Categories list on the Profile page.
  - Expected: Both dropdowns list exactly the same expense categories as the profile, with no missing, stale, or misspelled entries.
  - Bug Report:
    - Issue: Non-Expense Entry in Category Filter
    - Actual: The Transaction History "All Categories" filter includes an "Income" option that is not in the profile's Expense Categories list. The Add Transaction dropdown does not include it. Both lists otherwise match the profile, including the duplicate "Housing" from CS-04.
- [X] CT-04: Summary categories and labels are relevant to the budgeting content
  - Action: Review the default categories, income sources, and savings goals on the Profile page and the Monthly Summary page.
  - Expected: All labels, category names, and summary headings are budgeting-related with no placeholder text (such as "Lorem ipsum" or "Item 1") and no broken labels.

---

**Execution notes**
- Several Action labels differ from the app. The income form is inline and its submit button reads "Add Income Source" (not "Save"). The category and goal forms also use "Add Category" and "Add Goal". The transaction filters apply on change, and there is no "Apply" or "Clear Filters" label (the button is "Clear filters"). I judged these by behavior rather than label.
- Test data created during the run: Side Gig, Pets, Housing (duplicate), Travel, Holiday Trip, Negative Goal, Team lunch, CS check, and Overspend test.
- Tool calls used: about 80 of the 100 budget.