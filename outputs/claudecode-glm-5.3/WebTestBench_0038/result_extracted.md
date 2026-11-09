# Test Result

**Target:** http://localhost:6038/ (FlowSync — React SPA) · **Tester account:** `qa.tester@example.com` / `Passw0rd123` · **Verified prices:** Monthly Pro $29/Ent $99 · Quarterly Pro $79/Ent $269 · Annual Pro $290/Ent $990

## Functionality
- [ ] FT-01: Visitor can browse all subscription plans
  - Action: Open the pricing/plans page.
  - Expected: All default plans (e.g., Basic, Pro, Enterprise) are listed with name, price, and a "Subscribe"/"Choose plan" button for each.
  - Bug Report:
    - Issue: Missing Subscribe/Choose-plan action for Enterprise tier
    - Actual: Plans are listed at `/pricing` with names and prices (Free $0, Pro $29, Enterprise $99, all cycles switchable), and Free ("Get Started") and Pro ("Start Free Trial") have working subscribe CTAs, but the Enterprise plan's button is "Contact Sales" — clicking it only shows a toast "Contact Sales — Our team will reach out to discuss your enterprise needs" and opens no checkout/subscription flow. There is no way for a visitor to choose/subscribe to the Enterprise plan.

- [X] FT-02: Visitor can read detailed feature descriptions for each plan
  - Action: Click the "Learn more" / "See features" link (or expand the feature section) of any plan.
  - Expected: A detailed feature list for that plan is displayed (e.g., feature bullets with descriptions), matching the plan's tier.
  - (Verified: each plan card on `/pricing` displays an expanded, tier-matched feature list — Free: "Up to 3 projects, 1 GB storage, Community support, Basic analytics, API access (100 req/day)"; Pro adds "Unlimited projects, 50 GB storage, Priority support, Advanced analytics, API 10,000 req/day, Custom integrations, Team collaboration"; Enterprise adds "Everything in Pro, Unlimited storage, Dedicated support, SSO & SAML, Audit logs, SLA guarantee". The `/features` page additionally provides detailed per-feature descriptions with bullets.)

- [X] FT-03: Visitor can compare billing cycles (monthly / quarterly / annual)
  - Action: On the plans page, switch the billing cycle selector between "Monthly", "Quarterly", and "Annual".
  - Expected: The displayed price for each plan updates to the amount corresponding to the selected billing cycle.
  - (Verified: Monthly → Free $0/mo, Pro $29/mo, Ent $99/mo; Quarterly → $0/qtr, $79/qtr, $269/qtr with "Save 9%" and "Billed $79 every 3 months"; Annual → $0/yr, $290/yr, $990/yr with "Save 17%".)

- [X] FT-04: Visitor can compare plans against one another side by side
  - Action: View the plans/comparison page with the "Compare plans" view.
  - Expected: All plans are shown in a side-by-side layout where feature availability per plan can be directly compared (e.g., checkmarks vs. dashes).
  - (Verified: "Compare all features" table on `/pricing` with columns Free | Pro | Enterprise; boolean rows render lucide `check` (✓, highlighted) vs `x` (✗, muted) icons per plan, e.g. SSO & SAML: ✗/✗/✓, Custom Integrations: ✗/✓/✓.)

- [X] FT-05: Visitor can create an account
  - Action: Fill in the registration form (name, email, password) with valid values and submit it.
  - Expected: The account is created and the user is signed in (e.g., redirected to the account area or shown as logged in).
  - (Verified: registered "QA Tester" / qa.tester@example.com → toast "Account created! Welcome to FlowSync.", redirected to `/account`, user menu shows the name.)

- [X] FT-06: User can subscribe to a plan through the checkout flow
  - Action: While signed in, select any plan with a chosen billing cycle and complete the checkout (billing/payment details, confirm).
  - Expected: Checkout completes and the subscription to the selected plan and billing cycle becomes active.
  - (Verified twice: Pro + Quarterly → "Pay $79" → account shows "Pro Plan", Trial, $79/qtr (Quarterly); Pro + Annual → "Pay $290" → "Pro Plan", $290/yr (Annual), card •••• 4242 stored.)

