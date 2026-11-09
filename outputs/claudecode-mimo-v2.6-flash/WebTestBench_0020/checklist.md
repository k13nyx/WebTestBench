# Test Checklist

## Functionality
- [ ] FT-01: Admin can create a new box plan with a name, price, billing cycle, and maximum subscriber count.
  - Action: Open the plans section, click "Add Plan" (or equivalent), enter a name, price (e.g., 29.99), billing cycle (e.g., Monthly), and max subscribers (e.g., 100), then save.
  - Expected: The new plan is saved and appears in the plan list with all entered values displayed.
- [ ] FT-02: Admin can edit an existing plan's price, billing cycle, or maximum subscriber count.
  - Action: Select an existing plan from the default list, change its price to a new value, and save.
  - Expected: The plan record is updated and the plan list shows the new price.
- [ ] FT-03: Admin can assign specific products to a plan with quantities.
  - Action: Open a plan's product assignment, add a product from the default product catalog with a quantity per box, and save.
  - Expected: The product is listed under the plan with the specified quantity per box.
- [ ] FT-04: Admin can remove an assigned product from a plan.
  - Action: Open a plan's product list, remove one assigned product, and save.
  - Expected: The product no longer appears in that plan's assignment list.
- [ ] FT-05: Admin can view how many units of each product are needed for the upcoming shipment.
  - Action: Open the inventory/shipping requirements view for the current billing cycle.
  - Expected: Each product shows a required unit count reflecting (quantity per box × active subscribers on plans containing that product).
- [ ] FT-06: Admin can view the list of customer subscriptions.
  - Action: Open the subscriptions section using the default data.
  - Expected: A list of subscribers is displayed showing customer name, assigned plan, status, and next billing date.
- [ ] FT-07: Admin can update a subscriber's shipping address.
  - Action: Select a subscriber, edit the address fields to a new address, and save.
  - Expected: The subscriber record displays the newly entered address after saving.
- [ ] FT-08: Admin can change a subscriber's plan choice.
  - Action: Select a subscriber and change their plan to a different plan from the default list, then save.
  - Expected: The subscriber's record now shows the newly selected plan.
- [ ] FT-09: Admin can view a subscriber's payment history.
  - Action: Open the payment history for a subscriber that has default past payments.
  - Expected: A list of past payments is shown with date, amount, billing cycle, and payment status.
- [ ] FT-10: Admin can mark an order as prepared for the current billing cycle.
  - Action: Open the orders/shipping view for the current cycle, select a pending order, and click "Mark as Prepared".
  - Expected: The order's status changes to "Prepared".
- [ ] FT-11: Admin can mark a prepared order as shipped.
  - Action: Select an order with status "Prepared" and click "Mark as Shipped".
  - Expected: The order's status changes to "Shipped".
- [ ] FT-12: Admin can view recurring billing for the current cycle.
  - Action: Open the billing section for the current billing cycle using default subscriptions.
  - Expected: The view lists each active subscriber's upcoming/processed charge with amount matching their plan price and the correct cycle date.

## Constraint
- [ ] CS-01: A plan cannot be saved with an empty or non-positive price.
  - Action: Attempt to create or edit a plan leaving the price blank or entering 0/negative, then save.
  - Expected: Saving is blocked and an error is shown indicating the price is invalid; the plan is not created/modified.
- [ ] CS-02: A plan cannot be saved with an empty billing cycle or maximum subscriber count.
  - Action: Attempt to save a plan with the billing cycle or max subscriber count left empty.
  - Expected: Saving is blocked with a validation error naming the missing required field.
- [ ] CS-03: A new subscription cannot be assigned to a plan that has reached its maximum subscriber count.
  - Action: Identify a plan whose active subscriber count equals its maximum subscriber count, then attempt to assign another customer to it.
  - Expected: The assignment is rejected with an error indicating the plan has reached its subscriber limit.
- [ ] CS-04: An order cannot be marked as shipped unless its current status is "Prepared".
  - Action: Attempt to mark an order with status "Pending" directly as shipped.
  - Expected: The ship action is unavailable or rejected with an error; the order status remains unchanged.
- [ ] CS-05: A subscriber's address cannot be saved with empty required fields (street, city, postal code).
  - Action: Attempt to save an address update after clearing one of the required address fields.
  - Expected: Saving is blocked with an error identifying the empty required field; the stored address is unchanged.

## Interaction
- [ ] IX-01: Saving a plan change provides immediate visible confirmation.
  - Action: Edit a plan's price and save.
  - Expected: A success message/toast confirms the save, and the plan list reflects the new value without a manual refresh.
- [ ] IX-02: Order status changes update instantly and visibly after clicking the status action.
  - Action: Click "Mark as Prepared" on a pending order.
  - Expected: The order's status badge/text updates to "Prepared" immediately, and the available next action becomes "Mark as Shipped".
- [ ] IX-03: Inventory requirement figures refresh after a plan's product assignment or subscriber count changes.
  - Action: Assign an additional product to a plan (or change a subscriber's plan), then view the upcoming shipment requirements.
  - Expected: The required unit counts reflect the change without restarting the page.

## Content
- [ ] CT-01: Plan detail views display exactly the saved price, billing cycle, and maximum subscriber count.
  - Action: Open a plan whose saved values are known from the plan list.
  - Expected: The displayed price, cycle, and max subscriber count exactly match the saved values (e.g., "$29.99", "Monthly", "100").
- [ ] CT-02: Product names shown in a plan's assignment and in the shipment requirements view come from the actual product catalog.
  - Action: Compare products listed under a plan and in the upcoming shipment requirements against the default product catalog.
  - Expected: Every listed product name matches a real catalog product; no placeholder, empty, or duplicate-broken entries appear.
- [ ] CT-03: Payment history entries show coherent dates, amounts, and statuses.
  - Action: Review a subscriber's default payment history.
  - Expected: Each row shows a valid date, an amount equal to the subscriber's plan price for that cycle, and a clear status (e.g., Paid/Failed); no rows have missing or contradictory data.