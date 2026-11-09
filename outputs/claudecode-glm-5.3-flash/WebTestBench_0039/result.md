All 19 checklist items have been executed. Here are the complete results:

# Test Result

## Functionality
- [X] FT-01: Create a profile with an income source
  - Action: Open the profile creation page, enter an income source (e.g., "Salary", $3,000/month), and save the profile.
  - Expected: Profile is created and the income source "Salary" with amount $3,000 is listed on the profile.
  - Note: App opens with a pre-seeded profile (Alex Johnson). Income source "Salary, $3,000 / monthly" was added via Profile Settings → Income and is listed; dashboard "Expected income" updated from $6,300 to $9,300.
- [X] FT-02: Add an expense category with a budget amount
  - Action: In the profile, add an expense category (e.g., "Groceries") with a monthly budget of $500 and save.
  - Expected: "Groceries" appears in the expense categories list with its $500 budget shown.
- [X] FT-03: Add a savings goal
  - Action: Add a savings goal (e.g., "Vacation", target $2,000) to the profile and save.
  - Expected: "Vacation" appears in the savings goals list with its $2,000 target shown.
  - Note: A seeded "Vacation" goal ($1,200/$3,000) already existed, so the new goal was added as "Vacation Fund"; it appears in the goals list with the $2,000 target shown ($0 / $2,000).
- [X] FT-04: Log an income transaction
  - Action: Log a new transaction with amount $3,000, type income, description "Paycheck", date today, and save.
  - Expected: The transaction appears in the transaction history with its amount, date, and description.
- [X] FT-05: Log an expense transaction assigned to a category
  - Action: Log an expense of $120, assign it to the "Groceries" category, and save.
  - Expected: The transaction appears in history assigned to "Groceries", and Groceries' actual spending in the summary increases by $120.
- [ ] FT-06: Monthly summary compares actual spending vs. budget per category
  - Action: Open the monthly summary for the current month after logging transactions in at least two categories.
  - Expected: Each category shows its budgeted amount, actual spending, and the difference/remaining amount, matching the logged transactions.
  - Bug Report:
    - Issue: Missing Information — per-category remaining/difference not displayed
    - Actual: The "Budget vs. Actual" section shows only "actual / budget" pairs per category (e.g., "Food & Dining $50 / $600"). The difference/remaining amount is displayed only for overspent categories ("Groceries … Over budget by $100"); under-budget categories show no remaining amount anywhere (the only "Remaining" figure is the global total, $3,450). Budgeted and actual amounts themselves match the logged transactions ($600 Groceries = $120 + $480; $50 Food & Dining).
- [X] FT-07: Filter transactions by date range
  - Action: Set a date range covering only last month and apply it to the transaction history.
  - Expected: Only transactions dated within that range are displayed; all others are hidden.
  - Note: Range 2026-10-01 → 2026-10-31 showed only "October haircut, Oct 15, Health, -$30"; all other transactions were hidden.
- [X] FT-08: Filter transactions by category
  - Action: Select the "Groceries" category filter in the transaction history.
  - Expected: Only transactions assigned to "Groceries" are displayed.

## Constraint
- [ ] CS-01: Cannot save transaction with missing required fields
  - Action: Open the add-transaction form, leave the amount and/or category empty, and click Save.
  - Expected: The transaction is not created and a validation message indicates the missing required field(s).
  - Bug Report:
    - Issue: Missing Validation Feedback
    - Actual: No invalid transaction is created (the "Add Transaction" button stays disabled while amount, category, or description is empty), but no validation message, error text, aria-invalid marker, or alert is shown anywhere in the form indicating which field is missing — the user gets no explanation of why the button is disabled.
- [ ] CS-02: Amount must be a valid positive number
  - Action: Enter an amount of "0", "-50", or non-numeric text (e.g., "abc") in the transaction amount field and save.
  - Expected: The transaction is rejected with a validation error and no invalid transaction appears in history.
  - Bug Report:
    - Issue: Missing Validation Feedback
    - Actual: With amount "0" or "-50" the save button remains disabled and no transaction is created (non-numeric "abc" is blocked by the number input itself), but no validation error message is ever displayed to explain the rejection.
