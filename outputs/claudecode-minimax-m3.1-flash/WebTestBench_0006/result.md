All checklist items have been exercised. Here is the complete result.

# Test Result

## Functionality

- [ ] FT-01: User can create an income transaction with date, amount, description, category, and account
  - Action: Open the app, navigate to Transactions, click "Add Transaction", choose type Income, enter date/amount/description, select category and account, save.
  - Expected: A success confirmation appears and the new income record appears in the transaction list with the entered amount, date, and description.
  - Bug Report:
    - Issue: Missing feature (account field) + Missing success confirmation
    - Actual: The Add Transaction form contains only Type (Income/Expense), Date, Description, Amount, Category, Reference, Notes and Tax Related — there is no account dropdown, so "select account" is impossible. The record itself was created correctly (row "Nov 7, 2026 | QA Income | Sales Revenue | +$1,111.11"), but no success message/toast appeared: a 1.2 s polling probe after save found 0 `[data-sonner-toast]`/`[role=status]`/`[role=alert]` elements and no "success/saved/created" text anywhere on the page.

- [X] FT-02: User can create an expense transaction and it is recorded against the selected category/account
  - Action: Click "Add Transaction", choose type Expense, enter valid date, amount, description, category, account, save.
  - Expected: The record appears in the list labeled as an expense and is counted as an outflow in totals.
  - Note: The record appears as an outflow (row "Nov 7, 2026 | QA Expense | Office Supplies | -$222.22") and the footer totals changed from -$36,485.99 to -$36,708.21. There is no account selector in the form (feature gap, see FT-05).

- [ ] FT-03: User can create an invoice, bill, and payment record of their own type
  - Action: Open the records section and create one record each of type Invoice, Bill, and Payment with valid amount, date, and counterparty name.
  - Expected: All three records are saved and listed with their respective types, amounts, and dates.
  - Bug Report:
    - Issue: Missing feature (record types)
    - Actual: The Type dropdown in Add Transaction offers only "Income" and "Expense" (verified by reading the option list of the underlying select). There is no records/invoices/bills/payments section — /records, /invoices, /bills, /payments all render the app's "404 – Oops! Page not found". Invoice/Bill/Payment records can only be approximated with a free-text Reference field, and no Type column exists in the list.

- [ ] FT-04: User can assign a record to a category and an account, and the assignment is retained
  - Action: Create a record and pick a category and account from the dropdowns; then reopen/edit that record.
  - Expected: The saved record shows the selected category and account, and the reopened form displays them as the current selections.
  - Bug Report:
    - Issue: Assignment not retained on reopen + Missing feature (account)
    - Actual: (1) No account field/dropdown exists anywhere in the app (no Accounts route, /accounts → 404). (2) Reopening the Edit Transaction dialog shows the category trigger as "Select category" instead of the record's stored category — reproduced on seeded data: editing "Consulting Fee - Strategy Session" (category Consulting) prefilled amount 1800, date 2024-12-08, reference INV-002 and Tax=true, but the category trigger read "Select category". (3) Saving the form without re-picking the category silently WIPES the category: after re-saving "QA Income EDITED", the row became "Nov 8, 2026 | QA Income EDITED | (blank) | — | +$1,500.00 | ✓" and Reports/Tax Summary then showed the category as "Unknown".

- [ ] FT-05: User can create a new custom category and a new account
  - Action: Open Categories and Accounts management, add a category named "Consulting" and an account named "Business Checking", then save.
  - Expected: Both new items appear in their lists and are selectable when creating a transaction.
  - Bug Report:
    - Issue: Missing feature (accounts) + Duplicate name allowed
    - Actual: Only a Categories page exists (nav: Dashboard, Transactions, Categories, Reports, Tax Summary); there is no Accounts page (/accounts → "404 Oops! Page not found"), so "Business Checking" cannot be created. The category half works — "QA Consulting" was created, appears in the Income/Expense category lists and is selectable in the Add Transaction category dropdown (options: Office Supplies, Utilities, Salaries, Marketing, Travel, Software, Insurance, QA Consulting). However adding "Consulting", which already existed, created a SECOND category with the same name instead of being rejected.

