# Test Checklist

## Functionality
- [ ] FT-01: Admin can edit a plan's price, billing cycle, and maximum subscriber count.
  - Action: Open the Plans page, click a plan, change Price, Billing Cycle, and Max Subscribers, then click Save. Reopen the plan.
  - Expected: The plan shows the new price, billing cycle, and max subscriber count.
- [ ] FT-02: Admin can add and remove products on a plan.
  - Action: Open a plan's Products section, add one product not currently assigned, remove one assigned product, then Save and reopen the plan.
  - Expected: The added product appears in the plan's product list, and the removed product no longer appears.
- [ ] FT-03: Upcoming shipment forecast shows correct unit counts per product.
  - Action: Open the Shipments page and select the next upcoming billing cycle. Note each plan's active subscriber count and the products assigned to it.
  - Expected: For each product, the units needed equal the sum over plans containing that product of (active subscribers on that plan × quantity of that product per box).
- [ ] FT-04: Inventory page shows on-hand stock and units required for upcoming shipments.
  - Action: Open the Inventory page and locate any product with an on-hand value and a required value.
  - Expected: Each product lists an on-hand quantity and the units required for upcoming shipments, and any product where required exceeds on-hand is marked as short.
- [ ] FT-05: Admin can pause a subscription's recurring billing.
  - Action: Search for an active subscriber by name, open the subscription, click Pause Subscription, and confirm.
  - Expected: Subscription status shows Paused, and the subscriber's units are excluded from the next cycle's forecast (FT-03).
- [ ] FT-06: Admin can update a subscriber's shipping address.
  - Action: Search for a subscriber by name, open the subscription, change Street, City, and Postal Code, then Save. Reopen the subscription.
  - Expected: The new address is displayed on the subscription and is used for that subscriber's next pending order.
- [ ] FT-07: Admin can change a subscriber's plan, and the new plan applies to the next billing.
  - Action: Open an active subscription, change Plan to a different plan with available capacity, then Save.
  - Expected: The subscription shows the new plan, and the next billing charge uses the new plan's price.
- [ ] FT-08: Subscription payment history lists all past charges.
  - Action: Open a subscriber with existing charges and open the Payment History tab.
  - Expected: Each charge shows date, billing cycle, amount, and status, sorted newest first.
- [ ] FT-09: Admin can mark an order as Prepared for a billing cycle.
  - Action: On the Shipments page with a billing cycle selected, click Mark Prepared on a Pending order.
  - Expected: The order's status changes to Prepared, and the prepared date is recorded.
- [ ] FT-10: Admin can mark a prepared order as Shipped.
  - Action: On a Prepared order, click Mark Shipped.
  - Expected: The order's status changes to Shipped, and the shipped date is recorded.

## Constraint
- [ ] CS-01: Plan price must be greater than zero, and a billing cycle must be selected.
  - Action: On a plan, enter 0 or -5 as Price, clear Billing Cycle, and click Save.
  - Expected: Save is blocked, the invalid fields are highlighted with an error message, and the plan remains unchanged.
- [ ] CS-02: Max subscribers cannot be set below the plan's current active subscriber count.
  - Action: Open a plan with active subscribers, enter a Max Subscribers value lower than its active count, and click Save.
  - Expected: Save is blocked with a message stating the minimum allowed value, and the plan remains unchanged.
- [ ] CS-03: A subscriber cannot be moved to a plan that is at its maximum subscriber count.
  - Action: Open an active subscription and change Plan to a plan whose active count equals its max.
  - Expected: The full plan is unavailable for selection or Save is blocked with a "plan is full" message, and the subscription keeps its original plan.
- [ ] CS-04: Address cannot be saved with a required field empty.
  - Action: Open a subscription, clear Street or Postal Code, and click Save.
  - Expected: Save is blocked, the empty field is flagged as required, and the original address is kept.
- [ ] CS-05: An order cannot be marked Shipped before it is Prepared.
  - Action: On a Pending order, attempt to click Mark Shipped.
  - Expected: The action is unavailable (disabled) or is rejected with a message, and the order remains Pending.

## Interaction
- [ ] IX-01: A success confirmation appears after each successful save and then dismisses.
  - Action: Save a valid change to a plan, a subscription plan, or an address.
  - Expected: A green confirmation message reading "Saved successfully" appears near the top of the page and disappears within about 5 seconds.
- [ ] IX-02: Marking an order status shows a confirmation step that can be cancelled.
  - Action: Click Mark Prepared on a Pending order, then click Cancel in the confirmation dialog. Repeat and click Confirm.
  - Expected: Cancel closes the dialog and the status stays Pending. Confirm closes the dialog and changes the status to Prepared.
- [ ] IX-03: Changing the billing cycle selector refreshes the order list and unit totals.
  - Action: On the Shipments page, select a different billing cycle from the dropdown.
  - Expected: The order list and the per-product unit totals update to show only the selected cycle, without a full page reload.

## Content
- [ ] CT-01: Plan list values match the configured plan data and subscriber counts.
  - Action: Open the Plans list and compare each plan's name, price, billing cycle, and subscriber count with that plan's detail page.
  - Expected: Values match on both pages, and the subscriber count shows Active / Max (for example, 42 / 50) with Active equal to the number of active subscriptions on that plan.
- [ ] CT-02: Payment history amounts match the plan price for each billing date.
  - Action: Open a subscriber's Payment History and compare each charge amount with the price of the plan active on that billing date.
  - Expected: Each amount matches the plan price in effect on that date, with currency formatted consistently, and every status label is one of Paid, Failed, or Refunded.