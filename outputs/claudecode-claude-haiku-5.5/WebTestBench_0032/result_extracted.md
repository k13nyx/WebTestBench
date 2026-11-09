# Test Result

## Functionality

- [ ] FT-01: User can view all default financial goals and monthly budgets.
  - Action: Open the Goals and Budgets section.
  - Expected: Every default goal shows its name, target amount, and progress. Every default monthly budget shows its category, limit, and month.
  - Bug Report:
    - Issue: Incomplete Data Display
    - Actual: There is no single "Goals and Budgets" section; the page has "Budget Categories" and "Financial Goals". Goals show name, "Progress" amount and "Remaining" amount (e.g. Summer Vacation: Progress $1850.00, Remaining $1150.00), but no target amount is displayed. Budgets show category and limit ("$0.00 of $600.00" for Food & Dining) but no month.

- [ ] FT-02: Expense list shows all default expenses with their core fields.
  - Action: Open the Expenses list with no filters applied.
  - Expected: Every default expense row shows date, description, amount, category, and goal. The row count matches the default data.
  - Bug Report:
    - Issue: Missing Goal Field
    - Actual: 20 default rows appear, plus one test row I saved during CS-02 (so 21 total). Date, description, amount and category show on every row. Goal shows on only 2 rows (Flight booking and Hotel deposit), where it is run into the category text with no label: "TravelSummer Vacation". The other 18 rows show no goal value at all.

- [X] FT-03: Add Expense form offers multiple currencies.
  - Action: Click "Add Expense" and open the Currency dropdown. Close the form without saving.
  - Expected: The dropdown lists at least 3 currencies, each with its code and name. No expense is saved.

  Note: this item is marked FAIL below; the corrected status is in the Bug Report block.

- [ ] FT-03: Add Expense form offers multiple currencies.
  - Action: Click "Add Expense" and open the Currency dropdown. Close the form without saving.
  - Expected: The dropdown lists at least 3 currencies, each with its code and name. No expense is saved.
  - Bug Report:
    - Issue: Missing Currency Name
    - Actual: The dropdown lists 8 currencies (USD, EUR, GBP, JPY, CAD, AUD, CHF, MXN), each shown only as symbol and code (e.g. "€ EUR", "$ USD"). No currency name is shown. Closing the form saved nothing.

- [X] FT-04: Selecting a primary currency converts all summaries to that currency.
  - Action: Note the current primary currency. Open Settings, select a different currency, and save. Check the dashboard totals. Restore the original currency afterward.
  - Expected: All dashboard totals, budget figures, and goal amounts display in the newly selected currency with its symbol.

  Note: there is no Settings screen. The primary currency is changed from the header dropdown. Switching USD → EUR converted Total Spent ($1659.00 → €1526.28), Monthly Budget, Remaining, Daily Average, category budgets, goal amounts and chart axes to €. The currency was restored to USD afterward.

- [X] FT-05: Date range filter shows only expenses within the range.
  - Action: Set "From" and "To" dates that cover part of the default expense dates. Click "Apply".
  - Expected: Only expenses dated within the range (inclusive) appear. Expenses outside the range are hidden.

  Note: there is no Apply button. Filters apply on change. With From 2024-11-26 and To 2024-12-05, exactly the 10 expenses dated Nov 26 – Dec 5, 2024 appeared, including both endpoints.

- [X] FT-06: Category filter shows only expenses in the selected category.
  - Action: Select one category in the Category filter and apply it.
  - Expected: Only expenses assigned to that category appear.

  Note: selecting "✈️ Travel" showed only Flight booking and Hotel deposit.

- [X] FT-07: Goal filter shows only expenses linked to the selected goal.
  - Action: Select one goal in the Goal filter and apply it.
  - Expected: Only expenses linked to that goal appear.

  Note: selecting "Summer Vacation" showed only Flight booking and Hotel deposit.

- [X] FT-08: Combined filters return the intersection of all criteria.
  - Action: Set a date range, one category, and one goal together. Apply the filters.
  - Expected: Only expenses matching all three criteria appear. Each visible row matches every selected filter.

  Note: date range Nov 25–30, 2024 + Travel + Summer Vacation showed exactly one row, Hotel deposit (Nov 25, 2024, $200.00).

- [ ] FT-09: "Budget vs. Spending by Category" chart matches the default data.
  - Action: Open the category comparison chart. Compare each category's bars to the budget limit and the expense total for that category in the default data.
  - Expected: Each category shows a budget bar and a spending bar. The values match the budgets and expense totals for the displayed period.
  - Bug Report:
    - Issue: Default Data Not Reflected / Missing Spending Bars
    - Actual: The chart shows only one bar per category (the budget), with no spending bars rendered. Every spending value is $0. Hovering Utilities gives the tooltip "Spent: $0.00, Budget: $250.00". None of the 20 default expenses (dated Nov 24 – Dec 12, 2024) appear in the chart, and no period selector or period label exists, so the category totals in the default data cannot be matched.

- [ ] FT-10: "Spending Over Time" chart matches the default expense data.
  - Action: Open the spending-over-time chart. Compare each period's value to the sum of that period's expenses in the expense list.
  - Expected: Each period's point or bar matches the expense total for that period, in the primary currency.
  - Bug Report:
    - Issue: Default Data Not Reflected
    - Actual: The chart covers only the last 14 days (Oct 28 – Nov 9, 2026). Every point is $0.00 (hover on Nov 2 shows "$0.00"). None of the default expenses fall in this window, so the chart does not reflect the default expense data. No period selector is available.

