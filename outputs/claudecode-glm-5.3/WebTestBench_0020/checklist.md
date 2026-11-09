# Test Checklist

## Functionality
- [ ] FT-01: Admin can create a new box plan with all required configuration fields.
  - Action: Navigate to plan creation, enter a plan name, set a price (e.g., $29.99), select a billing cycle (e.g., Monthly), and set a max subscriber count (e.g., 100), then save.
  - Expected: New plan appears in the plan list with the entered name, price, billing cycle, and max subscriber count.

- [ ] FT-02: Admin can edit an existing plan's price, billing cycle, and max subscriber count.
  - Action: Select an existing plan from the plan list, change its price, billing cycle, and max subscriber count, then save.
  - Expected: Plan details update to reflect the new values in the plan list.

- [ ] FT-03: Admin can assign specific products to a plan.
  - Action: Open a plan's product assignment section, select one or more products from the available product list, and confirm the assignment.
  - Expected: Selected products are displayed as assigned to the plan.

- [ ] FT-04: Admin can view current inventory levels for all products.
  - Action: Navigate to the inventory section and review the product list.
  - Expected: Each product displays its name and current stock/inventory quantity.

- [ ] FT-05: Admin can view total units needed per product for upcoming shipments.
  - Action: Navigate to the shipment planning or product demand section and review the quantities listed for each product.
  - Expected: Each product displays the total number of units required for the upcoming billing cycle, calculated from active subscriber counts.

- [ ] FT-06: Admin can view a list of all customer subscriptions.
  - Action: Navigate to the subscriptions/customers section.
  - Expected: A list of customer subscriptions is displayed showing customer name, assigned plan, and subscription status.

- [ ] FT-07: Admin can update a customer's shipping address.
  - Action: Open a customer subscription record, edit the shipping address fields (street, city, state, zip), and save.
  - Expected: Customer's address is updated and displayed with the new values.

- [ ] FT-08: Admin can change a customer's plan choice.
  - Action: Open a customer subscription record, select a different plan from the plan dropdown, and save.
  - Expected: Customer's subscription displays the newly selected plan.

- [ ] FT-09: Admin can view payment history for a customer subscription.
  - Action: Open a customer subscription record and navigate to the payment history section.
  - Expected: A chronological list of past payments is displayed with relevant details.

- [ ] FT-10: Admin can mark an order as "Prepared" for a billing cycle.
  - Action: Locate an order in the current billing cycle, click the action to mark it as "Prepared".
  - Expected: Order status changes to "Prepared" and is visually indicated.

- [ ] FT-11: Admin can mark an order as "Shipped" for a billing cycle.
  - Action: Locate an order that has been prepared, click the action to mark it as "Shipped".
  - Expected: Order status changes to "Shipped" and is visually indicated.

## Constraint
- [ ] CS-01: Cannot save a new plan with empty required fields.
  - Action: Attempt to create a new plan leaving the plan name or price empty, then submit.
  - Expected: Form is not saved; a validation error indicates which required fields are missing.

- [ ] CS-02: Cannot enter a negative value for price or max subscriber count.
  - Action: Attempt to set a plan price or max subscriber count to a negative number (e.g., -10) and submit.
  - Expected: Form is rejected or the field is flagged with a validation error; negative values are not accepted.

- [ ] CS-03: Cannot set max subscriber count below the current number of active subscribers.
  - Action: Select a plan that has active subscribers (e.g., 25), attempt to set the max subscriber count to a number lower than 25, and save.
  - Expected: Change is rejected or blocked with an error message indicating the count cannot be below current subscribers.

- [ ] CS-04: Order must be marked "Prepared" before it can be marked "Shipped".
  - Action: Locate an order that has not been prepared and attempt to mark it as "Shipped".
  - Expected: Action is blocked or an error message indicates the order must be prepared first.

## Interaction
- [ ] IX-01: Success confirmation is displayed after saving a plan.
  - Action: Create or update a plan with valid data and submit.
  - Expected: A success toast or notification appears confirming the plan has been saved.

- [ ] IX-02: Order status label updates immediately when marked as prepared or shipped.
  - Action: Click the "Mark as Prepared" or "Mark as Shipped" button on an order in the billing cycle view.
  - Expected: The order's status badge/label changes instantly to reflect the new status without requiring a page refresh.

- [ ] IX-03: Product demand quantities recalculate when a customer's plan is changed.
  - Action: Change a customer's subscription from Plan A to Plan B, then navigate to the product demand/shipment planning section.
  - Expected: Unit quantities for products assigned to Plan A decrease and Plan B's products increase accordingly.

## Content
- [ ] CT-01: All displayed plans, products, customers, and orders are directly relevant to the subscription box business.
  - Action: Review the plan list, product inventory, customer subscriptions, and order sections.
  - Expected: All entries are coherent subscription-box business data (e.g., box plans, physical products, customer names, subscription orders); no placeholder or irrelevant content.

- [ ] CT-02: Payment history entries display relevant and complete details.
  - Action: Open a customer's payment history and review each entry.
  - Expected: Each payment entry shows at minimum the payment date, amount, and payment status (e.g., Paid, Failed); no blank or incomplete records.