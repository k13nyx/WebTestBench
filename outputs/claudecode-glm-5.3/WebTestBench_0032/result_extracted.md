# Test Result

## Functionality

- [ ] FT-01: Create a financial goal
  - Action: Open the Goals section, enter a goal name (e.g., "Emergency Fund") and a target amount, then save.
  - Expected: The new goal appears in the goals list showing the entered name and target amount.
  - Bug Report:
    - Issue: Missing Feature / Unreachable Functionality
    - Actual: The "Financial Goals" section only displays 3 static, pre-seeded goal cards (Summer Vacation, Emergency Fund, New Laptop). There is no "Add Goal" button, form, or input anywhere on the page. Clicking a goal card opens nothing. A full DOM sweep found 26 buttons (all identified: currency selector, Add Expense, Filters, 2 filter comboboxes, 21 expense-delete buttons), 0 links, and a single route — no goal-creation affordance exists.

- [ ] FT-02: Define a monthly budget
  - Action: Select an existing category, enter a monthly budget amount, and save.
  - Expected: The budget is stored and displayed as that category's budget for the chosen month.
  - Bug Report:
    - Issue: Missing Feature / Unreachable Functionality
    - Actual: The "Budget Categories" section shows 8 display-only cards with fixed budget values ($600, $400, $300, $200, $250, $150, $500, $200). There is no budget-editing control, no input field, and no month selector. Clicking a category card opens nothing. Budgets cannot be defined or modified by the user.

- [X] FT-03: Log an expense in a non-primary currency
  - Action: Add an expense with an amount and a currency different from the primary currency (e.g., EUR or GBP), then save.
  - Expected: The expense appears in the expense list showing the exact amount and currency entered.

- [X] FT-04: Assign an expense to a category
  - Action: While adding an expense, choose a category from the category selector and save.
  - Expected: The saved expense is displayed with the selected category in the expense list.

- [X] FT-05: Primary currency selection converts all summaries
  - Action: Change the primary currency (e.g., from USD to EUR).
  - Expected: All summary figures (total spending, budget comparisons, chart values) re-display converted into the newly selected primary currency.

- [X] FT-06: Filter expenses by date range
  - Action: Apply a date range that includes only some of the default expenses.
  - Expected: Only expenses dated within the range are listed; expenses outside the range are excluded.

- [X] FT-07: Filter expenses by category
  - Action: Apply the category filter for one existing category.
  - Expected: Only expenses assigned to that category are shown.

- [X] FT-08: Filter expenses by goal
  - Action: Apply the goal filter for one existing goal.
  - Expected: Only expenses linked to that goal are shown.

- [X] FT-09: Combine all three filters
  - Action: Apply a date range, a category, and a goal filter at the same time.
  - Expected: The list shows only expenses that satisfy all three conditions simultaneously.

- [X] FT-10: Budget vs. spending chart by category
  - Action: Open the category comparison chart for a month that has budgets set.
  - Expected: Each category shows its actual spending next to its monthly budget (a clear spending-vs-budget comparison).

- [X] FT-11: Spending over time chart
  - Action: Open the spending-over-time chart.
  - Expected: The chart shows spending totals per time period (e.g., per month) matching the logged expense data.

## Constraint

- [ ] CS-01: Expense form rejects invalid input
  - Action: Attempt to save an expense with an empty amount, or a non-numeric / negative / zero amount.
  - Expected: The expense is not saved and a validation error is displayed.
  - Bug Report:
    - Issue: Incorrect Form Submission (missing validation for zero amount)
    - Actual: A zero-amount expense was accepted and saved: with all other fields valid and Amount = 0, the app showed the success toast "Expense added — Added $0 for Invalid negative test" and the row "✈️ Invalid negative test · Travel · $0.00 · Nov 7, 2026" appeared in the list (I deleted it afterwards to restore state). Secondary issue: a negative amount (−50) is silently not saved with no error message displayed. The empty-field case works correctly ("Missing fields — Please fill in all required fields." toast), and non-numeric text cannot be entered into the numeric field.

- [ ] CS-02: Goal form rejects invalid input
  - Action: Attempt to save a goal with an empty name, or an empty / negative target amount.
  - Expected: The goal is not saved and the invalid fields are indicated.
  - Bug Report:
    - Issue: Missing Feature / Unreachable Functionality
    - Actual: No goal form exists anywhere in the application (see FT-01). There is no name field or target-amount field to attempt this action with, so the validation cannot be exercised.

- [ ] CS-03: Monthly budget rejects invalid amount
  - Action: Attempt to save a monthly budget with a negative or zero amount.
  - Expected: The budget is not saved and a validation error is displayed.
  - Bug Report:
    - Issue: Missing Feature / Unreachable Functionality
    - Actual: No monthly-budget form or input exists anywhere in the application (see FT-02). Budgets are fixed display values, so this validation cannot be exercised.

## Interaction

- [X] IX-01: Feedback after logging an expense
  - Action: Save a new expense via the expense form.
  - Expected: A success confirmation (message/toast) appears and the new expense is immediately visible in the list.

- [X] IX-02: Filters update the list instantly
  - Action: Change a filter value (e.g., switch category) while viewing the expense list.
  - Expected: The list refreshes immediately to show the matching expenses without a full page reload.

- [X] IX-03: Resetting filters restores the full list
  - Action: With active filters applied, reset/clear the filters.
  - Expected: The expense list returns to showing all default expenses.

## Content

- [X] CT-01: All summary amounts are labeled in the primary currency
  - Action: Inspect every summary total, budget figure, and chart value on the page.
  - Expected: Each amount is labeled with the primary currency's symbol/code (e.g., "$" or "USD"), with no mixed or unlabeled currencies.

- [ ] CT-02: Chart labels match the actual data
  - Action: Inspect chart titles, axis labels, and legends.
  - Expected: The category chart uses the real category names, the time chart uses the real time periods (e.g., month names), and no placeholder or empty labels appear.
  - Bug Report:
    - Issue: Incorrect/Missing Chart Labels
    - Actual: The "Budget vs Spending" category chart's x-axis shows only emoji icons (🍽️ 🚗 🛍️ 🎬 💡 🏥 ✈️ 📦) instead of the real category names ("Food & Dining", "Transportation", etc.), making category identification ambiguous. Additionally, neither chart has a legend, so the two bar series (budget vs. spending) in the category chart are not labeled. The time chart does use real dates (Oct 26 – Nov 8) and no empty/placeholder labels appear.

- [X] CT-03: Expense list entries are complete and accurate
  - Action: Inspect a row of an expense logged in a foreign currency.
  - Expected: The row displays the original amount with its currency code as entered, plus its date, category, and assigned goal — nothing missing or garbled.