## Constraint

- [ ] CS-01: Expense cannot be saved with required fields empty.
  - Action: Open "Add Expense", leave Amount, Category, Currency, and Date blank, and click "Save".
  - Expected: The form is not saved. Each empty required field shows an error message. No new row appears in the expense list.
  - Bug Report:
    - Issue: Missing Validation Messages
    - Actual: Clicking "Add Expense" with Description, Amount and Category empty did not save anything, and no new row appeared. No error message appeared for any empty field; the dialog stayed open with no error text. Note: Currency defaults to "$ USD" and Date defaults to 2026-11-09, so those two could not be left blank without manual clearing, which I did not test.

- [ ] CS-02: Expense amount must be a positive number.
  - Action: Open "Add Expense", enter "-5" in Amount, fill the other required fields, and click "Save". Repeat with "0" and "abc".
  - Expected: Each attempt is rejected with an error such as "Amount must be greater than zero" or "Enter a valid number". No expense is saved.
  - Bug Report:
    - Issue: Invalid Amount Accepted
    - Actual: "0" was accepted and saved as an expense ("QA negative test", Food & Dining, $0.00, Nov 9, 2026). "-5" was blocked only by the browser's native validation ("Value must be greater than or equal to 0."), with no in-page message. "abc" cannot be entered in the number field (it stays empty), and submission was blocked with no visible error text.

- [ ] CS-03: Date range filter rejects a start date later than the end date.
  - Action: Set "From" to a date after "To" and click "Apply".
  - Expected: An error such as "Start date must be before end date" appears. The list does not show results for the invalid range.
  - Bug Report:
    - Issue: Missing Error Message
    - Actual: With From = 2024-12-10 and To = 2024-12-01, the list shows 0 rows, but no error text such as "Start date must be before end date" appears anywhere on the page.

- [X] CS-04: Changing the primary currency does not alter stored expenses.
  - Action: Note the amount and currency code of several default expenses. Change the primary currency, then return to the expense list. Restore the original currency afterward.
  - Expected: Each expense still shows its original amount and currency code. Only the summaries change.

  Note: with EUR as primary, the original amounts stayed in place (Grocery shopping $85.50; Coffee shop €12.50; Train ticket €35.00; Lunch £18.50). Only the converted primary figures changed.

## Interaction

- [ ] IX-01: Result count updates after every filter change.
  - Action: Apply a date range, then a category, then a goal, and observe the result label.
  - Expected: The label (for example, "Showing X of Y expenses") updates to match the visible rows after each change.
  - Bug Report:
    - Issue: Missing Result Count Label
    - Actual: No result-count label (such as "Showing X of Y expenses") appears in the expense section before or after the date, category or goal filters were applied.

- [X] IX-02: Hovering a chart bar shows a tooltip with its details.
  - Action: Hover over one category bar in "Budget vs. Spending by Category" and one point in "Spending Over Time".
  - Expected: A tooltip appears showing the category or period name and its values in the primary currency.

  Note: the category tooltip showed "Utilities – Spent: $0.00 – Budget: $250.00". The trend tooltip showed "Nov 2 – $0.00".

- [X] IX-03: "Clear" resets all filters and restores the full list.
  - Action: Apply a date range, category, and goal. Click "Clear" or "Reset Filters".
  - Expected: All filter fields return to their default values. The expense list shows all default expenses again, and the result count matches the full total.

  Note: after Clear, Category = "All categories", Goal = "All", both date fields are empty, and all 21 rows (20 default + 1 test row) are shown.

## Content

- [ ] CT-01: Category labels are meaningful and consistent.
  - Action: Review the category names in the expense list, filter dropdown, and both charts.
  - Expected: Each category uses the same name in every location. No label is blank, generic, or reads "undefined".
  - Bug Report:
    - Issue: Category Labels Missing in Chart
    - Actual: The "Budget vs Spending" chart's category axis shows emoji only (🍽️ 🚗 🛍️ 🎬 💡 🏥 ✈️ 📦) and no names. Names ("Food & Dining", "Transportation", …) appear only in the chart tooltip, the budget list, the expense list and the filter dropdown.

- [X] CT-02: Each expense amount shows the currency it was logged in.
  - Action: Review the amount column in the expense list for default expenses in different currencies.
  - Expected: Each amount displays the correct symbol or code for its original currency (for example, a EUR expense shows "€" or "EUR", not the primary currency).

  Note: Coffee shop shows "$13.59" with its original "€12.50"; Train ticket shows "$38.04" with "€35.00"; Lunch shows "$23.42" with "£18.50".

- [X] CT-03: No placeholder or error text appears on any page.
  - Action: Review the dashboard, goals, budgets, expense list, and both charts.
  - Expected: No visible text reads "undefined", "NaN", "null", "lorem ipsum", or "TODO". No chart shows an empty or broken label.

  Note: a DOM text scan found none of those strings, and no chart axis label was empty. Separate from this check, the list text "TravelSummer Vacation" (category and goal run together) is noted under FT-02.
