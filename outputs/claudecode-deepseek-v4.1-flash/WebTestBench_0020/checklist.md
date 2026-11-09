# Test Checklist

## Functionality
- [ ] FT-01: Admin can create a new box plan
  - Action: Open the plan configuration form, enter a plan name, price, billing cycle, and maximum subscriber count, then save.
  - Expected: New plan appears in the plan list with the entered values.

- [ ] FT-02: Admin can assign specific products to a plan
  - Action: Select a plan, add one or more products from the available product list, then save.
  - Expected: Selected products are saved and displayed as belonging to that plan.

- [ ] FT-03: Plan list shows configuration details
  - Action: Open the plans view and inspect each plan row.
  - Expected: Each plan displays its price, billing cycle, and maximum subscriber count.

- [ ] FT-04: Admin can review customer subscriptions
  - Action: Open the subscriptions view.
  - Expected: A list of customer subscriptions displays with customer name, current plan, and subscription status.

- [ ] FT-05: Admin can update a customer's shipping address
  - Action: Open a customer subscription, edit the address fields, and save.
  - Expected: The saved address is shown as the customer's current shipping address.

- [ ] FT-06: Admin can change a customer's plan choice
  - Action: Open a customer subscription, select a different plan, and save.
  - Expected: The customer's subscription reflects the newly selected plan.

- [ ] FT-07: Admin can view a customer's payment history
  - Action: Open a customer subscription and view the payment history section.
  - Expected: A list of past payments (date and amount) is displayed for that customer.

- [ ] FT-08: Admin can mark an order as prepared
  - Action: Select an order for a billing cycle and click "Mark as Prepared".
  - Expected: The order status changes to "Prepared".

- [ ] FT-09: Admin can mark an order as shipped
  - Action: Select an order and click "Mark as Shipped".
  - Expected: The order status changes to "Shipped".

- [ ] FT-10: Admin can view inventory levels
  - Action: Open the inventory view.
  - Expected: Current stock quantity is displayed for each product.

- [ ] FT-11: Admin can see required units for upcoming shipments
  - Action: Open the upcoming shipment/inventory view for a billing cycle.
  - Expected: Each product shows the total units needed based on active subscriptions for that cycle.

## Constraint
- [ ] CS-01: Cannot exceed a plan's maximum subscriber count
  - Action: Attempt to add a subscriber to a plan that has already reached its maximum subscriber count.
  - Expected: The action is blocked and an error indicates the plan is full.

- [ ] CS-02: Cannot set maximum subscribers below current subscriber count
  - Action: Edit a plan's maximum subscriber count to a number lower than its current subscriber count and save.
  - Expected: Save is rejected with a message that the limit is below the existing subscriber count.

- [ ] CS-03: Required plan fields must be filled
  - Action: Attempt to save a plan with the name, price, billing cycle, or max subscriber count left empty.
  - Expected: Save is blocked and the missing required field(s) are flagged.

- [ ] CS-04: Plan price must be a positive value
  - Action: Enter a zero or negative value in the plan price field and save.
  - Expected: Save is rejected and a validation message states the price must be greater than zero.

## Interaction
- [ ] IX-01: Confirmation shown after saving a plan
  - Action: Save a valid plan configuration.
  - Expected: A success confirmation (toast/message) is displayed.

- [ ] IX-02: Order status updates visually when marked
  - Action: Mark an order as "Prepared", then as "Shipped".
  - Expected: The order's status badge/label updates on screen without a manual refresh.

- [ ] IX-03: Subscription view reflects address update immediately
  - Action: Save an edited customer address, then view the same subscription.
  - Expected: The updated address is displayed.

## Content
- [ ] CT-01: Upcoming shipment figures match assigned plan products
  - Action: Compare the required-units list for a billing cycle against the products assigned to active plans.
  - Expected: Only products assigned to active plans appear, with unit counts consistent with active subscriptions.

- [ ] CT-02: Payment history entries are valid and customer-specific
  - Action: Open payment history for two different customers and compare.
  - Expected: Each history shows only that customer's payments, with valid dates and non-zero amounts.