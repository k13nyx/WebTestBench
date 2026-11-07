# Test Result

## Functionality

- [X] FT-01: Admin can create a new box plan with name, price, billing cycle, and max subscriber count
  - Action: Open the Plans section, click the plan creation control (e.g. "New Plan"/"Add Plan"), fill in name, price, billing cycle, max subscribers, and save.
  - Expected: The new plan appears in the plan list showing the exact name, price, billing cycle, and max subscriber count that were entered.

- [X] FT-02: Existing (default) box plans are listed with their price, billing cycle, and subscriber count vs. max
  - Action: Open the Plans section without creating anything.
  - Expected: Every pre-existing plan is listed, each row showing its name, price, billing cycle, and current subscriber count against its maximum (e.g. "3 / 10").

- [X] FT-03: Admin can edit an existing plan's price, billing cycle, and max subscriber count
  - Action: Select a default plan, open its edit view, change the price, change the billing cycle, change the max subscriber count, and save.
  - Expected: The plan row and plan detail now display the new price, new billing cycle, and new max subscriber count; the old values are gone.

- [X] FT-04: Admin can assign specific products to a plan
  - Action: Open a default plan's product assignment area, select/add at least one product from the product list, and save.
  - Expected: The assigned product(s) are listed under that plan, and the same products are not shown as unassigned/available for that plan.

- [X] FT-05: Admin can view current inventory levels per product
  - Action: Open the Inventory section.
  - Expected: Each product row shows the product name and its stock-on-hand quantity as a number.

- [X] FT-06: Admin can see how many units of each product are needed for upcoming shipments
  - Action: Open the inventory or shipment-planning view for the upcoming/next billing cycle.
  - Expected: Each product row shows a "units needed" figure; the figure for any product equals (units per box × number of active subscribers on plans containing that product).

- [X] FT-07: Admin can review the list of customer subscriptions
  - Action: Open the Subscriptions/Customers section.
  - Expected: Each subscription row shows the customer name, their plan, and a subscription status (e.g. Active/Paused).

- [X] FT-08: Admin can update a customer's shipping address and their plan choice
  - Action: Open a default customer's subscription, edit street/city/zip fields, change the plan to a different existing plan, and save.
  - Expected: The customer record shows the new address values and the newly selected plan after saving.

- [X] FT-09: Admin can view a customer's payment history
  - Action: Open a default customer's subscription detail and locate the payment history area.
  - Expected: At least one payment entry is shown with a date, an amount, and a status (e.g. Paid/Failed).

- [X] FT-10: Admin can view orders for a billing cycle and mark them Prepared, then Shipped
  - Action: Open the Shipping/Orders section, select a billing cycle, open one order, mark it Prepared, then mark it Shipped.
  - Expected: Orders for the selected cycle are listed, and the order's status reads "Prepared" after the first action and "Shipped" after the second.

## Constraint

- [ ] CS-01: A plan cannot be saved with a missing, zero, or negative price, or with no billing cycle selected
  - Action: Attempt to save a new plan with price blank (then repeat with 0, then with -5, then with no billing cycle chosen).
  - Expected: Each attempt is blocked — the plan is not added to the list and an inline validation message appears on the offending field.
  - Bug Report:
    - Issue: Missing numeric range validation and missing inline field validation
    - Actual: Price blank was blocked (toast "Please fill in all required fields"), but price "0" was accepted — a plan named "Blank Price Plan" was created and rendered as "$0" in the plan list. Price "-5" was also accepted — "Neg Price Plan" was created and rendered as "$-5". In both blocked and unblocked cases no inline validation message appeared on the Price field; the only feedback was a transient toast. Additionally, "no billing cycle chosen" is not reproducible: the Billing Cycle dropdown is pre-seeded with "Monthly" and offers only Monthly/Quarterly/Yearly, so it can never be left unselected.

- [ ] CS-02: A plan cannot exceed its maximum subscriber count
  - Action: Set a plan's max subscriber count below its current subscriber count (or to equal it), save, then attempt to add/assign another subscriber to that plan.
  - Expected: The plan is marked full/at capacity and the new subscriber assignment is refused with a capacity message; subscriber count never exceeds the max.
  - Bug Report:
    - Issue: No capacity enforcement on max subscriber count
    - Actual: Editing "Starter Box" (342 current subscribers) and setting Max Subscribers to 300 was accepted with the toast "Plan updated successfully"; the plan card then displayed "342 / 300" — subscriber count exceeds the max. The plan was not marked full/at capacity (badge still reads "Active"; no "Full" indicator, no warning). The Plan dropdown in Edit Subscriber listed "Starter Box ($29.99)" as a normal, enabled option with no capacity annotation; assigning Emma Thompson to it saved successfully with "Subscriber updated successfully" and no capacity message.

