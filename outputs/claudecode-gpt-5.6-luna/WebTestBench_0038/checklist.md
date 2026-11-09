# Test Checklist

## Functionality
- [ ] **FT-01: Visitors can view all available subscription plans.**
  - **Action:** Open the subscription/pricing page and inspect the plan cards or comparison table.
  - **Expected:** Each available plan displays a selectable option with its plan name, price, and payment frequency.

- [ ] **FT-02: Visitors can compare monthly, quarterly, and annual payment outcomes.**
  - **Action:** Select or switch between the monthly, quarterly, and annual payment options for the same plan.
  - **Expected:** The displayed price, billing interval, total payment outcome, and applicable savings or differences update for each frequency.

- [ ] **FT-03: Visitors can read detailed features for each plan.**
  - **Action:** Open the feature details for each available plan.
  - **Expected:** The application displays the plan’s complete feature description and distinguishes included features from features unavailable on that plan.

- [ ] **FT-04: A visitor can create an account from the subscription journey.**
  - **Action:** Select a plan, choose a payment frequency, and select **Create account**; submit the account form with valid information.
  - **Expected:** The account is created and the visitor proceeds to the subscription checkout flow.

- [ ] **FT-05: An account holder can subscribe through checkout.**
  - **Action:** Complete checkout for a selected plan and payment frequency using valid payment information, then select **Subscribe**.
  - **Expected:** The subscription is created for the selected plan and frequency, and a subscription confirmation is displayed.

- [ ] **FT-06: A signed-in user can view current subscription and upcoming billing information.**
  - **Action:** Sign in, open the account area, and view the subscription details.
  - **Expected:** The account area shows the current plan, payment frequency, subscription status, next billing date, and upcoming billing amount.

- [ ] **FT-07: A signed-in user can change the subscription plan or payment frequency.**
  - **Action:** In the account area, select **Change plan**, choose a different plan or payment frequency, and confirm the change.
  - **Expected:** The subscription is updated and the account area shows the newly selected plan, frequency, billing amount, and next billing information.

- [ ] **FT-08: A signed-in user can cancel the subscription.**
  - **Action:** In the account area, select **Cancel subscription** and complete the cancellation flow.
  - **Expected:** The subscription is cancelled or marked to end according to the displayed cancellation terms, and the account area shows the resulting status and end date.

## Constraint
- [ ] **CS-01: Required account and checkout fields must be completed before submission.**
  - **Action:** Leave one or more required account or payment fields empty and select **Create account** or **Subscribe**.
  - **Expected:** Submission is blocked and a validation message identifies each missing required field.

- [ ] **CS-02: The checkout summary must match the selected plan and payment frequency.**
  - **Action:** Select different plans and switch among monthly, quarterly, and annual billing before completing checkout.
  - **Expected:** The checkout summary always shows the same plan, billing interval, amount, and billing outcome selected by the user.

- [ ] **CS-03: Subscription management must require authentication.**
  - **Action:** Attempt to open the account subscription area while signed out.
  - **Expected:** The application prevents access and presents a sign-in or account-access prompt.

- [ ] **CS-04: Cancellation must not occur without explicit confirmation.**
  - **Action:** Select **Cancel subscription**, then dismiss or reject the cancellation confirmation.
  - **Expected:** The subscription remains active and the account area continues to show the existing plan and billing status.

## Interaction
- [ ] **IX-01: Selecting a plan provides a clear active-state indication.**
  - **Action:** Select a plan card or plan option, then select a different plan.
  - **Expected:** The selected option is visibly identified, and the previous option is no longer marked as selected.

- [ ] **IX-02: Changing billing frequency updates relevant pricing information immediately.**
  - **Action:** Toggle between monthly, quarterly, and annual payment options on the pricing or checkout page.
  - **Expected:** The displayed price, billing interval, total, and savings or outcome information update without requiring a page reload.

- [ ] **IX-03: Successful subscription completion provides clear confirmation and account access.**
  - **Action:** Complete a valid subscription checkout.
  - **Expected:** A success confirmation appears and the user can continue to the signed-in account area showing the new subscription.

- [ ] **IX-04: Account changes provide visible status feedback.**
  - **Action:** Change a plan or complete a cancellation from the account area.
  - **Expected:** The application displays a success or status message and refreshes the subscription details to reflect the completed action.

## Content
- [ ] **CT-01: Plan pricing and billing labels are complete and unambiguous.**
  - **Action:** Review every plan and each monthly, quarterly, and annual option.
  - **Expected:** Each option clearly identifies its price, currency, billing frequency, total or recurring amount, and any savings or differences.

- [ ] **CT-02: Feature descriptions accurately correspond to their plans.**
  - **Action:** Compare the feature descriptions shown for all available plans.
  - **Expected:** Every listed feature is relevant to the software service, uses understandable wording, and is consistently marked as included or unavailable for each plan.

- [ ] **CT-03: Account billing information clearly identifies dates, amounts, and status.**
  - **Action:** Review the current subscription and upcoming billing section for a signed-in user.
  - **Expected:** The content clearly identifies the active plan, billing frequency, next billing date, upcoming amount, subscription status, and—after cancellation—the subscription end date.