All tests are complete and the app state has been restored to match my test actions. Here is the full test result report:

# Test Result

## Functionality

- [X] FT-01: Admin can create a new box plan with all required configuration fields.
  - Action: Navigate to plan creation, enter a plan name, set a price (e.g., $29.99), select a billing cycle (e.g., Monthly), and set a max subscriber count (e.g., 100), then save.
  - Expected: New plan appears in the plan list with the entered name, price, billing cycle, and max subscriber count.
  - Result: Created "Seasonal Treats Box" ($29.99, Monthly, max 100) via the "New Plan" dialog; it immediately appeared in the plan list with the exact name, price, cycle, and "0 / 100" subscriber capacity.

- [X] FT-02: Admin can edit an existing plan's price, billing cycle, and max subscriber count.
  - Action: Select an existing plan from the plan list, change its price, billing cycle, and max subscriber count, then save.
  - Expected: Plan details update to reflect the new values in the plan list.
  - Result: Edited "Seasonal Treats Box": price 29.99 → 39.99, cycle Monthly → Quarterly, max 100 → 150. After "Update Plan", the card showed $39.99, /quarterly, 0 / 150.

- [X] FT-03: Admin can assign specific products to a plan.
  - Action: Open a plan's product assignment section, select one or more products from the available product list, and confirm the assignment.
  - Expected: Selected products are displayed as assigned to the plan.
  - Result: In the plan form's "Products in Box" section, checked Artisan Chocolate Bar and Handmade Soap Bar; after saving, the plan card shows "Products (2): Artisan Chocolate Bar, Handmade Soap Bar".

- [X] FT-04: Admin can view current inventory levels for all products.
  - Action: Navigate to the inventory section and review the product list.
  - Expected: Each product displays its name and current stock/inventory quantity.
  - Result: Products & Inventory page lists all 8 products with name, SKU, category, and stock quantity (e.g., Artisan Chocolate Bar 1,200; Organic Tea Sampler 800; Exclusive Wine Selection 100).

- [X] FT-05: Admin can view total units needed per product for upcoming shipments.
  - Action: Navigate to the shipment planning or product demand section and review the quantities listed for each product.
  - Expected: Each product displays the total number of units required for the upcoming billing cycle, calculated from active subscriber counts.
  - Result: The "Reserved" column shows per-product units required for the upcoming cycle, matching active-plan subscriber counts (e.g., 707 = Starter 342 + Premium 287 + Deluxe 78; Handmade Soap 420 = 342 + 78). Dashboard "Low Stock Alerts" additionally surfaces shortages (Tea 93 left, Leather Journal −15 left).

- [X] FT-06: Admin can view a list of all customer subscriptions.
  - Action: Navigate to the subscriptions/customers section.
  - Expected: A list of customer subscriptions is displayed showing customer name, assigned plan, and subscription status.
  - Result: Subscribers page lists 6 subscriptions (Emma Thompson, Marcus Chen, Sofia Rodriguez, James Wilson, Aisha Patel, Oliver Brown) each with customer name/email, assigned plan + price, status (active/paused), address, next billing date, and total spent.

- [X] FT-07: Admin can update a customer's shipping address.
  - Action: Open a customer subscription record, edit the shipping address fields (street, city, state, zip), and save.
  - Expected: Customer's address is updated and displayed with the new values.
  - Result: Edited Emma Thompson's address to 456 Pine Avenue, Bend, OR 97701; after "Save Changes" the row displays "Bend, OR" and the record persists the full new address.

- [X] FT-08: Admin can change a customer's plan choice.
  - Action: Open a customer subscription record, select a different plan from the plan dropdown, and save.
  - Expected: Customer's subscription displays the newly selected plan.
  - Result: Changed Emma Thompson from Premium Box to "Starter Box ($29.99)" via the Plan combobox; after saving, her row shows "Starter Box $29.99/mo".

- [X] FT-09: Admin can view payment history for a customer subscription.
  - Action: Open a customer subscription record and navigate to the payment history section.
  - Expected: A chronological list of past payments is displayed with relevant details.
  - Result: Payment History page lists 8 transactions sortable/filterable per customer; searching "Emma Thompson" shows her payments in chronological order (pay-6 2024-11-15, pay-1 2024-12-15) with amount, plan, and status.

