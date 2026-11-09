# Test Checklist

## Functionality
- [ ] FT-01: Staff can create a new customer record.
  - Action: Click "Add Customer", fill all required fields with valid values, click "Save".
  - Expected: New customer appears in the customer list with the entered details.

- [ ] FT-02: Staff can update an existing customer record.
  - Action: Open a customer record, edit a field (e.g., phone/notes), click "Save".
  - Expected: The updated value persists and displays on reopening the record.

- [ ] FT-03: Staff can attach a related item (e.g., artwork) to a customer.
  - Action: On a customer record, click "Attach Item", select an existing artwork, confirm.
  - Expected: The artwork is listed under the customer's related items.

- [ ] FT-04: Staff can track an ongoing workflow on a customer record.
  - Action: Open a customer, view the workflow section (e.g., exhibition invitations / purchases).
  - Expected: The workflow stages and current step for that customer are displayed.

- [ ] FT-05: Staff can apply a custom status to a customer.
  - Action: On a customer record, select a status from the custom status list and apply it.
  - Expected: The customer's status updates and is shown on the record and/or list.

- [ ] FT-06: Staff can filter customers by attribute.
  - Action: Apply a filter (e.g., status, location, interest) from the filter controls.
  - Expected: Only customers matching the filter criteria are listed.

- [ ] FT-07: Staff can segment customers by behavior.
  - Action: Apply a behavior-based segment (e.g., "attended exhibition", "made purchase").
  - Expected: The list shows only customers meeting that behavioral segment.

- [ ] FT-08: Staff can view a performance summary report.
  - Action: Open the reports/summary section.
  - Expected: A summary showing engagement and revenue patterns is displayed.

- [ ] FT-09: Staff can configure the summary report.
  - Action: Change a report setting (e.g., date range, metric, grouping) and apply it.
  - Expected: The report re-renders reflecting the selected configuration.

## Constraint
- [ ] CS-01: Customer cannot be saved with empty required fields.
  - Action: Attempt to save a customer with one or more required fields blank.
  - Expected: Save is blocked and the missing required fields are flagged.

- [ ] CS-02: Only predefined custom statuses can be applied.
  - Action: Open the status control and attempt to enter/select an undefined status.
  - Expected: Only configured statuses are selectable; an invalid status cannot be applied.

- [ ] CS-03: Only existing items can be attached to a customer.
  - Action: Attempt to attach an item that does not exist in the system.
  - Expected: The attach action is rejected; no invalid item is added.

- [ ] CS-04: Report requires a valid date range.
  - Action: Configure a report with an end date earlier than the start date.
  - Expected: The report does not generate and an invalid-range message is shown.

## Interaction
- [ ] IX-01: Success feedback is shown after a customer is saved.
  - Action: Successfully create or update a customer and save.
  - Expected: A success notification/toast is displayed confirming the save.

- [ ] IX-02: Filter and segment results update immediately.
  - Action: Toggle a filter or segment on/off.
  - Expected: The customer list updates to the correct subset without a manual page reload.

- [ ] IX-03: Chart/report values are inspectable.
  - Action: Hover over a data point in the engagement or revenue chart.
  - Expected: A tooltip shows the exact value and label for that point.

## Content
- [ ] CT-01: Default customer data matches the gallery niche.
  - Action: Review the pre-existing customer list.
  - Expected: Entries represent collectors with niche-relevant fields (interests, purchases, invitations).

- [ ] CT-02: Statuses and workflow labels reflect the business-specific vocabulary.
  - Action: Inspect available statuses and workflow stage names.
  - Expected: Labels are niche-specific (e.g., "Invitation Sent", "Purchase Completed") rather than generic placeholders.

- [ ] CT-03: Summary reports show niche-relevant engagement and revenue content.
  - Action: View the performance summary report.
  - Expected: Metrics reference engagement (invitations/interest activity) and revenue (artwork purchases) — no irrelevant or placeholder categories.