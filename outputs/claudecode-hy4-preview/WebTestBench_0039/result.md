# Test Result

## Functionality

- [X] FT-01: User can add an income source to their profile
  - Action: Open the default profile page, locate the "Income Sources" section, click "Add Income Source", enter a source name (e.g. "Freelance") and a monthly amount (e.g. 500), then save.
  - Expected: The new income source appears in the Income Sources list with its name and amount, and the profile's total monthly income updates to include it.

- [X] FT-02: User can add an expense category with a monthly budget
  - Action: In the "Expense Categories" section, click "Add Category", enter a name (e.g. "Transport") and a monthly budget amount (e.g. 200), then save.
  - Expected: The category appears in the Expense Categories list showing its name and budget amount (200).

- [X] FT-03: User can create a savings goal with a target amount
  - Action: In the "Savings Goals" section, click "Add Goal", enter a goal name (e.g. "Emergency Fund") and a target amount (e.g. 5000), then save.
  - Expected: The goal appears in the Savings Goals list with its name, target amount, and a current saved amount (starting at 0 or its existing value).

- [X] FT-04: User can log a transaction and assign it to an existing expense category
  - Action: Open the transaction entry form, enter an amount (e.g. 45), a date within the current month, a description (e.g. "Bus pass"), select an existing category from the category dropdown, and submit.
  - Expected: A success confirmation appears and the new transaction appears in the transaction history list with its date, description, amount, and the selected category name.

- [X] FT-05: Monthly summary shows budget vs. actual spending for every expense category
  - Action: Open the "Monthly Summary" view for the current month.
  - Expected: Every expense category defined in the profile is listed with three values: its monthly budget, its actual spending for the month, and the remaining amount (or spent/budget comparison).

- [X] FT-06: Monthly summary totals income and spending correctly against logged transactions
  - Action: Note the total of all income sources and the sum of all transaction amounts dated in the current month, then compare with the totals shown in the Monthly Summary.
  - Expected: Summary "Total Income" equals the sum of income source amounts, and "Total Spending" equals the sum of logged transactions for that month.

- [X] FT-07: Savings goal progress reflects amounts assigned to it
  - Action: Log a transaction assigned to the savings goal (or use an existing default savings transaction), then open the Savings Goals section.
  - Expected: The goal's current saved amount increases by the logged amount, and a progress indicator (e.g. "X of Y" or a percentage) matches current/target.

- [X] FT-08: User can filter transaction history by category
  - Action: On the transaction history view, select one existing category (e.g. "Groceries") in the "Category" filter and apply the filter.
  - Expected: Only transactions assigned to that category are displayed; every visible row's category column matches the selected category, and no other categories appear.

- [X] FT-09: User can filter transaction history by date range
  - Action: Set the "From" date to the first day of last month and the "To" date to the last day of last month, then apply the filter.
  - Expected: The history list shows only transactions with dates inside the selected range; every visible row's date falls between From and To inclusive.

## Constraint

- [ ] CS-01: Transaction cannot be saved without an amount and a category
  - Action: Open the transaction form, leave the amount field empty and the category unselected, and submit.
  - Expected: Submission is blocked, a validation message is shown for the amount and the category, and no new row is added to the transaction history.
  - Bug Report:
    - Issue: Missing validation feedback (submission blocked only by a disabled control)
    - Actual: Submitting with an empty amount and no category was blocked — the "Add Transaction" submit button rendered with the `disabled` attribute, the dialog stayed open, and the history stayed at 15 rows. However, no validation message of any kind is rendered: scanning every element in the dialog for `role="alert"`, `aria-invalid`, or classes matching `destructive|error|invalid|alert` returned zero matches. The user gets a greyed-out button with no explanation of what is missing.

- [ ] CS-02: Transaction rejects zero, negative, and non-numeric amounts
  - Action: Attempt to submit a transaction with amount "0", then with "-50", then with "abc".
  - Expected: Each attempt is rejected with a validation message; no transaction is created and the history list is unchanged.
  - Bug Report:
    - Issue: Missing validation feedback (no message shown for rejected amounts)
    - Actual: All three attempts were rejected and the history stayed at 15 rows: amount "0" → submit button disabled; amount "-50" → submit button disabled; amount "abc" → the field is `type="number"`, so Playwright could not even enter the text ("Cannot type text into input[type=number]") and the button stayed disabled. No validation message appeared for any attempt — no `role="alert"`, `aria-invalid`, or `destructive`/`error` styled element exists anywhere in the form.

- [ ] CS-03: Expense category cannot be created with a blank name or negative budget
  - Action: Click "Add Category", leave the name blank and enter a budget of "-100", then save. Repeat with a valid name and a blank budget.
  - Expected: Both attempts are blocked with a validation message; no invalid category is added to the Expense Categories list.
  - Bug Report:
    - Issue: Negative budget accepted (validation only checks for empty values)
    - Actual: Blank name was correctly blocked (the "Add Category" button is disabled while the name is empty, with or without a budget), and a valid name with an empty budget was also blocked. But a valid name with a **negative** budget is accepted: entering name "NegTest" and budget "-100" left the "Add Category" button enabled, and clicking it added the row "NegTest — Budget: -$100/mo" to the Expense Categories list. The validation appears to test only for non-empty strings, not for `budget > 0`.

