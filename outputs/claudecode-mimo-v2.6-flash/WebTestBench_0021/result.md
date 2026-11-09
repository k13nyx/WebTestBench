All test items are now executed. I verified: customer CRUD, artwork attachment, status changes, filters, report views, validation/duplicate handling, and content consistency against reference data.

# Test Result

## Functionality
- [ ] FT-01: Create a new customer record
  - Action: Open the customer creation form, enter a name, email, and niche-relevant attributes (e.g., collector interests), then save.
  - Expected: The new customer appears in the customer list with all entered data visible.
  - Bug Report:
    - Issue: Broken Customer Record Link / Entered Data Not Visible
    - Actual: "Clara Nightingale" was created and briefly appeared in the list with name/email/phone/status, but the entered niche attribute (Notes: "Collector interests: Impressionist paintings...") is not visible in the list, clicking the new record's link shows "Customer not found", and the record vanishes completely after a page reload — the entered data cannot be viewed anywhere.

- [ ] FT-02: Update an existing customer's details
  - Action: Open an existing customer record, change a field (e.g., email or interest category), and save.
  - Expected: The updated value is displayed in the record and persists after reloading the page.
  - Bug Report:
    - Issue: Updated Data Not Persisted After Reload
    - Actual: Changing Victoria Ashworth's email to v.ashworth@newdomain.com showed a "Customer updated" toast and the record displayed the new value, but after reloading the page the record reverted to the original v.ashworth@email.com (no storage/localStorage persistence at all).

- [X] FT-03: Attach a related item (artwork) to a customer
  - Action: Open a customer record, add an artwork from the default items list as a related item, and save.
  - Expected: The artwork is listed under the customer's related items.

- [X] FT-04: Apply a custom workflow status to a customer
  - Action: Select a customer and apply a workflow status such as "Invitation Sent" or "Purchase In Progress".
  - Expected: The selected status is shown on the customer record.

- [X] FT-05: Filter customers by attribute or behavior
  - Action: Apply a filter (e.g., by status, interest, or purchase behavior) from the filter controls.
  - Expected: Only customers matching the filter criteria are listed.

- [ ] FT-06: Create a custom segment of customers
  - Action: Define a segment combining criteria (e.g., collectors with a purchase in the last period) and apply it.
  - Expected: The customer list updates to show only customers in that segment, and the segment can be re-applied later.
  - Bug Report:
    - Issue: Missing Feature — No Segment Builder
    - Actual: The Customers page offers only a text search box and a single "All Statuses" dropdown; no multi-criteria segment definition UI exists on Customers, Settings, or Reports, and the word "segment" appears nowhere in the application, so segments cannot be defined, applied, or re-applied.

- [X] FT-07: View a summary report of engagement and revenue
  - Action: Navigate to the summary/report view.
  - Expected: A report displays engagement metrics (e.g., invitations, interest activity) and revenue figures based on purchases.

- [X] FT-08: Reconfigure report settings
  - Action: Change a report configuration option (e.g., time range or metric selection) and apply it.
  - Expected: The report content updates to reflect the new configuration.

## Constraint
- [ ] CS-01: Cannot create a customer with empty required fields
  - Action: Submit the customer creation form with required fields (e.g., name) left blank.
  - Expected: Submission is blocked and an inline validation message identifies the missing required field(s).
  - Bug Report:
    - Issue: Missing Inline Validation Message
    - Actual: Submission is blocked (dialog stays open, no record created), but the only feedback is a global toast at the top of the page ("Missing required fields - Please fill in first name, last name, and email."); no inline/field-level validation message appears inside the form and fields are not marked invalid (no aria-invalid, no field error text).

