# Test Checklist

## Functionality
- [ ] FT-01: Create a new customer record
  - Action: Open the customer creation form, enter a name, email, and niche-relevant attributes (e.g., collector interests), then save.
  - Expected: The new customer appears in the customer list with all entered data visible.

- [ ] FT-02: Update an existing customer's details
  - Action: Open an existing customer record, change a field (e.g., email or interest category), and save.
  - Expected: The updated value is displayed in the record and persists after reloading the page.

- [ ] FT-03: Attach a related item (artwork) to a customer
  - Action: Open a customer record, add an artwork from the default items list as a related item, and save.
  - Expected: The artwork is listed under the customer's related items.

- [ ] FT-04: Apply a custom workflow status to a customer
  - Action: Select a customer and apply a workflow status such as "Invitation Sent" or "Purchase In Progress".
  - Expected: The selected status is shown on the customer record.

- [ ] FT-05: Filter customers by attribute or behavior
  - Action: Apply a filter (e.g., by status, interest, or purchase behavior) from the filter controls.
  - Expected: Only customers matching the filter criteria are listed.

- [ ] FT-06: Create a custom segment of customers
  - Action: Define a segment combining criteria (e.g., collectors with a purchase in the last period) and apply it.
  - Expected: The customer list updates to show only customers in that segment, and the segment can be re-applied later.

- [ ] FT-07: View a summary report of engagement and revenue
  - Action: Navigate to the summary/report view.
  - Expected: A report displays engagement metrics (e.g., invitations, interest activity) and revenue figures based on purchases.

- [ ] FT-08: Reconfigure report settings
  - Action: Change a report configuration option (e.g., time range or metric selection) and apply it.
  - Expected: The report content updates to reflect the new configuration.

## Constraint
- [ ] CS-01: Cannot create a customer with empty required fields
  - Action: Submit the customer creation form with required fields (e.g., name) left blank.
  - Expected: Submission is blocked and an inline validation message identifies the missing required field(s).

- [ ] CS-02: Cannot apply an invalid status to a customer
  - Action: Attempt to apply a workflow status not permitted for the customer's current state (or select an empty status).
  - Expected: The invalid status is rejected with a clear error message, and the customer's status remains unchanged.

- [ ] CS-03: Filters and segments cannot combine conflicting criteria without result
  - Action: Apply a filter combination that matches no customers (e.g., two mutually exclusive statuses).
  - Expected: The list shows an explicit "no results" state rather than unfiltered or partial data.

- [ ] CS-04: Duplicate customer prevention
  - Action: Create a customer using an email address already existing in the default data.
  - Expected: The save is rejected with a message indicating the email is already in use.

## Interaction
- [ ] IX-01: Success feedback after saving a customer
  - Action: Create or update a customer successfully.
  - Expected: A success toast/confirmation message appears and the list or record view refreshes to show the change.

- [ ] IX-02: Error feedback on failed save
  - Action: Trigger a save failure (e.g., via a validation error).
  - Expected: An error message appears near the affected action, and previously entered data is preserved.

- [ ] IX-03: Customer list responds immediately to filter changes
  - Action: Toggle a filter or segment on and off.
  - Expected: The list updates without a full page reload, and clearing filters restores the full default list.

- [ ] IX-04: Report view reflects configuration changes visually
  - Action: Change a report option and apply it.
  - Expected: The report's charts/figures re-render to match the new selection, with a visible loading or update state if needed.

## Content
- [ ] CT-01: Customer records display niche-relevant fields
  - Action: Inspect a customer record from the default data.
  - Expected: Fields relate to the niche CRM theme (e.g., collector interests, exhibition invitations, artwork purchases), with no generic or placeholder labels.

- [ ] CT-02: Related items show correct artwork details
  - Action: Open a customer's related items list.
  - Expected: Each attached artwork shows its correct title, artist, and other stored details matching the default data.

- [ ] CT-03: Report figures are consistent with underlying customer data
  - Action: Compare report revenue/engagement totals against the purchase and interaction data shown in customer records.
  - Expected: Report values are numerically consistent with the record data (no mismatched totals).

- [ ] CT-04: Status labels are meaningful to the workflow
  - Action: Review the available custom statuses in the status selector.
  - Expected: All statuses are specific to the niche workflow (e.g., "Invitation Sent", "Acquisition In Progress"), with no generic labels like "Status 1" or "TBD".