# Test Checklist

## Functionality
- [ ] FT-01: Staff can create a new customer record with details and collector interests.
  - Action: Click "New Customer", enter Name "Elena Marsh", Email "elena.marsh@example.com", select Interests "Contemporary Painting" and "Photography", then click "Save".
  - Expected: The record is saved and appears in the customer list with the entered name, email, and both interests.
- [ ] FT-02: Staff can update an existing customer's details.
  - Action: Open a default customer, change the "Phone" field to "+1 555 0142", click "Save", then reopen the record.
  - Expected: The new phone number persists after reopening.
- [ ] FT-03: Staff can attach an artwork to a customer.
  - Action: Open a default customer, go to the "Related Items" tab, click "Attach Artwork", select an available default artwork, then click "Attach".
  - Expected: The artwork appears under "Related Items" with its title, artist, and status.
- [ ] FT-04: Staff can apply a custom workflow status to a customer.
  - Action: Open a default customer, open the "Status" dropdown, select "Viewing Scheduled", then click "Save".
  - Expected: The status badge shows "Viewing Scheduled" on the record and in the customer list.
- [ ] FT-05: Staff can filter customers by attributes and by behavior.
  - Action: In the customer list, set "Collector Interest" to "Sculpture" and "Last Purchase" to "Within 12 months", then click "Apply".
  - Expected: Only customers matching both criteria are listed, and the result count updates to match.
- [ ] FT-06: Staff can generate a configurable summary report.
  - Action: Open "Reports", select the metrics "Engagement Rate", "Invitation Response Rate", and "Artwork Sales Revenue", set the date range to the last 12 months, then click "Generate Report".
  - Expected: The report shows only the selected metrics with values for the chosen period.
- [ ] FT-07: Staff can log an exhibition invitation for a customer.
  - Action: Open a default customer, click "Log Invitation", select a default exhibition from the list, then click "Save".
  - Expected: The invitation appears in the customer's activity timeline with the exhibition name and date.
- [ ] FT-08: Staff can record an artwork purchase for a customer.
  - Action: Open a default customer, click "Record Purchase", select an available artwork and a price, then click "Save".
  - Expected: The purchase appears in the customer's purchase history, and the artwork status changes to "Sold".

## Constraint
- [ ] CS-01: A customer cannot be saved without required fields.
  - Action: Open "New Customer", leave "Name" empty, enter a valid email, then click "Save".
  - Expected: The message "Name is required" appears next to the field, and no record is created.
- [ ] CS-02: A customer cannot be saved with a duplicate or invalid email.
  - Action: Enter the email of an existing default customer in "New Customer" and click "Save". Then enter "collector@" as the email and click "Save".
  - Expected: "A customer with this email already exists" appears for the duplicate. "Enter a valid email address" appears for the invalid format. No record is saved in either case.
- [ ] CS-03: The same artwork cannot be attached to the same customer twice.
  - Action: Open a default customer with an attached artwork, click "Attach Artwork", and select that same artwork.
  - Expected: The message "Artwork already attached" appears, and the artwork is not listed twice.
- [ ] CS-04: A sold artwork cannot be purchased again.
  - Action: Open "Record Purchase" for a customer and select an artwork whose status is "Sold".
  - Expected: The artwork is disabled or the message "Artwork already sold" appears, and no second purchase is recorded.
- [ ] CS-05: A report cannot be generated with an end date before the start date.
  - Action: In "Reports", set the start date to "2026-06-01" and the end date to "2026-01-01", then click "Generate Report".
  - Expected: The message "End date must be after start date" appears, and the report is not generated.

## Interaction
- [ ] IX-01: A success toast confirms each save.
  - Action: Edit a default customer's "Notes" field and click "Save".
  - Expected: A toast reading "Customer saved" appears at the top of the screen and disappears within about 5 seconds.
- [ ] IX-02: Filter results update without a page reload.
  - Action: Apply the filter "Collector Interest: Photography", then click "Clear All".
  - Expected: The list and result count update immediately after each action, and the page does not reload. After clearing, all customers are shown again.
- [ ] IX-03: Leaving an edited record with unsaved changes prompts a warning.
  - Action: Open a default customer, change the "Email" field, then click "Back to Customers" without saving.
  - Expected: A dialog reading "You have unsaved changes" appears with "Leave" and "Stay" buttons. "Stay" keeps the edits on screen, and "Leave" discards them.

## Content
- [ ] CT-01: Collector interest tags relate to art.
  - Action: Open the "Interests" filter and review the options. Then open any three default customers and review their interest tags.
  - Expected: All interests are art categories (for example, "Contemporary Painting", "Sculpture", "Photography", "Works on Paper"). No unrelated terms appear.
- [ ] CT-02: Report totals match the underlying default data.
  - Action: Generate "Artwork Sales Revenue" for the last 12 months. Then open the purchase records for the same period.
  - Expected: The report total equals the sum of purchase prices for that period, and the currency format matches the rest of the application.
- [ ] CT-03: Workflow statuses and exhibition names are gallery-specific.
  - Action: Open the "Status" dropdown on a customer record and open the "Log Invitation" exhibition list.
  - Expected: Statuses reflect gallery workflows (for example, "Invited", "Viewing Scheduled", "Offer Made", "Purchased"). Exhibition names are art exhibitions with valid dates. No generic CRM terms such as "Lead" or "Deal" appear.