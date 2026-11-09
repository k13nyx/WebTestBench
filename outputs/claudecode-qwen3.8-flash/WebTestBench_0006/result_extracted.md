# Test Result

## Functionality
- [X] FT-01: User can record an income transaction
  - Action: Open the transactions view, click "Add Transaction", select type "Income", enter a description, amount, date, and a category, then save.
  - Expected: The new income entry appears in the transaction list with type "Income" and the entered details.

- [X] FT-02: User can record an expense transaction
  - Action: Click "Add Transaction", select type "Expense", enter description, amount, date, and category, then save.
  - Expected: The new expense entry appears in the transaction list with type "Expense".

- [ ] TEST-ID FT-03: User can create financial records of each supported type
  - Action: Using the records module, create one Invoice, one Bill, and one Payment, each with an amount and category/account assignment, and save.
  - Expected: All three records appear in the records list, each labeled with its correct type.
  - Bug Report:
    - Issue: Missing Feature — no records module
    - Actual: The app has no Records/Invoice/Bill/Payment functionality. Navigation exposes only Dashboard, Transactions, Categories, Reports, Tax Summary; the URL `/records` renders the 404 page ("Oops! Page not found"). The transaction form supports only "Income"/"Expense" types; values like "INV-001"/"PAY-DEC-01" are free-text Reference fields, not record types.

- [X] FT-04: User can edit an existing entry
  - Action: Open an existing transaction, change its amount and category, and save.
  - Expected: The entry re-displays with the updated amount and category.
  - Verified: "Edit Transaction" dialog prefilled (amount 250.75, Office Supplies); after "Update Expense" the row showed Utilities and −$300.50.

