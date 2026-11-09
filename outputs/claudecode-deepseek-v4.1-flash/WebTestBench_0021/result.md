I have gathered enough evidence across all pages. Let me compile the final results.

# Test Result

## Functionality

- [X] FT-01: Staff can create a new customer record.
  - Action: Click "Add Customer", fill all required fields with valid values, click "Save".
  - Expected: New customer appears in the customer list with the entered details.

- [ ] FT-02: Staff can update an existing customer record.
  - Action: Open a customer record, edit a field (e.g., phone/notes), click "Save".
  - Expected: The updated value persists and displays on reopening the record.
  - Bug Report:
    - Issue: Update not persisted (data reverts on re-open).
    - Actual: On Victoria Ashworth's record (cust-1) the phone was changed to "+1 (555) 999-8888" and saved (toast "Customer updated / Changes have been saved successfully.", value displayed immediately). After navigating away (Settings → Reports → Customers) and reopening the record, the phone reverted to the original "+1 (555) 234-5678". The edited value does not persist on reopening.

- [X] FT-03: Staff can attach a related item (e.g., artwork) to a customer.
  - Action: On a customer record, click "Attach Item", select an existing artwork, confirm.
  - Expected: The artwork is listed under the customer's related items.

- [X] FT-04: Staff can track an ongoing workflow on a customer record.
  - Action: Open a customer, view the workflow section (e.g., exhibition invitations / purchases).
  - Expected: The workflow stages and current step for that customer are displayed.

- [X] FT-05: Staff can apply a custom status to a customer.
  - Action: On a customer record, select a status from the custom status list and apply it.
  - Expected: The customer's status updates and is shown on the record and/or list.

- [X] FT-06: Staff can filter customers by attribute.
  - Action: Apply a filter (e.g., status, location, interest) from the filter controls.
  - Expected: Only customers matching the filter criteria are listed.

- [X] FT-07: Staff can segment customers by behavior.
  - Action: Apply a behavior-based segment (e.g., "attended exhibition", "made purchase").
  - Expected: The list shows only customers meeting that behavioral segment.

- [X] FT-08: Staff can view a performance summary report.
  - Action: Open the reports/summary section.
  - Expected: A summary showing engagement and revenue patterns is displayed.

- [ ] FT-09: Staff can configure the summary report.
  - Action: Change a report setting (e.g., date range, metric, grouping) and apply it.
  - Expected: The report re-renders reflecting the selected configuration.
  - Bug Report:
    - Issue: Missing configuration control.
    - Actual: The Reports page exposes only the tabs "Revenue / Engagement / Sales Funnel" and statistic cards. DOM inspection of the page shows no date-range picker, no metric/grouping selector, and no "Apply" action — there is no way to configure the report (only tab navigation between predefined reports).

## Constraint

- [X] CS-01: Customer cannot be saved with empty required fields.
  - Action: Attempt to save a customer with one or more required fields blank.
  - Expected: Save is blocked and the missing required fields are flagged.

- [X] CS-02: Only predefined custom statuses can be applied.
  - Action: Open the status control and attempt to enter/select an undefined status.
  - Expected: Only configured statuses are selectable; an invalid status cannot be applied.

- [X] CS-03: Only existing items can be attached to a customer.
  - Action: Attempt to attach an item that does not exist in the system.
  - Expected: The attach action is rejected; no invalid item is added.

- [ ] CS-04: Report requires a valid date range.
  - Action: Configure a report with an end date earlier than the start date.
  - Expected: The report does not generate and an invalid-range message is shown.
  - Bug Report:
    - Issue: Missing feature — no date-range control to validate.
    - Actual: The Reports page contains no start/end date inputs (only tabs and stat cards). An invalid date range cannot be configured and no invalid-range validation message is ever rendered.

## Interaction

- [X] IX-01: Success feedback is shown after a customer is saved.
  - Action: Successfully create or update a customer and save.
  - Expected: A success notification/toast is displayed confirming the save.

- [X] IX-02: Filter and segment results update immediately.
  - Action: Toggle a filter or segment on/off.
  - Expected: The customer list updates to the correct subset without a manual page reload.

- [X] IX-03: Chart/report values are inspectable.
  - Action: Hover over a data point in the engagement or revenue chart.
  - Expected: A tooltip shows the exact value and label for that point.

## Content

- [X] CT-01: Default customer data matches the gallery niche.
  - Action: Review the pre-existing customer list.
  - Expected: Entries represent collectors with niche-relevant fields (interests, purchases, invitations).

- [X] CT-02: Statuses and workflow labels reflect the business-specific vocabulary.
  - Action: Inspect available statuses and workflow stage names.
  - Expected: Labels are niche-specific (e.g., "Invitation Sent", "Purchase Completed") rather than generic placeholders.

- [X] CT-03: Summary reports show niche-relevant engagement and revenue content.
  - Action: View the performance summary report.
  - Expected: Metrics reference engagement (invitations/interest activity) and revenue (artwork purchases) — no irrelevant or placeholder categories.

---

### Evidence summary (for the failed items)

| Item | What was executed | Observed result |
|------|-------------------|-----------------|
| FT-02 | Edited cust-1 phone → "+1 (555) 999-8888", clicked "Save Changes" | Toast "Customer updated" and value shown immediately; after navigating away and reopening, phone reverted to "+1 (555) 234-5678". Same for the applied status (Negotiating, reverted to VIP Collector) and the attached artwork (disappeared). |
| FT-09 | Opened Reports, enumerated all interactive elements | Only 3 tabs + nav links present; no date-range/metric/grouping setting or Apply control. |
| CS-04 | Searched Reports page for date-range inputs | No date inputs exist; an invalid range cannot be configured and no validation message appears. |

> Note: Beyond FT-02, the same non-persistence behaviour was observed for creation (the newly created "Test Collector" record vanished after navigating away and back) and for status/attachment changes, but those checklist items do not specify a persistence/reopen requirement, so they were evaluated against their stated Expected result.