# Test Checklist

## Functionality

- [ ] FT-01: Plans comparison page displays all subscription plans side by side
  - Action: Open the site and click "Plans"/"Pricing" in the main navigation.
  - Expected: At least 3 distinct plans are displayed side by side, each showing a plan name, a price, and a summary list of included features.

- [ ] FT-02: Detailed feature descriptions are available for each plan
  - Action: On the plans page, open the detailed feature view for one plan (e.g., click "See features", "View details", or expand the plan's feature section). Repeat for a second plan.
  - Expected: A detailed feature list/description specific to that plan is displayed, containing more items than the card summary, and the content differs between the two plans.

- [ ] FT-03: Choosing a plan and billing cycle starts the checkout flow with the correct plan and price
  - Action: On the plans page, select the "Monthly" cycle and click the "Choose plan"/"Subscribe"/"Get started" button on one plan.
  - Expected: The user is taken to the sign-up/checkout flow, which displays the chosen plan name and its monthly price.

- [ ] FT-04: A new visitor can create an account during checkout
  - Action: In the checkout flow, fill the account fields (name, email, password) with valid unused values and submit.
  - Expected: The account is created and the flow advances to the payment step with no "email already in use" or validation error.

- [ ] FT-05: Completing payment activates the subscription
  - Action: At the payment step, enter the required payment details (card number, expiry, CVC or the test payment method shown) and submit the order.
  - Expected: The order completes, the user is signed in and redirected to the account/subscription area showing the purchased plan as active with its billing cycle.

- [ ] FT-06: A returning signed-in user can view their current plan
  - Action: Sign out, sign back in with the same credentials, then open the account/subscription section.
  - Expected: The current plan name and active billing cycle (e.g., "Pro — Annual") are displayed exactly as purchased.

- [ ] FT-07: Account area displays upcoming billing information
  - Action: While signed in, open the account/subscription section and locate the billing details.
  - Expected: A next billing/payment date and the amount due are both displayed, and the amount matches the price of the active plan and cycle.

- [ ] FT-08: Signed-in user can change to a different plan
  - Action: In the account/subscription section, click "Change plan", select a different plan than the active one, and confirm.
  - Expected: The subscription is updated — the account area now shows the newly selected plan as the current plan.

- [ ] FT-09: Signed-in user can cancel the subscription
  - Action: In the account/subscription section, click "Cancel subscription" and confirm the cancellation in the confirmation prompt.
  - Expected: The subscription status changes to cancelled/expired (e.g., "Cancelled", "Ends on <date>") and is no longer shown as active.

## Constraint

- [ ] CS-01: Checkout blocks empty and invalid account input
  - Action: Submit the account step of checkout with all fields empty; then submit again with email "test" and password "123".
  - Expected: Both attempts are blocked in place with inline error messages (required-field errors first, then email-format and password-strength errors); no account is created and the flow does not advance to payment.

- [ ] CS-02: The selected billing cycle determines the charged amount and billing term
  - Action: On the plans page select "Annual" for one plan and proceed to the checkout order summary; note the monthly amount for the same plan shown earlier.
  - Expected: The order summary shows the annual total and term (e.g., "$X billed yearly"), which is a different figure/outcome from the monthly amount for that same plan.

- [ ] CS-03: User cannot switch to the plan they are already on
  - Action: In the account area, open "Change plan" and attempt to select the currently active plan.
  - Expected: The active plan is labelled as the current plan and cannot be selected (control disabled or selection rejected with no change to the subscription).

- [ ] CS-04: Cancellation requires confirmation and is not applied if dismissed
  - Action: In the account area, click "Cancel subscription", then dismiss the prompt ("Go back"/"Keep subscription"/close).
  - Expected: The prompt closes and the subscription status remains active/unchanged.

- [ ] CS-05: Account area is not accessible while signed out
  - Action: Sign out, then navigate directly to the account/subscription page.
  - Expected: The user is redirected to the sign-in page and no plan or billing data is displayed.

## Interaction

- [ ] IX-01: Billing cycle toggle updates all plan prices immediately
  - Action: On the plans page (starting on "Monthly"), click "Quarterly", then "Annual".
  - Expected: All plan prices update immediately without a page reload, and the selected cycle button is visually marked as active.

- [ ] IX-02: Success confirmation is shown after purchase
  - Action: Complete the checkout payment step and observe the immediate response.
  - Expected: A confirmation message or confirmation screen naming the subscribed plan (e.g., "Subscription activated", "You're on Pro") is displayed.

- [ ] IX-03: Selecting a plan visually marks it as the chosen plan
  - Action: On the plans page, click the select/choose control of one plan, then click that of a different plan.
  - Expected: Each clicked plan is visually marked as selected (highlight, border, or check mark) and only one plan is marked selected at a time.

## Content

- [ ] CT-01: Plan prices, currency, and period labels are correct and non-placeholder
  - Action: On the plans page, review each plan card's displayed price, currency symbol, and period label (e.g., "/mo", "/yr") under each billing cycle.
  - Expected: Every plan shows a non-empty, correctly formatted price with currency and a period label matching the selected cycle; no "0", "NaN", "undefined", or blank prices.

- [ ] CT-02: Feature descriptions are relevant to the software service
  - Action: Read the feature lists and descriptions for all plans on the plans page and in the detailed feature views.
  - Expected: All items describe capabilities of the software service; no "Lorem ipsum", placeholder, or unrelated content, and higher-tier plans list at least as many features as lower tiers.

- [ ] CT-03: All images and icons render and are relevant to the service
  - Action: Load the plans page and the account/subscription page and inspect every image, logo, and icon.
  - Expected: All images load successfully (no broken-image icons or empty boxes) and each is relevant to the software service or plans being presented.