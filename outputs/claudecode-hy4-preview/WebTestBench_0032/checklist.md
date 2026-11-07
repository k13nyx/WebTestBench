# Test Checklist

## Functionality
- [ ] FT-01: User can create a new financial goal
  - Action: Open the Goals section, click "Add Goal" (or equivalent), enter a name (e.g. "Emergency Fund"), a target amount (e.g. 5000) and a target date, then save.
  - Expected: The new goal appears in the goals list showing the entered name, the target amount in the primary currency, and a progress value of 0 / 0%.

- [ ] FT-02: User can define a monthly budget for a category
  - Action: Open the Budgets / Monthly Budget section, set a monthly limit for an existing category (e.g. "Groceries" = 500) and save.
  - Expected: The budget is saved and displayed for that category, and it is reflected in the budget summary and in the "spending vs budget by category" chart.

- [ ] FT-03: User can log an expense in a non-primary currency and assign it to a category
  - Action: Open "Add Expense", enter amount 100, select a currency different from the currently selected primary currency (e.g. EUR), select category "Groceries", pick today's date, then submit.
  - Expected: The expense is saved and appears in the expense list showing amount 100 with its own currency code (EUR) alongside the assigned category "Groceries".

- [ ] FT-04: Expense list displays all logged expenses with their attributes
  - Action: Open the Expenses list and inspect the pre-existing (default) expense records.
  - Expected: Each listed row shows a date, an amount with currency, a category, and the linked goal (or an explicit "no goal" state); all default expenses are visible.

- [ ] FT-05: User can choose a primary currency
  - Action: Open the currency selector / settings and select a primary currency (e.g. USD).
  - Expected: The selection is applied and clearly indicated as the primary currency in the interface.

- [ ] FT-06: All summary figures are shown in the primary currency
  - Action: With primary currency = USD, view the summary figures (total spent, remaining budget, goal progress) while at least one expense exists in a different currency.
  - Expected: Every summary figure is displayed in USD with the USD symbol/code; the foreign-currency expense contributes a non-zero USD amount, and no summary figure remains labelled in a foreign currency.

- [ ] FT-07: "Spending vs budget by category" chart is displayed
  - Action: Locate the category chart on the dashboard/summary area with the default data loaded.
  - Expected: The chart renders with one entry per existing category; each entry displays that category's budget and the actual amount spent, both in the primary currency, with at least one non-zero spending value.

- [ ] FT-08: "Spending over time" chart is displayed
  - Action: Locate the spending-over-time chart on the dashboard/summary area.
  - Expected: The chart renders with a time axis (days / weeks / months) and plotted spending amounts in the primary currency; the default expenses produce at least one non-zero data point.

- [ ] FT-09: User can filter the expense list by date range
  - Action: Set the date-range filter to a narrow range covering a single known expense date (e.g. today) and apply it.
  - Expected: Only expenses whose date falls inside the selected range are listed, and the list count matches that subset.

- [ ] FT-10: User can filter the expense list by category
  - Action: Select a single category (e.g. "Groceries") in the category filter.
  - Expected: Only expenses assigned to that category are listed; no expense belonging to another category is shown.

- [ ] FT-11: User can filter the expense list by goal
  - Action: Select a single goal in the goal filter.
  - Expected: Only expenses assigned to that goal are listed; expenses assigned to other goals or to no goal are hidden.

## Constraint
- [ ] CS-01: Expense cannot be saved with missing required information
  - Action: Open "Add Expense", leave the amount (or date / category) empty, and attempt to submit.
  - Expected: Submission is blocked and a validation message identifies the missing field; no new row is added to the expense list.

- [ ] CS-02: Amount fields reject zero, negative, or non-numeric values
  - Action: Attempt to save an expense with amount "0", then with amount "-50", then with text "abc".
  - Expected: Each attempt is rejected with a validation message and no expense is created; the same applies to goal and budget amounts.

- [ ] CS-03: Expenses can only be assigned to existing categories and goals
  - Action: Open the category and goal selectors on the expense form and inspect the available options; attempt to type a value that is not in the list.
  - Expected: Only previously defined categories and goals are selectable; a category or goal that does not exist cannot be assigned.

- [ ] CS-04: Primary currency selection persists after reload
  - Action: Select a non-default primary currency, reload the page, then view summaries and charts.
  - Expected: The selected currency is still the primary currency, and all summaries and chart values are still displayed in it (no value reverts to a previous currency).

## Interaction
- [ ] IX-01: Changing the primary currency updates summaries and charts immediately
  - Action: Without reloading the page, change the primary currency from the current one to a different currency (e.g. USD → EUR).
  - Expected: All summary figures and both chart value labels update in place to the newly selected currency within a few seconds, without a page reload or a manual refresh action.

- [ ] IX-02: Applying and clearing filters updates the list instantly
  - Action: Apply any filter (e.g. a category), observe the list, then clear / reset all filters.
  - Expected: The list narrows immediately when a filter is applied and returns to showing all expenses immediately when filters are cleared, without a page reload.

- [ ] IX-03: Success feedback is shown after logging an expense
  - Action: Successfully submit a valid expense through the "Add Expense" form.
  - Expected: A confirmation (message or notification) is displayed confirming the expense was added, and the form is cleared / closed.

## Content
- [ ] CT-01: All text and labels are budgeting/finance themed and currencies are labelled correctly
  - Action: Read all section headings, labels, and buttons across Goals, Budgets, Expenses, and filters; check the currency codes/symbols shown next to monetary values.
  - Expected: All labels relate to budgeting/finance (e.g. Goals, Budgets, Expenses, Categories, Primary Currency) with no placeholder or off-topic text, and each currency is shown with its correct code or symbol (e.g. USD/$, EUR/€, JPY/¥).

- [ ] CT-02: Charts are labelled so their data is identifiable
  - Action: Inspect the "spending vs budget by category" and "spending over time" charts.
  - Expected: Each chart displays a title, a legend or category labels identifying what each series represents (budget vs spent), readable axis labels with units in the primary currency, and no missing/blank label text.