- [X] FT-05: User can delete an existing entry
  - Action: Delete a transaction from the list, confirming if prompted.
  - Expected: The entry no longer appears in the list, and dashboard/report totals recompute without it.
  - Verified: Trash icon → "Delete Transaction… Cancel/Delete" confirm → "Electric Bill" row removed; Total Expenses recomputed −$36,786.49 → −$36,501.49 (exactly −285.00); dashboard net recomputed ($934). (Note: the month selector cannot reach deleted entry's 2024 month, so report recomputation was checked via the list/dashboard aggregates.)

- [X] FT-06: User can create a custom category and assign it
  - Action: In the categories/accounts settings, add a new category (e.g., "Freelance"), then assign it to a transaction via the category dropdown.
  - Expected: The new category is listed in settings and selectable in the transaction form; the transaction saves with it.
  - Verified: "Freelance" (Income) appeared under Income Categories, was selectable in the form dropdown, and a transaction saved showing "Freelance" in its row.

- [X] FT-07: User can filter records by date range
  - Action: Apply a start and end date filter to the transactions/records list.
  - Expected: Only entries dated within the selected range are displayed.
  - Verified: 2026-11-01→2026-11-30 returned exactly the two Nov-2026 entries; 2024-12-01→2024-12-31 returned exactly the 9 Dec-2024 entries; clearing restored all 19 rows.

- [X] FT-08: User can filter records by category
  - Action: Select a category in the filter control.
  - Expected: Only entries assigned to that category are displayed.
  - Verified: Filtering by "Utilities" showed only the matching entry, and the summary recomputed (Income $0.00 / Expenses −$300.50); "All Categories" restored the full list.

- [X] FT-09: User can view a monthly profit and loss report
  - Action: Open the Reports section and select the current/default month.
  - Expected: The report displays total income, total expenses, and net profit/loss for that month.
  - Verified: Default "November 2026" showed Total Income $1,234.56, Total Expenses $300.5, Net Profit/Loss +$934.06, plus category breakdowns; month switch to "October 2026" correctly showed $0/$0/+$0.

- [X] FT-10: User can generate a tax summary
  - Action: Open the tax summary tool and generate/view the summary.
  - Expected: A tax summary page/section is displayed with tax figures available for review.
  - Verified: /tax-summary shows Total Taxable Income, Total Deductible Expenses, Net Taxable Income, per-category tables, and a full tax-transaction listing, with a year selector (2022–2026).

## Constraint
- [ ] TEST-ID CS-01: Invalid amounts are rejected
  - Action: Attempt to save a transaction with amount "0", a negative value, and non-numeric text.
  - Expected: Save is blocked and a validation error message is shown for each invalid amount.
  - Bug Report:
    - Issue: Missing amount validation
    - Actual: Amount "0" was accepted and saved — a transaction row "CS Amount Test 0 … −$0.00" appeared with no error. Amount "−50": save was silently blocked (dialog stayed open, no record created) but **no validation error message was displayed**. Non-numeric text ("abc") cannot be typed into the `input[type=number]` field at all (browser-level block), so no app validation message exists for it either.

- [ ] TEST-ID CS-02: Required fields must be provided
  - Action: Attempt to save a transaction with the description, amount, or category left empty.
  - Expected: The record is not created and the missing required fields are flagged.
  - Bug Report:
    - Issue: Missing category requirement & no field-level error flags
    - Actual: Saving with **Category empty succeeded** — a transaction was created showing "—" with no category ("Nov 8, 2026 CS2 NoCategory — $10.00"). Empty Description and empty Amount blocked the save (dialog remained open), but **no error message or visual flag** identifying the missing required field appeared in the dialog.

- [ ] TEST-ID CS-03: In-use categories are protected
  - Action: Attempt to delete a category that is assigned to at least one existing transaction.
  - Expected: Deletion is blocked or reassignment is required; no transaction is left without a category.
  - Bug Report:
    - Issue: Category deletion not guarded against usage
    - Actual: Deleting "Rent" (assigned to 2 transactions) only showed a generic "Delete Category… This action cannot be undone" confirm; it was **not blocked and no reassignment was required**. The 2 rent transactions were left with **empty category cells** (still listed with blank category; tax summary displayed them under an "Unknown $4,400.00" bucket), and re-creating a "Rent" category did not re-link them.

- [X] CS-04: Profit and loss calculation is consistent
  - Action: For a given month, sum income entries and expense entries from the transaction list, then compare against the P&L report figures.
  - Expected: Report net = (total income − total expenses) exactly matches the manually summed values.
  - Verified: November 2026 — list entries: +$1,234.56 income, $300.50 expense; manual net = $934.06; report showed $1,234.56 / $300.5 / +$934.06 — exact match. Second month October 2026: manual $0 (no entries in filtered list) vs report $0/$0/+$0 — match.

## Interaction
- [ ] TEST-ID IX-01: Save actions give immediate feedback
  - Action: Create a transaction and save it.
  - Expected: A success message/toast or confirmation is displayed, and the form/list reflects the new entry without a manual page reload.
  - Bug Report:
    - Issue: No success feedback
    - Actual: The list/form updates immediately without reload (that part is fine), but **no success message/toast is ever displayed**: a MutationObserver attached to both "Notifications" regions captured zero toast content across every save/update/delete operation (adds, "Update Expense"/"Update Income", delete confirmations, category creation).

- [X] IX-02: Tax-related flag can be toggled and persists
  - Action: Open an entry and toggle its "Tax-related" checkbox/indicator off and on, then save and reopen the entry.
  - Expected: The toggle state persists and the entry shows a visible tax indicator in the list.
  - Verified: Switch aria-checked false→true (ON) → list showed ✓ → reopen showed true → OFF → ✓ removed → ON → reopen persisted true and list shows ✓.

- [X] IX-03: Tax summary can be printed
  - Action: From the tax summary view, trigger the Print action.
  - Expected: A print dialog or print-friendly view of the tax summary opens containing the summary content.
  - Verified: "Print Report" invokes the browser print pipeline (instrumented `window.print()` call detected; no separate tab opened — it prints the current print-styled summary page containing the summary tables).

## Content
- [X] CT-01: Default data is present on first load
  - Action: Open the application's dashboard/transactions view.
  - Expected: Pre-existing sample transactions, records, and categories are displayed; the dashboard is not empty.
  - Verified: Dashboard showed KPI cards, Income-vs-Expenses chart, Expenses-by-Category, 5 Recent Transactions; transactions list had 18 seeded entries across 12 categories.

- [X] CT-02: Tax summary content is accurate
  - Action: Compare the tax summary against entries marked "Tax-related".
  - Expected: The summary lists only tax-marked entries, and its totals equal the sum of those entries.
  - Verified: 2026 — only the single tax-marked entry (+$1,234.56, tax ✓) listed; the non-tax-marked expense ($300.50) correctly excluded; Net Taxable $1,234.56 = sum. 2024 — "17 transactions" = all 17 remaining tax-marked entries; totals $47,592.50 income / $36,200.99 expenses / $11,391.51 net exactly match manual sums of tax-marked entries (verified expense total reflects the deleted entry's removal).

- [X] CT-03: Content is bookkeeping-appropriate and well-formatted
  - Action: Review dashboard, reports, and forms for labels, headings, and amounts.
  - Expected: All text is relevant to bookkeeping (no placeholder/lorem text), and monetary values display with currency formatting.
  - Verified: No "lorem ipsum"/TODO/placeholder strings found in any page text; headings/labels are bookkeeping-relevant ("Total Balance", "Monthly Income", "Deductible Expenses by Category", etc.); amounts render with currency symbols, signs, and thousands separators (e.g., "+$1,234.56", "−$36,501.49"). Minor: some views show un-padded decimals ("$300.5", "$42.5") — noted, but currency formatting is present.
