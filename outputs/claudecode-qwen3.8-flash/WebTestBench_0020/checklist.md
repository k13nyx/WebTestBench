# Test Checklist

## Functionality

- [ ] FT-01: Admin can create a new box plan by providing name, price, billing cycle, and max subscribers
  - Action: Open the "Plans" section, click "Add Plan", enter name = "Test Box", price = "29.99", billing cycle = "Monthly", max subscribers = "50", and save.
  - Expected: The new plan "Test Box" appears in the plan list showing $29.99, "Monthly" cycle, and a max of 50 subscribers.

- [ ] FT-02: Admin can assign products to a specific plan
  - Action: Open an existing plan's edit view, add one default product to the plan's contents, and save.
  - Expected: The added product is listed under that plan's "Products"/"Contents" and persists after reopening the plan.

- [ ] FT-03: Inventory report shows units of each product needed for upcoming shipments
  - Action: Open the "Inventory" section and view the "Needed for upcoming shipments" figures.
  - Expected: Each product row displays a required-unit count computed from active subscriptions, and on-hand stock level is shown alongside it.

- [ ] FT-04: Admin can review the list of customer subscriptions
  - Action: Open the "Subscriptions" section.
  - Expected: A table lists each customer with their plan, current status (e.g., Active), and billing cycle.

- [ ] FT-05: Admin can update a customer's shipping address
  - Action: Select a default customer's subscription, edit the address fields, and save.
  - Expected: The saved new address is reflected in that customer's subscription record.

- [ ] FT-06: Admin can change a customer's plan choice
  - Action: Edit a default customer's subscription and switch its plan to another existing plan, then save.
  - Expected: The customer's subscription now shows the newly selected plan name.

- [ ] FT-07: Admin can view payment history for a customer subscription
  - Action: Open the "Payment History" view for a default active customer.
  - Expected: A list of past payments is shown, each with an amount and a date.

- [ ] FT-08: Admin can select a billing cycle to organize shipping orders
  - Action: Open the "Shipping" section and select an upcoming billing cycle from the cycle selector.
  - Expected: The order list filters to show only the orders belonging to that billing cycle.

- [ ] FT-09: Admin can mark an order as "Prepared" for a billing cycle
  - Action: In the "Shipping" section, on a default order click the "Mark Prepared" (or status → "Prepared") action.
  - Expected: That order's status changes to "Prepared".

- [ ] FT-10: Admin can mark a prepared order as "Shipped" for a billing cycle
  - Action: On an order whose status is "Prepared", click the "Mark Shipped" (or status → "Shipped") action.
  - Expected: That order's status changes to "Shipped".

## Constraint

- [ ] CS-01: A plan cannot be saved with an invalid max subscriber count below its current subscriber count
  - Action: Edit a plan that has existing subscribers and set "Max Subscribers" to a value lower than its current active subscriber count, then save.
  - Expected: The save is rejected with a validation error and the plan's max is not decreased below the current count.

- [ ] CS-02: Required plan fields must be valid before a plan is accepted
  - Action: Click "Add Plan" and attempt to save with the name empty or the price negative/non-numeric.
  - Expected: The form is rejected with a validation message identifying the offending field; no plan is created.

- [ ] CS-03: An order cannot be marked "Shipped" before it is "Prepared"
  - Action: On an order still in the default "Pending"/"New" status, attempt to set status directly to "Shipped".
  - Expected: The action is blocked (control disabled or error) so an unprepared order cannot jump to "Shipped".

- [ ] CS-04: A product can only be assigned to a plan from the existing inventory catalog
  - Action: Open a plan's product-assignment control and attempt to assign a product that does not exist in the catalog.
  - Expected: Only catalog products are selectable/assignable; the nonexistent product cannot be added to the plan.

## Interaction

- [ ] IX-01: The interface provides navigation between the major admin sections
  - Action: Use the top-level navigation/tabs to move between "Plans", "Inventory", "Subscriptions", and "Shipping".
  - Expected: Selecting each section loads its corresponding view and highlights the active section.

- [ ] IX-02: A plan's subscriber count / capacity updates immediately after editing its settings
  - Action: Change a plan's max-subscriber value in "Plans" and return to the plan list.
  - Expected: The plan card/row refreshes to display the new max and current-subscriber figures without a manual reload.

- [ ] IX-03: The inventory "needed" total reflects subscription changes
  - Action: Note the "Needed for upcoming shipments" count for a product, then add/remove an active subscription on that product's plan and re-check.
  - Expected: The product's required-unit count increases or decreases accordingly.

- [ ] IX-04: The order list reflects status changes in real time
  - Action: Mark an order "Shipped" in the "Shipping" section.
  - Expected: The order's status badge updates to "Shipped" in the list immediately and its position/count in any "prepared"/"shipped" summary changes.

## Content

- [ ] CT-01: Default plans, products, and customer subscription data are present and internally consistent
  - Action: Load the app and inspect the "Plans", "Inventory", and "Subscriptions" sections.
  - Expected: Pre-existing plans, catalog products, and customer subscriptions are populated (not empty), with relevant subscription-box content.

- [ ] CT-02: Payment history amounts match the corresponding plan price
  - Action: Open the payment history for a default customer and compare the recorded charge amount to the price of that customer's plan.
  - Expected: Each payment amount equals the plan's configured price for its billing cycle.