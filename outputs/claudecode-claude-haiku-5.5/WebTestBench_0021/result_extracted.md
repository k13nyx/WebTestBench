# Test Result

## Functionality

- [ ] FT-01: Staff can create a new customer record with details and collector interests.
  - Action: Click "New Customer", enter Name "Elena Marsh", Email "elena.marsh@example.com", select Interests "Contemporary Painting" and "Photography", then click "Save".
  - Expected: The record is saved and appears in the customer list with the entered name, email, and both interests.
  - Bug Report:
    - Issue: Missing Form Field (Interests not available)
    - Actual: The "Add New Customer" dialog contains only First Name, Last Name, Email, Phone, Status, and Notes. There is no Interests control. The record "Elena Marsh" with email elena.marsh@example.com was created, but with no interests. When I navigated back to Customers, the record was no longer in the list (only 8 default customers were shown).
- [X] FT-02: Staff can update an existing customer's details.
  - Action: Open a default customer, change the "Phone" field to "+1 555 0142", click "Save", then reopen the record.
  - Expected: The new phone number persists after reopening.
- [ ] FT-03: Staff can attach an artwork to a customer.
  - Action: Open a default customer, go to the "Related Items" tab, click "Attach Artwork", select an available default artwork, then click "Attach".
  - Expected: The artwork appears under "Related Items" with its title, artist, and status.
  - Bug Report:
    - Issue: Expected Location and Flow Mismatch (no "Related Items" tab, no "Attach" step)
    - Actual: There is no "Related Items" tab (tabs are "Artworks", "Activity", "Notes & Tags") and no "Attach Artwork" button ("Add Artwork" is used). Clicking an artwork in the "Add Interested Artwork" dialog attached it immediately with the toast "Artwork added". "Urban Fragments" (David Park, $3,200, status "Available") appears under "Interested Artworks". The attachment itself worked, but the Expected location and the Attach step do not match.
- [ ] FT-04: Staff can apply a custom workflow status to a customer.
  - Action: Open a default customer, open the "Status" dropdown, select "Viewing Scheduled", then click "Save".
  - Expected: The status badge shows "Viewing Scheduled" on the record and in the customer list.
  - Bug Report:
    - Issue: Missing Workflow Status (Viewing Scheduled)
    - Actual: The Status dropdown options are "New Lead", "Contacted", "Interested", "Negotiating", "Purchased", "VIP Collector", "Inactive". "Viewing Scheduled" is not offered, so it could not be selected.
- [ ] FT-05: Staff can filter customers by attributes and by behavior.
  - Action: In the customer list, set "Collector Interest" to "Sculpture" and "Last Purchase" to "Within 12 months", then click "Apply".
  - Expected: Only customers matching both criteria are listed, and the result count updates to match.
  - Bug Report:
    - Issue: Missing Filter Controls
    - Actual: The Customers page has only a search textbox ("Search by name, email, or tag...") and an "All Statuses" dropdown. There is no "Collector Interest" filter, no "Last Purchase" filter, no "Apply" button, and no result count.
- [ ] FT-06: Staff can generate a configurable summary report.
  - Action: Open "Reports", select the metrics "Engagement Rate", "Invitation Response Rate", and "Artwork Sales Revenue", set the date range to the last 12 months, then click "Generate Report".
  - Expected: The report shows only the selected metrics with values for the chosen period.
  - Bug Report:
    - Issue: Missing Configuration Controls (no metric selector, date range, or Generate Report)
    - Actual: The Reports page shows fixed content: four KPI cards (Total Revenue (All Time) $740,000, Avg. Purchase Value, Conversion Rate, Active Relationships), tabs "Revenue", "Engagement", and "Sales Funnel", and fixed charts. No metric selection, date range inputs, or "Generate Report" button exist.
- [ ] FT-07: Staff can log an exhibition invitation for a customer.
  - Action: Open a default customer, click "Log Invitation", select a default exhibition from the list, then click "Save".
  - Expected: The invitation appears in the customer's activity timeline with the exhibition name and date.
  - Bug Report:
    - Issue: Missing Action (Log Invitation)
    - Actual: The customer detail page has only "Edit" and "Add Artwork" buttons plus the tabs "Artworks", "Activity", and "Notes & Tags". There is no "Log Invitation" button. The Activity tab is read-only and lists existing entries ("visit", "exhibition").
- [ ] FT-08: Staff can record an artwork purchase for a customer.
  - Action: Open a default customer, click "Record Purchase", select an available artwork and a price, then click "Save".
  - Expected: The purchase appears in the customer's purchase history, and the artwork status changes to "Sold".
  - Bug Report:
    - Issue: Missing Action (Record Purchase)
    - Actual: There is no "Record Purchase" button on the customer detail page. "Purchase History" is displayed as a read-only list.

## Constraint

- [ ] CS-01: A customer cannot be saved without required fields.
  - Action: Open "New Customer", leave "Name" empty, enter a valid email, then click "Save".
  - Expected: The message "Name is required" appears next to the field, and no record is created.
  - Bug Report:
    - Issue: Incorrect Validation Message (no inline error)
    - Actual: The form has separate "First Name *" and "Last Name *" fields, not "Name". With First Name empty, the submit produced a toast, "Missing required fields / Please fill in first name, last name, and email.". The text "Name is required" never appeared beside a field. No record was created.
- [ ] CS-02: A customer cannot be saved with a duplicate or invalid email.
  - Action: Enter the email of an existing default customer in "New Customer" and click "Save". Then enter "collector@" as the email and click "Save".
  - Expected: "A customer with this email already exists" appears for the duplicate. "Enter a valid email address" appears for the invalid format. No record is saved in either case.
  - Bug Report:
    - Issue: Missing Email Validation (duplicate and invalid format both saved)
    - Actual: Using the existing email v.ashworth@email.com with First/Last Name "Dup Test" produced the toast "Customer created – Dup Test has been added." Using "collector@" with name "Bad Email" also produced "Customer created – Bad Email has been added." Neither "A customer with this email already exists" nor "Enter a valid email address" appeared, and both records were saved. Both records are test artifacts left in the data.
