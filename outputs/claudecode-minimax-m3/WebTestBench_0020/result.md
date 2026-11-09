I have all the test results. Let me prepare the final report.

# Test Result

## Functionality
- [X] FT-01: Create a new subscription box plan
  - Action: Navigate to plans section and create a new plan with name, price, billing cycle, and max subscriber count
  - Expected: New plan appears in the plans list with all configured details saved

- [X] FT-02: Assign products to a box plan
  - Action: Open an existing plan and add specific products (with quantities per box) from the product catalog
  - Expected: Selected products are listed under the plan and saved successfully

- [X] FT-03: View upcoming shipment unit requirements per product
  - Action: Navigate to the shipments/upcoming section and view product demand
  - Expected: Each product shows total units required = (quantity per box) × (active subscribers) for upcoming shipments

- [X] FT-04: View list of customer subscriptions
  - Action: Navigate to the subscriptions section
  - Expected: A list of customers with their active plan, status, and next billing date is displayed

- [X] FT-05: Update a customer's shipping address
  - Action: Open a customer subscription, edit the shipping address fields, and save
  - Expected: Updated address is saved and reflected on the customer record

- [X] FT-06: Change a customer's plan assignment
  - Action: Open a customer subscription, select a different plan, and save
  - Expected: The customer's plan is updated and reflected on the subscription record

- [X] FT-07: View a customer's payment history
  - Action: Open a customer subscription and access the payment history section
  - Expected: A list of past payments with date, amount, and status is displayed

- [X] FT-08: Mark an order as prepared
  - Action: Open an order from a billing cycle and mark it as "prepared"
  - Expected: Order status updates to "prepared" and persists in the order list

- [X] FT-09: Mark an order as shipped
  - Action: Open a prepared order and mark it as "shipped"
  - Expected: Order status updates to "shipped" and persists in the order list

- [X] FT-10: View current inventory levels per product
  - Action: Navigate to the inventory section
  - Expected: Each product displays its current stock quantity

## Constraint
- [X] CS-01: Plan creation requires price and billing cycle
  - Action: Attempt to create a new plan leaving price or billing cycle blank
  - Expected: Submission is blocked and a validation message indicates the missing required fields

- [ ] CS-02: Plan cannot exceed configured max subscriber count
  - Action: Attempt to assign a customer to a plan that already reached its max subscriber limit
  - Expected: Assignment is blocked and a message indicates the plan is at capacity
  - Bug Report:
    - Issue: Missing Capacity Validation
    - Actual: Successfully changed Marcus Chen from Starter Box (342/500) to Premium Box (287/300) without any capacity check. The plan dropdown lists all available plans without showing subscriber count or capacity. No warning or blocking was applied when assigning to plans nearing capacity.

- [X] CS-03: Cannot mark an order as shipped before it is prepared
  - Action: On a new (not yet prepared) order, attempt to mark it as "shipped"
  - Expected: Action is blocked and a message indicates the order must be prepared first

- [ ] CS-04: Inventory cannot go negative when assigning products to plans
  - Action: Attempt to assign products in quantities that exceed available inventory
  - Expected: Assignment is blocked or a warning indicates insufficient inventory
  - Bug Report:
    - Issue: Negative Inventory Allowed
    - Actual: Leather Journal (JRN-006) shows Available: -15 in the Products table. The system permits inventory levels to drop below zero, with no warning, validation, or visual alert (only a generic icon) when stock becomes insufficient.

## Interaction
- [X] IX-01: Confirmation feedback appears after marking an order as shipped
  - Action: Mark an order as shipped and observe the page response
  - Expected: A success/confirmed message is displayed confirming the status change

- [ ] IX-02: Inventory levels decrement after an order is marked as shipped
  - Action: Note inventory level for a product, then mark an order containing that product as shipped
  - Expected: The product's inventory count decreases by the units shipped in that order
  - Bug Report:
    - Issue: Inventory Not Decremented On Shipping
    - Actual: After marking ord-2 (Marcus Chen, Starter Box) as shipped and ord-3 (Sofia Rodriguez, Deluxe Quarterly) as shipped, the Products page inventory values remained identical. Artisan Chocolate Bar Stock: 1,200 (unchanged), Organic Tea Sampler Stock: 800 (unchanged), Scented Candle Set Stock: 450 (unchanged), Luxury Bath Bomb Set Stock: 280 (unchanged). Reserved counts also unchanged.

- [X] IX-03: Order status indicator updates visually from prepared to shipped
  - Action: Mark a prepared order as shipped and observe the status display
  - Expected: The order's status indicator/badge visibly changes to reflect "shipped" state

## Content
- [X] CT-01: Plan details (name, price, billing cycle, max subscribers) display correctly
  - Action: Open any plan from the plans list
  - Expected: All four attributes (name, price, billing cycle, max subscribers) are shown with correct values

- [X] CT-02: Customer payment history shows correct amounts and dates
  - Action: Open the payment history for a customer who has been billed
  - Expected: Each payment entry shows the correct amount and the date the payment occurred