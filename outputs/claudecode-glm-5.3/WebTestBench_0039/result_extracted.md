# Test Result

## Functionality

- [X] FT-01: User can create a simple profile with an income source
  - Action: Open the profile setup page, enter a profile name and at least one income source (e.g., "Salary") with a monthly amount, then save.
  - Expected: Profile is created and the income source with its amount is displayed on the profile page.
  - (Verified: opened Profile Settings → Income tab, added "Side Gig" with $400 monthly; it appeared in the income sources list as "Side Gig — $400 / monthly", alongside existing "Salary — $5,500 / monthly"; dashboard expected income updated from $6,300 to $6,700.)

- [X] FT-02: User can add an expense category with a monthly budget
  - Action: In the expense categories section, add a category (e.g., "Groceries") with a monthly budget amount, then save.
  - Expected: The new category with its budget amount appears in the category list.
  - (Verified: added "Groceries" with $350 budget; category list shows "Groceries — Budget: $350/mo"; it also appears in the Budget vs. Actual summary and the total budget updated to $3,950.)

- [X] FT-03: User can add a savings goal
  - Action: In the savings goals section, add a goal (e.g., "Emergency Fund") with a target amount, then save.
  - Expected: The savings goal with its target amount appears in the goals list.
  - (Verified: added "New Laptop" with target $2,000 (current $300); goals list shows "New Laptop — $300 / $2,000" and the dashboard shows it with "15% complete, $1,700 to go"; total savings updated to $15,000 with 4 active goals.)

- [X] FT-04: User can log a transaction and assign it to a category
  - Action: Open the transaction log, fill in amount, date, and description, select an expense category from the category dropdown, then save.
  - Expected: Transaction is saved and appears in the transaction history with its amount, date, description, and assigned category.
  - (Verified: saved $120.75, "Weekend grocery run", category "Groceries", date 2026-11-08; history shows "Weekend grocery run — Nov 8 • Groceries — -$120.75".)

- [X] FT-05: Monthly summary compares actual spending to budget for each category
  - Action: Open the monthly summary for the current month.
  - Expected: Every expense category shows both its budgeted amount and its actual spent amount for that month.
  - (Verified: Budget Overview for November 2026 shows all 9 categories with actual/budget, e.g., "Housing $0 / $1,500", "Other $10 / $200", "Groceries $620.75 / $350".)

- [X] FT-06: Transaction history can be filtered by date range
  - Action: In the transaction history, set a start and end date that covers only part of the default transactions, then apply the filter.
  - Expected: Only transactions dated within the selected range are displayed.
  - (Verified: with From=2025-12-01, To=2025-12-05, exactly 6 in-range transactions displayed — Monthly rent (Dec 1), Grocery shopping (Dec 2), Gas station (Dec 3), Electric bill (Dec 4), Restaurant dinner (Dec 5), Monthly salary (Dec 1); all Dec 6+ and Nov 2026 transactions were excluded.)

- [X] FT-07: Transaction history can be filtered by category
  - Action: In the transaction history, select a single expense category in the category filter, then apply.
  - Expected: Only transactions assigned to the selected category are displayed.
  - (Verified: selecting "Housing" in the category filter displays only "Monthly rent — Dec 1 • Housing — -$1,500"; all other transactions are filtered out.)

## Constraint

- [ ] CS-01: Transaction cannot be saved with empty required fields
  - Action: Open the add-transaction form, leave amount (and/or date and category) empty, and attempt to save.
  - Expected: Transaction is not saved and a validation message identifies the missing required field(s).
  - Bug Report:
    - Issue: Missing validation feedback
    - Actual: With description ("Test transaction"), category ("Groceries"), and date filled but the amount empty, the "Add Transaction" button is disabled and clicking does nothing — no validation message identifying the missing amount is displayed. Same behavior with the date cleared (button disabled, no message). The transaction is indeed not saved, but the only feedback is the silently disabled button, not a validation message naming the missing required field(s).

- [ ] CS-02: Transaction cannot be saved with an invalid amount
  - Action: Enter a non-numeric value (e.g., "abc") or a negative number (e.g., "-50") in the amount field and attempt to save.
  - Expected: Transaction is rejected with an error message and no transaction is created.
  - Bug Report:
    - Issue: Missing error message on invalid amount
    - Actual: The amount field is a native number input (type=number, min=0, step=0.01); non-numeric characters cannot be entered at all, and entering "-50" (or "0") causes the "Add Transaction" button to become disabled (HTML validity: rangeUnderflow=true) with no error message rendered anywhere in the dialog. The transaction is not created, but the rejection is silent — no error message is shown.

