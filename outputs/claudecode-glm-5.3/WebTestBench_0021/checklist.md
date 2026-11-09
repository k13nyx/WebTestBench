# Test Checklist

## Functionality
- [ ] FT-01: Customer list displays default customer records
  - Action: Open the CRM admin page and go to the Customers section.
  - Expected: The list shows pre-existing default customers with identifying details (e.g., name, contact info) — the list is not empty.

- [ ] FT-02: Staff can create a new customer record
  - Action: Click the "Add Customer" (or equivalent) button, fill in all required fields (e.g., name, email, phone), and save.
  - Expected: The new customer appears in the customer list.

- [ ] FT-03: Staff can update an existing customer's details
  - Action: Open a default customer's record, edit one field (e.g., phone number), and save.
  - Expected: The updated value is displayed and persists when the record is re-opened.

- [ ] FT-04: Staff can attach a related item (artwork) to a customer
  - Action: On a customer's detail page, use the "Attach Artwork" / related-items control to attach an existing default artwork.
  - Expected: The artwork appears in that customer's related items list.

- [ ] FT-05: Staff can apply a custom workflow status to a customer
  - Action: On a customer record, change the workflow status to a custom status (e.g., "Invited to Exhibition") and save.
  - Expected: The customer shows the new custom status in both the detail view and the customer list.

- [ ] FT-06: Staff can filter/segment customers by attribute
  - Action: Apply a filter on the customer list (e.g., by status "Invited to Exhibition" or by an interest attribute).
  - Expected: Only customers matching the selected filter are displayed; non-matching customers are excluded.

- [ ] FT-07: Summary report displays engagement and revenue metrics
  - Action: Open the summary/reports section.
  - Expected: Performance metrics covering engagement (e.g., invitations, interactions) and revenue (e.g., purchase amounts) are displayed with values derived from default data.

- [ ] FT-08: Summary report is configurable
  - Action: Change a report configuration option (e.g., date range, metric, or report type selector) and apply it.
  - Expected: The report content updates to reflect the selected configuration (values/labels change accordingly).

## Constraint
- [ ] CS-01: Cannot save a customer with empty required fields
  - Action: Open the create-customer form, leave a required field (e.g., name) empty, and attempt to save.
  - Expected: Save is blocked; a validation error identifies the missing required field; no customer record is created.

- [ ] CS-02: Custom status must come from the defined workflow status list
  - Action: Open the status control on a customer record and attempt to set a status (including trying to type an arbitrary free-text status).
  - Expected: Only the predefined workflow statuses are selectable; an invalid/unknown status cannot be applied.

- [ ] CS-03: Filter with no matching customers returns an empty state
  - Action: Apply a filter combination that matches no default customers.
  - Expected: A clear "no results" empty state is shown; the app does not crash and does not display the full unfiltered list.

## Interaction
- [ ] IX-01: Success feedback shown after customer creation
  - Action: Successfully create a new customer via the form.
  - Expected: A success toast/message appears and the customer list refreshes to include the new record.

- [ ] IX-02: Status change reflects immediately in the UI
  - Action: Change a customer's workflow status from the detail page.
  - Expected: The status badge/value updates immediately without requiring a full page reload.

- [ ] IX-03: Customer list updates live as filter criteria change
  - Action: Type into the search box or change filter selections; then clear the filter.
  - Expected: The list updates instantly to match the criteria; clearing the filter restores the full default list.

- [ ] IX-04: Clicking a customer opens their detail view
  - Action: Click a customer row in the list.
  - Expected: The customer's detail page opens, showing that customer's records, related items, and workflow status.

## Content
- [ ] CT-01: Workflow statuses and labels match the gallery niche
  - Action: Review the available custom statuses and workflow terminology across the app.
  - Expected: They reflect the gallery workflow (e.g., collector interests, exhibition invitations, artwork purchases), not only generic CRM terms.

- [ ] CT-02: Attached artwork details are relevant and complete
  - Action: Open a customer's related artworks list.
  - Expected: Each item shows artwork-relevant details (e.g., title, artist, thumbnail or price) consistent with the gallery theme.

- [ ] CT-03: Summary report content reflects the niche's engagement and revenue patterns
  - Action: Review the metrics, labels, and figures in the summary report.
  - Expected: Metrics are engagement and revenue measures relevant to the niche (e.g., exhibition invitations, artwork purchases, sales revenue), not unrelated placeholders.

- [ ] CT-04: All images load and are theme-relevant
  - Action: Check all images in the app (artwork thumbnails, avatars, report graphics).
  - Expected: Every image renders (no broken-image icons) and is directly relevant to the gallery/artwork theme.