# Test Result

## Functionality

- [X] FT-01: Admin can create a new box plan by providing name, price, billing cycle, and max subscribers
  - Action: Open the "Plans" section, click "Add Plan", enter name = "Test Box", price = "29.99", billing cycle = "Monthly", max subscribers = "50", and save.
  - Expected: The new plan "Test Box" appears in the plan list showing $29.99, "Monthly" cycle, and a max of 50 subscribers.
  - Verified: New card "Test Box" rendered with "$29.99", "/monthly", "Subscribers 0 / 50" after clicking "New Plan" → Create.

- [X] FT-02: Admin can assign products to a specific plan
  - Action: Open an existing plan's edit view, add one default product to the plan's contents, and save.
  - Expected: The added product is listed under that plan's "Products"/"Contents" and persists after reopening the plan.
  - Verified: Added "Premium Coffee Beans" to Starter Box via Edit Plan; card shows "Products (4)"; reopening the edit dialog shows the coffee-beans checkbox still `[checked]`.

- [ ] FT-03: Inventory report shows units of each product needed for upcoming shipments
  - Action: Open the "Inventory" section and view the "Needed for upcoming shipments" figures.
  - Expected: Each product row displays a required-unit count computed from active subscriptions, and on-hand stock level is shown alongside it.
  - Bug Report:
    - Issue: Missing computed report / static mock data (Inventory = "Products & Inventory" page)
    - Actual: No "Needed for upcoming shipments" label exists; only a "Reserved" column is shown. The Reserved figures are hardcoded mock values that are NOT computed from active subscriptions: after "Premium Coffee Beans" was assigned to Starter Box (342 subscribers), Coffee's Reserved stayed 365 and its "Used In Plans" cell did not list Starter Box; values also did not change after a live subscription plan switch. On-hand "Stock" is displayed, but the required-unit count is not derived from subscription data as specified.

- [ ] FT-04: Admin can review the list of customer subscriptions
  - Action: Open the "Subscriptions" section.
  - Expected: A table lists each customer with their plan, current status (e.g., Active), and billing cycle.
  - Bug Report:
    - Issue: Incorrect billing-cycle display in subscriptions table
    - Actual: The Subscribers table lists customers with Plan, Status, and Address, but the billing cycle is rendered as "/mo" for every row regardless of the plan's real cycle: "Deluxe Quarterly $149.99/mo" (actual cycle: quarterly) and "Annual VIP $499.99/mo" (actual cycle: yearly). There is no dedicated billing-cycle column; only "Next Billing" dates are shown.

- [X] FT-05: Admin can update a customer's shipping address
  - Action: Select a default customer's subscription, edit the address fields, and save.
  - Expected: The saved new address is reflected in that customer's subscription record.
  - Verified: Emma Thompson's address fields changed (Street "456 Elm Street", City "Eugene", ZIP "97401"); after "Save Changes" ("Subscriber updated successfully"), the row's Address cell shows "Eugene, OR".

- [X] FT-06: Admin can change a customer's plan choice
  - Action: Edit a default customer's subscription and switch its plan to another existing plan, then save.
  - Expected: The customer's subscription now shows the newly selected plan name.
  - Verified: Marcus Chen switched from Starter Box to Premium Box via the Plan combobox; row now reads "Premium Box $49.99/mo". (Side note: the dropdown offered only the 4 default plans — the newly created "Test Box" was missing from the list.)

- [X] FT-07: Admin can view payment history for a customer subscription
  - Action: Open the "Payment History" view for a default active customer.
  - Expected: A list of past payments is shown, each with an amount and a date.
  - Verified: The "Payment History" page lists 8 transactions with columns Payment ID / Customer / Plan / Amount / Status / Date; e.g., Emma Thompson: pay-1 $49.99 on 2024-12-15 and pay-6 $49.99 on 2024-11-15 (customer search box available to filter by customer).

- [ ] FT-08: Admin can select a billing cycle to organize shipping orders
  - Action: Open the "Shipping" section and select an upcoming billing cycle from the cycle selector.
  - Expected: The order list filters to show only the orders belonging to that billing cycle.
  - Bug Report:
    - Issue: Missing control — no billing cycle selector exists
    - Actual: The Orders & Fulfillment page ("Shipping" equivalent) offers only a free-text search ("Search by customer or order ID...") and an "All Statuses" status-filter combobox. There is no billing-cycle selector/dropdown anywhere on the page, so the order list cannot be filtered to a billing cycle (cycles "January 2025", "Q1 2025", "2025", "December 2024" appear only as static column values).

