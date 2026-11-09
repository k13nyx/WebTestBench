All test executions are complete. The CS-02/CS-03 run was conclusive: price `0` and `-5` were both saved (only empty was rejected with "Please fill in all required fields"), and creating a plan without ever touching the billing cycle succeeded ("Plan created successfully") since the cycle selector defaults to "Monthly" with no empty option. Here is the full updated checklist:

# Test Result

## Functionality
- [X] FT-01: Create a new box plan with name, price, and billing cycle.
  - Action: Open the plan configuration section, click "Add Plan" (or equivalent), enter plan name, price, and select a billing cycle; save.
  - Expected: The new plan appears in the plan list with the entered name, price, and billing cycle.

- [X] FT-02: Edit an existing plan's price, billing cycle, and maximum subscriber count.
  - Action: Open an existing plan from the plan list, change its price, billing cycle, and max subscriber count; save.
  - Expected: The plan list shows the updated values for that plan after saving.

- [ ] FT-03: Assign specific products with quantities to a plan.
  - Action: Open a plan, add existing products to it with a quantity per product; save.
  - Expected: The plan's product assignment shows each selected product with its assigned quantity.
  - Bug Report:
    - Issue: Missing Quantity Input for Plan Product Assignment
    - Actual: The plan's "Products in Box" editor is checkbox-only — a full input inspection of the plan dialog found only Plan Name, Price, Description, Max Subscribers, and 8 product checkboxes, with no quantity field. After saving, the plan card shows "Products (2): Artisan Chocolate Bar, Organic Tea Sampler" with product names only; no quantity can be entered or displayed.

- [X] FT-04: View units of each product needed for upcoming shipments.
  - Action: Open the inventory / shipment needs view showing upcoming shipments.
  - Expected: Each product is listed with the total number of units needed for the upcoming shipment(s).

- [X] FT-05: Review the list of customer subscriptions.
  - Action: Open the customer subscriptions section.
  - Expected: A list of subscriptions is displayed, each showing the customer and their current plan.

- [X] FT-06: Update a customer's shipping address.
  - Action: Open an existing subscription, edit the shipping address fields; save.
  - Expected: The subscription record shows the new address after saving.

- [X] FT-07: Change a customer's plan choice.
  - Action: Open an existing subscription, select a different plan from the plan options; save.
  - Expected: The subscription record shows the newly selected plan after saving.

- [X] FT-08: View a customer's payment history.
  - Action: Open an existing subscription and view its payment history.
  - Expected: Past payments for that customer are listed.

- [X] FT-09: Mark an order as prepared for a billing cycle.
  - Action: In the orders view for the current billing cycle, click "Mark as Prepared" on an order.
  - Expected: The order's status changes to Prepared.

- [X] FT-10: Mark an order as shipped for a billing cycle.
  - Action: In the orders view for the current billing cycle, click "Mark as Shipped" on a prepared order.
  - Expected: The order's status changes to Shipped.

## Constraint
- [ ] CS-01: A plan cannot accept subscribers beyond its maximum subscriber count.
  - Action: Attempt to assign a new customer subscription to a plan whose current subscriber count equals its maximum.
  - Expected: The action is rejected and the subscriber count does not exceed the maximum.
  - Bug Report:
    - Issue: Subscriber Limit Not Enforced on Plan Assignment
    - Actual: With Premium Box verified at its maximum ("Subscribers 287 / 287" on the plan card after setting max = 287), saving a subscription's plan change to Premium Box succeeded without any rejection — toast "Subscriber updated successfully", and the subscription record now shows "Premium Box $49.99/mo". (Note: the app offers no flow to create a new customer subscription at all; the plan-assignment path was used as the equivalent action.)

- [ ] CS-02: Plan price cannot be invalid (empty, zero, negative, or non-numeric).
  - Action: Enter an empty, 0, negative, or non-numeric value in the plan price field and save.
  - Expected: The save is rejected with an error; the plan keeps its previous price.
  - Bug Report:
    - Issue: Invalid Plan Price Accepted
    - Actual: Price "0" was saved with toast "Plan updated successfully" and the plan list then displayed "$0"; price "-5" was also saved with toast "Plan updated successfully" (plan price becomes negative). The plan did not keep its previous price ($29.99) in either case. Only the empty price was rejected ("Please fill in all required fields", dialog kept open).

