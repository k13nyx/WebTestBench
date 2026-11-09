# Test Checklist

## Functionality
- [ ] FT-01: Visitor can compare all available subscription plans side by side.
  - Action: Open the pricing page as a signed-out visitor and review the plan listing.
  - Expected: All default plans are shown side by side, each with its name, price, and key features visible together.

- [ ] FT-02: Visitor can read detailed feature descriptions for each plan.
  - Action: On the pricing page, open a plan's detailed feature list (expand "View all features" / the feature section).
  - Expected: A detailed list of feature descriptions for that plan is displayed.

- [ ] FT-03: Visitor can compare Annual, Quarterly, and Monthly payment outcomes against one another.
  - Action: For one default plan, review the pricing shown under each billing period (Annual, Quarterly, Monthly).
  - Expected: Each billing period shows its own price outcome (e.g., amount plus billing total) and the three outcomes are distinct values, so the periods can be compared against one another.

- [ ] FT-04: Visitor can create an account within the checkout flow.
  - Action: Click "Subscribe" on a default plan and complete the account creation step with a valid email and password.
  - Expected: The account is created, the user is signed in, and checkout continues.

- [ ] FT-05: Visitor can complete the checkout and subscribe to the selected plan.
  - Action: Fill in the checkout billing/payment details and submit the order.
  - Expected: The subscription is created and active for the selected plan and billing period.

- [ ] FT-06: Signed-in subscriber can view their current plan.
  - Action: Sign in and open the account area.
  - Expected: The account area displays the current plan name and its billing period.

- [ ] FT-07: Signed-in subscriber can view upcoming billing information.
  - Action: In the account area, open the billing / upcoming billing section.
  - Expected: The next billing date and the upcoming charge amount are displayed.

- [ ] FT-08: Signed-in subscriber can change to a different plan.
  - Action: In the account area, click "Change Plan", select a different default plan, and confirm.
  - Expected: The account area updates and shows the newly selected plan as the current plan.

- [ ] FT-09: Signed-in subscriber can cancel their subscription.
  - Action: In the account area, click "Cancel Subscription" and confirm the cancellation.
  - Expected: The subscription is cancelled and its status is shown as cancelled/inactive.

## Constraint
- [ ] CS-01: Account creation is blocked when required fields are empty or invalid.
  - Action: Submit the account creation form with an empty email, then with an invalid email (e.g., "abc@"), then with an empty password.
  - Expected: Each submission is rejected with an error message on the offending field, and no account is created.

- [ ] CS-02: Checkout is blocked when required payment fields are empty or invalid.
  - Action: Submit the checkout form with empty payment fields, then with an invalid card number.
  - Expected: Each submission is rejected with an error message, and no subscription is created.

- [ ] CS-03: Plan and billing details are not accessible while signed out.
  - Action: Sign out, then open the account area again (via the "Account" link or direct URL).
  - Expected: The user is redirected to the sign-in page, and no plan or billing details are displayed.

- [ ] CS-04: Cancelling the subscription requires explicit confirmation.
  - Action: Click "Cancel Subscription", then dismiss/decline the confirmation prompt.
  - Expected: The subscription remains active; it is cancelled only after the user explicitly confirms.

## Interaction
- [ ] IX-01: Selecting a billing period immediately updates the displayed pricing.
  - Action: Click "Monthly", "Quarterly", and "Annual" in turn on the pricing page.
  - Expected: The clicked option is visually highlighted as selected and the displayed plan prices update to the chosen period right away.

- [ ] IX-02: A success confirmation is displayed after the subscription is created.
  - Action: Complete the checkout and submit the subscription.
  - Expected: A success confirmation (e.g., "Your subscription is active") is displayed on screen.

## Content
- [ ] CT-01: Plan feature descriptions are relevant to the software service.
  - Action: Review the feature descriptions listed for each default plan.
  - Expected: Every feature description relates to the software service being sold; no placeholder or off-theme text is shown.

- [ ] CT-02: Upcoming billing information matches the subscribed plan and billing period.
  - Action: In the account area, compare the displayed upcoming charge with the plan's listed price for the subscribed billing period.
  - Expected: The upcoming charge amount equals the plan's price for that billing period (e.g., the annual total for the Annual period).

- [ ] CT-03: The checkout summary matches the user's selection.
  - Action: Reach the checkout page after selecting a plan and billing period and review the order summary.
  - Expected: The summary shows the selected plan name, the selected billing period, and the total price for that period.