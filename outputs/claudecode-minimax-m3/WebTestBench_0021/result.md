I have completed all verification. Here is the full checklist report.

# Test Result

## Functionality

- [X] FT-01: Customers list loads default customer records
  - Action: Open the CRM admin app and click "Customers" in the left navigation.
  - Expected: A customer table/list renders with the pre-existing default customers, each row showing identifying details (name plus at least one contact or segment field), and no error/empty-state placeholder.

- [X] FT-02: Staff can create a new customer record
  - Action: Click "New Customer" (or "Add Customer"), fill in the required fields (name, plus email/phone as offered), and submit.
  - Expected: A success confirmation appears, the form closes, and the new customer appears in the customers list with the entered values.

- [X] FT-03: Staff can open a customer's detailed record
  - Action: Click any customer row/name in the list.
  - Expected: A customer detail view opens showing the full profile (contact details, status, interests, invitations, purchases) and any related items already attached.

- [ ] FT-04: Staff can update an existing customer and the change persists
  - Action: Open a default customer, click "Edit", change a visible field (e.g., email or note), save, then reload the page and reopen that customer.
  - Expected: The edited value is shown after reload (change persisted), with a confirmation message on save.
  - Bug Report:
    - Issue: Data Loss / Changes Not Persisted
    - Actual: Save produced a confirmation toast ("Customer updated — Changes have been saved successfully.") but nothing was written to any persistent store. After reloading `http://localhost:6021/customers/cust-1`, the Notes field still read "Prefers private viewings. Interested in large-scale installations." instead of the edited value "… QA-EDIT-2026 verified follow-up scheduled." The status change made in the same session (VIP Collector → Negotiating) also reverted to "VIP Collector", and the artwork added in FT-05 was gone ("Interested In" back to 2 instead of 3). Root cause confirmed via DOM/resource inspection: the app loads data from the static module `src/data/mockData.ts` with no API call and empty `localStorage`/`sessionStorage`, so all edits are transient React state. (Effectively FT-04, FT-06-list-sync, and FT-05 persistence all break at reload/navigation.)

- [X] FT-05: Staff can attach a related artwork/item to a customer
  - Action: On a customer detail view, open the related-items/artworks section and use "Add" to select an existing item and confirm.
  - Expected: The selected item appears in that customer's related-items list, and the item count on the customer (detail and/or list) increases accordingly.

- [ ] FT-06: Staff can apply a custom workflow status to a customer
  - Action: On a customer detail view, open the "Status" control, choose a status from the list, and confirm.
  - Expected: The customer displays the newly applied status, and the same status is reflected for that customer in the customers list.
  - Bug Report:
    - Issue: State Desynchronization Between Views (Status Not Reflected in List)
    - Actual: On `/customers/cust-1` the status was set to "Negotiating" (header badge and control showed "Negotiating", toast "Status updated — Customer status changed to Negotiating"), but after returning to the Customers list the row for Victoria Ashworth (cust-1) still read "VIP Collector". The list renders from the untouched seed data rather than the updated record, so the status change is never reflected in the customers list.

- [ ] FT-07: Staff can filter customers by attribute
  - Action: In the customers list, use the filter controls to filter by a customer attribute (e.g., status or interest) and apply.
  - Expected: The list narrows to only customers matching the chosen attribute, the active filter is indicated, and a result count is shown.
  - Bug Report:
    - Issue: Missing Result Count (and Missing Attribute Filter)
    - Actual: The status filter narrowed the list correctly (9 rows → 2 for "VIP Collector"; 8 → 1 for "Negotiating") and the active filter was indicated by the control label, but **no result count is rendered anywhere** — a full-text scan of `main` and `document.body` found no "Showing N results" / "N customers" text in either status-filter mode or search mode (search "high-value" → 2 rows, still no count). The Artworks page does render a count ("8 artworks · Total value: $89,600"), so the capability exists elsewhere but is absent here. Additionally, the only filter control is status; there is no interest/segment attribute filter.

