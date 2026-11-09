# Test Checklist

## Functionality

- [ ] FT-01: Customers list loads default customer records
  - Action: Open the CRM admin app and click "Customers" in the left navigation.
  - Expected: A customer table/list renders with the pre-existing default customers, each row showing identifying details (name plus at least one contact or segment field), and no error/empty-state placeholder.

- [ ] FT-02: Staff can create a new customer record
  - Action: Click "New Customer" (or "Add Customer"), fill in the required fields (name, plus email/phone as offered), and submit.
  - Expected: A success confirmation appears, the form closes, and the new customer appears in the customers list with the entered values.

- [ ] FT-03: Staff can open a customer's detailed record
  - Action: Click any customer row/name in the list.
  - Expected: A customer detail view opens showing the full profile (contact details, status, interests, invitations, purchases) and any related items already attached.

- [ ] FT-04: Staff can update an existing customer and the change persists
  - Action: Open a default customer, click "Edit", change a visible field (e.g., email or note), save, then reload the page and reopen that customer.
  - Expected: The edited value is shown after reload (change persisted), with a confirmation message on save.

- [ ] FT-05: Staff can attach a related artwork/item to a customer
  - Action: On a customer detail view, open the related-items/artworks section and use "Add" to select an existing item and confirm.
  - Expected: The selected item appears in that customer's related-items list, and the item count on the customer (detail and/or list) increases accordingly.

- [ ] FT-06: Staff can apply a custom workflow status to a customer
  - Action: On a customer detail view, open the "Status" control, choose a status from the list, and confirm.
  - Expected: The customer displays the newly applied status, and the same status is reflected for that customer in the customers list.

- [ ] FT-07: Staff can filter customers by attribute
  - Action: In the customers list, use the filter controls to filter by a customer attribute (e.g., status or interest) and apply.
  - Expected: The list narrows to only customers matching the chosen attribute, the active filter is indicated, and a result count is shown.

- [ ] FT-08: Staff can filter customers by behavior
  - Action: Apply a behavior-based filter (e.g., has an artwork purchase, or purchase/value threshold, or engagement level) in the customers list.
  - Expected: Only customers meeting that behavioral condition are listed, and the result count matches the condition.

- [ ] FT-09: Staff can save and reuse a customer segment
  - Action: Apply a filter combination, use "Save segment"/"Save view", give it a name, confirm, then clear filters and re-apply the saved segment.
  - Expected: The segment appears in the segments list, and re-applying it reproduces exactly the same customer set as when it was saved.

- [ ] FT-10: Staff can view a summary performance report
  - Action: Navigate to "Reports" (or "Summary") and open the default summary report.
  - Expected: The report renders engagement metrics and revenue metrics (cards/tables/charts) populated with real values from the default data, not zeros/placeholders.

- [ ] FT-11: Staff can configure the summary report
  - Action: Change the report configuration (e.g., date range, metric selection, or grouping such as by status/niche category) and apply.
  - Expected: The displayed metrics update to match the new configuration, and the control shows the currently applied configuration.

## Constraint

- [ ] CS-01: A customer cannot be saved with missing required information
  - Action: Open the new-customer form, leave a required field (e.g., name) empty, and submit.
  - Expected: Submission is blocked, a clear validation error identifies the missing field, and no customer record is created.

- [ ] CS-02: Duplicate customer records cannot be created
  - Action: Create a new customer using the email or name of an existing default customer and submit.
  - Expected: The save is rejected with a duplicate/already exists message, and the customers list count does not increase.

- [ ] CS-03: Only defined workflow statuses can be applied
  - Action: Attempt to apply a status value that is not among the available workflow statuses (e.g., via manual entry or by clearing the required status).
  - Expected: The invalid/empty status is rejected with an error, and the customer retains its previous valid status.

## Interaction

- [ ] IX-01: Success feedback is shown after creating and updating a customer
  - Action: Create a customer, then separately edit an existing customer and save.
  - Expected: Each completed action triggers a visible success confirmation (e.g., toast/banner) that disappears automatically or can be dismissed.

- [ ] IX-02: Filters apply and clear responsively without a page reload
  - Action: Apply a filter in the customers list, observe the results change, then click the active filter's remove/clear control.
  - Expected: The list updates in place to the filtered set, and on clearing, the full default customer list returns with no filter chip left active.

- [ ] IX-03: Navigation state and cross-section transitions are reflected
  - Action: Click between "Customers", a customer detail view, and "Reports" in the navigation.
  - Expected: The active navigation item is visibly highlighted, the correct view is displayed, and going back from detail to list preserves the previously applied filter state.

## Content

- [ ] CT-01: Customer records expose niche-relevant fields for the gallery example
  - Action: Open several default customers and review the fields shown on their detail views.
  - Expected: Fields cover collector interests, exhibition invitations, and artwork purchases (or equivalent niche workflow fields); no "Lorem ipsum", placeholder, or unrelated generic fields are present.

- [ ] CT-02: Attached artworks display correct and complete information
  - Action: Open the related-items/artworks section of a customer that has artworks attached.
  - Expected: Each item shows its artwork title and artist (plus price/value where stored) with a thumbnail/image that renders correctly — no broken images, empty labels, or duplicated names for different items.

- [ ] CT-03: Report content reflects engagement and revenue for the configured period
  - Action: Open the summary report, note the revenue and engagement values, then change the date range to a period containing fewer purchases and re-apply.
  - Expected: Metric labels are explicitly engagement- and revenue-oriented, values are numeric and currency-formatted where monetary, and the values change consistently with the selected period.