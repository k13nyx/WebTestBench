# Test Checklist

## Functionality

- [ ] **FT-01: Open the admin subscription-box management page**
  - **Action:** Open the admin webpage and inspect the available management areas.
  - **Expected:** Controls or sections are available for box plans, recurring billing, inventory, shipping, customer subscriptions, and payments.

- [ ] **FT-02: Configure an existing box plan**
  - **Action:** Edit a default plan using the **Price**, **Billing cycle**, and **Maximum subscribers** fields, then select **Save**.
  - **Expected:** The plan saves successfully and displays the updated price, billing cycle, and subscriber limit.

- [ ] **FT-03: Assign products to an existing plan**
  - **Action:** Open a default plan, select one or more default products in the plan’s product assignment control, and save the plan.
  - **Expected:** The selected products are shown as part of that plan after saving.

- [ ] **FT-04: Review recurring billing information**
  - **Action:** Open the recurring billing area and select an available billing cycle or plan.
  - **Expected:** The page shows the applicable billing frequency and the subscriptions or charges scheduled for that cycle.

- [ ] **FT-05: Review upcoming inventory requirements**
  - **Action:** Open the inventory or upcoming shipments view and select an available billing cycle.
  - **Expected:** Each assigned product displays the total number of units required for upcoming shipments in that cycle.

- [ ] **FT-06: Review customer subscriptions**
  - **Action:** Open the customer subscriptions area and select a default customer subscription.
  - **Expected:** The customer’s current plan, subscription status, address, and billing-cycle information are displayed.

- [ ] **FT-07: Update a customer address**
  - **Action:** Edit the selected customer subscription, replace the shipping address, and select **Save** or **Update**.
  - **Expected:** The new address is saved and displayed when the subscription is reopened.

- [ ] **FT-08: Change a customer’s plan**
  - **Action:** Edit a default customer subscription, select a different available plan in the **Plan** control, and save the change.
  - **Expected:** The customer subscription displays the newly selected plan and its associated billing details.

- [ ] **FT-09: View customer payment history**
  - **Action:** Open the payment history for a default customer subscription.
  - **Expected:** The page displays the customer’s recorded payment entries, including payment date, amount, and payment status.

- [ ] **FT-10: Process orders for a billing cycle**
  - **Action:** Open an available billing cycle’s orders and mark an order **Prepared**, then mark it **Shipped**.
  - **Expected:** The order status changes to **Prepared** and then to **Shipped** for that billing cycle.

## Constraint

- [ ] **CS-01: Require a valid plan price**
  - **Action:** In an existing plan, clear the **Price** field or enter a zero, negative, or non-numeric value, then select **Save**.
  - **Expected:** The plan is not saved, and the price field displays a validation error.

- [ ] **CS-02: Require a billing cycle**
  - **Action:** Clear the **Billing cycle** selection for an existing plan and select **Save**.
  - **Expected:** The plan is not saved, and the billing-cycle control displays a validation error.

- [ ] **CS-03: Enforce the maximum subscriber count**
  - **Action:** Attempt to save a plan with a **Maximum subscribers** value lower than its current subscriber count.
  - **Expected:** The change is rejected, and the plan retains a limit that is not lower than its current subscriber count.

- [ ] **CS-04: Validate the maximum subscriber value**
  - **Action:** Enter zero, a negative value, or non-numeric text in **Maximum subscribers**, then select **Save**.
  - **Expected:** The plan is not saved, and the field displays a validation error.

- [ ] **CS-05: Prevent incomplete customer address updates**
  - **Action:** Edit a customer subscription, remove a required address value, and select **Save** or **Update**.
  - **Expected:** The address update is rejected, and the missing required address field is identified.

- [ ] **CS-06: Keep inventory totals consistent with subscriptions**
  - **Action:** Compare the upcoming shipment quantity for each assigned product with the number of applicable subscribers and the product quantity assigned per box.
  - **Expected:** Each total equals the applicable subscriber count multiplied by the configured per-box product quantity.

## Interaction

- [ ] **IX-01: Open plan editing from the plan list**
  - **Action:** Select a default plan row or its **Edit** control.
  - **Expected:** The plan editor opens with the selected plan’s current price, billing cycle, subscriber limit, and assigned products populated.

- [ ] **IX-02: Confirm successful plan updates**
  - **Action:** Change one editable plan value and select **Save**.
  - **Expected:** A visible success confirmation appears, and the plan list reflects the updated value without requiring duplicate submission.

- [ ] **IX-03: Refresh dependent billing and inventory data**
  - **Action:** Change an existing plan’s billing cycle or assigned products, save it, and reopen the recurring billing and inventory views.
  - **Expected:** The affected billing schedule and upcoming product-unit totals reflect the saved plan configuration.

- [ ] **IX-04: Reflect customer plan changes in subscription details**
  - **Action:** Change a customer’s plan and save the subscription.
  - **Expected:** The subscription detail view immediately shows the new plan and corresponding billing-cycle information.

- [ ] **IX-05: Update shipping status in sequence**
  - **Action:** Select **Prepared** for an order, then select **Shipped** for the same order.
  - **Expected:** Each action visibly updates the order status and the final status is **Shipped**.

## Content

- [ ] **CT-01: Display complete box-plan information**
  - **Action:** Review the default plan list and open at least one plan.
  - **Expected:** Each plan shows a recognizable plan name, price, billing cycle, maximum subscriber count, and assigned products.

- [ ] **CT-02: Display complete subscription information**
  - **Action:** Review a default customer subscription.
  - **Expected:** The displayed customer, address, selected plan, subscription status, and next billing information correspond to the same subscription.

- [ ] **CT-03: Display meaningful payment records**
  - **Action:** Review the payment history for a default customer.
  - **Expected:** Every payment record identifies a date, amount, and status, and the values are associated with the selected customer.

- [ ] **CT-04: Display cycle-specific inventory and shipping data**
  - **Action:** Select an available billing cycle in the inventory and shipping views.
  - **Expected:** Product quantities and order statuses shown belong to the selected billing cycle and are not mixed with another cycle.