- [ ] CS-03: A customer address cannot be saved with required fields left empty
  - Action: Open a default customer, clear the street (or city/zip) field, and save.
  - Expected: The save is blocked, the previous address is retained, and a validation message is shown on the empty required field.
  - Bug Report:
    - Issue: Missing required-field validation on shipping address
    - Actual: Clearing the "Street" field for Emma Thompson (previously "456 Pine Avenue") and clicking "Save Changes" was accepted — toast read "Subscriber updated successfully", the dialog closed, and no validation message was shown. Reopening the subscriber confirmed Street is now empty; the previous value was not retained.

- [X] CS-04: Inventory shortfall is flagged when units needed exceeds stock on hand
  - Action: In the inventory/shipment-planning view, identify or create a product where units needed for the upcoming cycle is greater than stock on hand.
  - Expected: That product row is visibly flagged as insufficient/short (e.g. "Short 5" or a shortage warning), and the shortfall equals units needed minus stock on hand.

## Interaction

- [X] IX-01: A confirmation message appears after a plan is created or edited
  - Action: Complete a successful plan save (create or edit).
  - Expected: A success confirmation (toast/inline message) appears stating the plan was saved; it does not say an error occurred.

- [X] IX-02: Marking an order Prepared or Shipped updates its status in place, without a page reload
  - Action: In the Shipping/Orders list, click the "Prepared" action on a pending order, then the "Shipped" action, without navigating away or refreshing.
  - Expected: The status badge/label on that same order row changes immediately to "Prepared" then "Shipped" while the list stays on screen.

- [ ] IX-03: Changing the selected billing cycle refreshes the displayed orders and the units-needed figures
  - Action: In the Shipping/Orders view, select billing cycle A, note the orders and units-needed numbers, then switch to billing cycle B.
  - Expected: Both the order list and the per-product units-needed figures update to reflect the newly selected cycle (at least one value differs or the list is clearly labeled for the new cycle).
  - Bug Report:
    - Issue: Missing billing-cycle selector in the Orders view
    - Actual: The Orders & Fulfillment view exposes exactly one dropdown, "All Statuses" (verified via DOM: the only `[role=combobox]` on the page reads "All Statuses"). There is no control for selecting billing cycle A or B — orders for all cycles ("January 2025", "Q1 2025", "2025", "December 2024") are shown together in one unfiltered table. Additionally the Orders view contains no per-product units-needed figures at all (page text contains no "units needed" string); those figures live only on the Products & Inventory page, which itself has no cycle selector.

## Content

- [X] CT-01: Page identifies the subscription box admin and exposes all required sections
  - Action: Load the admin page and scan the headings/navigation.
  - Expected: The page heading identifies it as subscription box administration, and sections for Plans, Inventory, Subscriptions/Customers, Shipping/Orders, and Payments are all present with matching labels.

- [ ] CT-02: Monetary and count values are formatted correctly, with no placeholder data
  - Action: Inspect plan rows, inventory rows, and payment history entries.
  - Expected: Prices and payment amounts render as currency (e.g. "$29.99"), subscriber counts render as "current / max", and no row shows placeholder text such as "Lorem ipsum", "undefined", "N/A", or "$0.00" where real default data exists.
  - Bug Report:
    - Issue: Currency not formatted to two decimal places on inventory rows
    - Actual: Plan prices ($29.99, $49.99, $149.99, $499.99), payment amounts ($49.99, $29.99, $149.99, $499.99) and subscriber counts ("342 / 500", "287 / 300", "78 / 100", "23 / 50") are correct, and no "Lorem ipsum"/"undefined"/"N/A" placeholder text appears. However the inventory rows render unit prices without cents: "Artisan Chocolate Bar $4.5/unit" (should be "$4.50"), plus "Organic Tea Sampler $8/unit", "Scented Candle Set $12/unit", "Handmade Soap Bar $6/unit", "Premium Coffee Beans $15/unit", "Leather Journal $18/unit", "Luxury Bath Bomb Set $22/unit", "Exclusive Wine Selection $45/unit".

- [X] CT-03: All displayed content is relevant to running a subscription box business
  - Action: Review all text, labels, and images/icons across the page.
  - Expected: Every heading, label, and image relates to subscription boxes, plans, products, subscribers, billing, or shipping — no unrelated sample content, off-theme stock imagery, or generic demo copy.
