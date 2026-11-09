# Test Result

## Functionality
- [ ] FT-01: The user can create several financial goals, each with a name and a target amount.
  - Action: Open the goal creation form and create two goals: "Vacation" with target 2000 and "New Laptop" with 1500.
  - Expected: Both goals are saved and listed in the Goals section with their names and target amounts.
  - Bug Report:
    - Issue: Missing Feature — No Goal Creation Form
    - Actual: The application has no goal creation UI. The only actions available anywhere on the page are "Add Expense", "Filters", and a currency selector (plus per-row delete icon buttons). The Financial Goals section only lists 3 fixed pre-seeded goals ("Summer Vacation", "Emergency Fund", "New Laptop") with no control to enter a goal name or target amount, so "Vacation" (2000) and "New Laptop" (1500) cannot be created.

- [ ] FT-02: The user can define monthly budgets per category.
  - Action: Open the budget creation form and create two budgets for the current month: "Groceries" 500 and "Transport" 200.
  - Expected: Both budgets are saved and listed in the Budgets section with their month, category, and amount.
  - Bug Report:
    - Issue: Missing Feature — No Budget Creation Form
    - Actual: The "Budget Categories" section shows 8 fixed pre-defined categories with fixed amounts (Food & Dining $600, Transportation $400, Shopping $300, Entertainment $200, Utilities $250, Health $150, Travel $500, Other $200). There is no form or control to define a budget with a month, category, and amount; no "Groceries" or "Transport" category exists and budgets cannot be created or edited.

- [X] FT-03: The user can log an expense with amount, date, currency, and category.
  - Action: Log an expense: amount 45, currency set to a currency different from the primary currency (e.g., EUR), category "Groceries", date today. (Adapted: the app has a fixed category list without "Groceries" — the equivalent "Food & Dining" category was used; goal "Summer Vacation" also assigned so the row could be inspected in CT-02.)
  - Expected: The expense is saved and appears in the expense list.