- [ ] CS-03: The same artwork cannot be attached to the same customer twice.
  - Action: Open a default customer with an attached artwork, click "Attach Artwork", and select that same artwork.
  - Expected: The message "Artwork already attached" appears, and the artwork is not listed twice.
  - Bug Report:
    - Issue: Missing Duplicate Feedback
    - Actual: The "Add Interested Artwork" picker excludes already-attached artworks, so "Abstract Emotions III" and "Memories of Blue" were not offered. The artwork was not listed twice, but no "Artwork already attached" message appeared. The picker offered only "Digital Dreams".
- [ ] CS-04: A sold artwork cannot be purchased again.
  - Action: Open "Record Purchase" for a customer and select an artwork whose status is "Sold".
  - Expected: The artwork is disabled or the message "Artwork already sold" appears, and no second purchase is recorded.
  - Bug Report:
    - Issue: Unverifiable Flow (no Record Purchase feature)
    - Actual: No "Record Purchase" entry point exists on the customer record, so a sold artwork could not be selected. No "Artwork already sold" message or disabled state could be observed.
- [ ] CS-05: A report cannot be generated with an end date before the start date.
  - Action: In "Reports", set the start date to "2026-06-01" and the end date to "2026-01-01", then click "Generate Report".
  - Expected: The message "End date must be after start date" appears, and the report is not generated.
  - Bug Report:
    - Issue: Missing Date Range Inputs
    - Actual: The Reports page has no start date or end date inputs and no "Generate Report" button, so the invalid range could not be entered and the message could not be triggered.

## Interaction

- [ ] IX-01: A success toast confirms each save.
  - Action: Edit a default customer's "Notes" field and click "Save".
  - Expected: A toast reading "Customer saved" appears at the top of the screen and disappears within about 5 seconds.
  - Bug Report:
    - Issue: Incorrect Toast Text and Position
    - Actual: The toast reads "Customer updated / Changes have been saved successfully." instead of "Customer saved". It sits at y≈610px in a 720px-high viewport (bottom area, not the top). It cleared within 6 seconds.
- [ ] IX-02: Filter results update without a page reload.
  - Action: Apply the filter "Collector Interest: Photography", then click "Clear All".
  - Expected: The list and result count update immediately after each action, and the page does not reload. After clearing, all customers are shown again.
  - Bug Report:
    - Issue: Missing Filter Controls (no "Collector Interest" filter, no "Clear All")
    - Actual: The customer list has no filter panel, no "Apply" or "Clear All" buttons, and no result count. Only the search box and status dropdown exist.
- [ ] IX-03: Leaving an edited record with unsaved changes prompts a warning.
  - Action: Open a default customer, change the "Email" field, then click "Back to Customers" without saving.
  - Expected: A dialog reading "You have unsaved changes" appears with "Leave" and "Stay" buttons. "Stay" keeps the edits on screen, and "Leave" discards them.
  - Bug Report:
    - Issue: Missing Unsaved-Changes Guard
    - Actual: I changed the Email in the Edit dialog to "v.ashworth@changed.com", closed the dialog, and clicked "Back to Customers". The page navigated straight to /customers. No "You have unsaved changes" dialog, "Leave" button, or "Stay" button appeared.

## Content

- [ ] CT-01: Collector interest tags relate to art.
  - Action: Open the "Interests" filter and review the options. Then open any three default customers and review their interest tags.
  - Expected: All interests are art categories (for example, "Contemporary Painting", "Sculpture", "Photography", "Works on Paper"). No unrelated terms appear.
  - Bug Report:
    - Issue: Non-Art and Generic Tags / Missing Interests Filter
    - Actual: No "Interests" filter exists. The tags on the customer cards are mixed: "high-value", "private-client", "bulk-buyer", "corporate", "investor", "returning-client", "designer", "partnership-potential", "vip", "referral", "first-time-buyer", and "international". Several are generic CRM or segment terms, not art categories. The only art-related tags are "contemporary-collector" and "asian-art-interest".
- [ ] CT-02: Report totals match the underlying default data.
  - Action: Generate "Artwork Sales Revenue" for the last 12 months. Then open the purchase records for the same period.
  - Expected: The report total equals the sum of purchase prices for that period, and the currency format matches the rest of the application.
  - Bug Report:
    - Issue: Unverifiable Report (no period-based generation, no purchase records view)
    - Actual: The Reports page shows only "Total Revenue (All Time)" of $740,000. "Artwork Sales Revenue" cannot be generated for the last 12 months, and no purchase-records view exists to compare against. Currency format is "$" with "k" abbreviations on the dashboard.
- [ ] CT-03: Workflow statuses and exhibition names are gallery-specific.
  - Action: Open the "Status" dropdown on a customer record and open the "Log Invitation" exhibition list.
  - Expected: Statuses reflect gallery workflows (for example, "Invited", "Viewing Scheduled", "Offer Made", "Purchased"). Exhibition names are art exhibitions with valid dates. No generic CRM terms such as "Lead" or "Deal" appear.
  - Bug Report:
    - Issue: Generic CRM Terminology and Missing Gallery Workflow Statuses
    - Actual: The Status options are "New Lead", "Contacted", "Interested", "Negotiating", "Purchased", "VIP Collector", and "Inactive". "New Lead" is a generic CRM term, and "Invited", "Viewing Scheduled", and "Offer Made" are absent. The "Log Invitation" exhibition list could not be opened because no such control exists.
