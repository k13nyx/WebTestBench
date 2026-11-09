# Test Checklist

## Functionality
- [ ] FT-01: Create a new customer record
  - Action: Click the customer creation button (e.g., "Add Customer" / "New Customer"), fill in name and contact details, and save.
  - Expected: The customer is saved and appears in the customer list with the entered details.
- [ ] FT-02: Update an existing customer record
  - Action: Open a pre-existing customer, edit a field (e.g., change email or phone), and save.
  - Expected: The updated value is displayed on the customer record after saving.
- [ ] FT-03: Attach related items (e.g., artworks) to a customer
  - Action: On a customer detail page, use the attach/add-item control to link an artwork from the existing artwork list, then save.
  - Expected: The artwork appears in the customer's related items section with its name/details.
- [ ] FT-04: Apply a custom workflow status to a customer
  - Action: Open a customer record, change its status to a business-specific status (e.g., "Invited to Exhibition", "Interested Collector"), and save.
  - Expected: The customer's status shows the newly selected status on the detail page and list view.
- [ ] FT-05: Filter customers by behavior or attribute
  - Action: Apply a filter on the customer list (e.g., by status, interest category, or purchase behavior).
  - Expected: Only customers matching the filter criteria are displayed.
- [ ] FT-06: Segment customers based on a saved criteria set
  - Action: Create or select a segment (e.g., "Collectors interested in modern art") and view the segment.
  - Expected: The segment shows the subset of customers matching the segment definition.
- [ ] FT-07: View a summary report showing engagement and revenue patterns
  - Action: Navigate to the reports/summary section and view the default report.
  - Expected: The report displays engagement metrics (e.g., contacts, invitations, interests) and revenue figures (e.g., purchases/sales totals).
- [ ] FT-08: Configure the summary report content
  - Action: Open report settings/configuration, change the metrics or grouping shown (e.g., add "revenue by category"), and apply.
  - Expected: The report updates to reflect the selected configuration.
- [ ] FT-09: Track a business-specific workflow on a customer
  - Action: View a customer's workflow/history section showing tracked activities (e.g., invitations sent, artworks purchased).
  - Expected: Recorded workflow activities for that customer are listed with relevant details (type, date, item).

## Constraint
- [ ] CS-01: Cannot save a customer with empty required fields
  - Action: Open the customer creation form, leave required fields (e.g., name) blank, and attempt to save.
  - Expected: The save is blocked and a validation message indicates the required field(s) are missing.
- [ ] CS-02: Custom status values must come from the defined workflow statuses
  - Action: Open the status selector on a customer record and inspect the available options.
  - Expected: Only predefined/business-specific statuses are selectable; arbitrary free-text statuses are not accepted as a valid status.
- [ ] CS-03: Filters/segments with no matching customers show an empty result state
  - Action: Apply a filter or open a segment that matches no customers.
  - Expected: The list shows an explicit empty state (e.g., "No customers match") rather than unrelated customers or an error.
- [ ] CS-04: Attach the same related item to a customer only once (no duplicates)
  - Action: On a customer record, attempt to attach an artwork that is already attached.
  - Expected: The system prevents the duplicate (blocked, or existing attachment is kept without adding a second entry).
- [ ] CS-05: Report configuration with no selectable metrics cannot be applied
  - Action: Open report configuration, deselect all metrics, and attempt to apply.
  - Expected: Applying is blocked or defaults are retained; the report never renders completely empty/invalid.

## Interaction
- [ ] IX-01: Success feedback after saving a customer or change
  - Action: Create or update a customer and save.
  - Expected: A visible success confirmation (toast/message) appears confirming the save.
- [ ] IX-02: Opening a customer from the list shows its detail view
  - Action: Click a customer row/name in the customer list.
  - Expected: The customer's detail page opens showing that customer's profile, status, and related items.

## Content
- [ ] CT-01: Customer records display niche-relevant attributes
  - Action: Open the customer list/detail views.
  - Expected: Displayed fields reflect the niche business context (e.g., collector interests, purchase history, invitation status), not generic-only placeholders.
- [ ] CT-02: Related items shown are actual artworks with relevant details
  - Action: View a customer's attached items.
  - Expected: Each attached item shows artwork-relevant information (e.g., title, artist, price) — content matches the gallery/artwork theme.
- [ ] CT-03: Summary report data aligns with displayed customer/workflow records
  - Action: Compare counts in the summary report (e.g., number of customers with a given status, total purchase revenue) against the customer list.
  - Expected: Report figures are consistent with the actual records in the application.