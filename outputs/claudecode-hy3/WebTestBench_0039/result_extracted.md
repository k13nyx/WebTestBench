# Test Result

## Functionality
- [X] FT-01: Create a profile with income sources
  - Action: Open profile setup and add at least one income source (e.g., name and amount).
  - Expected: The income source is saved and visible in the profile.
- [X] FT-02: Add expense categories to the profile
  - Action: In profile setup, add at least one expense category (e.g., "Groceries").
  - Expected: The expense category is saved and listed in the profile.
- [X] FT-03: Set savings goals in the profile
  - Action: In profile setup, add a savings goal (e.g., name and target amount).
  - Expected: The savings goal is saved and displayed in the profile.
- [X] FT-04: Log an individual transaction
  - Action: Open the transaction log form and enter an amount, date, and description, then submit.
  - Expected: The transaction is recorded and appears in the transaction history.
- [X] FT-05: Assign a transaction to an expense category
  - Action: When logging a transaction, select an existing expense category from the category field.
  - Expected: The transaction is saved with the selected category assigned.
- [X] FT-06: View monthly summary comparing actual vs budget per category
  - Action: Open the monthly summary view.
  - Expected: For each category, actual spending is shown alongside its budget.
- [X] FT-07: Filter transaction history by date range
  - Action: Set a start and end date in the transaction history filter and apply it.
  - Expected: Only transactions within the selected date range are displayed.
- [X] FT-08: Filter transaction history by category
  - Action: Select a category in the transaction history filter and apply it.
  - Expected: Only transactions assigned to the selected category are displayed.

## Constraint
- [ ] CS-01: Profile cannot be saved with empty required fields
  - Action: Attempt to save the profile without providing a required field (e.g., no income source).
  - Expected: Save is blocked and a validation error identifies the missing required field.
  - Bug Report:
    - Issue: Missing validation error message (silent block)
    - Actual: In Profile Settings, clearing the required "Your Name" field and clicking Save keeps the dialog open (save is blocked — the name was not saved, top-right label remained unchanged), but no validation error text or invalid-field indicator appears. The field has `required=false` and `aria-invalid=null`; there is no message identifying the missing required field.
- [ ] CS-02: Transaction cannot be logged with invalid required fields
  - Action: Attempt to submit a transaction with a missing amount or invalid date.
  - Expected: Submission is blocked and a validation error identifies the invalid field.
  - Bug Report:
    - Issue: Missing validation error message (disabled submit without field-level error)
    - Actual: With the Amount field left empty (description, category, and date filled), the "Add Transaction" submit button is correctly disabled (`submitDisabled=true`, submission blocked), but no validation error text or invalid-field indicator appears to identify that Amount is the missing/invalid required field (`aria-invalid=null`, no error message in the dialog).
- [X] CS-03: Transaction cannot be assigned to a non-existent category
  - Action: Attempt to log a transaction and select a category that is not in the profile.
  - Expected: The invalid category is unavailable or submission is rejected.

## Interaction
- [X] IX-01: Overspending is visually highlighted in the monthly summary
  - Action: View the monthly summary for a category whose actual spending exceeds its budget.
  - Expected: The overspent category is visually highlighted (e.g., color/indicator) to draw attention.
- [ ] IX-02: Confirmation is shown after saving profile and logging transaction
  - Action: Save the profile, then log a transaction.
  - Expected: A success confirmation (toast/message) appears after each action.
  - Bug Report:
    - Issue: No success confirmation after save/log
    - Actual: After saving the profile (name) and after logging transactions, no confirmation toast or success message appears. Verified via a MutationObserver and DOM checks: no `data-sonner-toaster` element mounts, no `aria-live`/`role=alert`/`role=status` content is produced, and no on-screen success text is shown. The only feedback is the item appearing in its respective list.

## Content
- [X] CT-01: Monthly summary displays each category's budget and actual amounts
  - Action: Open the monthly summary.
  - Expected: Each listed category shows its name, budgeted amount, and actual spent amount, all relevant and complete.
- [X] CT-02: Transaction history shows relevant transaction fields
  - Action: Open the transaction history.
  - Expected: Each transaction displays date, amount, assigned category, and description, all correctly populated.
