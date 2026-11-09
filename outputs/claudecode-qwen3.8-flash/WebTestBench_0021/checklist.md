# Test Checklist

## Functionality
- [ ] FT-01: Customer list displays default records
  - Action: Open the CRM admin page and navigate to the Customers view.
  - Expected: A list/table of pre-existing customer records is shown with names and at least one niche-relevant attribute (e.g., interest or status) per row.

- [ ] FT-02: Staff can create a new customer
  - Action: Click "New Customer" (or equivalent), fill all required fields (e.g., name, contact), and submit.
  - Expected: The customer is saved and appears in the customer list; opening it shows the entered values.

- [ ] FT-03: Staff can update an existing customer
  - Action: Open a default customer, modify a detail field (e.g., contact info or interest), and save.
  - Expected: The update succeeds; reopening the record and the list view both show the new value.

- [ ] FT-04: Customer detail shows gallery-specific record sections
  - Action: Open a default customer's detail view.
  - Expected: Dedicated sections/fields for collectors' interests, exhibition invitations, and artwork purchases are present and populated for records that have that data.

- [ ] FT-05: Staff can attach an artwork to a customer
  - Action: On a customer detail page, use the attach/link control to add an artwork item, then save.
  - Expected: The artwork appears under that customer's related-items section.

- [ ] FT-06: Staff can apply a custom workflow status
  - Action: Change a customer's status via the status selector and save.
  - Expected: The new status is applied and shown on the record and in the list view.

- [ ] FT-07: Filter/segment customers by behavior or attribute
  - Action: Apply a filter (e.g., interest category = a default value, or "has purchased artwork") and submit.
  - Expected: The list updates to show only customers matching the filter; non-matching customers are excluded.

- [ ] FT-08: Performance summary report is viewable
  - Action: Navigate to the Reports/Summary section.
  - Expected: A summary report is displayed containing both engagement metrics (e.g., invitations sent/accepted) and revenue metrics (e.g., purchase totals) derived from the default data.

- [ ] FT-09: Report configuration is changeable
  - Action: On the report view, change a configuration control (e.g., date range, metric, or segment) and apply.
  - Expected: The displayed report values change or re-aggregate accordingly (not a static hardcoded view).

## Constraint
- [ ] CS-01: Required-field validation blocks empty customer submission
  - Action: Open "New Customer", leave a required field (e.g., name) empty, and attempt to save.
  - Expected: Save is blocked with a visible validation error identifying the missing field; no new record is created.

- [ ] CS-02: Status selection is limited to defined workflow statuses
  - Action: Open the status selector on a customer.
  - Expected: Only predefined custom statuses (matching the business workflow, e.g., gallery stages) are selectable; no free-text or unrelated generic statuses are accepted.

- [ ] CS-03: Attached artwork belongs only to the linked customer
  - Action: After attaching an artwork to customer A (FT-05), open customer B's detail page.
  - Expected: The artwork appears only under customer A's related items; customer B's record is unchanged.

## Interaction
- [ ] IX-01: Confirmation shown after record changes
  - Action: Perform a save action (create customer, update customer, or attach artwork).
  - Expected: A visible confirmation (toast or inline message such as "saved" / "customer created") appears after the successful action.

- [ ] IX-02: Status change reflected immediately in the UI
  - Action: Apply a new status to a customer from the list or detail view.
  - Expected: The status badge/label updates instantly in place (with distinct visual styling per status) without needing a full app restart or manual re-navigation.

- [ ] IX-03: Active filter state is visible and clearable
  - Action: Apply a filter (FT-07), then use the clear/reset control.
  - Expected: Active filters are displayed (e.g., highlighted controls or filter chips); clearing restores the full unfiltered customer list.

## Content
- [ ] CT-01: Default customer data matches the niche theme
  - Action: Inspect the default customers' records.
  - Expected: Records contain gallery-relevant content (collector names, art interests, exhibition invitations, purchase entries) — not placeholder/lorem text unrelated to the theme.

- [ ] CT-02: Custom status labels reflect the gallery workflow
  - Action: View the available status options.
  - Expected: Statuses correspond to workflow stages for the niche (e.g., "Interested Collector", "Invited to Exhibition", "Artwork Purchased"), not generic ones like "Open/Closed" only.

- [ ] CT-03: Artwork items display relevant details
  - Action: Open a customer's attached artwork entry or the artwork attach picker.
  - Expected: Each artwork shows meaningful attributes (e.g., title, artist, price) appropriate to a gallery context.

- [ ] CT-04: Report labels align with engagement and revenue intent
  - Action: Read the titles/labels of metrics on the summary report.
  - Expected: Labels explicitly reference engagement and revenue for the niche (e.g., "Invitations sent", "Artwork sales revenue"); no irrelevant or empty/unlabeled sections.