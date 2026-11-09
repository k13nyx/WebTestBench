# Test Checklist

## Functionality
- [ ] FT-01: Visitor can browse all subscription plans
  - Action: Open the pricing/plans page.
  - Expected: All default plans (e.g., Basic, Pro, Enterprise) are listed with name, price, and a "Subscribe"/"Choose plan" button for each.
- [ ] FT-02: Visitor can read detailed feature descriptions for each plan
  - Action: Click the "Learn more" / "See features" link (or expand the feature section) of any plan.
  - Expected: A detailed feature list for that plan is displayed (e.g., feature bullets with descriptions), matching the plan's tier.
- [ ] FT-03: Visitor can compare billing cycles (monthly / quarterly / annual)
  - Action: On the plans page, switch the billing cycle selector between "Monthly", "Quarterly", and "Annual".
  - Expected: The displayed price for each plan updates to the amount corresponding to the selected billing cycle.
- [ ] FT-04: Visitor can compare plans against one another side by side
  - Action: View the plans/comparison page with the "Compare plans" view.
  - Expected: All plans are shown in a side-by-side layout where feature availability per plan can be directly compared (e.g., checkmarks vs. dashes).
- [ ] FT-05: Visitor can create an account
  - Action: Fill in the registration form (name, email, password) with valid values and submit it.
  - Expected: The account is created and the user is signed in (e.g., redirected to the account area or shown as logged in).
- [ ] FT-06: User can subscribe to a plan through the checkout flow
  - Action: While signed in, select any plan with a chosen billing cycle and complete the checkout (billing/payment details, confirm).
  - Expected: Checkout completes and the subscription to the selected plan and billing cycle becomes active.
- [ ] FT-07: Signed-in user can view their current plan
  - Action: Sign in and open the account area / "Subscription" section.
  - Expected: The currently subscribed plan name and its billing cycle (monthly/quarterly/annual) are displayed.
- [ ] FT-08: Signed-in user can see upcoming billing information
  - Action: Open the account area / "Billing" section.
  - Expected: Upcoming billing details are shown, including the amount to be charged and the next billing date.
- [ ] FT-09: Signed-in user can change to a different plan
  - Action: In the account area, click "Change plan", select a different plan (with a billing cycle), and confirm.
  - Expected: The current plan is updated to the newly selected plan/cycle, and the account area reflects the change.
- [ ] FT-10: Signed-in user can cancel their subscription
  - Action: In the account area, click "Cancel subscription" and confirm the cancellation.
  - Expected: The subscription status changes to "Canceled" (or equivalent), and the account area shows the subscription as canceled.

## Constraint
- [ ] CS-01: Registration cannot be submitted with empty required fields
  - Action: On the registration form, leave required fields (e.g., email, password) empty and submit.
  - Expected: The form is not submitted; a validation error indicates which required fields are missing.
- [ ] CS-02: Registration cannot be completed with an already-registered email
  - Action: Attempt to register using the email of an existing default account.
  - Expected: Registration is rejected with an error such as "Email already in use"; no duplicate account is created.
- [ ] CS-03: Checkout cannot be completed with empty or invalid payment details
  - Action: Start checkout for a plan and submit with empty or malformed payment fields (e.g., blank card number).
  - Expected: Checkout is blocked; an error indicates the payment details are missing/invalid, and no subscription is created.
- [ ] CS-04: Checkout requires a plan and billing cycle to be selected
  - Action: Attempt to open/submit the checkout without any plan or billing cycle chosen.
  - Expected: The checkout cannot proceed; the user is prompted to select a plan and billing cycle first.
- [ ] CS-05: Cancellation requires explicit confirmation
  - Action: In the account area, click "Cancel subscription" but dismiss/abort the confirmation step.
  - Expected: The subscription remains active; no cancellation is applied without explicit confirmation.
- [ ] CS-06: Subscription actions are unavailable to signed-out visitors
  - Action: While signed out, attempt to access the account area / manage subscription pages directly.
  - Expected: The user cannot view or manage any subscription; they are redirected to sign in.

## Interaction
- [ ] IX-01: Billing cycle selector updates prices immediately
  - Action: On the plans page, click between "Monthly", "Quarterly", and "Annual" toggles.
  - Expected: Plan prices update instantly without a page reload, and the selected cycle is visually highlighted.
- [ ] IX-02: Checkout shows a success confirmation after subscribing
  - Action: Complete a valid checkout.
  - Expected: A success message/confirmation (e.g., "Subscription successful" toast or confirmation page) is shown to the user.
- [ ] IX-03: Plan change shows a confirmation of the new plan
  - Action: Complete a plan change in the account area.
  - Expected: Feedback is shown confirming the plan change (e.g., "Your plan has been updated" message).
- [ ] IX-04: Cancellation shows a confirmation of cancellation
  - Action: Confirm the cancellation of a subscription.
  - Expected: Feedback is shown confirming the cancellation (e.g., "Your subscription has been canceled" message).

## Content
- [ ] CT-01: Displayed prices are consistent with the selected billing cycle and plan
  - Action: Compare the price shown on the plans page for each plan/cycle combination against the price charged at checkout and shown in billing.
  - Expected: The amounts are consistent for the same plan and billing cycle across plans page, checkout, and billing section.
- [ ] CT-02: All plan content is relevant to the software service theme
  - Action: Review plan names, feature descriptions, and marketing text on the plans and comparison pages.
  - Expected: All text and features describe software-service capabilities (e.g., seats, storage, API access); no irrelevant or placeholder content is present.