# Test Checklist

## Functionality
- [ ] FT-01: Customer list displays existing customer records on the admin page.
  - Action: Open the CRM admin page and view the customer list.
  - Expected: The list shows the default customer records with columns for name, status, and last activity.

- [ ] FT-02: Staff can create a new customer record.
  - Action: Click "Add Customer", fill in name "Test Collector", interest "Contemporary Painting", and save.
  - Expected: The new customer appears in the customer list with the entered details.

- [ ] FT-03: Staff can update an existing customer record.
  - Action: Open a default customer, change its interest field, and click "Save Changes".
  - Expected: The updated value is shown in the customer detail view and persists after reload.

- [ ] FT-04: Staff can attach a related item (e.g., artwork) to a customer record.
  - Action: Open a customer, click "Attach Item", select an artwork from the default item list, and confirm.
  - Expected: The artwork appears under the customer's related items list.

- [ ] FT-05: Staff can remove an attached item from a customer record.
  - Action: On a customer with an attached artwork, click the remove control for that item and confirm.
  - Expected: The item no longer appears in the customer's related items list.

- [ ] FT-06: Staff can create a custom workflow status.
  - Action: Open the status manager, click "Add Status", enter "Exhibition Invited", and save.
  - Expected: The new status appears in the status list and in the status dropdown on customer records.

- [ ] FT-07: Staff can apply a custom status to a customer to track workflow stage.
  - Action: Open a customer, set its status to "Exhibition Invited" (or another default custom status), and save.
  - Expected: The customer's record shows the selected status and it persists after reload.

- [ ] FT-08: Staff can filter customers by status.
  - Action: Select status "Exhibition Invited" in the filter panel.
  - Expected: The customer list shows only customers whose status is "Exhibition Invited".

- [ ] FT-09: Staff can filter customers by attribute or behavior (e.g., interest or purchase activity).
  - Action: Filter by interest "Contemporary Painting" (or equivalent default attribute).
  - Expected: The list shows only customers matching that interest; the count label reflects the filtered number.

- [ ] FT-10: Staff can combine multiple filters to segment customers.
  - Action: Apply a status filter together with an interest filter.
  - Expected: The list shows only customers matching both criteria simultaneously.

- [ ] FT-11: Clearing filters restores the full customer list.
  - Action: Click "Clear Filters" after applying one or more filters.
  - Expected: All default customers are shown again.

- [ ] FT-12: Staff can view a summary report of engagement and revenue patterns.
  - Action: Open the reports section and select the default summary report.
  - Expected: A report is displayed showing engagement figures and revenue totals for the listed customers.

- [ ] FT-13: Staff can configure a report (e.g., change metric or time range) and see it update.
  - Action: Change the report's metric or date range selector to another option.
  - Expected: The report re-renders with data matching the newly selected metric/range.

## Constraint
- [ ] CS-01: Customer cannot be created with an empty required name field.
  - Action: Click "Add Customer", leave the name field blank, and submit.
  - Expected: Submission is blocked and a validation error marks the name field as required; no customer is added.

- [ ] CS-02: A custom status cannot be created without a name.
  - Action: In the status manager, click "Add Status" with an empty name and save.
  - Expected: Submission is blocked with a validation error; no status is created.

- [ ] CS-03: A duplicate status name cannot be created.
  - Action: Create a status with a name identical to an existing default status (e.g., "Purchased").
  - Expected: Creation is blocked with a message indicating the status name already exists.

- [ ] CS-04: A duplicate customer record cannot be created for the same email.
  - Action: Create a customer using the email address of a default existing customer.
  - Expected: Save is blocked with a message indicating the email is already in use.

## Interaction
- [ ] IX-01: Saving a customer create or update shows a success confirmation.
  - Action: Save a new or edited customer record.
  - Expected: A success toast/notification (e.g., "Customer saved") is displayed and dismissed after a short time.

- [ ] IX-02: Submitting an invalid form shows inline field-level error feedback.
  - Action: Submit the Add Customer form with the name field empty.
  - Expected: The offending field is highlighted with an inline error message next to it, and focus moves to that field.

- [ ] IX-03: Changing a filter immediately updates the customer list without a manual refresh.
  - Action: Select a different status in the filter panel.
  - Expected: The list content updates in place to reflect the new filter, with no full page reload.

## Content
- [ ] CT-01: Page content uses niche-domain (gallery) terminology consistent with the instruction.
  - Action: Review labels, fields, and headings across the customer, workflow, and reports sections.
  - Expected: Text references domain concepts such as collectors' interests, exhibition invitations, and artwork purchases; no placeholder or unrelated text is shown.

- [ ] CT-02: Report content presents engagement and revenue data relevant to the niche.
  - Action: Open the summary report and review its metrics and labels.
  - Expected: The report shows engagement and revenue figures derived from the default customer/related-item data, with labels matching the domain (e.g., artwork purchases).