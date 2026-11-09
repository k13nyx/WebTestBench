All tests executed. Here is the complete result.

# Test Result

## Functionality
- [ ] FT-01: User can define a new financial goal
  - Action: Open the goal-creation form, enter a name (e.g., "Emergency Fund") and a target amount, and save.
  - Expected: The goal is saved and appears in the goals list with its name and target amount.
  - Bug Report:
    - Issue: Missing Feature — no goal-creation UI exists
    - Actual: The "Financial Goals" section renders three default goal cards but contains no "Add Goal" button, form, link, or route anywhere on the page (exhaustive sweep of all buttons/links/inputs found only: currency selector, "Add Expense", "Filters", "Clear Filters", and expense delete buttons). Clicking a goal card opens no editor. A new goal cannot be created.

- [ ] FT-02: User can define monthly budgets per category
  - Action: Open the budget form, set a monthly budget for at least two categories (e.g., Groceries 400, Rent 1200), and save.
  - Expected: Each budget is listed showing category, monthly amount, and applies to the current month's summaries.
  - Bug Report:
    - Issue: Missing Feature — no budget-creation/editing UI exists
    - Actual: The "Budget Categories" section shows only fixed default budgets (Food & Dining $600, Transportation $400, etc.). There is no button, form, or control to create or change a category budget; the section contains zero interactive controls.

- [X] FT-03: User can log an expense in a non-primary currency and assign it to a category and goal
  - Action: Add an expense with amount 50, currency EUR, a date, a category ("Food & Dining"), and a goal ("Summer Vacation"); save.
  - Expected: The expense appears in the expense list showing amount with "EUR", its category, and its assigned goal.
  - Verified: New row rendered as "🍽️ Team dinner / Food & Dining / Summer Vacation / $54.35 €50.00 / Nov 8, 2026" (entered EUR amount "€50.00", category, and goal all displayed).

- [X] FT-04: User can select a primary currency
  - Action: Use the primary-currency selector to switch from the current primary currency to another (e.g., USD → EUR).
  - Expected: The selection persists and all summary totals on the page are immediately re-displayed in EUR.
  - Verified: Selector switched to "€ EUR" and stayed selected through all subsequent operations; header total became €1576.28, cards €2600.00 / €50.00 / €2550.00 / €112.59, budget bar "€50.00 of €600.00", and chart axes in €. (Note: selection persists in-session only — the app has no storage layer, so reload resets state; no checklist item requires cross-reload persistence.)

- [X] FT-05: Summaries convert multi-currency expenses into the primary currency
  - Action: With USD as primary currency, view the total-spent summary while default expenses in other currencies (e.g., EUR, JPY) exist.
  - Expected: The summary shows a single USD total; no foreign-currency amounts are summed unconverted into it.
  - Verified: Header "Total Spent $1659.00" exactly equals the sum of the per-row converted USD values (manually summed all 20 rows to $1,659.00). EUR/GBP entries were converted at consistent rates (€12.50→$13.59, £18.50→$23.42, €35.00→$38.04); after adding €50 the total moved to $1713.35 (+$54.35). No raw €/$ mixed summation.

- [X] FT-06: Chart compares spending vs. budget by category
  - Action: View the "Spending by Category" chart.
  - Expected: A chart renders with one entry per budgeted category, visually showing actual spending against that category's budget.
  - Verified: "Budget vs Spending" recharts bar chart renders 8 category ticks (🍽️🚗🛍️🎬💡🏥✈️📦) with 16 bars = 2 series (Spent vs Budget); tooltip confirmed "Food & Dining — Spent: €50.00 / Budget: €600.00".

- [X] FT-07: Chart shows spending over time
  - Action: View the "Spending Over Time" chart.
  - Expected: A chart renders showing total spending per time period (e.g., per month), with each period's spending value plotted.
  - Verified: "Spending Trend (Last 14 Days)" line chart renders with 10 labeled day ticks (Oct 26–Nov 8) and a plotted line; after adding the €50 expense dated Nov 8, the y-axis re-scaled from €0–€4 to €0–€60, confirming the period's value is plotted.

- [X] FT-08: Expense list can be filtered by date range
  - Action: Set a start and end date covering only some default expenses, and apply the filter.
  - Expected: The list shows only expenses dated within the range; expenses outside it are hidden.
  - Verified: Range 2024-12-01→2024-12-12 showed exactly the 13 in-range rows; all Nov 2024 rows, and the 2026-11-08 row, were hidden; clearing restored all 21 rows.

- [X] FT-09: Expense list can be filtered by category
  - Action: Select a single category in the category filter.
  - Expected: The list shows only expenses in that category; clearing the filter restores the full list.
  - Verified: Category "Utilities" → only "Electric bill" and "Internet bill" shown; selecting "All categories" restored 21 rows.

