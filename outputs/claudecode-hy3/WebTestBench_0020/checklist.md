# Test Checklist

## Functionality
- [ ] FT-01: Admin can create a new box plan
  - Action: Click "Add Plan" (or "New Plan") and fill in the plan name, then click "Save".
  - Expected: The new box plan appears in the plans list.

- [ ] FT-02: Admin can set a plan price
  - Action: Open a plan's edit view and enter a value in the "Plan Price" field, then save.
  - Expected: The entered price is displayed for that plan.

- [ ] FT-03: Admin can set a billing cycle for a plan
  - Action: Open a plan's edit view and select a cycle (e.g., Monthly / Quarterly) from the "Billing Cycle" control, then save.
  - Expected: The chosen billing cycle is shown for that plan.

- [ ] FT-04: Admin can set a maximum subscriber count for a plan
  - Action: Open a plan's edit view and enter a number in the "Max Subscribers" field, then save.
  - Expected: The entered maximum subscriber count is displayed for that plan.

- [ ] FT-05: Admin can assign specific products to a plan
  - Action: Open a plan's "Products" section and add/select one or more products, then save.
  - Expected: The assigned products are listed under that plan.

- [ ] FT-06: Admin can see units needed per product for upcoming shipments
  - Action: Open the upcoming shipments / inventory forecast view.
  - Expected: Each product shows the number of units required for the next shipment.

- [ ] FT-07: Admin can review customer subscriptions
  - Action: Open the "Subscriptions" (or "Customers") list.
  - Expected: A list of customer subscriptions with their current plan is displayed.

- [ ] FT-08: Admin can update a customer's shipping address
  - Action: Open a customer's subscription and edit the address fields, then save.
  - Expected: The updated address is shown for that customer.

- [ ] FT-09: Admin can change a customer's plan choice
  - Action: Open a customer's subscription and select a different plan, then save.
  - Expected: The customer's subscription now reflects the new plan.

- [ ] FT-10: Admin can view a customer's payment history
  - Action: Open a customer's subscription and open the "Payment History" section.
  - Expected: A list of past payments (date and amount) is displayed.

- [ ] FT-11: Admin can mark an order as prepared for a billing cycle
  - Action: Open a customer's order for a billing cycle and click "Mark as Prepared".
  - Expected: The order status changes to "Prepared".

- [ ] FT-12: Admin can mark an order as shipped for a billing cycle
  - Action: Open a customer's order for a billing cycle and click "Mark as Shipped".
  - Expected: The order status changes to "Shipped".

- [ ] FT-13: Admin can view inventory levels
  - Action: Open the "Inventory" view.
  - Expected: Each product shows its current stock/inventory level.

## Constraint
- [ ] CS-01: Plan cannot be saved with missing required fields
  - Action: Attempt to save a plan with the name or price field left empty.
  - Expected: Save is blocked and a validation message indicates the required field(s).

- [ ] CS-02: Subscriber count cannot exceed the plan's maximum
  - Action: Attempt to add/assign subscribers beyond the configured "Max Subscribers" value.
  - Expected: The action is blocked and a message states the subscriber limit is reached.

- [ ] CS-03: Order cannot be marked shipped before being prepared
  - Action: On an order that is not yet "Prepared", click "Mark as Shipped".
  - Expected: The action is blocked; status remains not-shipped with an explanatory message.

## Interaction
- [ ] IX-01: Success confirmation appears after saving a plan
  - Action: Create or edit a plan and click "Save".
  - Expected: A success toast/confirmation is shown and the plan list/status updates.

- [ ] IX-02: Order status badge updates immediately after status change
  - Action: Click "Mark as Prepared" or "Mark as Shipped" on an order.
  - Expected: The order's status badge visually changes to the new state without page reload.

## Content
- [ ] CT-01: Product media in plan assignment is relevant to assigned products
  - Action: Open a plan's assigned products and review the displayed images/icons.
  - Expected: Each image/icon directly corresponds to the assigned product (no placeholders or unrelated media).

- [ ] CT-02: Payment history shows accurate date and amount data
  - Action: Open a customer's "Payment History".
  - Expected: Each entry displays a correct payment date and amount with no missing or garbled values.