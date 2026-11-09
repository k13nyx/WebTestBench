# Test Result

## Functionality

- [X] FT-01: Create a new customer record
  - Action: Click the customer creation button (e.g., "Add Customer" / "New Customer"), fill in name and contact details, and save.
  - Expected: The customer is saved and appears in the customer list with the entered details.
  - Note: "Add Customer" → filled Nora Whitfield / nora.w@collector.com / +1 (555) 111-2222 → "Customer created" toast, and the record appeared at the top of the list with the entered email, phone and "New Lead" status. (Caveat: the record is lost after a full page reload — see FT-04 bug.)

- [X] FT-02: Update an existing customer record
  - Action: Open a pre-existing customer, edit a field (e.g., change email or phone), and save.
  - Expected: The updated value is displayed on the customer record after saving.
  - Note: Edit dialog on Victoria Ashworth → phone changed to "+1 (555) 999-0000" → "Customer updated" toast and the detail page immediately displayed the new phone.

- [X] FT-03: Attach related items (e.g., artworks) to a customer
  - Action: On a customer detail page, use the attach/add-item control to link an artwork from the existing artwork list, then save.
  - Expected: The artwork appears in the customer's related items section with its name/details.
  - Note: "Add Artwork" dialog on Victoria Ashworth → selected "Urban Fragments" (David Park, $3,200) → it appeared in "Interested Artworks" with artist/year/medium/price and the "Interested In" counter went 2 → 3.

- [ ] FT-04: Apply a custom workflow status to a customer
  - Action: Open a customer record, change its status to a business-specific status (e.g., "Invited to Exhibition", "Interested Collector"), and save.
  - Expected: The customer's status shows the newly selected status on the detail page and list view.
  - Bug Report:
    - Issue: Status change does not propagate to the list view and is not persisted
    - Actual: On the detail page the status combobox change to "Negotiating" applied immediately (badge + "Status updated" toast), but navigating back via "Back to Customers" the list still showed Victoria Ashworth as "VIP Collector". Additionally, after a page reload even the detail page reverted to "VIP Collector", i.e., the change is held only in transient detail-page state and is never saved to the shared customer data.

- [X] FT-05: Filter customers by behavior or attribute
  - Action: Apply a filter on the customer list (e.g., by status, interest category, or purchase behavior).
  - Expected: Only customers matching the filter criteria are displayed.
  - Note: Status filter "VIP Collector" → list reduced to exactly Victoria Ashworth and Alexander Petrov.

- [ ] FT-06: Segment customers based on a saved criteria set
  - Action: Create or select a segment (e.g., "Collectors interested in modern art") and view the segment.
  - Expected: The segment shows the subset of customers matching the segment definition.
  - Bug Report:
    - Issue: Missing feature — no segment functionality exists
    - Actual: No segment UI exists anywhere. The Customers page offers only a text search and a status dropdown; the customer row menu contains only "View Details", "Send Email", "Log Interaction"; the Settings page has gallery info/workflow/notification toggles; Reports has only Revenue/Engagement/Sales Funnel tabs. There is no way to create, save, or view a customer segment.

- [X] FT-07: View a summary report showing engagement and revenue patterns
  - Action: Navigate to the reports/summary section and view the default report.
  - Expected: The report displays engagement metrics (e.g., contacts, invitations, interests) and revenue figures (e.g., purchases/sales totals).
  - Note: Reports page shows KPIs (Total Revenue $740,000, Avg. Purchase Value, Conversion Rate 38%, Active Relationships 7), a Revenue tab (Monthly Revenue Trend, Revenue by Customer Type, Artist Performance) and an Engagement tab (Customer Engagement Over Time with Emails/Calls/Gallery Visits, Customer Acquisition).

- [ ] FT-08: Configure the summary report content
  - Action: Open report settings/configuration, change the metrics or grouping shown (e.g., add "revenue by category"), and apply.
  - Expected: The report updates to reflect the selected configuration.
  - Bug Report:
    - Issue: Missing feature — no report configuration control
    - Actual: The Reports page contains only three fixed tabs (Revenue, Engagement, Sales Funnel) and static charts. A DOM scan of all buttons/links/controls on the page found no settings/configuration/customize entry point, so metrics or grouping cannot be changed.

- [X] FT-09: Track a business-specific workflow on a customer
  - Action: View a customer's workflow/history section showing tracked activities (e.g., invitations sent, artworks purchased).
  - Expected: Recorded workflow activities for that customer are listed with relevant details (type, date, item).
  - Note: The "Activity" tab on the customer detail page shows an "Interaction History" list, e.g. type "visit" — January 10, 2024 — "Private viewing of new Elena Voss collection"; type "exhibition" — December 1, 2023 — "Attended winter gala".

