# Test Result

## Functionality

- [X] FT-01: Staff can create a new customer record
  - Action: Click "Add Customer" / "New Collector", fill Name, Email, and Collector Interests, then click "Save".
  - Expected: Customer appears in the customer list with the exact name and email entered, and a confirmation is shown.

- [ ] FT-02: Staff can update an existing customer record
  - Action: Open an existing default customer, edit the Name and Collector Interests fields, click "Save", then reload the page.
  - Expected: The detail view and list show the updated values after reload; no other fields are altered.
  - Bug Report:
    - Issue: Data Not Persisted After Reload + Missing Editable Field
    - Actual: Editing cust-1 (Victoria Ashworth) via "Edit" → changed First Name to "Viktoria", Last Name to "Ashworth-Blake" and Notes to "Interests: Contemporary abstracts…". Immediately after "Save Changes" the detail heading updated to "Viktoria Ashworth-Blake" and a "Customer updated" toast appeared (email/phone unchanged). After navigating to http://localhost:6021/customers/cust-1 (full reload) the heading reverted to "Victoria Ashworth" and Notes reverted to "Prefers private viewings. Interested in large-scale installations." The "Collector Interests" component of the action could not be executed at all: no editable interests field exists anywhere — the Edit dialog contains only First Name/Last Name/Email/Phone/Notes, and the detail view's "Notes & Tags" tab shows Interests (Contemporary, Abstract, Sculpture) as read-only chips with no add/remove control.

- [ ] FT-03: Staff can attach a related item (artwork) to a customer
  - Action: Open a customer, go to the "Artworks" / "Related Items" section, attach an existing default artwork, and save.
  - Expected: The artwork title appears in that customer's related-items list and is visible after reload.
  - Bug Report:
    - Issue: Attachment Not Persisted After Reload
    - Actual: On cust-1, "Interested Artworks" → "Add Artwork" → selecting "Urban Fragments" (David Park, $3,200) added it to the list (3 items) and showed the toast "Artwork added — The artwork has been added to interested list." After a full reload of /customers/cust-1 the list was back to 2 items (Abstract Emotions III, Memories of Blue) and the "Interested In" stat returned to "2"; "Urban Fragments" was gone.

- [ ] FT-04: Staff can log an exhibition invitation for a customer
  - Action: Open a customer's workflow/activity timeline, add an "Exhibition Invitation" entry for a default exhibition, and save.
  - Expected: The invitation entry (exhibition name + date) appears in that customer's timeline and in their workflow history.
  - Bug Report:
    - Issue: Missing Feature / No Input Control
    - Actual: The "Activity" tab of cust-1 renders only a read-only "Interaction History" list (two entries: "visit — January 10, 2024 — Private viewing of new Elena Voss collection" and "exhibition — December 1, 2023 — Attended winter gala"). There is no "Add", "Log Interaction", or "Exhibition Invitation" button or form anywhere on the tab, so no invitation could be logged. No exhibition/invitation workflow control exists on the Customers, Artworks, or Settings pages either.

- [ ] FT-05: Staff can record an artwork purchase for a customer
  - Action: Open a customer, record a purchase of an attached default artwork with a positive amount, and save.
  - Expected: The purchase appears in the customer's history with artwork title and amount, and the customer's total revenue figure increases by that amount.
  - Bug Report:
    - Issue: Missing Feature / No Input Control
    - Actual: The "Purchase History" section of the Artworks tab is read-only. For cust-3 (Sophia Chen) it shows only the text "No purchases yet"; for cust-1 it lists two historical purchases ("Sunset Over Manhattan $12,500", "Bronze Horizon $28,000"). There is no "Record Purchase" / "Add Purchase" button or amount input in either case, so no purchase could be recorded and Total Spent could not be incremented.

- [ ] FT-06: Staff can apply a custom workflow status to a customer
  - Action: Open a customer and assign a custom status (e.g., "Invited", "Negotiating", "Closed – Sold") from the status control, then save.
  - Expected: The chosen status is displayed on the customer's detail view and in the customer list row.
  - Bug Report:
    - Issue: Detail/List State Desync — Status Change Not Reflected in List Row
    - Actual: On cust-1, selecting "Negotiating" from the status control updated the detail badge to "Negotiating" and showed the toast "Status updated — Customer status changed to Negotiating". Clicking "Back to Customers" (client-side navigation, no reload) showed the cust-1 row still displaying "VIP Collector". The list row never reflected the new status. (Also, the configured status list does not contain the workflow examples "Invited" or "Closed – Sold"; only New Lead, Contacted, Interested, Negotiating, Purchased, VIP Collector, Inactive are offered, and a full reload reverts the status to the original value.)

