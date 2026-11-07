# Test Checklist

## Functionality
- [ ] FT-01: Create a profile with income sources
  - Action: Open profile setup and add at least one income source (e.g., name and amount).
  - Expected: The income source is saved and visible in the profile.

- [ ] FT-02: Add expense categories to the profile
  - Action: In profile setup, add at least one expense category (e.g., "Groceries").
  - Expected: The expense category is saved and listed in the profile.

- [ ] FT-03: Set savings goals in the profile
  - Action: In profile setup, add a savings goal (e.g., name and target amount).
  - Expected: The savings goal is saved and displayed in the profile.

- [ ] FT-04: Log an individual transaction
  - Action: Open the transaction log form and enter an amount, date, and description, then submit.
  - Expected: The transaction is recorded and appears in the transaction history.

- [ ] FT-05: Assign a transaction to an expense category
  - Action: When logging a transaction, select an existing expense category from the category field.
  - Expected: The transaction is saved with the selected category assigned.

- [ ] FT-06: View monthly summary comparing actual vs budget per category
  - Action: Open the monthly summary view.
  - Expected: For each category, actual spending is shown alongside its budget.

- [ ] FT-07: Filter transaction history by date range
  - Action: Set a start and end date in the transaction history filter and apply it.
  - Expected: Only transactions within the selected date range are displayed.

- [ ] FT-08: Filter transaction history by category
  - Action: Select a category in the transaction history filter and apply it.
  - Expected: Only transactions assigned to the selected category are displayed.

## Constraint
- [ ] CS-01: Profile cannot be saved with empty required fields
  - Action: Attempt to save the profile without providing a required field (e.g., no income source).
  - Expected: Save is blocked and a validation error identifies the missing required field.

- [ ] CS-02: Transaction cannot be logged with invalid required fields
  - Action: Attempt to submit a transaction with a missing amount or invalid date.
  - Expected: Submission is blocked and a validation error identifies the invalid field.

- [ ] CS-03: Transaction cannot be assigned to a non-existent category
  - Action: Attempt to log a transaction and select a category that is not in the profile.
  - Expected: The invalid category is unavailable or submission is rejected.

## Interaction
- [ ] IX-01: Overspending is visually highlighted in the monthly summary
  - Action: View the monthly summary for a category whose actual spending exceeds its budget.
  - Expected: The overspent category is visually highlighted (e.g., color/indicator) to draw attention.

- [ ] IX-02: Confirmation is shown after saving profile and logging transaction
  - Action: Save the profile, then log a transaction.
  - Expected: A success confirmation (toast/message) appears after each action.

## Content
- [ ] CT-01: Monthly summary displays each category's budget and actual amounts
  - Action: Open the monthly summary.
  - Expected: Each listed category shows its name, budgeted amount, and actual spent amount, all relevant and complete.

- [ ] CT-02: Transaction history shows relevant transaction fields
  - Action: Open the transaction history.
  - Expected: Each transaction displays date, amount, assigned category, and description, all correctly populated.