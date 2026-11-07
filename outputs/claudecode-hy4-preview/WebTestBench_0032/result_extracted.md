# Test Result

## Functionality
- [ ] FT-01: User can create a new financial goal
  - Action: Open the Goals section, click "Add Goal" (or equivalent), enter a name (e.g. "Emergency Fund"), a target amount (e.g. 5000) and a target date, then save.
  - Expected: The new goal appears in the goals list showing the entered name, the target amount in the primary currency, and a progress value of 0 / 0%.
  - Bug Report:
    - Issue: Missing Feature / No Creation UI
    - Actual: The "Financial Goals" section is read-only. Enumerating every interactive element on the page returned only "Add Expense", "Filters", the currency combobox and 20 per-row delete buttons — there is no "Add Goal", "New Goal" or "+" control anywhere, and clicking a goal card (e.g. "Emergency Fund") opens no dialog (0 dialogs). Only the 3 pre-seeded goals (Summer Vacation, Emergency Fund, New Laptop) can ever be shown, so a new goal cannot be created.

- [ ] FT-02: User can define a monthly budget for a category
  - Action: Open the Budgets / Monthly Budget section, set a monthly limit for an existing category (e.g. "Groceries" = 500) and save.
  - Expected: The budget is saved and displayed for that category, and it is reflected in the budget summary and in the "spending vs budget by category" chart.
  - Bug Report:
    - Issue: Missing Feature / Read-only Budget Values
    - Actual: The "Budget Categories" cards only display fixed values ("Food & Dining $0.00 of $600.00", etc.) with no input, edit or Save control; the section contains no button, input or clickable target (clicking the "Food & Dining" heading opened no dialog, 0 dialogs). No monthly limit can be set or changed from the UI.

- [X] FT-03: User can log an expense in a non-primary currency and assign it to a category
  - Action: Open "Add Expense", enter amount 100, select a currency different from the currently selected primary currency (e.g. EUR), select category "Groceries", pick today's date, then submit.
  - Expected: The expense is saved and appears in the expense list showing amount 100 with its own currency code (EUR) alongside the assigned category "Groceries".

- [X] FT-04: Expense list displays all logged expenses with their attributes
  - Action: Open the Expenses list and inspect the pre-existing (default) expense records.
  - Expected: Each listed row shows a date, an amount with currency, a category, and the linked goal (or an explicit "no goal" state); all default expenses are visible.

- [X] FT-05: User can choose a primary currency
  - Action: Open the currency selector / settings and select a primary currency (e.g. USD).
  - Expected: The selection is applied and clearly indicated as the primary currency in the interface.

- [X] FT-06: All summary figures are shown in the primary currency
  - Action: With primary currency = USD, view the summary figures (total spent, remaining budget, goal progress) while at least one expense exists in a different currency.
  - Expected: Every summary figure is displayed in USD with the USD symbol/code; the foreign-currency expense contributes a non-zero USD amount, and no summary figure remains labelled in a foreign currency.

- [ ] FT-07: "Spending vs budget by category" chart is displayed
  - Action: Locate the category chart on the dashboard/summary area with the default data loaded.
  - Expected: The chart renders with one entry per existing category; each entry displays that category's budget and the actual amount spent, both in the primary currency, with at least one non-zero spending value.
  - Bug Report:
    - Issue: Empty Chart Data (all spending values zero with default data)
    - Actual: The chart renders with one entry per category (8 categories, 16 bars, USD axis $0–$600), but hovering every category returns "Food & Dining / Spent: $0.00 / Budget: $600.00", "Transportation / Spent: $0.00 / Budget: $400.00", "Shopping / Spent: $0.00 …", "Travel / Spent: $0.00 / Budget: $500.00" etc. — every "Spent" value is $0.00 and every budget card reads "$0.00 of $600.00". Spending is aggregated for the current month only, while all default expenses are dated Nov 24 – Dec 12, 2024, so no non-zero spending value is displayed on load (a spend logged for the current date did show $108.70 correctly, then vanished on reload).

- [ ] FT-08: "Spending over time" chart is displayed
  - Action: Locate the spending-over-time chart on the dashboard/summary area.
  - Expected: The chart renders with a time axis (days / weeks / months) and plotted spending amounts in the primary currency; the default expenses produce at least one non-zero data point.
  - Bug Report:
    - Issue: Empty Chart Data (all data points zero with default data)
    - Actual: The "Spending Trend (Last 14 Days)" chart renders with a day axis (Oct 26 … Nov 8) and USD Y-axis ticks, but hovering all 14 points returns "Oct 26 / $0.00", "Oct 27 / $0.00" … "Nov 7 / $0.00" — there is no non-zero data point; the plotted line collapses to a single vertical segment ("M560,10L560,170"). The default expenses (Nov–Dec 2024) fall outside the 14-day window ending on the current date.

- [X] FT-09: User can filter the expense list by date range
  - Action: Set the date-range filter to a narrow range covering a single known expense date (e.g. today) and apply it.
  - Expected: Only expenses whose date falls inside the selected range are listed, and the list count matches that subset.