- [X] FT-07: Signed-in user can view their current plan
  - Action: Sign in and open the account area / "Subscription" section.
  - Expected: The currently subscribed plan name and its billing cycle (monthly/quarterly/annual) are displayed.
  - (Verified: `/account` Subscription section shows "Pro Plan" + "$79/qtr (Quarterly)" and later "$290/yr (Annual)".)

- [X] FT-08: Signed-in user can see upcoming billing information
  - Action: Open the account area / "Billing" section.
  - Expected: Upcoming billing details are shown, including the amount to be charged and the next billing date.
  - (Verified: amount "$79/qtr" / "$290/yr" plus "Next billing date: February 6, 2027" / "November 3, 2027" and payment method "•••• •••• •••• 4242" in the account area.)

- [X] FT-09: Signed-in user can change to a different plan
  - Action: In the account area, click "Change plan", select a different plan (with a billing cycle), and confirm.
  - Expected: The current plan is updated to the newly selected plan/cycle, and the account area reflects the change.
  - (Verified: "Change Plan" dialog → selected Free $0/qtr → "Confirm change" → plan became "Free Plan, $0/qtr (Quarterly)", features list switched to Free tier, "Upgrade to Pro" button appeared. Note: selecting Enterprise in this dialog only triggers a "Contact Sales" toast and does not change the plan.)

- [X] FT-10: Signed-in user can cancel their subscription
  - Action: In the account area, click "Cancel subscription" and confirm the cancellation.
  - Expected: The subscription status changes to "Canceled" (or equivalent), and the account area shows the subscription as canceled.
  - (Verified: confirmation dialog → "Cancel subscription" → account now shows "Your subscription will end on November 3, 2027", "Access ends November 3, 2027", and a "Reactivate" button replaces "Cancel subscription"; toast "Subscription cancelled — Your subscription will end at the current billing period.")

## Constraint
- [X] CS-01: Registration cannot be submitted with empty required fields
  - Action: On the registration form, leave required fields (e.g., email, password) empty and submit.
  - Expected: The form is not submitted; a validation error indicates which required fields are missing.
  - (Verified: error toast "Please fill in all fields.", stayed on `/signup`, no account created.)

- [ ] CS-02: Registration cannot be completed with an already-registered email
  - Action: Attempt to register using the email of an existing default account.
  - Expected: Registration is rejected with an error such as "Email already in use"; no duplicate account is created.
  - Bug Report:
    - Issue: Duplicate email registration accepted / no uniqueness validation
    - Actual: After creating `qa.tester@example.com`, registering again with the same email under name "Duplicate User" succeeded — no "Email already in use" error; a second account with the identical email was created and I was signed in as "Duplicate User" on `/account`.

- [ ] CS-03: Checkout cannot be completed with empty or invalid payment details
  - Action: Start checkout for a plan and submit with empty or malformed payment fields (e.g., blank card number).
  - Expected: Checkout is blocked; an error indicates the payment details are missing/invalid, and no subscription is created.
  - Bug Report:
    - Issue: No validation of malformed payment details
    - Actual: Empty fields are correctly blocked with "Please fill in all payment details.", but submitting malformed values — Card Number "1234" (4 digits, not a card number), Expiry "13/45" (invalid month 13), CVC "1" — was accepted without any error. Checkout completed, a toast "Success! You're now subscribed to the Pro plan." appeared, and a Pro/Quarterly subscription was created (account even displays a hard-coded card "•••• •••• •••• 4242" regardless of the entered number).

- [X] CS-04: Checkout requires a plan and billing cycle to be selected
  - Action: Attempt to open/submit the checkout without any plan or billing cycle chosen.
  - Expected: The checkout cannot proceed; the user is prompted to select a plan and billing cycle first.
  - (Verified: with no plan selected, navigating to `/checkout` does not render checkout — SPA navigation redirects back to `/pricing` where the billing-cycle selector and plan buttons are shown; a hard load of `/checkout` also redirects away (to `/login` due to an auth-hydration race, while still signed in). Checkout is only reachable via a plan button that carries both plan and cycle, e.g. Pro + Quarterly → "Pay $79".)

