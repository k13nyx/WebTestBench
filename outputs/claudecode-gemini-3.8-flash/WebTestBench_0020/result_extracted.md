# Test Result

## Functionality
- [X] FT-01: Configure box plan pricing, billing cycle, and subscriber limit
  - Action: Navigate to "Box Plans", select an existing plan, update the price, billing cycle frequency, and maximum subscriber count, then click "Save Plan".
  - Expected: The updated price, billing cycle, and maximum subscriber limit are saved and displayed on the plan card.
- [X] FT-02: Assign products to a box plan
  - Action: Open a plan configuration drawer, choose items from the "Available Products" inventory list, and click "Assign to Plan".
  - Expected: The selected products appear under the "Assigned Products" section for that specific box plan.
- [X] FT-03: Update customer plan selection
  - Action: Select a customer in the "Subscriptions" list, choose a different plan from the "Change Plan" dropdown, and click "Update Subscription".
  - Expected: The customer's active plan immediately reflects the newly selected box plan.
- [X] FT-04: Update customer shipping address
  - Action: Open a customer profile, edit the street address and postal code fields, and click "Save Address".
  - Expected: The updated shipping address is saved and displayed in the customer's delivery information.
- [ ] FT-05: View customer recurring payment history
  - Action: In a customer profile, click on the "Payment History" tab.
  - Expected: A chronological list of past billing events is displayed, showing transaction dates, amounts billed, and payment statuses.
  - Bug Report:
    - Issue: Missing Payment History Tab
    - Actual: The customer profile dialog only contains fields for Name, Email, Plan, Status, and Shipping Address. There is no "Payment History" tab or past billing events list available within the customer profile.
- [X] FT-06: View required product units for upcoming shipments
  - Action: Navigate to the "Inventory & Shipments" page and view the upcoming cycle demand summary.
  - Expected: The table lists each assigned product alongside the exact total unit count required to fulfill upcoming cycle shipments.
- [X] FT-07: Mark billing cycle order as Prepared
  - Action: In the "Shipping Management" table, locate a pending order for the current billing cycle and click "Mark as Prepared".
  - Expected: The order fulfillment status changes from "Pending" to "Prepared".
- [X] FT-08: Mark prepared order as Shipped
  - Action: Locate an order in "Prepared" status and click "Mark as Shipped".
  - Expected: The order status updates to "Shipped" and the dispatch timestamp is recorded.

## Constraint
- [ ] CS-01: Prevent setting negative price or zero subscriber capacity
  - Action: Enter a negative number in the plan price field and "0" in the maximum subscriber limit field, then click "Save Plan".
  - Expected: The form submission is blocked with validation error messages indicating price must be positive and capacity must be at least 1.
  - Bug Report:
    - Issue: Missing Input Validation
    - Actual: Form submission was not blocked when entering a negative price (`-10`) and zero capacity (`0`). The plan card updated to display `$-10` and `342 / 0` subscribers with no validation error messages shown.
- [ ] CS-02: Prevent assigning subscriptions to a plan at maximum capacity
  - Action: Attempt to switch a customer's subscription to a plan that has reached its maximum subscriber count.
  - Expected: The plan option is disabled or displays an error stating the plan has reached maximum subscriber capacity.
  - Bug Report:
    - Issue: Missing Capacity Limit Enforcement
    - Actual: In the subscription edit dropdown, all plan options remain enabled regardless of capacity, allowing assignments to plans that have reached their maximum subscriber limit without warnings or errors.
- [ ] CS-03: Prevent saving empty required shipping address fields
  - Action: Clear the "Street Address" and "Postal Code" fields in the customer address editor and click "Save Address".
  - Expected: Submission is blocked and required field warnings appear below the empty inputs.
  - Bug Report:
    - Issue: Missing Required Field Validation
    - Actual: Clearing the Street and ZIP Code inputs did not block submission. The customer record was saved with empty address fields and displayed a success toast without any validation warnings.
- [X] CS-04: Prevent marking order as Shipped before Prepared
  - Action: Locate an order in "Pending" status and attempt to mark it directly as "Shipped".
  - Expected: The "Mark as Shipped" button is disabled or an alert states the order must be marked "Prepared" first.

## Interaction
- [ ] IX-01: Customer details slide-over panel display
  - Action: Click the "Edit" button on any row in the customer subscriptions table.
  - Expected: A slide-over panel opens smoothly from the side with the customer's current details pre-populated.
  - Bug Report:
    - Issue: Incorrect Component Type
    - Actual: Clicking the "Edit" button opens a standard centered modal dialog (`DialogContent`), rather than a slide-over panel sliding in from the side.
- [X] IX-02: Action success feedback on fulfillment update
  - Action: Click "Mark as Prepared" on any pending order.
  - Expected: A success toast message appears confirming the order status has been updated.
- [ ] IX-03: Filter shipping list by billing cycle
  - Action: Select a specific billing cycle from the "Billing Cycle" dropdown filter on the Shipping page.
  - Expected: The orders table instantly refreshes to display only shipments associated with the chosen cycle.
  - Bug Report:
    - Issue: Missing Filter Control
    - Actual: The Orders page only provides a status filter dropdown ("All Statuses") and a text search input; there is no "Billing Cycle" dropdown filter available to filter shipments by cycle.

## Content
- [X] CT-01: Box plan metrics display
  - Action: Review the Box Plans overview section.
  - Expected: Each plan card displays plan name, recurring price, cycle frequency, assigned products count, and current vs. maximum subscriber counts.
- [X] CT-02: Inventory level vs. shipment demand display
  - Action: Review the inventory overview table.
  - Expected: Each product row clearly displays product name, current stock on hand, required units for next shipment, and remaining stock balance.
