# Test Result

## Functionality
- [X] FT-01: Visitors can compare available plans.
  - Action: Open the plans/pricing page.
  - Expected: All available plans are displayed together with their price and key features for side-by-side comparison.

- [X] FT-02: Visitors can read detailed feature descriptions.
  - Action: Select a plan's "See all features" / details control.
  - Expected: The full, detailed list of features included in that plan is displayed.

- [X] FT-03: Visitors can create an account.
  - Action: Complete the sign-up form with a valid name, email, and password, then submit.
  - Expected: The account is created and the user is signed in.

- [X] FT-04: Visitors can subscribe through the checkout flow.
  - Action: Choose a plan and a billing cycle, enter valid payment details, and submit checkout.
  - Expected: The subscription is activated and the account shows the selected plan as active.

- [X] FT-05: Signed-in users can view their current plan.
  - Action: Open the account/billing area while signed in.
  - Expected: The current plan name, billing cycle, and price are displayed.

- [ ] FT-06: Signed-in users can see upcoming billing information.
  - Action: View the billing information section in the account area.
  - Expected: The next charge amount and the next billing date are displayed.
  - Bug Report:
    - Issue: Missing "next charge amount" data in the billing information section.
    - Actual: The billing section displays only the next billing date (e.g. "Next billing date: December 8, 2026" / "November 3, 2027") alongside the plan price ("$29/mo (Monthly)" / "$290/yr (Annual)"). No next-charge amount is rendered (DOM text search for "next charge"/"amount due"/"total" returns nothing). Only one of the two required values is present.

- [X] FT-07: Signed-in users can change to a different plan.
  - Action: Select a different plan and confirm the change.
  - Expected: The subscription is updated to the newly selected plan and the account area reflects it.

- [X] FT-08: Signed-in users can cancel their subscription.
  - Action: Click "Cancel subscription" and confirm.
  - Expected: The subscription is cancelled and the account shows a cancelled/inactive status.

## Constraint
- [X] CS-01: Account form rejects missing required fields.
  - Action: Submit the sign-up form with required fields left empty.
  - Expected: The form is rejected with validation errors and no account is created.

- [ ] CS-02: Checkout rejects missing or invalid payment details.
  - Action: Submit checkout with empty or invalid payment details.
  - Expected: Checkout is rejected with an error and no subscription is created.
  - Bug Report:
    - Issue: Insufficient payment validation — invalid payment details are accepted.
    - Actual: Submitting checkout with clearly invalid data (Card Number "1234", Expiry "13/40", CVC "1") was accepted: the app navigated to /account with a "Success! You're now subscribed to the Pro plan." toast, and the subscription was created. (Empty submission is correctly rejected with "Please fill in all payment details.", but the "invalid" case is not validated.)

- [X] CS-03: User cannot switch to the plan they already have.
  - Action: In the account area, attempt to change to the plan currently subscribed to.
  - Expected: The change is blocked with a message stating the plan is already active.

- [X] CS-04: Account and billing area is blocked for signed-out users.
  - Action: Open the account/billing area URL while signed out.
  - Expected: The user is redirected to sign-in and cannot view billing details.

## Interaction
- [X] IX-01: Billing cycle selection updates prices immediately.
  - Action: On the plans page, switch between Monthly, Quarterly, and Annual cycles.
  - Expected: The displayed prices update immediately without a page reload.

- [X] IX-02: Successful subscription shows a confirmation.
  - Action: Complete a subscription through checkout successfully.
  - Expected: A success confirmation message (e.g., "Subscription confirmed") is displayed.

- [X] IX-03: Cancellation shows confirmation feedback.
  - Action: Confirm the subscription cancellation.
  - Expected: A message confirming the cancellation is displayed.

- [ ] IX-04: Invalid input shows inline error feedback.
  - Action: Enter invalid data in sign-up or checkout fields.
  - Expected: Inline error messages appear next to the offending fields.
  - Bug Report:
    - Issue: Missing inline field-level error messages (feedback is only surfaced as toast notifications).
    - Actual: Entering an invalid email ("invalid-email") and an invalid password ("123") and submitting produced only toast notifications ("Please fill in all fields." and "Password must be at least 6 characters."). No error text, aria-invalid, or error element appeared next to the offending Email/Password fields (DOM query of `[class*="error"]`, `[role="alert"]`, `[aria-invalid]` returned empty).

## Content
- [X] CT-01: Feature descriptions are relevant and accurate.
  - Action: Read the feature descriptions across all plans.
  - Expected: Each plan's features are relevant to the software service and accurately describe what is included.

- [X] CT-02: Pricing is consistent across all pages.
  - Action: Compare the price shown on the plans page, at checkout, and in the account billing area.
  - Expected: The price for the same plan and billing cycle matches on all pages.

- [X] CT-03: All displayed media is relevant to the theme.
  - Action: Review images and icons on the plans, checkout, and account pages.
  - Expected: All media relate to the software/subscription theme, and none are broken or off-topic.

- [X] CT-04: No placeholder content is present.
  - Action: Review all page text across the site.
  - Expected: No lorem ipsum, "TODO", or empty placeholder text appears.
