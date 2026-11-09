# Test Result

## Functionality
- [X] FT-01: Pricing landing page presents the subscription plans for comparison
  - Action: Open the home/pricing page and count the distinct plan cards (e.g., "Starter", "Pro", "Business").
  - Expected: At least 3 plan cards are visible, each showing plan name, its price, and a call-to-action button such as "Choose plan" / "Subscribe".
  - Note: 3 cards present — Free ($0/mo, "Get Started"), Pro ($29/mo, "Start Free Trial"), Enterprise ($99/mo, "Contact Sales").

- [X] FT-02: Side-by-side plan comparison is available to visitors
  - Action: Click the "Compare Plans" / "View comparison" control on the pricing page.
  - Expected: A comparison view/table appears listing features as rows and the plans as columns, showing which plan includes each feature.
  - Note: No explicit "Compare Plans" button exists, but the "Compare all features" table is always visible on the pricing page — 10 feature rows × Free/Pro/Enterprise columns with text values and check/cross icons. Outcome satisfied.

- [X] FT-03: Detailed feature descriptions are readable
  - Action: Open a plan's feature detail ("Features", "See what's included", or an individual feature row/expander).
  - Expected: Each listed feature has a descriptive text explaining it (not only a name or a check mark).
  - Note: /features page gives each feature a descriptive paragraph (Real-time Collaboration, AI-Powered Automation, Advanced Analytics, Enterprise Security) plus sub-bullets; plan cards list concrete feature descriptions ("API access (100 req/day)").

- [X] FT-04: Annual, quarterly, and monthly periods yield different outcomes and can be compared
  - Action: On the pricing page, select each period in the "Monthly / Quarterly / Annual" selector, note the price per plan, then start checkout for the same plan under two different periods.
  - Expected: The displayed price and the checkout summary charge change per period (monthly price ≠ quarterly total ≠ annual total), and all three periods remain directly comparable on the same screen.
  - Note: Pro: $29/mo vs $79/qtr vs $290/yr; checkout "Pay $29" (monthly) vs "Pay $290 / Billed annual / Total today $290". All three periods toggle on the same screen with "$26.33/mo equivalent", "Billed $79 every 3 months", and "Save X%" labels aiding comparison.

- [X] FT-05: Visitor can create an account
  - Action: Click "Sign up" / "Create account", enter a valid unused email and password, submit.
  - Expected: The account is created and the visitor is signed in and routed to the dashboard/account area.
  - Note: Signed up qa.tester118@example.com → toast "Account created! Welcome to FlowSync." → routed to /account with user name/email shown.

- [X] FT-06: Signed-in user can subscribe through a simple checkout flow
  - Action: From a plan, click "Subscribe", pick a billing period, enter payment details on one short form, click "Confirm subscription" / "Pay".
  - Expected: Checkout completes in a single flow and the account's subscription becomes active for the chosen plan and period.
  - Note: Pro CTA → /checkout (4-field card form, "Pay $290") → success toast "Success! You're now subscribed to the Pro plan." → /account shows Pro Plan $290/yr (Annual), Trial badge, active.

- [X] FT-07: Account area shows the current plan
  - Action: Sign in as a subscribed user and open the account/billing area.
  - Expected: The active plan name and billing period (e.g., "Pro — Annual") are displayed and match what was purchased.
  - Note: Account shows "Pro Plan — $290/yr (Annual)", matching the purchased Pro/Annual checkout.

- [X] FT-08: Account area shows upcoming billing information
  - Action: Open the account/billing area of an active subscriber.
  - Expected: Next billing/charge date and the amount that will be charged for the current period are both shown.
  - Note: "Next billing date: November 3, 2027" and the charge amount "$290/yr" both displayed (card •••• 4242 also shown).

- [ ] FT-09: Signed-in user can change to a different plan
  - Action: In the account area, click "Change plan" / "Switch plan", select another plan and period, and confirm.
  - Expected: The account area updates to show the new plan and the new period's price/next charge; the old plan is no longer shown as active.
  - Bug Report:
    - Issue: Missing period selector in Change Plan dialog; Enterprise plan change silently no-ops
    - Actual: The "Change your plan" dialog only lists Free/Pro/Enterprise with prices at the *current* period ($0/yr, $290/yr, $990/yr) — there is no way to select a different period, so "select another plan and period" cannot be performed. Plan changes between Free and Pro do work with correct feedback, but selecting Enterprise and clicking "Confirm change" produces no plan change at all: the account stays "Pro Plan $290/yr (Annual)" and an unrelated "Contact Sales" toast appears with no error or explanation.

## Constraint
- [X] CS-01: Account creation rejects invalid or missing required data
  - Action: Submit the sign-up form with the email field empty, then with an invalid string such as `notanemail`, then with an empty/short password.
  - Expected: Each submission is blocked with a field-level validation message and no account is created.
  - Note: Empty submit → error "Please fill in all fields."; `notanemail` → blocked with field message "Please include an '@' in the email address..."; password "123" → "Password must be at least 6 characters." All stayed on /signup; no account created.

- [ ] CS-02: An email address cannot be registered twice
  - Action: Sign up using an email that already has an account.
  - Expected: Registration is rejected with a message indicating the email is already in use, and the existing account is unaffected.
  - Bug Report:
    - Issue: Duplicate email registration accepted (no uniqueness check) and it overwrote the existing account
    - Actual: Signing up again with qa.tester118@example.com succeeded — "Account created! Welcome to FlowSync." toast and redirect to /account. No "email already in use" message. The existing account was also affected: its display name was changed from "QA Tester" to "Duplicate User" and the password was replaced by the new signup's password.