- [X] FT-06: User can edit an existing transaction's amount, date, category, and description
  - Action: Open a saved transaction, change its amount and category, save, and view the list and dashboard.
  - Expected: The list shows the updated values and the dashboard totals reflect the edited amount, not the original.
  - Note: Row changed from "QA Income / +$1,111.11 / Sales Revenue / Nov 7" to "Nov 8, 2026 | QA Income EDITED | Consulting | +$1,500.00", list Total Income moved to +$49,592.50 and the Dashboard "Monthly Income" card changed from $0 to $1,500 (original amount no longer used).

- [X] FT-07: User can delete a transaction record
  - Action: Select a saved transaction and use the delete action, confirming the prompt.
  - Expected: The record disappears from the list and its amount is no longer included in dashboard totals.
  - Note: Confirm dialog "Delete Transaction — Are you sure you want to delete this transaction? This action cannot be undone." appeared and was confirmed; row count 21 → 20, the row disappeared, and Dashboard "Monthly Expenses" fell from $272 to $222.

- [X] FT-08: Monthly profit and loss report shows income, expenses, and net profit for a selected month
  - Action: Open Reports, select a month from the period selector, and view the Profit & Loss section.
  - Expected: Income, Expenses, and Net Profit amounts are displayed and match the totals of the transactions in that month.
  - Note: Reports → period "November 2026" showed Total Income $1,500, Total Expenses $272.22, Net Profit/Loss +$1,227.78, exactly matching that month's transactions ($1,500.00 income; $222.22 + $50.00 expenses). The selector only offers Nov 2026 → Dec 2025, so the seeded data month (Dec 2024) cannot be selected; the section is labelled "Reports" with "Total Income / Total Expenses / Net Profit/Loss" cards rather than a "Profit & Loss" heading.

- [X] FT-09: User can filter records by date range
  - Action: On the transactions/records view, set a from-date and to-date filter and apply.
  - Expected: Only records dated within the range are listed, and records outside the range are excluded.
  - Note: From 2024-12-01 / To 2024-12-31 listed exactly the 10 December 2024 rows (Dec 15 … Dec 1); all Nov/Oct 2024 rows were excluded. Filtering is applied on change; a "Clear Filters" control appears while filters are active.

- [X] FT-10: User can filter records by category
  - Action: Select a category in the category filter and apply it.
  - Expected: Only records assigned to that category are listed, and the filter value is shown as active.
  - Note: Category filter "Consulting" reduced the list from 18 to 3 rows (Consulting Fee - Strategy Session, Client Project - Website Redesign, Client Retainer Fee) and the filter select displayed "Consulting" instead of "All Categories".

- [X] FT-11: Dashboard shows a summary of financial status (income, expenses, balance/profit totals)
  - Action: Open the Dashboard on the default data set.
  - Expected: Summary cards/totals for income, expenses, and net balance are visible and consistent with the record list totals.
  - Note: Cards "Total Balance $74,931", "Monthly Income $1,500", "Monthly Expenses $272", "Net Profit/Loss $1,228" plus Income-vs-Expenses chart, Expenses by Category and Recent Transactions. The monthly figures matched the November 2026 list totals exactly; the "Total Balance" card is a static value that never changed after adding, editing or deleting records (no accounts exist to derive it from).

- [X] FT-12: User can mark a record as tax-related and the flag is displayed and persisted
  - Action: Edit a record and enable the tax-related flag, save, then re-open the record.
  - Expected: The tax-related flag is shown as enabled in the list and remains enabled after re-opening.
  - Note: After enabling the "Tax Related" switch and saving, the row's Tax column showed "✓"; re-opening the edit dialog reported the switch `aria-checked="true"`, and toggling it off removed the ✓ from the list.