- [ ] FT-08: Staff can filter customers by behavior
  - Action: Apply a behavior-based filter (e.g., has an artwork purchase, or purchase/value threshold, or engagement level) in the customers list.
  - Expected: Only customers meeting that behavioral condition are listed, and the result count matches the condition.
  - Bug Report:
    - Issue: Missing Feature (No Behavioral Filter)
    - Actual: The customers list exposes only two controls — a text input ("Search by name, email, or tag...") and a status dropdown. A DOM inventory of `main` found no control for purchase presence, spend/value threshold, or engagement level (no inputs, selects, or comboboxes other than the status one; text search of the page for "behavior/threshold/spend/segment" matched only unrelated copy such as "Purchases" and "asian-art-interest"). No behavior-based filter could be applied.

- [ ] FT-09: Staff can save and reuse a customer segment
  - Action: Apply a filter combination, use "Save segment"/"Save view", give it a name, confirm, then clear filters and re-apply the saved segment.
  - Expected: The segment appears in the segments list, and re-applying it reproduces exactly the same customer set as when it was saved.
  - Bug Report:
    - Issue: Missing Feature (No Saved Segments / Saved Views)
    - Actual: No "Save segment"/"Save view" control exists. The customers list toolbar contains only "Add Customer", the search box and the status dropdown; the row action menu offers only "View Details", "Send Email", "Log Interaction"; the Settings page contains only Gallery Information, Workflow Settings and Notifications. No segments list exists anywhere in the app, so a segment can neither be saved nor re-applied.

- [X] FT-10: Staff can view a summary performance report
  - Action: Navigate to "Reports" (or "Summary") and open the default summary report.
  - Expected: The report renders engagement metrics and revenue metrics (cards/tables/charts) populated with real values from the default data, not zeros/placeholders.

- [ ] FT-11: Staff can configure the summary report
  - Action: Change the report configuration (e.g., date range, metric selection, or grouping such as by status/niche category) and apply.
  - Expected: The displayed metrics update to match the new configuration, and the control shows the currently applied configuration.
  - Bug Report:
    - Issue: Missing Feature (No Report Configuration Controls)
    - Actual: The Reports page contains no configuration controls at all — a DOM inventory of `main` returned only three buttons (the "Revenue", "Engagement", "Sales Funnel" tabs) and no `input`, `select`, or `role=combobox` elements. There is no date-range picker, metric selector, or grouping control, so the report cannot be configured and no control displays an applied configuration.

## Constraint

- [X] CS-01: A customer cannot be saved with missing required information
  - Action: Open the new-customer form, leave a required field (e.g., name) empty, and submit.
  - Expected: Submission is blocked, a clear validation error identifies the missing field, and no customer record is created.

- [ ] CS-02: Duplicate customer records cannot be created
  - Action: Create a new customer using the email or name of an existing default customer and submit.
  - Expected: The save is rejected with a duplicate/already exists message, and the customers list count does not increase.
  - Bug Report:
    - Issue: Missing Validation (Duplicate Customer Accepted)
    - Actual: Submitting the new-customer form with First Name "Victoria", Last Name "Ashworth", Email "v.ashworth@email.com" — identical to the existing default customer cust-1 — was accepted with the success toast "Customer created — Victoria Ashworth has been added." No duplicate/already-exists warning was shown, and the customers list grew from 8 to 9 rows, with a new row "Victoria Ashworth / v.ashworth@email.com / New Lead" (id cust-1794056788909) rendered above the original. There is also no way to remove the duplicate afterwards: the row action menu offers only View Details / Send Email / Log Interaction.

- [X] CS-03: Only defined workflow statuses can be applied
  - Action: Attempt to apply a status value that is not among the available workflow statuses (e.g., via manual entry or by clearing the required status).
  - Expected: The invalid/empty status is rejected with an error, and the customer retains its previous valid status.

## Interaction

- [X] IX-01: Success feedback is shown after creating and updating a customer
  - Action: Create a customer, then separately edit an existing customer and save.
  - Expected: Each completed action triggers a visible success confirmation (e.g., toast/banner) that disappears automatically or can be dismissed.