- [X] FT-10: Expense list can be filtered by goal
  - Action: Select a specific goal in the goal filter.
  - Expected: The list shows only expenses assigned to that goal.
  - Verified: Goal "Summer Vacation" → only "Team dinner", "Flight booking", "Hotel deposit" (the three goal-assigned expenses) shown; restored after clearing.

## Constraint
- [X] CS-01: Expense cannot be saved with missing required fields
  - Action: Open the add-expense form, leave required fields (e.g., amount, date, category) empty, and submit.
  - Expected: The expense is rejected, a validation indication appears on the missing fields, and no new row is added to the list.
  - Verified: Submitting the empty form produced the visible validation toast "Missing fields — Please fill in all required fields.", the dialog stayed open, and no expense row was added.

- [ ] CS-02: Invalid expense amounts are rejected
  - Action: Enter an expense with amount 0 or a negative/non-numeric value and attempt to save.
  - Expected: The save is blocked with a validation message; the expense is not added.
  - Bug Report:
    - Issue: Missing validation — zero amount accepted; negative amount silently blocked
    - Actual: An expense with amount 0 (all other fields valid) was saved: a new row "$0.00 / Invalid test / Utilities" appeared in the list with no validation message. A negative amount (-50) was blocked from saving, but produced no error message whatsoever (silent no-op — toasts, field errors, and aria-invalid all empty).

- [ ] CS-03: Only one monthly budget per category
  - Action: Try to create a second budget for a category that already has a budget for the same month.
  - Expected: The duplicate is prevented (error message, or the existing budget is updated rather than a second entry created).
  - Bug Report:
    - Issue: Untestable — budget creation feature does not exist
    - Actual: There is no budget form or control anywhere on the page (see FT-02); a duplicate budget cannot be attempted, so the constraint has no enforcement path in the UI.

- [X] CS-04: Expenses cannot reference non-existent categories or goals
  - Action: Open the add-expense form and inspect the category and goal fields.
  - Expected: Category and goal are chosen from the existing defined options only; free-text entries for undefined categories/goals are not accepted.
  - Verified: Category and Goal fields are dropdown-only comboboxes — Category options exactly the 8 defined categories; Goal options exactly "No goal" + the 3 defined goals. The only free-text inputs are Description, Amount (number), and Date; there is no field to type an arbitrary category/goal.

## Interaction
- [ ] IX-01: Success feedback after adding an item
  - Action: Save a new goal, budget, and expense.
  - Expected: Each successful save produces a visible confirmation (e.g., toast or success message) and the relevant list/summary updates without a manual page reload.
  - Bug Report:
    - Issue: Missing functionality prevents the check — goals and budgets cannot be added/saved
    - Actual: The expense portion passes (toast "Expense added — Added €50 for Team dinner"; expense list, header total, summary cards, and charts all updated live without reload). However, saving a new goal and a new budget is impossible because no creation UI exists (see FT-01/FT-02), so no confirmation can be produced for those items and the test cannot pass in full.

- [X] IX-02: Filtering updates results live, including an empty state
  - Action: Apply a filter combination that matches no default expenses (e.g., a category with no expenses in a narrow date range).
  - Expected: The list updates to show an explicit "no results" message rather than an unexplained blank area or stale rows.
  - Verified: Selecting category "Other" (0 expenses) updated the list instantly to zero rows with the explicit message "No expenses found matching your filters."

- [X] IX-03: Chart hover reveals values
  - Action: Hover over a bar/segment in the category chart and a point/period in the time chart.
  - Expected: A tooltip (or equivalent) shows the specific value(s), e.g., category spend vs. budget, and the amount for the hovered time period.
  - Verified: Hovering the Food & Dining bar showed tooltip "Food & Dining — Spent: €50.00 / Budget: €600.00"; hovering the Nov 8 position on the trend chart showed tooltip "Nov 8 — €50.00".

## Content
- [X] CT-01: Default data is present and spans multiple currencies and categories
  - Action: Load the page fresh and inspect the goals, budgets, and expense lists.
  - Expected: Pre-existing goals, monthly budgets, and sample expenses across several currencies, categories, and dates are displayed, sufficient to exercise filters and charts.
  - Verified: Fresh load showed 3 goals (Summer Vacation, Emergency Fund, New Laptop), 8 category budgets totaling $2,600/mo, and 20 expenses spanning USD/EUR/GBP original currencies, 8 categories, 3 goal-attached expenses, and dates Nov 24–Dec 12, 2024 — sufficient for all filters and both charts.

- [X] CT-02: Monetary values are labeled with the correct currency
  - Action: Inspect expense list rows, budget entries, and summary totals.
  - Expected: Every monetary value displays a currency symbol or code; per-expense amounts show the entered currency, summaries show the primary currency only.
  - Verified: Every amount carried a symbol ($/€/£). Expense rows showed converted primary-currency value plus the entered original (e.g., "$13.59 €12.50", "$23.42 £18.50", "$54.35 €50.00"); summaries (header total, cards, budget bars "€50.00 of €600.00", chart axes) displayed the primary currency only (all $ when USD, all € when EUR).