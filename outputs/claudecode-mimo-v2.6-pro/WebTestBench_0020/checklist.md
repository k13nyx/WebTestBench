# Test Checklist

## Functionality
- [ ] FT-01: Create a new box plan with name, price, and billing cycle.
  - Action: Open the plan configuration section, click "Add Plan" (or equivalent), enter plan name, price, and select a billing cycle; save.
  - Expected: The new plan appears in the plan list with the entered name, price, and billing cycle.

- [ ] FT-02: Edit an existing plan's price, billing cycle, and maximum subscriber count.
  - Action: Open an existing plan from the plan list, change its price, billing cycle, and max subscriber count; save.
  - Expected: The plan list shows the updated values for that plan after saving.

- [ ] FT-03: Assign specific products with quantities to a plan.
  - Action: Open a plan, add existing products to it with a quantity per product; save.
  - Expected: The plan's product assignment shows each selected product with its assigned quantity.

- [ ] FT-04: View units of each product needed for upcoming shipments.
  - Action: Open the inventory / shipment needs view showing upcoming shipments.
  - Expected: Each product is listed with the total number of units needed for the upcoming shipment(s).

- [ ] FT-05: Review the list of customer subscriptions.
  - Action: Open the customer subscriptions section.
  - Expected: A list of subscriptions is displayed, each showing the customer and their current plan.

- [ ] FT-06: Update a customer's shipping address.
  - Action: Open an existing subscription, edit the shipping address fields; save.
  - Expected: The subscription record shows the new address after saving.

- [ ] FT-07: Change a customer's plan choice.
  - Action: Open an existing subscription, select a different plan from the plan options; save.
  - Expected: The subscription record shows the newly selected plan after saving.

- [ ] FT-08: View a customer's payment history.
  - Action: Open an existing subscription and view its payment history.
  - Expected: Past payments for that customer are listed.

- [ ] FT-09: Mark an order as prepared for a billing cycle.
  - Action: In the orders view for the current billing cycle, click "Mark as Prepared" on an order.
  - Expected: The order's status changes to Prepared.

- [ ] FT-10: Mark an order as shipped for a billing cycle.
  - Action: In the orders view for the current billing cycle, click "Mark as Shipped" on a prepared order.
  - Expected: The order's status changes to Shipped.

## Constraint
- [ ] CS-01: A plan cannot accept subscribers beyond its maximum subscriber count.
  - Action: Attempt to assign a new customer subscription to a plan whose current subscriber count equals its maximum.
  - Expected: The action is rejected and the subscriber count does not exceed the maximum.

- [ ] CS-02: Plan price cannot be invalid (empty, zero, negative, or non-numeric).
  - Action: Enter an empty, 0, negative, or non-numeric value in the plan price field and save.
  - Expected: The save is rejected with an error; the plan keeps its previous price.

- [ ] CS-03: Plan must have a billing cycle selected before saving.
  - Action: Create or edit a plan leaving the billing cycle empty/unselected and save.
  - Expected: The save is rejected with an error indicating billing cycle is required.

- [ ] CS-04: Product quantity assigned to a plan cannot be zero, negative, or empty.
  - Action: Assign a product to a plan with quantity 0, a negative number, or left empty; save.
  - Expected: The save is rejected with an error; the invalid assignment is not stored.

- [ ] CS-05: An order cannot be marked as shipped before it is marked as prepared.
  - Action: On an order with a pending (not prepared) status, click "Mark as Shipped".
  - Expected: The action is rejected; the order status remains pending.

## Interaction
- [ ] IX-01: Order status change is reflected immediately in the orders view.
  - Action: Mark an order as Prepared (then Shipped) and observe the orders list without reloading the page.
  - Expected: The order's status indicator updates immediately to the new status in the list.

- [ ] IX-02: Confirmation feedback is shown after saving plan or subscription changes.
  - Action: Save a plan edit (or a subscription address/plan change) and observe the page.
  - Expected: A visible success confirmation (e.g., toast or inline message) appears after the save.

## Content
- [ ] CT-01: Plan list displays name, price, billing cycle, and current vs. maximum subscriber count.
  - Action: View the plan list.
  - Expected: Each plan row shows its name, price, billing cycle, and subscriber count against its maximum.

- [ ] CT-02: Shipment needs view shows product names with required unit counts.
  - Action: View the upcoming-shipment inventory needs.
  - Expected: Each listed product shows its product name and the number of units needed.

- [ ] CT-03: Payment history entries show date, amount, and payment status.
  - Action: View a customer's payment history.
  - Expected: Each payment entry displays its date, amount, and status (e.g., paid/failed).