- [X] IX-02: Filters apply and clear responsively without a page reload
  - Action: Apply a filter in the customers list, observe the results change, then click the active filter's remove/clear control.
  - Expected: The list updates in place to the filtered set, and on clearing, the full default customer list returns with no filter chip left active.

- [ ] IX-03: Navigation state and cross-section transitions are reflected
  - Action: Click between "Customers", a customer detail view, and "Reports" in the navigation.
  - Expected: The active navigation item is visibly highlighted, the correct view is displayed, and going back from detail to list preserves the previously applied filter state.
  - Bug Report:
    - Issue: Filter State Lost Across Navigation
    - Actual: Navigation highlighting works (the active link carries `aria-current="page"` and a distinct background — `rgb(39,44,53)` for "Customers" on the list vs `rgba(0,0,0,0)` for the others, and `aria-current="page"` on "Reports"), and each section renders the correct view. However, the applied filter is not preserved: after selecting "VIP Collector" on `/customers` and opening a customer detail, returning to Customers showed the filter reset to "All Statuses" and the full unfiltered list, with no indication that a filter had been applied. The same reset also discarded the status change made on the detail page (cust-1 displayed "VIP Collector" again).

## Content

- [X] CT-01: Customer records expose niche-relevant fields for the gallery example
  - Action: Open several default customers and review the fields shown on their detail views.
  - Expected: Fields cover collector interests, exhibition invitations, and artwork purchases (or equivalent niche workflow fields); no "Lorem ipsum", placeholder, or unrelated generic fields are present.

- [ ] CT-02: Attached artworks display correct and complete information
  - Action: Open the related-items/artworks section of a customer that has artworks attached.
  - Expected: Each item shows its artwork title and artist (plus price/value where stored) with a thumbnail/image that renders correctly — no broken images, empty labels, or duplicated names for different items.
  - Bug Report:
    - Issue: Missing Thumbnail / Incomplete Item Information
    - Actual: Text data is correct and distinct ("Abstract Emotions III — Marcus Chen · 2024 · Acrylic — $8,900", "Memories of Blue — Elena Voss · 2024 · Oil Painting — $15,800", "Urban Fragments — David Park · 2024 · Photography — $3,200"), but **no artwork image is rendered at all**: a DOM query for `img` inside the customer detail's "Interested Artworks"/"Purchase History" lists returned zero elements (only a letter-initial tile such as "VA"/"S"), and the whole Artworks page (`/artworks`) likewise contains zero `<img>` elements. Separately, Alexander Petrov (cust-8) shows "Purchases: 12" and "Total Spent: $420,000" while his "Purchase History" section reads "No purchases yet", and Robert Williams (cust-4) shows 5 purchases/$89,000 but lists only one purchase record.

- [ ] CT-03: Report content reflects engagement and revenue for the configured period
  - Action: Open the summary report, note the revenue and engagement values, then change the date range to a period containing fewer purchases and re-apply.
  - Expected: Metric labels are explicitly engagement- and revenue-oriented, values are numeric and currency-formatted where monetary, and the values change consistently with the selected period.
  - Bug Report:
    - Issue: Missing Feature (No Date Range / Period Control)
    - Actual: Labels and values are correct and engagement/revenue-oriented ("Total Revenue (All Time) $740,000", "Avg. Purchase Value $123,333", "Conversion Rate 38%", "Active Relationships 7", "Monthly Revenue Trend", "Revenue by Customer Type", "Artist Performance", "Customer Engagement Over Time" with Emails/Calls/Gallery Visits, "Customer Acquisition", "Sales Conversion Funnel", "Customer Status Breakdown"), and the charts are populated with real non-zero data (e.g. six monthly revenue bars of heights 91/146.25/104/188.5/234/133.25). However, the Reports page exposes no date-range, period, metric-selection or grouping control (only the three tabs), so the period cannot be changed and the "values change consistently with the selected period" requirement cannot be met.