- [ ] CS-03: Plan must have a billing cycle selected before saving.
  - Action: Create or edit a plan leaving the billing cycle empty/unselected and save.
  - Expected: The save is rejected with an error indicating billing cycle is required.
  - Bug Report:
    - Issue: Billing Cycle Requirement Not Enforced (No Required-Field Rejection)
    - Actual: The Billing Cycle selector cannot be left empty/unselected — it is pre-set to "Monthly" (marked selected in the dropdown) and offers only Monthly/Quarterly/Yearly with no empty option. Creating a plan without ever touching the billing cycle succeeded — toast "Plan created successfully" and the plan appeared in the list — instead of being rejected with an error indicating billing cycle is required.

- [ ] CS-04: Product quantity assigned to a plan cannot be zero, negative, or empty.
  - Action: Assign a product to a plan with quantity 0, a negative number, or left empty; save.
  - Expected: The save is rejected with an error; the invalid assignment is not stored.
  - Bug Report:
    - Issue: Missing Quantity Field — Invalid-Quantity Validation Cannot Occur
    - Actual: The plan's product assignment has no quantity input whatsoever (checkbox-only list; product editor also has no plan-quantity setting). Quantities of 0, negative, or empty cannot be entered, the save cannot be rejected on quantity grounds, and assignments are stored with no quantity at all ("Products (2)" shows product names only).

- [X] CS-05: An order cannot be marked as shipped before it is marked as prepared.
  - Action: On an order with a pending (not prepared) status, click "Mark as Shipped".
  - Expected: The action is rejected; the order status remains pending.

## Interaction
- [X] IX-01: Order status change is reflected immediately in the orders view.
  - Action: Mark an order as Prepared (then Shipped) and observe the orders list without reloading the page.
  - Expected: The order's status indicator updates immediately to the new status in the list.

- [X] IX-02: Confirmation feedback is shown after saving plan or subscription changes.
  - Action: Save a plan edit (or a subscription address/plan change) and observe the page.
  - Expected: A visible success confirmation (e.g., toast or inline message) appears after the save.

## Content
- [X] CT-01: Plan list displays name, price, billing cycle, and current vs. maximum subscriber count.
  - Action: View the plan list.
  - Expected: Each plan row shows its name, price, billing cycle, and subscriber count against its maximum.

- [X] CT-02: Shipment needs view shows product names with required unit counts.
  - Action: View the upcoming-shipment inventory needs.
  - Expected: Each listed product shows its product name and the number of units needed.

- [X] CT-03: Payment history entries show date, amount, and payment status.
  - Action: View a customer's payment history.
  - Expected: Each payment entry displays its date, amount, and status (e.g., paid/failed).

---

**Notes on evidence gathered during execution:**

- **CS-05 PASS rationale:** pending orders (e.g., ord-3) expose only a "Prepare" button — no ship/Mark-as-Shipped affordance exists on them (verified via button inspection; clicking the row opens no detail dialog). Shipping before preparing is therefore impossible and the order status remains pending, satisfying the constraint (enforced by unavailability rather than by an error message).
- **FT-09/FT-10 mapping:** the app's "Prepare" button is the "Mark as Prepared" equivalent — it moves the order from `pending` to the app's prepared-state badge `preparing` and enables the "Ship" action (toast: "Order marked as preparing"); the Ship dialog's "Mark as Shipped" button then sets status `shipped` (toast: "Order marked as shipped"). Both transitions updated the list instantly without reload (IX-01).
- **FT-04/CT-02 mapping:** the shipment-needs data is the "Reserved" column on the Products & Inventory page (e.g., Artisan Chocolate Bar 707 units, Scented Candle Set 365 units), which equals the sum of subscribers across plans containing each product — the total units needed for upcoming shipments.
- **FT-08 mapping:** payment history per customer is presented on the dedicated "Payment History" page (e.g., Emma Thompson: pay-1 $49.99 completed 2024-12-15, pay-6 $49.99 completed 2024-11-15), rather than inside the subscription dialog.
- **Environment caveat:** the app's data state is not persistent — it silently reset to seed data multiple times mid-session (e.g., the created "QA Test Plan" vanished after navigation). All results above were verified immediately at the moment of each action in the same page session, so the recorded pass/fail behaviors were directly observed; the resets were not counted against any checklist item since persistence is not part of the checklist.