- [X] FT-07: Staff can filter customers by attributes
  - Action: Apply a filter on an attribute (e.g., status = a specific value, or interest = a specific art category) and apply it.
  - Expected: The customer list shows only records matching that attribute, and the displayed count equals the number of matching rows.

- [ ] FT-08: Staff can segment customers by behavior
  - Action: Apply a behavior-based filter (e.g., "made a purchase", "invited but no purchase", or engagement within a date range).
  - Expected: The list contains only customers satisfying that behavior; customers that clearly do not satisfy it are absent.
  - Bug Report:
    - Issue: Missing Feature / No Segmentation Control
    - Actual: The Customers page offers only two controls: a text search box ("Search by name, email, or tag...") and a status dropdown ("All Statuses" + the 7 defined statuses). There is no behavior-based filter of any kind — no "made a purchase", "invited but no purchase", or engagement/date-range segment control. The Settings page contains no segmentation configuration either (only Gallery Information, three Workflow toggles, and three Notification toggles). The action could not be executed.

- [X] FT-09: Staff can view a summary report of engagement and revenue
  - Action: Open the Reports / Summary section with default settings.
  - Expected: The report displays at least one engagement metric (e.g., invitations sent, responses) and at least one revenue metric (e.g., total sales), each with a non-empty numeric value.

- [ ] FT-10: Staff can configure the summary report
  - Action: Change a report configuration option (e.g., date range or displayed metric) and apply it.
  - Expected: The report values and/or chart update to reflect the new configuration without a page reload.
  - Bug Report:
    - Issue: Missing Feature / No Report Configuration Controls
    - Actual: The Reports page has no configuration controls: a DOM query returned 0 `<select>` elements, 0 `[role=combobox]`, 0 `input[type=date]`, and 0 sliders. The only interactive controls are three preset view tabs (Revenue / Engagement / Sales Funnel). The four KPI values ("Total Revenue (All Time) $740,000", "Avg. Purchase Value $123,333", "Conversion Rate 38%", "Active Relationships 7") are identical and static across all three tabs — only the chart area changes. No date range can be selected and no metric can be added/removed.

## Constraint

- [ ] CS-01: Customer cannot be saved with empty required fields
  - Action: Open the new-customer form, leave Name and Email blank, and click "Save".
  - Expected: Save is blocked; an inline error message appears on each empty required field and no customer is added to the list.
  - Bug Report:
    - Issue: Missing Inline Per-Field Validation Errors
    - Actual: Clicking "Create Customer" with First Name, Last Name and Email blank was blocked (the dialog stayed open and the list remained at 8 customers), but the only feedback was a single top-right toast: "Missing required fields — Please fill in first name, last name, and email." No error text was rendered beneath or beside the "First Name *", "Last Name *" or "Email *" inputs — the dialog snapshot shows the three fields unchanged with no inline messages.

- [ ] CS-02: Duplicate customer email is rejected
  - Action: Create a customer using the email address of an existing default customer and click "Save".
  - Expected: Save is blocked with an error stating the email is already in use; no duplicate record is created.
  - Bug Report:
    - Issue: Missing Duplicate-Email Validation
    - Actual: Creating "Victoria Dupont" with the email `v.ashworth@email.com` (already used by default customer Victoria Ashworth, cust-1) was accepted. Toast shown: "Customer created — Victoria Dupont has been added." The new record `/customers/cust-1794078551887` was appended to the list, which now contains two different customers sharing `v.ashworth@email.com`. No duplicate-email error was displayed.

- [X] CS-03: The same artwork cannot be attached to one customer twice
  - Action: On a customer already linked to a default artwork, attempt to attach that same artwork again.
  - Expected: The duplicate is prevented (option unavailable or error shown); the related-items list still contains that artwork exactly once.

