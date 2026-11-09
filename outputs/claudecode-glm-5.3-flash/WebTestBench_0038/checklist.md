# Test Checklist

## Functionality
- [ ] FT-01: Pricing page displays all three billing periods as comparable plans
  - Action: Open the pricing/plans page.
  - Expected: Three plans are shown — Annual, Quarterly, and Monthly — each with a visible price, and they are laid out so they can be compared side by side (e.g., in a comparison table or pricing cards).
- [ ] FT-02: Detailed feature descriptions are available for each plan
  - Action: View each plan's feature list or open its detailed description.
  - Expected: Every plan (Annual, Quarterly, Monthly) shows a list of features with descriptions, and differences between plans (e.g., which features are included) are visible/indicated.
- [ ] FT-03: Visitor can create a new account
  - Action: Click the sign-up/register button, enter a valid email, password, and any required fields, then submit.
  - Expected: Account is created, user is signed in, and a signed-in state is visible (e.g., account name/avatar in the header).
- [ ] FT-04: Signed-in user can subscribe to a plan via checkout
  - Action: While signed in, select a plan (e.g., Monthly) and complete the checkout form with valid payment details, then submit.
  - Expected: Subscription is created successfully and a confirmation is shown indicating the active plan.
- [ ] FT-05: Account area shows the user's current plan
  - Action: After subscribing, open the account/billing area.
  - Expected: The currently subscribed plan name (matching the one purchased) and its status (e.g., Active) are displayed.
- [ ] FT-06: Account area shows upcoming billing information
  - Action: Open the account area after subscribing to the Monthly plan.
  - Expected: An upcoming billing/renewal date and the amount to be charged are displayed, consistent with the plan's billing cycle.
- [ ] FT-07: User can change to a different plan
  - Action: In the account area, use the change-plan option to switch from the current plan to a different one (e.g., Monthly → Annual) and confirm.
  - Expected: The change succeeds and the account area now shows the new plan as the current plan.
- [ ] FT-08: User can cancel their subscription
  - Action: In the account area, click the cancel-subscription option and confirm.
  - Expected: The subscription is cancelled; the account area reflects cancelled status (e.g., "Cancelled" or plan expiry) and no upcoming charge is shown.
- [ ] FT-09: Billing outcomes differ across the three payment plans
  - Action: Note the price and billing terms for Annual, Quarterly, and Monthly (e.g., Annual = $X/year, Quarterly = $Y/quarter, Monthly = $Z/month) and check any stated totals/savings.
  - Expected: The three plans produce different outcomes (different prices/cadence/savings, e.g., Annual is cheaper per period than Monthly), and these differences are accurately reflected in checkout and billing info.
- [ ] FT-10: A plan comparison view aligns plans against one another
  - Action: Use the comparison view/table (or toggle to compare plans) on the pricing page.
  - Expected: Features/prices for Annual, Quarterly, and Monthly are displayed in a directly comparable format (e.g., same rows across plans), so differences are readable at a glance.

## Constraint
- [ ] CS-01: Account creation rejects empty or invalid required fields
  - Action: Submit the sign-up form with an empty email/password (or invalid email format).
  - Expected: Registration is blocked and a validation error is shown naming the invalid field.
- [ ] CS-02: Checkout rejects missing/invalid required payment fields
  - Action: Submit checkout with required payment fields empty or invalid (e.g., invalid card number).
  - Expected: Submission is blocked, no subscription is created, and an error message is displayed.
- [ ] CS-03: Account/checkout areas are inaccessible without signing in
  - Action: While signed out, attempt to open the account/billing page or subscribe to a plan.
  - Expected: Access is prevented — user is redirected to the sign-in/sign-up page or prompted to log in first.
- [ ] CS-04: A user cannot hold two conflicting active subscriptions for the same service
  - Action: While already subscribed to one plan, subscribe to another plan again via checkout.
  - Expected: The system does not create a duplicate subscription — it either replaces the current plan or prevents the action with a message directing to "change plan".
- [ ] CS-05: Plan change / cancellation requires explicit confirmation
  - Action: Initiate a plan change or cancellation and attempt to complete it in a single click (if no confirmation step exists, this fails).
  - Expected: A confirmation step/prompt is shown before the change or cancellation takes effect.

## Interaction
- [ ] FT-free IX-01: Selecting a billing period updates the displayed price immediately
  - Action: On the pricing page, toggle/select between Monthly, Quarterly, and Annual (e.g., a billing-cycle toggle or plan card selection).
  - Expected: The displayed prices and terms update immediately without a page reload error, showing the correct amount for the selected period.
- [ ] IX-02: Successful checkout shows a confirmation state
  - Action: Complete checkout with valid details.
  - Expected: A success message/confirmation page is displayed (e.g., "Subscription successful" or plan confirmation), not a silent failure.
- [ ] IX-03: After a plan change or cancellation, the account area updates to reflect the new state
  - Action: Confirm a plan change, then confirm a cancellation, checking the account area after each.
  - Expected: The account area immediately reflects the updated plan/status without requiring logout/login.

## Content
- [ ] CT-01: All plan and feature content is relevant to the software service
  - Action: Review the pricing page, feature descriptions, and checkout summary.
  - Expected: All text describes the software service's plans/features (no placeholder text like "Lorem ipsum", no unrelated products); prices include currency and billing period.
- [ ] CT-02: Feature descriptions are complete and non-empty
  - Action: Open each plan's feature list/description.
  - Expected: Every listed feature has a meaningful description (no empty sections, "TBD", or missing descriptions), and the plan names shown are exactly Annual, Quarterly, and Monthly.