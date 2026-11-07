# Test Checklist

## Functionality
- [ ] FT-01: Compare different subscription plans side by side
  - Action: Navigate to the Plans page and open the plan comparison view.
  - Expected: All available plans are displayed together with their features aligned for direct comparison.

- [ ] FT-02: Read detailed feature descriptions for each plan
  - Action: Select or expand an individual plan (e.g., click "View Details" on a plan card).
  - Expected: A detailed feature description for that plan is displayed with no missing or placeholder text.

- [ ] FT-03: Create an account
  - Action: Click "Sign Up" / "Create Account", enter valid credentials, and submit.
  - Expected: A new account is created and the user is signed in (redirected to account area or confirmation shown).

- [ ] FT-04: Subscribe via the simple checkout flow
  - Action: Choose a plan, click "Subscribe"/"Checkout", and complete the checkout steps with valid payment details.
  - Expected: The subscription is created and the user's account reflects the active subscription.

- [ ] FT-05: View current plan as a signed-in user
  - Action: Sign in and open the Account area ("My Account" / "Current Plan" section).
  - Expected: The user's currently active subscription plan is clearly displayed.

- [ ] FT-06: View upcoming billing information
  - Action: In the Account area, open the "Billing" section.
  - Expected: Upcoming billing details are shown (next charge amount, billing cycle, and next billing date).

- [ ] FT-07: Change to a different plan
  - Action: In the Account area, click "Change Plan" and select a different plan, then confirm.
  - Expected: The subscription updates to the newly selected plan and the change is reflected in the account.

- [ ] FT-08: Cancel subscription from the account area
  - Action: In the Account area, click "Cancel Subscription" and confirm the cancellation.
  - Expected: The subscription is canceled and the account shows a canceled/no-active-subscription status.

- [ ] FT-09: Compare Annual, Quarterly, and Monthly plan outcomes
  - Action: On the Plans page, switch the billing-period toggle between Annual, Quarterly, and Monthly.
  - Expected: Each period yields a distinct, comparable outcome (price and/or savings) shown for the same plan.

## Constraint
- [ ] CS-01: Subscription requires a signed-in account
  - Action: Attempt to reach checkout and subscribe without being signed in.
  - Expected: Checkout is blocked and the user is prompted to create an account or sign in first.

- [ ] CS-02: Plan change/cancel only allowed with an active subscription
  - Action: As a signed-in user with no active subscription, look for "Change Plan" / "Cancel Subscription".
  - Expected: These actions are unavailable or return an error stating no active subscription exists.

- [ ] CS-03: Different billing periods must produce distinct outcomes
  - Action: Select Annual, then Quarterly, then Monthly for the same plan.
  - Expected: The displayed price/outcome differs for each period (no two periods show identical pricing).

## Interaction
- [ ] IX-01: Success feedback after account creation
  - Action: Complete the account creation form with valid input and submit.
  - Expected: A success message/toast appears confirming the account was created.

- [ ] IX-02: Success confirmation after subscribing
  - Action: Complete the checkout flow with valid payment details.
  - Expected: A confirmation message/toast appears stating the subscription was successful.

- [ ] IX-03: Account state updates immediately after plan change or cancellation
  - Action: Change or cancel a plan and return to the Account area without refreshing.
  - Expected: The updated plan/cancellation status is reflected instantly in the account UI.

## Content
- [ ] CT-01: Plan feature descriptions are complete and on-theme
  - Action: Review the feature descriptions for every available plan.
  - Expected: Each description is relevant to the software service, fully written, and free of placeholder/lorem text.

- [ ] CT-02: Billing information is accurate and complete
  - Action: Open the Billing section for an active subscription.
  - Expected: Amount, billing cycle, and next billing date are all present, correctly formatted, and consistent with the chosen plan/period.