All test items have been executed. Here is the complete checklist with results:

# Test Result

## Functionality
- [ ] FT-01: Pricing page displays all three billing periods as comparable plans
  - Action: Open the pricing/plans page.
  - Expected: Three plans are shown — Annual, Quarterly, and Monthly — each with a visible price, and they are laid out so they can be compared side by side (e.g., in a comparison table or pricing cards).
  - Bug Report:
    - Issue: Incorrect Plan Structure / Mismatched Content
    - Actual: The pricing page shows three tier plans named **Free, Pro, Enterprise** (not Annual, Quarterly, Monthly). Billing periods exist only as a toggle (Monthly/Quarterly/Annual buttons) that changes prices for all three tiers — only one period is visible at a time, so the three billing periods are never shown side by side with prices.

- [ ] FT-02: Detailed feature descriptions are available for each plan
  - Action: View each plan's feature list or open its detailed description.
  - Expected: Every plan (Annual, Quarterly, Monthly) shows a list of features with descriptions, and differences between plans (e.g., which features are included) are visible/indicated.
  - Bug Report:
    - Issue: Missing Feature Descriptions / Wrong Plan Names
    - Actual: Plans show feature bullet lists (e.g., "Unlimited projects", "50 GB storage") with **no per-feature descriptions**. The plan names are Free/Pro/Enterprise, not Annual/Quarterly/Monthly. (Feature descriptions do exist on the separate /features page, but not on the plans.)

- [X] FT-03: Visitor can create a new account
  - Action: Click the sign-up/register button, enter a valid email, password, and any required fields, then submit.
  - Expected: Account is created, user is signed in, and a signed-in state is visible (e.g., account name/avatar in the header).
  - Actual: Account created for testuser@example.com; header shows the signed-in user name ("Test User"). PASS.

- [X] FT-04: Signed-in user can subscribe to a plan via checkout
  - Action: While signed in, select a plan (e.g., Monthly) and complete the checkout form with valid payment details, then submit.
  - Expected: Subscription is created successfully and a confirmation is shown indicating the active plan.
  - Actual: Checkout with Pro/Monthly completed → "Success! You're now subscribed to the Pro plan." PASS.

- [X] FT-05: Account area shows the user's current plan
  - Action: After subscribing, open the account/billing area.
  - Expected: The currently subscribed plan name (matching the one purchased) and its status (e.g., Active) are displayed.
  - Actual: Account shows "Pro Plan" with status "Trial" (14-day free trial), matching the purchased plan. PASS.

- [ ] FT-06: Account area shows upcoming billing information
  - Action: Open the account area after subscribing to the Monthly plan.
  - Expected: An upcoming billing/renewal date and the amount to be charged are displayed, consistent with the plan's billing cycle.
  - Bug Report:
    - Issue: Missing Amount-to-be-Charged
    - Actual: Account shows "Next billing date: December 8, 2026" and card "•••• 4242", but **no amount to be charged is displayed**. DOM scan for "amount|charge|due|renewal|total" found nothing in the account subscription section.

- [X] FT-07: User can change to a different plan
  - Action: In the account area, use the change-plan option to switch from the current plan to a different one (e.g., Monthly → Annual) and confirm.
  - Expected: The change succeeds and the account area now shows the new plan as the current plan.
  - Actual: Change Pro → Free succeeded with confirmation dialog; account now shows "Free Plan" / "$0/mo (Monthly)". PASS. (Note: selecting Enterprise in the change dialog opens a "Contact Sales" page instead of changing the plan — only Free/Pro changes are supported.)

- [X] FT-08: User can cancel their subscription
  - Action: In the account area, click the cancel-subscription option and confirm.
  - Expected: The subscription is cancelled; the account area reflects cancelled status (e.g., "Cancelled" or plan expiry) and no upcoming charge is shown.
  - Actual: After confirmation, account shows "Subscription cancelled — Your subscription will end at the current billing period", "Your subscription will end on December 8, 2026", and a "Reactivate" button. The next-billing-date line (upcoming charge) is removed. PASS. (Note: the Free plan has no cancel button — only "Upgrade to Pro" — since it has no billing; cancellation was tested on the paid Pro plan.)

- [X] FT-09: Billing outcomes differ across the three payment plans
  - Action: Note the price and billing terms for Annual, Quarterly, and Monthly (e.g., Annual = $X/year, Quarterly = $Y/quarter, Monthly = $Z/month) and check any stated totals/savings.
  - Expected: The three plans produce different outcomes (different prices/cadence/savings, e.g., Annual is cheaper per period than Monthly), and these differences are accurately reflected in checkout and billing info.
  - Actual: Monthly $29/mo; Quarterly $79/qtr (Save 9%, $26.33/mo equivalent); Annual $290/yr (Save 17%, $24.17/mo equivalent). Checkout for Annual showed "Billed annual, $290, Save 17%, $24.17/mo equivalent, Total today $290, Pay $290"; account after purchase showed "$290/yr (Annual)" with next billing Nov 3, 2027; monthly showed "$29/mo (Monthly)", next billing Dec 8, 2026. Differences accurately reflected. PASS.

- [ ] FT-10: A plan comparison view aligns plans against one another
  - Action: Use the comparison view/table (or toggle to compare plans) on the pricing page.
  - Expected: Features/prices for Annual, Quarterly, and Monthly are displayed in a directly comparable format (e.g., same rows across plans), so differences are readable at a glance.
  - Bug Report:
    - Issue: Comparison Table Does Not Compare Billing Periods
    - Actual: A "Compare all features" table exists with columns **Feature / Free / Pro / Enterprise** (rows: Projects, Storage, API Requests, Team Members, Analytics, Support, Custom Integrations, SSO & SAML, Audit Logs, SLA Guarantee). It does not compare Annual/Quarterly/Monthly — no prices appear in the table, and billing periods are not columns.

