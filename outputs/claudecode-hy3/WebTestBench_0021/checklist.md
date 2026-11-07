# Test Checklist

## Functionality
- [ ] FT-01: Create a new customer record
  - Action: Click "Add Customer" / "New Customer", fill in name and required details, click "Save".
  - Expected: A new customer record appears in the customer list with the entered details.

- [ ] FT-02: Update an existing customer record
  - Action: Open an existing customer, edit a field (e.g., contact info), click "Save".
  - Expected: The customer record updates and shows the new value.

- [ ] FT-03: Attach a related item (e.g., artwork) to a customer
  - Action: Open a customer, click "Attach Item" / "Add Related Item", select an item from the list, confirm.
  - Expected: The selected item appears in the customer's related items section.

- [ ] FT-04: Apply a custom workflow status to a customer
  - Action: Open a customer, open the status control, select a defined custom status, confirm.
  - Expected: The customer now displays the selected custom status.

- [ ] FT-05: Filter customers by attribute or behavior
  - Action: Use the filter panel to set a criterion (e.g., "Interested in Sculpture"), apply the filter.
  - Expected: Only customers matching the criterion are shown in the list.

- [ ] FT-06: Segment customers into a group
  - Action: Select multiple customers and choose "Create Segment" / "Add to Segment", name it, save.
  - Expected: A new segment is created containing the selected customers.

- [ ] FT-07: View a configurable summary report
  - Action: Open the "Reports" / "Performance Summary" view.
  - Expected: A summary report renders showing engagement and revenue patterns.

- [ ] FT-08: Track a business-specific workflow step
  - Action: Open a customer, advance a workflow step (e.g., mark "Exhibition Invitation Sent").
  - Expected: The workflow step is recorded and reflected in the customer's workflow timeline.

## Constraint
- [ ] CS-01: Block customer creation with missing required fields
  - Action: Click "New Customer", leave required fields empty, click "Save".
  - Expected: Save is prevented and a validation message identifies the missing required field(s).

- [ ] CS-02: Prevent attaching a duplicate related item
  - Action: Attempt to attach an item already attached to the customer.
  - Expected: The duplicate attachment is rejected with an explanatory message.

- [ ] CS-03: Restrict status to defined workflow values
  - Action: Attempt to set a status not present in the defined workflow set.
  - Expected: The invalid status cannot be applied; only valid workflow statuses are selectable.

- [ ] CS-04: Require valid report configuration
  - Action: Open Reports and attempt to generate with an invalid/empty date range or no selected metrics.
  - Expected: Report generation is blocked until a valid date range and at least one metric are provided.

## Interaction
- [ ] IX-01: Confirm success after create/update
  - Action: Create or update a customer and save.
  - Expected: A success confirmation (toast/banner) appears indicating the record was saved.

- [ ] IX-02: Reflect status change visually
  - Action: Apply a custom status to a customer.
  - Expected: The status indicator updates immediately with a distinct visual state (color/label).

- [ ] IX-03: Re-render report on configuration change
  - Action: Change report settings (date range, metrics, segment) and apply.
  - Expected: The report updates dynamically to reflect the new configuration without a full page reload.

## Content
- [ ] CT-01: Customer record shows niche-relevant fields
  - Action: Open a customer record.
  - Expected: Fields relevant to the niche (e.g., interests, purchases, invitations) are present and populated from default data.

- [ ] CT-02: Report displays engagement and revenue metrics
  - Action: Open the summary report.
  - Expected: Report contains both engagement metrics (e.g., interactions) and revenue metrics relevant to the niche.

- [ ] CT-03: Related items show relevant media and info
  - Action: Open a customer and view attached related items (e.g., artworks).
  - Expected: Each item displays relevant media (image/icon) and identifying info consistent with the niche theme.