- [X] FT-13: Tax summary lists only tax-related records with income/expense totals
  - Action: Open the Tax Summary section and compare its listed records and totals against the records flagged as tax-related.
  - Expected: Only tax-related records are included, and the summary income and expense totals equal the sum of those records.
  - Note: Tax Summary (year 2026) showed "1 transactions", Total Taxable Income $1,500.00, Total Deductible Expenses $0.00, Net Taxable Income $1,500.00 with the single line item "Nov 8, 2026 | QA Income EDITED | — | +$1,500.00". Year 2024 showed the 18 seeded tax-flagged records with $47,592.50 income / $36,485.99 expenses / $11,106.51 net, equal to the sum of the listed items.

## Constraint

- [ ] CS-01: Cannot save a transaction with a missing required field
  - Action: Open "Add Transaction", leave amount or date blank (and separately try an empty description if required), and click Save.
  - Expected: The transaction is not created and an inline validation error identifies the missing field; no new row appears in the list.
  - Bug Report:
    - Issue: Missing validation feedback (silent rejection)
    - Actual: The row count stayed unchanged (20 before and after), so nothing was created, but NO inline validation message appeared. The dialog text after the failed save contained no error text and the only extra element found was the helper "Include in tax summary reports". Same silent behaviour with amount filled but date/description empty.

- [ ] CS-02: Cannot save a transaction with a non-positive or non-numeric amount
  - Action: Enter an amount of 0, then a negative amount, then a non-numeric value, and attempt to save each time.
  - Expected: Each attempt is rejected with a validation message and no record is created.
  - Bug Report:
    - Issue: Validation bypass (zero amount accepted) + Missing validation message
    - Actual: Amount 0 WAS accepted and saved — a new row appeared: "Nov 7, 2026 | CS02 zero | Office Supplies | — | -$0.00". A negative amount (-50) was rejected but silently (no message shown, dialog stayed open). A non-numeric value cannot even be typed because the field is `input[type=number]` (Playwright refused: "Cannot type text into input[type=number]").

- [ ] CS-03: A transaction cannot be saved without a date
  - Action: Open "Add Transaction", fill in all fields except the date, and click Save.
  - Expected: Saving is blocked and the date field is flagged as required.
  - Bug Report:
    - Issue: Missing required-field indicator
    - Actual: Saving was blocked (no new row; row count unchanged) but the date field was NOT flagged: no required attribute, asterisk, red border or message appeared, and the dialog's inner text contained no error text.

- [ ] CS-04: Duplicate record numbers are rejected for invoices and bills
  - Action: Create an invoice with a specific number, then create another record with the same number and type, and save.
  - Expected: The second save is rejected with a duplicate/uniqueness message and only one record with that number exists.
  - Bug Report:
    - Issue: Missing uniqueness validation + Missing feature (invoice/bill types)
    - Actual: Creating an expense with reference "INV-001" — already used by the seeded "Client Project - Website Redesign" (INV-001) — succeeded; the list afterwards contained both "Dec 1, 2024 | Client Project - Website Redesign | Consulting | INV-001" and "Nov 7, 2026 | QA Dup Ref | Office Supplies | INV-001 | -$50.00". No duplicate message was shown. Invoice and Bill types do not exist to be tested.

- [ ] CS-05: A record amount cannot exceed the account balance for a payment/bill drawn on that account
  - Action: Attempt to record a payment from an account with a balance smaller than the payment amount.
  - Expected: The entry is rejected with a message about insufficient balance and no negative/overdrawn record is created.
  - Bug Report:
    - Issue: Missing feature (accounts, balances, payment/bill records)
    - Actual: The app has no Accounts entity (no Accounts nav item, no Accounts route, /accounts → 404), no account selector in the transaction form and no Payment/Bill record types, so no account balance exists to draw against and the scenario cannot be performed. The only balance-like figure in the app is the static Dashboard card "Total Balance $74,931", which is not linked to any record.

