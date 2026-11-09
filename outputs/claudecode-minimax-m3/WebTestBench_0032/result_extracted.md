# Test Result

## Functionality

- [ ] FT-01: User can create a new financial goal with a name and target amount.
  - Action: Click "Add Goal" (or equivalent), enter a goal name (e.g., "Vacation") and target amount, save.
  - Expected: The new goal appears in the goals list and is available for selection when assigning expenses.
  - Bug Report:
    - Issue: Missing Feature / No Goal Creation UI
    - Actual: No "Add Goal" control exists anywhere in the app. A full DOM sweep of the dashboard found only 3 actionable buttons ("$ USD" currency selector, "Add Expense", "Filters") plus 20 expense-row icon buttons — a regex search for `/add\s*goal/i` over the page text returned no match, and the "Financial Goals" section header contains no button. The 3 goal cards (Summer Vacation, Emergency Fund, New Laptop) contain 0 buttons/links/inputs and are read-only. Navigating to `/goals` returns the app's "404 — Oops! Page not found" page, and no `AddGoalDialog`/`GoalForm` component exists in the source. The goal dropdown inside "Add Expense" only offers the 3 seeded goals, so a new goal can neither be created nor selected.

- [ ] FT-02: User can create a new monthly budget by category for a specific month/year.
  - Action: Click "Add Budget" (or equivalent), select a category, enter an amount, choose month/year, save.
  - Expected: The new budget appears in the budgets list and is reflected in the category-vs-budget chart.
  - Bug Report:
    - Issue: Missing Feature / No Budget Creation UI
    - Actual: No "Add Budget" control exists. `/add\s*budget/i` search over the page text returns no match; the "Budget Categories" section header contains no button and each of the 8 budget category cards contains 0 buttons. `/budgets` returns the 404 page and no budget-form component exists. Budgets are a single static `monthlyBudget` number per category (Food & Dining $600, Transportation $400, Shopping $300, Entertainment $200, Utilities $250, Health $150, Travel $500, Other $200) — there is no month/year selector, no editable amount field, and no way to add a budget for a specific period.

- [X] FT-03: User can log a new expense specifying amount, currency, category, and date.
  - Action: Click "Add Expense", fill in amount, currency (e.g., USD, EUR, JPY), category, and date, save.
  - Expected: The expense appears in the expense list and contributes to the relevant summaries.

- [ ] FT-04: User can assign an existing expense to a financial goal.
  - Action: When logging or editing an expense, select a goal from the goals dropdown.
  - Expected: The expense is linked to the chosen goal and counts toward it.
  - Bug Report:
    - Issue: Goal Progress Not Updated / Linked Expense Not Counted Toward Goal
    - Actual: Linking works — the goal dropdown in "Add Expense" contains "No goal / Summer Vacation / Emergency Fund / New Laptop", and after saving with "Summer Vacation" the new row reads "QA Test Expense | Food & DiningSummer Vacation | $108.70 | Nov 7, 2026". However, the linked amount does **not** count toward the goal: the Summer Vacation card showed "Progress $1850.00 | Remaining $1150.00" both before and after adding the $108.70 expense (progress bar and percentage unchanged). Goal progress is rendered from the static `goal.currentAmount` field, and the two pre-seeded Summer Vacation expenses (Flight booking $350, Hotel deposit $200 = $550) are likewise excluded from its $1850 progress.

- [X] FT-05: User can select a primary currency for the application.
  - Action: Open settings/preferences and choose a primary currency (e.g., USD).
  - Expected: The selected currency is saved and used as the display currency throughout the app.
  - Note: The currency selector lives in the header (there is no separate settings page). The choice is applied throughout the app but is session-only — no localStorage/sessionStorage persistence exists, so a reload reverts to USD.

- [X] FT-06: User can view a chart comparing spending vs. budget by category.
  - Action: Navigate to the category summary/chart view.
  - Expected: A chart is displayed showing actual spend vs. budgeted amount for each category in the primary currency.

- [X] FT-07: User can view a chart showing spending over time.
  - Action: Navigate to the time/trend chart view.
  - Expected: A chart is displayed plotting expense totals across time (e.g., by day/week/month) in the primary currency.

- [X] FT-08: User can filter the expense list by a date range.
  - Action: Set a start date and end date in the expense list filter controls, apply.
  - Expected: Only expenses with dates within the selected range are shown.