- [X] FT-10: Admin can mark an order as "Prepared" for a billing cycle.
  - Action: Locate an order in the current billing cycle, click the action to mark it as "Prepared".
  - Expected: Order status changes to "Prepared" and is visually indicated.
  - Result: Clicked "Prepare" on ord-2 (Marcus Chen, January 2025, pending); status badge changed to "preparing" (the app's prepared state) with icon, "Preparing" counter updated 2 → 3, and toast "Order marked as preparing" shown.

- [X] FT-11: Admin can mark an order as "Shipped" for a billing cycle.
  - Action: Locate an order that has been prepared, click the action to mark it as "Shipped".
  - Expected: Order status changes to "Shipped" and is visually indicated.
  - Result: Clicked "Ship" on ord-1 (preparing), confirmed "Mark as Shipped" in the Ship Order dialog (with optional tracking number); status badge changed to "shipped", "Shipped" counter 1 → 2, action became "Delivered", toast "Order marked as shipped".

## Constraint

- [X] CS-01: Cannot save a new plan with empty required fields.
  - Action: Attempt to create a new plan leaving the plan name or price empty, then submit.
  - Expected: Form is not saved; a validation error indicates which required fields are missing.
  - Result: Submitting the empty Create Plan form showed the validation toast "Please fill in all required fields", the dialog stayed open, no plan was created, and required fields are marked with asterisks (Plan Name*, Price*, Max Subscribers*).

- [ ] CS-02: Cannot enter a negative value for price or max subscriber count.
  - Action: Attempt to set a plan price or max subscriber count to a negative number (e.g., -10) and submit.
  - Expected: Form is rejected or the field is flagged with a validation error; negative values are not accepted.
  - Bug Report:
    - Issue: Missing input validation (negative values accepted)
    - Actual: Entered Price = −10 and Max Subscribers = −10 in the Create Plan form and clicked "Create Plan"; the plan was saved successfully with toast "Plan created successfully" and a new plan card "Negative Test Plan — $-10 /monthly, Subscribers 0 / -10" appeared in the list. No validation error or field flag was shown. (The junk plan was subsequently deleted.)

- [ ] CS-03: Cannot set max subscriber count below the current number of active subscribers.
  - Action: Select a plan that has active subscribers (e.g., 25), attempt to set the max subscriber count to a number lower than 25, and save.
  - Expected: Change is rejected or blocked with an error message indicating the count cannot be below current subscribers.
  - Bug Report:
    - Issue: Missing business-rule validation (max below current subscribers accepted)
    - Actual: Edited Starter Box (342 current subscribers), set Max Subscribers to 300 (< 342) and clicked "Update Plan"; the change saved with toast "Plan updated successfully" and the card displayed "342 / 300" with no error or warning. (Max was restored to 500 afterward.)

- [X] CS-04: Order must be marked "Prepared" before it can be marked "Shipped".
  - Action: Locate an order that has not been prepared and attempt to mark it as "Shipped".
  - Expected: Action is blocked or an error message indicates the order must be prepared first.
  - Result: Pending orders (e.g., ord-3, Sofia Rodriguez) expose only a "Prepare" action — no "Ship" control exists until the order is prepared, so shipping an unprepared order is structurally blocked by the UI workflow (pending → preparing → shipped).

## Interaction

- [X] IX-01: Success confirmation is displayed after saving a plan.
  - Action: Create or update a plan with valid data and submit.
  - Expected: A success toast or notification appears confirming the plan has been saved.
  - Result: Toast notifications "Plan created successfully" and "Plan updated successfully" appeared immediately after each save.

- [X] IX-02: Order status label updates immediately when marked as prepared or shipped.
  - Action: Click the "Mark as Prepared" or "Mark as Shipped" button on an order in the billing cycle view.
  - Expected: The order's status badge/label changes instantly to reflect the new status without requiring a page refresh.
  - Result: On clicking Prepare/Ship, the row's status badge changed in place instantly ("pending" → "preparing"; "preparing" → "shipped") along with the summary counters, with no page reload.

- [ ] IX-03: Product demand quantities recalculate when a customer's plan is changed.
  - Action: Change a customer's subscription from Plan A to Plan B, then navigate to the product demand/shipment planning section.
  - Expected: Unit quantities for products assigned to Plan A decrease and Plan B's products increase accordingly.
  - Bug Report:
    - Issue: Demand quantities are static and do not recalculate from subscription data
    - Actual: Changed Emma Thompson from Premium Box to Starter Box, then re-checked the Products page: Reserved/Available values were unchanged (Scented Candle Set still 365, Handmade Soap Bar still 420 — no −1/+1 shift), and the plan cards still showed Premium Box 287 / Starter Box 342. The demand figures are seeded static values (e.g., 707) that do not respond to actual subscription changes.

## Content

- [X] CT-01: All displayed plans, products, customers, and orders are directly relevant to the subscription box business.
  - Action: Review the plan list, product inventory, customer subscriptions, and order sections.
  - Expected: All entries are coherent subscription-box business data (e.g., box plans, physical products, customer names, subscription orders); no placeholder or irrelevant content.
  - Result: All content is coherent subscription-box data — 4 box plans (Starter Box, Premium Box, Deluxe Quarterly, Annual VIP) with prices/cycles/capacities, 8 physical products with SKUs/categories/unit prices, 6 realistic customers with addresses and billing dates, 6 orders tied to billing cycles (January 2025, Q1 2025), and 8 matching payments. No lorem-ipsum or placeholder content anywhere.

- [X] CT-02: Payment history entries display relevant and complete details.
  - Action: Open a customer's payment history and review each entry.
  - Expected: Each payment entry shows at minimum the payment date, amount, and payment status (e.g., Paid, Failed); no blank or incomplete records.
  - Result: All 8 payment entries (pay-1 … pay-8) display payment ID, customer, plan, amount, status (completed / failed / refunded), and date — e.g., pay-7 James Wilson $49.99 failed 2024-12-05; pay-8 Marcus Chen $29.99 refunded 2024-11-22. No blank or incomplete records.

**Summary: 17 passed, 3 failed.** The failures are all validation/recalculation gaps: negative values are accepted for plan price/max subscribers (CS-02), max subscriber count can be set below current subscribers (CS-03), and product demand quantities are static seeded numbers that never recalculate when a customer changes plans (IX-03).