I have now completed all checklist items. Here is the full test result:

# Test Result

## Functionality
- [X] FT-01: Customer list displays default customer records
  - Action: Open the CRM admin page and go to the Customers section.
  - Expected: The list shows pre-existing default customers with identifying details (e.g., name, contact info) — the list is not empty.
  - (Verified: 8 default customers — e.g., Victoria Ashworth, v.ashworth@email.com, +1 (555) 234-5678, VIP Collector — each with name, email, phone, status, tags, spend, purchases, last contact.)

- [X] FT-02: Staff can create a new customer record
  - Action: Click the "Add Customer" (or equivalent) button, fill in all required fields (e.g., name, email, phone), and save.
  - Expected: The new customer appears in the customer list.
  - (Verified: Created "Daniel Reyes" via the Add Customer dialog; he appeared at the top of the customer list immediately after saving. Note: the record is later lost on route navigation due to the same state-persistence bug documented under FT-03.)

- [ ] FT-03: Staff can update an existing customer's details
  - Action: Open a default customer's record, edit one field (e.g., phone number), and save.
  - Expected: The updated value is displayed and persists when the record is re-opened.
  - Bug Report:
    - Issue: State Persistence Failure — customer edits are not saved to the underlying data store
    - Actual: Editing Victoria Ashworth's phone from "+1 (555) 234-5678" to "+1 (555) 999-8888" and clicking "Save Changes" shows a success toast ("Customer updated — Changes have been saved successfully") and the detail page transiently displays the new phone, but navigating back to the customer list and re-opening the record shows the old value "+1 (555) 234-5678"; the re-opened Edit dialog is also pre-filled with the old value. localStorage is empty and the update is lost on any route change. The same defect causes newly created customers (e.g., "Daniel Reyes" from FT-02) to disappear from the list after navigating away and back.