- [X] FT-09: User can filter the expense list by category.
  - Action: Select one or more categories from the category filter, apply.
  - Expected: Only expenses belonging to the selected category(ies) are shown.

- [X] FT-10: User can filter the expense list by financial goal.
  - Action: Select a goal from the goal filter, apply.
  - Expected: Only expenses assigned to the selected goal are shown.

## Constraint

- [X] CS-01: Required fields cannot be empty when creating an expense, goal, or budget.
  - Action: Try to submit the expense/goal/budget form with one required field left blank.
  - Expected: Submission is blocked and a clear validation message identifies the missing field.
  - Note: Verified on the expense form (the only creatable entity): submitting with Description/Amount/Category empty blocked submission, kept the dialog open and raised the toast "Missing fields — Please fill in all required fields." Goal and budget forms do not exist, so no validation path could be exercised there.

- [X] CS-02: All monetary summaries and charts must display values in the chosen primary currency, regardless of the expense's original currency.
  - Action: Log expenses in mixed currencies (e.g., USD, EUR) while primary currency is USD; view summaries and charts.
  - Expected: Every displayed amount is converted to and shown in the primary currency; original currencies are not used in totals/charts.
  - Note: With USD selected, Grocery shopping ($85.50) and Train ticket ($38.04) display as $85.50/$38.04; with EUR selected they became €78.66/€35.00 while Coffee shop (€12.50) stayed €12.50. Header total switched $1767.69 ↔ €1626.28, all stat cards, category cards, goal cards and both chart axes re-labelled, and chart tooltips showed "Spent: $108.70 | Budget: $600.00". No non-primary currency symbol appears in any total or chart. (Only the per-row expense list shows the original amount as a secondary line under the converted value, e.g. "$13.59 / €12.50".)

- [X] CS-03: Expenses logged in non-primary currencies must be accepted and converted, not rejected.
  - Action: Log an expense using a currency different from the primary currency.
  - Expected: The expense is saved successfully and its converted primary-currency value appears in summaries.

## Interaction

- [X] IX-01: Adding a new expense immediately updates the category-vs-budget chart and time chart.
  - Action: Open the charts, then log a new expense.
  - Expected: Both charts reflect the new expense without requiring a manual page reload.

- [X] IX-02: Changing filters on the expense list dynamically refreshes the displayed expenses.
  - Action: Apply or change a date/category/goal filter on the expense list.
  - Expected: The list updates immediately to show only matching expenses; no manual refresh required.

- [X] IX-03: Changing the primary currency immediately updates all monetary summaries and charts.
  - Action: Switch the primary currency from, e.g., USD to EUR in settings.
  - Expected: All totals, charts, and budget comparisons re-render with values converted to the new primary currency.

## Content

- [X] CT-01: Chart labels and category names in the category-vs-budget chart must match the categories defined in budgets/expenses.
  - Action: Create categories (e.g., "Food", "Transport") and view the category chart.
  - Expected: The chart uses the exact same category names as those configured by the user.
  - Note: The chart is keyed to the exact configured category names — each rendered bar carries `name="Food & Dining"`, `"Transportation"`, `"Shopping"`, … and the tooltip header shows the identical string ("Food & Dining"). The visible category axis ticks show each category's emoji (🍽️ 🚗 🛍️ 🎬 💡 🏥 ✈️ 📦) rather than the text name.

- [X] CT-02: Pre-existing default data (sample goals, budgets, or expenses) must be relevant to a budgeting application.
  - Action: Load the application on first use and inspect any pre-populated goals/budgets/expenses.
  - Expected: Default items use realistic budgeting categories, currencies, and amounts that align with the app's purpose; no placeholder text like "Lorem ipsum" or unrelated content is shown.
  - Note: Defaults are realistic — goals (Summer Vacation $3000, Emergency Fund $10000, New Laptop $2000), 8 standard budget categories, and 20 plausible expenses with mixed currencies (Grocery shopping $85.50, Uber ride $24.00, Netflix subscription $15.99, Train ticket €35.00, Lunch £18.50); no placeholder/Lorem ipsum text. Minor observation: all three goals display "Deadline passed" because their deadlines are in 2025 while the current date is Nov 7, 2026.