- [ ] CS-03: Duplicate category names are not allowed
  - Action: Add an expense category named "Groceries" when "Groceries" already exists, then save.
  - Expected: The duplicate is rejected with an error message and no second "Groceries" category is created.
  - Bug Report:
    - Issue: Incorrect Form Submission — duplicate accepted
    - Actual: Adding "Groceries" with budget $300 while "Groceries" ($500) already existed was accepted silently — two "Groceries" categories ("Budget: $500/mo" and "Budget: $300/mo") appeared in the list with no error message. (Duplicate removed manually after the test.)
- [ ] CS-04: Savings goal target must be a positive amount
  - Action: Add a savings goal with a target of "0" or a negative value and save.
  - Expected: The goal is rejected with a validation error and is not added to the goals list.
  - Bug Report:
    - Issue: Incorrect Form Submission — invalid data accepted
    - Actual: Goals "Test Zero" ($0 / $0) and "Test Neg" ($0 / -$50) were both created with no validation error. The dashboard also rendered a broken "NaN% complete" progress label for the $0-target goal. (Both test goals removed manually after the test.)

## Interaction
- [ ] IX-01: Success feedback after saving a transaction
  - Action: Log a valid transaction and save it.
  - Expected: A success confirmation (message/toast) appears, and the new transaction is immediately visible in the transaction list without a page reload.
  - Bug Report:
    - Issue: Missing Success Feedback
    - Actual: The new transaction appears immediately at the top of the list without a page reload (correct), but no success confirmation, toast, or notification of any kind appears after saving — the notification/toast regions were polled for ~1.2s after each of three saves and remained empty.
- [X] IX-02: Summary highlights overspending categories
  - Action: In a category, log expenses exceeding its budget (e.g., $600 spent on a $500 "Groceries" budget) and view the monthly summary.
  - Expected: The "Groceries" category is visually highlighted (e.g., red indicator/"over budget" label) and shows the overspent amount.
  - Note: Groceries row shows a red (destructive) progress bar, an alert icon, and red text "Over budget by $100".
- [X] IX-03: Filters update the transaction list dynamically
  - Action: Apply or change a date-range or category filter and observe the transaction list.
  - Expected: The list refreshes immediately to show only matching transactions, and clearing the filter restores the full history.
  - Note: Applying/clearing filters updates the list instantly without reload; "Clear filters" restored all entries (Paycheck, October haircut, Monthly rent, etc.).
- [X] IX-04: Monthly summary responds to newly logged transactions
  - Action: With the monthly summary open, log a new expense and return to the summary.
  - Expected: The affected category's actual spending and remaining budget update to include the new transaction.
  - Note: After logging $50 Food & Dining, the Budget overview updated to Total Spent $650 and "Food & Dining $50 / $600".

## Content
- [ ] CT-01: Transaction history shows complete details for each entry
  - Action: Open the transaction history and inspect logged transactions.
  - Expected: Each entry displays its date, description, amount, and assigned category, with amounts correctly formatted as currency.
  - Bug Report:
    - Issue: Incorrect Currency Formatting
    - Actual: Each entry does show date, description, amount, and category, but seeded amounts are not formatted to two decimal places: "Grocery shopping … -$85.5" (should be -$85.50) and "Pharmacy … -$42.3" (should be -$42.30). All other amounts (e.g., +$3,000, -$120, -$1,500) are formatted correctly.
- [X] CT-02: Monthly summary shows period and totals consistent with logged data
  - Action: View the monthly summary for the current month.
  - Expected: The summary is labeled with the month it covers, and totals (total income, total spending, per-category amounts) exactly match the logged transactions for that month.
  - Note: "November 2026 • Total budget: $4,100"; Monthly Income $3,000, Total Spent $650, Groceries $600, Food & Dining $50 — all exactly match the logged transactions.
- [X] CT-03: Profile page accurately displays all saved profile data
  - Action: Open the profile page after saving income sources, categories, and goals.
  - Expected: Every saved income source, expense category (with budget), and savings goal (with target) is listed with correct names and amounts — no missing or altered entries.
  - Note: Income shows Salary $5,500, Freelance $800, Salary $3,000; Categories shows all 9 including Groceries $500/mo; Goals shows all 4 including Vacation Fund $0/$2,000 — no missing or altered entries.

**Summary: 13 PASS / 6 FAIL.** Key defects: no validation error messages (CS-01/CS-02), duplicate categories accepted (CS-03), non-positive goal targets accepted with a NaN display bug (CS-04), no success toast on save (IX-01), missing per-category remaining amounts in the summary (FT-06), and two amounts rendered without trailing currency zeros (CT-01).