- [X] CS-05: Cancellation requires explicit confirmation
  - Action: In the account area, click "Cancel subscription" but dismiss/abort the confirmation step.
  - Expected: The subscription remains active; no cancellation is applied without explicit confirmation.
  - (Verified: dialog "Cancel subscription?" → clicked "Keep subscription" → dialog closed, plan still "Pro Plan $290/yr (Annual)", next billing date intact, "Cancel subscription" button still available.)

- [X] CS-06: Subscription actions are unavailable to signed-out visitors
  - Action: While signed out, attempt to access the account area / manage subscription pages directly.
  - Expected: The user cannot view or manage any subscription; they are redirected to sign in.
  - (Verified: signed-out navigation to `/account` redirected to `/login` (page URL became http://localhost:6038/login with the sign-in form); nav shows "Sign in"/"Get Started" only.)

## Interaction
- [X] IX-01: Billing cycle selector updates prices immediately
  - Action: On the plans page, click between "Monthly", "Quarterly", and "Annual" toggles.
  - Expected: Plan prices update instantly without a page reload, and the selected cycle is visually highlighted.
  - (Verified: a `window` marker survived all three toggles → no full reload; prices swapped instantly ($29→$79→$290 for Pro); the active toggle receives the highlighted style `bg-primary text-primary-foreground shadow-md`.)

- [X] IX-02: Checkout shows a success confirmation after subscribing
  - Action: Complete a valid checkout.
  - Expected: A success message/confirmation (e.g., "Subscription successful" toast or confirmation page) is shown to the user.
  - (Verified: toast "Success! You're now subscribed to the Pro plan." on redirect to `/account` after "Pay $79" and again after "Pay $290".)

- [X] IX-03: Plan change shows a confirmation of the new plan
  - Action: Complete a plan change in the account area.
  - Expected: Feedback is shown confirming the plan change (e.g., "Your plan has been updated" message).
  - (Verified: toast "Plan updated! You've switched to the Free plan." and the Subscription section immediately showed "Free Plan $0/qtr (Quarterly)".)

- [X] IX-04: Cancellation shows a confirmation of cancellation
  - Action: Confirm the cancellation of a subscription.
  - Expected: Feedback is shown confirming the cancellation (e.g., "Your subscription has been canceled" message).
  - (Verified: toast "Subscription cancelled — Your subscription will end at the current billing period." plus in-page "Your subscription will end on November 3, 2027".)

## Content
- [X] CT-01: Displayed prices are consistent with the selected billing cycle and plan
  - Action: Compare the price shown on the plans page for each plan/cycle combination against the price charged at checkout and shown in billing.
  - Expected: The amounts are consistent for the same plan and billing cycle across plans page, checkout, and billing section.
  - (Verified for Pro Quarterly: pricing page "$79/qtr" → checkout "Total today $79 / Pay $79" → account billing "$79/qtr (Quarterly)". Verified for Pro Annual: pricing "$290/yr" → checkout "Total today $290 / Pay $290" → account "$290/yr (Annual)". Amounts match across all three surfaces.)

- [X] CT-02: All plan content is relevant to the software service theme
  - Action: Review plan names, feature descriptions, and marketing text on the plans and comparison pages.
  - Expected: All text and features describe software-service capabilities (e.g., seats, storage, API access); no irrelevant or placeholder content is present.
  - (Verified: features are all software-SaaS capabilities — projects, storage (1 GB/50 GB/unlimited), API requests (100/day → unlimited), team members/seats, analytics tiers, support tiers, Custom Integrations, SSO & SAML, Audit Logs, SLA guarantee; marketing copy ("Streamline Your Workflow", "14-day free trial", "Trusted by 10,000+ teams") matches the workflow-automation theme. No lorem-ipsum/placeholder text found on `/`, `/pricing`, `/features`.)
