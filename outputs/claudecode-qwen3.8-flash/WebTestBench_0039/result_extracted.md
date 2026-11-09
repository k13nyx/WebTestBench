# Test Result

## Functionality
- [X] FT-01: User can create a profile containing income sources
  - Action: Open the profile page, add an income source (e.g., "Salary", amount 5000) and save.
  - Expected: The income source "Salary — $5,000" is listed in the profile after saving.
  - Note: Profile Settings dialog → Income tab → added "Salary" $5,000; list now shows "Salary $5,000 / monthly".

- [X] FT-02: User can create expense categories with a monthly budget
  - Action: Add a new expense category "Groceries" with monthly budget $400 and save.
  - Expected: "Groceries" appears in the category list showing budget $400.
  - Note: Categories tab → list shows "Groceries — Budget: $400/mo".

- [X] FT-03: User can create savings goals
  - Action: Add a savings goal "Emergency Fund" with target amount $6,000 and save.
  - Expected: Goal "Emergency Fund — $6,000" is displayed in the savings goals section.
  - Note: Goals tab → "Emergency Fund $0 / $6,000" appears (duplicates the seeded $15,000 fund; app permits same-name goals).

- [X] FT-04: User can log a transaction and assign it to a category
  - Action: Log a transaction (date: current month, amount $50, description "Supermarket") assigned to category "Groceries" and submit.
  - Expected: The transaction appears in history with amount $50 and category "Groceries".
  - Note: Row "Supermarket — Nov 8 • Groceries — -$50" appears at the top of Transaction History (date defaulted to current month 2026-11-08).

- [X] FT-05: Monthly summary compares actual spending to budget per category
  - Action: Open the Monthly Summary for the current month.
  - Expected: Each expense category shows both "Spent" (actual) and "Budget" values, e.g., Groceries: $150 of $400.
  - Note: Budget page ("November 2026") shows every expense category with spent/budget, e.g., "Groceries $500 / $400", "Housing $0 / $1,500".

- [X] FT-06: Overspending categories are highlighted in the summary
  - Action: Open the Monthly Summary for a month where default data has a category whose actual spending exceeds its budget.
  - Expected: That category row/card is visually flagged (e.g., red text/badge "Over budget" or a warning icon) and other categories are not.
  - Note: Adapted — the default data contains no over-budget month (max: Housing $1,500/$1,500, exactly at budget; there is also no month selector beyond November 2026), so overspending was created via the normal logging flow (Groceries $500 vs $400). The Groceries row is then flagged with red text "Over budget by $100" (computed color rgb(220,40,40), class `text-destructive`), and all 9 other category rows show no flag. Highlight feature works as specified.

- [X] FT-07: Transaction history can be filtered by date range
  - Action: In Transaction History, set a start and end date covering only part of the default transactions and apply.
  - Expected: Only transactions dated within that range are listed; all others disappear.
  - Note: Range 2025-12-01 → 2025-12-05 listed exactly the 6 in-range items (Rent, Grocery shopping, Gas station, Electric bill, Restaurant dinner, Monthly salary); Dec 6–15 items disappeared.

- [X] FT-08: Transaction history can be filtered by category
  - Action: Select a single existing category in the category filter and apply.
  - Expected: Only transactions belonging to that category are listed.
  - Note: Filter "Food & Dining" listed exactly 3 rows (Grocery shopping, Restaurant dinner, Weekly groceries), all Food & Dining.

- [X] FT-09: Date range and category filters combine
  - Action: Apply both a date range and a category filter at the same time.
  - Expected: Result list contains only transactions matching BOTH criteria (intersection, not union).
  - Note: Food & Dining + 2025-12-01→05 returned exactly "Grocery shopping (Dec 2)" and "Restaurant dinner (Dec 5)" — Dec 10 groceries and all non-Food items correctly excluded.

## Constraint
- [ ] CS-01: Transaction cannot be saved with missing or invalid fields
  - Action: Submit the add-transaction form with no amount, and separately with a non-numeric/negative amount, and with no category selected.
  - Expected: Submission is blocked and a validation message names the offending field; no new row appears in history.
  - Bug Report:
    - Issue: Missing validation messages (blocking works, feedback is silent)
    - Actual: Submission is blocked in all cases — with amount empty (0.00), amount negative (-50), or category left at "Select a category" (and non-numeric text is impossible because the field is `input[type=number]`) the submit button becomes `disabled`, and the history row count stayed at 14 with no new row. However, no validation message ever names the offending field: dialog innerText contains no error text, inputs have no `aria-invalid`, and no toast/error appears on interaction. The "validation message names the offending field" half of the expectation is not met.