- [X] CS-03: Account area is only reachable by signed-in users
  - Action: While signed out, navigate directly to the account/billing URL.
  - Expected: The subscription details are not shown; the visitor is redirected to (or prompted for) login/sign-up.
  - Note: /account while signed out → redirected to /login ("Welcome back — Sign in to your FlowSync account"); no subscription data shown.

- [ ] CS-04: Checkout cannot be completed without a selected plan/period and valid payment details
  - Action: Open checkout and attempt to confirm with a payment card field empty or invalid (e.g., `123`), and attempt to confirm with no period selected.
  - Expected: Submission is blocked with an inline validation error and no subscription is created.
  - Bug Report:
    - Issue: Checkout submits with empty/invalid payment fields — no validation
    - Actual: Clicking "Pay $29" with all four card fields (Cardholder Name, Card Number, Expiry, CVC) completely empty completed the payment: the app navigated to /account showing an active "Pro Plan — $29/mo (Monthly)" subscription with card "•••• •••• •••• 4242". No inline validation error was displayed. An invalid card number ("123") was likewise accepted. (The "no period selected" case could not occur — checkout always inherits a period from the pricing-page toggle, there is no unselected state to test.)

- [ ] CS-05: Cancellation is confirmed and stops future billing
  - Action: Click "Cancel subscription", dismiss the confirmation prompt, then re-open and confirm it.
  - Expected: Dismissing leaves the subscription active; after confirming, no upcoming charge date is shown and further plan changes require re-subscribing.
  - Bug Report:
    - Issue: Plan changes after cancellation do not require re-subscribing; cancelled state is silently overwritten
    - Actual: First two clauses passed — clicking "Keep subscription" in the "Cancel subscription?" modal left the Pro plan active, and after confirming, the "Next billing date" line disappeared (replaced by "Your subscription will end on November 3, 2027" / "Reactivate"). However, while cancelled, the "Change Plan" button remained fully available: opening the dialog, selecting Free, and confirming switched the account directly to "Free Plan $0/yr" with a "Plan updated!" toast — no checkout/re-subscribe/payment step, and the cancellation state ("will end on…/Reactivate") vanished silently from the account area.

## Interaction
- [X] IX-01: The billing-period selector updates the whole page immediately
  - Action: Click "Quarterly" then "Annual" in the period toggle while watching the plan cards and comparison table.
  - Expected: The selected period becomes visually active and all prices/savings labels update in place without a manual reload of the page.
  - Note: Clicking Quarterly/Annual moved the active styling (bg-primary + shadow-md) to the selected button and instantly re-rendered card prices ($29/mo → $79/qtr → $290/yr) with "Save 9%/17%" badges and "$26.33/mo equivalent" labels, all without a page reload.

- [X] IX-02: Subscription and plan changes give visible feedback
  - Action: Complete a checkout, then perform a plan change in the account area.
  - Expected: Each action produces a confirmation (success message/toast or a confirmation screen naming the plan and period), and the account area refreshes to the new state.
  - Note: Checkout → toast "Success! You're now subscribed to the Pro plan." and account refreshed to Pro Annual instantly. Plan change → toast "Plan updated! You've switched to the Free plan." and account refreshed to Free instantly.

- [ ] IX-03: Plan CTAs carry context into checkout
  - Action: Click the "Subscribe" / "Choose plan" button on two different plans from the pricing page.
  - Expected: Checkout opens with that specific plan preselected, and the back/return path brings the user back to the pricing/comparison view.
  - Bug Report:
    - Issue: Only one plan's CTA enters checkout; second-plan CTAs do not carry plan context
    - Actual: The Pro CTA works correctly ("Start Free Trial" → /checkout with "Order Summary / Pro Plan" preselected, and its "Back" control returns to /pricing). But for the other two plans the requirement fails: the Free card's "Get Started" button is completely unresponsive for a signed-in user (no navigation, no toast, no state change), and the Enterprise card's "Contact Sales" button only shows a "Our team will reach out…" toast without any checkout/contact page. Thus a checkout preselected for two different plans is not achievable.

## Content
- [X] CT-01: All plan content is real and relevant to a software subscription service
  - Action: Read every plan card, the comparison table, and the feature descriptions on the pricing page.
  - Expected: Names, prices, and feature text are specific to the software service (no lorem ipsum, "Plan 1/Feature A" placeholders, `$0.00`, `Lorem`, or broken/missing images or icons).
  - Note: Plans Free/Pro/Enterprise with real prices ($0/$29/$79/$99/$269/$290/$990) and workflow-tool features (projects, storage, API request limits, SSO & SAML, audit logs, SLA). No lorem ipsum, no placeholder names, no `$0.00` artifacts; icons render as inline SVG elements throughout.

- [ ] CT-02: Pricing and feature data are consistent across views
  - Action: For one plan, compare the price and included-features list on the pricing card against the comparison table, the checkout summary, and the account area after subscribing.
  - Expected: The same price for the chosen period and the same set of features appear in all four places (no contradictions such as a check-marked feature missing from the account area).
  - Bug Report:
    - Issue: Feature list inconsistent between checkout summary and the other three views
    - Actual: Prices were consistent everywhere (Pro card $290/yr = checkout "Total today $290" = comparison table = account "$290/yr"). However, the pricing card and account area both list 7 Pro features (Unlimited projects, 50 GB storage, Priority support, Advanced analytics, API access (10,000 req/day), Custom integrations, Team collaboration), while the checkout Order Summary lists only the first 5 — "Custom integrations" and "Team collaboration" are omitted from checkout even though the comparison table marks them ✓ for Pro.