- [X] FT-10: User can filter the expense list by category
  - Action: Select a single category (e.g. "Groceries") in the category filter.
  - Expected: Only expenses assigned to that category are listed; no expense belonging to another category is shown.

- [X] FT-11: User can filter the expense list by goal
  - Action: Select a single goal in the goal filter.
  - Expected: Only expenses assigned to that goal are listed; expenses assigned to other goals or to no goal are hidden.

## Constraint
- [X] CS-01: Expense cannot be saved with missing required information
  - Action: Open "Add Expense", leave the amount (or date / category) empty, and attempt to submit.
  - Expected: Submission is blocked and a validation message identifies the missing field; no new row is added to the expense list.

- [ ] CS-02: Amount fields reject zero, negative, or non-numeric values
  - Action: Attempt to save an expense with amount "0", then with amount "-50", then with text "abc".
  - Expected: Each attempt is rejected with a validation message and no expense is created; the same applies to goal and budget amounts.
  - Bug Report:
    - Issue: Zero Amount Accepted / Missing Validation Message for Negative Input
    - Actual: Amount "0" was accepted — the dialog closed, a row was added and the toast read "Expense added / Added $0 for Validation probe". Amount "-50" and non-numeric text were blocked (the number input carries min="0", checkValidity false, "Value must be greater than or equal to 0.", and letters cannot even be typed into the field), but the only rejection message is the native browser bubble, not an in-app validation message. Goal and budget amount fields do not exist at all, so their validation could not be exercised.

- [X] CS-03: Expenses can only be assigned to existing categories and goals
  - Action: Open the category and goal selectors on the expense form and inspect the available options; attempt to type a value that is not in the list.
  - Expected: Only previously defined categories and goals are selectable; a category or goal that does not exist cannot be assigned.

- [ ] CS-04: Primary currency selection persists after reload
  - Action: Select a non-default primary currency, reload the page, then view summaries and charts.
  - Expected: The selected currency is still the primary currency, and all summaries and chart values are still displayed in it (no value reverts to a previous currency).
  - Bug Report:
    - Issue: State Not Persisted After Reload
    - Actual: After switching the primary currency to EUR (header showed "€ EUR", summaries read "Total Spent €1626.28 / Monthly Budget €2600.00", chart axes "€0,€150,€300,€450,€600"), reloading the page reverted everything: the selector showed "$ USD", summaries read "Total Spent $1659.00 / Monthly Budget $2600.00", axes "$0,$150,$300,$450,$600". Expenses added before the reload were also lost (Total Spent back to $0.00 for the month).

## Interaction
- [X] IX-01: Changing the primary currency updates summaries and charts immediately
  - Action: Without reloading the page, change the primary currency from the current one to a different currency (e.g. USD → EUR).
  - Expected: All summary figures and both chart value labels update in place to the newly selected currency within a few seconds, without a page reload or a manual refresh action.

- [X] IX-02: Applying and clearing filters updates the list instantly
  - Action: Apply any filter (e.g. a category), observe the list, then clear / reset all filters.
  - Expected: The list narrows immediately when a filter is applied and returns to showing all expenses immediately when filters are cleared, without a page reload.

- [X] IX-03: Success feedback is shown after logging an expense
  - Action: Successfully submit a valid expense through the "Add Expense" form.
  - Expected: A confirmation (message or notification) is displayed confirming the expense was added, and the form is cleared / closed.

## Content
- [X] CT-01: All text and labels are budgeting/finance themed and currencies are labelled correctly
  - Action: Read all section headings, labels, and buttons across Goals, Budgets, Expenses, and filters; check the currency codes/symbols shown next to monetary values.
  - Expected: All labels relate to budgeting/finance (e.g. Goals, Budgets, Expenses, Categories, Primary Currency) with no placeholder or off-topic text, and each currency is shown with its correct code or symbol (e.g. USD/$, EUR/€, JPY/¥).

- [ ] CT-02: Charts are labelled so their data is identifiable
  - Action: Inspect the "spending vs budget by category" and "spending over time" charts.
  - Expected: Each chart displays a title, a legend or category labels identifying what each series represents (budget vs spent), readable axis labels with units in the primary currency, and no missing/blank label text.
  - Bug Report:
    - Issue: Missing Chart Legend / Unlabelled Category Axis
    - Actual: Both charts have titles ("Budget vs Spending", "Spending Trend (Last 14 Days)") and USD axis ticks ($0–$600, $0–$120), but the category chart renders zero legend elements (`.recharts-legend-wrapper` count = 0) although it plots two series per category, so nothing on the chart labels which bar is "Budget" and which is "Spent" — that is only revealed on hover ("Travel / Spent: $0.00 / Budget: $500.00"). Its X-axis labels are bare emoji icons ("🍽️ 🚗 🛍️ 🎬 💡 🏥 ✈️ 📦") with no category names, so the plotted categories are not identifiable as text.