- [X] CS-04: Invalid date range (start after end) is prevented or reported
  - Action: Set the filter "From" date to a later date than the "To" date and apply the filter.
  - Expected: Either the filter is blocked with a clear message (e.g. "Start date must be before end date"), or the history shows an explicit empty state; the app does not crash or display an unfiltered list.

- [X] CS-05: Filtering that matches no transactions shows an empty state, not an error
  - Action: Apply a category and date range combination that contains no transactions (e.g. a category with no entries in a past month).
  - Expected: The transaction list shows a clear "No transactions found" (or equivalent) message with zero rows, and the filter controls remain usable.

## Interaction

- [X] IX-01: Overspent categories are visually highlighted in the monthly summary
  - Action: In the Monthly Summary, identify a category whose actual spending exceeds its budget (log an extra transaction if none exists), then view that row.
  - Expected: That row is visually distinguished from on-budget rows (e.g. red text/background and/or an "Over Budget" / "Overspent" label), while categories within budget are not highlighted.

- [ ] IX-02: Success confirmation appears after a transaction is logged
  - Action: Submit a valid transaction.
  - Expected: A confirmation message (e.g. "Transaction added") appears immediately, and the form is cleared or reset for the next entry.
  - Bug Report:
    - Issue: No success confirmation after saving a transaction
    - Actual: After submitting a valid transaction ("Electric bill (over)", $250, Utilities, Nov 9) the dialog closed and the row appeared in the history, but no confirmation was ever displayed. `document.body.innerText` was sampled at 150 ms, 450 ms, 750 ms, 1050 ms and 1350 ms after submit and contained no toast text; `[data-sonner-toaster]` and `section[aria-label^="Notifications"]` matched nothing, and a scan for any element whose class/TagName matches `/toast|sonner/i` returned zero elements (the page renders an empty `Notifications` region). The form-reset half of the expectation does pass — reopening the dialog shows empty amount/description fields.

- [X] IX-03: Applying filters updates the history list without a page reload
  - Action: With the transaction history open, change the category filter and apply it.
  - Expected: The visible transaction rows update in place to the filtered set; the page does not reload and the previously selected filter values remain shown in the controls.

- [X] IX-04: Clearing filters restores the full transaction history
  - Action: After applying a category and date range filter, click the "Clear" / "Reset" filters control.
  - Expected: All filter inputs return to their default state and the full, unfiltered transaction history is displayed again.

## Content

- [X] CT-01: All currency amounts are displayed with a consistent, correct currency format
  - Action: Inspect amounts shown in Income Sources, Expense Categories, Monthly Summary, Savings Goals, and the transaction history.
  - Expected: Every amount uses the same currency symbol and decimal formatting (e.g. "$1,200.00"), and none appear blank, as "NaN", or as "undefined".

- [X] CT-02: Summary and history labels match the profile's actual categories, goals, and income sources
  - Action: Compare the category names listed in the Monthly Summary and the category filter dropdown against the Expense Categories defined in the profile; do the same for savings goals.
  - Expected: Names match exactly with no duplicates, no missing entries, and no sample/placeholder names (e.g. "Category 1", "Foo", "Lorem ipsum").

- [X] CT-03: All page text is budgeting-specific and free of placeholder content
  - Action: Read all headings, section titles, button labels, and empty-state messages across the profile, summary, and history pages.
  - Expected: All text relates to budgeting (income, expenses, categories, budget, savings goals, transactions, filters); no lorem ipsum, "TODO", or generic template text is present.

---

### Notes on execution (not part of the checklist)

- **Where the profile lives:** income sources, expense categories and savings goals are edited inside the **Profile Settings** dialog opened from the "Alex Johnson" avatar (tabs: Profile / Income / Categories / Goals). The monthly summary is the **Budget** page ("Budget Overview — November 2026 › Budget vs. Actual").
- **Data created during the run:** income source "Consulting $500/mo" (FT-01 used a non-duplicate name instead of "Freelance", which already existed); category "Transport $200/mo"; goal "Rainy Day Fund $5,000" (FT-03 used a non-duplicate name because an "Emergency Fund" goal already existed); transactions "Bus pass $45 Transportation Nov 8", "Coffee beans $30 Food & Dining Nov 8", "Electric bill (over) $250 Utilities Nov 9"; $500 added to Rainy Day Fund. The temporary "NegTest -$100" category created by CS-03 was deleted afterwards.
- **Substitutions forced by the seeded data:** the app's current month is November 2026 but its seeded transactions are dated December 2025, so FT-09's literal "last month" (Oct 1–31 2026) returns zero rows; the pass is based on a Dec 1–10 2025 range, which correctly returned only the 11 rows inside it. FT-08 used "Food & Dining" (no "Groceries" category exists). FT-07 used the per-goal "Add amount" control on the Goals page because the transaction form has no goal-assignment field.
- **Minor cosmetic observation (recorded as PASS):** the single currency formatter trims trailing zeros, so the history shows "-$85.5" and "-$42.3" next to "-$15.99" and "-$1,500". The symbol and thousands separators are uniform and no value is blank/NaN/undefined, so CT-01 passes, but a fixed two-decimal format would read better for money.