## Constraint
- [X] CS-01: Account creation rejects empty or invalid required fields
  - Action: Submit the sign-up form with an empty email/password (or invalid email format).
  - Expected: Registration is blocked and a validation error is shown naming the invalid field.
  - Actual: Empty fields → blocked with "Error: Please fill in all fields." Invalid email ("not-an-email") → blocked by native HTML validation (email input typeMismatch=true, validationMessage present). PASS.

- [ ] CS-02: Checkout rejects missing/invalid required payment fields
  - Action: Submit checkout with required payment fields empty or invalid (e.g., invalid card number).
  - Expected: Submission is blocked, no subscription is created, and an error message is displayed.
  - Bug Report:
    - Issue: Invalid Payment Data Accepted
    - Actual: Empty payment fields are correctly blocked ("Please fill in all fields"). However, **invalid payment data was accepted and a subscription was created**: card number "1234", expiry "13/25", CVC "1" → "Success! You're now subscribed to the Pro plan." No validation error was shown for the invalid card number/expiry/CVC.

- [X] CS-03: Account/checkout areas are inaccessible without signing in
  - Action: While signed out, attempt to open the account/billing page or subscribe to a plan.
  - Expected: Access is prevented — user is redirected to the sign-in/sign-up page or prompted to log in first.
  - Actual: While signed out, clicking "Start Free Trial" on Pro redirected to the signup page; navigating directly to /account while signed out redirected to /login ("Welcome back — Sign in to your FlowSync account"). PASS.

- [X] CS-04: A user cannot hold two conflicting active subscriptions for the same service
  - Action: While already subscribed to one plan, subscribe to another plan again via checkout.
  - Expected: The system does not create a duplicate subscription — it either replaces the current plan or prevents the action with a message directing to "change plan".
  - Actual: While subscribed to Pro, the Pro card on the pricing page shows "Current Plan" (disabled, no checkout possible). Re-subscribing to the same plan is prevented. PASS.

- [X] CS-05: Plan change / cancellation requires explicit confirmation
  - Action: Initiate a plan change or cancellation and attempt to complete it in a single click (if no confirmation step exists, this fails).
  - Expected: A confirmation step/prompt is shown before the change or cancellation takes effect.
  - Actual: Plan change opens a "Change your plan" dialog requiring plan selection + "Confirm change" click; cancellation opens a "Cancel subscription?" dialog with "Your subscription will remain active until December 8, 2026..." and "Keep subscription"/"Cancel subscription" buttons. PASS.

## Interaction
- [X] FT-free IX-01: Selecting a billing period updates the displayed price immediately
  - Action: On the pricing page, toggle/select between Monthly, Quarterly, and Annual (e.g., a billing-cycle toggle or plan card selection).
  - Expected: The displayed prices and terms update immediately without a page reload error, showing the correct amount for the selected period.
  - Actual: Toggle Monthly → Quarterly → Annual updated prices immediately ($29/mo → $79/qtr with "Save 9%, $26.33/mo equivalent" → $290/yr with "Save 17%, $24.17/mo equivalent"), no page reload, no errors. PASS.

- [X] IX-02: Successful checkout shows a confirmation state
  - Action: Complete checkout with valid details.
  - Expected: A success message/confirmation page is displayed (e.g., "Subscription successful" or plan confirmation), not a silent failure.
  - Actual: After payment, redirected to /account with "Success! You're now subscribed to the Pro plan." (and a toast notification). PASS.

- [X] IX-03: After a plan change or cancellation, the account area updates to reflect the new state
  - Action: Confirm a plan change, then confirm a cancellation, checking the account area after each.
  - Expected: The account area immediately reflects the updated plan/status without requiring logout/login.
  - Actual: After plan change confirmation: "Plan updated! You've switched to the Free plan." and the account immediately showed "Free Plan". After cancellation confirmation: "Subscription cancelled" and the account immediately showed the end date + Reactivate. No logout/login needed. PASS.

## Content
- [X] CT-01: All plan and feature content is relevant to the software service
  - Action: Review the pricing page, feature descriptions, and checkout summary.
  - Expected: All text describes the software service's plans/features (no placeholder text like "Lorem ipsum", no unrelated products); prices include currency and billing period.
  - Actual: All content is about FlowSync (workflow automation software); no "Lorem ipsum" or placeholder text found; prices include currency and billing period ($29/mo, $79/qtr, $290/yr). PASS.

- [ ] CT-02: Feature descriptions are complete and non-empty
  - Action: Open each plan's feature list/description.
  - Expected: Every listed feature has a meaningful description (no empty sections, "TBD", or missing descriptions), and the plan names shown are exactly Annual, Quarterly, and Monthly.
  - Bug Report:
    - Issue: Plan Names Mismatch
    - Actual: The plan names shown are **Free, Pro, and Enterprise** — not Annual, Quarterly, and Monthly as expected. Feature list items are short labels without descriptions (e.g., "Unlimited projects", "50 GB storage"). No empty sections or "TBD" found, but the plan-name requirement is not met. (The /features page does have full descriptions for the four feature categories, but it is not tied to the three plans.)

---

**Summary of confirmed bugs:** The app's pricing model is built around three tier plans (Free/Pro/Enterprise) with a billing-period toggle, rather than the three period-based plans (Annual/Quarterly/Monthly) the checklist expects — this affects FT-01, FT-02, FT-10, and CT-02. Additionally, checkout accepts invalid payment data (CS-02), and the account area omits the next charge amount (FT-06).