# Test Result

## Functionality

- [X] FT-01: Customer list displays default records
  - Action: Open the CRM admin page and navigate to the Customers view.
  - Expected: A list/table of pre-existing customer records is shown with names and at least one niche-relevant attribute (e.g., interest or status) per row.
  - *Verified: 8 default rows (Victoria Ashworth/VIP Collector, James Morrison/Negotiating, Sophia Chen/Interested, Robert Williams/Purchased, Emma Thompson/Contacted, Michael Foster/New Lead, Isabella Romano/Inactive, Alexander Petrov/VIP Collector), each with email, phone, niche tags (`high-value`, `contemporary-collector`, `asian-art-interest`, `bulk-buyer`), Total Spent, Purchases, Last Contact.*

- [ ] FT-02: Staff can create a new customer
  - Action: Click "New Customer" (or equivalent), fill all required fields (e.g., name, contact), and submit.
  - Expected: The customer is saved and appears in the customer list; opening it shows the entered values.
  - Bug Report:
    - Issue: Created record not saved / broken detail route
    - Actual: "Add Customer" → Eleanor Whitfield / e.whitfield@collector.com / +1 (555) 111-2222 produced the toast "Customer created — Eleanor Whitfield has been added." and appeared in the list, but clicking its row link (`/customers/cust-1794111446437`) renders **"Customer not found"** — the entered values are never viewable. The record then disappears entirely: after navigating to Dashboard and back the list is again 8 default customers, and after a reload only `cust-1`…`cust-8` exist. `localStorage` is empty, so nothing is persisted anywhere.

- [ ] FT-03: Staff can update an existing customer
  - Action: Open a default customer, modify a detail field (e.g., contact info or interest), and save.
  - Expected: The update succeeds; reopening the record and the list view both show the new value.
  - Bug Report:
    - Issue: Update not persisted / list view stale
    - Actual: On James Morrison (cust-2), Edit → email `j.morrison@corporate-updates.com`, phone `+1 (555) 999-0000` → "Save Changes" fired the toast "Customer updated — Changes have been saved successfully." and the header updated. However the **list view still showed the old values** (`j.morrison@company.com`, `+1 (555) 345-6789`), and **reopening the record reverted to the old values** as well. The same non-persistence applies to every field tested.

- [X] FT-04: Customer detail shows gallery-specific record sections
  - Action: Open a default customer's detail view.
  - Expected: Dedicated sections/fields for collectors' interests, exhibition invitations, and artwork purchases are present and populated for records that have that data.
  - *Verified on cust-1: "Interested Artworks" (Abstract Emotions III, Memories of Blue), "Purchase History" (Sunset Over Manhattan, Bronze Horizon), "Activity → Interaction History" with typed entries `Visit — Private viewing of new Elena Voss collection` and `Exhibition — Attended winter gala`, and "Notes & Tags" with an explicit **Interests** field (Contemporary, Abstract, Sculpture).*

- [X] FT-05: Staff can attach an artwork to a customer
  - Action: On a customer detail page, use the attach/link control to add an artwork item, then save.
  - Expected: The artwork appears under that customer's related-items section.
  - *Verified: "Add Artwork" → picker "Add Interested Artwork" → clicked "Urban Fragments" → toast "Artwork added — The artwork has been added to interested list." and the item appeared under cust-1's Interested Artworks with full details (David Park · 2024 · Photography · $3,200 · Available). See Notes — this attachment is lost on re-mount.*

- [ ] FT-06: Staff can apply a custom workflow status
  - Action: Change a customer's status via the status selector and save.
  - Expected: The new status is applied and shown on the record and in the list view.
  - Bug Report:
    - Issue: Status change not reflected in list view / not persisted
    - Actual: On cust-1 the status selector → "Negotiating" produced the toast "Status updated — Customer status changed to Negotiating" and the in-page badge changed. But the **list row for Victoria Ashworth still showed "VIP Collector"**, and re-opening the record after navigating away showed "VIP Collector" again (status reverted).

