# Test Checklist

## Functionality
- [ ] FT-01: Create a new financial goal
  - Action: Navigate to the Financial Goals section, enter a goal name, target amount, and target completion date, then click "Save Goal".
  - Expected: The new goal appears in the active goals list with its name, target amount, and progress indicators.
- [ ] FT-02: Define a monthly category budget
  - Action: In the Monthly Budgets section, select an existing category from the dropdown, enter a budget limit amount, and click "Set Budget".
  - Expected: The monthly budget is saved and displayed under the corresponding category with the specified limit.
- [ ] FT-03: Log an expense with a non-primary currency and assign a category and goal
  - Action: Fill out the expense form with an amount, select a non-primary currency (e.g., "EUR"), choose a category, select an associated financial goal, and click "Add Expense".
  - Expected: The expense is saved and listed in the expense table with its original currency amount, assigned category, and linked goal.
- [ ] FT-04: Switch primary currency and convert summaries
  - Action: Change the primary currency dropdown setting (e.g., from "USD" to "GBP").
  - Expected: All summary metrics, budget limits, and expense totals automatically recalculate and display converted values in GBP.
- [ ] FT-05: Filter expense list by date range
  - Action: In the expense filter controls, set a start date and end date covering a past week, then click "Apply Filter".
  - Expected: The expense list updates to display only transactions with dates falling within the selected start and end dates.
- [ ] FT-06: Filter expense list by category
  - Action: Select a specific category (e.g., "Dining Out") from the expense category filter dropdown.
  - Expected: The expense list displays only transactions assigned to "Dining Out".
- [ ] FT-07: Filter expense list by financial goal
  - Action: Select a specific goal (e.g., "Emergency Fund") from the goal filter dropdown.
  - Expected: The expense list updates to display only transactions linked to "Emergency Fund".

## Constraint
- [ ] CS-01: Prevent logging an expense with missing required fields
  - Action: Leave the amount and category fields blank in the expense form and click "Add Expense".
  - Expected: The form is not submitted, and required field error messages are displayed beneath the empty inputs.
- [ ] CS-02: Prevent non-positive values for expense amounts and budgets
  - Action: Enter "0" or "-25" into the expense amount or budget limit input and attempt to save.
  - Expected: The submission is blocked, and an error message states that the amount must be greater than zero.
- [ ] CS-03: Restrict invalid date range selection in expense filters
  - Action: Select a filter start date that is later than the selected end date and click "Apply Filter".
  - Expected: The filter action is blocked, and an error message indicates the start date must precede or equal the end date.
- [ ] CS-04: Prevent duplicate budget creation for the same category and month
  - Action: Attempt to add a new budget for a category that already has an assigned budget for the current month.
  - Expected: The system blocks creation of a duplicate entry and prompts the user to edit the existing category budget instead.

## Interaction
- [ ] IX-01: Real-time update of spending vs. budget chart upon adding an expense
  - Action: Add a new expense under a budgeted category and observe the "Spending vs. Budget by Category" chart.
  - Expected: The corresponding category bar or gauge dynamically increases its spent value without requiring a full page refresh.
- [ ] IX-02: Tooltip details on spending over time chart
  - Action: Hover the mouse cursor over a data point or bar on the "Spending Over Time" chart.
  - Expected: A tooltip appears showing the specific date/period and total expenditure converted to the primary currency.
- [ ] IX-03: Reset active filters
  - Action: Apply category, goal, and date range filters, then click the "Reset Filters" button.
  - Expected: All filter selectors return to their default all/unfiltered states, and the full default expense list is restored.

## Content
- [ ] CT-01: Primary currency denomination across all summary cards
  - Action: Inspect the "Total Budget", "Total Spent", and "Remaining Balance" overview cards.
  - Expected: Every summary value displays the currency symbol or ISO code matching the selected primary currency.
- [ ] CT-02: Spending vs. Budget by Category chart data representation
  - Action: View the "Spending vs. Budget by Category" chart.
  - Expected: Each budgeted category is clearly labeled, displaying both the allocated budget limit and current spent amount side-by-side or as a ratio.
- [ ] CT-03: Spending Over Time chart axes and trend line
  - Action: View the "Spending Over Time" chart.
  - Expected: The horizontal axis displays chronological time intervals (e.g., days/months) and the vertical axis displays monetary amounts in the primary currency.
- [ ] CT-04: Multi-currency expense item display
  - Action: Locate a foreign-currency transaction in the expense list.
  - Expected: The row displays the transaction's original amount with its currency code alongside the converted equivalent in the primary currency.