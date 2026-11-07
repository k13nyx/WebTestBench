# Test Result

## Functionality
- [ ] FT-01: Create a financial goal
  - Action: Open the goals section and add a new financial goal with a name and target amount.
  - Expected: The goal appears in the goals list with its defined name and target.
  - Bug Report:
    - Issue: Missing feature / No creation control
    - Actual: The Financial Goals section only displays three seeded, read-only goal cards (Summer Vacation, Emergency Fund, New Laptop). There is no "Add Goal" button, form, or any control to create a new goal anywhere in the UI. A full DOM scan confirmed only 23 buttons exist (currency selector, Add Expense, Filters, and 20 per-expense delete buttons) — none for goal creation.

- [ ] FT-02: Create a monthly budget
  - Action: Open the budgets section and add a monthly budget with an amount and period.
  - Expected: The monthly budget is saved and visible in the budgets list.
  - Bug Report:
    - Issue: Missing feature / No creation control
    - Actual: The "Monthly Budget" figure (€2600.00) is displayed as a static stat card only. There is no "Add Budget" button, budget section, or any control to create/edit a monthly budget. No budget list or creation UI exists in the application.

- [X] FT-03: Log an expense with amount and currency
  - Action: Open "Add Expense" and enter an amount and select a currency (e.g., USD, EUR).
  - Expected: The expense is recorded and shown in the expense list with its amount and currency.
  - Verification: Opened "Add New Expense", entered amount 100, selected currency USD, submitted. New row "Test Expense Nov" appeared at the top of the Recent Expenses list showing "$100.00" (and converted €92.00).

- [X] FT-04: Assign an expense to a category
  - Action: When logging an expense, select a category from the category list.
  - Expected: The expense is saved and displays the chosen category.
  - Verification: Selected "🍽️ Food & Dining" from the category dropdown. The saved expense displays "Food & Dining" beneath its description.

- [X] FT-05: Choose a primary currency
  - Action: Open settings and select a primary currency (e.g., USD).
  - Expected: The selected currency is marked as primary and saved.
  - Verification: (No dedicated Settings page exists; the header currency selector serves as the primary-currency control.) Clicking the header currency combobox opened a list of currencies; selecting "€ EUR" marked it as the selected option and persisted — all summaries immediately switched to €.

- [X] FT-06: View all summaries in the primary currency
  - Action: Open the summary/dashboard view after setting a primary currency.
  - Expected: All totals and summaries are displayed in the primary currency.
  - Verification: After selecting EUR as primary, header "Total Spent" became €1526.28, Monthly Budget €2600.00, Remaining €2600.00, Daily Average €109.02, all category budgets (e.g., "€0.00 of €600.00"), goals, and chart axes all rendered in €.

- [X] FT-07: View spending-vs-budget chart by category
  - Action: Open the charts view.
  - Expected: A chart shows each category's spending compared to its budget.
  - Verification: A "Budget vs Spending" chart is present with one bar per category (8 categories) on a budget-scaled €0–€600 axis. Additionally, the "Budget Categories" section shows each category's spending vs budget (e.g., "€92.00 of €600.00", 15%), which updates with data.

- [X] FT-08: View spending-over-time chart
  - Action: Open the charts view.
  - Expected: A chart shows spending totals across time periods (e.g., by month).
  - Verification: A "Spending Trend (Last 14 Days)" chart is present, with a time axis (Oct 26 → Nov 7 dates) and a € y-axis. After logging a dated expense it rescaled to €100 and reflected the new data point.

- [X] FT-09: Filter expense list by date range
  - Action: Apply a date range filter (start and end date) to the expense list.
  - Expected: Only expenses within the selected date range are displayed.
  - Verification: Set From=2024-12-01, To=2024-12-31. The list filtered to only Dec 2024 expenses (Dec 1–12); Nov 2024 and the 2026 test expense were correctly hidden.

- [X] FT-10: Filter expense list by category
  - Action: Select a category filter on the expense list.
  - Expected: Only expenses assigned to the selected category are displayed.
  - Verification: Selected category "Food & Dining". The list showed only Food & Dining expenses (Test Expense Nov, Grocery shopping, Coffee shop, Restaurant dinner, Lunch, Groceries); all other categories hidden.