- [X] CS-02: Transactions can only be assigned to defined categories
  - Action: Open the category selector on the add-transaction form.
  - Expected: Only categories defined in the profile are selectable; there is no free-text entry that accepts an undefined category name.
  - Note: Category control is a Radix combobox (`aria-autocomplete="none"`, not typeable) backed by a hidden `<select>` whose options are exactly the defined categories (Housing…Other, Groceries). No free-text category entry exists (the only text input is Description).

- [X] CS-03: Categories within budget are never marked as overspending
  - Action: Check a category in the Monthly Summary whose actual spending is less than or equal to its budget.
  - Expected: It shows no "Over budget" flag/highlight and is shown as remaining/under budget.
  - Note: All under/equal-budget rows (Housing $0/$1,500, Food & Dining $0/$600, Pet Care $0/$100, etc.) contain no "Over budget" text or destructive styling; page shows Remaining $3,600 with bars under 100%. Only the exceeding category (Groceries $500/$400) was flagged.

- [X] CS-04: Invalid date range is rejected or handled
  - Action: Set the filter start date later than the end date and apply.
  - Expected: Either a message states the range is invalid, or the filter shows no transactions — the page must not crash or silently show all transactions.
  - Note: From 2025-12-10 → To 2025-12-05 renders "No transactions match your filters" (0 rows), page stable, no crash, no silent fallback to the full list.

## Interaction
- [ ] IX-01: Saving a transaction produces confirmation and updates lists
  - Action: Log a valid transaction and observe the interface after submit.
  - Expected: A success confirmation (toast/message) is shown, the form clears, and the new transaction appears in the history list without re-creating data.
  - Bug Report:
    - Issue: Missing success confirmation
    - Actual: History updated live (row "Supermarket — Nov 8 • Groceries -$50" appeared without reload) and the form reset (reopening the dialog shows empty amount/description and "Select a category"), but no success toast or message is ever shown: the Notifications region stayed empty and a 2-second post-submit poll (20 samples) captured zero toast/list items.

- [X] IX-02: New profile category becomes available immediately
  - Action: Create a new expense category in the profile, then open the add-transaction form and the Monthly Summary.
  - Expected: The new category appears as an option in the transaction form and as a row with $0 spent in the summary.
  - Note: "Groceries", immediately after creation, appeared as a selectable option in the Add Transaction category list; a second new category "Pet Care" (created while November had no Pet Care transactions) appeared in the Budget page as a row "Pet Care $0 / $100".

- [X] IX-03: Applying or clearing filters updates the list in place
  - Action: Apply a category filter, then reset/clear it.
  - Expected: The history list re-renders to the filtered set and then back to the full default set; a "no results" state is shown if a filter matches nothing.
  - Note: Applying Food & Dining re-rendered the list to 3 rows in place; "Clear filters" (appears automatically next to the heading) restored the full 14-row set; an unmatched filter combination displayed "No transactions match your filters".

## Content
- [X] CT-01: Summary figures are consistent with logged transactions
  - Action: Compare the "Spent" amount for each category in the Monthly Summary against the sum of that category's transactions for the same month in history.
  - Expected: The two values match exactly for every category (no unaccounted or double-counted transactions).
  - Note: November 2026: Groceries Spent $500 = history sum (450 + 50); all other categories $0 = no November transactions; Total Spent $500; Remaining $3,600 = Total Budget $4,100 − $500. December-2025 transactions correctly excluded from the November summary.

- [X] CT-02: Transaction rows display complete, correct data
  - Action: Inspect the columns of the default transactions in history.
  - Expected: Every row shows date, amount, description, and category, with no blank/placeholder values such as "null", "TBD", or "Lorem ipsum".
  - Note: All 14 default rows (plus logged ones) show description, date (e.g., "Dec 1"), category tag, and signed amount; automated scan found zero rows missing any field and zero occurrences of null/undefined/TBD/Lorem.

- [X] CT-03: Savings goals show progress toward the target
  - Action: Open the savings goals section.
  - Expected: Each goal shows its name, target amount, and a progress indicator or remaining amount that is relevant to budgeting (not generic filler text).
  - Note: Goals page shows for each of 4 goals: name, Current, Target, "Progress X%" with a progressbar, and remaining (e.g., "Emergency Fund … Progress 57% … $6,500 remaining"; new goal "Emergency Fund … Progress 0% … $6,000 remaining"), plus totals (Total Saved $14,700 / Target $49,000) and deadlines. No filler text.