- [X] CS-03: Logging a transaction that exceeds a category's budget is permitted
  - Action: Log a transaction whose amount is larger than the remaining budget of its assigned category.
  - Expected: Transaction is saved successfully; overspending is handled via the summary, not blocked at entry.
  - (Verified: Groceries had $229.25 remaining ($350 − $120.75); a $500 "Big grocery haul" transaction in Groceries was saved successfully and appears in history; the Budget page flags it "Over budget by $270.75" rather than blocking entry.)

- [X] CS-04: Date range filter with start date after end date returns no transactions
  - Action: Set the history filter's start date later than its end date, then apply.
  - Expected: No transactions are displayed (or an empty-state / invalid-range message appears); the full history is NOT returned.
  - (Verified: with From=2025-12-10, To=2025-12-01 and category "All Categories", 0 transactions are displayed and the empty state "No transactions match your filters" appears; the full history is not returned.)

## Interaction

- [X] IX-01: Overspending is visually highlighted in the monthly summary
  - Action: In the monthly summary, locate a category whose actual spending exceeds its budget.
  - Expected: That category is visually distinguished (e.g., warning color or "over budget" badge) from categories within budget.
  - (Verified: the Groceries row ($620.75 / $350) is distinguished by an alert icon next to its name, a "Over budget by $270.75" message with class `text-destructive` (warning/red color), and a progress bar with `[&>div]:bg-destructive` (red fill), while within-budget categories use the default neutral styling.)

- [ ] IX-02: Confirmation appears after a transaction is saved
  - Action: Fill and save a valid transaction.
  - Expected: A success message or toast confirms the transaction was logged.
  - Bug Report:
    - Issue: Missing save confirmation
    - Actual: After saving valid transactions (including via a real button click, e.g., "Big grocery haul" and "Weekend grocery run"), no success message or toast appears; the dialog simply closes. The Sonner notifications region ("Notifications (F8)") remains empty — confirmed by DOM polling for 4 continuous seconds immediately after a save (no `[data-sonner-toast]`, `[role="status"]`, or `[role="alert"]` elements ever appear).

- [X] IX-03: New transaction appears immediately without a page reload
  - Action: Save a valid transaction, then open the transaction history and monthly summary.
  - Expected: The new transaction and its updated category totals appear without manually refreshing the page.
  - (Verified: each saved transaction instantly appeared at the top of the transaction history with no reload, and the Budget page subsequently showed the updated totals — Groceries $620.75/$350 and Other $10/$200, Total Spent $630.75 — purely via SPA navigation; the page URL never reloaded.)

- [X] IX-04: Clearing filters restores the full transaction history
  - Action: Apply a date or category filter, then click "Clear filters" (or equivalent reset control).
  - Expected: The complete default transaction history is displayed again.
  - (Verified: after applying the Housing category filter plus an inverted date range, clicking "Clear filters" reset the category to "All Categories", cleared both dates, and restored all 17 transactions.)

## Content

- [X] CT-01: Transaction history entries display complete, relevant details
  - Action: Inspect the entries in the transaction history.
  - Expected: Each entry shows date, description, amount, and assigned category, consistent with the logged data.
  - (Verified: e.g., "Coffee shop — Nov 8 • Other — -$10", "Weekend grocery run — Nov 8 • Groceries — -$120.75", "Monthly rent — Dec 1 • Housing — -$1,500"; every entry consistently shows date, description, amount, and category matching the logged data.)

- [ ] CT-02: Category filter options match the expense categories defined in the profile
  - Action: Open the category filter in the transaction history and compare its options against the profile's expense category list.
  - Expected: The filter lists exactly the defined expense categories — no missing or extra options.
  - Bug Report:
    - Issue: Extra filter option
    - Actual: The profile defines 9 expense categories (Housing, Food & Dining, Transportation, Utilities, Entertainment, Shopping, Health, Other, Groceries). The history's category filter lists all 9 (no missing), but also includes an extra "Income" option (plus the "All Categories" default), so the filter does not list exactly the defined expense categories.

- [X] CT-03: Summary figures are arithmetically correct
  - Action: For one category, sum its displayed transactions for the current month and compare with the summary's actual-spending figure.
  - Expected: The summary's actual-spending amount equals the sum of that category's transactions for the month.
  - (Verified: Groceries transactions for November 2026 = $120.75 + $500 = $620.75, which exactly matches the summary's "Groceries $620.75 / $350"; cross-check: Other = $10 (Coffee shop) matches "Other $10 / $200", and Total Spent $630.75 = $620.75 + $10.)