- [X] FT-04: Staff can attach a related item (artwork) to a customer
  - Action: On a customer's detail page, use the "Attach Artwork" / related-items control to attach an existing default artwork.
  - Expected: The artwork appears in that customer's related items list.
  - (Verified: On Sophia Chen's detail page, "Add Artwork" opened the "Add Interested Artwork" picker; attaching "Urban Fragments" (David Park, $3,200) added it to her Interested Artworks list, and the "Interested In" count updated from 2 to 3, with toast "Artwork added".)

- [ ] FT-05: Staff can apply a custom workflow status to a customer
  - Action: On a customer record, change the workflow status to a custom status (e.g., "Invited to Exhibition") and save.
  - Expected: The customer shows the new custom status in both the detail view and the customer list.
  - Bug Report:
    - Issue: State Persistence Failure — status change is reflected in the detail view but not in the customer list
    - Actual: Changing Sophia Chen's status from "Interested" to "Negotiating" updates the badge on the detail page immediately (with toast "Status updated — Customer status changed to Negotiating"), but after returning to the Customers list, Sophia Chen still shows the old status "Interested" instead of "Negotiating" (same non-persistent state root cause as FT-03).

- [X] FT-06: Staff can filter/segment customers by attribute
  - Action: Apply a filter on the customer list (e.g., by status "Invited to Exhibition" or by an interest attribute).
  - Expected: Only customers matching the selected filter are displayed; non-matching customers are excluded.
  - (Verified: Filtering by status "VIP Collector" showed only Victoria Ashworth and Alexander Petrov; all 6 non-matching customers were excluded. Search-by-attribute also works, e.g., "Ashworth" returns only Victoria Ashworth.)

- [X] FT-07: Summary report displays engagement and revenue metrics
  - Action: Open the summary/reports section.
  - Expected: Performance metrics covering engagement (e.g., invitations, interactions) and revenue (e.g., purchase amounts) are displayed with values derived from default data.
  - (Verified: Reports section shows Total Revenue $740,000, Avg. Purchase Value $123,333, Conversion Rate 38%, Active Relationships 7; Engagement tab shows Customer Engagement Over Time with Emails/Calls/Gallery Visits; Sales Funnel shows conversion counts matching the 8 default customers.)

- [X] FT-08: Summary report is configurable
  - Action: Change a report configuration option (e.g., date range, metric, or report type selector) and apply it.
  - Expected: The report content updates to reflect the selected configuration (values/labels change accordingly).
  - (Verified: Switching the report type selector between Revenue / Engagement / Sales Funnel tabs updates the report content: Revenue shows Monthly Revenue Trend, Revenue by Customer Type (VIP Collectors/Regular Buyers/New Collectors) and Artist Performance; Engagement shows Emails/Calls/Gallery Visits and Customer Acquisition; Sales Funnel shows the New Leads→Purchased conversion funnel and Customer Status Breakdown — labels and values change with each selection.)

## Constraint
- [X] CS-01: Cannot save a customer with empty required fields
  - Action: Open the create-customer form, leave a required field (e.g., name) empty, and attempt to save.
  - Expected: Save is blocked; a validation error identifies the missing required field; no customer record is created.
  - (Verified: Clicking "Create Customer" with empty fields shows error toast "Missing required fields — Please fill in first name, last name, and email"; dialog stays open and no record is created.)

- [X] CS-02: Custom status must come from the defined workflow status list
  - Action: Open the status control on a customer record and attempt to set a status (including trying to type an arbitrary free-text status).
  - Expected: Only the predefined workflow statuses are selectable; an invalid/unknown status cannot be applied.
  - (Verified: The status control is a closed select (not a text input) offering only the 7 predefined workflow statuses — New Lead, Contacted, Interested, Negotiating, Purchased, VIP Collector, Inactive — on both the create form, edit page, and list filter; arbitrary free-text statuses cannot be entered or applied.)

- [X] CS-03: Filter with no matching customers returns an empty state
  - Action: Apply a filter combination that matches no default customers.
  - Expected: A clear "no results" empty state is shown; the app does not crash and does not display the full unfiltered list.
  - (Verified: Searching "zzznonexistent" with the "VIP Collector" status filter shows "No customers found" empty state; the app remains functional and the full list is not displayed.)

## Interaction
- [X] IX-01: Success feedback shown after customer creation
  - Action: Successfully create a new customer via the form.
  - Expected: A success toast/message appears and the customer list refreshes to include the new record.
  - (Verified: Toast "Customer created — Daniel Reyes has been added." appeared and the list refreshed with the new record at the top.)

- [X] IX-02: Status change reflects immediately in the UI
  - Action: Change a customer's workflow status from the detail page.
  - Expected: The status badge/value updates immediately without requiring a full page reload.
  - (Verified: Selecting "Negotiating" on Sophia Chen's detail page instantly updated the status badge and combobox value, with a "Status updated" toast — no page reload.)

- [X] IX-03: Customer list updates live as filter criteria change
  - Action: Type into the search box or change filter selections; then clear the filter.
  - Expected: The list updates instantly to match the criteria; clearing the filter restores the full default list.
  - (Verified: Typing "Ashworth" instantly narrowed the list to one result; typing "zzznonexistent" showed the empty state; clearing the search and resetting the status filter to "All Statuses" restored all 8 default customers.)

- [X] IX-04: Clicking a customer opens their detail view
  - Action: Click a customer row in the list.
  - Expected: The customer's detail page opens, showing that customer's records, related items, and workflow status.
  - (Verified: Clicking Victoria Ashworth opened /customers/cust-1 with her stats (Total Spent $156,000, 8 Purchases), Interested Artworks, Purchase History, and workflow status "VIP Collector".)

## Content
- [X] CT-01: Workflow statuses and labels match the gallery niche
  - Action: Review the available custom statuses and workflow terminology across the app.
  - Expected: They reflect the gallery workflow (e.g., collector interests, exhibition invitations, artwork purchases), not only generic CRM terms.
  - (Verified: Statuses include "VIP Collector" and "Purchased"; app-wide terminology is gallery-specific: "Manage your collector relationships", "Interested Artworks", "Purchase History", interaction types "visit"/"exhibition" (e.g., "Private viewing of new Elena Voss collection", "Attended winter gala"), Settings offers "Exhibition invitations — auto-send exhibition invites based on customer interests", Engagement reports track "Gallery Visits", and customer interests include Contemporary/Abstract/Sculpture.)

- [X] CT-02: Attached artwork details are relevant and complete
  - Action: Open a customer's related artworks list.
  - Expected: Each item shows artwork-relevant details (e.g., title, artist, thumbnail or price) consistent with the gallery theme.
  - (Verified: Each attached artwork shows title, artist, year, medium, price, and availability — e.g., "Abstract Emotions III — Marcus Chen · 2024 · Acrylic — $8,900 — Available"; purchase history entries show title, artist, purchase date, and amount.)

- [X] CT-03: Summary report content reflects the niche's engagement and revenue patterns
  - Action: Review the metrics, labels, and figures in the summary report.
  - Expected: Metrics are engagement and revenue measures relevant to the niche (e.g., exhibition invitations, artwork purchases, sales revenue), not unrelated placeholders.
  - (Verified: Metrics include artwork sales revenue (Total Revenue, Avg. Purchase Value, Monthly Revenue Trend), Artist Performance (Elena Voss, Marcus Chen, etc.), Revenue by Customer Type (VIP Collectors/Regular Buyers/New Collectors), engagement interactions (Emails, Calls, Gallery Visits), Customer Acquisition, and a collector Sales Conversion Funnel (New Leads → Purchased) — all gallery-niche measures, no unrelated placeholders.)

- [X] CT-04: All images load and are theme-relevant
  - Action: Check all images in the app (artwork thumbnails, avatars, report graphics).
  - Expected: Every image renders (no broken-image icons) and is directly relevant to the gallery/artwork theme.
  - (Verified via DOM inspection on Dashboard, Customers, Artworks, Reports, and Settings pages: the app contains zero <img> elements with external src — all icons, avatars (initials), and report charts are inline SVGs that render correctly with no broken-image states; artwork cards use initial-letter placeholders with status badges, and all report graphics visualize gallery revenue/engagement data.)

---

**Summary**: 15 of 17 checks passed. Two failures (FT-03, FT-05) share a single root cause: **customer data mutations (edits and status changes, and also newly created records) are only held in transient component state and are not persisted to the shared data store — they are silently lost whenever the route changes**, despite success toasts confirming the save.