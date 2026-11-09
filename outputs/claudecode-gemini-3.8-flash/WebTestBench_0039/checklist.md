# Test Checklist

## Functionality
- [ ] FT-01: Add income source to profile
  - Action: Navigate to profile settings, enter an income source name and monthly amount, then click "Add Income".
  - Expected: The income source is saved and listed under the user's income profile.
- [ ] FT-02: Create an expense category with budget limit
  - Action: In the budget setup section, enter a category name (e.g., "Groceries"), enter a monthly budget limit, and click "Save Category".
  - Expected: The category is created and appears in the budget list with its allocated limit.
- [ ] FT-03: Create a savings goal in profile
  - Action: Navigate to the savings goal section, enter a goal title and target amount, and click "Create Goal".
  - Expected: The savings goal is added and displayed in the user profile goals list.
- [ ] FT-04: Log an individual expense transaction with category assignment
  - Action: Open the transaction form, enter an amount, date, and description, select an existing category from the dropdown, and click "Submit Transaction".
  - Expected: The transaction is saved and appears in the transaction history associated with the selected category.
- [ ] FT-05: Filter transaction history by category
  - Action: In the transaction history section, select a specific category from the category filter dropdown and apply.
  - Expected: The table updates to show only transactions assigned to the selected category.
- [ ] FT-06: Filter transaction history by date range
  - Action: In the transaction history section, enter a start date and an end date, then click "Apply Filter".
  - Expected: The transaction list updates to display only transactions with dates falling within the selected range.
- [ ] FT-07: Filter transaction history by both category and date range simultaneously
  - Action: Select a specific category and set a start and end date range, then click "Apply Filter".
  - Expected: Only transactions matching both the chosen category and date range are displayed in the list.

## Constraint
- [ ] CS-01: Prevent logging a transaction without required fields
  - Action: Leave the amount and category fields blank in the transaction form and click "Submit Transaction".
  - Expected: The transaction is not submitted, and inline validation errors appear on the empty required fields.
- [ ] CS-02: Prevent negative or non-numeric transaction amounts
  - Action: Enter "-50" or "abc" in the transaction amount field and submit the form.
  - Expected: Form submission is blocked, and an error message indicating a positive numeric value is required appears.
- [ ] CS-03: Prevent invalid date range selection where start date exceeds end date
  - Action: Set the filter start date to a date later than the end date and click "Apply Filter".
  - Expected: The filter is not applied, and an error message indicates that the start date cannot be after the end date.
- [ ] CS-04: Prevent duplicate expense category creation
  - Action: Attempt to create a new category using the name of an already existing category and click "Save Category".
  - Expected: Category creation is rejected, and a "Category name already exists" error message is displayed.

## Interaction
- [ ] IX-01: Visual alert indicator for overspent category in monthly summary
  - Action: View the monthly summary table for a category where actual spending exceeds its allocated budget.
  - Expected: The category row or card displays a prominent visual highlight (e.g., red text or warning badge indicating overspending).
- [ ] IX-02: Success feedback on transaction creation
  - Action: Fill in all valid transaction details and click "Submit Transaction".
  - Expected: A confirmation toast notification appears confirming the transaction was logged, and the input fields reset.
- [ ] IX-03: Reset active transaction filters
  - Action: With active date and category filters applied, click the "Clear Filters" button.
  - Expected: Filter controls return to default states and the transaction history restores the complete, unfiltered list.

## Content
- [ ] CT-01: Monthly summary actual vs. budget calculation accuracy
  - Action: Navigate to the monthly summary dashboard.
  - Expected: Each category displays the assigned budget amount, the sum of logged transactions for the month, and the remaining balance.
- [ ] CT-02: Transaction table data integrity
  - Action: Inspect any logged row in the transaction history table.
  - Expected: Each record accurately displays date, description, assigned category name, and monetary amount.
- [ ] CT-03: Profile financial overview summary display
  - Action: View the profile summary dashboard.
  - Expected: The page displays accurate totals for all combined income sources, total budgeted expenses, and active savings goals.