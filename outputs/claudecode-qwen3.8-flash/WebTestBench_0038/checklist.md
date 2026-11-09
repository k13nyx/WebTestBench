# Test Checklist

## Functionality
- [ ] FT-01: Pricing landing page presents the subscription plans for comparison
  - Action: Open the home/pricing page and count the distinct plan cards (e.g., "Starter", "Pro", "Business").
  - Expected: At least 3 plan cards are visible, each showing plan name, its price, and a call-to-action button such as "Choose plan" / "Subscribe".

- [ ] FT-02: Side-by-side plan comparison is available to visitors
  - Action: Click the "Compare Plans" / "View comparison" control on the pricing page.
  - Expected: A comparison view/table appears listing features as rows and the plans as columns, showing which plan includes each feature.

- [ ] FT-03: Detailed feature descriptions are readable
  - Action: Open a plan's feature detail ("Features", "See what's included", or an individual feature row/expander).
  - Expected: Each listed feature has a descriptive text explaining it (not only a name or a check mark).

- [ ] FT-04: Annual, quarterly, and monthly periods yield different outcomes and can be compared
  - Action: On the pricing page, select each period in the "Monthly / Quarterly / Annual" selector, note the price per plan, then start checkout for the same plan under two different periods.
  - Expected: The displayed price and the checkout summary charge change per period (monthly price ≠ quarterly total ≠ annual total), and all three periods remain directly comparable on the same screen.

- [ ] FT-05: Visitor can create an account
  - Action: Click "Sign up" / "Create account", enter a valid unused email and password, submit.
  - Expected: The account is created and the visitor is signed in and routed to the dashboard/account area.

- [ ] FT-06: Signed-in user can subscribe through a simple checkout flow
  - Action: From a plan, click "Subscribe", pick a billing period, enter payment details on one short form, click "Confirm subscription" / "Pay".
  - Expected: Checkout completes in a single flow and the account's subscription becomes active for the chosen plan and period.

- [ ] FT-07: Account area shows the current plan
  - Action: Sign in as a subscribed user and open the account/billing area.
  - Expected: The active plan name and billing period (e.g., "Pro — Annual") are displayed and match what was purchased.

- [ ] FT-08: Account area shows upcoming billing information
  - Action: Open the account/billing area of an active subscriber.
  - Expected: Next billing/charge date and the amount that will be charged for the current period are both shown.

- [ ] FT-09: Signed-in user can change to a different plan
  - Action: In the account area, click "Change plan" / "Switch plan", select another plan and period, and confirm.
  - Expected: The account area updates to show the new plan and the new period's price/next charge; the old plan is no longer shown as active.

- [ ] FT-10: Signed-in user can cancel their subscription
  - Action: In the account area, click "Cancel subscription" and confirm the cancellation.
  - Expected: The subscription state changes to cancelled (no active plan), and cancellation is reflected in the account area.

## Constraint
- [ ] CS-01: Account creation rejects invalid or missing required data
  - Action: Submit the sign-up form with the email field empty, then with an invalid string such as `notanemail`, then with an empty/short password.
  - Expected: Each submission is blocked with a field-level validation message and no account is created.

- [ ] CS-02: An email address cannot be registered twice
  - Action: Sign up using an email that already has an account.
  - Expected: Registration is rejected with a message indicating the email is already in use, and the existing account is unaffected.

- [ ] CS-03: Account area is only reachable by signed-in users
  - Action: While signed out, navigate directly to the account/billing URL.
  - Expected: The subscription details are not shown; the visitor is redirected to (or prompted for) login/sign-up.

- [ ] CS-04: Checkout cannot be completed without a selected plan/period and valid payment details
  - Action: Open checkout and attempt to confirm with a payment card field empty or invalid (e.g., `123`), and attempt to confirm with no period selected.
  - Expected: Submission is blocked with an inline validation error and no subscription is created.

- [ ] CS-05: Cancellation is confirmed and stops future billing
  - Action: Click "Cancel subscription", dismiss the confirmation prompt, then re-open and confirm it.
  - Expected: Dismissing leaves the subscription active; after confirming, no upcoming charge date is shown and further plan changes require re-subscribing.

## Interaction
- [ ] IX-01: The billing-period selector updates the whole page immediately
  - Action: Click "Quarterly" then "Annual" in the period toggle while watching the plan cards and comparison table.
  - Expected: The selected period becomes visually active and all prices/savings labels update in place without a manual reload of the page.

- [ ] IX-02: Subscription and plan changes give visible feedback
  - Action: Complete a checkout, then perform a plan change in the account area.
  - Expected: Each action produces a confirmation (success message/toast or a confirmation screen naming the plan and period), and the account area refreshes to the new state.

- [ ] IX-03: Plan CTAs carry context into checkout
  - Action: Click the "Subscribe" / "Choose plan" button on two different plans from the pricing page.
  - Expected: Checkout opens with that specific plan preselected, and the back/return path brings the user back to the pricing/comparison view.

## Content
- [ ] CT-01: All plan content is real and relevant to a software subscription service
  - Action: Read every plan card, the comparison table, and the feature descriptions on the pricing page.
  - Expected: Names, prices, and feature text are specific to the software service (no lorem ipsum, "Plan 1/Feature A" placeholders, `$0.00`, `Lorem`, or broken/missing images or icons).

- [ ] CT-02: Pricing and feature data are consistent across views
  - Action: For one plan, compare the price and included-features list on the pricing card against the comparison table, the checkout summary, and the account area after subscribing.
  - Expected: The same price for the chosen period and the same set of features appear in all four places (no contradictions such as a check-marked feature missing from the account area).