All checklist items have been executed. Here are the complete results:

# Test Result

## Functionality
- [X] FT-01: Admin can create a new box plan with name, price, billing cycle, and max subscriber count
  - Action: Open the plan configuration section, create a new plan (e.g., name "Monthly Box", price $29.99, billing cycle "Monthly", max subscribers 100) and save it.
  - Expected: The new plan appears in the plans list showing the entered name, price, billing cycle, and max subscriber count.

- [X] FT-02: Admin can edit an existing plan's price and settings
  - Action: Select an existing default plan, change its price to a new value, and save.
  - Expected: The plan list/detail now displays the updated price.

- [X] FT-03: Admin can assign products to a plan
  - Action: Open a plan, add one or more existing products from the product list to it, and save.
  - Expected: The assigned products are listed under that plan.

- [X] FT-04: Admin can review the list of customer subscriptions
  - Action: Open the customer subscriptions section.
  - Expected: Existing customers are listed with their subscribed plan and subscription status visible.

- [X] FT-05: Admin can update a customer's shipping address
  - Action: Open a customer's subscription, edit the address fields (street, city, ZIP, etc.), and save.
  - Expected: The customer's record shows the new address after saving.

- [X] FT-06: Admin can change a customer's plan choice
  - Action: Open a customer's subscription, select a different existing plan, and save.
  - Expected: The customer's subscription now shows the newly selected plan.

- [X] FT-07: Admin can view a customer's payment history
  - Action: Open a customer's record and view the payment history section.
  - Expected: Past payments are listed with at least an amount and a date for each entry.

- [X] FT-08: Admin can mark an order as prepared for a billing cycle
  - Action: Open the orders/shipping section for the current billing cycle and click "Prepare" (or equivalent) on a pending order.
  - Expected: The order's status changes to "Prepared".

- [X] FT-09: Admin can mark a prepared order as shipped
  - Action: On an order already marked "Prepared", click "Ship" (or equivalent).
  - Expected: The order's status changes to "Shipped".

- [X] FT-10: Admin can view inventory levels for each product
  - Action: Open the inventory section.
  - Expected: Each product is displayed with its current units-in-stock count.

- [X] FT-11: Admin can see how many units of each product are needed for upcoming shipments
  - Action: Open the upcoming shipments / requirements view.
  - Expected: A list shows each product with the number of units required, consistent with the products assigned to active subscriber plans.

## Constraint
- [X] CS-01: Plan cannot be saved with empty required fields
  - Action: Open the new plan form, leave name or price empty, and attempt to save.
  - Expected: The plan is not saved and a validation error is shown for the empty field(s).

- [ ] CS-02: Plan cannot be saved with a negative price
  - Action: Enter a negative value (e.g., -5) in the price field of the plan form and attempt to save.
  - Expected: The plan is not saved and an invalid-price error is shown.
  - Bug Report:
    - Issue: Missing Input Validation (negative price accepted)
    - Actual: A plan named "Negative Test" with price -5 was saved successfully — a "Plan created successfully" toast appeared and the plan card rendered as "$-5 /monthly" in the plans list. No validation error was shown.

- [ ] CS-03: Customer address cannot be saved with empty required fields
  - Action: Clear a required address field (e.g., street or city) on a customer's address and attempt to save.
  - Expected: The address is not saved and a validation error is shown.
  - Bug Report:
    - Issue: Missing Input Validation (empty required address field accepted)
    - Actual: Clearing the City field on Emma Thompson's address and clicking "Save Changes" produced a "Subscriber updated successfully" toast; the subscribers list then showed the address as ", OR" with a blank city. No validation error was shown.

- [X] CS-04: Order cannot be marked "Shipped" before being "Prepared"
  - Action: On an order whose status is still pending/not prepared, attempt to mark it as shipped directly.
  - Expected: The action is blocked (no "Ship" option available or an error is shown) and the status remains unchanged.

## Interaction
- [X] IX-01: Saving a plan shows visible success feedback
  - Action: Save a valid plan (new or edited).
  - Expected: A success message, toast, or visual confirmation appears after saving.

- [X] IX-02: Order status change reflects immediately without page reload
  - Action: Mark an order as prepared or shipped and observe the orders list.
  - Expected: The status label updates immediately in the list view.

## Content
- [X] CT-01: Inventory display shows product names with numeric stock quantities
  - Action: Inspect the inventory section.
  - Expected: Every listed product has a readable product name and a numeric quantity (not blank, "N/A", or placeholder text).

- [X] CT-02: Payment history entries show relevant billing details
  - Action: Inspect a customer's payment history entries.
  - Expected: Each entry shows a monetary amount and a date; entries correspond to subscription billing (no empty or unrelated records).

---

**Summary**: 17 of 19 tests passed. The two failures are both missing-validation bugs (CS-02: negative plan price is accepted and saved; CS-03: empty required address fields are accepted and saved). The invalid "-5 price" test plan created during CS-02 testing was deleted to restore clean state; all other test data changes (Monthly Box plan, Starter Box price $34.99 + added product, Emma Thompson's address/plan updates, ord-2 prepared → shipped) persist as side effects of the executed tests.