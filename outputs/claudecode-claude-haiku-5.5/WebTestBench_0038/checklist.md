# Test Checklist

## Functionality
- [ ] FT-01: Visitor can compare all subscription plans side by side on the pricing page.
  - Action: Open the pricing page on desktop and review all plan cards.
  - Expected: Every default plan appears together, each showing its name, price, billing cycle options, and key features, so plans can be compared without leaving the page.
- [ ] FT-02: Visitor can open detailed feature descriptions for a plan.
  - Action: Click the "View details" link (or "Features") on any plan card.
  - Expected: A detailed view opens listing that plan's full feature descriptions, with the plan name shown.
- [ ] FT-03: New visitor can create an account and reach checkout.
  - Action: Click "Subscribe" on any plan, then complete the sign-up form (name, email, password) and submit.
  - Expected: The account is created, the visitor is signed in, and the checkout page opens with the selected plan.
- [ ] FT-04: Signed-in user can complete a subscription with valid payment details.
  - Action: On checkout, enter valid test card details and click "Place order" (or "Subscribe").
  - Expected: A confirmation page shows the plan name, billing cycle, and "Subscription active" status.
- [ ] FT-05: Each billing cycle (Monthly, Quarterly, Annual) can be selected at checkout.
  - Action: On checkout, select each billing cycle option in turn.
  - Expected: Each selection is accepted and the chosen cycle is shown in the order summary.
- [ ] FT-06: Account area shows the current plan and billing cycle.
  - Action: Sign in and open "My Account" > "Subscription".
  - Expected: The active plan name, billing cycle, and status are displayed.
- [ ] FT-07: Account area shows upcoming billing information.
  - Action: On the Subscription page, locate the billing section.
  - Expected: The next billing date and next charge amount are displayed.
- [ ] FT-08: Signed-in user can change to a different plan.
  - Action: On the Subscription page, click "Change plan", select a different plan, and click "Confirm change".
  - Expected: The Subscription page shows the new plan name and its updated price and billing information.
- [ ] FT-09: Signed-in user can cancel the subscription.
  - Action: On the Subscription page, click "Cancel subscription" and confirm.
  - Expected: The status changes to "Canceled" and the end-of-access date is shown.

## Constraint
- [ ] CS-01: Checkout cannot be submitted with empty required fields.
  - Action: On checkout, leave the card number field empty and click "Place order".
  - Expected: The order is not placed, and the empty required field shows an error message such as "Card number is required."
- [ ] CS-02: A declined payment does not create an active subscription.
  - Action: On checkout, enter a card number designated to be declined and click "Place order".
  - Expected: An error message such as "Payment declined" appears, and the Subscription page does not show an active plan.
- [ ] CS-03: The currently active plan cannot be selected as the change target.
  - Action: Sign in, open "Change plan", and inspect the card for the current plan.
  - Expected: The current plan is labeled "Current plan" and its select button is disabled or absent.
- [ ] CS-04: Account pages are not accessible while signed out.
  - Action: Signed out, navigate directly to the Subscription page URL in the address bar.
  - Expected: The visitor is redirected to the sign-in page and no subscription details are shown.

## Interaction
- [ ] IX-01: Switching the billing cycle updates all plan prices immediately.
  - Action: On the pricing page, click the "Monthly", "Quarterly", and "Annual" toggle options in turn.
  - Expected: All plan prices and the cycle label update on each click without a page reload, and the selected toggle is highlighted.
- [ ] IX-02: Cancel confirmation prevents accidental cancellation.
  - Action: On the Subscription page, click "Cancel subscription", then click "Keep subscription" in the dialog.
  - Expected: The dialog closes, the subscription remains active, and no status change occurs.
- [ ] IX-03: A success message appears after a plan change is confirmed.
  - Action: Complete a plan change on the Subscription page (FT-08).
  - Expected: A success notification such as "Your plan has been changed" appears, and the page updates without a reload.

## Content
- [ ] CT-01: Feature lists are consistent between the pricing page and the detail view.
  - Action: Compare the features listed on a plan card with those in its detailed view.
  - Expected: The same features appear in both places with no missing or contradictory items.
- [ ] CT-02: Prices match across the pricing page, checkout, and account area for the same plan and cycle.
  - Action: Note the price for one plan and cycle on the pricing page, then check checkout and the Subscription page.
  - Expected: The price is identical on all three pages.
- [ ] CT-03: Savings percentages for quarterly and annual cycles are accurate.
  - Action: Compare the stated savings (e.g., "Save X%") with the monthly price for the same plan.
  - Expected: The stated savings match the calculated difference between the cycle's effective monthly price and the monthly price.
- [ ] CT-04: Next billing date and amount match the selected cycle.
  - Action: Sign in as a subscriber and check the upcoming billing section on the Subscription page.
  - Expected: The next billing date reflects the cycle interval (monthly, quarterly, or annual), and the amount equals the plan's price for that cycle.