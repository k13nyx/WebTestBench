All tests executed. Confirmed via DOM scan: no goal or budget input controls exist anywhere (no links/routes, no "Add Goal" text, only the two filter date inputs). Here is the complete result.

# Test Result

## Functionality

- [ ] FT-01: User can create a new financial goal from the default app state.
  - Action: Open the goal section, enter a goal name and target amount, click "Add Goal".
  - Expected: The new goal appears in the goals list with its name and target amount.
  - Bug Report:
    - Issue: Missing functionality (no goal-creation control)
    - Actual: The "Financial Goals" section (`h2: Financial Goals`) only renders existing goal cards (Summer Vacation, Emergency Fund, New Laptop) with progress bars. There is no goal-name input, no target-amount input, and no "Add Goal" button anywhere in the DOM. A full `button`/`input` enumeration returned only: logo, the primary-currency combobox, "Add Expense", "Filters", and the per-expense delete icons. No route/link to a goal editor exists (`document.querySelectorAll('a')` = []).

- [ ] FT-02: User can define a monthly budget per category.
  - Action: Enter an amount for a category in the monthly budget section and confirm.
  - Expected: The category shows the saved budget amount for the selected month.
  - Bug Report:
    - Issue: Missing functionality (no budget input)
    - Actual: The "Budget Categories" section and the "Monthly Budget" summary card are read-only displays (e.g., "Food & Dining $0.00 of $600.00"). No editable amount field or confirm control exists for any category; the only `input` elements present on the page are the two filter date fields (From/To).

- [X] FT-03: User can log an expense in a currency different from the primary currency.
  - Action: Add an expense selecting a non-primary currency (e.g., EUR), enter amount, date, and save.
  - Expected: The expense is saved and displayed in the expense list.

- [X] FT-04: User can assign a category to each logged expense.
  - Action: When adding an expense, select a category from the category selector and save.
  - Expected: The saved expense shows the assigned category in the expense list.

- [X] FT-05: User can choose a primary currency.
  - Action: Select a currency from the primary currency selector and confirm.
  - Expected: The selection is saved and used for all summary displays.

- [X] FT-06: All summaries are displayed in the selected primary currency.
  - Action: Change the primary currency and view the summary/total sections.
  - Expected: Every summary total is shown in the primary currency (correct symbol/format), not in the expense's original currency.

- [X] FT-07: Chart shows spending versus budget by category.
  - Action: Open the by-category chart.
  - Expected: It shows each category with spent amount compared against its budget.

- [X] FT-08: Chart shows spending over time.
  - Action: Open the over-time chart.
  - Expected: It shows expense totals plotted across time periods.

- [X] FT-09: User can filter the expense list by date range.
  - Action: Set a start and end date in the date range filter.
  - Expected: Only expenses whose date falls within the range are listed.

- [X] FT-10: User can filter the expense list by category.
  - Action: Select a single category in the category filter.
  - Expected: Only expenses in that category are listed.

- [X] FT-11: User can filter the expense list by goal.
  - Action: Select a goal in the goal filter.
  - Expected: Only expenses assigned to that goal are listed.

## Constraint

- [X] CS-01: Expense cannot be saved with empty required fields.
  - Action: Attempt to save an expense with amount, date, or category left empty.
  - Expected: Save is blocked and a validation message indicates the missing field(s).

- [ ] CS-02: Goal and budget amounts reject invalid values.
  - Action: Enter zero, a negative number, or non-numeric text for a goal or budget amount and confirm.
  - Expected: The value is rejected and the goal/budget is not saved.
  - Bug Report:
    - Issue: Untestable / Missing goal and budget amount inputs
    - Actual: No goal-amount or monthly-budget amount field exists in the application, so it is impossible to enter zero, negative, or non-numeric values; the validation behavior described cannot occur. (Same root cause as FT-01 / FT-02.)

- [X] CS-03: Currency conversion is applied consistently in summaries.
  - Action: Compare a summary total against the sum of the same expenses converted at the displayed rate.
  - Expected: The summary total equals the converted sum; no expense is counted in its original currency.

- [X] CS-04: Filters returning no matches show an empty state, not stale data.
  - Action: Apply a filter combination that matches no expenses.
  - Expected: An explicit empty/no-results state is shown; no unrelated expenses remain listed.

## Interaction

- [X] IX-01: User receives confirmation after adding an expense.
  - Action: Successfully save a new expense.
  - Expected: A success toast/message confirms the expense was added.

- [X] IX-02: Charts refresh after an expense is added.
  - Action: Add a new expense, then view both charts.
  - Expected: The by-category and over-time charts reflect the newly added expense without a manual reload.

- [X] IX-03: Applied filters are visibly indicated and can be cleared.
  - Action: Apply a date range, category, and goal filter, then use the clear/reset control.
  - Expected: Active filters are shown as selected, and clearing them restores the full expense list.

## Content

- [X] CT-01: Charts are labeled with category names and currency values.
  - Action: Inspect the legends, axis labels, and tooltips of both charts.
  - Expected: Category names and monetary values (in the primary currency) are present and readable.

- [X] CT-02: Displayed amounts use the correct formatting for the primary currency.
  - Action: Switch the primary currency between two options and inspect all summary and chart values.
  - Expected: The correct currency symbol/code and decimal formatting are applied consistently.

---

### Summary of failures
- **FT-01** — FAIL: no UI to create a financial goal (missing functionality).
- **FT-02** — FAIL: no UI to define/edit a monthly budget per category (missing functionality).
- **CS-02** — FAIL: no goal/budget amount inputs exist, so invalid-value rejection is untestable/impossible.

All other checklist items **PASS** (FT-03–FT-11, CS-01, CS-03, CS-04, IX-01–IX-03, CT-01, CT-02).

Note (not a scored item): when the primary currency was switched (USD→EUR→JPY), all summary/chart values converted correctly and consistently, but the monthly-budget totals and goal amounts only had their symbol swapped (e.g., `$2600.00` → `€2600.00` → `¥2600.00`) rather than being re-converted — consistent with budgets/goals being stored in the active primary currency. This did not violate any checklist Expectation as written.