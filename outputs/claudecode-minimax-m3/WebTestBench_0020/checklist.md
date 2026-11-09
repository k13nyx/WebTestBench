# Test Checklist

## Functionality
- [ ] FT-01: Create a new subscription box plan
  - Action: Navigate to plans section and create a new plan with name, price, billing cycle, and max subscriber count
  - Expected: New plan appears in the plans list with all configured details saved

- [ ] FT-02: Assign products to a box plan
  - Action: Open an existing plan and add specific products (with quantities per box) from the product catalog
  - Expected: Selected products are listed under the plan and saved successfully

- [ ] FT-03: View upcoming shipment unit requirements per product
  - Action: Navigate to the shipments/upcoming section and view product demand
  - Expected: Each product shows total units required = (quantity per box) × (active subscribers) for upcoming shipments

- [ ] FT-04: View list of customer subscriptions
  - Action: Navigate to the subscriptions section
  - Expected: A list of customers with their active plan, status, and next billing date is displayed

- [ ] FT-05: Update a customer's shipping address
  - Action: Open a customer subscription, edit the shipping address fields, and save
  - Expected: Updated address is saved and reflected on the customer record

- [ ] FT-06: Change a customer's plan assignment
  - Action: Open a customer subscription, select a different plan, and save
  - Expected: The customer's plan is updated and reflected on the subscription record

- [ ] FT-07: View a customer's payment history
  - Action: Open a customer subscription and access the payment history section
  - Expected: A list of past payments with date, amount, and status is displayed

- [ ] FT-08: Mark an order as prepared
  - Action: Open an order from a billing cycle and mark it as "prepared"
  - Expected: Order status updates to "prepared" and persists in the order list

- [ ] FT-09: Mark an order as shipped
  - Action: Open a prepared order and mark it as "shipped"
  - Expected: Order status updates to "shipped" and persists in the order list

- [ ] FT-10: View current inventory levels per product
  - Action: Navigate to the inventory section
  - Expected: Each product displays its current stock quantity

## Constraint
- [ ] CS-01: Plan creation requires price and billing cycle
  - Action: Attempt to create a new plan leaving price or billing cycle blank
  - Expected: Submission is blocked and a validation message indicates the missing required fields

- [ ] CS-02: Plan cannot exceed configured max subscriber count
  - Action: Attempt to assign a customer to a plan that already reached its max subscriber limit
  - Expected: Assignment is blocked and a message indicates the plan is at capacity

- [ ] CS-03: Cannot mark an order as shipped before it is prepared
  - Action: On a new (not yet prepared) order, attempt to mark it as "shipped"
  - Expected: Action is blocked and a message indicates the order must be prepared first

- [ ] CS-04: Inventory cannot go negative when assigning products to plans
  - Action: Attempt to assign products in quantities that exceed available inventory
  - Expected: Assignment is blocked or a warning indicates insufficient inventory

## Interaction
- [ ] IX-01: Confirmation feedback appears after marking an order as shipped
  - Action: Mark an order as shipped and observe the page response
  - Expected: A success/confirmed message is displayed confirming the status change

- [ ] IX-02: Inventory levels decrement after an order is marked as shipped
  - Action: Note inventory level for a product, then mark an order containing that product as shipped
  - Expected: The product's inventory count decreases by the units shipped in that order

- [ ] IX-03: Order status indicator updates visually from prepared to shipped
  - Action: Mark a prepared order as shipped and observe the status display
  - Expected: The order's status indicator/badge visibly changes to reflect "shipped" state

## Content
- [ ] CT-01: Plan details (name, price, billing cycle, max subscribers) display correctly
  - Action: Open any plan from the plans list
  - Expected: All four attributes (name, price, billing cycle, max subscribers) are shown with correct values

- [ ] CT-02: Customer payment history shows correct amounts and dates
  - Action: Open the payment history for a customer who has been billed
  - Expected: Each payment entry shows the correct amount and the date the payment occurred