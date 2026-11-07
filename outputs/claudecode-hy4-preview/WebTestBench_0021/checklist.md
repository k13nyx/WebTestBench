# Test Checklist

## Functionality

- [ ] FT-01: Staff can create a new customer record
  - Action: Click "Add Customer" / "New Collector", fill Name, Email, and Collector Interests, then click "Save".
  - Expected: Customer appears in the customer list with the exact name and email entered, and a confirmation is shown.

- [ ] FT-02: Staff can update an existing customer record
  - Action: Open an existing default customer, edit the Name and Collector Interests fields, click "Save", then reload the page.
  - Expected: The detail view and list show the updated values after reload; no other fields are altered.

- [ ] FT-03: Staff can attach a related item (artwork) to a customer
  - Action: Open a customer, go to the "Artworks" / "Related Items" section, attach an existing default artwork, and save.
  - Expected: The artwork title appears in that customer's related-items list and is visible after reload.

- [ ] FT-04: Staff can log an exhibition invitation for a customer
  - Action: Open a customer's workflow/activity timeline, add an "Exhibition Invitation" entry for a default exhibition, and save.
  - Expected: The invitation entry (exhibition name + date) appears in that customer's timeline and in their workflow history.

- [ ] FT-05: Staff can record an artwork purchase for a customer
  - Action: Open a customer, record a purchase of an attached default artwork with a positive amount, and save.
  - Expected: The purchase appears in the customer's history with artwork title and amount, and the customer's total revenue figure increases by that amount.

- [ ] FT-06: Staff can apply a custom workflow status to a customer
  - Action: Open a customer and assign a custom status (e.g., "Invited", "Negotiating", "Closed – Sold") from the status control, then save.
  - Expected: The chosen status is displayed on the customer's detail view and in the customer list row.

- [ ] FT-07: Staff can filter customers by attributes
  - Action: Apply a filter on an attribute (e.g., status = a specific value, or interest = a specific art category) and apply it.
  - Expected: The customer list shows only records matching that attribute, and the displayed count equals the number of matching rows.

- [ ] FT-08: Staff can segment customers by behavior
  - Action: Apply a behavior-based filter (e.g., "made a purchase", "invited but no purchase", or engagement within a date range).
  - Expected: The list contains only customers satisfying that behavior; customers that clearly do not satisfy it are absent.

- [ ] FT-09: Staff can view a summary report of engagement and revenue
  - Action: Open the Reports / Summary section with default settings.
  - Expected: The report displays at least one engagement metric (e.g., invitations sent, responses) and at least one revenue metric (e.g., total sales), each with a non-empty numeric value.

- [ ] FT-10: Staff can configure the summary report
  - Action: Change a report configuration option (e.g., date range or displayed metric) and apply it.
  - Expected: The report values and/or chart update to reflect the new configuration without a page reload.

## Constraint

- [ ] CS-01: Customer cannot be saved with empty required fields
  - Action: Open the new-customer form, leave Name and Email blank, and click "Save".
  - Expected: Save is blocked; an inline error message appears on each empty required field and no customer is added to the list.

- [ ] CS-02: Duplicate customer email is rejected
  - Action: Create a customer using the email address of an existing default customer and click "Save".
  - Expected: Save is blocked with an error stating the email is already in use; no duplicate record is created.

- [ ] CS-03: The same artwork cannot be attached to one customer twice
  - Action: On a customer already linked to a default artwork, attempt to attach that same artwork again.
  - Expected: The duplicate is prevented (option unavailable or error shown); the related-items list still contains that artwork exactly once.

- [ ] CS-04: Only defined custom statuses can be applied
  - Action: Attempt to assign a status value that is not in the configured status list (e.g., by clearing/overriding the picker).
  - Expected: The application rejects it — no arbitrary or blank status is persisted; the customer retains its previous valid status.

- [ ] CS-05: Filters that match nothing show an empty state, not stale data
  - Action: Apply a filter combination that no default customer satisfies.
  - Expected: The list is empty and shows an explicit "No customers match" empty-state message; no previously loaded rows remain.

## Interaction

- [ ] IX-01: Selecting a customer opens its detail view
  - Action: Click a customer row in the customer list.
  - Expected: That customer's detail view opens showing its full record (contact info, interests, related items, status, history).

- [ ] IX-02: Success feedback appears after a customer is saved
  - Action: Create or update a customer and save it.
  - Expected: A success confirmation message/toast appears (e.g., "Customer saved") and the form closes or returns to the list.

- [ ] IX-03: Active filters are shown as removable chips
  - Action: Apply two different filters, then click the "×" / "Clear" control on one chip.
  - Expected: The chip disappears, the list updates to reflect the remaining filter, and a "Clear all" action restores the full list.

## Content

- [ ] CT-01: Interface uses the niche's terminology (gallery example)
  - Action: Review labels, headers, and field names across the customer list, detail view, and reports.
  - Expected: Terminology matches the gallery niche ("Collector"/"Customer", "Artwork", "Exhibition Invitation", "Purchase", "Interests"); no generic unrelated template terms (e.g., "Leads", "Deals", "Units Sold") are used.

- [ ] CT-02: Report figures are properly labeled and contain no placeholder or broken data
  - Action: Inspect all metrics, chart labels, and images/icons on the summary report.
  - Expected: Every metric shows a descriptive label, numeric value with correct unit (currency symbol or count) and its reporting period; no "Lorem ipsum", "N/A", "undefined", or broken-image icons appear anywhere.