- [X] FT-11: Filter expense list by goal
  - Action: Select a goal filter on the expense list.
  - Expected: Only expenses linked to the selected goal are displayed.
  - Verification: Selected goal "Summer Vacation". The list showed only the two linked expenses ("Flight booking" and "Hotel deposit", both tagged "TravelSummer Vacation"); all others hidden.

## Constraint
- [X] CS-01: Required fields enforced when logging an expense
  - Action: Attempt to submit an expense with a missing amount, currency, or category.
  - Expected: The expense is rejected with a clear validation error for the missing field.
  - Verification: Opened Add Expense with Description, Amount, and Category all empty and clicked "Add Expense". A toast appeared: "Missing fields — Please fill in all required fields." The dialog stayed open and no expense was created (header total remained €1618.28).

- [X] CS-02: Non-primary currency expenses converted in summaries
  - Action: Log an expense in a non-primary currency (e.g., EUR) and view the summary in the primary currency (e.g., USD).
  - Expected: The expense total is converted and shown in the primary currency, not the original currency.
  - Verification: Primary currency set to EUR; logged a USD expense of $100.00. It appeared in the list as €92.00 (converted) with the original $100.00 shown secondary, and the header "Total Spent" increased by exactly €92.00 (€1526.28 → €1618.28). Seeded non-primary expenses (£18.50 → €21.54, etc.) are likewise converted.

- [ ] CS-03: Date range filter validity enforced
  - Action: Apply a filter where the end date is earlier than the start date.
  - Expected: The filter is rejected with an error, and no invalid date range is applied.
  - Bug Report:
    - Issue: Missing validation / silent acceptance of invalid date range
    - Actual: Set From=2025-06-01 and To=2025-01-01 (end earlier than start). No validation error or warning was shown. The inverted range was silently applied and the list displayed the generic empty state "No expenses found matching your filters." — no error message and no explicit rejection of the invalid range.

## Interaction
- [ ] IX-01: Confirmation after creating goal, budget, or expense
  - Action: Successfully add a goal, a budget, and an expense.
  - Expected: A success confirmation (toast or message) appears after each successful creation.
  - Bug Report:
    - Issue: Confirmation partially unverifiable — goal and budget creation unavailable
    - Actual: The expense creation confirmation works correctly (toast "Expense added — Added $100 for Test Expense Nov" appeared). However, the app provides no UI to create goals or budgets (see FT-01/FT-02), so those two creations cannot be performed and their success confirmations cannot be verified. The item therefore cannot be fully satisfied.

- [X] IX-02: Charts and summaries update on data change or filter
  - Action: Log a new expense or apply a filter, then view charts/summary.
  - Expected: Charts and summaries immediately reflect the new expense or active filter.
  - Verification: After adding the expense, the dashboard "Total Spent" updated €0.00 → €92.00 (4% of budget), Remaining €2600 → €2508, Daily Average → €115.59, the Food & Dining category bar updated to "€92.00 of €600.00" (15%), and the Spending Trend chart rescaled to €100 to show the new point. Filters likewise updated the list live.

## Content
- [X] CT-01: Currency labels shown correctly in summaries
  - Action: Review the summary and expense views.
  - Expected: Each monetary value shows the correct currency symbol/code of the displayed (primary) currency.
  - Verification: With EUR as primary, every summary value (header total, budgets, goals, category totals, chart axes) displays the € symbol; each expense row shows the primary-currency value (€) with the original currency ($/£/€) shown secondarily. Symbol/code is consistent and correct.

- [X] CT-02: Chart labels are relevant and accurate
  - Action: Inspect the category and time charts.
  - Expected: Axes and legends show correct category names, time periods, and a spending-vs-budget reference with no irrelevant or placeholder text.
  - Verification: The Spending Trend chart's x-axis shows real time periods (Oct 26 → Nov 7) and the Budget vs Spending chart maps each of the 8 categories (y-axis in €, budget-scaled). The Budget Categories section provides an explicit spending-vs-budget reference ("€X of €Y"). No placeholder/lorem/irrelevant text was observed. (Note: the category chart axis uses emoji icons rather than textual category names; labels remain accurate and relevant, so this is a minor design choice, not a defect.)
