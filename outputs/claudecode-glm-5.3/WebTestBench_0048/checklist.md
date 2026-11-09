# Test Checklist

## Functionality
- [ ] FT-01: User can log in with valid credentials
  - Action: On the login page, enter a valid username and password, then click the "Log In" button.
  - Expected: User is logged in and taken to the policy list page (or personal center).
- [ ] FT-02: User can browse the list of company policies and procedures
  - Action: After logging in, view the policy list page.
  - Expected: A list of pre-existing company policies/procedures is displayed, each showing its title.
- [ ] FT-03: User can open a specific policy to read its full content
  - Action: Click the title of a pending policy in the list.
  - Expected: A detail view opens showing the complete policy content.
- [ ] FT-04: User can complete the read-and-understood confirmation step
  - Action: In an opened pending policy's detail view, check the "I have read and understood" acknowledgment and click the "Confirm" button.
  - Expected: The confirmation is recorded and the policy's status becomes "Confirmed".
- [ ] FT-05: User can see which items are confirmed and which are pending
  - Action: Review the entries in the policy list.
  - Expected: Every item is visibly labeled with its confirmation status (e.g., "Confirmed" / "Pending"); no item lacks a status.
- [ ] FT-06: Confirmation Progress Dashboard shows a doughnut chart of confirmed vs. pending
  - Action: Navigate to the Personal Center and open the Confirmation Progress Dashboard.
  - Expected: A doughnut chart is displayed showing the proportion of confirmed items vs. pending items.
- [ ] FT-07: Dashboard categorizes confirmation status by policy type
  - Action: On the Confirmation Progress Dashboard, view the category breakdown section.
  - Expected: All four policy types are shown — Administration, Human Resources, Finance, Compliance — each with its own confirmation status (confirmed/pending counts).
- [ ] FT-08: Doughnut chart reflects a new confirmation
  - Action: Confirm one pending policy, then return to the Confirmation Progress Dashboard.
  - Expected: The doughnut chart and counts update (confirmed +1, pending −1) compared to before.
- [ ] FT-09: Confirmed status persists across sessions
  - Action: Confirm a policy, log out, then log back in and open the policy list.
  - Expected: The previously confirmed policy still shows "Confirmed" (and the dashboard reflects it).

## Constraint
- [ ] CS-01: Cannot log in with empty credentials
  - Action: Leave the username and/or password fields empty and click "Log In".
  - Expected: Login is blocked and a validation message is shown; user is not taken to the policy list.
- [ ] CS-02: Confirmation cannot be submitted without the acknowledgment
  - Action: On a pending policy's detail view, attempt to submit the confirmation without checking the "I have read and understood" checkbox.
  - Expected: Confirmation is not recorded; the button is disabled or a validation error is shown.
- [ ] CS-03: An already-confirmed policy cannot be confirmed again
  - Action: Open a policy that is already marked "Confirmed".
  - Expected: No active confirmation step is available (button absent or disabled); the confirmed status cannot be reverted to pending.
- [ ] CS-04: Policies with a deadline within 3 days are automatically high priority and pinned to top
  - Action: Locate a pending policy whose confirmation deadline falls within the next 3 days (per default data) and check its position and tag in the list.
  - Expected: It is automatically tagged "High" priority without any manual action and appears at the top of the list, above non-urgent pending items.

## Interaction
- [ ] IX-01: Success feedback appears after confirming a policy
  - Action: Submit the confirmation for a pending policy.
  - Expected: A success message/toast (e.g., "Confirmation recorded") is displayed.
- [ ] IX-02: Policy list status updates immediately after confirmation
  - Action: After confirming a policy, navigate back to the policy list without reloading.
  - Expected: The item's status label changes from "Pending" to "Confirmed" instantly, with no manual refresh or re-login required.
- [ ] IX-03: Pending items display visually distinct priority tags
  - Action: View pending items in the policy list.
  - Expected: Each pending item shows a priority tag — High / Medium / Low — with distinguishable visual styling (e.g., different colors), where High stands out from Medium and Low.

## Content
- [ ] CT-01: All policy content is relevant and complete
  - Action: Open several policies from the list and read their detail pages.
  - Expected: Every title and body contains actual company policy/procedure content related to internal operations — no placeholder text, broken formatting, or empty pages.
- [ ] CT-02: Policy categories match the four defined types only
  - Action: Check the category labels shown across the policy list and dashboard.
  - Expected: Every policy is classified under exactly one of: Administration, Human Resources, Finance, Compliance — no other or missing category values appear.
- [ ] CT-03: Doughnut chart data matches actual list counts
  - Action: Count confirmed and pending policies in the list, then compare with the doughnut chart's segments and any displayed numbers/legend on the dashboard.
  - Expected: The chart's confirmed/pending proportions and counts exactly match the real list data.