## Constraint

- [X] CS-01: Cannot save a customer with empty required fields
  - Action: Open the customer creation form, leave required fields (e.g., name) blank, and attempt to save.
  - Expected: The save is blocked and a validation message indicates the required field(s) are missing.
  - Note: Clicking "Create Customer" with blank fields showed toast "Missing required fields — Please fill in first name, last name, and email", the dialog stayed open and no record was created.

- [X] CS-02: Custom status values must come from the defined workflow statuses
  - Action: Open the status selector on a customer record and inspect the available options.
  - Expected: Only predefined/business-specific statuses are selectable; arbitrary free-text statuses are not accepted as a valid status.
  - Note: The status selector is a closed dropdown offering exactly 7 predefined statuses (New Lead, Contacted, Interested, Negotiating, Purchased, VIP Collector, Inactive) with no free-text input.

- [X] CS-03: Filters/segments with no matching customers show an empty result state
  - Action: Apply a filter or open a segment that matches no customers.
  - Expected: The list shows an explicit empty state (e.g., "No customers match") rather than unrelated customers or an error.
  - Note: With status filter "VIP Collector" active plus a non-matching search term, the list area showed an explicit "No customers found" message with no rows and no error.

- [X] CS-04: Attach the same related item to a customer only once (no duplicates)
  - Action: On a customer record, attempt to attach an artwork that is already attached.
  - Expected: The system prevents the duplicate (blocked, or existing attachment is kept without adding a second entry).
  - Note: The "Add Artwork" picker only lists artworks not yet attached — after attaching, already-attached artworks are excluded from the selectable list, making duplicates impossible.

- [ ] CS-05: Report configuration with no selectable metrics cannot be applied
  - Action: Open report configuration, deselect all metrics, and attempt to apply.
  - Expected: Applying is blocked or defaults are retained; the report never renders completely empty/invalid.
  - Bug Report:
    - Issue: Untestable — report configuration feature does not exist
    - Actual: There is no report configuration UI on the Reports page (only fixed Revenue/Engagement/Sales Funnel tabs), so there is no way to deselect metrics or apply a configuration; the constraint could not be exercised.

## Interaction

- [X] IX-01: Success feedback after saving a customer or change
  - Action: Create or update a customer and save.
  - Expected: A visible success confirmation (toast/message) appears confirming the save.
  - Note: Toasts observed for every save: "Customer created — Nora Whitfield has been added", "Customer updated — Changes have been saved successfully", "Status updated — Customer status changed to Negotiating", "Artwork added — The artwork has been added to interested list".

- [X] IX-02: Opening a customer from the list shows its detail view
  - Action: Click a customer row/name in the customer list.
  - Expected: The customer's detail page opens showing that customer's profile, status, and related items.
  - Note: Clicking "Victoria Ashworth" navigated to /customers/cust-1 showing profile (name, email, phone, customer-since), status badge, stat cards, and tabs with Interested Artworks / Purchase History.

## Content

- [X] CT-01: Customer records display niche-relevant attributes
  - Action: Open the customer list/detail views.
  - Expected: Displayed fields reflect the niche business context (e.g., collector interests, purchase history, invitation status), not generic-only placeholders.
  - Note: Records show gallery-specific data: workflow statuses (VIP Collector, Negotiating…), Total Spent / Purchases / Last Contact, interest tags (contemporary-collector, asian-art-interest, high-value, vip), interested artworks and purchase history.

- [X] CT-02: Related items shown are actual artworks with relevant details
  - Action: View a customer's attached items.
  - Expected: Each attached item shows artwork-relevant information (e.g., title, artist, price) — content matches the gallery/artwork theme.
  - Note: Attached items show title, artist, year, medium and price with availability, e.g. "Abstract Emotions III — Marcus Chen · 2024 · Acrylic — $8,900 Available"; purchase history items show "Sunset Over Manhattan — Elena Voss · Purchased November 20, 2023 — $12,500".

- [X] CT-03: Summary report data aligns with displayed customer/workflow records
  - Action: Compare counts in the summary report (e.g., number of customers with a given status, total purchase revenue) against the customer list.
  - Expected: Report figures are consistent with the actual records in the application.
  - Note: Sum of per-customer "Total Spent" in the list = $156,000 + $24,500 + $0 + $89,000 + $5,500 + $0 + $45,000 + $420,000 = $740,000, matching the report's "Total Revenue (All Time) $740,000"; "Active Relationships 7" matches 8 customers minus 1 Inactive; dashboard "VIP Clients 2" matches the two VIP Collector records.
