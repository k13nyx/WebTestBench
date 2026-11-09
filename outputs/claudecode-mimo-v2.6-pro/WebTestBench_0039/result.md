All testing is complete (25 tool calls used). Here is the full checklist with updated statuses:

# Test Result

## Functionality
- [X] FT-01: User can create a profile and add income sources.
  - Action: Open the profile form, enter an income source name (e.g., "Salary") and amount, and save.
  - Expected: The income source is saved and listed in the profile with its name and amount.
- [X] FT-02: User can add expense categories with budget amounts.
  - Action: In the profile, add an expense category with a name and a monthly budget amount, then save.
  - Expected: The category is saved and displayed in the profile with its budget amount.
- [X] FT-03: User can add savings goals.
  - Action: In the profile, add a savings goal with a name and target amount, then save.
  - Expected: The savings goal is saved and displayed in the profile with its name and target amount.
- [X] FT-04: User can log a transaction and assign it to a category.
  - Action: Open the transaction form, enter date, description, amount, select an existing expense category, and save.
  - Expected: The transaction is saved and appears in the transaction history with the selected category.
- [X] FT-05: Monthly summary compares actual spending to budget per category.
  - Action: Open the monthly summary view for the current month.
  - Expected: Each expense category is listed with both its budget amount and its actual spending for that month.
- [X] FT-06: User can filter transaction history by date range.
  - Action: Set a start date and end date covering only part of the existing transaction history and apply the filter.
  - Expected: Only transactions dated within the selected range are shown; all others are hidden.
- [X] FT-07: User can filter transaction history by category.
  - Action: Select one expense category in the filter controls and apply the filter.
  - Expected: Only transactions assigned to that category are shown.
- [X] FT-08: User can combine date range and category filters.
  - Action: Apply both a date range and a category selection at the same time.
  - Expected: Only transactions matching both the date range and the selected category are shown.

## Constraint
- [ ] CS-01: Transaction cannot be saved with missing required fields.
  - Action: Submit the transaction form leaving amount blank, then repeat leaving date blank, then repeat with no category selected.
  - Expected: Each submission is rejected with an error; no partial transaction is created.
  - Bug Report:
    - Issue: Incorrect Form Submission — Missing Required Fields Silently Accepted / No Validation Error
    - Actual: With date left blank, the submission was accepted and a transaction was created with a silently substituted default date ("CS01 date blank" appears in history as "Nov 8 • QA Category • -$50"). With no category selected (selector left on its unselected state), the submission was also accepted and saved with the first category silently substituted ("CS01 no category" appears in history as "Nov 8 • Housing • -$50"). Only the blank-amount case was blocked (submit button disabled), and even then no error message was displayed — no case produced the expected rejection error.

- [ ] CS-02: Transaction amount must be a positive number.
  - Action: Enter "0", then "-50", then "abc" as the transaction amount and submit each.
  - Expected: Each submission is rejected with an error; no transaction is created.
  - Bug Report:
    - Issue: Missing Error Feedback — Invalid Amount Silently Blocked Without Error Message
    - Actual: Entering "0" or "-50" leaves the submit button disabled with no error message anywhere on the form (form text contains no error/validation message), so the submission is silently un-responsive rather than "rejected with an error". Entering "abc" is impossible at all — the amount field is `input[type=number]` and refuses text ("Cannot type text into input[type=number]"), with no error shown. No transaction was created in any of the three cases, but the expected rejection error never appears.

- [ ] CS-03: Profile entries require a name and a positive amount.
  - Action: In the income source, expense category, and savings goal forms, submit with a blank name, then with a zero or negative amount.
  - Expected: Each submission is rejected with an error; no unnamed or non-positive entry is saved.
  - Bug Report:
    - Issue: Incorrect Form Submission — Non-Positive Amounts Accepted and Saved in Profile Forms
    - Actual: The income form saved both "BadZero — $0 / monthly" and "BadNeg — -$50 / monthly". The savings goal form saved "BadGoalZero — $0 / $0" and "BadGoalNeg — $0 / -$100". The expense category form saved "BadCatZero" with a $0 budget, and the inline category budget editor accepted a negative value (QA Category's budget could be set to "-$50/mo" with no rejection). Blank names are only prevented by a disabled add button (no error message is shown).

- [X] CS-04: Transaction can only be assigned to a predefined expense category.
  - Action: Open the transaction form's category selector and review the available options.
  - Expected: Only the expense categories defined in the profile are selectable; no empty or free-form invalid category can be assigned.
- [ ] CS-05: Invalid date range is rejected in transaction filters.
  - Action: Set the filter's start date later than its end date and apply the filter.
  - Expected: The filter is rejected or prevented with an error message; the list is not silently mis-filtered.
  - Bug Report:
    - Issue: Missing Validation/Error Feedback — Inverted Date Range Applied Silently
    - Actual: With From = 2025-12-08 and To = 2025-12-01 (start after end), the filter is applied silently with no error message or prevention; the list just shows "No transactions match your filters". The expected rejection with an error message never occurs.

## Interaction
- [ ] IX-01: Saving a transaction gives success feedback.
  - Action: Save a valid transaction and observe the interface immediately afterward.
  - Expected: A success confirmation (e.g., toast or inline message) appears indicating the transaction was saved.
  - Bug Report:
    - Issue: Missing Success Feedback / Unresponsive Confirmation
    - Actual: After saving a valid transaction ("QA Test Transaction", -$75.25, Nov 10, QA Category), the form closed and the entry appeared in the history, but no toast or inline confirmation message appeared — the toast/notification region ("Notifications (F8)") remained empty and no text containing "saved/added/success" was rendered at any point after the save.

- [X] IX-02: Overspending is visually highlighted in the monthly summary.
  - Action: View the monthly summary for a category whose actual spending exceeds its budget (use existing default data).
  - Expected: The over-budget category is visually distinguished (e.g., warning color or "over budget" indicator) from categories within budget.
- [X] IX-03: Transaction list updates when filters are applied or cleared.
  - Action: Apply a filter, then clear/reset it.
  - Expected: The transaction list refreshes immediately in both cases, showing filtered results and then the full list again.
- [ ] IX-04: Invalid form input shows an error message at the point of entry.
  - Action: Submit the transaction form with an invalid amount and observe the form.
  - Expected: An error message is displayed near the offending field, and the entered data is not silently discarded.
  - Bug Report:
    - Issue: Missing Inline Error Message at Point of Entry
    - Actual: With an invalid amount ("0", then "-50") in the amount field, no error message is displayed near the amount field (or anywhere on the form); the submit button merely stays disabled. Entered data is retained (description and amount values persist in the fields), but the required error message at the offending field never appears.

## Content
- [X] CT-01: Transaction history entries display accurate details.
  - Action: Compare a saved transaction's date, description, amount, and category in the history list against what was entered.
  - Expected: All four fields are displayed exactly as entered, with no truncation or value drift.
- [X] CT-02: Monthly summary actuals equal the sum of the month's transactions per category.
  - Action: Sum the amounts of all transactions in one category for the displayed month and compare to that category's actual spending in the summary.
  - Expected: The summary's actual spending figure equals the computed sum for every category shown.
- [X] CT-03: Profile displays all saved entries with correct values.
  - Action: Review the profile's income sources, expense categories, and savings goals lists.
  - Expected: Every saved entry appears with its exact name and amount/target as entered.