- [ ] CS-02: Cannot apply an invalid status to a customer
  - Action: Attempt to apply a workflow status not permitted for the customer's current state (or select an empty status).
  - Expected: The invalid status is rejected with a clear error message, and the customer's status remains unchanged.
  - Bug Report:
    - Issue: No Status Validation — Invalid/Regression Status Not Rejected
    - Actual: Applying the state-regressive status "New Lead" to a VIP Collector with 8 purchases and $156,000 total was accepted with a success toast ("Status updated - Customer status changed to New Lead") and the status changed on the record; the selector contains only fixed options with no empty/invalid choice, so no rejection path or error message exists.

- [X] CS-03: Filters and segments cannot combine conflicting criteria without result
  - Action: Apply a filter combination that matches no customers (e.g., two mutually exclusive statuses).
  - Expected: The list shows an explicit "no results" state rather than unfiltered or partial data.

- [ ] CS-04: Duplicate customer prevention
  - Action: Create a customer using an email address already existing in the default data.
  - Expected: The save is rejected with a message indicating the email is already in use.
  - Bug Report:
    - Issue: Duplicate Email Not Rejected
    - Actual: Creating a customer with the existing email v.ashworth@email.com succeeded — toast "Customer created - Duplicate Tester has been added." and the list then showed two records sharing the same email; no rejection or "email already in use" message appeared.

## Interaction
- [X] IX-01: Success feedback after saving a customer
  - Action: Create or update a customer successfully.
  - Expected: A success toast/confirmation message appears and the list or record view refreshes to show the change.

- [X] IX-02: Error feedback on failed save
  - Action: Trigger a save failure (e.g., via a validation error).
  - Expected: An error message appears near the affected action, and previously entered data is preserved.

- [X] IX-03: Customer list responds immediately to filter changes
  - Action: Toggle a filter or segment on and off.
  - Expected: The list updates without a full page reload, and clearing filters restores the full default list.

- [X] IX-04: Report view reflects configuration changes visually
  - Action: Change a report option and apply it.
  - Expected: The report's charts/figures re-render to match the new selection, with a visible loading or update state if needed.

## Content
- [X] CT-01: Customer records display niche-relevant fields
  - Action: Inspect a customer record from the default data.
  - Expected: Fields relate to the niche CRM theme (e.g., collector interests, exhibition invitations, artwork purchases), with no generic or placeholder labels.

- [X] CT-02: Related items show correct artwork details
  - Action: Open a customer's related items list.
  - Expected: Each attached artwork shows its correct title, artist, and other stored details matching the default data.

- [ ] CT-03: Report figures are consistent with underlying customer data
  - Action: Compare report revenue/engagement totals against the purchase and interaction data shown in customer records.
  - Expected: Report values are numerically consistent with the record data (no mismatched totals).
  - Bug Report:
    - Issue: Mismatched Report Figures
    - Actual: Report shows "Avg. Purchase Value: $123,333" (= $740,000 ÷ 6 paying customers), but the records contain 31 total purchases for $740,000 (true average $23,871); additionally Victoria Ashworth's record shows "Purchases: 8 / Total Spent: $156,000" while her Purchase History lists only 2 artworks totaling $40,500. (Note: Total Revenue $740,000 does match the sum of customers' Total Spent, but the derived figures do not reconcile with the purchase data.)

- [ ] CT-04: Status labels are meaningful to the workflow
  - Action: Review the available custom statuses in the status selector.
  - Expected: All statuses are specific to the niche workflow (e.g., "Invitation Sent", "Acquisition In Progress"), with no generic labels like "Status 1" or "TBD".
  - Bug Report:
    - Issue: Generic (Non-Niche) Status Labels
    - Actual: The status selector offers only a generic sales pipeline — "New Lead", "Contacted", "Interested", "Negotiating", "Purchased", "VIP Collector", "Inactive". None reflect the gallery workflow referenced in FT-04 ("Invitation Sent", "Purchase In Progress") or the brief's exhibition-invitation/acquisition workflows; labels such as "New Lead"/"Contacted"/"Inactive" are industry-generic rather than niche-specific.

**Summary: 12 PASS / 8 FAIL** (across 20 items)