- [ ] CS-06: Category and account names must be unique and non-empty
  - Action: Try to save a category and an account with a blank name, then with a name that already exists.
  - Expected: All attempts are rejected with a validation message and no duplicate or unnamed item is created.
  - Bug Report:
    - Issue: Duplicate names allowed + Missing validation message + Missing feature (accounts)
    - Actual: (1) A blank name was blocked but silently — the dialog stayed open with no error text and no category was added. (2) Saving the name "Consulting" (already existing) SUCCEEDED — the dialog closed and the categories list then contained "Consulting" twice (headings: Sales Revenue, Consulting, Interest Income, Other Income, Office Supplies, Rent, Utilities, Salaries, Marketing, Travel, Software, Insurance, Consulting) with no duplicate/uniqueness message. (3) No account creation exists at all, so the account half of the test is not applicable.

- [ ] CS-07: A category or account in use cannot be deleted
  - Action: Attempt to delete a category that is assigned to at least one existing transaction.
  - Expected: Deletion is blocked with a message explaining it is in use, and the category and its transactions remain intact.
  - Bug Report:
    - Issue: Deletion of in-use entity not blocked
    - Actual: Deleting "Rent" (assigned to 2 transactions) was allowed. A confirm alertdialog appeared — "Delete Category / Are you sure you want to delete this category? Transactions using this category will not be deleted. / Cancel / Delete" — and after confirming, "Rent" disappeared from the category list while its two transactions remained with a BLANK category: "Dec 2, 2024 | Monthly Office Rent | (blank) | RENT-DEC | -$2,200.00" and "Nov 2, 2024 | Monthly Office Rent | (blank) | RENT-NOV | -$2,200.00". No "in use" message was shown.

- [X] CS-08: Non-tax-related records are excluded from the tax summary
  - Action: Verify a known non-tax-related transaction (tax flag off) is absent from the tax summary while tax-flagged records are present.
  - Expected: The unflagged transaction does not appear in the tax summary and does not affect its totals.
  - Note: In a session containing "QA Income" (+$1,111.11) and "QA Expense" (-$222.22) with tax off and "QA Income EDITED" (+$1,500.00) with tax on, the 2026 Tax Summary listed only 1 transaction with Total Taxable Income $1,500.00 and Total Deductible Expenses $0.00 — the unflagged $222.22 expense was absent and did not affect the totals.

- [X] CS-09: Totals cannot be manipulated by the tax flag
  - Action: Compare the dashboard/Profit & Loss totals with and without toggling the tax flag on one record.
  - Expected: Toggling the tax flag changes only tax-summary inclusion; profit and loss totals remain unchanged.
  - Note: Dashboard before toggling (tax off): Monthly Income $1,500 / Monthly Expenses $272 / Net Profit/Loss $1,228; after toggling tax on: identical values $1,500 / $272 / $1,228. Only the Tax column ✓ and the tax-summary inclusion changed.

## Interaction

- [ ] IX-01: Navigation between main sections works from a persistent navigation area
  - Action: Click each navigation item (Dashboard, Transactions/Records, Reports, Categories, Accounts, Tax Summary).
  - Expected: Each click loads the corresponding page/view with its expected heading and content, and the active item is indicated.
  - Bug Report:
    - Issue: Missing navigation item (Accounts)
    - Actual: The persistent sidebar renders only Dashboard, Transactions, Categories, Reports and Tax Summary. There is NO "Accounts" nav item (query for it returned 0 matches) and /accounts renders "404 – Oops! Page not found". The five existing items all work correctly: each click loads the matching view with heading Dashboard / Transactions / Categories / Reports / Tax Summary, and the active link is highlighted (aria-current + active styling) while the others are not.

