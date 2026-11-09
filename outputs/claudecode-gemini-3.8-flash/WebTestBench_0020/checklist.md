# Test Checklist

## Functionality
- [ ] FT-01: Configure box plan pricing, billing cycle, and subscriber limit
  - Action: Navigate to "Box Plans", select an existing plan, update the price, billing cycle frequency, and maximum subscriber count, then click "Save Plan".
  - Expected: The updated price, billing cycle, and maximum subscriber limit are saved and displayed on the plan card.
- [ ] FT-02: Assign products to a box plan
  - Action: Open a plan configuration drawer, choose items from the "Available Products" inventory list, and click "Assign to Plan".
  - Expected: The selected products appear under the "Assigned Products" section for that specific box plan.
- [ ] FT-03: Update customer plan selection
  - Action: Select a customer in the "Subscriptions" list, choose a different plan from the "Change Plan" dropdown, and click "Update Subscription".
  - Expected: The customer's active plan immediately reflects the newly selected box plan.
- [ ] FT-04: Update customer shipping address
  - Action: Open a customer profile, edit the street address and postal code fields, and click "Save Address".
  - Expected: The updated shipping address is saved and displayed in the customer's delivery information.
- [ ] FT-05: View customer recurring payment history
  - Action: In a customer profile, click on the "Payment History" tab.
  - Expected: A chronological list of past billing events is displayed, showing transaction dates, amounts billed, and payment statuses.
- [ ] FT-06: View required product units for upcoming shipments
  - Action: Navigate to the "Inventory & Shipments" page and view the upcoming cycle demand summary.
  - Expected: The table lists each assigned product alongside the exact total unit count required to fulfill upcoming cycle shipments.
- [ ] FT-07: Mark billing cycle order as Prepared
  - Action: In the "Shipping Management" table, locate a pending order for the current billing cycle and click "Mark as Prepared".
  - Expected: The order fulfillment status changes from "Pending" to "Prepared".
- [ ] FT-08: Mark prepared order as Shipped
  - Action: Locate an order in "Prepared" status and click "Mark as Shipped".
  - Expected: The order status updates to "Shipped" and the dispatch timestamp is recorded.

## Constraint
- [ ] CS-01: Prevent setting negative price or zero subscriber capacity
  - Action: Enter a negative number in the plan price field and "0" in the maximum subscriber limit field, then click "Save Plan".
  - Expected: The form submission is blocked with validation error messages indicating price must be positive and capacity must be at least 1.
- [ ] CS-02: Prevent assigning subscriptions to a plan at maximum capacity
  - Action: Attempt to switch a customer's subscription to a plan that has reached its maximum subscriber count.
  - Expected: The plan option is disabled or displays an error stating the plan has reached maximum subscriber capacity.
- [ ] CS-03: Prevent saving empty required shipping address fields
  - Action: Clear the "Street Address" and "Postal Code" fields in the customer address editor and click "Save Address".
  - Expected: Submission is blocked and required field warnings appear below the empty inputs.
- [ ] CS-04: Prevent marking order as Shipped before Prepared
  - Action: Locate an order in "Pending" status and attempt to mark it directly as "Shipped".
  - Expected: The "Mark as Shipped" button is disabled or an alert states the order must be marked "Prepared" first.

## Interaction
- [ ] IX-01: Customer details slide-over panel display
  - Action: Click the "Edit" button on any row in the customer subscriptions table.
  - Expected: A slide-over panel opens smoothly from the side with the customer's current details pre-populated.
- [ ] IX-02: Action success feedback on fulfillment update
  - Action: Click "Mark as Prepared" on any pending order.
  - Expected: A success toast message appears confirming the order status has been updated.
- [ ] IX-03: Filter shipping list by billing cycle
  - Action: Select a specific billing cycle from the "Billing Cycle" dropdown filter on the Shipping page.
  - Expected: The orders table instantly refreshes to display only shipments associated with the chosen cycle.

## Content
- [ ] CT-01: Box plan metrics display
  - Action: Review the Box Plans overview section.
  - Expected: Each plan card displays plan name, recurring price, cycle frequency, assigned products count, and current vs. maximum subscriber counts.
- [ ] CT-02: Inventory level vs. shipment demand display
  - Action: Review the inventory overview table.
  - Expected: Each product row clearly displays product name, current stock on hand, required units for next shipment, and remaining stock balance.