- [X] FT-04: The user can assign an expense to a financial goal.
  - Action: When logging an expense (amount 25, any valid currency, today's date), select the goal "Vacation" and a category. (Adapted: no "Vacation" goal exists and goals cannot be created — the pre-seeded goal "Summer Vacation" was used; category "Transportation".)
  - Expected: The expense is saved and the expense list shows it assigned to the goal "Vacation".

- [X] FT-05: The user can choose a primary currency, and all summaries are shown in that currency.
  - Action: Set the primary currency to USD via the primary currency selector, then open the summary section. (Verified by switching USD → EUR → USD.)
  - Expected: The setting is applied and every summary figure is displayed in USD.

- [X] FT-06: Expenses logged in other currencies are converted into the primary currency in summaries.
  - Action: With primary currency USD, view the summaries containing an expense logged in a different currency (e.g., the 45 EUR expense from FT-03).
  - Expected: The summary totals include that expense converted and displayed in USD.

- [X] FT-07: A chart shows spending compared to budget by category.
  - Action: With budgets and expenses in place (e.g., from FT-02 and FT-03), open the spending-vs-budget chart.
  - Expected: For each category with a budget, the chart shows both the budgeted amount and the actual spending of that category, in the primary currency.

- [ ] FT-08: A chart shows spending over time.
  - Action: With expenses dated across different periods, open the spending-over-time chart.
  - Expected: The chart shows total spending for each month that contains expenses, in the primary currency.
  - Bug Report:
    - Issue: Incorrect Chart Aggregation — over-time chart aggregates by day over a rolling window instead of by month
    - Actual: The only over-time chart is titled "Spending Trend (Last 14 Days)". It plots per-day spending for a rolling 14-day window with day labels ("Oct 28, Oct 30, Nov 1, … Nov 9"), not total spending per month. Expenses in Nov 2024 and Dec 2024 (e.g., "Grocery shopping" $85.50, Dec 12, 2024) are not shown at all; no month containing expenses is aggregated or labeled.

- [X] FT-09: The expense list can be filtered by date range.
  - Action: Set the date range filter to a range that contains only some of the existing expenses (e.g., the current month).
  - Expected: The list shows exactly the expenses dated within the range and excludes all expenses outside it.

- [X] FT-10: The expense list can be filtered by category.
  - Action: Select in the category filter a category that has expenses (e.g., "Groceries"). (Adapted: the fixed category "Food & Dining" was used; no "Groceries" category exists.)
  - Expected: The list shows only expenses whose category matches the selected one.

- [X] FT-11: The expense list can be filtered by goal.
  - Action: Select in the goal filter a goal that has expenses assigned (e.g., "Vacation"). (Adapted: the pre-seeded goal "Summer Vacation" was used.)
  - Expected: The list shows only expenses assigned to that goal; expenses with no goal or a different goal are excluded.

- [X] FT-12: Filters can be combined to narrow the expense list.
  - Action: Apply a date range filter and a category filter at the same time (e.g., current month + "Groceries"). (Adapted: current month + "Food & Dining".)
  - Expected: The list shows only expenses that match both filters simultaneously.

## Constraint
- [ ] CS-01: An expense cannot be saved with a missing, zero, or negative amount.
  - Action: Attempt to log an expense with the amount left blank, then with 0, then with -10 (other fields valid).
  - Expected: Each attempt is rejected with a validation message and no expense is added to the expense list.
  - Bug Report:
    - Issue: Insufficient Form Validation — zero amount is accepted and saved
    - Actual: Submitting with amount 0 was NOT rejected: an expense "CS-01 zero amount" with amount $0.00 was saved and added to the expense list. (Blank amount was rejected with toast "Missing fields — Please fill in all required fields." and -10 with field message "Value must be greater than or equal to 0.", neither adding an expense; only the zero-amount attempt fails the constraint.)

- [X] CS-02: An expense cannot be saved without a category.
  - Action: Fill in an expense (amount 25, currency, date) but leave the category unselected, then submit.
  - Expected: Submission is rejected with a validation message and no expense is added to the expense list.

- [ ] CS-03: Goals and budgets cannot be saved without a name or with a non-positive amount.
  - Action: Try to save a goal with an empty name; try to save a budget with amount 0; try to save a budget with amount -100.
  - Expected: Each attempt is rejected with a validation message and no goal or budget is added.
  - Bug Report:
    - Issue: Missing Feature — goal/budget creation UI absent, validation behavior cannot be exercised
    - Actual: The application provides no form to save a goal or a budget (only "Add Expense" exists; goals and budgets are fixed pre-seeded data), so the described attempts cannot be performed at all and no validation message for empty name / non-positive amounts can be observed.

- [ ] CS-04: An invalid date range cannot be applied to the expense filter.
  - Action: In the date range filter, set the end date earlier than the start date.
  - Expected: A validation error is shown and the invalid range is not applied (the expense list is unchanged).
  - Bug Report:
    - Issue: Missing Validation — invalid date range silently applied
    - Actual: With From = 2026-11-30 and To = 2026-11-01 (end before start), no validation error is shown anywhere in the filter panel, and the invalid range IS applied: the expense list became empty (0 rows) instead of remaining unchanged.

## Interaction
- [ ] IX-01: Saving an entry gives success feedback and the new entry appears immediately.
  - Action: Save a new goal, then a new budget, then a new expense, observing the UI after each save.
  - Expected: Each save displays a success confirmation and the new entry is immediately visible in its list without a page reload.
  - Bug Report:
    - Issue: Missing Feature — goal and budget saves cannot be performed
    - Actual: Only expense saving is possible: it does show an "Expense added" toast and the entry appears immediately in the list without reload (verified for 3 expenses). However, no UI exists to save a goal or a budget (see FT-01/FT-02), so their success feedback and immediate visibility cannot be observed; the expected behavior is only met for expenses.

- [X] IX-02: Summaries and charts refresh when spending data changes.
  - Action: Log one more expense, then view the summary figures and both charts without reloading the page.
  - Expected: The summary totals and both charts immediately include the newly logged expense.

## Content
- [ ] CT-01: Chart labels match the underlying data.
  - Action: With existing expenses in at least two categories and two different months, view both charts.
  - Expected: The by-category chart is labeled with exactly the category names used in the expense list, and the over-time chart is labeled with the months that contain expenses (no missing or placeholder labels).
  - Bug Report:
    - Issue: Chart Labels Do Not Match Underlying Data
    - Actual: The by-category ("Budget vs Spending") chart is labeled with emojis only (🍽️, 🚗, 🛍️, 🎬, 💡, 🏥, ✈️, 📦) instead of the category names used in the expense list ("Food & Dining", "Transportation", "Shopping", …). The over-time ("Spending Trend") chart is labeled with individual days (Oct 28, Oct 30, Nov 1, … Nov 9) instead of the months containing expenses (Nov 2024, Dec 2024, Nov 2026).

- [X] CT-02: Each expense row shows its original amount, currency, and exact category/goal labels.
  - Action: Inspect in the expense list the row of an expense logged as 45 EUR in category "Groceries" for goal "Vacation". (Adapted: the row inspected is the 45 EUR expense logged in FT-03 — category "Food & Dining", goal "Summer Vacation", since the app's fixed taxonomy has no "Groceries" category or "Vacation" goal and custom names cannot be created.)
  - Expected: The row shows the amount 45.00 with EUR (the currency it was logged in) and the labels "Groceries" and "Vacation" exactly as assigned.