- [ ] IX-02: Save actions give immediate visible feedback
  - Action: Save a transaction, a category, and a new account.
  - Expected: Each save shows a success message/toast and the newly created item appears in its list without a manual page reload.
  - Bug Report:
    - Issue: No success feedback (toast) shown
    - Actual: No toast/message appears for any save. A 1.2 s probe right after saving a transaction (10 samples at 120 ms) found 0 `[data-sonner-toast]`, 0 `[role=status]`, 0 `[role=alert]` elements and no "success/saved/created" text; the sonner "Notifications (F8)" region stayed empty. Saving a category ("QA Consulting") produced the same empty notification region. The newly created items do appear in their lists without a reload, but there is no success confirmation.

- [ ] IX-03: Validation errors are displayed inline next to the offending field and clear after correction
  - Action: Submit an empty required field, then enter a valid value and save again.
  - Expected: The error message appears beside the field, disappears once corrected, and the record saves successfully.
  - Bug Report:
    - Issue: Missing inline validation errors
    - Actual: Submitting the Add Transaction form with an empty amount/date produced no error message next to any field — the dialog's inner text after the failed save was "Add Transaction | Type | Expense | Income | Expense | Date | Description | Amount | Category | Office Supplies | … | Tax Related | Include in tax summary reports | Cancel | Add Expense | Close" with no validation text and no red/bordered field (only the unrelated helper text "Include in tax summary reports" was found). There is therefore no error to clear after correction.

- [X] IX-04: Opening and closing the add/edit form works via clear open and cancel actions
  - Action: Click "Add Transaction" to open the form, then click Cancel; repeat and close the form with the X control.
  - Expected: The form opens as a visible dialog/panel with a title, and both Cancel and X close it without creating a record.
  - Note: The form opened as a `role="dialog"` with heading "Add Transaction"; the Cancel button closed it (dialog count 0) and the X/Close control closed it as well, with the table row count unchanged at 18 in both cases.

- [X] IX-05: Filters can be applied, cleared, and reflected in the visible result count
  - Action: Apply a category filter, then clear filters via the reset/clear control.
  - Expected: The result list updates to the filtered set, the filter chips/selects show the applied values, and clearing restores the full list.
  - Note: Category filter "Consulting" updated the list to 3 rows and the select displayed "Consulting"; the "Clear Filters" button (which appears while filters are active) restored the full 18 rows and reset the category select to "All Categories" and the date inputs to empty. Note: no numeric result count is displayed anywhere — only the list itself changes.

- [X] IX-06: Tax summary offers a print action that opens a printable view
  - Action: Open the Tax Summary and trigger the print/print-report control.
  - Expected: A print-optimized view or print dialog appears showing the tax summary totals and the tax-related line items.
  - Note: The "Print Report" button is present on the Tax Summary page and invokes the browser print path (window.print was called exactly once when the button was clicked); the page also ships @media print rules, and the printed view contains the totals and the tax-related line items.

- [X] IX-07: A "no results" state is shown when filters exclude all records
  - Action: Apply a filter combination that matches no records (e.g., a date range with no transactions).
  - Expected: An empty-state message such as "No records found" is shown instead of a blank table or an error.
  - Note: With From 2025-01-01 / To 2025-01-31 the page showed "No transactions found" with the sub-text "Try adjusting your filters" instead of an empty table.

## Content

- [X] CT-01: Default data is present and visible on first load
  - Action: Open the app for the first time and view the transaction list, categories, and accounts.
  - Expected: Pre-seeded records, categories, and accounts are listed (not an empty application), each with a sensible label and amount.
  - Note: The app is pre-seeded: 18 transactions (Oct 5 2024 – Dec 15 2024, e.g. "Monthly Office Rent -$2,200.00", "Team Salaries - December -$12,500.00", "Client Project - Website Redesign +$5,500.00") and 12 categories (Sales Revenue, Consulting, Interest Income, Other Income, Office Supplies, Rent, Utilities, Salaries, Marketing, Travel, Software, Insurance) with sensible labels and amounts. No accounts are listed because the app has no accounts feature at all (see FT-05).

