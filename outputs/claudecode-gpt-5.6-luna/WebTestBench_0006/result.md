# Test Result

## Functionality

- [X] FT-01: View income and expense records
  - Action: Open the transactions or bookkeeping records area and review the pre-existing records.
  - Expected: Existing income and expense entries are listed with identifiable dates, descriptions, amounts, and transaction types.

- [X] FT-02: Create a financial record
  - Action: Open the control for adding a new income, expense, invoice, bill, or payment record and enter valid required details.
  - Expected: The record form accepts the details and provides a clear save or submit action for creating the record.

- [ ] FT-03: Manage invoices, bills, and payments
  - Action: Open the records area and select an existing invoice, bill, and payment from the default data.
  - Expected: Each record displays its record type, amount, date, status, and relevant account or category information.
  - Bug Report:
    - Issue: Missing record metadata
    - Actual: The transactions table includes references such as `INV-001`, `PAY-DEC-01`, and bill-like descriptions such as `Electric Bill`, but does not display an explicit record type or status for these records. The available edit form also has no status field.

- [X] FT-04: Assign transactions to categories or accounts
  - Action: Open an existing transaction and select an available category or account.
  - Expected: The selected category or account is displayed on the transaction after the change is saved.

- [X] FT-05: Manage customizable categories or accounts
  - Action: Open category or account management and use the available control to add or edit a category/account.
  - Expected: The interface provides fields for the name and relevant details and allows the category/account to be saved for later assignment.

- [X] FT-06: Review and adjust an existing entry
  - Action: Open a default transaction, change an editable value such as description, amount, date, or category, and save it.
  - Expected: The updated value is displayed when the entry is reopened or viewed in the record list.

- [X] FT-07: Filter records by date
  - Action: Apply a start date and end date in the records filter.
  - Expected: Only records whose dates fall within the selected date range are displayed.

- [X] FT-08: Filter records by category
  - Action: Select a category or account in the records filter.
  - Expected: Only records assigned to the selected category or account are displayed.

- [ ] FT-09: View monthly profit and loss
  - Action: Open reports, select a month, and view the profit-and-loss report.
  - Expected: The report separately summarizes income and expenses and displays the resulting profit or loss for the selected month.
  - Bug Report:
    - Issue: Report month selector does not include transaction months
    - Actual: The month selector only provided November 2026 through December 2025. The available records are dated October–December 2024, so a month containing existing records could not be selected. The displayed report showed `$0` income, `$0` expenses, and `+$0` net profit/loss.

- [X] FT-10: View financial dashboard
  - Action: Open the dashboard.
  - Expected: The dashboard shows a current financial overview using the available records, including income, expenses, and an overall balance or profit/loss indicator.

- [X] FT-11: Mark a record as tax-related
  - Action: Open an existing eligible income or expense record and enable its tax-related option.
  - Expected: The record is visibly marked as tax-related after the change is saved.

- [X] FT-12: Generate a tax summary
  - Action: Open the tax summary tool and select the applicable reporting period.
  - Expected: A tax summary is generated using records marked as tax-related and presents a reviewable total or breakdown.

- [ ] FT-13: Print the tax summary
  - Action: From the generated tax summary, select the print control.
  - Expected: A print preview or system print dialog opens with the tax summary content available for printing.
  - Bug Report:
    - Issue: Print control does not expose a print preview or dialog
    - Actual: After selecting `Print Report`, the application remained on the tax summary page at the same URL. No print preview, new tab, or system print dialog was observed.

## Constraint

- [ ] CS-01: Prevent incomplete financial records
  - Action: Open a record form, leave a required field such as amount, date, or record type empty, and attempt to save.
  - Expected: The record is not saved and a clear validation message identifies the missing required field.
  - Bug Report:
    - Issue: Missing required-field validation message
    - Actual: Submitting the blank transaction form did not create a record, but no visible validation message identified the missing description, amount, category, or other required field.

- [ ] CS-02: Validate invalid financial values
  - Action: Enter an invalid amount, date, or other format-required value in a record form and attempt to save.
  - Expected: The invalid value is rejected, an explanatory validation message is shown, and no invalid record is created.
  - Bug Report:
    - Issue: Invalid-value validation feedback is missing
    - Actual: The numeric amount field prevented the text value `abc` from being entered because it is an HTML number input, but the interface displayed no explanatory validation message. No user-facing validation feedback was provided.

- [ ] CS-03: Preserve report consistency after edits
  - Action: Change an existing transaction’s amount, type, date, or category and reopen the affected monthly report or dashboard.
  - Expected: The report and dashboard totals reflect the saved entry values without retaining the outdated values.
  - Bug Report:
    - Issue: Affected monthly report cannot be selected for verification
    - Actual: After changing a transaction category, the reports page did not provide the transaction’s December 2024 month. The selector only exposed December 2025 and newer months, preventing verification of the affected monthly report totals.

- [X] CS-04: Exclude unmarked records from the tax summary
  - Action: Compare the tax summary with the available records and identify records that are not marked tax-related.
  - Expected: Unmarked records are not included in the tax-related totals or breakdown.

## Interaction

- [ ] IX-01: Confirm successful record changes
  - Action: Save an edited transaction or category/account.
  - Expected: The interface provides a visible success confirmation and displays the saved values without requiring a page reload.
  - Bug Report:
    - Issue: Missing success confirmation
    - Actual: Edited values appeared immediately in the transaction list without a reload, but no visible success toast, confirmation message, or notification was displayed.

- [X] IX-02: Update results when filters change
  - Action: Apply a date or category filter, then change or clear the filter.
  - Expected: The record list refreshes to match the current filter selection, and clearing filters restores the unfiltered default records.

- [X] IX-03: Handle empty filter results
  - Action: Apply a date and category combination that matches no default records.
  - Expected: The interface clearly indicates that no records match the selected filters and does not display unrelated records.

## Content

- [X] CT-01: Verify financial record content integrity
  - Action: Compare a selected record’s list view, detail view, and any related report entry.
  - Expected: Description, record type, date, category/account, amount, and tax-related status are consistent in every view.

- [ ] CT-02: Verify tax summary content
  - Action: Review the generated tax summary and its print preview.
  - Expected: The summary contains the selected reporting period, tax-related income/expense information, totals, and readable labels that match the on-screen data.
  - Bug Report:
    - Issue: Print preview unavailable for content comparison
    - Actual: The on-screen 2024 tax summary contained the selected year, taxable income and deductible expense breakdowns, totals, and readable labels. However, selecting `Print Report` did not open a print preview or system print dialog, so the printed version could not be reviewed.