- [X] FT-09: Admin can mark an order as "Prepared" for a billing cycle
  - Action: In the "Shipping" section, on a default order click the "Mark Prepared" (or status → "Prepared") action.
  - Expected: That order's status changes to "Prepared".
  - Verified: ord-2 (Marcus Chen) "Prepare" button clicked → toast "Order marked as preparing", status badge changed to "preparing" (app's label for the Prepared state), and the action button became "Ship".

- [X] FT-10: Admin can mark a prepared order as "Shipped" for a billing cycle
  - Action: On an order whose status is "Prepared", click the "Mark Shipped" (or status → "Shipped") action.
  - Expected: That order's status changes to "Shipped".
  - Verified: On the now-"preparing" ord-2, "Ship" opened the "Ship Order" dialog; clicking "Mark as Shipped" produced toast "Order marked as shipped" and the row's status badge became "shipped" with the action changing to "Delivered".

## Constraint

- [ ] CS-01: A plan cannot be saved with an invalid max subscriber count below its current subscriber count
  - Action: Edit a plan that has existing subscribers and set "Max Subscribers" to a value lower than its current active subscriber count, then save.
  - Expected: The save is rejected with a validation error and the plan's max is not decreased below the current count.
  - Bug Report:
    - Issue: Missing validation — invalid max-subscriber value accepted
    - Actual: Starter Box has 342 subscribers; setting Max Subscribers to 100 and clicking "Update Plan" succeeded with toast "Plan updated successfully" and the card persisted as "Subscribers 342 / 100" (max stayed 100 on reopening the edit dialog). No validation error was shown and the max was decreased below the current count.

- [ ] CS-02: Required plan fields must be valid before a plan is accepted
  - Action: Click "Add Plan" and attempt to save with the name empty or the price negative/non-numeric.
  - Expected: The form is rejected with a validation message identifying the offending field; no plan is created.
  - Bug Report:
    - Issue: Missing price validation — negative price accepted
    - Actual: Empty-name submission was blocked, but only with a generic toast "Please fill in all required fields" (no field-level/identifying message; no `aria-invalid` on inputs). A plan with price "-5" was accepted: creating plan "Tmp" with Price = -5 succeeded ("Plan created successfully", card displayed "$-5"), proving required plan fields are not validated before acceptance.

- [X] CS-03: An order cannot be marked "Shipped" before it is "Prepared"
  - Action: On an order still in the default "Pending"/"New" status, attempt to set status directly to "Shipped".
  - Expected: The action is blocked (control disabled or error) so an unprepared order cannot jump to "Shipped".
  - Verified: Pending orders (ord-2 initially, ord-3 still pending) show only a "Prepare" action button — no "Ship"/status-editor control exists in the row; the "Ship" control appears only after the status becomes "preparing", so a direct pending→shipped jump is impossible.

- [X] CS-04: A product can only be assigned to a plan from the existing inventory catalog
  - Action: Open a plan's product-assignment control and attempt to assign a product that does not exist in the catalog.
  - Expected: Only catalog products are selectable/assignable; the nonexistent product cannot be added to the plan.
  - Verified: The "Products in Box" control in the Create/Edit Plan dialog is a fixed checkbox list of exactly the 8 catalog products (Artisan Chocolate Bar … Exclusive Wine Selection). There is no free-text/combobox input anywhere in the section, so a nonexistent product cannot be entered or assigned.

## Interaction

- [X] IX-01: The interface provides navigation between the major admin sections
  - Action: Use the top-level navigation/tabs to move between "Plans", "Inventory", "Subscriptions", and "Shipping".
  - Expected: Selecting each section loads its corresponding view and highlights the active section.
  - Verified: Sidebar navigation loads "Box Plans" (/plans), "Products & Inventory" (/products), "Subscribers" (/subscriptions→/subscribers), and "Orders & Fulfillment" (/orders) views; the selected link is marked `[active]` in the accessibility tree on each page (Payments also verified).

- [X] IX-02: A plan's subscriber count / capacity updates immediately after editing its settings
  - Action: Change a plan's max-subscriber value in "Plans" and return to the plan list.
  - Expected: The plan card/row refreshes to display the new max and current-subscriber figures without a manual reload.
  - Verified: Setting Starter Box max to 600 and saving auto-closed the dialog and the card instantly re-rendered as "Subscribers 342 / 600" with no page reload (also observed 342/500 → 342/100 earlier).

- [ ] IX-03: The inventory "needed" total reflects subscription changes
  - Action: Note the "Needed for upcoming shipments" count for a product, then add/remove an active subscription on that product's plan and re-check.
  - Expected: The product's required-unit count increases or decreases accordingly.
  - Bug Report:
    - Issue: Stale/static inventory figures — no recalculation on subscription change
    - Actual: Baseline Reserved counts were Chocolate 707 / Soap 420. After moving Marcus Chen (active) out of Starter Box into Premium Box, re-checking the Inventory page showed unchanged figures (Chocolate still 707, Soap still 420, Coffee still 365). The counts also ignored the plan-product assignment made in FT-02, proving the "needed" numbers are static mock values, not recomputed from subscriptions.

- [X] IX-04: The order list reflects status changes in real time
  - Action: Mark an order "Shipped" in the "Shipping" section.
  - Expected: The order's status badge updates to "Shipped" in the list immediately and its position/count in any "prepared"/"shipped" summary changes.
  - Verified: After "Mark as Shipped", ord-2's badge updated to "shipped" instantly in the same list, its action became "Delivered", and the summary tiles recomputed live (Preparing 3→2, Shipped 1→2) without a reload.

## Content

- [X] CT-01: Default plans, products, and customer subscription data are present and internally consistent
  - Action: Load the app and inspect the "Plans", "Inventory", and "Subscriptions" sections.
  - Expected: Pre-existing plans, catalog products, and customer subscriptions are populated (not empty), with relevant subscription-box content.
  - Verified: 4 default plans (Starter Box $29.99/mo, Premium Box $49.99/mo, Deluxe Quarterly $149.99/quarterly, Annual VIP $499.99/yr) with descriptions/prices/product lists; 8 catalog products with SKUs, categories, stock, prices; 6 customer subscriptions (5 active, 1 paused) with plans, addresses, and billing dates — all populated with subscription-box content. (Note: dashboard/plan "subscriberCount" aggregates like 342/500 are seed metadata and exceed the 6 listed rows, but section content itself is present and non-empty.)

- [X] CT-02: Payment history amounts match the corresponding plan price
  - Action: Open the payment history for a default customer and compare the recorded charge amount to the price of that customer's plan.
  - Expected: Each payment amount equals the plan's configured price for its billing cycle.
  - Verified: Every one of the 8 payments equals its plan's configured price — Premium Box $49.99 (pay-1, pay-6, pay-7), Starter Box $29.99 (pay-2, pay-4, pay-8), Deluxe Quarterly $149.99 (pay-3), Annual VIP $499.99 (pay-5).