- [X] FT-07: Filter/segment customers by behavior or attribute
  - Action: Apply a filter (e.g., interest category = a default value, or "has purchased artwork") and submit.
  - Expected: The list updates to show only customers matching the filter; non-matching customers are excluded.
  - *Verified: status filter "VIP Collector" → list reduced to exactly 2 rows (Victoria Ashworth, Alexander Petrov), 6 non-matching excluded; search box `asian-art-interest` → exactly 1 row (Sophia Chen). Both filters re-aggregate live from the data.*

- [X] FT-08: Performance summary report is viewable
  - Action: Navigate to the Reports/Summary section.
  - Expected: A summary report is displayed containing both engagement metrics (e.g., invitations sent/accepted) and revenue metrics (e.g., purchase totals) derived from the default data.
  - *Verified: `/reports` shows KPI tiles Total Revenue (All Time) $740,000 (equals the sum of the 8 rows' Total Spent), Avg. Purchase Value $123,333, Conversion Rate 38%, Active Relationships 7, plus tabs **Revenue** (Monthly Revenue Trend, Revenue by Customer Type: VIP Collectors/Regular Buyers/New Collectors, Artist Performance) and **Engagement** (Customer Engagement Over Time — Emails/Calls/Gallery Visits, Customer Acquisition).*

- [X] FT-09: Report configuration is changeable
  - Action: On the report view, change a configuration control (e.g., date range, metric, or segment) and apply.
  - Expected: The displayed report values change or re-aggregate accordingly (not a static hardcoded view).
  - *Verified: switching the metric tabs (Revenue → Engagement → Sales Funnel) re-renders different charts/aggregations — Sales Funnel shows a conversion funnel plus "Customer Status Breakdown: New Lead 1 (13%), Contacted 1 (13%), Interested 1 (13%), Negotiating 1 (13%), Purchased 1 (13%), VIP Collector 2 (25%), Inactive 1 (13%)", which exactly matches the 8 default records (not hardcoded). Note: no date-range control exists.*

## Constraint

- [X] CS-01: Required-field validation blocks empty customer submission
  - Action: Open "New Customer", leave a required field (e.g., name) empty, and attempt to save.
  - Expected: Save is blocked with a visible validation error identifying the missing field; no new record is created.
  - *Verified: clicking "Create Customer" with an empty form (fields labelled `First Name *`, `Last Name *`, `Email *`) raised the notification "Missing required fields — Please fill in first name, last name, and email."; the dialog stayed open, the record count stayed at 8.*

- [X] CS-02: Status selection is limited to defined workflow statuses
  - Action: Open the status selector on a customer.
  - Expected: Only predefined custom statuses (matching the business workflow, e.g., gallery stages) are selectable; no free-text or unrelated generic statuses are accepted.
  - *Verified: the Radix Select offers exactly 7 closed options — New Lead, Contacted, Interested, Negotiating, Purchased, VIP Collector, Inactive. No editable/free-text input exists in the selector.*

- [X] CS-03: Attached artwork belongs only to the linked customer
  - Action: After attaching an artwork to customer A (FT-05), open customer B's detail page.
  - Expected: The artwork appears only under customer A's related items; customer B's record is unchanged.
  - *Verified: baselines captured first — cust-2 (James Morrison) = Interested [Urban Fragments, Digital Dreams], Purchases [The Garden Path]. After attaching "Urban Fragments" to cust-1 (Victoria), cust-1 grew to 3 interested items while cust-2's panel was **byte-identical to baseline** (1× Urban Fragments, no duplicate, no new entries).*

## Interaction

- [X] IX-01: Confirmation shown after record changes
  - Action: Perform a save action (create customer, update customer, or attach artwork).
  - Expected: A visible confirmation (toast or inline message such as "saved" / "customer created") appears after the successful action.
  - *Verified in all four paths, in the `role="status"` notification region: "Customer created", "Customer updated — Changes have been saved successfully.", "Artwork added — The artwork has been added to interested list.", "Status updated — Customer status changed to Negotiating".*

- [X] IX-02: Status change reflected immediately in the UI
  - Action: Apply a new status to a customer from the list or detail view.
  - Expected: The status badge/label updates instantly in place (with distinct visual styling per status) without needing a full app restart or manual re-navigation.
  - *Verified: selecting "Purchased" on cust-1 changed the badge in place with no re-navigation, and styling differs per status — VIP Collector = `bg-primary/10 text-primary border-primary/20`, Purchased = `bg-success/10 text-success border-success/20`, Negotiating = `bg-accent/10 text-accent border-accent/20`.*

- [ ] IX-03: Active filter state is visible and clearable
  - Action: Apply a filter (FT-07), then use the clear/reset control.
  - Expected: Active filters are displayed (e.g., highlighted controls or filter chips); clearing restores the full unfiltered customer list.
  - Bug Report:
    - Issue: Missing clear/reset control and no active-filter indicator
    - Actual: With the "VIP Collector" filter applied the DOM contains no clear/reset affordance at all — no "Clear"/"Reset" button (checked button text, `aria-label`, and the search/filter bar region: only "Add Customer" + the combobox exist), no filter chips, and no highlighted/"active" state (`[data-state="active"]` count = 0). The filter value is only readable as the combobox's own label, and resetting requires manually re-selecting "All Statuses" (search text must be deleted character-by-character; there is no clear icon).

## Content

- [X] CT-01: Default customer data matches the niche theme
  - Action: Inspect the default customers' records.
  - Expected: Records contain gallery-relevant content (collector names, art interests, exhibition invitations, purchase entries) — not placeholder/lorem text unrelated to the theme.
  - *Verified: collector names (Victoria Ashworth, Alexander Petrov, Isabella Romano), gallery tags (`contemporary-collector`, `private-client`, `asian-art-interest`, `first-time-buyer`), Interests fields, artwork interests with artists/prices, purchases ("Sunset Over Manhattan — Elena Voss · Purchased November 20, 2023 · $12,500"), and exhibition/visit activity ("Private viewing of new Elena Voss collection", "Attended winter gala"). No lorem/placeholder text.*

- [X] CT-02: Custom status labels reflect the gallery workflow
  - Action: View the available status options.
  - Expected: Statuses correspond to workflow stages for the niche (e.g., "Interested Collector", "Invited to Exhibition", "Artwork Purchased"), not generic ones like "Open/Closed" only.
  - *Verified: New Lead → Contacted → Interested → Negotiating → Purchased → VIP Collector → Inactive — a collector pipeline including gallery-specific stages (VIP Collector, Negotiating, Purchased), not generic Open/Closed.*

- [X] CT-03: Artwork items display relevant details
  - Action: Open a customer's attached artwork entry or the artwork attach picker.
  - Expected: Each artwork shows meaningful attributes (e.g., title, artist, price) appropriate to a gallery context.
  - *Verified: attach picker rows show title/artist/medium/price ("Urban Fragments — David Park · Photography — $3,200"); customer lists add year and availability ("Memories of Blue — Elena Voss · 2024 · Oil Painting · $15,800 · Available"); the Artworks page lists all 8 works with artist, medium, year, price and Sold state plus "8 artworks · Total value: $89,600" and All Mediums/All Status filters.*

- [X] CT-04: Report labels align with engagement and revenue intent
  - Action: Read the titles/labels of metrics on the summary report.
  - Expected: Labels explicitly reference engagement and revenue for the niche (e.g., "Invitations sent", "Artwork sales revenue"); no irrelevant or empty/unlabeled sections.
  - *Verified labels: "Total Revenue (All Time)", "Avg. Purchase Value", "Conversion Rate", "Active Relationships", "Monthly Revenue Trend", "Revenue by Customer Type" (VIP Collectors/Regular Buyers/New Collectors), "Artist Performance" (Elena Voss, Marcus Chen, Anna Kowalski, David Park), "Customer Engagement Over Time" (Emails/Calls/Gallery Visits), "Customer Acquisition", "Sales Conversion Funnel", "Customer Status Breakdown". Every chart carries a heading and axis/series labels — no empty or unlabeled blocks.*
