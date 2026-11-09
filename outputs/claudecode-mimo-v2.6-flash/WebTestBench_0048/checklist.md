# Test Checklist

## Functionality
- [ ] FT-01: User can log in with valid credentials
  - Action: Enter valid username and password on the login page and submit.
  - Expected: Login succeeds and the user is taken to the main policy browsing view.

- [ ] FT-02: Policy list displays available policies and procedures
  - Action: After login, view the policies/procedures list.
  - Expected: A list of company policies and procedures is shown with each item's title, type, and status.

- [ ] FT-03: User can open a specific policy item and read it
  - Action: Click on a policy item in the list.
  - Expected: The item's detail page opens showing the full policy content.

- [ ] FT-04: User can complete the read-and-understood confirmation step
  - Action: On a policy detail page, perform the confirmation step (acknowledge "read and understood") and submit it.
  - Expected: The confirmation is recorded and the item's status changes to confirmed.

- [ ] FT-05: User can distinguish confirmed vs. pending items in the list
  - Action: View the policy list after confirming at least one item.
  - Expected: Confirmed items and pending items are clearly labeled with their respective statuses.

- [ ] FT-06: Personal center contains a Confirmation Progress Dashboard
  - Action: Open the personal center.
  - Expected: A "Confirmation Progress Dashboard" section is present and visible.

- [ ] FT-07: Dashboard shows confirmed/pending proportion in a doughnut chart
  - Action: View the Confirmation Progress Dashboard.
  - Expected: A doughnut chart is displayed showing the proportion of confirmed vs. pending items.

- [ ] FT-08: Dashboard categorizes confirmation status by policy type
  - Action: View the dashboard's status breakdown.
  - Expected: Confirmation status is grouped by the four policy types: Administration, Human Resources, Finance, and Compliance, each showing its own confirmed/pending status.

## Constraint
- [ ] CS-01: Login cannot proceed with empty credentials
  - Action: Submit the login form with empty username and/or password fields.
  - Expected: Login is blocked and an error message is displayed; user is not logged in.

- [ ] CS-02: Confirmation cannot be completed without the explicit acknowledgment
  - Action: On a policy detail page, attempt to submit the confirmation without checking/stating the "read and understood" acknowledgment.
  - Expected: The confirmation is rejected with a validation message; the item remains pending.

- [ ] CS-03: Already-confirmed items cannot be confirmed again
  - Action: Open a policy item that is already confirmed.
  - Expected: The confirmation control is unavailable/disabled (or the system rejects re-confirmation), and the item remains confirmed once.

- [ ] CS-04: Pending items carry a priority tag of High, Medium, or Low
  - Action: Inspect pending items in the policy list.
  - Expected: Every pending item shows exactly one priority tag: High, Medium, or Low.

- [ ] CS-05: Policies with a deadline within 3 days are automatically marked high-priority
  - Action: Inspect pending policies whose confirmation deadline is within 3 days.
  - Expected: Each such policy is automatically labeled with the High priority tag without manual action.

- [ ] CS-06: Deadline-driven high-priority policies are pinned to the top of the list
  - Action: View the policy list sorted as displayed by default.
  - Expected: All pending policies due within 3 days appear at the top of the list, above other items.

## Interaction
- [ ] IX-01: Confirmation action gives immediate feedback and updates status
  - Action: Complete the confirmation step on a policy detail page and return to the list.
  - Expected: A success indication (e.g., success message) is shown, and the item now displays as confirmed.

- [ ] IX-02: Dashboard updates after a new confirmation
  - Action: Note the doughnut chart values, confirm one more pending policy, then revisit the dashboard.
  - Expected: The doughnut chart and per-type status update to reflect the newly confirmed item.

- [ ] IX-03: Policy list items are selectable and open their detail view
  - Action: Hover over and click a policy row in the list.
  - Expected: The row shows a clickable/selected hover state and clicking navigates to that policy's detail page.

## Content
- [ ] CT-01: Policy detail page displays relevant and complete content
  - Action: Open any policy item from the list.
  - Expected: The detail page shows the correct title, policy type, deadline (if any), and the full policy text with no placeholder or unrelated content.

- [ ] CT-02: Dashboard labels and policy type names match the specified terminology
  - Action: View the dashboard and list labels.
  - Expected: Labels read "Confirmation Progress Dashboard" and use the exact type names Administration, Human Resources, Finance, Compliance, plus priority labels High/Medium/Low.