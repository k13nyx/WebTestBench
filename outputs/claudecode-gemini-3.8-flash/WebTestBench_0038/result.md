# Test Result

## Functionality
- [X] FT-01: Compare pricing plans across billing cycles
  - Action: Select each billing cycle option ("Monthly", "Quarterly", "Annual") on the pricing page.
  - Expected: The pricing cards update immediately to show the corresponding rates and billing intervals for each plan.
- [ ] FT-02: View detailed feature descriptions
  - Action: Click on a plan's "View Features" link or expandable feature section.
  - Expected: An expanded list or modal opens displaying in-depth descriptions of all included software service features.
  - Bug Report:
    - Issue: Missing Element
    - Actual: Neither a "View Features" link nor an expandable feature section exists on the pricing cards or comparison section; clicking to open an expanded list or modal displaying in-depth feature descriptions is unavailable.
- [X] FT-03: Complete account creation and subscription checkout
  - Action: Select a plan, fill out the registration form with valid credentials, enter valid payment details, and click "Subscribe".
  - Expected: The account is registered, payment is processed, and the user is redirected to a subscription confirmation screen.
- [X] FT-04: View current plan and upcoming billing details
  - Action: Navigate to the "Billing" section inside the signed-in user's account area.
  - Expected: Displays the active plan name, renewal date, billing cycle frequency, and upcoming charge amount.
- [X] FT-05: Change active subscription plan
  - Action: Click "Change Plan" in the account area, select a different tier or billing cycle, and confirm the switch.
  - Expected: The subscription updates to the newly selected plan, and the account reflects the adjusted plan details and next billing amount.
- [X] FT-06: Cancel active subscription
  - Action: Click "Cancel Subscription" in the account area and confirm the cancellation prompt.
  - Expected: The subscription status changes to "Canceled" (or "Pending Cancellation"), and automatic renewal is disabled.

## Constraint
- [ ] CS-01: Mandatory field validation during checkout
  - Action: Attempt to submit the checkout form with required fields (e.g., email, password, card details) left blank.
  - Expected: Submission is blocked and inline validation error messages appear beneath each missing required field.
  - Bug Report:
    - Issue: Incorrect Form Submission
    - Actual: Submission is blocked, but no inline validation error messages appear beneath each missing required field; instead, only a generic toast notification ("Please fill in all payment details.") is displayed.
- [ ] CS-02: Prevent selecting the currently active plan
  - Action: Open the "Change Plan" interface in the account area and locate the currently active plan.
  - Expected: The active plan's action button is disabled and labeled "Current Plan", preventing re-selection.
  - Bug Report:
    - Issue: Incorrect Element Label
    - Actual: While the active plan button is disabled to prevent re-selection, it is labeled with "(current)" (e.g., "Pro(current)") rather than "Current Plan".
- [X] CS-03: Prevent accidental cancellation without confirmation
  - Action: Click the "Cancel Subscription" button in the account dashboard.
  - Expected: System displays a confirmation dialog asking the user to confirm or keep the subscription before any cancellation takes effect.
- [X] CS-04: Restrict unauthenticated access to account billing area
  - Action: Enter the direct URL for the account billing page into an unauthenticated browser session.
  - Expected: Access is blocked and the browser redirects to the sign-in page.

## Interaction
- [X] IX-01: Active billing toggle visual feedback
  - Action: Click between "Monthly", "Quarterly", and "Annual" options on the billing toggle control.
  - Expected: The selected tab dynamically highlights with an active visual state (e.g., contrasting pill background) while non-selected tabs dim.
- [ ] IX-02: Plan card hover state
  - Action: Hover the mouse cursor over an individual plan card on the comparison page.
  - Expected: The hovered card visually elevates with a drop-shadow or border color change to indicate focus.
  - Bug Report:
    - Issue: Missing Element Style
    - Actual: When hovering over a plan card, the card elevates via CSS translateY transform (`hover:-translate-y-1`), but neither a drop-shadow change nor a border color change is applied.
- [ ] IX-03: Plan modification confirmation alert
  - Action: Finalize a plan change or cancellation in the account area.
  - Expected: A dismissible success toast notification appears at the top of the viewport confirming the update.
  - Bug Report:
    - Issue: Incorrect Element Placement
    - Actual: The dismissible success toast notification appears anchored to the bottom-right of the viewport (`sm:bottom-0 sm:right-0 sm:top-auto`) instead of at the top of the viewport.

## Content
- [X] CT-01: Plan comparison table feature accuracy
  - Action: Review the side-by-side plan comparison table on the main subscription page.
  - Expected: Lists all available tiers with software service feature names, checkmarks, limits, and tier names clearly distinguished.
- [X] CT-02: Billing period outcome and savings display
  - Action: Switch between Monthly, Quarterly, and Annual billing options.
  - Expected: Displays the calculated breakdown including per-month equivalent costs, total billed amounts, and applicable savings badges (e.g., "Save 20% on Annual").
- [ ] CT-03: Renewal terms and cancellation policy visibility
  - Action: Inspect the checkout review step and account billing overview.
  - Expected: Explicit text is visible detailing recurring renewal terms, next charge dates, and cancellation policy guidelines.
  - Bug Report:
    - Issue: Missing Element
    - Actual: The checkout review step lacks explicit text detailing recurring renewal terms, next charge dates, and cancellation policy guidelines; additionally, cancellation policy guidelines are not visibly displayed on the account billing overview.