- [ ] CT-02: Transaction list displays the required identifying fields for each record
  - Action: Inspect the columns/cells of any listed transaction.
  - Expected: Date, description/name, type (income/expense/invoice/bill/payment), category, account, and amount are all shown and populated with meaningful values.
  - Bug Report:
    - Issue: Missing columns (type and account)
    - Actual: The table header is "Date | Description | Category | Reference | Amount | Tax | Actions" — there is no Type column (income/expense/invoice/bill/payment is conveyed only by the +/- sign and an arrow icon) and no Account column (and no account data exists). Category can also be empty: after editing a record without re-selecting the category, the row read "Nov 8, 2026 | QA Income EDITED | (blank) | — | +$1,500.00 | ✓".

- [X] CT-03: Dashboard and report labels use finance-appropriate terminology
  - Action: Review the wording of dashboard cards, the Profit & Loss report, and the Tax Summary headings.
  - Expected: Labels such as "Income", "Expenses", "Net Profit", and "Tax Summary" are used and read correctly; no placeholder text (e.g., "Lorem", "Test 1"), untranslated keys, or broken text appears.
  - Note: Dashboard "Total Balance / Monthly Income / Monthly Expenses / Net Profit/Loss", Reports "Total Income / Total Expenses / Net Profit/Loss / Income by Category / Expenses by Category", Tax Summary "Total Taxable Income / Total Deductible Expenses / Net Taxable Income". A scan of the rendered text of all five pages for lorem/ipsum/undefined/NaN/[object/TODO/Test 1 found zero matches.

- [ ] CT-04: Currency values are formatted consistently and correctly
  - Action: Review amounts across the dashboard, list, and reports.
  - Expected: All monetary values display with the same currency symbol and thousand/decimal separators (e.g., $1,250.00), with no raw or unformatted numbers.
  - Bug Report:
    - Issue: Inconsistent currency/decimal formatting
    - Actual: The same values are formatted differently across views. Transaction list: "+$1,234.56" / "+$1,500.00" (2 decimals); Dashboard: "Monthly Income $1,500", "Monthly Expenses $272", "Total Balance $74,931" (no decimals); Reports: "Total Income $1,500" but "Total Expenses $272.22" and "Net Profit/Loss +$1,227.78"; Categories page: "Total $42.5" for Interest Income (vs "$42.50" in the transaction list) and "$1,046" / "$54.99" for other categories.

- [X] CT-05: Tax summary content reflects only tax-relevant records with matching totals
  - Action: Open the Tax Summary and verify each listed line item and the printed summary totals.
  - Expected: Line items are the tax-flagged records with their dates, descriptions, and amounts, and the stated totals equal the sum of those line items.
  - Note: Tax Summary 2024 listed all 18 tax-flagged records with dates, descriptions and amounts (e.g. "Dec 15, 2024 | Software Subscription - Adobe CC | Software | — | -$54.99") and the stated totals equal their sums: $47,592.50 income + $36,485.99 expenses, Net $11,106.51. In the 2026 view the single line item ("Nov 8, 2026 | QA Income EDITED | +$1,500.00") matched Total Taxable Income $1,500.00 / Net $1,500.00, although its Category cell was blank (it was listed as "Unknown" in the category breakdown).

- [X] CT-06: Tax-related indicator is clearly communicated on records
  - Action: Locate a tax-flagged record in the transaction list.
  - Expected: A visible "Tax" badge, tag, or label marks the record so its tax status is unambiguous.
  - Note: Tax-flagged rows show a filled circular badge containing "✓" in the "Tax" column (e.g. "Dec 15, 2024 | Software Subscription - Adobe CC | Software | — | -$54.99 | ✓"), while unflagged rows show an empty cell, so tax status is unambiguous in the list (the badge itself is a check glyph without a text label).