# Test Checklist

## Functionality
- [ ] FT-01: Display of subscription plans on the pricing page
  - Action: Navigate to the pricing/plans section of the site.
  - Expected: All available plans are listed with their billing cycle options (annual, quarterly, monthly) and prices, each selectable.
- [ ] FT-02: Access to detailed plan feature descriptions
  - Action: Open the details of any plan (e.g., click "View details" or expand the plan card).
  - Expected: A detailed feature list for that plan is shown, covering what the plan includes.
- [ ] FT-03: Account creation flow
  - Action: Start signup from the pricing or checkout flow and submit valid new-account details.
  - Expected: The account is created and the user is signed in, proceeding to checkout.
- [ ] FT-04: Completing a subscription checkout
  - Action: With a signed-in user, fill the checkout form with valid payment details and confirm the subscription.
  - Expected: The checkout completes and the selected plan becomes the user's active subscription.
- [ ] FT-05: Viewing current plan in account area
  - Action: Open the account area of a subscribed user.
  - Expected: The current plan name (and its billing cycle) is displayed.
- [ ] FT-06: Viewing upcoming billing information
  - Action: Open the billing/subscription section of the account area.
  - Expected: The next billing date and the amount due are displayed.
- [ ] FT-07: Changing to a different plan
  - Action: From the account area, select a different plan and confirm the change.
  - Expected: The change completes and the account area now shows the newly selected plan as current.
- [ ] FT-08: Canceling a subscription
  - Action: From the account area, choose to cancel the subscription and confirm.
  - Expected: The subscription is canceled and the account area reflects the canceled state.
- [ ] FT-09: Distinct billing outcomes per billing cycle, comparable to one another
  - Action: Subscribe once with a monthly plan, once with a quarterly plan, and once with an annual plan (separate test accounts), checking the account area each time.
  - Expected: Each cycle shows a different, correct billing outcome (e.g., next billing date ≈1 month, ≈3 months, or ≈12 months out, with matching amounts), allowing the three to be compared.

## Constraint
- [ ] CS-01: Checkout blocked when required fields are empty or invalid
  - Action: Leave required checkout fields (e.g., email, payment details) empty or invalid and attempt to submit.
  - Expected: Submission is blocked and an error identifies the invalid/missing field; no subscription is created.
- [ ] CS-02: Signup blocked when required account fields are missing or invalid
  - Action: Attempt to create an account with an empty or invalid required field (e.g., malformed email, empty password).
  - Expected: Account creation is blocked with an error on the offending field.
- [ ] CS-03: Account area inaccessible when signed out
  - Action: While signed out, attempt to open the account area (via direct URL or navigation link).
  - Expected: Access is denied and the user is prompted to sign in; no account/subscription data is shown.
- [ ] CS-04: No active plan or upcoming charge shown after cancellation
  - Action: After canceling a subscription, reload the account area.
  - Expected: The plan no longer shows as active and no upcoming billing charge is listed.

## Interaction
- [ ] IX-01: Confirmation feedback after completing checkout
  - Action: Finish a valid checkout.
  - Expected: A visible success confirmation (e.g., message or confirmation screen) appears indicating the subscription is active.
- [ ] IX-02: Explicit confirmation required before canceling
  - Action: Click the cancel-subscription option.
  - Expected: A confirmation prompt appears asking the user to confirm; the subscription is unchanged until confirmed.
- [ ] IX-03: Billing-cycle selection dynamically updates displayed prices
  - Action: On the pricing page, switch between annual, quarterly, and monthly billing options.
  - Expected: The displayed prices update immediately to reflect the selected cycle, without a page reload.
- [ ] IX-04: Signed-in state reflected in the interface after login
  - Action: Sign in after creating an account.
  - Expected: The navigation/header updates to show the signed-in state (e.g., account menu or sign-out option).

## Content
- [ ] CT-01: Feature descriptions align with each plan's tier
  - Action: Compare the feature lists of the lower and higher plans.
  - Expected: Each plan's described features match its tier, with higher tiers including at least all lower-tier features plus extras; no irrelevant content.
- [ ] CT-02: Consistency of displayed price between pricing page and checkout
  - Action: Note a plan's price on the pricing page, then proceed to checkout for that plan.
  - Expected: The checkout shows the same plan name, billing cycle, and price as displayed on the pricing page.
- [ ] CT-03: Billing details shown in the account area are accurate
  - Action: After subscribing to a known plan, inspect the current plan and next billing info in the account area.
  - Expected: The plan name, cycle, next billing date, and amount all correspond to the plan chosen at checkout.