- [X] CS-04: Only defined custom statuses can be applied
  - Action: Attempt to assign a status value that is not in the configured status list (e.g., by clearing/overriding the picker).
  - Expected: The application rejects it — no arbitrary or blank status is persisted; the customer retains its previous valid status.
  - Bug Report:
    - Issue: (PASSED — no defect; recording evidence) The status control is a closed Radix listbox that is not text-editable: attempting to fill the string "Invited-ZZZ" returned "Error: Element is not an `<input>`, `<textarea>` or [contenteditable] element" for `<div role="listbox">`. Typing "I" + Enter could only commit a value from the 7 defined options ("Inactive"), and the toast confirmed "Status updated — Customer status changed to Inactive". No arbitrary or blank status was persisted.

- [X] CS-05: Filters that match nothing show an empty state, not stale data
  - Action: Apply a filter combination that no default customer satisfies.
  - Expected: The list is empty and shows an explicit "No customers match" empty-state message; no previously loaded rows remain.

## Interaction

- [ ] IX-01: Selecting a customer opens its detail view
  - Action: Click a customer row in the customer list.
  - Expected: That customer's detail view opens showing its full record (contact info, interests, related items, status, history).
  - Bug Report:
    - Issue: Unresponsive Row — Row Body Is Not Clickable
    - Actual: Clicking the Victoria Ashworth row card twice (first on the name/status/tags block `VAVictoria AshworthVIP Collector`, then on the stats block `Total Spent $156,000 / Purchases 8 / Last Contact Jan 10`) produced no response — the URL stayed at /customers and no detail view opened. Only the customer-name link (`<a href="/customers/cust-1">Victoria Ashworth</a>`) navigates; clicking it does open the full detail view with contact info, Interests, Interested Artworks, status and Purchase History. The rest of the row surface (avatar, email/phone, tags, metrics) is dead.

- [X] IX-02: Success feedback appears after a customer is saved
  - Action: Create or update a customer and save it.
  - Expected: A success confirmation message/toast appears (e.g., "Customer saved") and the form closes or returns to the list.

- [ ] IX-03: Active filters are shown as removable chips
  - Action: Apply two different filters, then click the "×" / "Clear" control on one chip.
  - Expected: The chip disappears, the list updates to reflect the remaining filter, and a "Clear all" action restores the full list.
  - Bug Report:
    - Issue: Missing Filter-Chip UI
    - Actual: With two filters active simultaneously — status dropdown = "VIP Collector" and search box = "Victoria" — the list correctly narrowed to 1 row (Victoria Ashworth), but no chip row rendered anywhere on the page. The only filter UI remains the search textbox (`Victoria`) and the status combobox (`VIP Collector`); there is no "×" remove control, no individual chip, and no "Clear all" action. Changing a filter can only be done by editing those two inputs directly.

## Content

- [ ] CT-01: Interface uses the niche's terminology (gallery example)
  - Action: Review labels, headers, and field names across the customer list, detail view, and reports.
  - Expected: Terminology matches the gallery niche ("Collector"/"Customer", "Artwork", "Exhibition Invitation", "Purchase", "Interests"); no generic unrelated template terms (e.g., "Leads", "Deals", "Units Sold") are used.
  - Bug Report:
    - Issue: Generic Template Terminology Present
    - Actual: The explicitly-forbidden generic CRM terms "Deals" and "Leads" are used in the gallery UI: the Dashboard KPI card reads "Active Deals — 2 — In negotiation"; "New Lead" is one of the seven customer statuses (shown on the customer list rows for Michael Foster, in the detail status control, and in the status filter); the Reports → Sales Funnel chart uses the stage label "New Leads"; and Settings → Workflow Settings shows "Auto-assign new leads — Automatically assign new leads to available staff". Gallery-correct terms are used elsewhere ("Artworks", "Interested Artworks", "Purchase History", "Interests", "VIP Collector"), and "Exhibition Invitation" appears only as a Settings toggle, not as a recordable workflow item.

- [X] CT-02: Report figures are properly labeled and contain no placeholder or broken data
  - Action: Inspect all metrics, chart labels, and images/icons on the summary report.
  - Expected: Every metric shows a descriptive label, numeric value with correct unit (currency symbol or count) and its reporting period; no "Lorem ipsum", "N/A", "undefined", or broken-image icons appear anywhere.
